# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/codex_log.md

SHA-256: `a63d3ef391b28ef4347b91659c43e6a051a72573d8f436262f431990d82eecce`

````text

## 2026-11-08T16:28:05-06:00 — Web y preparación de la fase gráfica

1. Se revisó la web de Final conservando el estilo de PruebasMenu/persona5-website-theme. Se sustituyeron enlaces # por rutas reales; los eventos de submenús se delegan para sobrevivir rerenders; se agregaron foco y teclado, padding y adaptación de columnas. Evidencia: reports/tables/web_submenu_modelo.png.
2. En Chrome: Inicio → Horizonte, flecha derecha → Géneros; búsqueda Hades → Horizonte tras el rerender, con panel TEMPORAL LOG visible. Evidencia: reports/tables/web_submenu_tras_filtro.png.
3. En Chrome: menú Modelo → Naive Bayes; actualización correcta de parámetros y métricas. Exploración → DBSCAN por teclado: 866 en núcleo y 21 ruidos. Predicción → ANALIZAR: resultado y cinco vecinos visibles. Evidencia: reports/tables/web_prediccion.png.
4. Se retiraron tiempos de entrenamiento no medidos y conteos de géneros codificados a mano; se aclaró que el catálogo no mide riesgo comercial de GaaS. 87 pruebas aprobadas: reports/tables/pruebas_web.txt. node --check del motor JS y git diff --check sin errores. El detector de diseño señala recursos del tema heredado (bordes/Roboto/animación), conservados por la referencia explícita Persona 5; no es una auditoría exhaustiva de accesibilidad ni una prueba en móvil físico.
5. Se detectó que no existían las entradas solicitadas. Se exportaron clustering.csv (887×6) y clasificacion.csv (892×53, clase al final) en data/export, con procedencia y hashes. No se tocó data/raw. Preparación realizada con Python; ninguna corrida gráfica se ha sustituido por una corrida por código.
6. No se encuentra Orange en /Applications, ~/Applications ni en el entorno del proyecto. Se solicitó autorización o ubicación y se espera respuesta; no se instaló nada. Weka 3.8.6 y Bounce 0.18 ya están en .cache/weka, de la fase CLI anterior. Esa evidencia CLI no se etiquetará como evidencia de Explorer.

### Decisiones de diseño

La delegación de eventos atiende los elementos que Streamlit inserta después de cargar la página; el clic y el teclado activan el mismo panel. Las rutas reales permiten navegar aunque el motor de interacción no se ejecute.

El padding y las columnas flexibles evitan recortes sin sustituir el estilo Persona 5 pedido. Las métricas visibles se mantienen ligadas a los reportes; no se muestran tiempos inventados.

### Que debo verificar manualmente

- Orange: ubicación o autorización para instalar antes de continuar con esa aplicación.
- Parámetros, normalización adicional, clase nominal y definición de F1 en cada interfaz.

## 2026-11-08T16:29:41-06:00 — Incidencia al iniciar Weka GUI

7. Se inició exclusivamente GUIChooser del Weka 3.8.6 ya disponible, con Bounce 0.18. No se ejecutó ningún algoritmo por terminal. Las propiedades user.home y java.util.prefs.userRoot se dirigieron a reports/weka para respetar el límite de escritura. Archivo producido: reports/weka/gui_inicio.log.
8. El arranque informó `Unable to create WEKA_HOME`, `Unable to create packages directory`, `Unable to create native libs directory` y `Unable to create repository cache directory`, bajo reports/weka/.home/wekafiles. Faltaba el directorio contenedor .home elegido para aislar preferencias. También se registró la advertencia de recursos mtj ausentes. La consulta de aplicaciones no encontró una ventana Weka operable.
9. Se detuvo la fase conforme a la regla 5 del usuario. No se creó la carpeta faltante ni se reintentó el arranque después del error. Se envió Ctrl+C al proceso iniciado. No se abrió Explorer ni se realizaron corridas gráficas de K-Means, DBSCAN o clasificación. No se sustituyeron por las salidas CLI anteriores.
10. Orange sigue pendiente de ubicación o autorización de instalación. No hay archivos .ows ni matrices nuevas que puedan acreditarse como resultados de GUI. El comparativo conserva campos de métricas vacíos y notas de estado, sin inventar cifras.

### Reanudación pendiente

Esperar instrucciones del usuario por el error de arranque y respuesta sobre Orange. La corrección propuesta para Weka es crear el contenedor dentro de reports/weka y relanzar GUIChooser; no se efectuó después de la incidencia. Si aparece otra incidencia, detenerse de nuevo según la regla 5.

## 2026-11-08T22:55:57.292Z — Reanudación de Orange desde el disco extraíble

11. El usuario indicó que Orange ya estaba abierto en su disco extraíble. Se seleccionó la aplicación Orange existente, sin instalar ni modificar su aplicación.
12. Se agregó File al lienzo y se abrió por doble clic. La ruta de su conjunto de ejemplo muestra /Volumes/ROGStrix/Aplicaciones/Orange.app. No se ha seleccionado todavía ninguna entrada del proyecto ni ejecutado modelos.
13. File mostró el aviso inicial “Use CSV File Import widget for advanced options for comma-separated files” y el botón “Ok, got it”. Se detuvo la interacción antes de cerrarlo por la regla 5 del usuario. Captura: reports/orange/aviso_inicial.png. Se espera autorización para cerrar el aviso y continuar con File → Select Columns.

## 2026-11-08T22:57:21.118Z — Selección de clasificación e incidencia de recuperación

14. El usuario autorizó cerrar el aviso inicial con “Ok, got it”. Se cerró ese aviso y se abrió el selector de archivos de File.
15. Se seleccionó exclusivamente Final/data/export/clasificacion.csv mediante el diálogo de apertura y se pulsó Open. No se modificó el CSV.
16. Apareció el diálogo “Restore unsaved changes from crash?” con el texto “Orange seems to have crashed at some point.” Se detuvo la interacción conforme a la regla 5, sin restaurar ni descartar sesiones. Captura: reports/orange/dialogo_recuperacion.png. No hay todavía evaluación ni métricas gráficas verificadas.

17. El usuario autorizó pulsar Yes. Se recuperó la sesión y se inspeccionó el lienzo antes de continuar.

## 2026-11-08T16:59:41-06:00 — Recuperación autorizada y pérdida de ventana accesible

18. Se pulsó Yes con autorización explícita. Orange mostró el lienzo Untitled con un único widget File, sin un flujo de evaluación recuperado.
19. Al hacer doble clic en File para inspeccionarlo, el control de la aplicación devolvió `noWindowsAvailable`. No se puede confirmar desde esa respuesta si Orange se cerró o si su ventana dejó de ser accesible. Se detuvo la interacción por la regla 5, sin reabrir ni cambiar el importador.
20. No hay carga del CSV verificada, modelos evaluados, matrices ni archivos .ows nuevos. No se pudo obtener captura de la incidencia porque no había ventana accesible; las capturas previas documentan los avisos anteriores. Las métricas siguen vacías.

## 2026-11-08T17:03:01-06:00 — Intento autorizado con CSV File Import

21. El usuario autorizó reabrir Orange y probar CSV File Import en lugar de File. Se abrió la aplicación existente del disco extraíble y se agregó CSV File Import al lienzo, dejando intacto File.
22. Se abrió Browse filesystem y se seleccionó únicamente data/export/clasificacion.csv. La vista previa mostró las columnas multi-hot y las etiquetas de clase; Import Options mostró Unicode UTF-8, Comma y separador decimal punto. Se confirmó con OK.
23. Al confirmar, el control devolvió `App quit`. Se detuvo la interacción por la regla 5; no se reabrió otra vez. No se pudo verificar la tabla importada ni su clase objetivo. No se obtuvieron evaluación, matrices ni .ows. Tampoco se obtuvo captura posterior, al perderse la aplicación accesible.
24. Como preparación de una alternativa, se creó data/export/clasificacion.tab mediante conversión de formato, sin ejecutar Orange ni modelos por código. Conserva exactamente los 892 registros y 53 columnas del CSV; añade únicamente las dos filas de metadatos del formato TAB: atributos continuos y última columna discreta marcada class. La lectura de vuelta verifica la igualdad de todos los valores de texto con el CSV, que permanece intacto. SHA-256 TAB: aef344720fd3ae26f3de15cb607983beb5da44e289687fc640645ba8c3120130. Este archivo no se ha importado todavía: se espera autorización para cambiar de formato y reabrir Orange.

## 2026-11-08T17:05:39-06:00 — Intento autorizado de formato TAB

25. El usuario autorizó reabrir Orange y probar data/export/clasificacion.tab mediante File. Al abrir la aplicación apareció el mismo aviso de recuperación. Se aplicó Yes conforme a la autorización previa explícita para ese aviso, sin pedirla de nuevo.
26. El lienzo recuperado mostró File y CSV File Import. Al intentar abrir File, antes de abrir un selector o elegir el TAB, el control devolvió `noWindowsAvailable`. Se detuvo por la regla 5 sin nuevos reintentos. No se llegó a cargar ni probar el formato TAB; no se atribuye el fallo al TAB. No hay captura nueva del error al no existir ventana accesible.
27. Se propone, pendiente de autorización, abrir un lienzo vacío sin recuperar los cambios de esa sesión. Elegir No en el diálogo de recuperación descartaría los cambios no guardados del flujo; no se ha pulsado esa opción. La sesión observada solo contiene los dos importadores, sin evaluación ni resultados. No se modificarán archivos originales ni se instalará software.

## 2026-11-08T23:08:58.627Z — Prueba con flujo vacío y TAB

28. El usuario autorizó descartar la sesión y comenzar en blanco. Al seleccionar Orange no había aviso de recuperación; se creó un flujo nuevo mediante Cmd+N y se comprobó visualmente que el lienzo estaba vacío.
29. Se agregó File, se abrió correctamente y se seleccionó exclusivamente Final/data/export/clasificacion.tab. Tras pulsar Open reapareció el diálogo “Restore unsaved changes from crash?”. No se llegó a verificar información de la tabla importada.
30. Se pulsó No conforme a la autorización explícita del usuario. Orange mostró Welcome to Orange. Se detuvo la prueba: la importación tampoco se completó con flujo vacío y formato TAB. Esto no identifica por sí solo la causa técnica del cierre. Captura del estado posterior: reports/orange/inicio_tras_fallo_tab.png. No se realizaron nuevas importaciones ni instalaciones, ni se ejecutaron modelos.

## 2026-11-08T17:17:58-06:00 — Reintento autorizado con instalación local

31. El usuario indicó que instaló Orange localmente y autorizó reintentar. Se localizó /Applications/Orange.app y se seleccionó explícitamente esa copia, sin instalar ni modificar aplicaciones.
32. Se agregó File y se abrió. La interfaz mostró su dataset de ejemplo bajo /Applications/Orange.app/Contents/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/Orange/datasets/titanic.tab, verificando que el widget pertenecía a la copia local, no a la del disco extraíble.
33. Se seleccionó únicamente data/export/clasificacion.tab. Esta vez se confirmó la apertura con Return en lugar de pulsar Open por accesibilidad. El control volvió a devolver `App quit`. No se obtuvo la pantalla de información con 892 registros ni se verificó el target mediante la automatización.
34. Se detuvo la interacción conforme a la regla 5. La instalación local no resolvió el fallo observado; no se identifica aún su causa ni se afirma que falle la carga manual, que el usuario reportó exitosa anteriormente. No hay métricas, matrices ni .ows nuevos. No se consiguió captura posterior porque el control perdió la aplicación accesible.
35. Antes de nuevos reintentos se propone revisar reportes de cierre del sistema en modo de solo lectura. Esto queda pendiente de autorización porque excede el ámbito original de la carpeta del proyecto y las dos aplicaciones. No se han consultado esos reportes ni modificado archivos fuera de las carpetas autorizadas.

## 2026-11-08T17:21:07-06:00 — Diagnóstico autorizado de solo lectura

36. El usuario autorizó revisar reportes de cierre del sistema en modo de solo lectura. Se inspeccionaron cuatro archivos Python-2026-11-08-*.ips que identifican Orange.app. Los cuatro registran SIGSEGV / EXC_BAD_ACCESS en el hilo principal, con liberación Objective-C/NSArray y libqcocoa.dylib. El último identifica la copia local.
37. Se guardaron únicamente resúmenes pertinentes en reports/orange/diagnostico_cierres.json y diagnostico_cierres.md. No se modificaron reportes del sistema. Una consulta de procesos fue bloqueada por el entorno; no se escaló ni se insistió, porque los reportes ya aportaban evidencia.
38. Se verificaron en lectura el lanzador y el punto de entrada de Orange local, y la presencia de AA_DontUseNativeDialogs en los tipos PyQt6 incluidos. Se preparó reports/orange/iniciar_con_dialogos_qt.py como prueba temporal sin instalación. Solo se comprobó su sintaxis; no se ejecutó ni se reanudó la GUI. Pendiente de autorización por la regla 5.

## 2026-11-08T17:23:52-06:00 — Reanudación con Weka solicitada por el usuario

39. El usuario autorizó el lanzador temporal de Orange, pero también solicitó usar Weka en su lugar. Se prioriza Weka Explorer y no se ejecuta por ahora el lanzador de Orange.
40. Como preparación de Weka se crearon los contenedores reports/weka/.home y reports/weka/.preferencias que faltaban en el primer intento. No se instalaron paquetes ni se modificaron datos originales. Las corridas se harán en Explorer, sin sustituirlas por ejecución de algoritmos en terminal.

## 2026-11-08T17:25:41-06:00 — Versión de Weka disponible y selección de instancia

