"""Actualiza las cifras y compone el informe con la plantilla del anteproyecto."""
import csv
import json
from pathlib import Path
import shutil
import unicodedata

DOCUMENTO = Path(__file__).resolve().parent
RAIZ = DOCUMENTO.parent
REPORTES = RAIZ / 'Final/reports'
TABLAS = REPORTES / 'tables'
MODELOS = {
    'DummyClassifier': 'Referencia mayoritaria',
    'CategoricalNB': 'Naive Bayes categórico',
    'DecisionTreeClassifier': 'Árbol de decisión',
    'RandomForestClassifier': 'Random Forest',
    'MLPClassifier': 'Red neuronal',
}


def leer(nombre):
    with (TABLAS / f'{nombre}.csv').open(encoding='utf-8', newline='') as archivo:
        return list(csv.DictReader(archivo))


def escapar(valor):
    especiales = {'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#', '$': r'\$',
                  '{': r'\{', '}': r'\}', '–': '--', '—': '---'}
    return ''.join(especiales.get(c, c) for c in str(valor))


def sin_acentos(texto):
    """Quita los acentos y conserva la ñ y la diéresis."""
    descompuesto = unicodedata.normalize('NFD', texto)
    return unicodedata.normalize('NFC', ''.join(
        c for c in descompuesto if c not in '\u0300\u0301\u0302\u030c'
    ))


def tabla(titulo, columnas, alineacion, filas):
    encabezado = ' & '.join(map(escapar, columnas)) + r'\\'
    return '\n'.join([
        r'\begin{table}[!htbp]', r'\centering\small', r'\caption{' + titulo + '}',
        r'\begin{tabular}{' + alineacion + '}', r'\toprule', encabezado, r'\midrule',
        *(' & '.join(map(escapar, fila)) + r'\\' for fila in filas),
        r'\bottomrule', r'\end{tabular}', r'\end{table}', r'\FloatBarrier',
    ])


