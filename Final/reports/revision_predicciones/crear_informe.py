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