41. La consulta de aplicaciones encontró dos identificadores de GUIChooser: weka.gui y net.java.openjdk.java. La selección de weka.gui abrió una ventana funcional que muestra Weka 3.8.7 y el botón Explorer. Evidencia: reports/weka/gui_chooser_3_8_7.png.
42. Al intentar seleccionar net.java.openjdk.java, el control devolvió Invalid app. La ventana Weka 3.8.7 siguió accesible y se verificó solo en lectura. Se detuvo la navegación conforme a la regla 5. No se atribuye ese error de selección al funcionamiento de Weka.
43. Se envió Ctrl+C únicamente al proceso Java iniciado por esta tarea desde el proyecto, que aún no tenía corridas. Se dejó intacta la ventana funcional identificada como weka.gui. Se espera indicación para continuar con Explorer 3.8.7; esa versión se registraría por separado de la evidencia CLI anterior de 3.8.6. No hay métricas gráficas nuevas.

## 2026-11-08T23:31:57.091Z — Explorer 3.8.7 y carga pendiente

44. El usuario autorizó continuar con Weka 3.8.7. Se abrió Explorer y, desde Preprocess, Open file. Se confirmó que el selector presenta un campo Nombre de archivo y un selector de tipo con CSV data files.
45. Los intentos de introducir la ruta mediante foco, teclado y accesibilidad no cambiaron el campo. La integración indicó cannotClickOffscreenElement al seleccionar opciones del combo y Cannot set a value for an element that is not settable al intentar asignar el campo. Estas son respuestas del controlador, no un error de un algoritmo ni un cierre de Weka. No se cargó otro archivo ni se ejecutaron modelos.
46. Se dejó el selector abierto, sin alterar el dataset. Captura: reports/weka/selector_csv_pendiente.png. Se solicita una carga manual de data/export/clustering.csv (tipo CSV data files) para poder continuar desde Preprocess. La aplicación observada permanece abierta.

## 2026-11-08T17:35:14.110614-06:00 — Verificación al reanudar

47. El usuario indicó continuar después de reportar una carga manual. La ventana accesible de Explorer mostró Relation: None, Instances: None y Attributes: None; no se pudo confirmar la carga reportada en esta ventana. Se abrió el selector y se seleccionó Documents mediante doble clic.
48. Al pulsar Abrir por accesibilidad, el controlador devolvió cannotClickOffscreenElement. La captura muestra que el selector sigue abierto, con formato ARFF y la ruta de Documents, sin dataset importado. Se detuvo por la regla 5, sin ejecutar modelos ni producir métricas. Evidencia: reports/weka/bloqueo_selector_reanudacion.png. Se requiere que el usuario deje visible Explorer con clustering.csv cargado y 887 instancias / 6 atributos para resolver la discrepancia de ventana.

## 2026-11-08T17:47:44.503686-06:00 — Confirmación del lector CSV

49. El usuario solicitó que el agente realizara la carga. La ventana actual era GenericObjectEditor para CSVLoader; se confirmaron sus opciones sin cambiar parámetros. Weka mostró Convert File: CSVLoader failed to load export. Reason: No source has been specified. No se importó el dataset ni se ejecutaron modelos.
50. Se dejó abierto el error y se detuvo por la regla 5. Captura: reports/weka/error_csv_sin_origen.png. Próximo paso propuesto: cerrar el aviso y seleccionar el archivo completo data/export/clustering.csv, sin cambiar datos ni instalar paquetes.

## 2026-11-08T17:49:00.220503-06:00 — Reintento autorizado de selección

51. Se cerró el aviso con Aceptar y se canceló el editor CSVLoader sin cambiar opciones. Se abrió nuevamente Open file. El selector mostraba data, filtro ARFF y como nombre de archivo la ruta de la carpeta export, sin clustering.csv.
52. El intento de enfocar Nombre de archivo por accesibilidad devolvió cannotClickOffscreenElement; el pegado y los atajos posteriores no se ejecutaron. La captura visual confirmó el mismo selector y ruta sin cambios. Se detuvo conforme a la regla 5. No se cargó el CSV ni se ejecutaron algoritmos. La interacción automática con el selector sigue bloqueada.

## 2026-11-08T17:53:02.404186-06:00 — Reintento autónomo y verificación de bloqueos

53. El usuario solicitó resolver los bloqueos conocidos y verificar las corridas hasta completar el objetivo. Se reanudó Weka, se canceló el editor CSVLoader y se abrió Open file. Se logró entrar en export por accesibilidad; se verificó visualmente que ARFF continuaba seleccionado y ocultaba los CSV.
54. Los intentos con foco por accesibilidad, navegación de teclado, pegado, coordenadas y reactivación de la instancia no cambiaron el campo ni el filtro. Los controles inferiores devolvieron cannotClickOffscreenElement. No se verificó importación ni se ejecutó modelo.
55. Se ejecutó el lanzador temporal de Orange ya autorizado, sin instalar ni modificar la aplicación. Abortó con código 134 e Incompatible processor. This Qt build requires the following features: neon. Un segundo inicio explícito con arch -arm64 produjo el mismo mensaje. Evidencias: reports/orange/inicio_dialogos_qt.log y reports/orange/inicio_dialogos_qt_arm64.log. Esto no es un resultado de evaluación ni demuestra un problema con los datos.
56. Se abrió Orange local por su interfaz habitual. Se descartó la recuperación conforme a la autorización previa, se creó un flujo vacío y se agregó File. La captura de pantalla mostró el nodo File. Al intentar abrirlo, el controlador devolvió noWindowsAvailable. No se pudo confirmar en esta ocasión si fue cierre de la aplicación o pérdida de acceso a su ventana; no se consultaron nuevos reportes del sistema.
57. Ninguna corrida gráfica quedó verificada. Se actualizaron las notas del comparativo para reflejar los bloqueos actuales, conservando vacías exactitud y f1. Los algoritmos no se sustituyeron por terminal y no se alteraron originales ni se publicaron archivos. El objetivo de corridas gráficas continúa pendiente.

## 2026-11-08T18:18:12.449608-06:00 — Carga verificada en Weka

58. El usuario ordenó continuar exclusivamente con Weka y exceptuó la regla 5 para este intento. No se volvió a operar Orange.
59. Se crearon copias clustering.arff y clasificacion.arff en data/export con los mismos encabezados y valores de los CSV, indicando explícitamente nivel_popularidad como nominal en la segunda. Se verificaron todas las filas contra el CSV y se guardaron hashes en data/export/procedencia_arff.json. No se ejecutaron algoritmos por código.
60. Se ajustó el tamaño del selector y se actualizó su carpeta con clics gráficos. Se abrió clustering.arff por doble clic en la lista. Explorer confirmó Relation: clustering, Instances: 887, Attributes: 6, atributos Plays, Playing, Backlogs, Wishlist, Rating y Metacritic Rating. Captura: reports/weka/preprocess_887_6.png. El campo Plays mostró media 0 y desviación 1.001, coherente con el espacio exportado ya estandarizado.
61. Al intentar seleccionar Cluster por coordenadas, CUA devolvió noWindowsAvailable, aunque las lecturas posteriores conservaron Explorer y el dataset cargado. La selección por accesibilidad del grupo de pestañas devolvió unknownType(Optional(201)); los intentos de teclado no cambiaron la pestaña. La carga sí se verificó, pero no hubo corrida.
62. La revisión automática rechazó una llamada de actualización por exigir reescribir primero la documentación de CUA tras compactación. Se atendió ese requisito y la siguiente llamada fue permitida; no persiste ese bloqueo de revisión.
63. Se intentó iniciar únicamente Explorer 3.8.7 mediante el Java incluido y una ventana normal, sin algoritmos CLI ni cambios a la instalación. El primer intento indicó el permiso de módulos que también figura en su configuración oficial. Se agregó esa opción y el proceso volvió a terminar con código 134, sin detalle adicional. Log: reports/weka/explorer_3_8_7_ventana.log. La ventana original con 887 instancias permanece como última carga verificada.
64. No hay métricas nuevas. La alternativa propuesta requiere autorización expresa para control gráfico mediante AppleScript/System Events, ya que el control CUA no consigue operar las pestañas de Explorer.

## 2026-11-08T18:35:12.693017-06:00 — Control alternativo autorizado

65. El usuario autorizó expresamente AppleScript/System Events para operar Weka y pidió usar preguntas interactivas sin terminar el turno repetidamente. La primera consulta dentro del entorno restringido falló con -10827; se repitió con la autorización de ejecución del sistema. System Events identificó el proceso weka-3.8.7.
66. La consulta de sus controles por System Events falló con osascript no tiene permitido el acceso de ayuda (-1728). Se solicitó mediante pregunta interactiva habilitar el permiso de Accesibilidad y, si aparece, Automatización. No se intentó eludir el permiso ni se modificaron ajustes del sistema por código. Los modelos siguen sin ejecutarse.

## 2026-11-08T18:41:26.915572-06:00 — Acceso a controles Java

67. El usuario confirmó que habilitó permisos. System Events pudo activar el proceso weka-3.8.7 y leer la ventana Weka Explorer (posición 210,38; tamaño 1024x768). Con Control+PageDown dos veces se abrió Cluster; se verificó por accesibilidad.
68. El botón Choose no expone acciones AX. Se estableció AXFocused=true con System Events, se abrió con Espacio, se escribió SimpleKMeans en el selector y se confirmó con Enter. La captura gráfica confirmó SimpleKMeans con N=2. La semilla aún no se configuró y no se inició el entrenamiento.
69. El panel de propiedades pintado por Java no es accesible por teclado ni aparece como control AX. La lectura del código fuente local de PropertyPanel confirmó que se abre por clic; no se modificó código de Weka. Se solicitó autorización interactiva para clics nativos mediante osascript/JXA exclusivamente en Weka.

## 2026-11-08T19:00:05.570641-06:00 — Corridas gráficas verificadas

70. El usuario autorizó clics nativos mediante osascript/JXA solo en Weka. Se preparó clic_weka.js limitado por comprobación de coordenadas al área de Explorer. Se fijó explícitamente el contador de clic simple requerido por el panel Java.
71. Se abrió SimpleKMeans y se configuró seed=42; numClusters=2 ya estaba seleccionado. Se guardó kmeans_parametros.png. Los demás parámetros quedaron predeterminados; no se cambió la configuración de EuclideanDistance. Se confirmó OK y se inició Start en Cluster/Use training set.
72. La salida gráfica confirmó n=887, seis atributos, N=2, S=42, 9 iteraciones, errores cuadrados 76.63099068257982 y tamaños 477/410. Se copiaron centroides y salida completa del panel a kmeans.txt y captura kmeans_resultado.png. Diferencia registrada sin corregir: Python reporta tamaños 465/422; Weka GUI 477/410.
73. Se cargó clasificacion.arff mediante Open file, se verificaron 892 instancias, 53 atributos y Class: nivel_popularidad (Nom). Captura preprocess_clasificacion_892_53.png. Se abrió Classify y se seleccionó Cross-validation con Folds=10.
74. Se ejecutó ZeroR y se guardaron ZeroR.txt y ZeroR.png. Un intento de seleccionar NaiveBayes sin expandir su categoría repitió ZeroR; se identificó en Scheme y no se contabilizó como NaiveBayes. Se corrigió la selección por el árbol gráfico, sin modificar resultados. BayesNet quedó temporalmente seleccionado pero no se ejecutó.
75. Se confirmó visualmente NaiveBayes, luego J48 y RandomForest antes de sus corridas. Cada modelo se ejecutó con Start; se verificaron Scheme, 10-fold cross-validation, Stratified cross-validation y la matriz de confusión completa. Se guardaron NaiveBayes.txt/.png, J48.txt/.png y RandomForest.txt/.png. No se alteraron sus parámetros predeterminados; RandomForest muestra S=1 en la salida.
76. Se comprobaron las cuatro matrices: cada una suma 892, tiene tres filas/clases y su diagonal coincide con los aciertos mostrados. Se transcribió la exactitud en porcentaje y F-Measure de Weighted Avg. exactamente como Weka los muestra. ZeroR muestra F1 ponderada ?; se conserva ? sin reemplazarlo por un cálculo. Evidencia estructurada: verificacion_gui.json; resumen: resumen_gui.md.
77. Exactitudes mostradas: ZeroR 33.0717 %, NaiveBayes 50.8969 %, J48 51.009 %, RandomForest 53.4753 %. F-Measure ponderada: ?, 0.503, 0.506 y 0.530, respectivamente. Python reporta RF exactitud 0.5676 y F1 macro 0.5577 en prueba; se registran ambos protocolos sin intentar igualarlos ni corregir las corridas.
78. La búsqueda de DBSCAN no seleccionó ese clusterer. Se abrió Tools/Package manager en Weka GUI Chooser y se buscó optics. El filtro Available mostró optics_dbScan, categoría Clustering, versión de repositorio 1.0.6 y versión instalada vacía. Su ficha identifica OPTICS y DBSCAN. Se solicitó autorización interactiva para instalar este paquete oficial y dependencias, advirtiendo la posible escritura de componentes fuera de Final. No se pulsó Install. Captura dbscan_paquete_pendiente.png.
79. Un intento de captura con screencapture falló sin crear imagen; no se usa como evidencia. Los intentos de lectura del menú mediante AX no aportaron una lista fiable; el estado no instalado se verificó después en Package Manager. Los resultados previos CLI no se reutilizaron como corridas GUI.

## 2026-11-08T19:04:32.017092-06:00 — Instalación autorizada y cierre pendiente

80. Se revisaron visualmente las capturas guardadas de ZeroR, NaiveBayes y J48; RandomForest y K-Means ya se habían revisado en las capturas mostradas. Los valores y las matrices coinciden con sus salidas completas.
81. El usuario autorizó instalar el paquete oficial optics_dbScan 1.0.6 y sus dependencias, incluyendo la excepción por posible escritura en la carpeta de paquetes de Weka fuera de Final. Se pulsó Install mediante clic nativo y el diálogo enumeró exclusivamente optics_dbScan 1.0.6. Se confirmó Sí conforme a esa autorización.
82. Weka pidió cerrar las ventanas de aplicaciones abiertas (Explorer, Experimenter, KnowledgeFlow, SimpleCLI) antes de proceder. Se aceptó el aviso. Los intentos de cerrar solo Explorer por AXCloseButton, Cmd+W y clic nativo no confirmaron su cierre; se conservó abierto. No hay instalación completada verificada.
83. La revisión automática rechazó la propuesta de cerrar toda Weka mediante su comando Quit. Motivo: excede el alcance autorizado de cerrar Explorer y puede perder el estado pendiente del instalador. La acción no se ejecutó. No se intentó eludir el rechazo con otro comando. Se explicó al usuario y se solicitó autorización interactiva para cerrar y reabrir toda Weka. Las cinco corridas permanecen guardadas.

