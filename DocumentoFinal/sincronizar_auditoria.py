"""Inserta en el documento los resultados verificables de la auditoría integral."""
import csv
import json
from pathlib import Path
import re
import shutil
import subprocess

D = Path(__file__).resolve().parent
ROOT = D.parent
TABLAS = ROOT / 'Final/reports/tables'
NOMBRES = {'DummyClassifier': 'Referencia mayoritaria', 'CategoricalNB': 'Naive Bayes categórico',
           'DecisionTreeClassifier': 'Árbol CART', 'RandomForestClassifier': 'Random Forest',
           'MLPClassifier': 'Red neuronal MLP'}


def leer(nombre):
    with (TABLAS / f'{nombre}.csv').open(encoding='utf-8', newline='') as archivo:
        return list(csv.DictReader(archivo))


def decimal(valor, digitos=4):
    return f'{float(valor):.{digitos}f}'


def p_tex(valor):
    p = float(valor)
    if p == 0:
        return r'$<10^{-15}$'
    if p >= .0001:
        return f'{p:.4f}'
    mantisa, exponente = f'{p:.2e}'.split('e')
    return rf'${mantisa}\times10^{{{int(exponente)}}}$'


def tabla(titulo, columnas, filas, anchos=None):
    anchos = anchos or [f'.{int(83 / len(columnas)):02d}'] * len(columnas)
    formato = ''.join(r'p{' + a + r'\textwidth}' for a in anchos)
    cabecera = ' & '.join(columnas) + r'\\\midrule'
    return '\n'.join([
        r'\begin{longtable}{' + formato + '}', r'\caption{' + titulo + r'}\\\toprule',
        cabecera + r'\endfirsthead', cabecera + r'\endhead',
        *[' & '.join(map(str, fila)) + r'\\' for fila in filas],
        r'\bottomrule\end{longtable}',
    ])


def periodo_git(ruta):
    historial = subprocess.check_output(
        ['git', 'log', '--diff-filter=A', '--format=%h %as', '--', ruta], cwd=ROOT, text=True,
    ).splitlines()
    if not historial:
        return '', ''
    revision, fecha = historial[-1].split()
    return fecha, revision


def plan():
    actividades = [
        ('Anteproyecto y revisión', '1--5 oct.', 'Proyecto/main.tex', 'Versión base conservada.'),
        ('Preparación y limpieza', '6--15 oct.', 'Final/src/02_limpieza.py', 'El maestro ya estaba curado.'),
        ('EDA y correlaciones', '15--29 oct.', 'Final/src/01_inspeccion.py', 'Esquema, rangos y cobertura documentados.'),
        ('Clustering', '29 oct.--10 nov.', 'Final/src/03_clustering.py', 'K-Means, Ward y DBSCAN.'),
        ('Clasificación', '5--11 nov.', 'Final/src/04_modelo.py', 'Evaluación anidada incorporada en revisión.'),
        ('Weka', 'Durante modelado', 'Final/reports/weka/kmeans.txt', 'Evidencia gráfica.'),
        ('Web', '8--16 nov.', 'Final/app.py', 'Ejecución local.'),
        ('Despliegue público', '16--18 nov.', '', 'Descartado por decisión de conservar los datos localmente.'),
        ('Evaluación en Orange', 'Durante modelado', '', 'Parcial. Cierres de Qt documentados.'),
        ('Documento y revisión', '10--24 nov.', 'DocumentoFinal/main.tex', 'Fuente versionada.'),
        ('Entrega y demo', '25 nov.', '', 'La fecha de exposición sigue siendo una fecha planificada.'),
    ]
    filas, datos = [], []
    for nombre, base, ruta, estado in actividades:
        fecha, revision = periodo_git(ruta) if ruta else ('', '')
        justificacion = '[PENDIENTE: confirmar equipo]' if ruta else estado
        datos.append(dict(actividad=nombre, baseline=base, evidencia_git=fecha, revision=revision,
                          ruta=ruta, estado=estado, justificacion_desviacion=justificacion))
        filas.append((nombre, base, f'{fecha} ({revision})' if fecha else 'Sin registro',
                      f'{estado} {justificacion}' if ruta else estado))
    with (TABLAS / 'plan_baseline_git.csv').open('w', newline='', encoding='utf-8') as archivo:
        salida = csv.DictWriter(archivo, fieldnames=list(datos[0]), lineterminator='\n')
        salida.writeheader()
        salida.writerows(datos)
    return tabla('Línea base y primera evidencia fechada en Git por producto.',
                 ['Actividad', 'Línea base', 'Fecha Git', 'Evidencia y justificación'], filas,
                 ['.19', '.15', '.18', '.36'])


