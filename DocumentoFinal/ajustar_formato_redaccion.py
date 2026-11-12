"""Restaura la plantilla del anteproyecto y añade discusión verificable de escenarios."""
from pathlib import Path
import json,re,runpy
D=Path(__file__).resolve().parent;P=D.parent/'Proyecto'
runpy.run_path(str(D/'generar_documento.py'))
s=(D/'main.tex').read_text();body=s.split(r'\section*{Resumen}',1)[1]
body=r'\section*{Resumen}'+body
body=body.replace(r'\tableofcontents\clearpage','')
# El preámbulo se toma del anteproyecto, no de una plantilla aproximada.
pre=(P/'main.tex').read_text().split(r'\begin{document}',1)[0]
pre+=r'\usepackage{caption}\captionsetup[table]{skip=8pt}'+'\n'
inicio=r'''\begin{document}
\hypersetup{pageanchor=false}
\begin{titlepage}\input{Portada.tex}\end{titlepage}
\newpage
{\makeatletter\let\ps@plain\ps@indice\makeatother
\pagestyle{indice}\thispagestyle{indice}\hypersetup{linkcolor=black}\tableofcontents\thispagestyle{indice}}
\newpage\setcounter{page}{1}\hypersetup{pageanchor=true}\singlespacing
'''
port=(P/'Portada.tex').read_text().replace('Anteproyecto','Proyecto final').replace('Análisis del mercado de videojuegos mediante minería de datos','Análisis de recepción y popularidad de videojuegos mediante minería de datos').replace('Fecha de Entrega:','Fecha de corte:').replace('30 de Septiembre del 2026','11 de noviembre de 2026').replace('Versión 2.0 -- actualizada el 8 de noviembre del 2026','Versión final revisada -- evidencia al 11 de noviembre de 2026').replace('[1cm]','[0.45cm]').replace('\\Huge','\\LARGE')
(D/'Portada.tex').write_text(port)
# Se conserva la organización de inicio del anteproyecto.
head,rest=body.split(r'\section{Introducción y problemática}',1)
blocks=re.split(r'(?=\\section\{)',r'\section{Introducción y problemática}'+rest)
blocks=[b for b in blocks if b]
intro,objs,ctx,est=blocks[:4]
objs=objs.replace('Objetivos y expectativas','Objetivos del proyecto');ctx=ctx.replace('Contexto del conjunto de datos','Contexto del proyecto');est=est.replace('Estrategia y metodología aplicada','Estrategia a seguir');intro=intro.replace('Introducción y problemática','Problemática a atender')
body=head+objs+ctx+est+intro+''.join(blocks[4:])
# Ajustes de redacción guiados por la explicación continua del anteproyecto.
reemplazos={
'En este proyecto analizamos la recepción y popularidad relativa de los videojuegos a partir de registros de Backloggd y notas de prensa incorporadas al archivo curado. Partimos de un problema: una calificación alta no equivale necesariamente a una comunidad grande, y el interés pendiente tampoco equivale a ventas. Por eso distinguimos las notas, la actividad acumulada y las listas de interés antes de construir perfiles y un clasificador.':
'Este proyecto tiene como finalidad analizar de forma práctica cómo se relacionan la opinión de los jugadores, la crítica especializada y la popularidad que alcanza un videojuego dentro de Backloggd. La idea surge porque normalmente se utiliza una calificación para hablar del éxito de un título, aunque esa nota no nos dice cuántas personas lo juegan ni cuántas tienen interés en hacerlo. Para atender esta situación se revisaron las calificaciones y las métricas de interacción por separado, después se buscaron grupos de juegos similares y finalmente se construyó una aplicación que permite consultar los resultados y probar un modelo supervisado.',
'Analizar la relación entre recepción y popularidad relativa en el catálogo curado de videojuegos mediante correlaciones, agrupamiento y clasificación supervisada, y presentar resultados verificables en una aplicación local de Streamlit.':
'Aplicar técnicas de minería de datos sobre el catálogo de videojuegos contenido en games\\_curated.csv para analizar la diferencia entre la valoración de la comunidad y la crítica especializada, reconocer cómo se distribuyen la actividad y el interés de los jugadores, encontrar grupos de títulos con características similares y estimar su nivel de popularidad relativa mediante un modelo supervisado. Los resultados se integran en una aplicación web local para que puedan explorarse y contrastarse con ejemplos concretos.',
'El punto de partida fue entender qué significa que un videojuego tenga éxito. En una plataforma social podemos encontrar un juego con buena recepción y pocos registros de actividad, o un juego muy conocido cuya calificación no sea particularmente alta. Si juntamos estas situaciones en una sola medida, perdemos la diferencia entre calidad percibida, alcance e interés.':
'La problemática principal es que el éxito de un videojuego no se puede explicar con un solo indicador. Por ejemplo, un título puede tener una calificación alta porque quienes lo jugaron quedaron satisfechos, pero eso no significa que haya llegado a una comunidad numerosa. También puede suceder lo contrario: un juego conocido puede acumular muchos registros de actividad y al mismo tiempo recibir opiniones divididas. Si únicamente revisamos la nota, estaríamos dejando fuera una parte importante de lo que sucede con ese videojuego.',
'Lo que sí podemos atender es la falta de una lectura conjunta de los indicadores disponibles. Contrastamos la recepción de usuarios y prensa, distinguimos actividad e interés y evaluamos si los atributos de un juego permiten estimar su posición relativa en este catálogo. La finalidad es apoyar la exploración y formular preguntas mejor delimitadas, no sustituir un estudio de mercado.':
'Por esta razón, el proyecto se concentró en utilizar los datos que sí teníamos disponibles: las opiniones, los registros de juego y las listas de interés. Esto nos permite comparar situaciones diferentes dentro del catálogo y revisar si un modelo puede reconocerlas a partir del género, la organización, la década y las calificaciones. El resultado puede servir para orientar una exploración del mercado, aunque por sí solo no reemplaza un estudio de ventas o rentabilidad.',
'Los faltantes de notas permanecen ausentes en los análisis descriptivos. La imputación por mediana se reserva al modelo y se ajusta únicamente con su entrenamiento. La nota crítica analítica usa la procedencia documentada en el maestro y deja fuera las estimaciones propias. Esto valida coherencia interna de etiquetas, no una comprobación externa de cada Metascore.':
'Una decisión importante fue no llenar las calificaciones faltantes durante el análisis descriptivo. Si asignábamos una nota promedio antes de comparar usuarios y prensa, estaríamos agregando información que no estaba realmente en el archivo. Por eso las correlaciones utilizan únicamente los pares disponibles. La mediana se utiliza después, cuando el modelo necesita una entrada completa, y se calcula solamente con los datos de entrenamiento. De la misma forma, las notas marcadas como estimaciones propias no se tratan como una opinión independiente de la prensa.',
'Un juego con muchas listas pendientes puede tener demanda potencial dentro de la plataforma, pero también puede acumular espera sin convertirse en actividad. Por esta razón evitamos llamar éxito comercial a un valor alto del índice.':
'Esto quiere decir que aparecer en muchas listas no garantiza que esas personas finalmente jueguen el título. El interés pendiente y la actividad ya registrada nos hablan de momentos distintos. Por eso un índice alto se interpreta como una posición alta dentro del catálogo y no como una cantidad de ventas.',
'La clase medio solo recupera 27 de 80 casos, 33.75\\,\\%. Por ello una cifra global moderada no significa que identifique correctamente todos los niveles. La cercanía entre las fronteras artificiales de terciles es una posible explicación del solapamiento, no una causa demostrada por el experimento.':
'Al revisar la matriz se observa que la clase media es el problema más claro del modelo: de ochenta juegos que realmente pertenecían a ese nivel, solamente veintisiete fueron identificados correctamente. Los demás se repartieron entre bajo y alto. Esto nos muestra que no era suficiente presentar únicamente la exactitud general, porque esa cifra podía ocultar una dificultad importante. Una explicación posible es que los juegos cercanos a las fronteras de los terciles compartan atributos con ambos extremos, aunque este experimento no permite demostrar que esa sea la causa.',
'La clasificación funciona de manera reproducible y supera a Dummy, pero su rendimiento es moderado y la clase media conserva baja recuperación. Las siete variantes adicionales no mejoraron el F1 de CV, por lo que mantener el modelo existente fue una decisión sustentada en resultados, no falta de entrenamiento. Más complejidad no habría sido una mejora por sí misma.':
'En cuanto a la predicción, sí se logró construir un modelo que supera a la referencia mayoritaria, pero los resultados no permiten decir que pueda decidir por sí solo qué videojuego tendrá éxito. La clase media siguió siendo difícil y los escenarios mostraron que algunas respuestas cambian bastante cuando falta la nota de prensa. También se entrenaron siete variantes adicionales del bosque y ninguna mejoró el criterio de validación utilizado. Por eso se conservó el modelo que ya teníamos, en lugar de presentar como mejora un cambio que no estaba respaldado por sus resultados.',
'El análisis confirma que no conviene reducir la situación de un videojuego a una sola cifra. Las notas resumen recepción, Plays aproxima alcance registrado y las listas aportan interés pendiente. Al separarlas observamos una asociación moderada entre usuarios y prensa y diferencias entre grupos, sin convertirlas en explicaciones causales.':
'Después de realizar el análisis, podemos concluir que la idea inicial de revisar varios indicadores sí fue útil. Las calificaciones nos ayudaron a entender la recepción, mientras que Plays, Backlogs y Wishlist mostraron diferencias de alcance e interés que no se veían solamente con una nota. La relación entre usuarios y prensa fue positiva, aunque moderada, por lo que tampoco sería correcto asumir que ambas opiniones siempre coinciden.',
'El objetivo de perfiles se cumple de forma descriptiva con dos grupos K-Means. DBSCAN aporta un resultado negativo para segmentación múltiple, que también es un hallazgo. La silhouette moderada y la dominancia de magnitud conjunta aconsejan no convertir los nombres de los grupos en categorías naturales o permanentes del mercado.':
'En la parte de agrupamiento se obtuvieron dos perfiles con K-Means que permiten resumir diferencias de actividad, interés y recepción. Sin embargo, DBSCAN no encontró varios segmentos útiles con la configuración establecida. Esto también forma parte del resultado: el hecho de aplicar un algoritmo no obliga a que aparezcan los grupos que esperábamos. Los nombres de los perfiles se utilizaron para explicar sus promedios y no para afirmar que todo el mercado se divide de esa manera.'
}
for a,b in reemplazos.items():body=body.replace(a,b)
# Lectura prudente de p-valores que alcanzan el límite numérico.
body=body.replace('pares completos para cada comparación.', 'pares completos para cada comparación. Un p impreso como cero corresponde al límite numérico del cálculo, no a una probabilidad matemática exactamente nula.')
# Bloque nuevo con casos hipotéticos y errores reales, elaborado de datos del artefacto.
hip=json.loads((D/'evidencias/escenarios/hipoteticos.json').read_text());real=json.loads((D/'evidencias/escenarios/contraejemplos.json').read_text())
def e(x):return str(x).replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')
casos=r'''\section{Escenarios de predicción y contrastación del modelo}\label{sec:escenarios}
\subsection{Qué queríamos comprobar con los escenarios}
Después de revisar la exactitud general, todavía quedaba una pregunta importante: ¿cómo se comporta el modelo cuando cambiamos las características de un videojuego? Para responderla planteamos situaciones concretas y mantuvimos fijas las demás entradas. La intención no fue buscar ejemplos que hicieran ver bien al modelo, sino mostrar qué información parece pesar en sus respuestas y en qué situaciones conviene cuestionarlas.

Se separaron dos tipos de prueba. Los escenarios hipotéticos permiten revisar sensibilidad, pero no tienen una clase real observada; por eso no pueden demostrar por sí solos que una respuesta sea correcta o incorrecta. Para refutar predicciones concretas también recuperamos juegos del conjunto de prueba y comparamos la clase estimada con la clase calculada a partir de sus señales de popularidad. Estos ejemplos ya forman parte de la evaluación histórica: no constituyen una muestra nueva ni una nueva medición del rendimiento.
\subsection{Escenarios con cambios controlados}
El escenario de referencia utiliza Adventure y RPG, organización Otro y década de 2020. En S1 a S5 únicamente se modifican las calificaciones y la presencia de prensa. S6 cambia la organización a Nintendo; S7 cambia la década a 1980; S8 utiliza Shooter. Se trata de comparaciones de entradas del mismo modelo, no de afirmaciones causales sobre esas organizaciones o géneros.
\begin{longtable}{p{.08\textwidth}p{.28\textwidth}p{.11\textwidth}p{.11\textwidth}p{.12\textwidth}p{.14\textwidth}}
\caption{Escenarios hipotéticos calculados con el Pipeline guardado. La última columna muestra la mayor probabilidad, sin calibrar.}\\\hline
Caso&Situación&Rating&Prensa&Predicción&Probabilidad\\\hline\endfirsthead
Caso&Situación&Rating&Prensa&Predicción&Probabilidad\\\hline\endhead
'''
for h in hip:
 prob=max(h['p_alto'],h['p_medio'],h['p_bajo']);crit='Ausente' if h['metacritic'] is None else str(h['metacritic'])
 casos+=' & '.join(map(e,[h['id'],h['escenario'],h['rating'],crit,h['prediccion'],f'{prob:.1%}']))+r'\\\hline'+'\n'