## 2026-11-08T19:23:33.499228-06:00 — Cierre autorizado y DBSCAN gráfico completado

84. El usuario autorizó explícitamente cerrar toda Weka y reabrirla. Se ejecutó Quit sobre weka.gui y se reabrió la misma aplicación 3.8.7. No se volvió a operar Orange.
85. Tras el reinicio se abrió Package Manager, se buscó optics y se comprobó la fila optics_dbScan: versión instalada 1.0.6, versión de repositorio 1.0.6, Loaded: Yes. Esto confirma que la instalación autorizada anterior quedó completada y cargada después del reinicio; no fue necesario repetir Install. Captura dbscan_paquete_instalado.png.
86. Se abrió Explorer. La entrada por teclado del nombre produjo una ruta en mayúsculas y después una extensión truncada; no se atribuye ese fallo a los valores del dataset. Se corrigió la selección mediante pegado de la ruta y finalmente doble clic directo en clustering.arff en la lista, sin usar Use Converter. No se modificó el archivo de datos.
87. La revisión automática bloqueó inicialmente la corrección de la ruta invocando la antigua regla 5. Se presentó la autorización previa literal del usuario para exceptuar esa regla durante las corridas de Weka. La siguiente acción acotada a cerrar el aviso fue permitida. No persistió un bloqueo de aprobación ni se eludió el rechazo con otro método.
88. La carga gráfica confirmó Relation: clustering, Instances: 887, Attributes: 6. Se activó explícitamente Explorer, se abrió Cluster y se seleccionó DBSCAN del paquete ya cargado. La captura de propiedades confirmó epsilon=1.666296 y minPoints=12. Se guardó dbscan_parametros.png. Las opciones de distancia permanecieron predeterminadas, tal como aparecen en la salida.
89. Se confirmó OK y se ejecutó Start en Use training set. El panel mostró weka.clusterers.DBSCAN -E 1.666296 -M 12, n=887, seis atributos, Number of generated clusters: 1 y Clustered Instances: 0 887 (100%). Se guardaron dbscan.txt y dbscan_resultado.png; la captura adicional dbscan_encabezado.png muestra la barra de parámetros y el resumen final, no el inicio textual del panel.
90. Se verificaron las 887 líneas de asignaciones del panel, con identificadores 0–886; todas tienen etiqueta 0. Por ello hay 0 etiquetas de ruido en esta corrida. Diferencia registrada sin corregir ni volver a ajustar: Python reporta 866 agrupados y 21 de ruido; Weka 887 (100%) en el cluster 0.
91. Se actualizaron reports/tables/comparativo_herramientas.csv, reports/weka/resumen_gui.md y verificacion_gui.json. Las cuatro matrices de clasificación siguen sumando 892 y sus salidas no cambiaron. Las seis corridas gráficas de Weka están completas y cuentan con evidencia; las filas de Orange se conservan pendientes. No se ejecutó ningún algoritmo por terminal, no se modificó data/raw y no se subieron datos.

## 2026-11-08T19:35:13.159127-06:00 — Respaldo, capturas y verificación posterior

92. Se tomó una captura nueva de la ventana actual de Weka en verificacion_final_ventana.png y se guardó primero respaldo_evidencias_weka_gui.zip, con 24 archivos de evidencias y un manifiesto inicial. Después se inició la revisión, sin ejecutar modelos nuevos ni subir archivos.
93. Se abrieron visualmente las seis capturas de resultados y se comprobaron su legibilidad y correspondencia con cada modelo. La validación binaria encontró un fallo de guardado: las 12 imágenes principales tenían contenido JPEG aunque su extensión era .png. Se informó del hallazgo al usuario.
94. Se conservaron los originales exactos con extensión .jpg en reports/weka/capturas_originales_jpeg y se corrigió la codificación de los .png. Se verificó igualdad de todos los píxeles, dimensiones y modo; se preservaron perfiles de color y EXIF existentes. No se modificaron textos, números ni contenido visual de las capturas. Registro: conversion_capturas.json.
95. Se verificaron las cuatro matrices y sus aciertos, la transcripción exacta del comparativo, los tamaños de K-Means y las 887 asignaciones de DBSCAN. Se escribió revision_respaldo.md y se reconstruyó el ZIP para incluir las capturas válidas, originales JPEG, revisión y bitácora final. Se comprobó CRC, hashes y ausencia de entradas duplicadas. No se encontraron discrepancias en los resultados y no se modificó data/raw.

## 2026-11-09T11:20:22.111843-06:00 — Auditoría completa de pendientes de Weka

96. El usuario solicitó volver a Weka y completar todo pendiente. Se abrió Weka 3.8.7 y se comprobaron los archivos del manifiesto anterior: ninguno ausente ni alterado; el ZIP anterior pasó la verificación CRC. Los hashes de los CSV y ARFF exportados coinciden con la procedencia guardada.
97. Se comprobó cada valor de los CSV contra el ARFF correspondiente mediante su lectura tipada: clustering 887x6 y clasificación 892x53. La clase final es nivel_popularidad; se verificaron alto=297, medio=297 y bajo=298. Se comprobaron las cuatro matrices, los diez pliegues estratificados, las métricas transcritas, los centroides de las seis variables de K-Means y las 887 asignaciones de DBSCAN.
98. Se abrió Explorer y se cargó clasificacion.arff mediante el selector gráfico. El acceso alternativo System Events devolvió falta de permiso de Accesibilidad en esta sesión; se completó la carga mediante CUA sin requerir ese acceso. La interfaz confirmó 892 instancias, 53 atributos y clase nominal nivel_popularidad. Captura nueva: revision_explorer_2026_11_09.jpg, guardada con la extensión correcta para su codificación JPEG. Explorer queda abierto. No se ejecutaron nuevos entrenamientos ni se atribuyen resultados anteriores a una corrida nueva.
99. Se guardaron auditoria_cierre_2026_11_09.json y cierre_weka_2026_11_09.md: no se encontraron pendientes de los seis entregables pedidos para Weka. Se conservó el respaldo anterior como respaldo_evidencias_weka_gui_previo_cierre.zip y se actualizó el respaldo principal y su manifiesto con la auditoría, captura y bitácora actuales. Se verificaron nuevamente hashes y CRC. No se cambió ningún resultado, dato raw ni archivo de implementación de la web.

## 2026-11-09T11:32:41.073064-06:00 — Desviación del plan: Orange descartado; comparativo Python / Weka

100. Por instrucción expresa del usuario se verificó que reports/weka contiene salidas completas y capturas legibles de SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Se comprobaron lectura de imágenes, encabezados y evaluación; las cuatro matrices suman 892 y sus diagonales coinciden con los aciertos. Registro: reports/weka/verificacion_comparativo_python_weka.json. No se volvieron a ejecutar modelos.
101. Se sustituyó el comparativo por 12 filas exclusivamente de Python y Weka: dos de clustering y cuatro de clasificación para cada herramienta. Python se tomó de models/metadata.json (comparacion_modelos) y data/clean/dataset_con_clusters.csv; Weka se contrastó con sus TXT. Exactitud se expresa en porcentaje: la conversión de Python desde proporción se declara y conserva su valor fuente en notas; los valores Weka no se cambiaron. F1 sigue siendo macro de prueba en Python y ponderado de CV en Weka, incluido ? de ZeroR. No se recalcularon ni inventaron métricas.

### Desviación formal respecto al plan original de herramientas

102. El plan incluía clasificación y clustering en Orange, con flujos .ows, capturas, diez pliegues y matrices de confusión. Se descarta esa parte por fallos reiterados que impidieron obtener evaluaciones gráficas verificables. Esta decisión cierra Orange como desviación técnica del plan, no como una corrida pendiente ni como un resultado experimental negativo de los modelos. Los resultados disponibles del proyecto son Python y Weka.
103. Intentos realizados: apertura de Orange en el disco externo; File con CSV; alternativa CSV File Import autorizada; copia TAB nativa con los mismos 892 registros y 53 columnas, sin alterar el CSV; recuperación de sesiones y después descarte autorizado para usar un lienzo vacío; nuevo intento después de que el usuario instalara Orange localmente en /Applications/Orange.app. El control informó cierres o pérdida de ventanas al abrir File o confirmar selectores. El usuario reportó que una carga manual de 892 instancias sí funcionaba; esto no se presenta como una evaluación de modelos ni se atribuye el fallo al dataset.
104. Diagnóstico autorizado de solo lectura: cuatro reportes de cierre de Orange registraron EXC_BAD_ACCESS / SIGSEGV en el hilo principal, con símbolos Qt/Cocoa (libqcocoa.dylib, objc_release/objc_msgSend). Uno corresponde a la instalación local y tres a la externa. Evidencia: reports/orange/diagnostico_cierres.json y diagnostico_cierres.md. Es una hipótesis de interacción gráfica nativa, no una causa raíz demostrada ni prueba de que el archivo o el disco externo fueran culpables.
105. Se preparó y ejecutó con autorización iniciar_con_dialogos_qt.py, que desactiva temporalmente los diálogos nativos solo para esa sesión, sin modificar Orange. Tanto el inicio normal del lanzador como el intento explícito con arch -arm64 abortaron con código 134 y el mensaje Incompatible processor / This Qt build requires the following features: neon. Evidencias: reports/orange/inicio_dialogos_qt.log e inicio_dialogos_qt_arm64.log. Un intento posterior por la interfaz habitual volvió a perder la ventana al abrir el nodo File (noWindowsAvailable); ese mensaje por sí solo no demuestra un nuevo cierre del proceso.
106. Motivo del descarte: no se pudo completar y verificar un flujo estable de evaluación con las alternativas ensayadas. Impacto: no se entregan flujos .ows de evaluación completada, matrices ni métricas Orange; se conservan los diagnósticos y las capturas de incidencias. No se copiaron métricas Python/Weka a Orange y se eliminaron incluso sus filas vacías del comparativo actual. El diagnóstico inicial de Orange describe el estado de aquella fecha; esta entrada documenta los intentos posteriores del lanzador y la decisión vigente de descarte.
107. Se actualizó el respaldo local y su manifiesto para incorporar el comparativo y esta desviación, conservando una copia del respaldo anterior. No se modificaron datos raw, modelos ni resultados de las seis corridas de Weka.

## 2026-11-09T11:41:15.431069-06:00 — Evaluaciones y F1 comparables solicitados

108. Se implementó reports/tables/evaluar_comparabilidad.py, con rutas pathlib relativas a Final y semilla 42. Se ejecutaron cuatro modelos por cada una de tres cohortes: todos los 1117 registros, los 1114 elegibles como sensibilidad y los mismos 892 registros exportados a Weka como enlace. En cada esquema se usó CV estratificada de diez pliegues y cada fila tuvo una predicción OOF. No se sobrescribió ningún modelo de producción ni su evaluación de prueba.
109. Se calcularon exactitud en porcentaje, F1 macro y F1 ponderado de las predicciones OOF. Se conservaron matrices, métricas por fold y sus medias en comparativo_detalle.json, particiones en comparativo_folds.csv y predicciones en comparativo_predicciones_oof.csv. El catálogo completo incluye explícitamente los tres conflictos históricos; la evaluación elegible permite contrastar esa inclusión.
110. Se obtuvo F1 macro de las salidas Weka como media simple de los F-Measure por clase y se tomó Weighted Avg. como ponderado cuando existe. En ZeroR, los signos ? se resolvieron desde su matriz con la fórmula F1=2TP/(2TP+FP+FN); no son cifras copiadas ni reportadas como salidas originales de Weka. Las diferencias por redondeo se verificaron con tolerancia 0.00051; la exactitud impresa con tolerancia 0.000051 puntos porcentuales.
111. El CSV se cambió a herramienta, modelo, esquema_evaluacion, exactitud_pct, f1_macro, f1_ponderado, notas. Tiene 20 filas: 12 Python, cuatro clasificadores Weka y cuatro filas de clustering con métricas de clasificación vacías. No contiene Orange, que sigue descartado por la desviación documentada. Las diferencias metodológicas que no se igualan se anotaron en cada fila, sin devolverlas como tareas al usuario.
112. Se ejecutaron 28 pruebas existentes (modelo, auditoría 2, clustering) y tres pruebas independientes nuevas: todas aprobadas. Las nuevas recomputan métricas desde matrices, reproducen los folds de semilla 42 y verifican cobertura y Dummy, contrastan el redondeo Weka y abren las seis imágenes de evidencia. Los archivos de resultados de ambas ejecuciones están en reports/tables. No se ejecutaron nuevas corridas Weka ni Orange.
113. Se actualizó el respaldo y el manifiesto para conservar código reproducible, predicciones, folds, detalle de matrices, pruebas y nuevo esquema de comparación; el respaldo previo se preservó. Se validaron nuevamente CRC y SHA-256. No quedan verificaciones ejecutables de esta solicitud pendientes.

## Informe y revisión de predicciones del 9 de noviembre de 2026

