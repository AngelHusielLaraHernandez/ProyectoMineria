"""Compone LaTeX y copia evidencias tabulares sin entrenar ni modificar el proyecto."""
from pathlib import Path
import csv,json,shutil,re,hashlib
D=Path(__file__).resolve().parent;R=D.parent/'Final/reports'
def esc(s):
 s={'RandomForestClassifier':'Random Forest','DecisionTreeClassifier':'Árbol CART','DummyClassifier':'Dummy','CategoricalNB':'Naive Bayes','MLPClassifier':'Red neuronal MLP','generos':'Géneros','estudio':'Organización','decada':'Década','Rating':'Usuarios','Metacritic Rating':'Metacritic'}.get(str(s),str(s))
 return ''.join({'&':r'\&','%':r'\%','_':r'\_\allowbreak{}','#':r'\#','$':r'\$','{':r'\{','}':r'\}','−':'-'}.get(c,c) for c in str(s))
for nombre in ['clase_ward_dendrograma.png','comparacion_mlp.png','dashboard_interactivo.png']:
 shutil.copy2(R/'figures'/nombre,D/'figuras'/nombre)
for nombre in ['modelo.md','modelo_confusion_MLPClassifier.csv','clase_ward_perfiles.csv','clase_ward_cortes.csv']:
 shutil.copy2(R/nombre,D/'evidencias'/nombre)
shutil.copy2(D.parent/'Final/models/metadata.json',D/'evidencias/metadata.json')
partes=[]
def texto(t):partes.append(t)
def tabla(archivo,campos,titulos,caption,fmt=None,limite=None):
 p=R/archivo;filas=list(csv.DictReader(p.open()));filas=filas[:limite] if limite else filas
 shutil.copy2(p,D/'tablas'/p.name)
 s='\\begin{longtable}{'+('p{'+str(round(.87/len(campos),3))+r'\textwidth}')*len(campos)+'}\n\\caption{'+esc(caption)+'}\\\\\n\\toprule\n'+' & '.join(map(esc,titulos))+r'\\\midrule\endfirsthead'+'\n'+' & '.join(map(esc,titulos))+r'\\\midrule\endhead'+'\n'
 for f in filas:
  vs=[]
  for c in campos:
   v=f[c]
   if fmt and c in fmt:
    try:v=fmt[c](float(v))
    except ValueError:pass
   vs.append(esc(v if v else 'No aplica'))
  s+=' & '.join(vs)+r'\\'+'\n'
 s+=r'\bottomrule\end{longtable}'+'\n';texto(s)
def fig(nombre,cap,alto='.65'):
 texto(r'\begin{figure}[htbp]\centering\includegraphics[width=\linewidth,height='+alto+r'\textheight,keepaspectratio]{figuras/'+nombre+'}\n\\caption{'+cap+r'}\end{figure}\FloatBarrier'+'\n')
