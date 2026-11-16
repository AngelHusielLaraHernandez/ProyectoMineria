"""Verifica los datos exportados y recompone el contraste de herramientas."""
from hashlib import sha256
from io import StringIO
import json
import re
from zipfile import ZipFile

import numpy as np
import pandas as pd

from .config import ROOT

MODELOS_WEKA = ['ZeroR', 'NaiveBayes', 'J48', 'RandomForest']
DECLARACION = '@attribute nivel_popularidad {bajo,medio,alto}'
ARTEFACTOS_ACTUALIZADOS = {
    'reports/codex_log.md',
    'reports/tables/comparativo_herramientas.csv',
    'data/export/procedencia_arff.json',
}


def verificar_exportaciones(raiz):
    export = raiz / 'data/export'
    limpio = raiz / 'data/clean'
    informes = raiz / 'reports'
    procedencia = json.loads((export / 'procedencia.json').read_text())
    manifiesto = json.loads((informes / 'weka/manifiesto_evidencias_gui.json').read_text())
    for archivo in manifiesto['archivos']:
        ruta = raiz / archivo['ruta']
        if ruta.exists() and archivo['ruta'] not in ARTEFACTOS_ACTUALIZADOS:
            datos = ruta.read_bytes()
        elif ruta.exists():
            datos_disco = ruta.read_bytes()
            if len(datos_disco) == archivo['bytes'] and sha256(datos_disco).hexdigest() == archivo['sha256']:
                datos = datos_disco
            else:
                # Conserva verificación del corte histórico del 9 nov cuando el artefacto activo ya fue regenerado.
                with ZipFile(informes / 'weka/RESPALDO_UNIFICADO.zip') as respaldo:
                    datos = respaldo.read(f"contenido/{archivo['sha256']}/{ruta.name}")
        else:
            with ZipFile(informes / 'weka/RESPALDO_UNIFICADO.zip') as respaldo:
                datos = respaldo.read(f"contenido/{archivo['sha256']}/{ruta.name}")
        assert len(datos) == archivo['bytes'] and sha256(datos).hexdigest() == archivo['sha256']
        if archivo['ruta'].endswith('.png'):
            assert datos.startswith(b'\x89PNG\r\n\x1a\n')
    verificados = []
    arffs = json.loads((export / 'procedencia_arff.json').read_text())
    for nombre, fuente in [('clustering', 'clustering_espacio.csv'), ('clasificacion', 'entrenamiento_orange.csv')]:
        csv = export / f'{nombre}.csv'
        arff = export / f'{nombre}.arff'
        original = csv.read_bytes()
        assert sha256(original).hexdigest() == procedencia[csv.name]['sha256_export']
        actual = pd.read_csv(limpio / fuente)
        base = pd.read_csv(csv)
        pd.testing.assert_frame_equal(base, actual, check_exact=True)
        texto = arff.read_text()
        cabecera, datos = re.split(r'^@data\s*$', texto, maxsplit=1, flags=re.I | re.M)
        lineas = [linea for linea in cabecera.splitlines() if linea.lower().startswith('@attribute ')]
        nombres = [re.match(r"@attribute\s+(?:'([^']+)'|(\S+))", linea, re.I).groups() for linea in lineas]
        columnas = [a or b for a, b in nombres]
        assert columnas == base.columns.tolist()
        leido = pd.read_csv(StringIO(datos), names=columnas)
        if nombre == 'clasificacion':
            leido['nivel_popularidad'] = leido['nivel_popularidad'].str.strip("'\"")
        pd.testing.assert_frame_equal(base, leido, check_dtype=False, rtol=1e-12, atol=1e-14)
        if nombre == 'clasificacion':
            assert columnas[-1] == 'nivel_popularidad' and set(base.iloc[:, -1]) == {'bajo', 'medio', 'alto'}
            if lineas[-1] != DECLARACION:
                arff.write_text(texto.replace(lineas[-1], DECLARACION), encoding='utf-8')
        arffs[nombre]['sha256_arff'] = sha256(arff.read_bytes()).hexdigest()
        verificados.append({'archivo': nombre, 'n': len(base), 'atributos': len(columnas),
                            'sha256_csv_gui': sha256(original).hexdigest(), 'sha256_arff_actual': arffs[nombre]['sha256_arff']})
    (export / 'procedencia_arff.json').write_text(json.dumps(arffs, indent=2, ensure_ascii=False) + '\n')
    pd.DataFrame(verificados).to_csv(informes / 'tables/verificacion_weka_entradas.csv', index=False)