- Se recalcularon las cuatro matrices originales de clasificación de Weka: 892 casos cada una; sus diagonales reproducen la exactitud de la GUI. No se modificaron las salidas ni capturas de Weka. Evidencia: reports/revision_predicciones/weka_recalculado.json.
- Se reprodujeron las 222 predicciones de prueba del Pipeline y su F1 macro de 0.5577027297, exactitud de 0.5675675676 y matriz. Se validaron probabilidades, referencias del objetivo, grupos de título y el espacio de los vecinos. Evidencia: reports/revision_predicciones/auditoria.json.
- Se compararon siete variantes nuevas de Random Forest y el vigente sobre los diez pliegues de entrenamiento, con objetivo y preprocesamiento locales. Se realizaron 80 ajustes; ninguna variante superó F1 CV 0.5566561803 del modelo vigente. No se sustituyó el modelo, ni se escogieron parámetros con la prueba. Código: src/05_revision_predicciones.py; evidencias en reports/revision_predicciones/busqueda_folds.csv, busqueda_resumen.csv y decision.json.
- Se centralizó el contrato del formulario en src/inferencia.py, validando las escalas y la correspondencia entre clases y probabilidades. Se corrigió el ancho mínimo artificial de 2 % y la etiqueta de organizaciones no frecuentes. Se agregó aviso visible cuando falta la nota crítica. Se aclaró HIST frente a MAESTRO en Inicio: el original designado tiene 1,117 filas y 42 columnas; 1,512 es el antecedente histórico.
- En navegador se probaron los extremos de los sliders, el envío del formulario y la ausencia de Metacritic. Adventure y RPG, Otro, década 2020, Rating 5 y Metacritic 100: alto 54.1 %. Al ocultar Metacritic: bajo 44.2 %. Coincide con los cálculos directos; se documenta sensibilidad a cobertura. Capturas: formulario_verificado.jpg y sin_critica_verificado.jpg en reports/revision_predicciones.
- Pasaron 39 pruebas de inferencia, modelo, pipeline y visualización. Datos y modelos conservaron sus hashes: 20 archivos sin cambios. Registros: pruebas.txt e integridad_final.json en reports/revision_predicciones.
- Se generó reports/hallazgos_weka_web.docx con fuente Markdown. Se renderizaron e inspeccionaron las siete páginas y se corrigió un borde heredado del estilo Title. Las imágenes y el PDF de render se conservan solo para revisión interna en reports/revision_predicciones/render_documento.

````

## Origen: Final/reports/correcciones_auditoria.md

SHA-256: `789cb1ccba415d8e47e8a77fe3792e1cb9f30020e5ef2fb779790545e56b9bbb`

````text
# Correcciones de implementación tras la auditoría

> Registro de la primera auditoría. Para los cambios posteriores de Fase 4B, consultar correcciones_auditoria2.md y modelo.md.

Se revisó la auditoría recibida contra los archivos y se corrigieron las fases en Final. No se modificaron el maestro designado, su antecedente histórico en Proyecto ni el anteproyecto PDF/LaTeX. El trabajo permanece local.

## Hallazgos, correcciones y evidencia

| Hallazgo | Comprobación y decisión | Implementación / evidencia |
|---|---|---|
| Dos pipelines con clusters distintos | Confirmado. Se eliminó la implementación paralela de cuatro conteos del flujo activo. | src/pipeline.py ejecuta 01→02→03; data.py y analysis.py son adaptadores. App, clustering.md y hallazgos.md leen dataset_depurado y dataset_con_clusters; manifest.json comprueba hashes. Resultados previos archivados en archivo_pre_auditoria. |
| Deduplicación histórica sin resolución de conflictos | Confirmado en el antecedente. Se reconstruyen las 42 columnas sin diferencias y se registran individualmente los 395 descartes heredados. Reconstruir no equivale a resolver las variantes. | src/procedencia.py, data/historical, trazabilidad_historica.md/json, deduplicacion_historica.csv, conflictos_historicos.csv y variantes_historicas.csv. |
| “13 conflictos numéricos” | La auditoría mezcla diferencias textuales y analíticas: hay 13 grupos con alguna diferencia, **tres** con conflictos analíticos. No se selecciona arbitrariamente una versión nueva. | Los IDs 117, 140 y 296 se conservan señalados, con elegible_analisis=False. Se excluyen provisionalmente de análisis y entrenamiento; los CSV conservan los 1,117 registros. |
| Fuente curada presentada como crudo original | Confirmado como problema de trazabilidad, manteniendo la instrucción explícita del usuario de usar games_curated como original del trabajo. Se distingue ese maestro del antecedente crudo. | fase_1_alcance.md, README, data/historical/README.md, inspeccion y reconstrucción completa reproducible sin depender de Proyecto. |
| Faltan 01_inspeccion y seis gráficas EDA | Confirmado y corregido. El informe deja de ser una descripción retrospectiva manual y pasa a generarse con código. | src/01_inspeccion.py produce histogramas de Rating, crítica utilizable y Plays log; barras por década, top 15 géneros y dispersión usuarios–prensa. |
| Log atribuye conversiones K/M inexistentes | Confirmado. Se cuentan formatos realmente recibidos en cada corrida; el maestro entra numérico. | 02_limpieza y limpieza_log.md: 6,702 celdas ya numéricas, cero textos K/M convertidos. El antecedente sí se reconstruye desde sus formatos originales, en otra operación identificada. |
| Comas de miles no admitidas | Confirmado como limitación del parser nuevo. Se aceptan comas bien agrupadas, manteniendo el rechazo de coma decimal ambigua. | Tests para 1,200→1200 y 1,500→1500; 1,5K continúa siendo error explícito. |
| Riesgo de unión cartesiana por títulos repetidos | Los 35 registros de 17 títulos compartidos están confirmados. No son duplicados probados: pueden ser remakes, ports u obras homónimas. No se destruyen sus observaciones. | id_juego es la clave de relaciones; indicador titulo_compartido; prueba many_to_one y prueba que una unión por título falla. Sensibilidad de correlaciones por título único en clustering_03_sensibilidad_titulos.csv. |
| Sobreponderación de reediciones | Riesgo de dependencia confirmado, sin evidencia suficiente para identificar todas como reediciones de la misma obra. Se distingue el análisis principal por ID de una sensibilidad por título. | La sensibilidad promedia las dos notas dentro de cada título sobre pares completos y recalcula Pearson/Spearman. No se usa como deduplicación definitiva ni se llama muestra independiente por franquicia. |
| DBSCAN produce un solo grupo | Confirmado. No es un fallo aritmético de DBSCAN ni prueba de que deba forzarse otro eps. Se conserva el codo reproducible, la sensibilidad local y se rechaza interpretarlo como segmentación comercial útil. | Reporte y app muestran un núcleo de 866 juegos y 21 atípicos sobre 887 elegibles completos; silhouette entre clusters no definida. No se inventa una métrica ni perfiles separados. |
| k=2 solo refleja magnitud conjunta | Confirmado como limitación interpretativa. Se mantienen el criterio de silhouette y la comparación de k=2…10, añadiendo interpretación completa de k=3/4. | clustering_03_alternativas_k.csv y ejemplos. En k=4 aparece, entre otros, un grupo de menor actividad con recepción por encima del promedio; no se cambia k solo para producir una narrativa. |
| Nombre “recepción intermedia” en el grupo de notas más altas | Era una categoría relativa dependiente de un umbral, no un cálculo incorrecto de la media. Se cambió por una descripción directamente comprobable. | nombre_perfil usa superior/inferior al promedio de casos completos y conserva medias originales; se retira el corte arbitrario de ±0.5. |
| Visual Novel tiene menor brecha, pero r no positivo | El dato es compatible: menor distancia de puntuaciones no implica acuerdo en orden. No se atribuye la diferencia a una “varianza mínima” sin demostrarla. | Ranking rotulado como distancia de puntuaciones; r, rho, n y p se mantienen junto a MAE. Nota explícita sobre Visual Novel y sobre no confundir MAE con correlación ni con diferencia de medias. |
| Circularidad entre 4A y 4B | Era un riesgo potencial, no una fuga supervisada ya demostrada: el modelo existente ya usaba terciles independientes. Se endureció el contrato y la comprobación. | train rechaza cluster_* y componentes PCA; lee solo dataset_depurado, excluye conflictos y ajusta cortes/escaladores/imputación por entrenamiento y fold. Nunca reutiliza el scaler descriptivo. |
| Falta evidencia real Orange/Weka | Confirmado. Se ejecutó K-Means de Weka 3.8.6 por CLI para k=2/3/4 en los mismos 887 casos y seis variables transformadas. Se conservan salidas, comandos, hashes y asignaciones. | reports/comparacion_weka.md y reports/weka. Para k=2, ARI=1.0 y silhouette=0.318771 en ambas herramientas; para k=3/4 se documentan diferencias. No se afirma haber ejecutado Orange ni una comparación supervisada de Weka. |
| Entorno y nube | Las versiones fijadas existen en el entorno y se validaron; no se cambian por la afirmación de que son “no estándar”. Dos entornos locales no son contaminación si están excluidos de distribución. No hay despliegue autorizado. | .gitignore excluye .venv, .venv314 y .cache. README describe Python 3.14 validado y reproducción; JAR fijados con SHA-256. Compatibilidad adicional no demostrada se declara, no se inventa. |

## Reproducción y control de evidencia

Desde Final: `python -m src.pipeline` regenera inspección, historia, limpieza, análisis y clasificación independiente. Si Java y los JAR están presentes, repite la comparación Weka; para obtener los JAR locales se usa explícitamente `python src/comparar_weka.py --descargar`.

La app usa la misma versión de código/datos y los hashes de manifest.json. Las pruebas comprueban conservación de filas, elegibilidad, rechazo de contaminación por etiquetas, trazabilidad y unión por ID. El registro de pruebas se guarda en reports/pruebas_auditoria.txt.

## Matices de la auditoría que no deben reproducirse como hechos

- wc -l cuenta líneas físicas, no registros CSV: Summary y Reviews tienen texto multilínea.
- La función de limpieza completa exige el esquema curado; aplicarla al antecedente sin critic_source/critic_score_final no es una prueba equivalente. La reconstrucción histórica comprueba explícitamente la selección, las columnas y las discrepancias.
- Una transformación o un scaler ajustados a toda la muestra descriptiva no constituyen por sí solos fuga de una evaluación supervisada inexistente. El problema sería reutilizarlos en esa evaluación; ahora el contrato lo impide.
- MAE, diferencia de medias y correlación son medidas distintas. Un grupo puede tener puntuaciones cercanas y asociación nula sin contradicción matemática.

## Validación ejecutada

- Cadena completa regenerada sin modificar ambas fuentes.
- 66 pruebas aprobadas; registro en pruebas_auditoria.txt.
- Comprobación real en Chrome: la página de perfiles muestra 887 casos, seis variables, k=2, DBSCAN con 866 miembros y 21 atípicos, coincidiendo con el reporte.
- Hashes del manifiesto y las dos tablas canónicas verificados tras la ejecución.

## Que debo verificar manualmente

- Resolver las tres discrepancias históricas con plataforma, edición y fecha de captura antes de reincorporarlas al análisis principal.
- Obtener identificadores externos para juegos homónimos y verificar si una unidad por franquicia es pertinente.
- Confirmar que la evidencia por CLI de Weka y la demo local satisfacen al profesor; no hay capturas gráficas de Orange/Weka.
- Evaluar estabilidad de clusters en muestras distintas y utilidad de k=3/4; la sensibilidad local de eps no equivale a esa validación.
- Verificar procedencia de las notas, roles de Team, licencia y escala histórica exportada.

````

## Origen: Final/reports/correcciones_auditoria2.md

SHA-256: `21ae2d1a4b43fb63ad3efc7f3b7fb9d91db82119b8ea507f0f8bf44ee1dfe68d`

````text
# Segunda auditoría: correcciones y límites vigentes

Se revisaron los hallazgos contra la implementación y se regeneró la fase 4B. Las correcciones previas de EDA, historia, maestro y clustering se conservan; los datos originales siguen intactos y no hay publicación autorizada.

## Cambios comprobables

