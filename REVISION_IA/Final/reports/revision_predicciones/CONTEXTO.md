# Carpeta: Final/reports/revision_predicciones

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/revision_predicciones/BITACORA_UNIFICADA.md` · Bytes: 2871 · SHA-256: `a1fa73e8a1c2763b593643a2bcce16a7a79a139ecfcca92c7626b5ae82022d3f`

`````text
# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/revision_predicciones/ejecucion.txt

SHA-256: `4e8c4bbd9f547365a4641a6e14668a1d4d7cf84f27d7d534628b52a4df4ea28d`

````text
Auditoría de integridad completada.
Vigente: F1 CV=0.5567
RF_revision_1: F1 CV=0.5403
RF_revision_2: F1 CV=0.5508
RF_revision_3: F1 CV=0.5510
RF_revision_4: F1 CV=0.5427
RF_revision_5: F1 CV=0.5374
RF_revision_6: F1 CV=0.5300
RF_revision_7: F1 CV=0.5368
{"ganador_cv": "Vigente", "mejora_f1_cv": 0.0, "pliegues_superiores": 0, "criterio_predefinido": "Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.", "recomienda_promocion": false, "parametros": {"bootstrap": true, "ccp_alpha": 0.0, "class_weight": null, "criterion": "gini", "max_depth": null, "max_features": "sqrt", "max_leaf_nodes": null, "max_samples": null, "min_impurity_decrease": 0.0, "min_samples_leaf": 5, "min_samples_split": 2, "min_weight_fraction_leaf": 0.0, "monotonic_cst": null, "n_estimators": 200, "n_jobs": 1, "oob_score": false, "random_state": 42, "verbose": 0, "warm_start": false}, "limitacion": "Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva."}

````

## Origen: Final/reports/revision_predicciones/pruebas.txt

SHA-256: `a31747bb2f56fc4588546a71b681c00e1f4f82bc0018e97fa60077a1f45a0134`

````text
.......................................                                  [100%]
=============================== warnings summary ===============================
tests/test_inferencia.py::test_interfaz_envia_valores_del_formulario
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
39 passed, 1 warning in 15.20s

````

## Origen: Final/reports/revision_predicciones/render.log

SHA-256: `d8963fe932f6957b471ee8a0a0f820eaf2f2e75957fe1adb3a0942593e55c1f5`

````text
Pages rendered to /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/revision_predicciones/render_documento

````