casos+=r'''\end{longtable}
La tabla muestra cómo responde la MLP cuando se modifican las notas y los demás atributos. S2, con ambas notas altas, estima popularidad media. S5 conserva el Rating de S2 y oculta Metacritic. En ese caso se estima la clase baja y se usa la mediana aprendida para sustituir el faltante. Los escenarios S6 a S8 ilustran la sensibilidad a organización, década y género. Las probabilidades son salidas del modelo y carecen de calibración.

\begin{figure}[htbp]\centering\includegraphics[width=\linewidth]{figuras/sensibilidad_escenarios.png}\caption{Veinticinco combinaciones de Rating y Metacritic con el resto de atributos fijos. La etiqueta es la clase estimada y el color muestra la probabilidad no calibrada de alto.}\end{figure}\FloatBarrier
\subsection{Contraejemplos con juegos del conjunto de prueba}
Para no quedarnos solamente con escenarios inventados, seleccionamos un acierto y un error por cada clase real. Dentro de cada caso se tomó el registro con mayor probabilidad máxima del modelo. Esta selección es posterior a observar las predicciones y busca ilustrar sus límites; no sirve para estimar una nueva exactitud ni representa una muestra aleatoria de casos.
\begin{longtable}{p{.35\textwidth}p{.12\textwidth}p{.12\textwidth}p{.12\textwidth}p{.15\textwidth}}
\caption{Aciertos y errores reales frente al objetivo de popularidad del proyecto. No se usa ventas como verdad de referencia.}\\\hline
Juego&Clase real&Predicción&Resultado&Probabilidad\\\hline\endfirsthead
Juego&Clase real&Predicción&Resultado&Probabilidad\\\hline\endhead
'''
for h in real:casos+=' & '.join(map(e,[h['titulo']+' (ID '+str(h['id_juego'])+')',h['real'],h['prediccion'],'Acierto' if h['acierto'] else 'Error',f"{h['probabilidad_maxima']:.1%}"]))+r'\\\hline'+'\n'
casos+=r'''\end{longtable}
Los tres errores de la tabla muestran que una probabilidad máxima alta puede acompañar una clasificación equivocada. La comparación usa los terciles de entrenamiento y los conteos observados de Backloggd. Los tres aciertos sirven para contrastar cómo se comporta el mismo modelo cuando coincide con esa etiqueta.

Para estos registros se conservaron ID, listas completas de género y organización, calificaciones, década, conteos y probabilidades. La comprobación numérica se hizo directamente con las entradas crudas del Pipeline. No se presenta una captura del formulario como réplica exacta de un registro con varias organizaciones o categorías que el formulario no permite seleccionar: esa distinción evita confundir una demostración simplificada con una reproducción del dato real.
\subsection{Qué aprendimos de las pruebas}
Los escenarios permiten cuestionar dos expectativas del planteamiento inicial: una calificación alta no basta para asignar popularidad alta en todos los casos y una probabilidad mayor tampoco garantiza una predicción correcta. La ausencia de prensa, el género y la organización cambian el espacio de entrada, mientras que la clase real depende de actividad e interés observados que deliberadamente no se entregan como predictores.

Por eso la aplicación debe entenderse como una estimación orientativa que ayuda a contrastar situaciones. Los contraejemplos no se utilizaron para volver a escoger parámetros sobre la prueba. La forma adecuada de evaluar una mejora futura sería reservar una muestra temporal nueva y establecer antes los criterios de comparación. Reentrenar hasta que desaparezcan los errores elegidos solo memorizaría una parte de la evaluación que ya conocemos.
'''
# Inserción anterior al plan; las referencias de la rúbrica se corrigen con etiquetas.
capturas = r"""\subsection{Verificación del formulario}
\begin{figure}[htbp]\centering\includegraphics[width=\linewidth,height=.49\textheight,keepaspectratio]{figuras/prediccion_mlp_web.png}\caption{Ejecución del formulario en la web con la MLP activa.}\end{figure}\FloatBarrier
"""
casos = casos.replace(r'\subsection{Contraejemplos con juegos del conjunto de prueba}',capturas+r'\subsection{Contraejemplos con juegos del conjunto de prueba}')
meta=json.loads((D.parent/'Final/models/metadata.json').read_text());c1,c2=meta['definicion_objetivo']['cortes']
senales = r'\subsection{Cómo comprobamos la clase real de los ejemplos}'+'\n'+f'Los cortes de entrenamiento son {c1:.6f} y {c2:.6f}. Bajo corresponde a un índice menor o igual al primer corte; medio supera el primero sin rebasar el segundo; alto supera el segundo. La tabla conserva los conteos y el índice calculado frente a esa referencia, no frente a una referencia ajustada con estos seis casos.\n'
senales += r'\begin{longtable}{p{.1\textwidth}p{.14\textwidth}p{.14\textwidth}p{.14\textwidth}p{.14\textwidth}p{.13\textwidth}}\caption{Señales observadas que permiten contrastar la clase real de los ejemplos. Los ID se corresponden con el archivo de evidencia.}\\\hline ID&Plays&Wishlist&Backlogs&Índice&Clase real\\\hline\endfirsthead ID&Plays&Wishlist&Backlogs&Índice&Clase real\\\hline\endhead'+'\n'
for h in real:
 senales += ' & '.join(map(e,[h['id_juego'],int(h['Plays']),int(h['Wishlist']),int(h['Backlogs']),f"{h['indice']:.4f}",h['real']]))+r'\\\hline'+'\n'