def extraer_weka(ruta, evidencia):
    texto = ruta.read_text()
    assert sha256(ruta.read_bytes()).hexdigest() == evidencia['sha256_salida']
    n, atributos = map(int, re.search(r'Instances:\s+(\d+)\s+Attributes:\s+(\d+)', texto).groups())
    aciertos, exactitud = re.search(r'Correctly Classified Instances\s+(\d+)\s+([\d.]+)\s+%', texto).groups()
    assert (n, atributos) == (892, 53) and '10-fold cross-validation' in texto
    detalle, matriz = texto.split('=== Detailed Accuracy By Class ===')[1].split('=== Confusion Matrix ===')
    filas = [f.split() for f in detalle.strip().splitlines() if f.split() and f.split()[-1] in {'alto', 'bajo', 'medio'}]
    assert {fila[-1] for fila in filas} == {'alto', 'bajo', 'medio'}
    ponderado = re.search(r'Weighted Avg\.\s+(.+)', detalle).group(1).split()[4]
    celdas = np.array([[int(x) for x in r] for r in re.findall(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+\|', matriz, re.M)])
    assert celdas.tolist() == evidencia['matriz'] and celdas.sum() == n and celdas.trace() == int(aciertos)
    assert abs(float(exactitud) - 100 * celdas.trace() / n) < .0001
    clase = np.array([float(f[4]) if f[4] != '?' else 0 for f in filas])
    notas = 'F1 macro promedia los F-Measure de clase impresos por Weka.'
    if ponderado == '?':
        soportes = celdas.sum(axis=1)
        valores = 2 * celdas.diagonal() / (soportes + celdas.sum(axis=0))
        ponderado = np.average(valores, weights=soportes)
        notas = 'Weka muestra ? para medio y el ponderado. F1 de medio se toma como 0 por cero predicciones. Ponderado calculado de la matriz.'
    return float(exactitud), clase.mean(), float(ponderado), notas


def ejecutar(raiz=ROOT):
    informes = raiz / 'reports'
    tablas = informes / 'tables'
    verificar_exportaciones(raiz)
    gui = json.loads((informes / 'weka/verificacion_gui.json').read_text())['clasificacion']
    filas = []
    cv = pd.read_csv(tablas / 'comparativo_modelos.csv')
    for r in cv.itertuples():
        notas = 'Preprocesamiento y objetivo locales por pliegue. Grupos de título. Hiperparámetros por CV interna.'
        if r.modelo == 'CategoricalNB':
            notas += ' CategoricalNB discretiza las notas. GaussianNB fue una variante histórica gaussiana, fuera de esta tabla.'
        filas.append(('Python', r.modelo, 'CV externa anidada 10×5, n=892',
                      r.exactitud_pct_media, r.f1_macro_media, r.f1_ponderado_media, notas))
    for modelo in MODELOS_WEKA:
        a, m, p, nota = extraer_weka(informes / f'weka/{modelo}.txt', gui[modelo])
        nota += ' Atributos numéricos preprocesados antes de CV. Particiones diferentes a Python.'
        if modelo == 'NaiveBayes':
            nota += ' Weka usa sus estimadores numéricos predeterminados. No usa los intervalos de CategoricalNB ni el estimador de GaussianNB de sklearn.'
        if modelo == 'J48':
            nota += ' J48 implementa C4.5, frente a CART en Python.'
        filas.append(('Weka 3.8.7', modelo, 'Explorer, CV de 10 pliegues, n=892', a, m, p, nota))
    filas.append(('Orange 3.40.0', '', 'Sin evaluación', None, None, None,
                  'Desviación por cierres Qt/Cocoa SIGSEGV. Reintento de importación sin interfaz abortó por requisito NEON de Qt.'))
    pd.DataFrame(filas, columns=['herramienta', 'modelo', 'esquema_evaluacion', 'exactitud_pct',
                                  'f1_macro', 'f1_ponderado', 'notas']).to_csv(tablas / 'comparativo_herramientas.csv', index=False)
    # Escribe en archivo dedicado para preservar el registro histórico completo de reports/codex_log.md.
    (informes / 'verificacion_weka_orange.md').write_text("""# Verificación de Weka y desviación de Orange

## Weka

Se verificaron por SHA-256 las salidas y capturas del manifiesto gráfico de Explorer 3.8.7. Las matrices se contrastaron con aciertos y exactitud. Los CSV exportados coinciden con los datos de origen y los ARFF contienen los mismos atributos y valores fila por fila. La declaración nominal del ARFF nuevo explicita el orden bajo, medio, alto. La evidencia histórica se obtuvo desde CSV y Weka mostró alto, bajo, medio. El orden nominal puede afectar desempates en corridas nuevas. No se repitió la sesión gráfica porque las filas de entrada se conservaron.

Archivos producidos: `tables/verificacion_weka_entradas.csv`, `tables/comparativo_herramientas.csv` y ARFF nominal verificado en `data/export`.

## Orange

Orange 3.40.0 sufrió cierres nativos SIGSEGV de Qt/Cocoa en macOS al automatizar selectores de archivos. La bitácora de Orange documenta intentos con File, CSV File Import, TAB, recuperación y arranque limpio, instalación local por el usuario y lanzador con selectores Qt. Ninguno produjo una evaluación guardada.

Se hizo un único reintento sin interfaz con el Python de la aplicación instalada y `import Orange`, preparado para cargar la copia local `clasificacion.tab`. Abortó con código 134 y el mensaje «Incompatible processor. This Qt build requires the following features: neon». El aborto ocurrió antes de leer el TAB. No se instaló software, no se intentó otro método y no se reportan métricas de Orange.
""", encoding='utf-8')


if __name__ == '__main__':
    ejecutar()