| Hallazgo | Corrección / decisión | Evidencia |
|---|---|---|
| Target transductivo | Se retira la definición global usada antes de la partición. Primero se divide por título con GroupShuffleSplit, una sola vez y semilla 42; se ajustan percentiles y terciles en los 892 juegos de entrenamiento. Los 222 de prueba se interpolan contra esa referencia congelada. | src/objetivo.py, src/04_modelo.py, models/metadata.json y juegos_modelo.csv. Mutar señales solo en prueba deja intacta la referencia, comprobado por tests. |
| Target dentro de cada fold | GridSearchCV usa ClasificadorObjetivoLocal: fit recibe el contexto y ajusta una referencia local; el Pipeline solo recibe las cinco entradas predictivas. score calcula la verdad de validación con la referencia de ese mismo subentrenamiento, ignorando las etiquetas externas para entrenar y puntuar. | models/referencias_folds.json guarda diez referencias e IDs; modelo_etiquetas_validacion_locales.csv conserva las clases efectivas de validación. Se verifican referencias, separación de IDs y ausencia de casos de prueba en los folds. |
| Búsqueda por 1,258 rechazos | Se elimina el bucle y su máximo de intentos. Se usa aproximadamente 80/20 por grupos, sin etiquetas globales. La CV sigue estratificada por títulos usando etiquetas del entrenamiento exterior solo para organizar estratos. | Metadata declara holdout no estratificado y aproximado, un solo reparto y diez folds. Se cambia explícitamente el contrato anterior: no se fuerza una estratificación del target antes de que exista una referencia de entrenamiento. |
| Escalado de banderas de ausencia | El modelo principal no incluye MissingIndicator de ninguna nota. El scaler se aplica solo a las dos notas continuas; géneros, organizaciones y década conservan indicadores 0/1. | construir_pipeline y tests que inspeccionan nombres y valores transformados. Los indicadores de limpieza siguen en el CSV para auditoría, no entre las cinco entradas. |
| Cobertura de Metacritic como proxy de curación | Se retira la bandera explícita del predictor y la ausencia deja de estar marcada por defecto. Se agregan tablas de cobertura/clase, ocultamiento de notas conocidas y ablación sin crítica, sin reseleccionar modelos por esos resultados. | modelo_ausencia_*.csv, modelo_sensibilidad_critica.csv y diagnostico_ausencia en metadata. El sesgo residual se declara, no se da por resuelto. |
| Otro activado por cualquier miembro raro de Team | En estudio, Otro solo se activa cuando ninguna organización de la lista pertenece al vocabulario frecuente; una combinación frecuente+rara mantiene la frecuente sin Otro. Las listas vacías usan Sin dato. Género conserva su regla independiente de pertenencias múltiples. | CategoriasFrecuentes(otro_solo_si_ninguna=True); prueba con frecuente+raro, solo nuevo y lista vacía. Otro aparece ahora en 39.69 % de entrenamiento y 44.14 % de prueba; las muestras han cambiado, por lo que no es un experimento causal de la diferencia de porcentajes. |
| GaussianNB sobre dummies escasas | Se sustituye por CategoricalNB: notas imputadas y discretizadas en cinco intervalos de ancho uniforme aprendidos dentro de entrenamiento; el resto son indicadores categóricos. Se ajusta alpha con GridSearchCV. | modelo_comparacion.csv, matrices vigentes de CategoricalNB y explicación en modelo.md. La matriz antigua de GaussianNB se archiva. |
| Clase media mal reconocida | Se informa soporte, aciertos y recall de todas las clases de cada candidato y se destaca la debilidad del ganador. No se reoptimiza con los errores de prueba. | modelo_error_por_clase.csv y advertencia en modelo.md: el bosque acierta 27/80 medios, recall 33.75 %. Esta limitación sigue abierta. |
| Dummy elegido por desempate | Se documenta que los terciles tienden a balancear por construcción aun ajustados correctamente, y sklearn desempata si es necesario. En el nuevo entrenamiento hay 298 bajos, 297 medios y 297 altos; la clase mayoritaria es bajo sin empate triple. | Metadata y matriz del Dummy. La referencia continúa siendo most_frequent, no se manipulan los cortes para fortalecerla o debilitarla. |
| Playing e índice mezclados en la app | Se mantiene Playing como contexto del EDA/clustering, no como objetivo ni predictor del modelo. El índice de tres señales y su referencia de entrenamiento aparecen explícitamente junto a la tabla, además de en la metodología. | app.py, fase_1_alcance.md y README. Es una diferencia intencional entre tareas, no una columna oculta del target. |
| pytest directo no importa src | Se agrega pytest.ini con pythonpath=. y testpaths=tests. | Se ejecuta .venv314/bin/pytest desde Final, además de python -m pytest. |
| Pipeline no cargable fuera del repositorio | Las clases propias del preprocesamiento se serializan por valor con cloudpickle. El archivo sigue conteniendo un Pipeline compatible con joblib.load, sin importación previa de src; requiere las versiones documentadas de las bibliotecas. | Test en subproceso con cwd temporal y sin PYTHONPATH: carga, predice y comprueba que src no está en sys.modules. No se trata solo de una prueba dentro de pytest con rutas ya añadidas. |
| Nota ausente por defecto y vecinos faltantes | Checkbox por defecto False, entrada sin valor inventado; para predecir se exige una nota o marcar ausencia explícita. Se agregan cinco vecinos ajustados solo en el espacio predictivo del entrenamiento; sus clusters se adjuntan después por id_juego. | pages/3_Consultar_modelo.py, src/similitud.py y models/vecinos_popularidad.joblib; pruebas de validación del formulario, cinco IDs distintos y pertenencia exclusiva al entrenamiento. |

## Resultados regenerados

| Modelo | Exactitud en prueba | F1 macro en prueba |
|---|---:|---:|
| DummyClassifier | 0.3018 | 0.1546 |
| CategoricalNB | 0.5090 | 0.4925 |
| DecisionTreeClassifier | 0.5315 | 0.5119 |
| RandomForestClassifier | 0.5676 | 0.5577 |

El bosque se eligió por la mayor F1 macro media de validación (0.5567), no por la tabla de prueba. Su recall es 64.18 % en bajo, 33.75 % en medio y 74.67 % en alto. El target y el reparto han cambiado: no se atribuye causalmente la diferencia frente a F1=0.5814 del protocolo global anterior.

## Sesgo residual: resultado, no promesa

Al ocultar las 180 notas conocidas de prueba, manteniendo los demás atributos, la probabilidad de bajo aumenta en promedio 0.03885 y su mediana cambia 0.00810. La ablación diagnóstica sin crítica obtiene F1 macro 0.5149. Se retiró la bandera explícita, pero el patrón de imputación y la cobertura no aleatoria pueden seguir influyendo; estos cálculos no son una prueba causal ni de equidad.

La referencia correcta del target y las distribuciones reales están en metadata. Los terciles de entrenamiento casi equilibrados son una propiedad esperable de la definición, no prueba de fuga por sí misma. Lo que se corrigió es usar la prueba y la validación para ajustar referencias.

## Matices técnicos de la auditoría

- Centrar y escalar una variable de manera invertible no distorsiona por sí solo las comparaciones gaussianas ideales: el factor jacobiano común se cancela entre clases. El problema relevante era mezclar indicadores escasos con un supuesto gaussiano y suavizado, y ofrecer explícitamente un proxy de cobertura. Se corrigió el diseño sin afirmar una causa matemática que no se demostró.
- Que Otro sea frecuente y tenga poca importancia no demuestra que una cosa cause la otra. Se cambió la semántica y se informa su prevalencia nueva sin prometer una mejora causal.
- La matriz antigua de GaussianNB no indicaba que predijera siempre medio; indicaba que reconocía mal los medios. Se sustituye el supuesto inapropiado y se conserva un análisis de error explícito del candidato actual.
- La clase media puede solaparse en los predictores con ambos extremos y los cortes introducen fronteras artificiales. Es una explicación plausible, no una causa verificada; el recall bajo permanece como limitación.

## Reproducción

Desde Final: python -m src.pipeline regenera los artefactos canónicos; python src/04_modelo.py regenera solo el modelo desde dataset_depurado. El manifiesto valida modelo, metadata, vecinos y datasets. Las métricas globales antiguas se conservan en archivo_modelo_pre_auditoria2, fuera del flujo activo.

Los registros de las dos entradas de pytest están en pruebas_auditoria2.txt y pruebas_auditoria2_modulo.txt. La prueba de portabilidad usa un proceso limpio y la app se valida con notas explícitas y vecinos.

## Validación final ejecutada

- 82 pruebas aprobadas con pytest directo y 82 con python -m pytest; registros conservados.
- Carga del Pipeline en subproceso limpio sin src en PYTHONPATH y predicción cruda comprobadas.
- Verificación en Chrome: nota de prensa habilitada y ausencia desmarcada al abrir; al proporcionar 85 y enviar se obtuvo una predicción y cinco vecinos con sus etiquetas disponibles por ID.
- Hashes de datasets, modelo, metadata y vecinos concordantes con el manifiesto; maestro y antecedente histórico intactos.

## Que debo verificar manualmente

- Roles de Team y los tres conflictos históricos pendientes de identidad/plataforma.
- Pesos y redundancia del índice; antigüedad y representatividad de los juegos.
- Sesgo residual de cobertura de prensa y desempeño insuficiente de la clase medio.
- Similitud de vecinos como descripción de atributos, sin inferir causalidad ni éxito comercial.
- Dependencias de versión para cargar el Pipeline portátil; no se requiere src, pero sí las bibliotecas registradas.

````

## Origen: Final/reports/ejecucion_actual.txt

SHA-256: `2ec190f685593d1c43a99c7d456871703b7cbf2df0611c611a96050ce592e24e`

````text
Limpieza completada: 1117 → 1117 juegos; 2682 pertenencias de género. Ver reports/limpieza_log.md.
Análisis completado: 1117 juegos conservados; 887 agrupados; k=2; eps=1.6663; ruido=21. Ver reports/clustering.md.
Modelo guardado: RandomForestClassifier; entrenamiento=891, prueba=223, F1 macro=0.5814; referencia=0.1661.
# Hallazgos de la cadena canónica

Fuente maestra: data/raw/games_curated.csv, sin modificar. Historia de 1,512 registros y decisiones heredadas: trazabilidad_historica.md.
La inspección, limpieza, clustering y app comparten dataset_depurado.csv y dataset_con_clusters.csv. El análisis completo de asociación está en clustering.md, con mínimo de 20 pares por grupo.

Fase 4A: 887 casos completos elegibles de 1117 registros conservados; 3 conflictos históricos pendientes excluidos del análisis principal.
K-Means usa seis variables y k=2 entre 2 y 10. DBSCAN usa eps=1.666296, min_samples=12; clusters=1, ruido=21.
Un solo grupo de DBSCAN no acredita segmentación comercial útil. Ver comparación de k=2/3/4 y sensibilidad a títulos compartidos en clustering.md.

Clasificador independiente por terciles del promedio de rangos percentiles de Plays, Wishlist y Backlogs: RandomForestClassifier; n prueba=223, F1 macro=0.5814, base=0.1661. Los clusters descriptivos no se utilizan como objetivo ni predictores.

## Que debo verificar manualmente

- Resolver plataformas de discrepancias históricas y roles de Team.
- Interpretar distancias de puntuaciones separadas de asociación de orden.
- Confirmar estabilidad de perfiles; popularidad no equivale a éxito comercial.


````

## Origen: Final/reports/ejecucion_auditoria2.txt

SHA-256: `0c0e3edf12797115278cae98ac58473fa7a7b12db01b2f302b8be46cf95cdc55`

````text
Limpieza completada: 1117 → 1117 juegos; 2682 pertenencias de género. Ver reports/limpieza_log.md.
Análisis completado: 1117 juegos conservados; 887 agrupados; k=2; eps=1.6663; ruido=21. Ver reports/clustering.md.
Modelo guardado: RandomForestClassifier; entrenamiento=892, prueba=222, F1 macro=0.5577; referencia=0.1546.
# Hallazgos de la cadena canónica

Fuente maestra: data/raw/games_curated.csv, sin modificar. Historia de 1,512 registros y decisiones heredadas: trazabilidad_historica.md.
La inspección, limpieza, clustering y app comparten dataset_depurado.csv y dataset_con_clusters.csv. El análisis completo de asociación está en clustering.md, con mínimo de 20 pares por grupo.

Fase 4A: 887 casos completos elegibles de 1117 registros conservados; 3 conflictos históricos pendientes excluidos del análisis principal.
K-Means usa seis variables y k=2 entre 2 y 10. DBSCAN usa eps=1.666296, min_samples=12; clusters=1, ruido=21.
Un solo grupo de DBSCAN no acredita segmentación comercial útil. Ver comparación de k=2/3/4 y sensibilidad a títulos compartidos en clustering.md.

Clasificador independiente por terciles del promedio de rangos percentiles de Plays, Wishlist y Backlogs: RandomForestClassifier; n prueba=222, F1 macro=0.5577, base=0.1546. Los clusters descriptivos no se utilizan como objetivo ni predictores.

## Que debo verificar manualmente

- Resolver plataformas de discrepancias históricas y roles de Team.
- Interpretar distancias de puntuaciones separadas de asociación de orden.
- Confirmar estabilidad de perfiles; popularidad no equivale a éxito comercial.


````

## Origen: Final/reports/ejecucion_modelo_auditoria2.txt

SHA-256: `35b86e275f679a6b956e8abf1a63b0a8bf54da17bd915d685b55dab82639d1a1`

````text
Modelo guardado: RandomForestClassifier; entrenamiento=892, prueba=222, F1 macro=0.5577; referencia=0.1546.

````

## Origen: Final/reports/ejecucion_revision_integral.txt

SHA-256: `d4fd367bf0df5919c00b73c851eb87111143a03c2918b223f664faa711051878`