senales += r'\end{longtable}'+'\n'
casos = casos.replace(r'\subsection{Qué aprendimos de las pruebas}',senales+r'\subsection{Qué aprendimos de las pruebas}')
body=body.replace(r'\section{Plan real frente a la línea base}',casos+'\n'+r'\section{Plan real frente a la línea base}')
labels={'Objetivos del proyecto':'objetivos','Contexto del proyecto':'contexto','Estrategia a seguir':'estrategia','Plan real frente a la línea base':'plan','Preparación y control de calidad':'preparacion','Análisis exploratorio y recepción':'eda','Clustering y perfiles del catálogo':'clustering','Clasificación supervisada':'clasificacion','Corridas gráficas y contraste con Weka':'weka','Aplicación y demostración':'web','Evaluación de los objetivos y discusión':'discusion','Conclusiones':'conclusiones'}
for t,l in labels.items():body=body.replace('\\section{'+t+'}','\\section{'+t+'}\\label{sec:'+l+'}')
for a,b in {'Sección 2: objetivo general':'Sección~\\ref{sec:objetivos}: objetivo general','Sección 3: origen':'Sección~\\ref{sec:contexto}: origen','Sección 4: CRISP-DM':'Sección~\\ref{sec:estrategia}: CRISP-DM','Sección 2: criterios':'Sección~\\ref{sec:objetivos}: criterios','Sección 11: ventanas':'Sección~\\ref{sec:plan}: ventanas','Secciones 5--8: preparación':'Secciones~\\ref{sec:preparacion}--\\ref{sec:clasificacion}: preparación','Secciones 8--10: Python':'Secciones~\\ref{sec:clasificacion}--\\ref{sec:web}: Python','Secciones 6--9 y 12--13: resultados':'Secciones~\\ref{sec:eda}--\\ref{sec:weka} y \\ref{sec:discusion}--\\ref{sec:conclusiones}: resultados'}.items():body=body.replace(a,b)
body=body.replace(r'\printbibliography[heading=bibintoc,title={Referencias}]',r'\clearpage\pagestyle{referencias}\printbibliography[heading=bibintoc,title={Referencias}]')
(D/'main.tex').write_text(pre+inicio+body)