def cifras():
    correlacion = leer('correlacion_catalogo')[0]
    procedencia = {fila['etapa']: fila for fila in leer('procedencia_datos')}
    h = procedencia['Antecedente enriquecido']
    d = procedencia['Maestro curado']
    p = leer('metricas_prueba')[0]
    metadata = json.loads((RAIZ / 'Final/models/metadata.json').read_text(encoding='utf-8'))
    calibracion = metadata['calibracion_web']
    m = leer('matriz_confusion')
    db = next(f for f in leer('metricas_clusters') if f['metodo'] == 'DBSCAN' and float(f['factor_eps']) == 1)
    test = next(f for f in leer('comparacion_estadistica')
                if f['prueba'].startswith('t corregida') and f['modelo_b'] == 'MLPClassifier')
    casos_comerciales = leer('evidencia_comercial')
    escenarios = {f['id']: f for f in leer('escenarios_prediccion')}
    casos = leer('contraejemplos_prediccion')
    errores = [f for f in casos if f['acierto'].lower() == 'false']
    generos = {'Adventure': 'Aventura', 'RPG': 'Rol', 'Shooter': 'Disparos', 'Platform': 'Plataformas'}
    asociaciones = []
    for nombre, cantidad in [('correlacion_generos', 4), ('correlacion_organizaciones', 3)]:
        grupos = [f for f in leer(nombre) if f['estado'] == 'incluido']
        for f in sorted(grupos, key=lambda f: int(f['n']), reverse=True)[:cantidad]:
            asociaciones.append((generos.get(f['grupo'], f['grupo']), f['n'],
                                  f"{float(f['pearson_r']):.3f}", f"{float(f['spearman_rho']):.3f}",
                                  f"{float(f['brecha_absoluta_media']):.2f}"))
    return {
        'Historico': f"{int(h['filas']):,}", 'Catalogo': f"{int(d['filas']):,}",
        'Descartes': int(h['filas']) - int(d['filas']), 'Elegibles': f"{int(correlacion['n_juegos']):,}",
        'Pares': correlacion['n'], 'PearsonGlobal': f"{float(correlacion['pearson_r']):.4f}",
        'SpearmanGlobal': f"{float(correlacion['spearman_rho']):.4f}",
        'JuegosPrueba': p['n'], 'ExactitudPrueba': f"{float(p['exactitud_pct']):.2f}" + r'\,\%',
        'FPrueba': f"{float(p['f1_macro']):.4f}", 'GruposDbscan': db['k'], 'RuidoDbscan': db['ruido'],
        'PComparacion': f"$p={float(test['p_valor']):.4f}$",
        'JuegosCalibracion': calibracion['n_ajuste'],
        'MetricasCalibracion': tabla('Calidad de las probabilidades en los juegos de prueba.',
            ['Medida', 'Antes del ajuste', 'Despues del ajuste'], 'lrr',
            [(nombre, f"{metadata['metricas'][clave]:.4f}", f"{calibracion['metricas_prueba'][clave]:.4f}")
             for nombre, clave in [('Brier multiclase', 'brier_multiclase'), ('Log-loss', 'log_loss')]]),
        'AsociacionGrupos': tabla('Relación y separación de notas en grupos con más pares.',
            ['Grupo', 'Pares', 'Pearson', 'Spearman', 'Brecha media absoluta'], 'lrrrr', asociaciones),
        'SilTitulo': tabla('Comparación de los cortes seleccionados.',
            ['Método', 'Grupos', 'Silueta', 'Calinski--Harabasz', 'Davies--Bouldin'], 'lrrrr',
            [(f['metodo'], f['k'], f"{float(f['silhouette']):.3f}",
              f"{float(f['calinski_harabasz']):.1f}", f"{float(f['davies_bouldin']):.3f}")
             for f in leer('clase_comparacion_clustering')]),
        'EscenariosNotas': tabla('Ejemplo con los mismos géneros, organización y década.',
            ['Prueba', 'Usuarios', 'Prensa', 'Nivel estimado'], 'lrrl',
            [(nombre, f['rating'], f['metacritic'] or 'Ausente', f['prediccion'].capitalize())
             for nombre, f in [('Con ambas notas', escenarios['S2']), ('Sin nota de prensa', escenarios['S5'])]]),
        'EjemplosError': tabla('Juegos de prueba en los que el modelo asignó otro nivel.',
            ['Juego', 'Nivel real', 'Nivel asignado'], r'p{.52\linewidth}ll',
            [(f['titulo'], f['real'].capitalize(), f['prediccion'].capitalize()) for f in errores]),
        'PlanTrabajo': tabla('Actividades planeadas y primera evidencia fechada de su realización.',
            ['Actividad', 'Periodo planeado', 'Evidencia fechada'], 'lll',
            [(f['actividad'], f['baseline'].replace('--', '–'), f['evidencia_git'])
             for f in leer('plan_baseline_git') if f['evidencia_git'] and f['actividad'] != 'Web']),
        'TotalMedio': sum(int(m[1][c]) for c in ('bajo', 'medio', 'alto')), 'AciertosMedio': m[1]['medio'],
        'ComparacionModelos': tabla('Resultados promedio de la comparación en Python.',
            ['Modelo', 'Exactitud (%)', 'F1 macro', 'Variación del F1'], 'lrrr',
            [(MODELOS[f['modelo']], f"{float(f['exactitud_pct_media']):.2f}", f"{float(f['f1_macro_media']):.4f}",
              f"{float(f['f1_macro_de']):.4f}") for f in leer('comparativo_modelos')]),
        'MatrizConfusion': tabla('Juegos por nivel real y nivel asignado en la prueba.',
            ['Nivel real', 'Asignado bajo', 'Asignado medio', 'Asignado alto'], 'lrrr',
            [(f['real'].capitalize(), f['bajo'], f['medio'], f['alto']) for f in m]),
        'ResultadosWeka': tabla('Resultados de clasificación en Weka.',
            ['Modelo', 'Exactitud (%)', 'F1 macro', 'F1 ponderado'], 'lrrr',
            [(f['modelo'], f"{float(f['exactitud_pct']):.2f}", f"{float(f['f1_macro']):.3f}",
              f"{float(f['f1_ponderado']):.3f}") for f in leer('comparativo_herramientas')
             if f['herramienta'].startswith('Weka') and f['exactitud_pct']]),
        'Perfiles': tabla('Promedios de los grupos de K-Means.',
            ['Grupo', 'Juegos', 'Partidas registradas', 'Juegos pendientes', 'Nota de usuarios'], 'lrrrr',
            [(f['cluster'], f['n'], f"{float(f['media_Plays']):,.0f}", f"{float(f['media_Backlogs']):,.0f}",
              f"{float(f['media_Rating']):.2f}") for f in leer('perfiles_clusters') if f['metodo'] == 'K-Means']),
        'ProcedenciaDatos': tabla('Tamaño del catálogo en cada etapa.', ['Etapa', 'Registros', 'Columnas'], 'lrr',
            [(nombre, f['filas'], f['columnas']) for nombre, f in
             [('Anteproyecto (tamaño declarado)', procedencia['Anteproyecto']), ('Versión con notas de prensa', h),
              ('Catálogo con el que trabajamos', d), ('Datos después de limpiar', procedencia['Depurado actual'])]]),
        'CasosComerciales': '\n\n'.join(
            r'\noindent\textbf{' + escapar(f['juego']) + '.} ' + escapar(f['evidencia'])
            for f in casos_comerciales),
        'FuentesComerciales': ','.join(f[campo] for f in casos_comerciales
                                     for campo in ('cita', 'cita_contexto') if f[campo]),
    }


def main():
    plantilla = (RAIZ / 'Proyecto/main.tex').read_text(encoding='utf-8')
    preambulo = plantilla.split(r'\begin{document}', 1)[0]
    preambulo += r'''
\usepackage{xurl}
\usepackage{caption}
\captionsetup[table]{skip=8pt}
\addto\captionsspanish{\renewcommand{\contentsname}{Indice}}
\setcounter{tocdepth}{1}
\newcommand{\captura}[3]{%
  \begin{figure}[!htbp]
  \centering
  \includegraphics[width=\linewidth,height=.40\textheight,keepaspectratio]{figuras/#1}
  \caption{#2}\label{#3}
  \end{figure}\FloatBarrier
}
'''
    portada = r'''\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}\input{Portada.tex}\end{titlepage}
\newpage
{\makeatletter\let\ps@plain\ps@indice\makeatother
\pagestyle{indice}\thispagestyle{indice}\hypersetup{linkcolor=black}\tableofcontents\thispagestyle{indice}}
\newpage\setcounter{page}{1}\hypersetup{pageanchor=true}\singlespacing
'''
    datos = '\n'.join(rf'\newcommand{{\{clave}}}{{{valor}}}' for clave, valor in cifras().items())
    (DOCUMENTO / 'cifras_informe.tex').write_text(sin_acentos(datos) + '\n', encoding='utf-8')
    cuerpo = r'\input{cifras_informe.tex}' + '\n' + (DOCUMENTO / 'informe.tex').read_text(encoding='utf-8')
    (DOCUMENTO / 'main.tex').write_text(preambulo + portada + sin_acentos(cuerpo), encoding='utf-8')
    shutil.copyfile(TABLAS / 'evidencia_comercial.csv', DOCUMENTO / 'tablas/evidencia_comercial.csv')


if __name__ == '__main__':
    main()