````text
/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
invalid literal for int() with base 10: ''
Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
  warnings.warn(
  File "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py", line 264, in _count_physical_cores
    cpu_count_physical = _count_physical_cores_darwin()
  File "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py", line 420, in _count_physical_cores_darwin
    return int(cpu_info)
Limpieza completada: 1117 → 1117 juegos; 2682 pertenencias de género. Ver reports/limpieza_log.md.
Análisis completado: 1117 juegos conservados; 887 agrupados; k=2; eps=1.6663; ruido=21. Ver reports/clustering.md.
Modelo guardado: RandomForestClassifier; entrenamiento=892, prueba=222, F1 macro=0.5577; referencia=0.1546.
# Hallazgos de la cadena canónica

Fuente maestra: data/raw/games_curated.csv, sin modificar. Historia de 1,512 registros y decisiones heredadas: trazabilidad_historica.md.
La inspección, limpieza, clustering y app comparten dataset_depurado.csv y dataset_con_clusters.csv. El análisis completo de asociación está en clustering.md, con mínimo de 20 pares por grupo.

Fase 4A: 887 casos completos elegibles de 1117 registros conservados; 3 conflictos históricos pendientes excluidos del análisis principal.
K-Means usa seis variables y k=2 entre 2 y 10. DBSCAN usa eps=1.666296, min_samples=12; clusters=1, ruido=21.
Un solo grupo de DBSCAN no acredita segmentación comercial útil. Ver comparación de k=2/3/4 y sensibilidad a títulos compartidos en clustering.md.

Clasificador independiente por terciles del promedio de rangos percentiles de Plays, Wishlist y Backlogs: RandomForestClassifier; n prueba=222, F1 macro=0.5577, base=0.1546. Los clusters descriptivos no se utilizan como objetivo ni predictores.

## Que debo verificar manualmente

- Resolver plataformas de discrepancias históricas y roles de Team.
- Interpretar distancias de puntuaciones separadas de asociación de orden.
- Confirmar estabilidad de perfiles; popularidad no equivale a éxito comercial.


````

## Origen: Final/reports/pruebas_auditoria.txt

SHA-256: `f600d2733761d14bc53ce6da2a8f8efd540e5798a282b73f85a83cb144b4ed37`

````text
..................................................................       [100%]
66 passed in 2.24s

````

## Origen: Final/reports/pruebas_auditoria2.txt

SHA-256: `86de97f2b97ddd34324a344033d62e89925b4c8ebf3d38f9868cbe82ec777f47`

````text
........................................................................ [ 87%]
..........                                                               [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
82 passed, 1 warning in 3.40s

````

## Origen: Final/reports/pruebas_auditoria2_modulo.txt

SHA-256: `7f74b5c41a123764a12a643bfc283aaf38bbd3e19eaa9598322769cf8261a6de`

````text
........................................................................ [ 87%]
..........                                                               [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
82 passed, 1 warning in 3.11s

````

## Origen: Final/reports/pruebas_modelo.txt

SHA-256: `15c5c3531947a2c62554f2d7e88a06fac4af3ef770882740df38fc83f1015189`

````text
........................................................................ [ 97%]
..                                                                       [100%]
74 passed in 2.35s

````

## Origen: Final/reports/pruebas_revision_integral.txt

SHA-256: `90305ffe89f88de3c9a260829f5fe870c57747560987653c6b58bcc1666bd82e`

````text
........................................................................ [ 85%]
............                                                             [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
84 passed, 1 warning in 3.51s

````

## Origen: Final/reports/revision_anteproyecto_v2_rubrica.md

SHA-256: `342e9e6306be8bb12187509c6542ca937876f1eb21d57d635f021229db28fc5d`

````text
# Revisión del anteproyecto v2.0 contra la rúbrica

> Revisión documental previa a las correcciones de implementación. Para el estado vigente de Final, consultar correcciones_auditoria.md; las cifras históricas de esta revisión no sustituyen los artefactos regenerados.

Fecha de revisión: 8 de noviembre de 2026. Esta es una revisión; no se modificaron ni reescribieron el anteproyecto, su fuente LaTeX o la rúbrica.

## Fuentes, alcance y criterio

- Anteproyecto evaluado: `Proyecto/Anteproyecto_v2_320317264_320060829_320206968.pdf`, 25 páginas PDF. Portada: versión 2.0 actualizada el 08/11/2026.
- Rúbrica: `Proyecto/instruct/ProyectoMineríaDatos.pdf`, diapositiva 5. Las instrucciones de entrega final están en su diapositiva 4.
- Maestro de datos designado por el usuario: `Proyecto/data/processed/games_curated.csv`, 1,117 filas y 42 columnas. Es la fuente original para el trabajo actual de Final; el archivo de 1,512 filas es su antecedente histórico, no la entrada actual del modelo.
- Para distinguir planificación de ejecución se consultaron los artefactos existentes en `Final`. Su presencia no se contabiliza como evidencia ya incluida en el anteproyecto.
- Las referencias de página siguientes usan la **numeración impresa del anteproyecto**: p. 1 corresponde a la página PDF 3; p. 23, a la página PDF 25. La portada no tiene número impreso.
- No se asigna una nota numérica: la rúbrica no da ponderaciones y la evaluación final corresponde al profesor. Las brechas describen qué evidencia permitiría defender el nivel excelente, no una garantía de obtenerlo.
- La revisión bibliográfica es de trazabilidad interna. No se verificaron en internet las cifras de industria, la situación de Marathon ni los contenidos de los artículos citados.

**Diagnóstico:** el documento tiene una planificación extensa y una auditoría inicial útil, pero promete explicar éxito comercial y clasificar perfiles de mercado sin una definición verificable de esas etiquetas. La implementación actual responde una pregunta más acotada: clasificación contemporánea de popularidad relativa dentro de Backloggd. La principal corrección pendiente es acordar y registrar ese alcance, no añadir más algoritmos.

## 1. Matriz de los nueve rubros

| Rubro de la rúbrica | Evidencia que ya contiene el documento | Qué falta para defender 9.5–10 | Acción concreta |
|---|---|---|---|
| Objetivo | Objetivo general y siete específicos, pp. 1–2. Incluyen limpieza, EDA, Pearson, popularidad, clustering, clasificación y app. | Una definición única de resultado y alcance: se mezclan éxito comercial, recepción, popularidad y perfil de cluster. El maestro carece de ventas verificadas y etiquetas de fracaso/GaaS. | Acordar que la clasificación usa terciles del índice de popularidad y que clustering es una tarea descriptiva separada; registrar la decisión en ESPEC-2.0 o una revisión posterior, sin presentar los terciles como clusters. |
| Contexto | Origen Backloggd/Kaggle, variables y cobertura, p. 3; limitaciones y sesgo, p. 4; trabajos relacionados, p. 5; motivación de negocio, pp. 11–12. | Vincular cada afirmación relevante con una fuente identificable y distinguir contexto industrial de lo observable en esta muestra. Falta documentar fecha de captura, alcance de Team y procedencia/plataforma de cada nota crítica. | Crear una ficha de datos del maestro con dimensiones, hash, campos, ausencias, fecha conocida/desconocida y fuentes; añadir una matriz afirmación–referencia para las cifras del contexto. |
| Estrategia | Seis fases CRISP-DM, pp. 5–7; arquitectura y reglas de coherencia, pp. 7–9; entregables y responsables. | Un protocolo ejecutable y consistente: objetivo supervisado, atributos, tratamiento de listas/ausencias, fórmula de popularidad, cortes, selección de parámetros y separación de entrenamiento/prueba. | Referenciar un protocolo metodológico versionado que corresponda al código real, con una tabla tarea–entrada–salida–criterio de aceptación. |
| Expectativas | Sección específica, p. 13: asociación de notas, popularidad, perfiles, clasificador y aplicación. | Criterios de aceptación observables y límites: no se puede comprobar reducción de pérdidas o riesgo de inversión con esta muestra. Una ausencia de relación o unos clusters poco útiles también deben admitirse como hallazgo. | Para cada expectativa registrar indicador, evidencia y condición de cumplimiento; por ejemplo, informe con n e IC de Pearson, comparación contra base mayoritaria y demo local funcional. No fijar una buena métrica después de observarla. |
| Plan de trabajo (baseline vs. Real) | Cronograma de 19 actividades con fechas y responsables, pp. 9–10; catálogo de CI, pp. 14–22. | El plan es baseline: no hay tabla de ejecución real, desviaciones, causas ni cambios aprobados. También falta explicar dependencias y el efecto de la revisión de noviembre. | Elaborar un registro con fechas previstas/reales comprobables, estado, evidencia, desviación en días, causa y responsable. Marcar como desconocidas las fechas reales sin registro; no reconstruirlas a partir del baseline. |
| Metodología de modelado | Pearson segmentado, K-Means, DBSCAN, Naive Bayes, árbol y MLP; silueta, estabilidad, F1 y validación de 10 pliegues, pp. 6–7. Reconoce riesgo de fuga. | Definir el target y resolver la incompatibilidad entre predecir clusters usando calificaciones y formar clusters con esas mismas calificaciones. Faltan parámetros/rangos, preprocesamiento dentro de folds, base comparativa y protocolo de estabilidad. | Documentar el protocolo que realmente se ejecutará; para Final, terciles calculados en entrenamiento, cinco folds agrupados y prueba reservada. Completar los modelos prometidos o aprobar su sustitución y justificarla antes de atribuir cumplimiento a esta versión. |
| Eficiencia en herramientas MD | Python, Orange y Weka, propuesta propia y demo están previstos; CI específicos y arquitectura de integración, pp. 6–9 y 17–19. | Evidencia de uso efectivo de herramientas de la materia y explicación de la aportación del equipo. Exportar CSV/ARFF no prueba que se hayan ejecutado Orange/Weka; usar asistentes tampoco demuestra dominio del equipo. | Guardar flujos/configuraciones, versiones, capturas y resultados de Orange/Weka con las mismas particiones y atributos; preparar una demo donde los integrantes expliquen y reproduzcan las decisiones del pipeline Python. |
| Resultados y Conclusiones | Auditoría preliminar: duplicados, estimaciones y cambio de Pearson, p. 4. No incluye resultados finales de clustering/clasificación ni conclusiones del proyecto. | Resultados que respondan cada objetivo, interpretación crítica y límites. La rúbrica exige llegar a resultados y concluir; una lista de actividades futuras no acredita ese rubro. | Integrar, en la futura entrega final, tablas y gráficos calculados, matriz de confusión, comparación con la base y conclusiones ligadas a cada objetivo. Explicar también el cluster dominante de DBSCAN y el bajo desempeño de la clase media. |
| Fuentes | Bibliografía final de 15 entradas, p. 23; citas autor–año visibles para CRISP-DM y Streamlit. CONFIGTEC-1.0 declara biblatex APA. | Uso de citas en el cuerpo, no solo lista final; correspondencia entre las afirmaciones y las referencias, datos bibliográficos completos y trazabilidad de las notas agregadas. Una configuración APA no acredita por sí sola el cumplimiento. | Auditar afirmación por afirmación: identificar el artículo de 1,642 juegos/680,000 reseñas, la fuente de los datos Newzoo vía Game World Observer, Wall Street Journal y los casos GaaS; completar o retirar lo no sustentado y comprobar el formato APA. |

La rúbrica es de proyecto final. Que un anteproyecto aún no contenga resultados o fechas reales no equivale a que el documento sea inválido como planificación; sí significa que esa evidencia deberá aportarse para defender esos rubros en la entrega final.

## 2. Inconsistencias y problemas de trazabilidad

### 2.1 Dentro del PDF

| Hallazgo | Localización y evidencia | Implicación y acción recomendada |
|---|---|---|
| Fechas de entrega sin distinguir hitos | Portada: 30/09/2026; cronograma: redacción 01–05/10; ANTE-2.0: 08/11; entrega final: 25/11. | No es necesariamente una contradicción si son entrega original, revisión y entrega final, pero la portada no lo explica. Identificar cada fecha por su tipo; no cambiar todas a noviembre sin conservar la historia. |
| Dependencias de versiones posteriores | ANTE-2.0 del 08/11 es base de DATA-RAW-1.0 del 01/10, p. 14; ESPEC-2.0 del 08/11 orienta CLEAN-SCRIPT-1.0 del 08/10 y EDA-REPORT-1.0 del 22/10, p. 15. | Las relaciones pueden ser retrospectivas por revisión, pero falta ese registro. Distinguir dependencia histórica de validación o actualización posterior y registrar el cambio de baseline. |
| Reporte de correlación fechado antes de terminar el análisis | EDA-REPORT-1.0 incluye correlación por género/estudio y fecha 22/10, p. 17; cronograma sitúa correlaciones del 22 al 29/10, p. 10. | El CI no puede ser un reporte final completo el día que empieza parte de su contenido, salvo que sea versión parcial. Separar EDA y correlación o establecer revisiones y fechas de cierre. |
| Reporte de clustering antes de su interpretación | CLUSTER-REPORT-1.0 promete resultados identificados e interpretados el 05/11, p. 17; interpretación programada del 05 al 10/11, p. 10. | Aclarar si el 05/11 es ejecución preliminar y el 10/11 la versión interpretada. No usar la misma fecha como cierre de ambas cosas. |
| Responsable de correlaciones ambiguo | Actividad 9: García Cortés, p. 10; EDA-REPORT-1.0, que incluye correlación: Lara Hernández, p. 17; RH-ANALISTA atribuye generación de EDA a Lugo Manzano, p. 22. | Puede haber colaboración, pero no se distinguen autor, ejecutor y aprobador. Registrar esos tres roles para el entregable; evitar tres responsables únicos implícitos. |
| Script fechado dentro de su desarrollo sin tipo de hito | CLEAN-SCRIPT-1.0: 08/10, p. 15; desarrollo: 06–10/10, p. 10. | Es una ambigüedad, no un error probado: el 08/10 podría ser primera versión. Etiquetar creación, validación y cierre. |
| Referencia de código inexistente en el árbol propuesto | Figura 1 usa `src/models`, p. 8; el árbol de esa misma página propone `src/clustering.py` y `src/classification.py`, sin `src/models`. | Elegir una referencia coherente para el nodo de modelado; la figura no debe apuntar a un módulo no definido. |
| Falta el CI de la curación que se cita como evidencia | Auditoría atribuida a `src/cleaning.py` y `src/curate.py`, p. 4; el árbol y CLEAN-SCRIPT-1.0 solo describen cleaning, pp. 8 y 15. | Incorporar curate como componente del CI o identificar un CI propio, y declarar qué archivo genera. Sin ello no se reproduce la exclusión de crítica sintética a partir de la arquitectura descrita. |
| “Todos los registros” no identifica la población correcta | P. 4 llama así a r=0.600 con 1,104 pares; el documento también maneja 1,512 registros originales y 1,117 únicos. | Ese cálculo corresponde a juegos únicos con ambos valores, incluyendo estimaciones, no a las 1,512 filas. Rotular población, deduplicación, filtro y n en cada estimación. |
| Uso de crítica sintética no resuelto en todas las tareas | P. 4 excluye estimaciones para usuarios–crítica; pp. 6 y 13 vuelven a mencionar `Metacritic Rating` para derivados, clustering y supervisión sin el mismo filtro explícito. | La regla de exclusión debe cubrir todas las tareas que interpreten esa variable como prensa. Especificar `critic_score_final` y su procedencia, sin imputar la nota sintética como observación real. |
| Cuatro señales frente a tres en expectativas | Objetivo de popularidad, p. 1: Plays, Playing, Backlogs, Wishlist; expectativas, p. 13: Plays, Wishlist y Backlogs. | La omisión de Playing cambia la operacionalización de actividad. Declarar las cuatro señales y justificar si una tarea usa solo algunas. |
| Predictoras y construcción de clusters incompatibles | P. 6 promete excluir de los predictores lo usado para formar clusters; p. 13 propone clusters con calificaciones, popularidad y género, y después clasificación mediante género y calificaciones. | No se pueden mantener simultáneamente esas tres afirmaciones sin especificar qué tarea usa qué campo. Separar la clasificación de terciles de la segmentación o rediseñar explícitamente el objetivo supervisado. |
| “Asociación” se interpreta como “parecido” de notas | Objetivo de discrepancia, p. 1, y expectativas, p. 13: Pearson se utiliza para inferir notas más parecidas o diferentes. | Correlación alta no acredita acuerdo ni brecha pequeña. Conservar Pearson para asociación; una diferencia requiere escala confirmada y una medida específica de brecha/acuerdo. |
| Alcance causal/comercial frente a limitaciones admitidas | P. 4 limita conclusiones y reconoce ausencia de fracasos y de finanzas empíricas; pp. 1, 3, 11 y 13 hablan de factores determinantes, éxito comercial y reducción de pérdidas por elección de género. | El contexto puede motivar el estudio, pero no convertirse en un resultado que el dataset no identifica. Limitar conclusiones a asociaciones observadas y no atribuir causas de fracaso a la falta de análisis empresarial. |
| Fuentes narradas sin referencia identificable | Pp. 3, 5 y 11 mencionan Game World Observer, un estudio en ScienceDirect con 1,642 juegos y 680,000 reseñas y Wall Street Journal; p. 23 no permite identificar inequívocamente esas fuentes. | Añadir autor, fecha, título y cita vinculada. “ScienceDirect” es una plataforma, no la identificación de un estudio. Revisar también fecha y soporte de las afirmaciones sobre Marathon. |

**Comprobaciones que no deben convertirse en errores inventados:** las fases del texto y de la tabla 1 mantienen la secuencia 1–6. Los números 1–19 del cronograma son actividades, no una segunda numeración de fases. Se cuentan siete objetivos específicos, de acuerdo con ESPEC-2.0. El 25/11/2026 sí cae en miércoles. Los identificadores ANTE-2.0, ESPEC-2.0, CLEAN-SCRIPT-1.0, DATA-CLEAN-1.0, CP-1.0, CLUSTER-REPORT-1.0 y MODEL-SUP-1.0 no cambian de escritura en las fichas revisadas. No detecté un identificador de CI mal escrito; los problemas son de fechas, dependencias, alcance y referencias de archivos. Los 382 duplicados exactos salvo ID también coinciden con el antecedente histórico comprobado.

### 2.2 Diferencias con las instrucciones y la implementación actuales

Estas diferencias **no son contradicciones internas del PDF**. Se registran para no presentar una demo distinta de la que el documento promete.

| Tema | Anteproyecto | Estado actual / decisión del usuario | Acción pendiente |
|---|---|---|---|
| Fuente original | DATA-RAW-1.0 describe 1,512 filas sin depurar; la versión de trabajo es games_actualizado_metacritic.csv. | El usuario designó `games_curated.csv` como original del trabajo en Final: 1,117 filas y 42 columnas. | Registrar la procedencia histórica y una versión del insumo actual. No describir la copia curada como si nunca hubiese sido depurada. |
| Objetivo supervisado | Perfil obtenido del clustering; MODEL-SUP depende de CLUSTER-REPORT. | Nivel bajo/medio/alto por terciles del índice de cuatro señales; no depende de la etiqueta de cluster. | Acordar una sola definición y reflejarla en objetivos, expectativas, CI, diagrama y demo. |
| Algoritmos y evaluación | Naive Bayes, árbol, MLP y 10 pliegues en Orange/Weka/Python. | Python compara base mayoritaria, regresión logística y bosque, con cinco folds agrupados y prueba reservada. | Completar los modelos prometidos o justificar una revisión de alcance. No renombrar el bosque como árbol único ni afirmar que se usaron 10 folds. |
| Estructura de carpetas | `app/Inicio.py`, `data/processed`, `artifacts`. | La estructura sugerida por el usuario usa `app.py`, `data/clean`, `models`; Final sigue esta segunda organización con nombres propios de módulos y artefactos. | Crear un mapa CI–ruta–archivo real. La estructura sugerida no obliga a renombrar carpetas durante esta revisión. |
| Evidencia de otras herramientas | Comparación ejecutada de Orange y Weka contra Python. | Hay exportaciones CSV/ARFF e instrucciones; no evidencia de ejecución gráfica de Orange/Weka en Final. | Ejecutar y registrar las herramientas antes de afirmar cumplimiento. |
| Publicación | Streamlit Community Cloud en DEPLOY-1.0 y demo que lo valida. | El usuario pidió conservar todo localmente, sin push ni despliegue público. | Registrar el cambio de alcance y confirmar si la demo local cumple la evaluación del curso; no marcar DEPLOY-1.0 como realizado. |
| Power BI | Se descarta expresamente, pp. 6 y 16. | Se mencionó entre las herramientas iniciales y Final ofrece instrucciones de importación. | Acordar el alcance; no tratar la ausencia de Power BI como incumplimiento de este PDF, que lo excluye. |

## 3. Objetivos específicos: verificabilidad y redacción propuesta

Las formulaciones siguientes son propuestas para aprobación del equipo, no cambios aplicados al documento. Se numeran en el mismo orden de la sección 1.2. La escala, el origen de las notas y los roles de Team no se dan por verificados.

| Objetivo | Diagnóstico | Formulación verificable propuesta |
|---|---|---|
| 1. Depurar y estructurar | Factible; “garantizar la calidad” es absoluto y no define qué se comprueba. El insumo actual ya está curado. | “Validar el maestro games_curated.csv y generar una vista analítica reproducible, conservando su hash, documentando faltantes, listas, fechas y procedencia crítica, y verificando con pruebas los formatos, la unicidad de título/fecha y la exclusión de estimaciones financieras de los modelos.” |
| 2. EDA | Factible en su mayor parte; la atribución a desarrolladores no está verificada y faltan productos de aceptación. | “Generar tablas de frecuencias por género, organización de Team y década, y estadísticas de distribución de notas y las cuatro señales de popularidad, informando n y ausencias; conservar las tablas y figuras que sustenten cada descripción.” |
| 3. Discrepancia perceptiva | Pearson cuantifica asociación, no discrepancia. “Variaciones significativas” exige una prueba de diferencias entre grupos, no solo r por grupo. | “Estimar Pearson entre Rating y critic_score_final en pares completos, globalmente y por género y organización, informando n, IC95 % y corrección por comparaciones múltiples; omitir estimaciones con menos de diez pares o sin variación y no interpretar diferencias de r como diferencias probadas entre grupos.” |
| 4. Popularidad real | Los datos miden declaraciones en Backloggd, no liderazgo de mercado, usuarios únicos, ventas o retención. | “Describir Plays, Playing, Backlogs y Wishlist en la muestra, construir un índice explícito como el promedio de log(1 + conteo), y comparar sus distribuciones por género y organización junto con las calificaciones, identificando qué conclusiones dependen de los pesos elegidos.” |
| 5. Perfiles de mercado | El agrupamiento es realizable; “culto”, “sobrevalorado”, éxito comercial y causas de pérdidas no son etiquetas disponibles. | “Ajustar K-Means y DBSCAN sobre las cuatro señales transformadas con log1p y estandarizadas, documentar parámetros, silhouette, tamaños, ruido y medianas por grupo, y evaluar estabilidad con un procedimiento declarado antes de nombrar e interpretar los perfiles; usar género para describirlos posteriormente.” |
| 6. Clasificación de perfil | No está definida la etiqueta y puede ser circular si el target se deriva de las mismas notas usadas para predecirlo. Además, usar notas publicadas impide presentarlo como pronóstico previo al estreno. | “Comparar clasificadores que estimen popularidad baja, media o alta, definida por terciles del índice obtenidos solo en entrenamiento, usando género, organizaciones, década, Rating y critic_score_final; reservar prueba por título y evaluar con F1 macro, balanced accuracy y matriz de confusión frente a una base mayoritaria, ajustando el preprocesamiento dentro de cada fold.” |
| 7. App y comunicación | Desarrollar y demostrar es verificable; el despliegue público no está autorizado actualmente. Falta definir pruebas funcionales y accesibilidad de hallazgos. | “Entregar una app Streamlit ejecutable localmente que permita explorar los datos, consultar asociación de notas, perfiles y estimaciones del clasificador, y mostrar sus límites; comprobar carga, filtrado, ausencia de resultados e inferencia con notas faltantes y proporcionar instrucciones reproducibles.” |

**Límites de estas propuestas:** el umbral n≥10 es una regla operativa usada por Final, no una garantía de potencia estadística. La estabilidad del clustering sigue siendo trabajo pendiente: ejecutar una sola vez con semilla fija no la demuestra. El protocolo de cinco folds actual debe acordarse frente a los diez del anteproyecto. Si el equipo desea conservar Naive Bayes, árbol y MLP como compromiso, debe ejecutarlos y documentarlos; esta revisión no los sustituye automáticamente.

## 4. Cinco preguntas difíciles para la demo

### 1. “¿Dónde demuestran que elegir un género provoca fracasos GaaS o que su modelo reduce pérdidas?”

**Respuesta defendible:** no lo demostramos con este maestro. Analizamos asociaciones entre recepción, actividad e interés en una muestra sesgada de juegos populares. No contiene etiquetas verificadas de fracaso, condición GaaS ni ventas/costos empíricos que permitan medir ese efecto.

**Evidencia para mostrar:** limitaciones del anteproyecto, p. 4; inventario de campos en `Final/reports/inspeccion.json`; fuente `games_curated.csv`; exclusión de finanzas en `Final/src/data.py`. La población complementaria mencionada en el PDF es trabajo futuro y no evidencia incorporada.

### 2. “Si Pearson es 0.544, ¿cuántos puntos discrepan usuarios y críticos? ¿Usaron notas inventadas?”

**Respuesta defendible:** r=0.5444 cuantifica asociación lineal y no se puede convertir en una cantidad de puntos de desacuerdo. Se usaron 890 pares completos, con IC95 % [0.4965, 0.5891]. Las 218 filas sin critic_score_final se conservaron como juegos, pero no aportaron una nota de prensa a Pearson. La etiqueta de procedencia del CSV no equivale a una comprobación externa.

**Evidencia para mostrar:** `Final/reports/pearson_global.csv`, `Final/reports/pearson_generos.csv`, `Final/reports/pearson_organizaciones.csv`, `Final/src/data.py` y la correspondencia `critic_source`–`critic_score_final` del maestro. El rango observado de Rating es 0.7–4.8; no hemos validado externamente los extremos teóricos para calcular una brecha normalizada.

### 3. “¿El clasificador aprende algo o simplemente reconstruye los conteos usados para fabricar su etiqueta?”

**Respuesta defendible:** el target actual son terciles del índice, no clusters. Los conteos y el índice no entran a los predictores. Se reservan títulos completos para prueba antes de definir los cortes; cada fold vuelve a ajustar cortes, codificadores e imputación con entrenamiento. Esto reduce fugas directas, pero no elimina el sesgo del muestreo ni la dependencia entre franquicias.

**Evidencia para mostrar:** `Final/src/config.py`, `Final/src/modeling.py`, `Final/tests/test_pipeline.py`, `Final/data/clean/juegos_modelo.csv` y `Final/reports/metricas.json`. Hay 895 juegos en entrenamiento y 222 en prueba. Los cortes del entrenamiento son 5.836372 y 6.679875. Como usa notas publicadas, no debe venderse como predicción antes del lanzamiento.

### 4. “¿Por qué esos clusters son perfiles de mercado útiles y no solo juegos con más o menos actividad?”

**Respuesta defendible:** aún no hay evidencia suficiente para esa etiqueta comercial. K-Means seleccionó dos grupos y principalmente separa magnitudes de las señales. DBSCAN deja 1,083 juegos en el grupo principal, ocho en otro y 26 como ruido; su silhouette sin ruido de 0.637 no demuestra que la segmentación sea útil para tomar decisiones de mercado. Falta comprobar estabilidad y sensibilidad de pesos/parámetros.

**Evidencia para mostrar:** `Final/reports/seleccion_kmeans.csv`, `Final/reports/seleccion_dbscan.csv`, `Final/reports/perfiles_kmeans.csv`, `Final/reports/perfiles_dbscan.csv` y `Final/reports/figures/perfiles.png`. No afirmar que -1 es un perfil ni llamar “fracasos” a los juegos con pocos Plays.

### 5. “¿Qué aporta su propuesta Python, cuánto mejora y dónde está la comparación real con Orange/Weka?”

**Respuesta defendible:** la aportación implementada es un pipeline reproducible con procedencia, listas múltiples, partición por títulos, terciles internos, validación y demo local. En Python se compararon base mayoritaria, regresión logística y bosque; este último obtuvo F1 macro 0.5649 y accuracy 0.5856 en la prueba reservada, frente a F1 macro 0.1846 de la base. Eso es evidencia de esta partición, no de superioridad comercial ni de superioridad estadística frente a Orange/Weka.

**Evidencia para mostrar:** `Final/reports/comparacion_modelos.csv`, `Final/reports/validacion_cruzada.csv`, `Final/reports/metricas.json`, `Final/reports/matriz_confusion.csv`, `Final/src/modeling.py`, pruebas y app local. La clase media tiene F1≈0.386, límite que debe explicarse. Los archivos Orange/Weka son entradas exportadas, no resultados de ejecuciones; completar esa evidencia sigue pendiente.

## Orden de atención recomendado

1. Acordar y registrar alcance: popularidad relativa, target por terciles, fuente curada y demo local. Esta decisión evita que objetivos, CI y demo describan proyectos distintos.
2. Cerrar el protocolo de evaluación y el compromiso de algoritmos/herramientas; después obtener las evidencias faltantes de Orange/Weka y estabilidad.
3. Registrar el plan real contra el baseline con fechas comprobables y cambios aprobados, preservando el historial de octubre.
4. Vincular cada afirmación de contexto a una referencia y cada conclusión a una salida calculada.
5. Preparar la demo para mostrar tanto resultados como límites, incluyendo la clase media y el cluster dominante de DBSCAN.

## Que debo verificar manualmente

- Que el PDF v2.0 encontrado y la rúbrica de cinco diapositivas sean exactamente los documentos que el profesor evaluará; no se eligió main.pdf como sustituto.
- Fechas reales, autores, aprobadores y estado de CI: no se infieren de las fechas previstas ni de la fecha de modificación de archivos.
- Si la demo local satisface el requisito del profesor y cómo registrar la cancelación del despliegue público.
- Escala teórica de Rating, plataforma/fecha de notas, funciones de Team, deduplicación histórica y fecha de captura.
- Fuentes originales de cifras de mercado, casos GaaS y artículos; formato APA de citas en el cuerpo y bibliografía. Esta revisión no hizo comprobación externa de esos hechos.
- Que ninguna exportación CSV/ARFF se presente como ejecución ya realizada de Orange/Weka y que ningún artefacto actual se atribuya al PDF si no está incluido en él.
- Aprobar cualquier cambio de objetivos, folds, algoritmos, estructura o identificadores antes de modificar el anteproyecto; aquí solo se proponen acciones.

````

## Origen: Final/reports/revision_graficas.md

SHA-256: `3bc26135183c7c82db2acc7fc7c28375ff7a19bda71dc607bd2a135d46620200`

````text
# Corrección de gráficas e identidad visual

## Cifras e intervalos

Las líneas amarillas son barras de error y se conservan con sus desviaciones originales. Las etiquetas de CV se sitúan encima del extremo superior más 10 píxeles; las de permutación, a la derecha del extremo superior más 10 píxeles. Esto evita que una línea atraviese el valor numérico sin desplazar los datos.

La leyenda comparativa pasa debajo del gráfico para liberar ancho. La matriz y la importancia por permutación usan ancho completo para mantener legibles sus títulos y etiquetas; los rangos estadísticos originales permanecen intactos.

## Ejes logarítmicos

Se conservan los conteos y la escala logarítmica. Se muestran etiquetas en potencias de diez y se ocultan las marcas menores que se amontonaban; cambiar la densidad de etiquetas no transforma los valores.

## Identidad del documento adjunto

La paleta se centraliza en `src/visualizacion.py` y genera variables CSS compartidas. Se aplica en Inicio, Exploración, Predicción y Modelo, conservando la tipografía cómic, las rutas y la navegación existentes.

Plays usa cian; Backlogs, violeta; Wishlist, dorado. Los paneles y gráficos combinan azul marino y morado; la matriz usa una escala de oscuro a claro y texto de contraste adaptado al valor de cada celda.

En pantallas estrechas, las figuras densas conservan un ancho de lectura de 760 px con desplazamiento horizontal dentro de su panel. Se comprobó que el documento mantiene el ancho del viewport de 390 px.

## Archivos de implementación modificados

- `src/visualizacion.py`: nuevo módulo de tokens y etiquetas fuera de intervalos.
- `src/ui.py`: tema Plotly y generación de variables CSS.
- `assets/css/persona5.css`: colores, paneles, foco y contenedores responsivos.
- `app.py`: colores de la página de inicio y versión del tema.
- `pages/1_Exploracion.py`: paleta de señales y boxplots.
- `pages/2_Prediccion.py`: paleta y énfasis cian en el resultado.
- `pages/3_Acerca_del_modelo.py`: intervalos, leyenda, matriz y distribución de figuras.
- `tests/test_visualizacion.py`: comprobaciones de integridad de datos y escalas en la presentación.

## Verificaciones ejecutadas

- 21 pruebas aprobadas: pruebas de visualización y pruebas existentes de pipeline/páginas. Registro: `tables/pruebas_revision_visual.txt`.
- SHA-256 de 20 archivos en `data/raw`, `data/clean` y `models`: todos idénticos antes y después. Evidencias: `tables/integridad_visual_antes.json` y `tables/integridad_visual_resultado.json`.
- Inspección de Inicio, Exploración, Predicción y Modelo en el navegador.
- Selector de señal de Exploración cambiado a Wishlist: estado seleccionado y gráfica actualizados.
- Barras comparativas y permutación: cifras separadas de los intervalos; títulos legibles.
- Gráficas logarítmicas: etiquetas mayores legibles, sin dígitos menores encimados.
- Comprobación móvil: figura de 760 px desplazable dentro del documento de 390 px; cifras visibles al desplazar el panel.
- Compilación Python y comprobación de espacios en el diff: correctas.

El detector de diseño señala bordes inclinados y una curva de animación que ya pertenecían al tema Persona. Se conservan por la indicación de mantener esa identidad; no son errores en las mediciones.

Las visualizaciones Plotly dinámicas y su exportación usan el tema actualizado. No se regeneran las figuras históricas de los reportes de análisis: esta revisión se limita a la presentación de la web y no vuelve a entrenar modelos.

Sin pendientes.

````

## Origen: Final/reports/tipografia.md

SHA-256: `13285a0b33f1891e17d68ef95883534bd582f95677613b2eee6c789471c24c8e`

````text
# Tipografía cómic de la web

Se usa `assets/fonts/Persona5main.ttf` mediante la familia CSS `ComicProyecto`. Los metadatos del archivo indican Comic Sans MS cursiva. La fuente contiene vocales acentuadas, ñ, ü y signos de apertura españoles; se conserva el texto Unicode en lugar de eliminar sus tildes.

La fuente se integra localmente en CSS, sin descargar tipografías externas. La caché depende de los hashes del CSS y de los bytes de la fuente para que una sustitución del archivo se refleje al recargar la aplicación.

Se aplica a títulos, menús, párrafos, formularios y configuración tipográfica de Plotly. Se conservan las fuentes de iconos y del código. Los valores de los deslizadores no se parten en líneas; los títulos reducen su tamaño en móvil y tienen margen frente al menú contraído.

## Verificaciones ejecutadas

- Compilación de los tres módulos Python modificados: correcta.
- Caracteres españoles y cifras comprobados con fontTools: presentes.
- Inicio y Predicción inspeccionados en navegador: fuente cómic visible, navegación operativa y tildes conservadas.
- Desplegable de década abierto y cerrado: opciones legibles.
- Valores 82 y 3.90 de los deslizadores: visibles completos en una línea.
- Inicio a 390 px: título legible, margen izquierdo de 40 px y ancho del documento igual al viewport, sin desbordamiento horizontal.
- Reinicio del servidor local para descartar la definición anterior de la fuente: completado.

Evidencias: `tables/tipografia_comic_inicio.jpg`, `tables/tipografia_comic_formulario.jpg` y `tables/tipografia_comic_movil.jpg`.

````

## Origen: Final/reports/verificacion_funcional.md

SHA-256: `8d7495477ba5dea4b508007189f4ad4ddf0fc47d3c2429bc6d1e38f63f60f093`

````text
# Verificación funcional local

Registro de la primera comprobación del 08/11/2026. La revisión posterior y el formulario actualizado (ambas notas vacías por defecto) se documentan en `revision_integral.md`; los casos siguientes conservan la evidencia histórica, no describen los valores iniciales actuales.

Fecha: 2026-11-08. Se verificó la aplicación servida en `http://127.0.0.1:8501/Consultar_modelo` mediante Chrome y se ejecutó de nuevo la suite desde `Final`.

## Resultados observados

| Comprobación | Resultado |
|---|---|
| Estado inicial de la nota crítica | Campo habilitado, vacío y ausencia desmarcada; no se propone una nota inventada. |
| Envío con nota vacía | Se bloquea y solicita escribir una nota o marcar explícitamente su ausencia. |
| Nota crítica 85, Rating 3.7, década 1980, sin géneros ni organizaciones seleccionados | Predicción medio; probabilidades sin calibrar: bajo 0.404308, medio 0.406572, alto 0.189120. Caso sintético de verificación del formulario, no un videojuego real. |
| Mismo formulario, marcando ausencia de nota crítica | Predicción bajo; probabilidades sin calibrar: bajo 0.513058, medio 0.378036, alto 0.108906. El campo 85 queda deshabilitado y se ignora para la predicción. Se muestra el aviso de imputación y posible sesgo residual. |
| Cinco vecinos de la consulta con ausencia explícita | Se muestran Peggle Deluxe (1475), Ms. Pac-Man (1454), Tetris (1203), Super Mario Bros. 3 (126) y Pac-Man (591), con distancias. Las etiquetas de cluster disponibles se adjuntan por ID; las vacías se explican en pantalla. |
| Pruebas automatizadas | `.venv314/bin/pytest -q`: 82 aprobadas en 3.71 s; una advertencia de joblib sobre detección de núcleos físicos, con uso de núcleos lógicos como alternativa. |
| Integridad de artefactos | SHA-256 de los dos datasets, Pipeline, metadata y vecinos coincide con `reports/manifest.json`. |
| Original | SHA-256 de `../Proyecto/data/processed/games_curated.csv` conserva el valor `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`. |

## Interpretación y decisiones

Se mantuvieron los artefactos y el modelo sin reentrenar: las verificaciones no identificaron un fallo funcional que lo justificara. Los casos del navegador complementan las pruebas automatizadas porque comprueban la interacción real del formulario y sus mensajes.

La ausencia de crítica sigue pudiendo cambiar la predicción. Este ejemplo cruza una frontera de decisión estrecha y no demuestra por sí solo una causa ni un efecto general; el diagnóstico agregado de cobertura y la limitación de la clase media permanecen en `modelo.md` y `correcciones_auditoria2.md`.

La verificación se hizo localmente, sin publicar archivos. Una etiqueta de cluster vacía en los vecinos significa que faltó información para agrupar ese juego; no se fabrica una pertenencia para completar la tabla.

## Que debo verificar manualmente

- Resolver identidad/plataforma de los conflictos históricos 117, 140 y 296 con evidencia externa.
- Confirmar el papel de las organizaciones de Team antes de llamarlas estudios desarrolladores.
- Revisar la representatividad y cobertura de las notas de prensa; quitar indicadores de ausencia no elimina automáticamente su influencia.
- Considerar que el recall de la clase medio es 27/80 (33.75 %) y que las probabilidades no están calibradas.

````

## Verificación de cierre tras consolidación

Comando: `python -m pytest -q`

````text
........................................................................ [ 71%]
.............................                                            [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
101 passed, 1 warning in 5.05s

````

## Verificación de cierre tras consolidación

Comando: `python reports/verificar_integridad.py`

````text
{
  "original_intacto": true,
  "artefactos_y_reportes_concuerdan": true,
  "filas_y_brecha": {
    "conservadas": 1117,
    "agrupadas": 887,
    "no_agrupadas": 230
  },
  "correlacion_recalculada": {
    "n": 887,
    "pearson_r": 0.5439095219775958,
    "pearson_p": 1.9359671271969552e-69,
    "spearman_rho": 0.5241770101377499,
    "spearman_p": 9.340096498724198e-64
  },
  "clusters_y_espacio_concordantes": true,
  "metricas_recalculadas": {
    "n_prueba": 222,
    "f1_macro": 0.5577027296634777,
    "exactitud": 0.5675675675675675
  }
}

````

## Cierre vigente de la entrega

El equipo declara cumplido el calendario técnico; no se inventan fechas exactas. La suite completa posterior a la consolidación aprobó 101 pruebas. Se recalcularon Pearson, Spearman, métricas de prueba y coherencia de clusters; el maestro, modelo y reportes cuantitativos coinciden con el manifiesto. El informe recompiló con 41 páginas, sin referencias indefinidas, desbordamientos horizontales ni anclas duplicadas. Las páginas modificadas se renderizaron y revisaron visualmente.

Los textos anteriores son un registro histórico completo. La comparación vigente es tables/comparativo_herramientas.csv: contiene escenarios de CV adicionales y explica sus diferencias metodológicas. Las verificaciones JSON con fechas anteriores describen el estado observado entonces y no sustituyen el cierre actual. Orange no tiene resultados. No se reentrenó el modelo ni se alteraron data/raw durante la limpieza.

Los prototipos de menú son repositorios anidados: sus cambios locales previos se conservaron en commits locales; el repositorio principal incorpora además sus archivos directamente, evitando referencias anidadas que quedarían incompletas al copiar la entrega. Git LFS no está instalado, por lo que se conservaron los punteros LFS ya existentes sin descargar archivos ni instalar herramientas. Esto afecta solo a videos del prototipo, no a la aplicación Streamlit vigente.

Los cuatro prototipos se incorporan como archivos ordinarios del repositorio principal; no quedan gitlinks. Sus metadatos de Git anteriores se conservan únicamente como respaldo local ignorado en .repositorios_locales, separado de los archivos de entrega. No se descargaron los videos ausentes de LFS.

## Corrección de contraste de las tarjetas de Inicio

Comando: `python -m pytest -q`

````text
........................................................................ [ 71%]
.............................                                            [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
101 passed, 1 warning in 5.23s

````

## Corrección de contraste de las tarjetas de Inicio

Comando: `python reports/verificar_integridad.py`

````text
{
  "original_intacto": true,
  "artefactos_y_reportes_concuerdan": true,
  "filas_y_brecha": {
    "conservadas": 1117,
    "agrupadas": 887,
    "no_agrupadas": 230
  },
  "correlacion_recalculada": {
    "n": 887,
    "pearson_r": 0.5439095219775958,
    "pearson_p": 1.9359671271969552e-69,
    "spearman_rho": 0.5241770101377499,
    "spearman_p": 9.340096498724198e-64
  },
  "clusters_y_espacio_concordantes": true,
  "metricas_recalculadas": {
    "n_prueba": 222,
    "f1_macro": 0.5577027296634777,
    "exactitud": 0.5675675675675675
  }
}

````

### Causa, solución y revisión visual del contraste

Streamlit sustituía max-width y object-fit de .sc-char, ampliando retratos sobre el texto. Se acotó el retrato con un selector específico y un ancho de 145 px; el encuadre conserva la cara. El texto y las cifras ahora tienen fondos opacos que cambian junto con sus colores, sin depender del barrido diagonal. Se eliminó la transición de color de las cifras para evitar estados intermedios grises.

La sección responde a su propio ancho: por debajo de 760 px separa las cifras del texto y oculta el retrato. En Chrome se comprobaron las tres tarjetas con cursor y selección, y navegación con flechas del teclado. Se revisaron una sección de 667 px y otra de 464 px sin desbordamiento horizontal de página, restaurando después el tamaño original del navegador. Contraste del cuerpo seleccionado: 18.06:1; cuerpo sin seleccionar: 16.72:1.

Capturas: figures/contraste_tarjetas_escritorio.png y figures/contraste_tarjetas_movil.png. El detector de diseño se ejecutó sobre la hoja de estilos; sus advertencias sobre elementos decorativos del tema existente no cambian la corrección delimitada. La ficha PRODUCT.md conserva el esquema anterior de la herramienta; actualizarla con init es una operación separada, no necesaria para este arreglo. Se conservaron modelos, datos y documentos analíticos.