texto(r'''\documentclass[letterpaper,11pt]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[spanish,mexico]{babel}
\usepackage{lmodern,microtype,graphicx,booktabs,longtable,array,amsmath,float,placeins}
\usepackage[margin=2.5cm,headheight=15pt]{geometry}
\usepackage{xcolor,hyperref,fancyhdr,csquotes,caption}\captionsetup[table]{skip=8pt}
\usepackage[backend=biber,style=apa]{biblatex}\addbibresource{referencias.bib}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black,citecolor=blue!45!black}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{Minería de Datos}\fancyhead[R]{Videojuegos}\fancyfoot[C]{\thepage}
\setlength{\parskip}{.5em}\setlength{\parindent}{0pt}\setlength{\emergencystretch}{3em}
\renewcommand{\arraystretch}{1.2}\setlength{\tabcolsep}{4pt}
\begin{document}\begin{titlepage}\centering
\includegraphics[width=1.7cm]{figuras/der.png}\hfill\includegraphics[width=1.7cm]{figuras/izq.png}\\[.5cm]
{\Large Universidad Nacional Autónoma de México\\Facultad de Ingeniería}\\[1.2cm]
{\LARGE\bfseries Análisis de recepción y popularidad de videojuegos mediante minería de datos}\\[.6cm]
{\Large Proyecto final\\Minería de Datos}\\[1cm]
Lara Hernández Angel Husiel -- 320060829\\[.2cm]
Lugo Manzano Rodrigo -- 320206968\\[.2cm]
García Cortés Adolfo de Jesús -- 320317264\\[.8cm]
Grupo 01\quad Semestre 2027-1\\[.7cm]
Profesor\\MTRO. GERARDO GABRIEL CARRASCO ZUÑIGA\\[1cm]
Documento integrado con evidencia disponible al 11 de noviembre de 2026\\[.3cm]
Entrega prevista en la línea base: 25 de noviembre de 2026
\vfill\end{titlepage}
\section*{Resumen}\addcontentsline{toc}{section}{Resumen}
En este proyecto analizamos la recepción y popularidad relativa de los videojuegos a partir de registros de Backloggd y notas de prensa incorporadas al archivo curado. Partimos de un problema: una calificación alta no equivale necesariamente a una comunidad grande, y el interés pendiente tampoco equivale a ventas. Por eso distinguimos las notas, la actividad acumulada y las listas de interés antes de construir perfiles y un clasificador.

El original designado, \texttt{games\_curated.csv}, contiene 1,117 registros y 42 columnas; 1,114 son elegibles para el análisis principal y 887 tienen las seis variables completas para clustering. Pearson entre usuarios y prensa es 0.5439 en esos 887 pares. K-Means y Ward seleccionaron dos grupos, con siluetas de 0.3188 y 0.2807. La MLP activa en la web obtiene 50.90\,\% de exactitud y F1 macro de 0.5008 sobre 222 casos de prueba. Random Forest obtiene 0.5577 de F1 macro en esa misma prueba. En Weka, RandomForest obtiene 53.4753\,\% con validación cruzada de diez pliegues sobre 892 registros exportados. Las evaluaciones no son equivalentes y se presentan por separado.

La aplicación permite explorar los hallazgos, enviar atributos crudos al Pipeline y consultar vecinos del entrenamiento. El resultado más importante es que podemos describir diferencias de recepción y popularidad dentro del catálogo, pero no demostrar rentabilidad, causalidad ni riesgo financiero de juegos como servicio. La clase media y la cobertura de prensa limitan la utilidad predictiva.
\tableofcontents\clearpage
\section{Introducción y problemática}
El punto de partida fue entender qué significa que un videojuego tenga éxito. En una plataforma social podemos encontrar un juego con buena recepción y pocos registros de actividad, o un juego muy conocido cuya calificación no sea particularmente alta. Si juntamos estas situaciones en una sola medida, perdemos la diferencia entre calidad percibida, alcance e interés.

La preocupación del anteproyecto por las apuestas a géneros y juegos como servicio sirvió para plantear el problema. Sin embargo, los datos no contienen una identificación confiable de GaaS ni ingresos, costos y ventas observados. Por ello no atribuimos fracasos comerciales a la elección de un género ni presentamos el modelo como una herramienta para evitar pérdidas. Esa relación requeriría otras fuentes y otro diseño de estudio.

Lo que sí podemos atender es la falta de una lectura conjunta de los indicadores disponibles. Contrastamos la recepción de usuarios y prensa, distinguimos actividad e interés y evaluamos si los atributos de un juego permiten estimar su posición relativa en este catálogo. La finalidad es apoyar la exploración y formular preguntas mejor delimitadas, no sustituir un estudio de mercado.
\section{Objetivos y expectativas}
\subsection{Objetivo general}
Analizar la relación entre recepción y popularidad relativa en el catálogo curado de videojuegos mediante correlaciones, agrupamiento y clasificación supervisada, y presentar resultados verificables en una aplicación local de Streamlit.
\subsection{Objetivos específicos}
\begin{enumerate}
\item Verificar el esquema, las escalas, los faltantes y la procedencia del maestro, conservando su integridad y documentando cada transformación.
\item Estimar Pearson y Spearman entre notas, reportando tamaño muestral y p-valor por catálogo, género y organización, con un mínimo de veinte pares completos por grupo.
\item Describir Plays, Playing, Backlogs y Wishlist; distinguir actividad observada de interés pendiente sin equipararlas a ventas.
\item Comparar K-Means y Ward de dos a diez grupos sobre seis variables transformadas, informando métricas internas y tamaños. Conservar DBSCAN como contraste exploratorio histórico.
\item Comparar una referencia mayoritaria, Naive Bayes, árbol y bosque para clasificar terciles de popularidad con entradas que no incluyan las señales del objetivo.
\item Verificar el formulario contra el Pipeline guardado y ofrecer una demo local con exploración, predicción y explicación de las limitaciones.
\end{enumerate}
\subsection{Expectativas y criterios de aceptación}
Esperábamos encontrar relaciones entre las notas, perfiles interpretables y un clasificador superior a una referencia mayoritaria. Estas expectativas se comprueban con evidencia, no por la apariencia de las gráficas. Una correlación no equivale a acuerdo; un grupo dominante no basta para afirmar segmentación útil; una exactitud superior al azar no garantiza buen desempeño en cada clase.

El proyecto se considera funcional cuando las tablas y predicciones se reproducen, las transformaciones no usan información de prueba y la aplicación muestra los resultados del artefacto real. La capacidad para predecir éxito comercial queda fuera del criterio de aceptación porque no puede verificarse con este archivo.
\section{Contexto del conjunto de datos}
\subsection{Origen y unidad de análisis}
El antecedente se atribuye al conjunto de Arnab Chaki publicado en Kaggle, construido con información de Backloggd \parencite{chaki2023popular}. El archivo que el usuario designó como original es una versión ya curada, no una descarga virgen del catálogo público. Contiene datos adicionales, incluidas notas y estimaciones. La portada del dataset menciona 1980--2023, pero el maestro local tiene cobertura histórica hasta 2025; no sustituimos una cosa por la otra.

La unidad analítica se identifica por \texttt{id\_juego}. El mismo título puede aparecer con otra fecha, por lo que las uniones no se realizan solo por nombre. Hay 35 registros de 17 títulos repetidos en fechas distintas. Para particionar el modelo sí agrupamos nombres normalizados, de forma conservadora, para que versiones del mismo título no aparezcan a ambos lados de la evaluación.
\subsection{Variables y escalas verificadas}
Rating corresponde a usuarios en escala de cero a cinco; su rango observado es 0.7 a 4.8, con trece ausencias. La nota original de Metacritic tiene valores de 45 a 99; la escala de referencia de prensa es cero a cien. Los extremos observados no se usan como denominadores de normalización.

Plays representa registros de juego; Playing contextualiza actividad en curso; Backlogs y Wishlist reflejan interés registrado. No son personas únicas verificadas, copias vendidas ni ingresos. Genres y Team son listas. Team puede mezclar organizaciones con papeles distintos y no acredita por sí mismo cuál desarrolló o publicó el juego.

El maestro incluye columnas financieras estimadas. No se utilizan para concluir que un título fue rentable. Asimismo, 218 notas marcadas como estimaciones propias no se aceptan como evidencia independiente de prensa: en el antecedente, 214 estimaciones con Rating siguen una relación lineal tras redondear. Incluirlas inflaría artificialmente la relación que se desea estudiar.
\subsection{Poblaciones y sesgos}
El antecedente de 1,512 registros se reconstruye hasta el maestro de 1,117, con 395 descartes históricos documentados. Esto no significa que la limpieza actual haya eliminado 395 filas: recibe un maestro ya curado y conserva sus 1,117 registros. Tres conflictos históricos se mantienen señalados y se excluyen del análisis principal; quedan 1,114 elegibles.

Las correlaciones y el clustering completo usan 887 casos elegibles con las notas y señales necesarias. Las ausencias no son ruido de DBSCAN ni una categoría de popularidad. La selección de juegos visibles en Backloggd implica sesgo de cobertura y supervivencia; las conclusiones se limitan al catálogo y al corte disponible.
\section{Estrategia y metodología aplicada}
Adoptamos CRISP-DM como estructura de trabajo \parencite{chapman2000crisp}. Sus seis fases organizan la comprensión del problema, la inspección, la preparación, el modelado, la evaluación y la entrega. No las confundimos con los nombres de scripts: \texttt{03\_clustering.py} corresponde a tareas de modelado y evaluación, no a una tercera fase de negocio.

El proceso fue iterativo. Las auditorías obligaron a revisar la procedencia de las notas, la definición del objetivo y las separaciones del entrenamiento. La propuesta propia en Python consiste en integrar estas salvaguardas en Pipelines, recalcular referencias del objetivo dentro de cada pliegue y verificar la inferencia del formulario. La complejidad adicional no se justifica por agregar un modelo más, sino por evitar que una comparación favorable provenga de fuga de información.

Las herramientas cumplen papeles distintos: pandas prepara y verifica tablas; matplotlib produce figuras de reporte; scikit-learn entrena y evalúa; Weka aporta corridas gráficas de una herramienta de la materia; Streamlit y Plotly presentan resultados interactivos; LaTeX integra la documentación. El uso del Pipeline facilita mantener el mismo preprocesamiento en validación e inferencia \parencite{pedregosa2011scikit,sklearncv}.
\section{Preparación y control de calidad}
Los campos numéricos se interpretan con una función que reconoce sufijos K y M, espacios y nulos; un texto inválido no se convierte silenciosamente a cero. No obstante, los seis conteos del maestro ya eran numéricos: la limpieza actual no se adjudica conversiones que no realizó. Las pruebas sí incluyen casos como 999, 1K y 1.5M.

Las fechas se convierten a un formato común y generan año y década. Se mantienen tres fechas ausentes con sus indicadores en lugar de inventarlas. Los géneros se conservan como listas y se expanden a una tabla larga de 2,682 pertenencias. El género principal es una convención de presentación, no una taxonomía dominante demostrada; un juego participa en cada género declarado cuando hacemos análisis por género.

Los faltantes de notas permanecen ausentes en los análisis descriptivos. La imputación por mediana se reserva al modelo y se ajusta únicamente con su entrenamiento. La nota crítica analítica usa la procedencia documentada en el maestro y deja fuera las estimaciones propias. Esto valida coherencia interna de etiquetas, no una comprobación externa de cada Metascore.

La normalización y la brecha se definen como:
\begin{equation} R_{100}=\frac{R}{5}\,100,\qquad \Delta=R_{100}-M.\end{equation}
Un signo positivo indica que la valoración de usuarios normalizada es mayor. La brecha absoluta mide distancia entre puntuaciones, mientras que Pearson mide asociación. No aplicamos min--max con los extremos de la muestra porque cambiaría el significado de la brecha cada vez que cambia el catálogo.

La limpieza registra conteos antes y después de cada paso y conserva el maestro. Los indicadores de conflicto y elegibilidad permiten conservar filas para trazabilidad sin introducirlas en la evaluación principal. Los hashes aportan una comprobación adicional de integridad, pero no garantizan que la fuente histórica carezca de errores.
\section{Análisis exploratorio y recepción}
\subsection{Actividad e interés}
La distribución de actividad e interés es asimétrica. Por eso presentamos conteos con escala logarítmica para que los títulos de menor alcance no desaparezcan frente a los más conocidos. Logaritmar la visualización no crea popularidad nueva ni cambia el orden de los juegos.

Plays se interpreta como alcance registrado y Backlogs y Wishlist como interés pendiente. Playing se conserva como contexto de actividad. Un juego con muchas listas pendientes puede tener demanda potencial dentro de la plataforma, pero también puede acumular espera sin convertirse en actividad. Por esta razón evitamos llamar éxito comercial a un valor alto del índice.
''')
fig('eda_plays_log.png','Distribución de Plays en la inspección del maestro. Fuente: figura reproducible del proyecto.', '.42')
fig('graficas_logaritmicas_corregidas.jpg','Captura histórica de la distribución por género en la aplicación. Escala logarítmica y etiquetas mayores legibles.', '.48')
tabla('clustering_03_correlaciones_senales.csv',['variable_a','variable_b','n','spearman_rho','spearman_p'],['Variable A','Variable B','Pares','Spearman','p Spearman'],'Relaciones de rango entre señales y notas; pares completos para cada comparación.',{'spearman_rho':lambda x:f'{x:.4f}','spearman_p':lambda x:f'{x:.2e}'})
texto(r'''\subsection{Usuarios y prensa}
En el catálogo elegible, Pearson es 0.5439 con $p=1.936\times10^{-69}$ y Spearman es 0.5242 con $p=9.34\times10^{-64}$, sobre 887 pares completos. La asociación positiva es moderada; el p-valor pequeño no transforma esa asociación en acuerdo perfecto ni en efecto causal.

Para grupos se exige un mínimo de veinte pares válidos, no simplemente veinte filas. Los géneros se superponen: sus tamaños no deben sumarse para obtener el total de juegos. Los estudios se presentan como organizaciones de Team y no como desarrolladores confirmados. La comprobación con Spearman reduce la dependencia de una relación estrictamente lineal, pero tampoco demuestra acuerdo.
''')
fm={c:(lambda x:f'{x:.4f}') for c in ['pearson_r','spearman_rho','brecha_absoluta_media']};fm.update({c:(lambda x:f'{x:.2e}') for c in ['pearson_p','spearman_p']})
tabla('clustering_03_correlaciones_generos.csv',['grupo','n','pearson_r','pearson_p','spearman_rho'],['Género','Pares','Pearson','p Pearson','Spearman'],'Correlaciones por género. La tabla conserva las filas reportadas; las exclusiones se documentan en la evidencia.',fm)
texto(r'''Los resultados no sostienen que todos los géneros tengan la misma relación. Arcade presenta $r=0.7548$ con 39 pares, mientras que Visual Novel tiene $r=-0.1042$ con 27 y $p=0.605$. En este último grupo no hay evidencia suficiente de asociación lineal distinta de cero. Comparar coeficientes de grupos superpuestos no constituye una prueba formal de diferencia entre géneros.
''')
tabla('clustering_03_correlaciones_organizaciones.csv',['grupo','n','pearson_r','pearson_p'],['Organización','Pares','Pearson','p Pearson'],'Asociaciones de las primeras doce organizaciones reportadas, ordenadas por cobertura.',fm,12)
tabla('clustering_03_correlaciones_ranking_generos.csv',['grupo','n','brecha_absoluta_media','pearson_r'],['Género','Pares','Brecha absoluta','Pearson'],'Orden de géneros por menor distancia absoluta media entre puntuaciones.',fm)
texto(r'''Visual Novel aparece con menor distancia media entre notas, pero su correlación no es positiva de forma concluyente. Esto muestra por qué distinguimos coincidencia de niveles y asociación: que dos series tengan notas cercanas no implica que ordenen los juegos de la misma forma. Los p-valores segmentados son exploratorios; el proyecto también conserva ajustes por comparaciones múltiples en las tablas originales.
\section{Clustering y perfiles del catálogo}
\subsection{Transformación y elección de K-Means}
Se utilizaron Plays, Playing, Backlogs, Wishlist, Rating y Metacritic Rating. Los cuatro conteos reciben $\log(1+x)$ y después se estandarizan las seis variables. Con ello reducimos la asimetría de los conteos y evitamos que las unidades de una sola variable dominen la distancia. El género no entra a la distancia; sirve para interpretar la composición posterior.

K-Means se evaluó de $k=2$ a $10$, con semilla 42 y treinta inicializaciones. La elección de dos grupos maximiza silhouette, 0.3188; los valores de $k=3$ y $k=4$ son 0.2377 y 0.2268. La inercia disminuye al aumentar grupos, por lo que no se usa su mínimo como una regla automática para escoger el mayor $k$.
''')
fig('clustering_03_kmeans.png','Inercia y silhouette para la selección de k. Fuente: ejecución de Python.', '.45')
texto(r'''Los grupos de Python contienen 465 y 422 juegos. El primero combina mayor actividad, interés y notas medias: Plays 7,680.62, Wishlist 1,053.28 y Rating 3.91; el segundo registra Plays 2,980.68, Wishlist 246.23 y Rating 3.38. Los nombres propuestos describen esas diferencias y no certifican segmentos comerciales naturales.

Adventure aparece en ambos perfiles, por lo que su predominio no distingue por sí solo una oportunidad de mercado. Además, la primera separación resume magnitud conjunta: las alternativas con tres y cuatro grupos se conservaron para explorar combinaciones sin cambiar la selección por conveniencia narrativa. La figura PCA es una proyección descriptiva y no las dimensiones con las que se entrenó K-Means.
''')
fig('clustering_03_proyeccion.png','Proyección de los casos agrupables. Los ejes reducidos se utilizan para visualización, no para definir el objetivo supervisado.', '.48')
tabla('clustering_03_ejemplos.csv',['cluster','id_juego','juego'],['Grupo','ID','Juego'],'Cinco ejemplos descriptivos por grupo K-Means, próximos al centro del perfil en el espacio transformado.',limite=10)
texto(r'''\subsection{DBSCAN y puntos atípicos}
La elección de eps usa la curva de distancia al vecino y una regla geométrica reproducible sobre la curva normalizada. Se obtuvo eps de 1.666296, con doce vecinos mínimos. DBSCAN encontró un grupo válido y 21 puntos de ruido, 2.37\,\% de los 887 agrupables.

No se reporta silhouette para un solo grupo válido. La etiqueta $-1$ significa ruido dentro de los casos analizados; una etiqueta vacía significa que el juego no fue agrupable por ausencia o conflicto. DBSCAN no aportó aquí una segmentación múltiple útil del mercado: funcionó como descripción de núcleo y atípicos. Forzar eps para producir más perfiles hubiera ocultado este resultado.
''')
fig('clustering_03_dbscan_kdistancia.png','Curva utilizada para seleccionar eps en Python.', '.44')
texto(r"""\subsection{Agrupamiento jerárquico con Ward}
Aplicamos Ward con distancia euclidiana sobre los mismos 887 juegos y las mismas seis variables transformadas que K-Means. Se compararon cortes de dos a diez grupos y se eligió el de mayor silueta. Con dos grupos, Ward obtuvo tamaños de 558 y 329 juegos. El dendrograma presenta las últimas fusiones y resume cuántos juegos contiene cada rama.
""")
tabla('clase_comparacion_clustering.csv',['metodo','k','silhouette','davies_bouldin','calinski_harabasz'],['Método','Grupos','Silueta','Davies--Bouldin','Calinski--Harabasz'],'Comparación de los cortes elegidos por silueta en el mismo espacio.',{c:(lambda x:f'{x:.4f}') for c in ['silhouette','davies_bouldin','calinski_harabasz']})
texto(r"""K-Means obtuvo mayor silueta y Calinski--Harabasz, y menor Davies--Bouldin. Los tres índices favorecen K-Means en esta muestra y con esta representación. Los perfiles se interpretan mediante sus variables originales. El mapa PCA solo proyecta los grupos ya ajustados.
""")
fig('clase_ward_dendrograma.png','Últimas fusiones del dendrograma de Ward. Cada etiqueta entre paréntesis indica la cantidad de juegos representada.', '.42')
texto(r'''\section{Clasificación supervisada}
\subsection{Definición de popularidad relativa}
Comparamos conceptualmente dos objetivos. Solo Plays es más simple y representa alcance acumulado; el índice compuesto incorpora interés pendiente, aunque da dos tercios del peso a Wishlist y Backlogs, dos señales relacionadas. Se eligió el índice por ese alcance más amplio y se declara la redundancia como limitación:
\begin{equation}I(x)=\frac{P_{\mathrm{train}}(Plays_x)+P_{\mathrm{train}}(Wishlist_x)+P_{\mathrm{train}}(Backlogs_x)}{3}.\end{equation}
Los percentiles se ajustan como rangos medios divididos entre el tamaño del entrenamiento; para datos externos se interpolan entre valores distintos y se usan cero y uno fuera de sus extremos. Dos cortes en los terciles del índice de entrenamiento definen bajo, medio y alto, preservando empates. Estos niveles son relativos al catálogo popular, no umbrales absolutos de toda la industria.
\subsection{Separación y prevención de fuga}
Antes de definir etiquetas se aplica GroupShuffleSplit por título normalizado, semilla 42 y proporción aproximada 80/20: 892 registros de entrenamiento y 222 de prueba. No se exige estratificar clases que todavía no están definidas. La referencia del objetivo se calcula con entrenamiento y se aplica a ambos conjuntos.

La selección utiliza StratifiedGroupKFold de diez pliegues. Dentro de cada ajuste se recalculan referencia y cortes del objetivo, categorías e imputaciones usando solo el subentrenamiento. Las etiquetas de entrenamiento externo organizan los estratos, pero la puntuación de cada validación usa la referencia local. Esta distinción evita que la definición del objetivo conozca los conteos de la validación.

Las entradas del Pipeline son géneros, organizaciones, década y las dos notas. Ninguno de los cuatro conteos, el índice de popularidad, los clusters, PCA ni las banderas de procedencia entra al clasificador. El preprocesamiento forma parte del artefacto y recibe atributos crudos, tanto en las pruebas como en la web.
\subsection{Representación y comparación de modelos}
Los géneros se codifican multi-hot con hasta quince categorías y frecuencia mínima veinte dentro de cada ajuste. Las organizaciones usan frecuencia mínima diez; Otro se activa si no hay ninguna organización conocida. Las notas se imputan por mediana entrenada. La década se codifica mediante one-hot, conservando una categoría de ausencia.

La referencia es DummyClassifier con la clase más frecuente. CategoricalNB discretiza las notas en cinco intervalos; se prefiere a ajustar gaussianas sobre decenas de indicadores binarios raros, reconociendo la pérdida de resolución y la independencia aproximada. Se comparan además árbol CART, Random Forest y una red neuronal MLP. Se probaron capas ocultas de 16 y 32 neuronas con activación tanh, optimizador L-BFGS y regularización L2. El ajuste elegido usa 32 neuronas y alpha de 5. La selección se cierra por F1 macro media de CV antes de evaluar la prueba.
''')
tabla('modelo_comparacion.csv',['modelo','f1_macro_cv','desviacion_cv','exactitud_prueba','f1_macro_prueba'],['Modelo','F1 CV','Desv CV','Exactitud prueba','F1 prueba'],'Comparación de candidatos en la prueba reservada de 222 casos. Exactitud expresada como fracción.',{c:(lambda x:f'{x:.4f}') for c in ['f1_macro_cv','desviacion_cv','exactitud_prueba','f1_macro_prueba']})
texto(r"""La MLP obtiene el mayor F1 macro medio de validación cruzada, 0.5608 frente a 0.5567 de Random Forest. La diferencia de 0.0041 es pequeña y no se sometió a una prueba de significancia. En la prueba reservada, la MLP obtiene F1 macro 0.5008 y exactitud de 50.90\,\%. Random Forest alcanza F1 macro 0.5577 y exactitud de 56.76\,\% en esos mismos juegos. La app carga la MLP según la regla fijada de selección por validación cruzada.

La matriz de la MLP, en orden bajo, medio y alto para filas reales y columnas predichas, es:
\begin{equation}\begin{pmatrix}40&17&10\\31&23&26\\10&15&50\end{pmatrix}.\end{equation}
La clase media recupera 23 de 80 casos, 28.75\,\%. La comparación utiliza una prueba histórica que el equipo ya había observado en corridas anteriores. Haría falta una muestra externa para medir generalización prospectiva.
\subsection{Interpretación y revisión del entrenamiento}
La web muestra la importancia por reducción de impureza de Gini de Random Forest, el bosque incluido en la comparación. Se suman las contribuciones de las columnas codificadas de cada variable original. La importancia describe las divisiones aprendidas por ese bosque y depende de la codificación y del número de atributos disponibles por variable. La MLP se revisa con su matriz, casos de prueba y escenarios. Los CSV de permutación se conservan como diagnóstico complementario del modelo activo.
""")
tabla('modelo_importancia_gini.csv',['variable','importancia'],['Variable','Importancia relativa'],'Importancia agrupada por variable original en Random Forest.',{'importancia':lambda x:f'{float(x):.2%}'})
fig('gini_web.png','Importancia de Gini del bosque comparado en la página Modelo.', '.48')
tabla('revision_predicciones/busqueda_resumen.csv',['candidato','f1_macro_cv','recall_medio_cv'],['Candidato','F1 CV','Recall medio CV'],'Auditoría histórica con el bosque original y siete variantes, usando únicamente entrenamiento.',{'f1_macro_cv':lambda x:f'{x:.4f}','recall_medio_cv':lambda x:f'{x:.4f}'})
texto(r'''Se hicieron ochenta ajustes, ocho candidatos por diez pliegues, variando mínimo por hoja, ponderación y número de variables por división. El criterio previo de sustitución exigía al menos 0.01 de mejora en F1 macro y superioridad en seis pliegues. Ninguna de esas variantes superó al bosque de referencia de esa revisión. La MLP se incorporó después como familia adicional.

La búsqueda amplía la exploración sobre los mismos pliegues y no es una CV anidada. La prueba histórica ya fue observada. Por ello no afirmamos que estas medias midan mejora prospectiva ni presentamos un entrenamiento nuevo como mejor solo por haberlo ejecutado.
\section{Corridas gráficas y contraste con Weka}
Weka Explorer 3.8.7 es la herramienta de la materia utilizada para contrastar clasificación y clustering \parencite{frank2016weka,wekaweb}. Se conservaron las salidas completas y capturas de seis corridas. No se atribuyen a Orange los resultados de Weka.

La clasificación usa 892 instancias y 53 atributos, incluida nivel\_popularidad nominal, con diez pliegues. Las cuatro matrices se recalcularon: cada una suma 892 y sus diagonales reproducen la exactitud mostrada por el programa. El F1 macro se obtiene del promedio simple de F Measure por clase impreso; el ponderado se toma de Weighted Avg salvo ZeroR, donde los valores no definidos se resuelven desde la matriz y se identifican como calculados.
''')
filas=json.loads((R/'revision_predicciones/weka_recalculado.json').read_text());texto(r'\begin{table}[htbp]\centering\caption{Clasificación en Weka sobre 892 casos.}\begin{tabular}{lrrr}\toprule Modelo&Exactitud (\%)&F1 macro&F1 ponderado\\\midrule'+'\n'+''.join(esc(f['modelo'])+f" & {f['exactitud_pct']:.4f} & {f['f1_macro_promedio_mostrado']:.4f} & {f['f1_ponderado']:.4f}"+r'\\'+'\n' for f in filas)+r'\bottomrule\end{tabular}\end{table}')
fig('RandomForest.png','Evidencia de la corrida gráfica de RandomForest en Weka; incluye resumen, métricas por clase y matriz.', '.44')
texto(r'''RandomForest fue el mejor de las cuatro corridas, con 477 aciertos. Su recall de medio fue 0.360, lo que coincide cualitativamente con la dificultad de la clase central en Python. Sin embargo, no se debe comparar directamente su 53.4753\,\% con el 56.76\,\% de prueba de la app: son poblaciones y protocolos distintos.

La comparación de enlace de Python usa los mismos 892 registros y 52 atributos numéricos exportados. Allí Random Forest obtiene 54.8206\,\% y F1 macro 0.5442. Las particiones Java y sklearn no son idénticas, la semilla de CV de la sesión Weka no se recuperó, y los algoritmos difieren: J48 no es CART; Weka NaiveBayes no garantiza estimadores numéricos iguales a GaussianNB. Weka RandomForest usa cien árboles y semilla del estimador uno, frente a cien y 42 en el enlace de Python.

Además, el preprocesamiento de los archivos exportados ocurre antes de la CV de enlace. Ese contraste sirve para comparación descriptiva entre herramientas, pero no sustituye el protocolo de producción con categorías e imputaciones locales por pliegue. El archivo comparativo conserva también evaluaciones de Python sobre 1,117 y 1,114 casos, identificando cada universo.

En SimpleKMeans se usaron dos grupos y semilla 42. Se obtuvieron 477 y 410 casos tras nueve iteraciones; en Python fueron 465 y 422. Los centros de Weka son positivos en las seis variables para el primer grupo y negativos para el segundo, compatibles con una separación por magnitud conjunta. La suma de cuadrados de Weka, 76.6310, no se compara con la de Python como si ambas configuraciones de distancia fueran idénticas.
''')
fig('kmeans_resultado.png','Salida gráfica de SimpleKMeans en Weka. Los centroides corresponden a las variables exportadas transformadas.', '.55')
texto(r'''Weka DBSCAN, con eps 1.666296 y minPoints doce, agrupó los 887 casos en un solo grupo sin ruido. Python dejó veintiún puntos como ruido. Compartir parámetros nominales no demuestra equivalencia de la distancia interna de EuclideanDistance y la implementación de sklearn. No se modificaron resultados ni se ajustó eps para forzar coincidencia.
''')
fig('dbscan_resultado.png','Salida original de DBSCAN en Weka. Un grupo dominante no demuestra múltiples segmentos de mercado.', '.52')
texto(r'''Orange no produjo evaluaciones utilizables. Hubo cierres en Qt/Cocoa al emplear selectores; se probaron instalación local, recuperación y reinicio del lienzo, importación CSV y TAB y un lanzador con selectores Qt. El cierre de esta vía se documentó como desviación del plan. Power BI no se utilizó. La corrida MLP se realizó en Python.
\section{Aplicación y demostración}
La web se implementó en Streamlit con cuatro páginas. Inicio presenta alcance, límites y consulta del catálogo. Exploración ofrece señales, brechas y perfiles; Predicción recibe atributos crudos y muestra la clase y sus probabilidades; Modelo documenta resultados por algoritmo, errores por clase y el diagnóstico de ausencias. El artefacto incluye su preprocesamiento y los vecinos se calculan exclusivamente en el espacio predictivo de entrenamiento.

El formulario utiliza géneros, organización, década y notas. No solicita Plays ni listas de interés porque serían las señales con las que se construyó la respuesta. Las pruebas comparan sus salidas con el Pipeline y usan el orden real de clases; una inversión entre el orden de las probabilidades y el de las etiquetas habría producido una interfaz errónea aun con un buen modelo.
''')
fig('dashboard_interactivo.png','Dashboard con filtros e indicadores de la consulta.', '.48')
fig('comparacion_mlp.png','Comparación de los cinco candidatos con puntos y segmentos de desviación estándar en CV.', '.48')
texto(r'''Exploración incluye filtros por género, década y calificaciones. El dashboard actualiza indicadores y la selección de puntos de la dispersión acota la tabla y el CSV. El selector de agrupamiento ofrece K-Means y Ward. El dendrograma resume el ajuste completo y el mapa PCA responde a los filtros de la consulta. Pearson, Spearman y la corrección de comparaciones múltiples quedan en la sección complementaria de brechas.

La web conserva la identidad azul marino, morado, cian y dorado. Se ajustaron títulos, etiquetas y anchos para escritorio y pantallas estrechas. La gráfica de comparación usa puntos para las métricas y segmentos de una desviación estándar para el F1 de CV.

Se corrigió también el mínimo visual artificial de dos por ciento en las barras de probabilidad y la etiqueta que confundía una organización no frecuente con un estudio independiente. Los inputs validan escalas y dejan los nulos a la imputación entrenada. Las probabilidades no están calibradas y no se presentan como posibilidades actuariales de éxito.

La aplicación se entrega para ejecución local con \texttt{streamlit run app.py} desde Final. No se desplegó en Community Cloud ni se subió el dataset a GitHub por instrucción del usuario. La demo local satisface la comprobación funcional, pero no equivale a una publicación accesible públicamente.
\section{Plan real frente a la línea base}
La línea base del anteproyecto v2.0 programaba actividades del 1 de octubre al 25 de noviembre de 2026. El equipo declara que las actividades técnicas realizadas cumplieron el calendario previsto. La tabla contrasta ese plan con los productos disponibles y las desviaciones de alcance documentadas. No se asignan fechas exactas de terminación porque no se cuenta con un registro por actividad; la entrega y exposición académicas se distinguen de la ejecución técnica.
\begin{longtable}{p{.22\textwidth}p{.19\textwidth}p{.49\textwidth}}
\caption{Línea base frente a evidencia disponible al 11 de noviembre de 2026.}\\\toprule Actividad & Línea base & Estado real y justificación\\\midrule\endfirsthead
Actividad&Línea base&Estado real y justificación\\\midrule\endhead
Anteproyecto y revisión & 1--5 octubre & Documento v2.0 conservado como antecedente; auditorías posteriores revisaron su alcance. No se reconstruye su fecha de terminación.\\
Limpieza y validación & 6--15 octubre & Scripts, dataset y log disponibles. Se recibe un maestro ya curado y se auditan decisiones heredadas.\\
EDA y correlaciones & 15--29 octubre & Tablas y figuras ejecutadas. Se distingue asociación de brecha y se exige cobertura mínima por grupo.\\
Clustering e interpretación & 29 octubre--10 noviembre & K-Means y DBSCAN quedaron documentados en Python y Weka. La vista principal compara K-Means con Ward.\\
Clasificación & 5--11 noviembre & Cinco candidatos evaluados. Se incorporó la MLP prevista y se seleccionó por validación cruzada.\\
Arquitectura y web & 8--16 noviembre & Web funcional comprobada al corte, anterior al fin planeado; no se atribuyen horas de adelanto sin bitácora temporal completa.\\
Despliegue público & 16--18 noviembre & Cancelado por preferencia de mantener datos y modelos locales; demo en localhost.\\
Evaluación en Orange & Durante modelado & Descartada por cierres; Weka sí conserva seis corridas gráficas.\\
Documento y revisión & 10--24 noviembre & Integración al corte actual con evidencia y bibliografía. No se afirma entrega formal al profesor.\\
Entrega y demo & 25 noviembre & Fecha planificada; ejecución local verificada, presentación académica aún no acreditada.\\\bottomrule
\end{longtable}
Las principales desviaciones no fueron simples cambios de calendario: se sustituyó el target de perfil de cluster por terciles de popularidad, se corrigió la procedencia de notas y se recalculó el objetivo dentro de la validación. También se abandonó Orange y se mantuvo la app local. Estos ajustes reducen el alcance respecto de promesas iniciales, pero hacen que lo reportado sea comprobable.
\section{Evaluación de los objetivos y discusión}
El objetivo de inspección se cumple con un esquema comprobado, log de preparación, pruebas y conservación del maestro. La existencia de tres conflictos históricos impide afirmar que todos los registros tengan verificación semántica externa. Se conserva esa incertidumbre en la elegibilidad en vez de escoger el máximo o promediar variantes de forma arbitraria.

El objetivo de relaciones se cumple con Pearson, Spearman, tamaños y p-valores segmentados. La hipótesis de coincidencia perfecta entre comunidad y prensa no se sostiene. Tampoco puede concluirse que un género sea mejor oportunidad comercial por su correlación o por su brecha media: esas medidas no evalúan demanda no satisfecha, competencia ni ingresos.

K-Means y Ward produjeron dos grupos. Los tres índices internos favorecen K-Means en el mismo espacio de datos. Los grupos resumen diferencias de actividad, interés y recepción en esta muestra.

El clasificador supera a la referencia en la partición disponible, pero sigue confundiendo especialmente la clase media. Su etiqueta es un tercil artificial y depende de una referencia histórica del catálogo. Una predicción no puede comprobarse contra ventas ni contra el futuro solo porque el formulario funcione; son validaciones distintas.

La propuesta propia integra control de procedencia, objetivo local, agrupación por título, inferencia cruda y pruebas de interfaz. Esto aporta trazabilidad respecto de una corrida aislada. Aun así, la CV no anidada y la ausencia de validación externa limitan cualquier comparación predictiva más fuerte.
\section{Conclusiones}
El análisis confirma que no conviene reducir la situación de un videojuego a una sola cifra. Las notas resumen recepción, Plays aproxima alcance registrado y las listas aportan interés pendiente. Al separarlas observamos una asociación moderada entre usuarios y prensa y diferencias entre grupos, sin convertirlas en explicaciones causales.

K-Means ofrece una síntesis interpretable de dos niveles conjuntos de actividad y recepción, pero no demuestra mercados naturales. DBSCAN no generó una segmentación múltiple útil bajo el protocolo fijado. Conservar ese resultado, y la diferencia de ruido entre Weka y Python, permite explicar lo que cada herramienta produjo sin acomodarlo a una expectativa.

La clasificación funciona de manera reproducible y supera a Dummy, pero su rendimiento es moderado y la clase media conserva baja recuperación. La MLP ganó por el criterio de CV fijado y Random Forest logró el mayor F1 en la prueba reservada. La evidencia apoya distinguir selección, desempeño en prueba y generalización a datos nuevos.

La web convierte el análisis en una demostración consultable y mantiene visibles los límites de las estimaciones. La ausencia de Metacritic puede alterar mucho una respuesta y requiere cautela. Para estudiar nuevos lanzamientos o rentabilidad necesitaríamos una muestra temporal externa, métricas comerciales observadas, control de plataforma y fecha, y un diseño específico para esa pregunta.

Por tanto, resolvemos la exploración de recepción y popularidad relativa dentro del catálogo y entregamos una herramienta local verificable. No demostramos reducción de pérdidas ni capacidad para anticipar éxito comercial de juegos como servicio. La conclusión se limita deliberadamente a la evidencia que tenemos.
\section{Reproducibilidad y alcance de la verificación}
El repositorio organiza original en data/raw, derivados en data/clean, código en src, artefactos en models, pruebas en tests y evidencias en reports. Los scripts usan pathlib y semilla 42 cuando el método dispone de aleatoriedad. La carpeta de este documento copia figuras y tablas para poder compilar sin rutas absolutas ni conexión a los directorios originales.

Se aprobaron 102 pruebas en la ejecución completa más reciente de la suite; la revisión específica anterior de inferencia, modelo, pipeline y visualización incluyó 39 pruebas. Las 222 predicciones almacenadas coinciden con el artefacto; las probabilidades son válidas y los vecinos contienen solo IDs de entrenamiento en el mismo espacio. Los hashes del manifiesto vinculan los resultados vigentes con sus entradas y artefactos. Esto comprueba integridad e implementación, no la verdad externa de cada calificación.

El informe se puede compilar con \texttt{latexmk -pdf main.tex}. El manifiesto local identifica hashes de las evidencias copiadas. La bibliografía distingue documentos metodológicos y fuentes de software de las mediciones propias del proyecto. La consulta al sitio de Kaggle confirma su identificación, pero no sustituye el archivo local por una versión actual del servicio.

La documentación y el código recibieron apoyo de asistentes de inteligencia artificial, incluidas operaciones gráficas autorizadas y revisión automatizada. Los resultados se verificaron contra archivos y pruebas; no se presenta esa asistencia como validación humana independiente de cada dato. La responsabilidad académica y la aprobación final corresponden al equipo autor.
\appendix
\section{Correspondencia con la rúbrica}
\begin{longtable}{p{.25\textwidth}p{.65\textwidth}}\toprule Rubro& Evidencia en el documento\\\midrule
Objetivo & Sección 2: objetivo general delimitado y seis objetivos verificables.\\
Contexto & Sección 3: origen, maestro curado, unidad analítica, escalas y sesgos.\\
Estrategia & Sección 4: CRISP-DM y función de herramientas.\\
Expectativas & Sección 2: criterios comprobables y alcance excluido.\\
Plan baseline y real & Sección 11: ventanas originales, evidencia al corte y desviaciones.\\
Metodología & Secciones 5--8: preparación, relaciones, clustering y clasificación.\\
Herramientas y propuesta & Secciones 8--10: Python, corridas Weka y demo local; Orange sin resultados.\\
Resultados y conclusiones & Secciones 6--9 y 12--13: resultados positivos, negativos y límites.\\
Fuentes & Bibliografía APA y referencias internas a evidencias.\\\bottomrule\end{longtable}
\section{Guion reproducible de la demostración}
\begin{enumerate}
\item Abrir Inicio y explicar que el maestro tiene 1,117 registros y el antecedente 1,512; mostrar la limitación de ventas.
\item En Exploración, cambiar Plays a Wishlist y distinguir asociación de brecha. Identificar el tamaño de pares del grupo consultado.
\item En Modelo, leer la matriz: medio tiene 23 aciertos de 80. Explicar por qué esto limita una exactitud global moderada.
\item En Predicción, probar el formulario con la MLP. Usar los valores de la tabla de escenarios para reproducir S2 y S5 y comparar qué sucede al ocultar Metacritic.
\item En Exploración, alternar K-Means y Ward, revisar el dendrograma y explicar la comparación de índices.
\item Abrir las capturas originales de Weka y contrastar 892 casos de CV con 222 de prueba de producción. No atribuir silhouette de Python ni resultados a Orange.
\end{enumerate}
\section{Fuentes locales y trazabilidad}
La inspección y limpieza están en reports/inspeccion.md y limpieza\_log.md. Las relaciones, perfiles y sensibilidad se conservan en reports/clustering.md y sus CSV. Las métricas de producción están en models/metadata.json y reports/modelo\_comparacion.csv. El contraste entre herramientas está en reports/tables/comparativo\_herramientas.csv. Las seis corridas y capturas están en reports/weka y su respaldo ZIP verificado. La revisión adicional de predicción se conserva en reports/revision\_predicciones, incluyendo auditoria.json, decision.json y la bitácora unificada de esa carpeta.

Los nombres completos se conservan en el manifiesto y las tablas copiadas. No se atribuyen nuevas corridas a las capturas históricas. El PDF de criterios del profesor se adjunta como evidencia/rubrica\_proyecto.pdf y se utiliza como guía de cobertura, no como fuente de mediciones.
\section{Vinculación con las presentaciones de la materia}
El proyecto aplica la preparación y exploración de datos de Descubrimiento de Conocimiento, y el dashboard como capa de consulta de Arquitectura. Del Proceso de Minería de Datos se incorporaron Naive Bayes, CART, Random Forest, MLP, K-Means, Ward y PCA. Las métricas de clasificación y agrupamiento siguen los ejemplos de Evaluación de MD. La gráfica de Gini sigue el ejemplo del bosque en Evaluación de MD, p.~66. Ward se describe en las pp.~101--107 y la comparación interna de agrupamientos en las pp.~108--115. Las páginas corresponden al orden de los archivos PDF. La visualización y explicación de límites retoman Aplicación de la Minería de Datos.
\section{Capturas actuales de la aplicación}
\begin{figure}[htbp]\centering\includegraphics[width=\linewidth]{figuras/ward_web.png}\caption{Dendrograma en la vista de agrupamiento del dashboard.}\end{figure}\FloatBarrier
\nocite{chaki2023popular,chapman2000crisp,pedregosa2011scikit,mckinney2010pandas,frank2016weka,ester1996dbscan}
\printbibliography[heading=bibintoc,title={Referencias}]
\end{document}
''')
(D/'main.tex').write_text('\n'.join(partes))