def actualizar():
    archivo = D / 'main.tex'
    tex = archivo.read_text()
    if r'\subsection{Comparación estadística de los modelos}' in tex:
        return
    meta = json.loads((ROOT / 'Final/models/metadata.json').read_text())
    prueba = leer('metricas_prueba')[0]
    historica = next(r for r in leer('prueba_historica_modelos') if r['modelo'] == 'MLPClassifier')
    cv = leer('comparativo_modelos')
    estadistica = leer('comparacion_estadistica')
    rf, mlp = (next(r for r in cv if r['modelo'] == n) for n in ('RandomForestClassifier', 'MLPClassifier'))
    pruebas_rf_mlp = [r for r in estadistica if {r['modelo_a'], r['modelo_b']} ==
                      {'RandomForestClassifier', 'MLPClassifier'}]
    t, w, nemenyi = pruebas_rf_mlp
    friedman = next(r for r in estadistica if r['prueba'] == 'Friedman')
    muestra = meta['metricas']['reporte_clases']['medio']
    recuperados = meta['metricas']['matriz_confusion'][1][1]
    etiq = {**NOMBRES, 'Todos': 'Cinco modelos', '': '—'}
    valores = [('exactitud_pct', 'Exactitud (%)'), ('f1_macro', 'F1 macro'), ('f1_ponderado', 'F1 pond.'),
               ('kappa', 'Kappa'), ('roc_auc_ovr', 'AUC OvR')]
    filas = [(NOMBRES[r['modelo']], *(f"{decimal(r[k + '_media'], 2 if k == 'exactitud_pct' else 3)}"
             + r' $\pm$ ' + decimal(r[k + '_de'], 2 if k == 'exactitud_pct' else 3)
             for k, _ in valores)) for r in cv]
    tab_cv = tabla('Validación externa anidada. Media y desviación estándar de los pliegues.',
                   ['Modelo', *(v.replace('%', r'\%') for _, v in valores)], filas,
                   ['.20', '.13', '.126', '.126', '.126', '.126'])
    tab_p = tabla('Contrastes pareados de F1 macro del bosque y prueba global.',
                  ['Prueba', 'Comparación', 'p-valor'],
                  [(r['prueba'].replace('–', '--'), f"{etiq[r['modelo_a']]} / {etiq[r['modelo_b']]}",
                    p_tex(r['p_valor'])) for r in estadistica
                   if r['prueba'] != 'Nemenyi' or r is nemenyi], ['.25', '.44', '.16'])
    matriz = leer('matriz_confusion')
    matriz_tex = r'\\'.join('&'.join(r[c] for c in meta['clases']) for r in matriz)
    resumen = (f"Random Forest es el modelo activo. Obtuvo {decimal(prueba['exactitud_pct'], 2)}"
               rf"\,\% de exactitud y F1 macro de {decimal(prueba['f1_macro'])} "
               f"sobre {prueba['n']} juegos de prueba. ")
    tex = re.sub(r'La MLP activa en la web obtiene.*?en esa misma prueba\. ', lambda _: resumen, tex, count=1)
    tex = tex.replace('Adoptamos CRISP-DM como estructura de trabajo',
                      'Adoptamos CRISP-DM como estructura de trabajo. El método fue desarrollado por un consorcio de empresas, entre ellas Daimler-Benz, SPSS y NCR')
    tex = tex.replace('después se estandarizan las seis variables',
                      'después se aplica estandarización z-score a las seis variables')
    tex = tex.replace('Dos cortes en los terciles del índice de entrenamiento definen bajo, medio y alto, preservando empates.',
                      'Aplicamos una discretización no supervisada de igual frecuencia por terciles. Los cortes de entrenamiento definen bajo, medio y alto y preservan los empates.')
    cortes = meta['terciles_descriptivos_catalogo']
    tex = tex.replace(r'\subsection{Separación y prevención de fuga}',
        f"Para describir el catálogo elegible completo se calcularon aparte los cortes "
        f"{cortes['cortes'][0]:.6f} y {cortes['cortes'][1]:.6f} sobre {cortes['n']} juegos. "
        r'La evaluación estima su referencia en cada ajuste, de modo que los conteos de validación y prueba queden reservados.'
        '\n' + r'\subsection{Separación y prevención de fuga}')
    tex = tex.replace('La selección utiliza StratifiedGroupKFold de diez pliegues.',
        'La evaluación usa validación estratificada por grupos de título, con diez pliegues externos repetidos cinco veces y búsqueda interna de tres pliegues. Se usan las mismas particiones para los cinco modelos y semillas reproducibles a partir de 42.')
    tex = re.sub(r' El ajuste elegido usa 32 neuronas.*?\n\n\\begin\{longtable\}.*?(?=\\subsection\{Interpretación y revisión del entrenamiento\})',
        lambda _: '\n\n' + tab_cv + '\n' + r'\subsection{Comparación estadística de los modelos}' + '\n'
        + r'La t pareada se corrige por la razón entre los tamaños de validación y ajuste \parencite{nadeau2003}. Wilcoxon, Friedman y Nemenyi se presentan como contrastes complementarios \parencite{demsar2006}. Las particiones repetidas se solapan, por lo que los tres contrastes de rangos se interpretan como exploratorios.' + '\n'
        + tab_p + '\n'
        + f"Friedman dio p = {p_tex(friedman['p_valor'])}. Entre el bosque y la MLP, "
          f"la t corregida dio p = {p_tex(t['p_valor'])}, Wilcoxon p = {p_tex(w['p_valor'])} "
          f"y Nemenyi p = {p_tex(nemenyi['p_valor'])}. La MLP obtuvo F1 macro externo "
          f"{decimal(mlp['f1_macro_media'])} con DE {decimal(mlp['f1_macro_de'])}. El bosque obtuvo "
          f"{decimal(rf['f1_macro_media'])} con DE {decimal(rf['f1_macro_de'])}. "
          'La diferencia es inconclusa. El bosque permanece activo por decisión de proyecto, su menor dispersión observada y la posibilidad de inspeccionar importancias por variable.\n\n'
        + r'\subsection{Prueba reservada y fiabilidad}' + '\n' + resumen
        + f"El F1 ponderado fue {decimal(prueba['f1_ponderado'])}, kappa {decimal(prueba['kappa'])} "
          f"y ROC-AUC macro uno contra el resto {decimal(prueba['roc_auc_ovr'])}. "
          f"La MLP obtuvo en la corrida histórica F1 macro {decimal(historica['f1_macro_prueba'])} "
          f"y exactitud {100 * float(historica['exactitud_prueba']):.2f}" + r'\,\%. '
          'El código anterior escogió por CV y después calculó las métricas de prueba de todos los candidatos. '
          'La decisión actual se tomó con esos resultados ya conocidos. Por ello, la partición sirve para comprobar la consistencia del artefacto y falta una muestra independiente para evaluar esa decisión.\n\n'
        + r'La matriz del bosque tiene filas reales y columnas predichas en orden bajo, medio y alto.' + '\n'
        + r'\begin{equation}\begin{pmatrix}' + matriz_tex + r'\end{pmatrix}.\end{equation}' + '\n'
        + f"La clase media recupera {recuperados} de {int(muestra['support'])} juegos, "
          f"{100 * muestra['recall']:.2f}" + r'\,\%. '
        + f"El Brier multiclase, como suma de errores cuadrados por clase, fue {decimal(prueba['brier_multiclase'])}. "
          f"La pérdida logarítmica fue {decimal(prueba['log_loss'])}. "
          'La web permite explorar la fracción observada por intervalos de probabilidad y ver cuántos juegos aporta cada intervalo.\n'
        + r'\begin{figure}[htbp]\centering\includegraphics[width=.75\linewidth]{figuras/fiabilidad_rf.png}'
          r'\caption{Curva de fiabilidad uno contra el resto en la partición de prueba.}\end{figure}\FloatBarrier' + '\n',
        tex, count=1, flags=re.S)
    tex = tex.replace('la brecha se calcula', 'el atributo sintético de brecha se calcula')
    if 'atributo sintético' not in tex:
        tex = tex.replace(r'\section{Clustering y perfiles del catálogo}',
            'La brecha usuarios--crítica es un atributo sintético calculado a partir de las dos notas en una escala común.\n\n'
            + r'\section{Clustering y perfiles del catálogo}', 1)
    tex = tex.replace('el bosque incluido en la comparación', 'el modelo activo de la web')
    tex = tex.replace('La MLP se revisa con su matriz, casos de prueba y escenarios.',
                      'El bosque se revisa con su matriz, casos de prueba y escenarios.')
    tex = tex.replace('Importancia de Gini del bosque comparado en la página Modelo.',
                      'Importancia de Gini del bosque en la página Modelo.')
    tex = re.sub(r'RandomForest fue el mejor de las cuatro corridas,.*?(?=En SimpleKMeans)',
        lambda _: 'RandomForest alcanzó la mayor exactitud de las corridas gráficas de clasificación. '
        + resumen + 'Weka evalúa mediante CV sobre los atributos exportados. Python ajusta el preprocesamiento y los cortes dentro de cada pliegue, agrupa por título y usa CV anidada. J48 corresponde a C4.5 y el árbol de Python a CART. Los estimadores numéricos de Weka NaiveBayes difieren de la discretización de CategoricalNB.\n\n',
        tex, count=1, flags=re.S)
    tex = tex.replace('La corrida MLP se realizó en Python.',
        'El único reintento sin interfaz abortó porque la compilación de Qt requería NEON. Las métricas de Orange quedaron sin valores. La corrida de MLP se realizó en Python.')
    tex = tex.replace('El selector de agrupamiento ofrece K-Means y Ward.',
                      'El selector de agrupamiento ofrece K-Means, Ward y DBSCAN.')
    tex = re.sub(r'\\begin\{figure\}[^\n]*\{figuras/comparacion_mlp\.png\}\n.*?\\FloatBarrier\n',
                 '', tex, count=1, flags=re.S)
    tex = re.sub(r'\\begin\{figure\}[^\n]*\{figuras/prediccion_mlp_web\.png\}[^\n]*\n',
        r'La auditoría reprodujo una predicción del formulario con Random Forest y la contrastó con el Pipeline guardado.\n',
        tex, count=1)
    escenarios = {r['id']: r for r in leer('escenarios_prediccion')}
    tex = re.sub(r'La tabla muestra cómo responde la MLP.*?carecen de calibración\.',
        lambda _: f"Al ingresar las dos notas altas de S2, el bosque estima la clase {escenarios['S2']['prediccion']}. "
        f"Al ocultar Metacritic en S5, estima la clase {escenarios['S5']['prediccion']}. "
        'Las probabilidades se obtienen del Pipeline guardado y carecen de calibración.', tex, count=1)
    tex = tex.replace('probar el formulario con la MLP', 'probar el formulario con Random Forest')
    tex = tex.replace('alternar K-Means y Ward', 'alternar K-Means, Ward y DBSCAN')
    tex = tex.replace('La MLP ganó por el criterio de CV fijado y Random Forest logró el mayor F1 en la prueba reservada.',
                      'La MLP obtuvo el mayor F1 macro medio en la validación anidada. La diferencia frente a Random Forest no fue concluyente y se mantuvo el bosque activo.')
    tex = tex.replace('la CV no anidada y la ausencia de validación externa limitan cualquier comparación predictiva más fuerte.',
                      'la evaluación repetida comparte juegos entre particiones y falta una muestra externa para medir generalización prospectiva.')
    tex = re.sub(r'(?<=\\label\{sec:plan\})\n.*?(?=\\section\{Evaluación de los objetivos y discusión\})',
        lambda _: '\nEl equipo declara que las actividades técnicas realizadas cumplieron el calendario previsto. '
        'Las fechas de Git registran la primera evidencia disponible por producto y pueden corresponder a una entrega agrupada posterior. '
        'La fecha exacta de terminación de cada actividad requiere respaldo adicional.\n'
        + plan() + '\n', tex, count=1, flags=re.S)
    etica = r"""\subsection{Ética y alcance de uso}
La unidad del análisis es el juego. Las señales representan interacciones agregadas de Backloggd y no permiten reconstruir trayectorias individuales. La presencia de reseñas de prensa y la visibilidad del catálogo pueden estar relacionadas con la popularidad histórica. El clasificador puede favorecer géneros con mayor presencia en la muestra y desfavorecer propuestas de nicho. Usamos la predicción como estimación orientativa. Los datos carecen de ventas observadas y no permiten evaluar rentabilidad ni riesgo de juegos como servicio.
"""
    tex = tex.replace(r'\section{Conclusiones}', etica + r'\section{Conclusiones}', 1)
    bics = leer('bic_gmm')
    mejor_bic = min(bics, key=lambda r: float(r['bic']))
    shutil.copyfile(ROOT / 'Final/reports/figures/pca_tres_metodos.png', D / 'figuras/pca_tres_metodos.png')
    bloque_pca = (f"La mezcla gaussiana obtuvo el menor BIC con {mejor_bic['k']} componentes "
                  f"({decimal(mejor_bic['bic'], 2)}). Este criterio describe el ajuste probabilístico de la mezcla. "
                  'Se conservan los cortes de K-Means y Ward elegidos por silueta. '
                  'DBSCAN queda como descripción de densidad y casos atípicos.\n'
                  r'\begin{figure}[htbp]\centering\includegraphics[width=\linewidth]{figuras/pca_tres_metodos.png}'
                  r'\caption{Proyección exploratoria de las mismas dos componentes principales para los tres métodos.}'
                  r'\end{figure}\FloatBarrier' + '\n')
    tex = tex.replace(r'\section{Clasificación supervisada}', bloque_pca + r'\section{Clasificación supervisada}', 1)
    archivo.write_text(tex)


if __name__ == '__main__':
    actualizar()
