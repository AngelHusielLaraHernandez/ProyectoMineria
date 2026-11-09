"""Comparación real de K-Means en Weka y sklearn sobre el mismo espacio canónico."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.request

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

RAIZ = Path(__file__).resolve().parents[1]
URLS = {
    'weka-stable-3.8.6.jar': 'https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/weka-stable/3.8.6/weka-stable-3.8.6.jar',
    'bounce-0.18.jar': 'https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/thirdparty/bounce/0.18/bounce-0.18.jar',
}
HUELLAS_JAR = {'weka-stable-3.8.6.jar': '932ea2f342b58fe45736389e9c426d5b5955e610d1f5f6485117f532068915e9',
               'bounce-0.18.jar': 'bffff1505335c02256b7ab2ccffbe4aa4d3ac9fe14c17557809b7c9d99d666ca'}


def ejecutar(raiz=RAIZ, descargar=False):
    raiz = Path(raiz)
    cache = raiz / '.cache/weka'
    cache.mkdir(parents=True, exist_ok=True)
    for nombre, url in URLS.items():
        destino = cache / nombre
        if not destino.exists():
            if not descargar:
                raise FileNotFoundError('Falta Weka/Bounce en .cache/weka; ejecutar este script con --descargar para obtenerlos de Maven Central.')
            urllib.request.urlretrieve(url, destino)
        if hashlib.sha256(destino.read_bytes()).hexdigest() != HUELLAS_JAR[nombre]:
            raise ValueError(f'El JAR {nombre} no coincide con la versión validada; revisar la descarga.')
    df = pd.read_csv(raiz / 'data/clean/clustering_espacio.csv')
    orden = pd.read_csv(raiz / 'data/clean/clustering_orden.csv')
    datos = df.to_numpy()
    if len(df) != len(orden) or df.shape[1] != 6 or not np.isfinite(datos).all():
        raise ValueError('Espacio de comparación inválido o IDs no alineados.')
    arff = raiz / 'data/clean/clustering_weka.arff'
    lineas = ['@RELATION clustering_canonico'] + [f'@ATTRIBUTE variable_{i} NUMERIC' for i in range(6)] + ['@DATA']
    lineas += [','.join(format(float(v), '.17g') for v in row) for row in datos]
    arff.write_text('\n'.join(lineas), encoding='utf-8')
    destino = raiz / 'reports/weka'
    destino.mkdir(parents=True, exist_ok=True)
    resultados, comandos = [], []
    for k in [2, 3, 4]:
        comando = ['java', '-Dweka.packageManager.offline=true', '-DWEKA_HOME=.cache/weka/home',
                   '-cp', '.cache/weka/*', 'weka.clusterers.SimpleKMeans', '-t', 'data/clean/clustering_weka.arff',
                   '-N', str(k), '-S', '42', '-I', '300', '-init', '1',
                   '-A', 'weka.core.EuclideanDistance -D', '-p', '0']
        ejecucion = subprocess.run(comando, cwd=raiz, text=True, capture_output=True, timeout=120)
        (destino / f'k{k}_stdout.txt').write_text(ejecucion.stdout)
        (destino / f'k{k}_stderr.txt').write_text(ejecucion.stderr)
        if ejecucion.returncode != 0:
            raise RuntimeError(f'Weka terminó con error; revisar reports/weka/k{k}_stderr.txt.')
        filas = [tuple(map(int, m.groups())) for linea in ejecucion.stdout.splitlines()
                 if (m := re.fullmatch(r'\s*(\d+)\s+(\d+)\s*', linea))]
        if [f[0] for f in filas] != list(range(len(df))):
            raise ValueError('Weka no devolvió una asignación por fila, en el orden esperado.')
        weka = np.array([f[1] for f in filas])
        python = KMeans(n_clusters=k, n_init=30, max_iter=300, random_state=42).fit_predict(datos)
        predicciones = orden.copy()
        predicciones['cluster_weka'] = weka
        predicciones['cluster_python'] = python
        predicciones.to_csv(destino / f'k{k}_asignaciones.csv', index=False)
        for herramienta, etiquetas in [('Weka 3.8.6', weka), ('sklearn', python)]:
            inercia = sum(float(np.square(datos[etiquetas == c] - datos[etiquetas == c].mean(axis=0)).sum()) for c in np.unique(etiquetas))
            resultados.append({'k': k, 'herramienta': herramienta, 'n': len(df),
                               'silhouette': silhouette_score(datos, etiquetas), 'inercia_comun': inercia,
                               'ARI_weka_python': adjusted_rand_score(weka, python),
                               'tamanos': json.dumps(pd.Series(etiquetas).value_counts().sort_index().to_dict())})
        comandos.append(comando)
    comparacion = pd.DataFrame(resultados)
    comparacion.to_csv(destino / 'comparacion.csv', index=False)
    manifest = {'java': subprocess.run(['java', '-version'], capture_output=True, text=True).stderr.strip(),
                'sha256_dataset_depurado': hashlib.sha256((raiz / 'data/clean/dataset_depurado.csv').read_bytes()).hexdigest(),
                'comandos': comandos, 'sha256_arff': hashlib.sha256(arff.read_bytes()).hexdigest(),
                'jars': {n: {'url': u, 'sha256': hashlib.sha256((cache / n).read_bytes()).hexdigest()} for n, u in URLS.items()}}
    (destino / 'ejecucion.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    columnas = comparacion.columns
    tabla = '| ' + ' | '.join(columnas) + ' |\n| ' + ' | '.join(['---']*len(columnas)) + ' |\n'
    tabla += '\n'.join('| ' + ' | '.join(str(v) for v in row) + ' |' for row in comparacion.itertuples(index=False, name=None))
    (raiz / 'reports/comparacion_weka.md').write_text(f'''# Comparación ejecutada con Weka

Ejecución local real por CLI: Weka 3.8.6 y Java, sin enviar datos a servicios externos. Las salidas originales, comandos, versiones, hashes y asignaciones por id_juego están en reports/weka. No se simula una ejecución de Orange ni una captura de su interfaz.

Ambas herramientas reciben los mismos {len(df)} casos y seis columnas ya transformadas. Weka usa EuclideanDistance -D para desactivar su normalización adicional; no recibe Title ni etiquetas ni género. Python usa 30 inicializaciones, Weka una, con k-means++ y semilla 42; los generadores y criterios de parada pueden diferir.

Silhouette e inercia se recalculan para ambas asignaciones con la misma implementación sobre el mismo espacio. ARI compara particiones sin depender del número asignado a cada cluster; no se presentan números de cluster como correspondencias automáticas.

{tabla}

Para reproducir con Java instalado: python src/comparar_weka.py --descargar. La descarga obtiene JAR de Maven Central; luego la ejecución es local. Sin --descargar requiere los JAR ya presentes en .cache/weka, excluido de Git.

Fuentes: [artefacto de Weka en Maven Central](https://central.sonatype.com/artifact/nz.ac.waikato.cms.weka/weka-stable/3.8.6) y ayuda de SimpleKMeans conservada junto a la ejecución. La comparación de Fase 4A no sustituye una comparación supervisada futura.

## Que debo verificar manualmente

- Diferencias de inicialización y convergencia antes de atribuir una mejora a la herramienta.
- Que la rúbrica admita evidencia por CLI; no se realizó una demo gráfica de Weka/Orange.
''', encoding='utf-8')
    ayuda = subprocess.run(['java', '-cp', '.cache/weka/*', 'weka.clusterers.SimpleKMeans', '-h'], cwd=raiz, capture_output=True, text=True)
    (destino / 'ayuda_simplekmeans.txt').write_text(ayuda.stdout + ayuda.stderr)
    return comparacion


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raiz', type=Path, default=RAIZ)
    parser.add_argument('--descargar', action='store_true', help='Descargar JAR faltantes de Maven Central, sin subir datos.')
    args = parser.parse_args()
    ejecutar(args.raiz, args.descargar)