`````

## auditoria.json

Ruta: `Final/reports/revision_predicciones/auditoria.json` · Bytes: 690 · SHA-256: `32b012b07dc1ceb64c76dbce53f2edd2b63d9322a23962af7f8019405d11edc2`

````text
{
  "n_entrenamiento": 892,
  "n_prueba": 222,
  "exactitud_prueba": 0.5675675675675675,
  "f1_macro_prueba": 0.5577027296634777,
  "f1_ponderado_prueba": 0.5539995111974958,
  "recall_por_clase": {
    "bajo": 0.6417910447761194,
    "medio": 0.3375,
    "alto": 0.7466666666666667
  },
  "matriz_confusion": [
    [
      43,
      14,
      10
    ],
    [
      32,
      27,
      21
    ],
    [
      9,
      10,
      56
    ]
  ],
  "paridad_predicciones_guardadas": true,
  "probabilidades_validas": true,
  "vecinos_solo_entrenamiento_y_mismo_espacio": true,
  "objetivo_reproducido": true,
  "sha256_modelo": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e"
}
````

## busqueda_folds.csv

Ruta: `Final/reports/revision_predicciones/busqueda_folds.csv` · Bytes: 5770 · SHA-256: `d1c0923c7c99d0f5c4e4896cc7d3ae71bb37bb05bc926dbf313d869f731d4c80`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## busqueda_resumen.csv

Ruta: `Final/reports/revision_predicciones/busqueda_resumen.csv` · Bytes: 621 · SHA-256: `08f959d3c26813eff03a0c8643f43df75daf36b031a33f0c53ff302580177fec`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## casos_formulario.json

Ruta: `Final/reports/revision_predicciones/casos_formulario.json` · Bytes: 973 · SHA-256: `3f052447ed86df1ee48104ec3f2af953f712282a513bd5c8a42368a6dad8026c`

````text
[
  {
    "generos": [
      "Adventure",
      "RPG"
    ],
    "estudio": [
      "Otro"
    ],
    "decada": 2020,
    "Metacritic Rating": 82,
    "Rating": 3.9,
    "clase": "bajo",
    "probabilidades": {
      "alto": 0.2955592390655418,
      "bajo": 0.40592126624713165,
      "medio": 0.29851949468732686
    }
  },
  {
    "generos": [
      "Adventure",
      "RPG"
    ],
    "estudio": [
      "Otro"
    ],
    "decada": 2020,
    "Metacritic Rating": 100,
    "Rating": 5,
    "clase": "alto",
    "probabilidades": {
      "alto": 0.5408269453085124,
      "bajo": 0.20861964106899933,
      "medio": 0.25055341362248806
    }
  },
  {
    "generos": [
      "Adventure",
      "RPG"
    ],
    "estudio": [
      "Otro"
    ],
    "decada": 2020,
    "Metacritic Rating": null,
    "Rating": 5,
    "clase": "bajo",
    "probabilidades": {
      "alto": 0.2779815193893014,
      "bajo": 0.44206113209632525,
      "medio": 0.27995734851437365
    }
  }
]
````

## crear_informe.py

Ruta: `Final/reports/revision_predicciones/crear_informe.py` · Bytes: 17956 · SHA-256: `a936769e528fd287e8a3ccce853df8808995cd944c47a0d4aca0ed65ea61e035`

````text
"""Genera el informe desde las evidencias locales sin modificar datos o modelos.

Ejecutar con el Python documental provisto por Codex.
"""
from pathlib import Path
import csv,json
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

RAIZ=Path(__file__).resolve().parents[2]
R=RAIZ/'reports'; E=R/'revision_predicciones'
leer=lambda p:json.loads(p.read_text())
a=leer(E/'auditoria.json'); decision=leer(E/'decision.json'); weka=leer(E/'weka_recalculado.json')
comp=list(csv.DictReader((R/'tables/comparativo_herramientas.csv').open()))
cv=list(csv.DictReader((E/'busqueda_resumen.csv').open()))
P=[]
def pagina(titulo):
    bloques=[];P.append((titulo,bloques));return bloques

def p(b,t):b.append(('p',t))
def tabla(b,cab,filas):b.append(('tabla',(cab,filas)))
def imagen(b,ruta,leyenda):b.append(('imagen',(ruta,leyenda)))
def fuente(b,t):b.append(('fuente',t))

b=pagina('Hallazgos de Weka y validación web')
p(b,'Informe técnico de avance • 9 de noviembre de 2026 • Versión 1')
p(b,'El modelo de la web reproduce correctamente las predicciones almacenadas y conserva la separación entre entrenamiento y prueba. Su capacidad predictiva es moderada: obtiene 56.76 % de exactitud y F1 macro de 0.5577 en 222 casos de prueba. La clase media sigue siendo la principal debilidad. Siete variantes nuevas del bosque no mejoraron la validación cruzada del modelo vigente, por lo que se conservó ese artefacto.')
p(b,'Este informe integra las corridas gráficas existentes de Weka, su contraste metodológico con Python y las verificaciones de la aplicación Streamlit. Los resultados describen popularidad relativa en un catálogo curado, no ventas, rentabilidad ni probabilidad de éxito comercial de un lanzamiento.')
tabla(b,['Población comprobada','Registros','Uso'],[
 ['Antecedente histórico','1,512','Auditoría de decisiones heredadas'],
 ['Maestro games_curated.csv','1,117','Original designado con 42 columnas'],
 ['Cohorte elegible','1,114','Análisis principal y clasificación'],
 ['Casos completos de clustering','887','Seis variables sin ausencias'],
 ['Entrenamiento y prueba','892 y 222','Partición por grupos de título']])
p(b,'El archivo en data/raw ya es un maestro curado. El antecedente de 1,512 filas se conserva aparte; no debe presentarse como si la limpieza actual hubiera recibido 1,512 filas. La web se aclaró para distinguir HIST y MAESTRO.')
p(b,'En los 887 pares elegibles con ambas notas, Pearson es 0.5439 con p = 1.936 × 10⁻⁶⁹ y Spearman es 0.5242. Es evidencia de asociación entre recepción de usuarios y prensa, no de acuerdo exacto ni de causalidad.')
fuente(b,'Fuentes: reports/inspeccion.md; reports/trazabilidad_historica.md; reports/clustering.md; reports/revision_predicciones/auditoria.json.')

b=pagina('Clasificación observada en Weka')
p(b,'Weka Explorer 3.8.7 evaluó 892 registros con 53 atributos, incluida la clase nominal nivel_popularidad, mediante validación cruzada de diez pliegues. Se verificaron las cuatro matrices originales: sus sumas son 892 y sus diagonales reproducen la exactitud publicada por el programa.')
filas=[]
for f in weka:
 filas.append(['Weka',f['modelo'],f"{f['exactitud_pct']:.4f}",f"{f['f1_macro_promedio_mostrado']:.4f}",f"{f['f1_ponderado']:.4f}"])
for f in comp:
 if f['herramienta']=='Python' and 'enlace_exportacion_weka' in f['esquema_evaluacion']:
  nom={'DummyClassifier':'Dummy','GaussianNB':'GaussianNB','DecisionTreeClassifier':'Árbol CART','RandomForestClassifier':'Random Forest'}[f['modelo']]
  filas.append(['Python enlace',nom,f"{float(f['exactitud_pct']):.4f}",f"{float(f['f1_macro']):.4f}",f"{float(f['f1_ponderado']):.4f}"])
tabla(b,['Herramienta','Modelo','Exactitud %','F1 macro','F1 pond'],filas)
p(b,'RandomForest fue el mejor clasificador de las cuatro corridas de Weka, con 477 aciertos de 892. Su F1 para la clase medio fue 0.381 y su recall 0.360, por debajo de los otros dos niveles; la dificultad de la clase central también aparece en Python.')
p(b,'El F1 macro de Weka promedia los F Measure por clase impresos a tres decimales. En ZeroR el valor no definido de medio se resolvió desde la matriz con la convención de cero; el F1 ponderado de 0.2533 también se calculó desde la matriz porque Weka imprimió un signo de interrogación. Los otros ponderados son los reportados por Weka.')
p(b,'Python enlace usa los mismos 892 registros y 52 predictores numéricos exportados, pero no los mismos pliegues de Java. NaiveBayes y GaussianNB tienen tratamientos distintos; J48 y CART son árboles diferentes. Weka usa 100 árboles y semilla del estimador 1; Python enlace usa 100 y semilla 42. La semilla de los pliegues de la sesión Weka no pudo recuperarse. El preprocesamiento de esta comparación se hizo antes de CV; no sustituye la evaluación de producción con preprocesamiento por pliegue.')
fuente(b,'Fuentes: reports/weka/ZeroR.txt, NaiveBayes.txt, J48.txt y RandomForest.txt; reports/tables/comparativo_herramientas.csv; revision_predicciones/weka_recalculado.json.')

b=pagina('Segmentación observada en Weka')
p(b,'SimpleKMeans utilizó k = 2 y semilla 42 sobre 887 instancias y seis atributos. Convergió en nueve iteraciones y produjo grupos de 477 y 410 juegos. Los centroides siguientes están en las unidades transformadas del archivo exportado, no en conteos originales ni puntos de calificación.')
tabla(b,['Variable','Centro del grupo 0','Centro del grupo 1'],[
 ['Plays','0.4100','−0.4770'],['Playing','0.6189','−0.7200'],['Backlogs','0.7093','−0.8252'],['Wishlist','0.6912','−0.8042'],['Rating','0.4797','−0.5581'],['Metacritic Rating','0.4270','−0.4968']])
p(b,'Los signos de los centros describen un perfil con mayor actividad, interés y recepción frente a otro con valores inferiores al promedio exportado. Es una interpretación descriptiva del catálogo y no prueba que existan segmentos comerciales naturales. Las etiquetas numéricas de los grupos son arbitrarias.')
tabla(b,['Resultado','Python','Weka'],[
 ['K Means con dos grupos','465 y 422','477 y 410'],
 ['DBSCAN grupos válidos','1','1'],
 ['DBSCAN asignados al grupo','866','887'],
 ['DBSCAN ruido','21','0']])
p(b,'En Python k = 2 maximizó silhouette entre 2 y 10, con 0.3188. Weka no reportó esa métrica en la corrida guardada; no se le atribuye el valor de Python. Las sumas de cuadrados tampoco se comparan como si provinieran de una configuración de distancias idéntica.')
p(b,'DBSCAN se ejecutó en Weka con eps = 1.666296 y minPoints = 12. Agrupó las 887 instancias en un solo grupo. En Python, los mismos parámetros nominales dejaron 21 casos como ruido. La igualdad de eps no acredita equivalencia de la distancia interna: Weka informa EuclideanDistance con sus opciones y las implementaciones no son una réplica exacta. No se forzaron parámetros ni se corrigieron las salidas para hacerlas coincidir.')
fuente(b,'Fuentes: reports/weka/kmeans.txt y dbscan.txt; reports/clustering.md; reports/clustering_03_perfiles.csv.')

b=pagina('Hallazgos y correcciones de la web')
p(b,'La aplicación mantiene cuatro páginas: Inicio, Exploración, Predicción y Modelo. Permite consultar señales de popularidad, asociaciones entre notas, perfiles de clustering, predicciones y vecinos del entrenamiento. La identidad azul y morada y la fuente cómic local se aplican sin modificar los datos analíticos.')
p(b,'Se corrigieron las cifras atravesadas por barras de error en los gráficos de desempeño e importancia por permutación. Las cifras se sitúan después del extremo del intervalo; se conservaron sus desviaciones y los rangos estadísticos. Los ejes logarítmicos muestran potencias de diez sin marcas menores amontonadas. En móvil, las figuras densas se desplazan dentro de su panel.')
imagen(b,'reports/revision_predicciones/formulario_verificado.jpg','Predicción comprobada en la interfaz con Adventure y RPG, organización Otro, década de 2020, Metacritic 100 y Rating 5. El modelo devuelve alto con 54.1 % de probabilidad no calibrada.')
p(b,'La revisión del formulario añadió validación explícita de Rating de 0 a 5 y Metacritic de 0 a 100, conservando los nulos para la imputación entrenada. Se eliminó el ancho mínimo artificial de 2 % de las barras. Otro ahora significa organización no frecuente y no presume que sea un estudio independiente.')
fuente(b,'Fuentes: pages/2_Prediccion.py; src/inferencia.py; reports/revision_graficas.md; revision_predicciones/casos_formulario.json.')

b=pagina('Verificación de las predicciones')
p(b,'Se compararon las 222 salidas del artefacto guardado con las predicciones de prueba almacenadas y todas coinciden. Las probabilidades son finitas, suman uno y su mayor valor corresponde a la clase mostrada, usando el orden real de pipeline.classes_. También se reprodujeron las etiquetas y los terciles desde la referencia de entrenamiento.')
tabla(b,['Métrica en prueba','Resultado'],[
 ['Exactitud',f"{100*a['exactitud_prueba']:.2f} %"],['F1 macro',f"{a['f1_macro_prueba']:.4f}"],['F1 ponderado',f"{a['f1_ponderado_prueba']:.4f}"],
 ['Recall bajo',f"{100*a['recall_por_clase']['bajo']:.2f} %"],['Recall medio',f"{100*a['recall_por_clase']['medio']:.2f} %"],['Recall alto',f"{100*a['recall_por_clase']['alto']:.2f} %"]])
tabla(b,['Clase real','Predice bajo','Predice medio','Predice alto'],[[c,*fila] for c,fila in zip(['bajo','medio','alto'],a['matriz_confusion'])])
p(b,'Las entradas son géneros, organizaciones de Team, década, Metacritic Rating y Rating. Plays, Wishlist y Backlogs definen el objetivo y no entran al clasificador; Playing tampoco es predictor. Las categorías e imputaciones se ajustan en entrenamiento. Los títulos agrupados de entrenamiento y prueba no se superponen y el índice de vecinos contiene únicamente IDs de entrenamiento en el mismo espacio transformado.')
p(b,'La ausencia de prensa es una limitación concreta. En el caso comprobado de la página anterior, ocultar Metacritic manteniendo Rating 5 cambia alto a bajo, con 44.2 % para bajo. El cálculo coincide con el Pipeline; no es una inversión de etiquetas del formulario. La web muestra ahora un aviso sobre la imputación. Esto evidencia sensibilidad a la cobertura y no demuestra que un juego sin nota vaya a tener baja popularidad.')
p(b,'Se aprobaron 39 pruebas, incluidas escalas inválidas, valores extremos, organizaciones nuevas, ausencia de crítica y envíos del formulario contrastados con el Pipeline. Las probabilidades no están calibradas y los casos de demostración no constituyen validación externa.')
fuente(b,'Fuentes: models/metadata.json; revision_predicciones/auditoria.json y casos_formulario.json; tests/test_inferencia.py; revision_predicciones/pruebas.txt.')

b=pagina('Revisión del entrenamiento y decisión')
p(b,'Se reutilizaron exclusivamente los 892 registros de entrenamiento y sus diez pliegues agrupados por título. Cada ajuste recalcula objetivo local, vocabularios e imputación sin consultar su validación. Se entrenaron siete variantes nuevas de Random Forest más la referencia vigente, con 200 árboles y random_state 42: 80 ajustes en total.')
config={'Vigente':('5','Sin ponderar','Raíz'), 'RF_revision_1':('1','Sin ponderar','Raíz'), 'RF_revision_2':('2','Balance por muestra','Raíz'), 'RF_revision_3':('5','Balance por muestra','Raíz'), 'RF_revision_4':('10','Balance por muestra','Raíz'), 'RF_revision_5':('2','Sin ponderar','0.5'), 'RF_revision_6':('5','Balance por muestra','0.5'), 'RF_revision_7':('10','Sin ponderar','0.5')}
filas=[]
for f in cv:
 hoja,peso,vars=config[f['candidato']]
 filas.append([f['candidato'].replace('RF_revision_','RF '),hoja,peso,vars,f"{float(f['f1_macro_cv']):.4f}"])
tabla(b,['Candidato','Hoja mín','Ponderación','Variables','F1 CV'],filas)
p(b,'Raíz indica max_features igual a sqrt; 0.5 usa la mitad de las variables transformadas en cada división. Balance por muestra corresponde a class_weight igual a balanced_subsample. La profundidad se mantiene sin límite en estas variantes.')
p(b,'Antes de consultar sus resultados se fijó un criterio de promoción: mejora de al menos 0.01 en F1 macro y superioridad en seis de diez pliegues. Ninguna variante superó siquiera la media del modelo vigente, 0.5567. Se conservan el artefacto y sus métricas; no se presenta una mejora inexistente ni se selecciona un candidato por la prueba.')
p(b,'El mejor recall medio de alguna variante no basta para reemplazar al modelo si disminuye el F1 macro elegido como criterio. La búsqueda no es una CV anidada y amplía la exploración de hiperparámetros sobre los mismos pliegues; sus medias no son una estimación independiente del rendimiento futuro.')
p(b,'La prueba existente ya fue observada. Sin una muestra externa posterior no se puede afirmar una mejora prospectiva ni validar el uso del sistema para géneros nuevos o resultados comerciales. Estas limitaciones se documentan; no se sustituyen con cifras de entrenamiento.')
fuente(b,'Reproducción desde Final: python src/05_revision_predicciones.py. Evidencias: revision_predicciones/busqueda_folds.csv, busqueda_resumen.csv, decision.json y ejecucion.txt.')

b=pagina('Evidencias y límites del informe')
imagen(b,'reports/weka/RandomForest.png','Corrida gráfica original de RandomForest en Weka. Las métricas del informe se extrajeron del texto guardado y se contrastaron con su matriz; la imagen aporta la evidencia visual de la sesión.')
p(b,'Las seis corridas gráficas conservan salidas y capturas locales: SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Esta revisión no reejecuta Weka ni cambia sus resultados. El script verificar_weka.py recalcula sus matrices de clasificación y conserva los hashes de las fuentes.')
p(b,'Orange se descartó por cierres de la aplicación en Qt y Cocoa al usar selectores de archivos. Se probaron la instalación local, recuperación y reinicio del lienzo, CSV y TAB, además de un lanzador con selectores Qt. No hay métricas de Orange en este informe; no se le atribuye ninguna salida de Weka.')
p(b,'La popularidad se refiere a rangos percentiles relativos de Plays, Wishlist y Backlogs. La muestra tiene sesgo de visibilidad comunitaria; Team no separa desarrolladores y publishers. Las notas con origen estimado se excluyen como evidencia independiente de prensa. Las columnas financieras estimadas del maestro no se utilizan para demostrar éxito comercial.')
fuente(b,'Trazabilidad principal: data/raw/games_curated.csv; reports/inspeccion.md; reports/trazabilidad_historica.md; reports/weka/; reports/codex_log.md; reports/tables/comparativo_herramientas.csv; reports/revision_predicciones/.')

# Documento de texto con el mismo contenido y tablas editables.
md=[]
for n,(titulo,bloques) in enumerate(P):
 md.append(('# ' if n==0 else '## ')+titulo+'\n')
 for tipo,v in bloques:
  if tipo in ('p','fuente'):md.append(v+'\n')
  elif tipo=='tabla':
   cab,filas=v;md += ['| '+' | '.join(cab)+' |','| '+' | '.join(['---']*len(cab))+' |',*['| '+' | '.join(map(str,f))+' |' for f in filas],'']
  else:
   ruta,leyenda=v;md.append(f'![{leyenda}]({ruta.removeprefix("reports/")})\n')
(R/'hallazgos_weka_web.md').write_text('\n'.join(md))

D=Document(); sec=D.sections[0]; sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.7);sec.bottom_margin=Inches(.65);sec.left_margin=sec.right_margin=Inches(.75)
sec.header_distance=sec.footer_distance=Inches(.3)
normal=D.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(11)
normal.paragraph_format.space_after=Pt(8);normal.paragraph_format.line_spacing=1.1
for nombre,tamano in [('Title',23),('Heading 1',19)]:
 est=D.styles[nombre];est.font.name='Calibri';est.font.size=Pt(tamano);est.font.color.rgb=RGBColor.from_string('000000' if nombre=='Title' else '15254A');est.font.bold=True
 est.paragraph_format.space_after=Pt(12)
for borde in D.styles['Title'].element.xpath('./w:pPr/w:pBdr'):
 borde.getparent().remove(borde)
D.core_properties.title=P[0][0];D.core_properties.author='';D.core_properties.subject='Resultados reproducibles y límites del modelo'
header=sec.header.paragraphs[0];header.text='';header.style='Caption'
f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.RIGHT
f.add_run('Informe de avance  •  ');campo=OxmlElement('w:fldSimple');campo.set(qn('w:instr'),'PAGE');f._p.append(campo)
for n,(titulo,bloques) in enumerate(P):
 if n:D.add_page_break()
 D.add_paragraph(titulo,'Title' if n==0 else 'Heading 1')
 for tipo,v in bloques:
  if tipo in ('p','fuente'):
   par=D.add_paragraph(v)
   if tipo=='fuente':
    for run in par.runs:run.font.size=Pt(9);run.font.color.rgb=RGBColor.from_string('41516D')
  elif tipo=='imagen':
   ruta,leyenda=v
   D.add_picture(str(RAIZ/ruta),width=Inches(6.85))
   par=D.add_paragraph(leyenda)
   for run in par.runs:run.font.size=Pt(10);run.italic=True
  else:
   cab,filas=v;t=D.add_table(rows=1, cols=len(cab));t.autofit=False
   t.style='Table Grid'
   for celda,texto in zip(t.rows[0].cells,cab):
    celda.text=texto;pr=celda._tc.get_or_add_tcPr();color=OxmlElement('w:shd');color.set(qn('w:fill'),'15254A');pr.append(color)
    for run in celda.paragraphs[0].runs:run.font.color.rgb=RGBColor(255,255,255);run.bold=True
   for fila in filas:
    for celda,texto in zip(t.add_row().cells,fila):celda.text=str(texto)
   for row in t.rows:
    pr=row._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
    for celda in row.cells:
     for par in celda.paragraphs:
      par.paragraph_format.space_after=Pt(4);par.paragraph_format.space_before=Pt(4);par.paragraph_format.line_spacing=1
      for run in par.runs:run.font.size=Pt(10)
   repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
   D.add_paragraph().paragraph_format.space_after=Pt(1)
D.save(R/'hallazgos_weka_web.docx')
print('Informe Word y fuente Markdown generados.')

````

## decision.json

Ruta: `Final/reports/revision_predicciones/decision.json` · Bytes: 1000 · SHA-256: `cd3c19e80e1eef1cd9b55801e659edd5d653e8dc0450b2cf2ef08ed5dfcf9e38`

````text
{
  "ganador_cv": "Vigente",
  "mejora_f1_cv": 0.0,
  "pliegues_superiores": 0,
  "criterio_predefinido": "Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.",
  "recomienda_promocion": false,
  "parametros": {
    "bootstrap": true,
    "ccp_alpha": 0.0,
    "class_weight": null,
    "criterion": "gini",
    "max_depth": null,
    "max_features": "sqrt",
    "max_leaf_nodes": null,
    "max_samples": null,
    "min_impurity_decrease": 0.0,
    "min_samples_leaf": 5,
    "min_samples_split": 2,
    "min_weight_fraction_leaf": 0.0,
    "monotonic_cst": null,
    "n_estimators": 200,
    "n_jobs": 1,
    "oob_score": false,
    "random_state": 42,
    "verbose": 0,
    "warm_start": false
  },
  "limitacion": "Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva."
}
````

## formulario_verificado.jpg

Ruta: `Final/reports/revision_predicciones/formulario_verificado.jpg` · Bytes: 138668 · SHA-256: `3cd54dcfd4cdbf08df46f28af97f92ecb43e198dccd9f2124cb5ad41220c383b`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## integridad_final.json

Ruta: `Final/reports/revision_predicciones/integridad_final.json` · Bytes: 169 · SHA-256: `90e1137d1c8fcc542b15d7f84670248c35134f5288086b6c057dc1ab4667a7b5`

````text
{
  "archivos_verificados": 20,
  "modificados": [],
  "modelo_conservado": true,
  "sha256_modelo": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e"
}
````

## qa_documento.json

Ruta: `Final/reports/revision_predicciones/qa_documento.json` · Bytes: 207 · SHA-256: `01f686eb15364a6032fec96f62af11b112b013a37083cfce67ae41ddc3cac3db`

````text
{
  "paginas_renderizadas": 7,
  "paginas_inspeccionadas_visualmente": [
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ],
  "titulo_negro_sin_borde": true,
  "tablas_y_capturas_sin_solapamientos": true
}
````

## sin_critica_verificado.jpg

Ruta: `Final/reports/revision_predicciones/sin_critica_verificado.jpg` · Bytes: 147412 · SHA-256: `c9f42e216d9c1ca2928c64ad965b607d0861e5d9c315a7d321d9337553818d0a`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## verificar_weka.py

Ruta: `Final/reports/revision_predicciones/verificar_weka.py` · Bytes: 1922 · SHA-256: `d818e9cbed6c2744fcd36e7d877ba5aee56de2eaa167cc13abd76c34681e3086`

````text
"""Recalcula aciertos y F1 desde salidas Weka existentes, sin ejecutar Weka."""
from pathlib import Path
import re,json,hashlib,csv
RAIZ=Path(__file__).resolve().parents[2]
resultados=[]
for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
    p=RAIZ/'reports/weka'/f'{nombre}.txt'; texto=p.read_text()
    filas=[re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+\|.*?=\s*(\w+)',l) for l in texto.splitlines()]
    filas=[f for f in filas if f]
    matriz=[[int(f[i]) for i in range(1,4)] for f in filas]
    clases=[f[4] for f in filas]
    total=sum(map(sum,matriz));aciertos=sum(matriz[i][i] for i in range(3))
    original=float(re.search(r'Correctly Classified Instances\s+\d+\s+([\d.]+)',texto)[1])
    assert total==892 and abs(original-100*aciertos/total)<.000051
    f1=[];f1_mostrados=[]
    for i,c in enumerate(clases):
        tp=matriz[i][i];den=sum(matriz[i])+sum(f[i] for f in matriz)
        f1.append(2*tp/den if den else 0)
        linea=next(l for l in texto.splitlines() if len(l.split())==9 and l.split()[-1]==c)
        v=linea.split()[4]
        f1_mostrados.append(f1[-1] if v=='?' else float(v))
    ponderado_txt=re.search(r'Weighted Avg\.\s+(.+)',texto)[1].split()[4]
    ponderado=sum(sum(matriz[i])*f1[i] for i in range(3))/total
    resultados.append({'modelo':nombre,'n':total,'aciertos':aciertos,'exactitud_pct':original,
        'f1_macro_promedio_mostrado':sum(f1_mostrados)/3,
        'f1_macro_desde_matriz':sum(f1)/3,'f1_ponderado':ponderado if ponderado_txt=='?' else float(ponderado_txt),
        'ponderado_calculado':ponderado,'ponderado_es_recalculado':ponderado_txt=='?',
        'clases':clases,'matriz':matriz,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(RAIZ/'reports/revision_predicciones/weka_recalculado.json').write_text(json.dumps(resultados,ensure_ascii=False,indent=2))
print('Cuatro matrices Weka verificadas; 892 casos en cada una y exactitudes reproducidas.')

````

## weka_recalculado.json

Ruta: `Final/reports/revision_predicciones/weka_recalculado.json` · Bytes: 2585 · SHA-256: `bdae11e086f67b81c5accbdc02878a6c6dc9c06fd6ec0dac8917fe05e246653d`

````text
[
  {
    "modelo": "ZeroR",
    "n": 892,
    "aciertos": 295,
    "exactitud_pct": 33.0717,
    "f1_macro_promedio_mostrado": 0.25333333333333335,
    "f1_macro_desde_matriz": 0.25307162121666166,
    "f1_ponderado": 0.25329318243206017,
    "ponderado_calculado": 0.25329318243206017,
    "ponderado_es_recalculado": true,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        87,
        210,
        0
      ],
      [
        90,
        208,
        0
      ],
      [
        90,
        207,
        0
      ]
    ],
    "sha256": "abc7807ce09733680834ddcfcbf72f7a71f72e62ad1d519db547385bc4fe1cad"
  },
  {
    "modelo": "NaiveBayes",
    "n": 892,
    "aciertos": 454,
    "exactitud_pct": 50.8969,
    "f1_macro_promedio_mostrado": 0.5033333333333333,
    "f1_macro_desde_matriz": 0.5033953898573705,
    "f1_ponderado": 0.503,
    "ponderado_calculado": 0.5034553457668585,
    "ponderado_es_recalculado": false,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        193,
        28,
        76
      ],
      [
        47,
        164,
        87
      ],
      [
        101,
        99,
        97
      ]
    ],
    "sha256": "5aac3e1f7f662eb504b71c7f77d1e31f2121a15ba7771c97b630a65bfd3027c6"
  },
  {
    "modelo": "J48",
    "n": 892,
    "aciertos": 455,
    "exactitud_pct": 51.009,
    "f1_macro_promedio_mostrado": 0.5063333333333334,
    "f1_macro_desde_matriz": 0.5063108540376969,
    "f1_ponderado": 0.506,
    "ponderado_calculado": 0.5063502534846777,
    "ponderado_es_recalculado": false,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        193,
        29,
        75
      ],
      [
        42,
        160,
        96
      ],
      [
        91,
        104,
        102
      ]
    ],
    "sha256": "88ceace97d84c7c67628688f9876a4d3de22c07935e6111dd954f3c401a88c8c"
  },
  {
    "modelo": "RandomForest",
    "n": 892,
    "aciertos": 477,
    "exactitud_pct": 53.4753,
    "f1_macro_promedio_mostrado": 0.5299999999999999,
    "f1_macro_desde_matriz": 0.5303083703633139,
    "f1_ponderado": 0.53,
    "ponderado_calculado": 0.5303645618510748,
    "ponderado_es_recalculado": false,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        195,
        29,
        73
      ],
      [
        39,
        175,
        84
      ],
      [
        89,
        101,
        107
      ]
    ],
    "sha256": "bed5274c54f92bc20ff70c7d64d600839b65e76ea4860e88d8e003dcd5bb47df"
  }
]
````

