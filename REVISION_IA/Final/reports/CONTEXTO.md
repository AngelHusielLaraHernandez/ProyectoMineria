# Carpeta: Final/reports

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/BITACORA_UNIFICADA.md` · Bytes: 116471 · SHA-256: `d4769647743a5d2e505cf7f7fcf30abfdb4b79cc50e751e94f7b656b76f90b3f`

`````text
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

`````

## analisis.json

Ruta: `Final/reports/analisis.json` · Bytes: 819 · SHA-256: `df298240ede139bee39b1c275e326993fdebc7df6a2250854864a839b8d0089b`

````text
{
  "sha256_entrada": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "semilla": 42,
  "variables": [
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist",
    "Rating",
    "Metacritic Rating"
  ],
  "log1p": [
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist"
  ],
  "n_entrada": 1117,
  "n_completos": 887,
  "n_excluidos_clustering": 230,
  "n_cohorte_analitica": 1114,
  "n_conflictos_historicos": 3,
  "minimo_pares_correlacion": 20,
  "kmeans_k": 2,
  "dbscan_eps": 1.6662963557646437,
  "dbscan_min_samples": 12,
  "dbscan_ruido": 21,
  "dbscan_clusters": 1,
  "dbscan_silhouette_sin_ruido": null,
  "pca_varianza": [
    0.5838385635506382,
    0.16724298816152772
  ],
  "regla_eps": "Máxima separación x−y respecto de la cuerda, tras normalizar ambos ejes a [0,1]."
}
````

## clustering.md

Ruta: `Final/reports/clustering.md` · Bytes: 21886 · SHA-256: `9f9f8a377f6920035fb8388546e68118bb28dc9e35924c4de2c5b6b8f944193d`

````text
# Correlaciones y clustering de videojuegos

Entrada: `data/clean/dataset_depurado.csv`, SHA-256 `f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652`. Semilla: 42. La fuente permanece intacta.

Universo: 1117 juegos. Cohorte histórica elegible: 1114; conflictos pendientes excluidos: 3. Casos completos elegibles: 887; no agrupados por ausencias o conflictos: 230. La salida conserva todos los juegos.

## 1. Correlaciones

**Poblaciones y cobertura.** Las correlaciones usan pares completos para cada comparación. Se excluyen grupos con menos de 20 pares válidos, criterio más conservador que contar 20 juegos aunque falten notas; los n y las exclusiones se muestran explícitamente.

**Procedencia.** Metacritic Rating es la columna analítica producida por la fase 02: excluye estimaciones propias. Se valida la coherencia con critic_source y la brecha antes de calcular; las etiquetas del CSV no son una comprobación externa de cada nota.

### Catálogo: usuarios frente a prensa

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Catálogo | 1114 | 887 | 0.5439 | 1.936e-69 | 0.5242 | 9.34e-64 |

Pearson estima asociación lineal y Spearman asociación monótona basada en rangos; ninguno mide acuerdo ni causalidad. No se interpretan las diferencias entre coeficientes de grupos superpuestos como diferencias estadísticamente probadas.

### Géneros incluidos

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Adventure | 724 | 598 | 0.5746 | 7.923e-54 | 0.5443 | 1.975e-47 |
| RPG | 366 | 286 | 0.5014 | 1.305e-19 | 0.5175 | 5.464e-21 |
| Shooter | 260 | 223 | 0.5596 | 8.892e-20 | 0.5286 | 1.886e-17 |
| Platform | 239 | 188 | 0.6428 | 2.68e-23 | 0.5525 | 2.029e-16 |
| Indie | 207 | 166 | 0.5383 | 7.452e-14 | 0.5536 | 1.034e-14 |
| Puzzle | 133 | 110 | 0.3601 | 0.0001118 | 0.45 | 8.137e-07 |
| Strategy | 116 | 94 | 0.434 | 1.241e-05 | 0.3373 | 0.0008857 |
| Brawler | 106 | 97 | 0.616 | 1.874e-11 | 0.615 | 2.06e-11 |
| Simulator | 94 | 79 | 0.5347 | 3.846e-07 | 0.5026 | 2.356e-06 |
| Turn Based Strategy | 71 | 51 | 0.2514 | 0.0752 | 0.382 | 0.005668 |
| Fighting | 62 | 46 | 0.6188 | 4.577e-06 | 0.5826 | 2.159e-05 |
| Arcade | 61 | 39 | 0.7548 | 2.832e-08 | 0.6229 | 2.289e-05 |
| Visual Novel | 54 | 27 | -0.1042 | 0.605 | -0.1382 | 0.4917 |
| Tactical | 42 | 37 | 0.3467 | 0.03554 | 0.3602 | 0.02852 |
| Racing | 37 | 31 | 0.4916 | 0.004976 | 0.4357 | 0.01428 |
| Point-and-Click | 36 | 27 | 0.6546 | 0.0002117 | 0.6395 | 0.0003293 |

Cada juego participa una vez en cada género declarado, no solo en genero_principal. Los grupos se superponen y sus n no se suman para contar juegos.

### Géneros excluidos

| grupo | n_juegos | n | estado |
| --- | --- | --- | --- |
| Music | 21 | 18 | excluido: menos de 20 pares completos |
| Sport | 20 | 18 | excluido: menos de 20 pares completos |
| Card & Board Game | 13 | 10 | excluido: menos de 20 pares completos |
| Real Time Strategy | 9 | 9 | excluido: menos de 20 pares completos |
| Quiz/Trivia | 3 | 2 | excluido: menos de 20 pares completos |
| MOBA | 2 | 2 | excluido: menos de 20 pares completos |
| Pinball | 1 | 1 | excluido: menos de 20 pares completos |

### Organizaciones con más juegos

Se seleccionan las 15 organizaciones con más títulos antes de observar los coeficientes y luego se aplica el mínimo de 20 pares. Team mezcla desarrolladores y editores: esta tabla no acredita que todas estas organizaciones sean estudios desarrolladores.

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Nintendo | 170 | 125 | 0.441 | 2.636e-07 | 0.4611 | 6.257e-08 |
| Capcom | 64 | 51 | 0.6717 | 6.802e-08 | 0.541 | 4.152e-05 |
| Square Enix | 59 | 49 | 0.5977 | 5.767e-06 | 0.5985 | 5.569e-06 |
| Sega | 46 | 31 | 0.6937 | 1.509e-05 | 0.6595 | 5.449e-05 |
| Electronic Arts | 43 | 42 | 0.558 | 0.0001233 | 0.5347 | 0.0002643 |
| Konami | 31 | 22 | 0.618 | 0.002175 | 0.4439 | 0.03851 |
| Activision | 30 | 26 | 0.4132 | 0.03587 | 0.3851 | 0.05204 |
| Bandai Namco Entertainment | 28 | 25 | 0.7966 | 1.897e-06 | 0.7371 | 2.636e-05 |
| Ubisoft Entertainment | 27 | 27 | 0.6419 | 0.0003076 | 0.683 | 8.648e-05 |
| Atlus | 26 | 23 | 0.5554 | 0.005934 | 0.4705 | 0.02347 |
| Sony Interactive Entertainment | 24 | 22 | 0.7309 | 0.0001116 | 0.6341 | 0.001529 |

Excluidas dentro de las 15 más frecuentes:

| grupo | n_juegos | n | estado |
| --- | --- | --- | --- |
| Nintendo EAD | 22 | 15 | excluido: menos de 20 pares completos |
| Game Freak | 20 | 16 | excluido: menos de 20 pares completos |
| Sony Computer Entertainment | 18 | 15 | excluido: menos de 20 pares completos |
| Square | 18 | 10 | excluido: menos de 20 pares completos |

El CSV clustering_03_correlaciones_organizaciones.csv conserva el inventario completo, incluidos los grupos pequeños y la razón de exclusión.

### Comprobación por sesgo de las señales

| variable | asimetria_original | asimetria_log1p |
| --- | --- | --- |
| Plays | 1.836 | -1.763 |
| Playing | 4.845 | -0.359 |
| Backlogs | 1.834 | -0.8745 |
| Wishlist | 2.343 | -0.6942 |

Spearman se calcula también para todos los pares de las seis variables, sobre sus valores originales. Es una comprobación útil ante asimetría y relaciones monótonas no lineales; log1p no cambia el orden de los conteos, y por tanto no cambia sus rangos.

| variable_a | variable_b | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Plays | Playing | 1114 | 0.5395 | 3.729e-85 | 0.5471 | 5.442e-88 |
| Plays | Backlogs | 1114 | 0.5959 | 4.68e-108 | 0.5973 | 1.146e-108 |
| Plays | Wishlist | 1114 | 0.3498 | 2.033e-33 | 0.3413 | 8.696e-32 |
| Plays | Rating | 1101 | 0.1517 | 4.282e-07 | 0.08737 | 0.003716 |
| Plays | Metacritic Rating | 896 | 0.4144 | 1.681e-38 | 0.423 | 3.291e-40 |
| Playing | Backlogs | 1114 | 0.654 | 5.851e-137 | 0.7505 | 3.137e-202 |
| Playing | Wishlist | 1114 | 0.6279 | 3.35e-123 | 0.7013 | 1.13e-165 |
| Playing | Rating | 1101 | 0.2375 | 1.392e-15 | 0.4017 | 5.977e-44 |
| Playing | Metacritic Rating | 896 | 0.2634 | 1.103e-15 | 0.3458 | 1.449e-26 |
| Backlogs | Wishlist | 1114 | 0.7912 | 1.028e-239 | 0.8542 | ≈0 (límite numérico) |
| Backlogs | Rating | 1101 | 0.3927 | 6.634e-42 | 0.4133 | 1.137e-46 |
| Backlogs | Metacritic Rating | 896 | 0.4047 | 1.244e-36 | 0.433 | 3.098e-42 |
| Wishlist | Rating | 1101 | 0.4232 | 4.518e-49 | 0.5035 | 7.762e-72 |
| Wishlist | Metacritic Rating | 896 | 0.3273 | 8.158e-24 | 0.3698 | 2.044e-30 |
| Rating | Metacritic Rating | 887 | 0.5439 | 1.936e-69 | 0.5242 | 9.34e-64 |

Los CSV conservan p-valores y q de Benjamini–Hochberg por familia y método. Los p-valores de Spearman usan la aproximación asintótica de SciPy, no permutaciones exactas; con grupos pequeños o muchos empates deben interpretarse con cautela. Cuando SciPy devuelve cero por límite numérico, se muestra ≈0 y no se afirma una probabilidad exactamente nula.

El p-valor es bilateral y contrasta asociación nula, no igualdad de notas; la dependencia entre juegos/franquicias y los grupos superpuestos limita la inferencia.

### Coincidencia y discrepancia por género

**Criterio.** Se ordena por media de la brecha absoluta, en puntos sobre 100: menor valor significa mayor cercanía de puntuaciones. La brecha firmada Rating × 20 − Metacritic informa dirección; una media cercana a cero puede ocultar diferencias opuestas, por eso no se usa para ordenar.

| grupo | n | brecha_absoluta_media | brecha_media | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Visual Novel | 27 | 8.222 | -1.926 | -0.1042 | 0.605 | -0.1382 | 0.4917 |
| Brawler | 97 | 8.959 | -7.99 | 0.616 | 1.874e-11 | 0.615 | 2.06e-11 |
| Point-and-Click | 27 | 9 | -8.259 | 0.6546 | 0.0002117 | 0.6395 | 0.0003293 |
| Arcade | 39 | 9.051 | -8.128 | 0.7548 | 2.832e-08 | 0.6229 | 2.289e-05 |
| RPG | 286 | 9.346 | -7.871 | 0.5014 | 1.305e-19 | 0.5175 | 5.464e-21 |
| Indie | 166 | 9.542 | -8.133 | 0.5383 | 7.452e-14 | 0.5536 | 1.034e-14 |
| Turn Based Strategy | 51 | 9.569 | -7.529 | 0.2514 | 0.0752 | 0.382 | 0.005668 |
| Puzzle | 110 | 9.982 | -7.745 | 0.3601 | 0.0001118 | 0.45 | 8.137e-07 |
| Adventure | 598 | 10.11 | -8.468 | 0.5746 | 7.923e-54 | 0.5443 | 1.975e-47 |
| Simulator | 79 | 10.16 | -7.835 | 0.5347 | 3.846e-07 | 0.5026 | 2.356e-06 |
| Platform | 188 | 10.55 | -9.585 | 0.6428 | 2.68e-23 | 0.5525 | 2.029e-16 |
| Tactical | 37 | 11.03 | -9.946 | 0.3467 | 0.03554 | 0.3602 | 0.02852 |
| Strategy | 94 | 11.89 | -10.28 | 0.434 | 1.241e-05 | 0.3373 | 0.0008857 |
| Racing | 31 | 12 | -12 | 0.4916 | 0.004976 | 0.4357 | 0.01428 |
| Fighting | 46 | 12.02 | -10.67 | 0.6188 | 4.577e-06 | 0.5826 | 2.159e-05 |
| Shooter | 223 | 12.82 | -12.03 | 0.5596 | 8.892e-20 | 0.5286 | 1.886e-17 |

Menor distancia de puntuaciones (sin implicar concordancia de orden): Visual Novel, Brawler, Point-and-Click, Arcade, RPG. Mayores brechas absolutas: Shooter, Fighting, Racing, Strategy, Tactical.

La conversión de la fase 02 usa el máximo de cinco estrellas documentado de Backloggd y la escala 0–100 de prensa; no implica equivalencia psicométrica entre sus sistemas. La incertidumbre y las diferencias de composición impiden interpretar este orden como un ranking poblacional definitivo.

## 2. Preparación del clustering

**Variables.** Se usan Plays, Playing, Backlogs, Wishlist, Rating y Metacritic Rating. Los cuatro conteos reciben log1p para reducir escala y asimetría, conservando ceros; después StandardScaler se ajusta a las seis variables entre los casos completos.

**Faltantes.** No se imputan notas: excluir casos incompletos evita fabricar la recepción de los juegos. Se conservan en el CSV con incluido_clustering=False, motivo_no_agrupado y etiquetas vacías; la cobertura parcial puede sesgar los perfiles hacia títulos con crítica disponible.

**Género.** No entra a las distancias: se usa únicamente para describir la composición posterior. Así no se impone una distancia arbitraria entre categorías ni se pondera adicionalmente a juegos con múltiples géneros.

**Alcance.** Es segmentación descriptiva de todos los casos completos, por eso no hay partición de entrenamiento/prueba. Estos clusters sí usan calificaciones: no se debe evaluar después un clasificador de sus etiquetas usando las mismas notas como si fuera una validación independiente.

## 3. K-Means: elección de k

| k | inercia | silhouette |
| --- | --- | --- |
| 2 | 3299 | 0.3188 |
| 3 | 2748 | 0.2377 |
| 4 | 2455 | 0.2268 |
| 5 | 2232 | 0.218 |
| 6 | 2052 | 0.1947 |
| 7 | 1914 | 0.1898 |
| 8 | 1803 | 0.1764 |
| 9 | 1706 | 0.1768 |
| 10 | 1630 | 0.1725 |

![Inercia y silhouette](figures/clustering_03_kmeans.png)

**Elección.** k=2 maximiza silhouette entre 2 y 10; ante empate se prefiere el menor k. Se usan 30 inicializaciones y random_state=42; la inercia se muestra como diagnóstico complementario, no como criterio que siempre escogería el k más grande.

La preferencia de silhouette no acredita que existan segmentos comerciales naturales ni estabilidad frente a otra muestra. El género no se utilizó para seleccionar k.

## 4. DBSCAN: k-distancia y ruido

**Parámetros.** Se fija min_samples=12 como convención operativa de dos veces las seis dimensiones. La curva usa ese vecino contando el propio punto, coherente con la definición de densidad de DBSCAN; no se mezclan distancias de la escala original y la estandarizada.

**Selección reproducible.** Máxima separación x−y respecto de la cuerda, tras normalizar ambos ejes a [0,1]. Se obtiene eps=1.666296; no se selecciona el valor para forzar un número de clusters ni maximizar silhouette.

![Curva de k-distancia](figures/clustering_03_dbscan_kdistancia.png)

Resultado: 1 clusters y **21 puntos de ruido** (2.37% de los agrupables). La etiqueta −1 es ruido, no un perfil. Silhouette excluyendo ruido: no definida: no hay al menos dos clusters válidos.

Sensibilidad local a eps (min_samples fijo):

| factor_eps | eps | clusters | ruido | grupo_mayor |
| --- | --- | --- | --- | --- |
| 0.8 | 1.333 | 1 | 67 | 820 |
| 1 | 1.666 | 1 | 21 | 866 |
| 1.2 | 2 | 1 | 11 | 876 |

Esta comparación local no demuestra estabilidad general frente a remuestreo u otros min_samples. Un grupo dominante o muchos puntos de ruido limitan la utilidad de la segmentación, aunque una métrica aislada resulte favorable.

## 5. Interpretación de cada perfil

**Nombres propuestos.** Se describe la posición superior o inferior al promedio de los casos completos mediante la media de z-scores, sin umbral arbitrario de 0.5 ni categorías absolutas de calidad. Los valores medios acompañan los nombres; no se infieren ventas, rentabilidad ni condición de culto.

**Géneros y ejemplos.** Se muestran los tres géneros más frecuentes, con número y porcentaje de juegos del grupo; sus porcentajes pueden sumar más de 100 %. Los cinco ejemplos son los más cercanos al centro descriptivo del grupo en las seis dimensiones transformadas; para ruido se eligen los primeros cinco IDs. Si hay menos de cinco juegos se muestran todos.

### kmeans: etiqueta 0 · Actividad e interés superiores al promedio; recepción superior al promedio

Tamaño: **465** juegos. Géneros dominantes: Adventure: 352 (75.7%); RPG: 187 (40.2%); Shooter: 129 (27.7%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 7681 |
| Playing | 337.4 |
| Backlogs | 2022 |
| Wishlist | 1053 |
| Rating | 3.909 |
| Metacritic Rating | 86.26 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1056 | The Messenger |
| 304 | Dragon Age: Origins |
| 172 | Metroid: Zero Mission |
| 980 | The Legend of Zelda: Majora's Mask 3D |
| 517 | Luigi's Mansion 3 |

### kmeans: etiqueta 1 · Actividad e interés inferiores al promedio; recepción inferior al promedio

Tamaño: **422** juegos. Géneros dominantes: Adventure: 246 (58.3%); RPG: 99 (23.5%); Shooter: 94 (22.3%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 2981 |
| Playing | 67.96 |
| Backlogs | 476.1 |
| Wishlist | 246.2 |
| Rating | 3.378 |
| Metacritic Rating | 78.01 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1360 | Sonic Rush Adventure |
| 1420 | Black |
| 1375 | Toy Story 2: Buzz Lightyear to the Rescue! |
| 1398 | Shantae: Half-Genie Hero |
| 1338 | Condemned: Criminal Origins |

### dbscan: etiqueta -1 · Atípicos de densidad (ruido; no es un cluster)

Tamaño: **21** juegos. Géneros dominantes: Adventure: 12 (57.1%); Strategy: 7 (33.3%); Shooter: 6 (28.6%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 3348 |
| Playing | 146.1 |
| Backlogs | 280.3 |
| Wishlist | 120.4 |
| Rating | 2.924 |
| Metacritic Rating | 68.05 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 109 | League of Legends |
| 276 | Shadow the Hedgehog |
| 610 | Marvel Snap |
| 661 | Paladins |
| 667 | Wanted: Dead |

### dbscan: etiqueta 0 · Actividad e interés superiores al promedio; recepción superior al promedio

Tamaño: **866** juegos. Géneros dominantes: Adventure: 586 (67.7%); RPG: 283 (32.7%); Shooter: 217 (25.1%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 5495 |
| Playing | 210.8 |
| Backlogs | 1311 |
| Wishlist | 682.6 |
| Rating | 3.674 |
| Metacritic Rating | 82.68 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1110 | Professor Layton and the Curious Village |
| 656 | Fire Emblem: The Sacred Stones |
| 666 | Persona 4 Arena Ultimax |
| 622 | Sunset Overdrive |
| 758 | Phoenix Wright: Ace Attorney - Spirit of Justice |

### Proyección complementaria

![Proyección PCA](figures/clustering_03_proyeccion.png)

PCA se usa solo para visualizar: las dos componentes conservan 75.1% de la varianza. Las etiquetas se ajustaron en seis dimensiones y no sobre esta proyección.

## 6. Artefactos y límites

`data/clean/dataset_con_clusters.csv` conserva los 1,117 registros de la fuente y agrega cluster_kmeans, cluster_dbscan, perfiles, incluido_clustering y motivo_no_agrupado. Las etiquetas vacías no significan ruido; −1 solo aparece para los casos completos considerados atípicos por DBSCAN.

Las tablas completas, búsqueda de k, curva de distancias, sensibilidad, medias y ejemplos se guardan con prefijo clustering_03_ en reports. El pipeline descriptivo se conserva en models/clustering_03.joblib junto con variables y parámetros; DBSCAN no aporta una regla predict de asignación para juegos nuevos.

Este es el único protocolo de clustering activo: la app y el orquestador leen estos mismos artefactos de seis variables. Los resultados antiguos de cuatro conteos quedan archivados fuera del flujo; las etiquetas descriptivas no se entregan al clasificador supervisado.

## Que debo verificar manualmente

- Procedencia/plataforma de Metacritic y escala histórica de Rating; las estimaciones siguen excluidas.
- Función de las organizaciones de Team: los nombres no acreditan que sean desarrolladores.
- Grupos con n<20 y sesgo por ausencias: los resultados representan los pares/casos disponibles.
- Codo de k-distancia, grupo dominante, ruido y estabilidad frente a otras muestras y parámetros.
- Interpretaciones de nombres y ejemplos: no son etiquetas de éxito comercial ni pruebas de causalidad.
- No usar notas para predecir estas etiquetas sin reconocer la circularidad de su construcción.

## Comparación interpretativa de k=2, k=3 y k=4

k=2 maximiza silhouette, pero resume sobre todo magnitud conjunta. Se presentan también k=3 y k=4 para evaluar perfiles cruzados sin cambiar k por conveniencia narrativa. Sus medias se calculan en las unidades originales; ver clustering_03_ejemplos_alternativas.csv para ejemplos de cada alternativa.

| metodo | cluster | n | perfil_propuesto | generos_dominantes | media_Plays | media_Playing | media_Backlogs | media_Wishlist | media_Rating | media_Metacritic Rating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| kmeans_k2 | 0 | 465 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 352 (75.7%); RPG: 187 (40.2%); Shooter: 129 (27.7%) | 7681 | 337.4 | 2022 | 1053 | 3.909 | 86.26 |
| kmeans_k2 | 1 | 422 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 246 (58.3%); RPG: 99 (23.5%); Shooter: 94 (22.3%) | 2981 | 67.96 | 476.1 | 246.2 | 3.378 | 78.01 |
| kmeans_k3 | 0 | 306 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 244 (79.7%); RPG: 131 (42.8%); Shooter: 87 (28.4%) | 8989 | 444.8 | 2472 | 1310 | 3.998 | 87.74 |
| kmeans_k3 | 1 | 177 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 91 (51.4%); Platform: 38 (21.5%); Shooter: 37 (20.9%) | 1949 | 32.81 | 273.3 | 146.5 | 3.146 | 74.54 |
| kmeans_k3 | 2 | 404 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 263 (65.1%); RPG: 129 (31.9%); Shooter: 99 (24.5%) | 4291 | 108.1 | 832.4 | 413.2 | 3.622 | 81.67 |
| kmeans_k4 | 0 | 238 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 155 (65.1%); Shooter: 77 (32.4%); RPG: 62 (26.1%) | 6319 | 140.5 | 904.3 | 357.2 | 3.356 | 81.55 |
| kmeans_k4 | 1 | 298 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 238 (79.9%); RPG: 127 (42.6%); Shooter: 83 (27.9%) | 9040 | 442.5 | 2504 | 1325 | 4.007 | 87.66 |
| kmeans_k4 | 2 | 159 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 76 (47.8%); Platform: 36 (22.6%); Shooter: 36 (22.6%) | 1992 | 31.4 | 265.1 | 140.5 | 3.097 | 73.66 |
| kmeans_k4 | 3 | 192 | Actividad e interés inferiores al promedio; recepción superior al promedio | Adventure: 129 (67.2%); RPG: 78 (40.6%); Indie: 46 (24.0%) | 1640 | 79.6 | 716.2 | 476.8 | 3.949 | 82.23 |

## Sensibilidad a títulos compartidos

Las relaciones entre tablas usan id_juego, nunca Title. Como análisis de sensibilidad, se promedian las dos notas dentro de cada título sobre sus pares completos y se recalculan Pearson/Spearman por título único. Esto reduce el peso de nombres repetidos, pero puede juntar obras distintas: no sustituye la unidad juego ni resuelve remakes. El archivo clustering_03_sensibilidad_titulos.csv incluye géneros y organizaciones.

| grupo | variable_a | variable_b | n_juegos | n | estado | pearson_r | pearson_p | spearman_rho | spearman_p | familia | n_registros_pareados |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Catálogo | Rating | Metacritic Rating | 876 | 876 | incluido | 0.5462 | 2.907e-69 | 0.5242 | 5.352e-63 | catalogo | 887 |

## Diagnóstico de la auditoría

Se excluyen 3 conflictos numéricos históricos señalados; no se cambia el maestro. El grupo Visual Novel puede tener menor brecha absoluta sin concordancia de orden: revisar r, rho y sus p-valores. La cercanía de puntuaciones no prueba que usuarios y críticos ordenen igual los juegos. Tampoco se atribuye una varianza mínima sin comprobarla.

Si DBSCAN devuelve un solo grupo, no se inventa una silhouette ni se fuerza eps para obtener perfiles. Con este protocolo es un detector de núcleo y atípicos; su utilidad como segmentación de mercado queda rechazada. La curva geométrica y la sensibilidad local son diagnósticos, no pruebas de separación natural.

## Que debo verificar manualmente

- Resolver plataformas de conflictos heredados y validar títulos compartidos.
- Elegir entre parsimonia de k=2 y utilidad descriptiva de k=3/4 antes de convertir perfiles en decisiones.
- No usar etiquetas ni scaler descriptivo como entrada de la clasificación supervisada.

````

## clustering_03_alternativas_k.csv

Ruta: `Final/reports/clustering_03_alternativas_k.csv` · Bytes: 2506 · SHA-256: `83a307d8df56e722e89679c47b445303b69b3f23e61a06ec2a51670a85e09391`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_correlaciones_catalogo.csv

Ruta: `Final/reports/clustering_03_correlaciones_catalogo.csv` · Bytes: 298 · SHA-256: `73efe968de1a24e4d8f7418e59345b20b71f5730d3c8f7dc9eb65b64b7ee2175`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_correlaciones_generos.csv

Ruta: `Final/reports/clustering_03_correlaciones_generos.csv` · Bytes: 4359 · SHA-256: `5869c0c310fe9e29da498effb41c0134dcb473c8d659db8004a7d7b7f5a1cdda`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_correlaciones_organizaciones.csv

Ruta: `Final/reports/clustering_03_correlaciones_organizaciones.csv` · Bytes: 70129 · SHA-256: `86304ee58a3749c71dbfed9eded58fee43a3d7dd81232f33082909e42f53cd95`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_correlaciones_ranking_generos.csv

Ruta: `Final/reports/clustering_03_correlaciones_ranking_generos.csv` · Bytes: 3530 · SHA-256: `149d78bb3b84b1aeb32e3dbdb34cf0eef72ae8e2947d5333a3af132965ce5131`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_correlaciones_senales.csv

Ruta: `Final/reports/clustering_03_correlaciones_senales.csv` · Bytes: 2729 · SHA-256: `c56c343f3b8b0b6b7acaebc9c831f18cbeefd81726457fb88a4e7243507d8a7a`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_ejemplos.csv

Ruta: `Final/reports/clustering_03_ejemplos.csv` · Bytes: 771 · SHA-256: `da04a559e0664d3f002be8225a2d058577a92cd13572d029a67bace4e371e1bf`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_ejemplos_alternativas.csv

Ruta: `Final/reports/clustering_03_ejemplos_alternativas.csv` · Bytes: 1820 · SHA-256: `d7d9ccfa85d4895ba760f289bec87d4b6411c71946bd997de400f31b3e171c20`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_kdistancia.csv

Ruta: `Final/reports/clustering_03_kdistancia.csv` · Bytes: 20126 · SHA-256: `fe7a8de755530ad3d2136cfbf1e425ac22a3f1d5c7b48249676c7d076310c191`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_parametros.json

Ruta: `Final/reports/clustering_03_parametros.json` · Bytes: 819 · SHA-256: `df298240ede139bee39b1c275e326993fdebc7df6a2250854864a839b8d0089b`

````text
{
  "sha256_entrada": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "semilla": 42,
  "variables": [
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist",
    "Rating",
    "Metacritic Rating"
  ],
  "log1p": [
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist"
  ],
  "n_entrada": 1117,
  "n_completos": 887,
  "n_excluidos_clustering": 230,
  "n_cohorte_analitica": 1114,
  "n_conflictos_historicos": 3,
  "minimo_pares_correlacion": 20,
  "kmeans_k": 2,
  "dbscan_eps": 1.6662963557646437,
  "dbscan_min_samples": 12,
  "dbscan_ruido": 21,
  "dbscan_clusters": 1,
  "dbscan_silhouette_sin_ruido": null,
  "pca_varianza": [
    0.5838385635506382,
    0.16724298816152772
  ],
  "regla_eps": "Máxima separación x−y respecto de la cuerda, tras normalizar ambos ejes a [0,1]."
}
````

## clustering_03_perfiles.csv

Ruta: `Final/reports/clustering_03_perfiles.csv` · Bytes: 1166 · SHA-256: `21a24f23191e0353093d3ec65790da70a7398ec27f5c8d158f8acbaf59b01265`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_seleccion_kmeans.csv

Ruta: `Final/reports/clustering_03_seleccion_kmeans.csv` · Bytes: 380 · SHA-256: `344e5e4cbe1fde8c00e6ad22b368c76fa71d800896b68872e550bd10463ad038`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_sensibilidad_dbscan.csv

Ruta: `Final/reports/clustering_03_sensibilidad_dbscan.csv` · Bytes: 137 · SHA-256: `59c1d25653df3a03d79885db1dca9bda619767e6349516f6b4228578690305e8`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering_03_sensibilidad_titulos.csv

Ruta: `Final/reports/clustering_03_sensibilidad_titulos.csv` · Bytes: 73246 · SHA-256: `e27273d0d4b1f2adb654f58d36298a2eea992755eba86576370ce0375e3ef145`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## comparacion_weka.md

Ruta: `Final/reports/comparacion_weka.md` · Bytes: 2407 · SHA-256: `9a9e959d2dc8e3a81511c846b8bdc947d46913c7d8837bfb011736caaf11cb7c`

````text
# Comparación ejecutada con Weka

Ejecución local real por CLI: Weka 3.8.6 y Java, sin enviar datos a servicios externos. Las salidas originales, comandos, versiones, hashes y asignaciones por id_juego están en reports/weka. No se simula una ejecución de Orange ni una captura de su interfaz.

Ambas herramientas reciben los mismos 887 casos y seis columnas ya transformadas. Weka usa EuclideanDistance -D para desactivar su normalización adicional; no recibe Title ni etiquetas ni género. Python usa 30 inicializaciones, Weka una, con k-means++ y semilla 42; los generadores y criterios de parada pueden diferir.

Silhouette e inercia se recalculan para ambas asignaciones con la misma implementación sobre el mismo espacio. ARI compara particiones sin depender del número asignado a cada cluster; no se presentan números de cluster como correspondencias automáticas.

| k | herramienta | n | silhouette | inercia_comun | ARI_weka_python | tamanos |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | Weka 3.8.6 | 887 | 0.318771290568622 | 3298.5136907203664 | 1.0 | {"0": 422, "1": 465} |
| 2 | sklearn | 887 | 0.318771290568622 | 3298.5136907203664 | 1.0 | {"0": 465, "1": 422} |
| 3 | Weka 3.8.6 | 887 | 0.23584911911092818 | 2748.816578572579 | 0.9702040990038893 | {"0": 399, "1": 304, "2": 184} |
| 3 | sklearn | 887 | 0.23770761869366513 | 2748.3649194969653 | 0.9702040990038893 | {"0": 306, "1": 177, "2": 404} |
| 4 | Weka 3.8.6 | 887 | 0.21890593755013293 | 2461.530540316411 | 0.7820944557579367 | {"0": 225, "1": 267, "2": 219, "3": 176} |
| 4 | sklearn | 887 | 0.22684617714843563 | 2455.4536828792275 | 0.7820944557579367 | {"0": 238, "1": 298, "2": 159, "3": 192} |

Para reproducir con Java instalado: python src/comparar_weka.py --descargar. La descarga obtiene JAR de Maven Central; luego la ejecución es local. Sin --descargar requiere los JAR ya presentes en .cache/weka, excluido de Git.

Fuentes: [artefacto de Weka en Maven Central](https://central.sonatype.com/artifact/nz.ac.waikato.cms.weka/weka-stable/3.8.6) y ayuda de SimpleKMeans conservada junto a la ejecución. La comparación de Fase 4A no sustituye una comparación supervisada futura.

## Que debo verificar manualmente

- Diferencias de inicialización y convergencia antes de atribuir una mejora a la herramienta.
- Que la rúbrica admita evidencia por CLI; no se realizó una demo gráfica de Weka/Orange.

````

## conflictos_historicos.csv

Ruta: `Final/reports/conflictos_historicos.csv` · Bytes: 1047 · SHA-256: `4a6138a89f326cbc3014585dd102df51f9b9ffa153edc9e0d5bc30a3a91a59b9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## deduplicacion_historica.csv

Ruta: `Final/reports/deduplicacion_historica.csv` · Bytes: 50132 · SHA-256: `8bfc7afe321893a7891d085d01adfcbc095e23ed3509230bcaa186f531b51aa3`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## despliegue.md

Ruta: `Final/reports/despliegue.md` · Bytes: 2378 · SHA-256: `e3de05696702f565640e30968dca0b671d89bc9552f9b18eb499cef0dcc69b11`

````text
# Estado y procedimiento de publicación

Por decisión explícita del usuario, el proyecto y sus datos se conservan **solo localmente**. La publicación no está autorizada.
Repositorio remoto detectado: `AngelHusielLaraHernandez/ProyectoMineria`; entrada prevista: `Final/app.py`.
No se hizo push ni se creó un servicio remoto. La entrega local se integra en la rama `main`; no se publica en el remoto.

La revisión automática rechazó el intento de push porque faltaba autorización explícita para transmitir el CSV y sus derivados a GitHub. Se solicitó esa autorización y el usuario eligió conservar todo localmente.
La sesión de Streamlit Cloud sí estaba activa; no hay un bloqueo de cuenta que deba resolverse para usar la app local.

## Ejecución local

Desde Final: `python3.14 -m streamlit run app.py` si las dependencias están instaladas en ese entorno; o `.venv314/bin/python -m streamlit run app.py` con el entorno creado aquí.
La comprobación inicial tuvo 17 pruebas. El entorno histórico se validó con Python 3.14. En el cierre actual, la suite completa aprobó 101 pruebas con el entorno local Python 3.15. Los registros anteriores y el cierre están en BITACORA_UNIFICADA.md. Esto no demuestra compatibilidad con un servicio remoto.

## Referencia para una eventual publicación autorizada

1. Validar `python -m src.pipeline` y `python -m pytest -q` desde Final.
2. Revisar y subir el directorio Final, excluyendo lo indicado por su `.gitignore`.
3. En Streamlit Community Cloud elegir el repositorio, la rama publicada y `Final/app.py`.
4. Seleccionar una versión de Python compatible con `Final/requirements.txt`. Este entorno se validó con Python 3.14; si no está disponible, crear y validar un entorno compatible antes de cambiar versiones fijadas.
5. Confirmar la reconstrucción de artefactos cuando cambie sklearn, consultar las cuatro páginas y probar una predicción.
6. Registrar aquí URL pública, revisión Git desplegada y versión de Python una vez comprobadas.

La documentación oficial describe la selección de repositorio y entrada:
[Desplegar una aplicación](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
Las dependencias pueden colocarse junto a la entrada:
[Organización de archivos](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization).

````

## escalas.md

Ruta: `Final/reports/escalas.md` · Bytes: 1483 · SHA-256: `417c4f52bc14c5db26ec0bd1594ffd33a37ec48c5139a17597bb30c07325be6e`

````text
# Evidencia documental de escalas

## Escalas verificadas antes de calcular la brecha

Consulta de documentación primaria: **8 de noviembre de 2026**. No se reemplazaron notas ni conteos del CSV por valores actuales del sitio.

- [Backloggd: página oficial de Elden Ring](https://backloggd.com/games/elden-ring/) muestra la media junto al gráfico de estrellas cuyo extremo superior es **5 estrellas**. [Su FAQ](https://backloggd.com/about/) distingue la media del juego y el promedio ponderado utilizado para ordenar. Esta evidencia respalda el denominador cinco; no prueba por sí sola cómo se extrajo cada fila histórica.
- [Metacritic: interpretación del Metascore](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore) documenta una escala de **0–100** para prensa.
- Los rangos del CSV son compatibles con esas escalas. El derivado heredado `rating_100` coincide con multiplicar por 20, pero se usa solo como corroboración y no como prueba independiente de la escala.

Se aplicará una conversión por el máximo documentado: `rating_normalizado = Rating / 5 × 100`; `brecha = rating_normalizado − Metacritic Rating` solo cuando la nota crítica tenga procedencia válida según el maestro.
No se usa normalización min–max de la muestra: convertir 0.7 y 4.8 en los extremos produciría una brecha dependiente de los juegos incluidos. La conversión tampoco afirma equivalencia psicométrica entre ambas plataformas.


````

## evaluacion.md

Ruta: `Final/reports/evaluacion.md` · Bytes: 7393 · SHA-256: `efbda1b45a1beb914db98816c2ac22d1586a0e99b7a7491775e4317ca24554a7`

````text
# Evaluación del proyecto frente a sus objetivos

Todas las cifras provienen de los reportes de `Final/reports/` y de `models/metadata.json`. No se calculó ningún número nuevo. Donde un dato necesario no existe en los reportes, se indica explícitamente al final de cada sección.

## 1. Objetivos específicos

| # | Objetivo | Evidencia (archivo y cifra) | Estado | Comentario |
|---|---|---|---|---|
| 1 | Depurar y estructurar el maestro | `limpieza_log.md`, `inspeccion.md`: 1,117 filas × 42 columnas (SHA-256 `b23cc1c4…625acd`); `trazabilidad_historica.md`: 1,512 → 1,117 con 395 descartes documentados; 218 notas críticas estimadas excluidas; 1,114 juegos elegibles | Cumplido | Los 3 conflictos históricos (`id_juego` 117, 140, 296) siguen sin resolver y están excluidos del análisis. |
| 2 | EDA (distribuciones, géneros, décadas) | `inspeccion.md`: seis figuras EDA; Rating 0.7–4.8 con 13 ausencias; `clustering_03_correlaciones_generos.csv`: 16 géneros incluidos y 7 excluidos | Cumplido | Los roles de `Team` no se acreditan como desarrolladores, y faltan 3 fechas. |
| 3 | Discrepancia usuarios–prensa | `clustering.md`: n = 887, Pearson r = 0.5439, Spearman ρ = 0.5242; brecha absoluta media por género, de 8.222 (Visual Novel) a 12.82 (Shooter) | Cumplido | Con correcciones BH por género. La conversión Rating/5×100 no implica equivalencia entre plataformas. |
| 4 | Popularidad con interacciones | `clustering_03_correlaciones_senales.csv`: Plays–Rating r = 0.1517; Plays–Metacritic r = 0.4144; Backlogs–Wishlist r = 0.7912 | Parcial | Se mide popularidad en Backloggd, no ventas. Las señales están muy correlacionadas entre sí. |
| 5 | Perfiles (K-Means y DBSCAN) | `clustering.md`: K-Means k = 2, silhouette 0.3188, grupos de 465 y 422; DBSCAN: 1 cluster de 866 y 21 de ruido | Parcial | El resultado de K-Means separa principalmente magnitud. DBSCAN no segmenta; no acredita segmentación comercial. |
| 6 | Clasificador de popularidad | `modelo.md` y `metadata.json`: RandomForest, n prueba = 222, exactitud 0.5676, F1 macro 0.5577, frente a 0.1546 del Dummy | Parcial | Supera la referencia en esta partición, sin prueba de significancia. Recall de la clase media = 0.3375. |
| 7 | App y comunicación | `pages/2_Prediccion.py`, `pages/3_Acerca_del_modelo.py`; `verificacion_funcional.md`; `pruebas_web.txt` (87 pruebas) | Parcial | App local funcional. No hay despliegue público (`despliegue.md`). |

**Comparación de herramientas (Python, Orange, Weka).** Weka 3.8.7 tiene seis corridas gráficas completas (`weka/resumen_gui.md`). En clasificación, RandomForest alcanzó 53.4753 % y NaiveBayes 50.8969 % (CV de 10 pliegues, n = 892). En K-Means con k = 2 hay ARI = 1.0 contra Python en la ejecución CLI 3.8.6. **Orange no tiene ninguna corrida verificada** (`diagnostico_cierres.md`: cierres con SIGSEGV). Esta comparación queda **parcial**.

## 2. Preguntas de la problemática

**¿Los juegos mejor calificados son los más jugados?** Solo en parte, y depende de quién califica.
- Plays frente a Rating (usuarios): r = 0.1517 y ρ = 0.08737. La asociación es débil.
- Plays frente a Metacritic: r = 0.4144 y ρ = 0.423. La asociación es moderada.
- Wishlist frente a Rating: r = 0.4232 y ρ = 0.5035.

Una asociación no implica causalidad.

**¿Hay géneros con muchos jugadores y calificaciones bajas, o al revés?** Los reportes **no contienen Plays por género**, así que no puedo responderlo con datos del género. Hay evidencia indirecta en K-Means k = 4: el cluster 0 (n = 238) tiene Plays = 6319 con Rating = 3.356, y el cluster 3 (n = 192) tiene Plays = 1640 con Rating = 3.949. Existen perfiles cruzados, pero eso no los asocia a un género. **Si lo necesitas, pídeme que calcule Plays y Rating medios por género.**

**¿El Metascore funciona igual en todos los géneros?** No. Entre los 16 géneros con n ≥ 20:
- Fuerte: Arcade (r = 0.7548, n = 39), Point-and-Click (r = 0.6546) y Platform (r = 0.6428).
- Débil o no significativa: Visual Novel (r = −0.1042, p = 0.605) y Turn Based Strategy (r = 0.2514, p = 0.0752).
- Brecha absoluta media: Shooter (12.82), Fighting (12.02) y Racing (12.0), frente a Visual Novel (8.222).

Las diferencias entre r de distintos géneros no están probadas como diferencias significativas entre grupos.

## 3. Análisis de errores del clasificador

Matriz del RandomForest (filas reales, columnas predichas bajo / medio / alto):

| real | bajo | medio | alto |
|---|---|---|---|
| bajo | 43 | 14 | 10 |
| medio | 32 | 27 | 21 |
| alto | 9 | 10 | 56 |

- **Recall por clase:** bajo 0.6418, medio 0.3375, alto 0.7467.
- **Confusión principal:** medio → bajo (32 de 80) y medio → alto (21 de 80).
- **Por qué es plausible:** la clase media es un tramo de un continuo, delimitado por cortes artificiales en los terciles [0.3623, 0.6267]. Sus notas y géneros pueden solaparse con ambos extremos (`modelo.md`). Es una hipótesis interpretativa, no una causa demostrada.
- **Otros modelos:** DecisionTree tiene recall medio 0.225 y CategoricalNB 0.2375. Todos fallan sobre todo en esa clase.
- **Cobertura de prensa:** al ocultar las 180 notas críticas conocidas de prueba, la probabilidad de "bajo" sube 0.03885 en promedio. La ablación sin crítica da F1 macro 0.5149. Esto es diagnóstico, no una prueba causal.

## 4. Limitaciones

- **Tamaño del catálogo:** 1,117 juegos (1,114 elegibles). Solo 887 tienen ambas notas, y 16 géneros alcanzan n ≥ 20. La prueba del clasificador tiene 222 casos.
- **Popularidad medida con Backloggd:** Plays, Playing, Backlogs y Wishlist son interacciones declaradas, no ventas ni usuarios únicos. El índice de popularidad usa pesos iguales, y esa elección es discutible.
- **Sin datos de juegos como servicio (GaaS):** el maestro no tiene etiquetas de fracaso, modelo de negocio ni ingresos. Los resultados no permiten hablar de riesgo comercial GaaS.
- **Sesgo de selección:** el catálogo contiene sobre todo juegos conocidos, y los fracasos están poco representados.
- **Notas de prensa:** 218 de 1,117 son estimaciones propias y se excluyen. La cobertura de Metacritic puede no ser aleatoria.
- **Posible review bombing en Rating:** los reportes no incluyen datos temporales ni de volumen de reseñas. No puedo confirmarlo ni descartarlo. La brecha media es negativa en casi todos los géneros, pero eso no demuestra manipulación.
- **Otras limitaciones:**
  - Orange no se ejecutó.
  - Weka y Python usan protocolos distintos (K-Means: 477/410 frente a 465/422; DBSCAN: 887 frente a 866 + 21 de ruido).
  - Hay tres conflictos históricos sin resolver.
  - Las probabilidades del modelo no están calibradas.

## 5. Conclusión

Este trabajo puede orientar a una desarrolladora sobre qué asociaciones aparecen entre recepción de usuarios, prensa e interés declarado en Backloggd, y sobre qué géneros muestran mayor o menor acuerdo entre usuarios y crítica. Un clasificador de popularidad relativa supera a la referencia en esta partición, con un F1 macro de 0.5577. Es modesto y falla sobre todo en la clase media. No puede afirmar que una nota alta cause más juego, ni predecir ventas o éxito comercial, ni evaluar riesgos de juegos como servicio. Tampoco acredita segmentos de mercado a partir de DBSCAN y K-Means. Tampoco sirve como predicción previa al lanzamiento, porque usa notas ya publicadas.


````

## fase_1_alcance.md

Ruta: `Final/reports/fase_1_alcance.md` · Bytes: 3526 · SHA-256: `b75cd6e137c83f4a4986b4992caa2eb95f68e717c0f3d89b6e14d326adf5ab69`

````text
# Fase 1: alcance y contratos de implementación

## Objetivo verificable

Describir recepción, actividad e interés en el maestro de Backloggd; comparar usuarios y prensa con procedencia explícita, explorar perfiles descriptivos y estimar popularidad relativa por terciles. No demostrar ventas, causalidad de fracasos GaaS ni rentabilidad.

## Fuente y unidad de análisis

games_curated.csv es el maestro designado por el usuario: 1,117 filas, 42 columnas, copia inmutable en data/raw. El antecedente de 1,512 filas vive en data/historical y se usa exclusivamente para auditar y reconstruir decisiones históricas.
Cada id_juego identifica una observación por título y fecha. Los títulos compartidos se señalizan; no se fusionan porque Doom o God of War pueden representar obras distintas. Las relaciones se validan por ID.

## Contratos por fase

| Fase | Implementación | Salida y condición verificable |
|---|---|---|
| 1. Alcance | Este documento | Diferenciar popularidad de éxito comercial; registrar maestro y unidad. |
| 2. Inspección | src/01_inspeccion.py | Esquema, procedencia y seis figuras EDA, sin cambiar fuentes. |
| 3. Limpieza | src/02_limpieza.py + src/procedencia.py | dataset_depurado.csv, géneros por ID, balance de filas e historia de cada descarte; conflictos heredados no elegibles hasta revisión. |
| 4A. Asociación y clustering | src/03_clustering.py | Correlación con mínimo de 20 pares; seis variables transformadas; k=2…10, DBSCAN y diagnóstico, alternativas k=3/4 y sensibilidad a títulos. |
| 4A. Comparación de herramienta | src/comparar_weka.py | Ejecución real de K-Means en Weka sobre el mismo espacio, con comandos, hashes, asignaciones y comparación de métricas. |
| 4B. Clasificación independiente | src/04_modelo.py | Objetivo por terciles del promedio de percentiles de Plays, Wishlist y Backlogs, ajustado solo con entrenamiento y de nuevo dentro de cada fold; holdout aproximadamente 80/20 por grupos sin target global y diez folds estratificados por título con objetivos locales. |
| Consulta local | app.py y pages | Lee los mismos artefactos de 4A, comprobados mediante reports/manifest.json. No hay publicación autorizada. |

## Decisiones y límites

**Conflictos históricos.** No se altera la selección del maestro ni se elige una cifra más reciente sin evidencia. Se conservan los tres registros con indicador y se excluyen provisionalmente de inferencia, clustering y clasificación: se informa cobertura y motivo.

**Evidencia histórica.** Reproducir las 42 columnas comprueba trazabilidad, no legitima la regla first ni valida la prensa. Las estimaciones propias se identifican por procedencia y se corrobora su dependencia de Rating sin tratarlas como crítica independiente.

**Perfiles.** K-Means seleccionado por silhouette se contrasta interpretativamente con k=3/4. DBSCAN puede devolver un núcleo y atípicos: se acepta ese resultado como falta de segmentación útil, sin forzar una respuesta favorable.

**Entorno.** Las versiones fijadas son las realmente instaladas y probadas; Python 3.14 está validado localmente. No se inventa compatibilidad de nube ni se cambian versiones solo por parecer poco comunes; los entornos y JAR están excluidos de Git.

## Que debo verificar manualmente

- Plataformas y capturas de las tres discrepancias numéricas; roles de Team.
- Identidad de los juegos con títulos iguales y la representatividad de la muestra.
- Aceptación de evidencia CLI de Weka y de una demo local por el profesor.

````

## hallazgos.md

Ruta: `Final/reports/hallazgos.md` · Bytes: 1283 · SHA-256: `1831b8e7455498ff69f788cb17d0c09c3def5cb6f502b0f5137d9582c7c19a2c`

````text
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

## hallazgos_weka_web.docx

Ruta: `Final/reports/hallazgos_weka_web.docx` · Bytes: 811697 · SHA-256: `293d515d455d9297401cb2dff6ffd4b390d0a707dc4d3c05288aeb57aa9fd9a0`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## hallazgos_weka_web.md

Ruta: `Final/reports/hallazgos_weka_web.md` · Bytes: 12997 · SHA-256: `0882706612b3036d5ed7863ec8c769bf8040b46e405fe34ee9ff003b8d1fcf05`

````text
# Hallazgos de Weka y validación web

Informe técnico de avance • 9 de noviembre de 2026 • Versión 1

El modelo de la web reproduce correctamente las predicciones almacenadas y conserva la separación entre entrenamiento y prueba. Su capacidad predictiva es moderada: obtiene 56.76 % de exactitud y F1 macro de 0.5577 en 222 casos de prueba. La clase media sigue siendo la principal debilidad. Siete variantes nuevas del bosque no mejoraron la validación cruzada del modelo vigente, por lo que se conservó ese artefacto.

Este informe integra las corridas gráficas existentes de Weka, su contraste metodológico con Python y las verificaciones de la aplicación Streamlit. Los resultados describen popularidad relativa en un catálogo curado, no ventas, rentabilidad ni probabilidad de éxito comercial de un lanzamiento.

| Población comprobada | Registros | Uso |
| --- | --- | --- |
| Antecedente histórico | 1,512 | Auditoría de decisiones heredadas |
| Maestro games_curated.csv | 1,117 | Original designado con 42 columnas |
| Cohorte elegible | 1,114 | Análisis principal y clasificación |
| Casos completos de clustering | 887 | Seis variables sin ausencias |
| Entrenamiento y prueba | 892 y 222 | Partición por grupos de título |

El archivo en data/raw ya es un maestro curado. El antecedente de 1,512 filas se conserva aparte; no debe presentarse como si la limpieza actual hubiera recibido 1,512 filas. La web se aclaró para distinguir HIST y MAESTRO.

En los 887 pares elegibles con ambas notas, Pearson es 0.5439 con p = 1.936 × 10⁻⁶⁹ y Spearman es 0.5242. Es evidencia de asociación entre recepción de usuarios y prensa, no de acuerdo exacto ni de causalidad.

Fuentes: reports/inspeccion.md; reports/trazabilidad_historica.md; reports/clustering.md; reports/revision_predicciones/auditoria.json.

## Clasificación observada en Weka

Weka Explorer 3.8.7 evaluó 892 registros con 53 atributos, incluida la clase nominal nivel_popularidad, mediante validación cruzada de diez pliegues. Se verificaron las cuatro matrices originales: sus sumas son 892 y sus diagonales reproducen la exactitud publicada por el programa.

| Herramienta | Modelo | Exactitud % | F1 macro | F1 pond |
| --- | --- | --- | --- | --- |
| Weka | ZeroR | 33.0717 | 0.2533 | 0.2533 |
| Weka | NaiveBayes | 50.8969 | 0.5033 | 0.5030 |
| Weka | J48 | 51.0090 | 0.5063 | 0.5060 |
| Weka | RandomForest | 53.4753 | 0.5300 | 0.5300 |
| Python enlace | Dummy | 33.0717 | 0.2531 | 0.2533 |
| Python enlace | GaussianNB | 47.4215 | 0.4437 | 0.4438 |
| Python enlace | Árbol CART | 46.9731 | 0.4693 | 0.4694 |
| Python enlace | Random Forest | 54.8206 | 0.5442 | 0.5442 |

RandomForest fue el mejor clasificador de las cuatro corridas de Weka, con 477 aciertos de 892. Su F1 para la clase medio fue 0.381 y su recall 0.360, por debajo de los otros dos niveles; la dificultad de la clase central también aparece en Python.

El F1 macro de Weka promedia los F Measure por clase impresos a tres decimales. En ZeroR el valor no definido de medio se resolvió desde la matriz con la convención de cero; el F1 ponderado de 0.2533 también se calculó desde la matriz porque Weka imprimió un signo de interrogación. Los otros ponderados son los reportados por Weka.

Python enlace usa los mismos 892 registros y 52 predictores numéricos exportados, pero no los mismos pliegues de Java. NaiveBayes y GaussianNB tienen tratamientos distintos; J48 y CART son árboles diferentes. Weka usa 100 árboles y semilla del estimador 1; Python enlace usa 100 y semilla 42. La semilla de los pliegues de la sesión Weka no pudo recuperarse. El preprocesamiento de esta comparación se hizo antes de CV; no sustituye la evaluación de producción con preprocesamiento por pliegue.

Fuentes: reports/weka/ZeroR.txt, NaiveBayes.txt, J48.txt y RandomForest.txt; reports/tables/comparativo_herramientas.csv; revision_predicciones/weka_recalculado.json.

## Segmentación observada en Weka

SimpleKMeans utilizó k = 2 y semilla 42 sobre 887 instancias y seis atributos. Convergió en nueve iteraciones y produjo grupos de 477 y 410 juegos. Los centroides siguientes están en las unidades transformadas del archivo exportado, no en conteos originales ni puntos de calificación.

| Variable | Centro del grupo 0 | Centro del grupo 1 |
| --- | --- | --- |
| Plays | 0.4100 | −0.4770 |
| Playing | 0.6189 | −0.7200 |
| Backlogs | 0.7093 | −0.8252 |
| Wishlist | 0.6912 | −0.8042 |
| Rating | 0.4797 | −0.5581 |
| Metacritic Rating | 0.4270 | −0.4968 |

Los signos de los centros describen un perfil con mayor actividad, interés y recepción frente a otro con valores inferiores al promedio exportado. Es una interpretación descriptiva del catálogo y no prueba que existan segmentos comerciales naturales. Las etiquetas numéricas de los grupos son arbitrarias.

| Resultado | Python | Weka |
| --- | --- | --- |
| K Means con dos grupos | 465 y 422 | 477 y 410 |
| DBSCAN grupos válidos | 1 | 1 |
| DBSCAN asignados al grupo | 866 | 887 |
| DBSCAN ruido | 21 | 0 |

En Python k = 2 maximizó silhouette entre 2 y 10, con 0.3188. Weka no reportó esa métrica en la corrida guardada; no se le atribuye el valor de Python. Las sumas de cuadrados tampoco se comparan como si provinieran de una configuración de distancias idéntica.

DBSCAN se ejecutó en Weka con eps = 1.666296 y minPoints = 12. Agrupó las 887 instancias en un solo grupo. En Python, los mismos parámetros nominales dejaron 21 casos como ruido. La igualdad de eps no acredita equivalencia de la distancia interna: Weka informa EuclideanDistance con sus opciones y las implementaciones no son una réplica exacta. No se forzaron parámetros ni se corrigieron las salidas para hacerlas coincidir.

Fuentes: reports/weka/kmeans.txt y dbscan.txt; reports/clustering.md; reports/clustering_03_perfiles.csv.

## Hallazgos y correcciones de la web

La aplicación mantiene cuatro páginas: Inicio, Exploración, Predicción y Modelo. Permite consultar señales de popularidad, asociaciones entre notas, perfiles de clustering, predicciones y vecinos del entrenamiento. La identidad azul y morada y la fuente cómic local se aplican sin modificar los datos analíticos.

Se corrigieron las cifras atravesadas por barras de error en los gráficos de desempeño e importancia por permutación. Las cifras se sitúan después del extremo del intervalo; se conservaron sus desviaciones y los rangos estadísticos. Los ejes logarítmicos muestran potencias de diez sin marcas menores amontonadas. En móvil, las figuras densas se desplazan dentro de su panel.

![Predicción comprobada en la interfaz con Adventure y RPG, organización Otro, década de 2020, Metacritic 100 y Rating 5. El modelo devuelve alto con 54.1 % de probabilidad no calibrada.](revision_predicciones/formulario_verificado.jpg)

La revisión del formulario añadió validación explícita de Rating de 0 a 5 y Metacritic de 0 a 100, conservando los nulos para la imputación entrenada. Se eliminó el ancho mínimo artificial de 2 % de las barras. Otro ahora significa organización no frecuente y no presume que sea un estudio independiente.

Fuentes: pages/2_Prediccion.py; src/inferencia.py; reports/BITACORA_UNIFICADA.md; revision_predicciones/casos_formulario.json.

## Verificación de las predicciones

Se compararon las 222 salidas del artefacto guardado con las predicciones de prueba almacenadas y todas coinciden. Las probabilidades son finitas, suman uno y su mayor valor corresponde a la clase mostrada, usando el orden real de pipeline.classes_. También se reprodujeron las etiquetas y los terciles desde la referencia de entrenamiento.

| Métrica en prueba | Resultado |
| --- | --- |
| Exactitud | 56.76 % |
| F1 macro | 0.5577 |
| F1 ponderado | 0.5540 |
| Recall bajo | 64.18 % |
| Recall medio | 33.75 % |
| Recall alto | 74.67 % |

| Clase real | Predice bajo | Predice medio | Predice alto |
| --- | --- | --- | --- |
| bajo | 43 | 14 | 10 |
| medio | 32 | 27 | 21 |
| alto | 9 | 10 | 56 |

Las entradas son géneros, organizaciones de Team, década, Metacritic Rating y Rating. Plays, Wishlist y Backlogs definen el objetivo y no entran al clasificador; Playing tampoco es predictor. Las categorías e imputaciones se ajustan en entrenamiento. Los títulos agrupados de entrenamiento y prueba no se superponen y el índice de vecinos contiene únicamente IDs de entrenamiento en el mismo espacio transformado.

La ausencia de prensa es una limitación concreta. En el caso comprobado de la página anterior, ocultar Metacritic manteniendo Rating 5 cambia alto a bajo, con 44.2 % para bajo. El cálculo coincide con el Pipeline; no es una inversión de etiquetas del formulario. La web muestra ahora un aviso sobre la imputación. Esto evidencia sensibilidad a la cobertura y no demuestra que un juego sin nota vaya a tener baja popularidad.

Se aprobaron 39 pruebas, incluidas escalas inválidas, valores extremos, organizaciones nuevas, ausencia de crítica y envíos del formulario contrastados con el Pipeline. Las probabilidades no están calibradas y los casos de demostración no constituyen validación externa.

Fuentes: models/metadata.json; revision_predicciones/auditoria.json y casos_formulario.json; tests/test_inferencia.py; revision_predicciones/pruebas.txt.

## Revisión del entrenamiento y decisión

Se reutilizaron exclusivamente los 892 registros de entrenamiento y sus diez pliegues agrupados por título. Cada ajuste recalcula objetivo local, vocabularios e imputación sin consultar su validación. Se entrenaron siete variantes nuevas de Random Forest más la referencia vigente, con 200 árboles y random_state 42: 80 ajustes en total.

| Candidato | Hoja mín | Ponderación | Variables | F1 CV |
| --- | --- | --- | --- | --- |
| Vigente | 5 | Sin ponderar | Raíz | 0.5567 |
| RF 3 | 5 | Balance por muestra | Raíz | 0.5510 |
| RF 2 | 2 | Balance por muestra | Raíz | 0.5508 |
| RF 4 | 10 | Balance por muestra | Raíz | 0.5427 |
| RF 1 | 1 | Sin ponderar | Raíz | 0.5403 |
| RF 5 | 2 | Sin ponderar | 0.5 | 0.5374 |
| RF 7 | 10 | Sin ponderar | 0.5 | 0.5368 |
| RF 6 | 5 | Balance por muestra | 0.5 | 0.5300 |

Raíz indica max_features igual a sqrt; 0.5 usa la mitad de las variables transformadas en cada división. Balance por muestra corresponde a class_weight igual a balanced_subsample. La profundidad se mantiene sin límite en estas variantes.

Antes de consultar sus resultados se fijó un criterio de promoción: mejora de al menos 0.01 en F1 macro y superioridad en seis de diez pliegues. Ninguna variante superó siquiera la media del modelo vigente, 0.5567. Se conservan el artefacto y sus métricas; no se presenta una mejora inexistente ni se selecciona un candidato por la prueba.

El mejor recall medio de alguna variante no basta para reemplazar al modelo si disminuye el F1 macro elegido como criterio. La búsqueda no es una CV anidada y amplía la exploración de hiperparámetros sobre los mismos pliegues; sus medias no son una estimación independiente del rendimiento futuro.

La prueba existente ya fue observada. Sin una muestra externa posterior no se puede afirmar una mejora prospectiva ni validar el uso del sistema para géneros nuevos o resultados comerciales. Estas limitaciones se documentan; no se sustituyen con cifras de entrenamiento.

Reproducción desde Final: python src/05_revision_predicciones.py. Evidencias: revision_predicciones/busqueda_folds.csv, busqueda_resumen.csv, decision.json y ejecucion.txt.

## Evidencias y límites del informe

![Corrida gráfica original de RandomForest en Weka. Las métricas del informe se extrajeron del texto guardado y se contrastaron con su matriz; la imagen aporta la evidencia visual de la sesión.](weka/RandomForest.png)

Las seis corridas gráficas conservan salidas y capturas locales: SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Esta revisión no reejecuta Weka ni cambia sus resultados. El script verificar_weka.py recalcula sus matrices de clasificación y conserva los hashes de las fuentes.

Orange se descartó por cierres de la aplicación en Qt y Cocoa al usar selectores de archivos. Se probaron la instalación local, recuperación y reinicio del lienzo, CSV y TAB, además de un lanzador con selectores Qt. No hay métricas de Orange en este informe; no se le atribuye ninguna salida de Weka.

La popularidad se refiere a rangos percentiles relativos de Plays, Wishlist y Backlogs. La muestra tiene sesgo de visibilidad comunitaria; Team no separa desarrolladores y publishers. Las notas con origen estimado se excluyen como evidencia independiente de prensa. Las columnas financieras estimadas del maestro no se utilizan para demostrar éxito comercial.

Trazabilidad principal: data/raw/games_curated.csv; reports/inspeccion.md; reports/trazabilidad_historica.md; reports/weka/; reports/BITACORA_UNIFICADA.md; reports/tables/comparativo_herramientas.csv; reports/revision_predicciones/.

````

## inspeccion.json

Ruta: `Final/reports/inspeccion.json` · Bytes: 4572 · SHA-256: `b287ad7e6f0127adade28748019cd9a67eb975e9076ab7cb5aec6fb978bf11cb`

````text
{
  "archivo_original": "Proyecto/data/processed/games_curated.csv",
  "copia_inmutable": "data/raw/games_curated.csv",
  "filas": 1117,
  "columnas": 42,
  "sha256": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
  "esquema": {
    "ID Original": {
      "tipo": "int64",
      "faltantes": 0
    },
    "Title": {
      "tipo": "str",
      "faltantes": 0
    },
    "Release Date": {
      "tipo": "str",
      "faltantes": 0
    },
    "Team": {
      "tipo": "str",
      "faltantes": 1
    },
    "Rating": {
      "tipo": "float64",
      "faltantes": 13
    },
    "Times Listed": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Number of Reviews": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Genres": {
      "tipo": "str",
      "faltantes": 0
    },
    "Summary": {
      "tipo": "str",
      "faltantes": 1
    },
    "Reviews": {
      "tipo": "str",
      "faltantes": 0
    },
    "Plays": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Playing": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Backlogs": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Wishlist": {
      "tipo": "float64",
      "faltantes": 0
    },
    "Metacritic Rating": {
      "tipo": "int64",
      "faltantes": 0
    },
    "Origen_calificacion": {
      "tipo": "str",
      "faltantes": 0
    },
    "ingresos_empresa_estimados_USD": {
      "tipo": "int64",
      "faltantes": 0
    },
    "gastos_estimados_USD": {
      "tipo": "int64",
      "faltantes": 0
    },
    "unidades_vendidas_estimadas": {
      "tipo": "int64",
      "faltantes": 0
    },
    "ventas_brutas_estimadas_USD": {
      "tipo": "int64",
      "faltantes": 0
    },
    "release_date": {
      "tipo": "str",
      "faltantes": 3
    },
    "year": {
      "tipo": "float64",
      "faltantes": 3
    },
    "decade": {
      "tipo": "float64",
      "faltantes": 3
    },
    "genres_list": {
      "tipo": "str",
      "faltantes": 0
    },
    "team_list": {
      "tipo": "str",
      "faltantes": 0
    },
    "n_genres": {
      "tipo": "int64",
      "faltantes": 0
    },
    "studio_main": {
      "tipo": "str",
      "faltantes": 1
    },
    "publisher_main": {
      "tipo": "str",
      "faltantes": 1
    },
    "genre_main": {
      "tipo": "str",
      "faltantes": 0
    },
    "rating_100": {
      "tipo": "float64",
      "faltantes": 13
    },
    "gap": {
      "tipo": "float64",
      "faltantes": 13
    },
    "metacritic_real": {
      "tipo": "bool",
      "faltantes": 0
    },
    "critic_score_final": {
      "tipo": "float64",
      "faltantes": 218
    },
    "critic_source": {
      "tipo": "str",
      "faltantes": 0
    },
    "gap_real": {
      "tipo": "float64",
      "faltantes": 227
    },
    "log_plays": {
      "tipo": "float64",
      "faltantes": 0
    },
    "log_wishlist": {
      "tipo": "float64",
      "faltantes": 0
    },
    "log_backlogs": {
      "tipo": "float64",
      "faltantes": 0
    },
    "log_playing": {
      "tipo": "float64",
      "faltantes": 0
    },
    "estimates_zero": {
      "tipo": "bool",
      "faltantes": 0
    },
    "has_rating": {
      "tipo": "bool",
      "faltantes": 0
    },
    "population": {
      "tipo": "str",
      "faltantes": 0
    }
  },
  "rangos_observados": {
    "Rating": {
      "min": 0.7,
      "max": 4.8
    },
    "Metacritic Rating": {
      "min": 45.0,
      "max": 99.0
    }
  },
  "procedencia_critica": {
    "Metacritic": 899,
    "Estimacion propia": 218
  },
  "filas_limpias": 1117,
  "duplicados_descartados": 0,
  "historia": {
    "estado": "verificado",
    "sha256_historico": "6073f43d0c0bd5722b03789ff51c97c4ecd53686cdedbef93fc69d0c990245b6",
    "sha256_maestro": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
    "filas_historicas": 1512,
    "filas_maestro": 1117,
    "descartes_heredados": 395,
    "grupos_con_diferencias": 13,
    "grupos_con_conflicto_analitico": 3,
    "ids_analiticos_pendientes": [
      117,
      140,
      296
    ],
    "columnas_reconstruidas": 42,
    "diferencias_reconstruccion": [],
    "critica_estimada_maestro": 218,
    "estimaciones_con_rating": 214,
    "coeficientes_ajuste_sintetico": [
      8.583326609989347,
      50.95839691488483
    ],
    "residuo_maximo_tras_redondear": 0.0
  },
  "rango_anios": [
    1980,
    2025
  ],
  "pares_critica_real": 890,
  "conflictos_historicos_pendientes": 3,
  "registros_titulo_compartido": 35,
  "titulos_compartidos": 17,
  "organizaciones_sin_roles": true
}
````

## inspeccion.md

Ruta: `Final/reports/inspeccion.md` · Bytes: 3232 · SHA-256: `52ae5a3d981eb4808a1107714f45469794e804b3222ab3a0e0c18b2e27a12c2b`

````text
# Inspección reproducible del maestro

Generado por src/01_inspeccion.py. Fuente: data/raw/games_curated.csv; 1117 filas y 42 columnas. SHA-256: b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd.
El maestro es el original designado, ya curado. El antecedente de 1,512 filas se conserva separado en data/historical y se audita en trazabilidad_historica.md; no se reemplaza el maestro.

Rating observado: 0.7–4.8, 13 ausencias. Metacritic original: 45–99; crítica utilizable: 899; estimaciones excluidas: 218.

Los seis conteos ya son numéricos en el maestro: esta fase no afirma haber convertido textos K/M. Su formato y la cuenta real de conversiones quedan en limpieza_log.md. El esquema completo está en inspeccion.json.

Hay 35 registros de 17 títulos compartidos en fechas distintas. No se presume que sean el mismo juego: relaciones por id_juego, nunca por Title. Los 3 casos numéricos heredados sin resolver se mantienen señalados y no participan del análisis principal.

## Seis figuras del EDA

![rating](figures/eda_rating.png)

![metacritic](figures/eda_metacritic.png)

![plays_log](figures/eda_plays_log.png)

![decadas](figures/eda_decadas.png)

![generos_top15](figures/eda_generos_top15.png)

![rating_vs_metacritic](figures/eda_rating_vs_metacritic.png)

Las distribuciones describen el maestro completo disponible; la inferencia y el clustering aplican además la elegibilidad histórica. Los géneros se cuentan como pertenencias múltiples; faltan tres fechas, sin inventar década. Team no acredita roles de desarrollo.

# Evidencia documental de escalas

## Escalas verificadas antes de calcular la brecha

Consulta de documentación primaria: **8 de noviembre de 2026**. No se reemplazaron notas ni conteos del CSV por valores actuales del sitio.

- [Backloggd: página oficial de Elden Ring](https://backloggd.com/games/elden-ring/) muestra la media junto al gráfico de estrellas cuyo extremo superior es **5 estrellas**. [Su FAQ](https://backloggd.com/about/) distingue la media del juego y el promedio ponderado utilizado para ordenar. Esta evidencia respalda el denominador cinco; no prueba por sí sola cómo se extrajo cada fila histórica.
- [Metacritic: interpretación del Metascore](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore) documenta una escala de **0–100** para prensa.
- Los rangos del CSV son compatibles con esas escalas. El derivado heredado `rating_100` coincide con multiplicar por 20, pero se usa solo como corroboración y no como prueba independiente de la escala.

Se aplicará una conversión por el máximo documentado: `rating_normalizado = Rating / 5 × 100`; `brecha = rating_normalizado − Metacritic Rating` solo cuando la nota crítica tenga procedencia válida según el maestro.
No se usa normalización min–max de la muestra: convertir 0.7 y 4.8 en los extremos produciría una brecha dependiente de los juegos incluidos. La conversión tampoco afirma equivalencia psicométrica entre ambas plataformas.


## Que debo verificar manualmente

- Procedencia de notas, escala histórica y decisiones de deduplicación.
- Roles de Team, fechas TBD y títulos iguales en versiones distintas.

````

## limpieza_log.md

Ruta: `Final/reports/limpieza_log.md` · Bytes: 7436 · SHA-256: `dd4b45eb48ce4f385f86d51166ea06cc0347fe85bf67370a74a70b86f8ae8d45`

````text
# Log de limpieza

SHA-256 del insumo inmutable: `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`.

Fuente: `data/raw/games_curated.csv`. Decisiones previas: `reports/inspeccion.md`.

| Paso | Filas antes | Filas después | Eliminadas | Razón del cambio | Detalle |
|---|---:|---:|---:|---|---|
| 1. Validación y conversión de conteos | 1117 | 1117 | 0 | Sin cambio de filas | En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución. |
| 2. Fechas | 1117 | 1117 | 0 | Sin cambio de filas | 0 fechas ausentes y 3 no interpretables; no se eliminan juegos. |
| 3. Géneros | 1117 | 1117 | 0 | Sin cambio de filas | Primer género no vacío como convención de presentación; tabla larga tras deduplicar. |
| 4. Faltantes y procedencia | 1117 | 1117 | 0 | Sin cambio de filas | Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa. |
| 5. Duplicados | 1117 | 1117 | 0 | Sin cambio de filas | Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución. |
| 6. Escalas y brecha | 1117 | 1117 | 0 | Sin cambio de filas | Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra. |
| 7. Preparación de exportación | 1117 | 1117 | 0 | Sin cambio de filas | Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one. |

## Decisiones y justificación

**Conteos y fechas.** Se convierten solo formatos numéricos reconocidos; los inválidos causan un error con columna y fila. Las fechas desconocidas o imposibles se conservan como NaT con indicador: inventar un año alteraría el análisis por década.

**Faltantes.** No se imputan notas ni se eliminan juegos por ausencia. La imputación estadística pertenece al entrenamiento dentro de cada fold; en análisis descriptivo se usan pares completos e indicadores para mostrar la cobertura.

**Procedencia.** Se conserva Metacritic original en metacritic_rating_original y se usa critic_score_final con su etiqueta de fuente para la columna analítica. Una nota derivada de Rating no aporta evidencia independiente de prensa; la etiqueta del CSV no demuestra verificación externa.

**Géneros.** El primer elemento no vacío es una convención de presentación, no un género dominante acreditado. La tabla larga conserva cada género distinto y el ID; sus filas no se suman para contar juegos únicos.

**Duplicados.** Solo se descartan equivalencias analíticas bajo la clave documentada y se guardan las filas eliminadas. Un conflicto impide exportar para evitar seleccionar una cifra sin fundamento.

## Verificación de escalas previa a la brecha

Fuentes primarias consultadas el 08/11/2026: [Backloggd, extremo superior de cinco estrellas](https://backloggd.com/games/elden-ring/) y [Metacritic, escala 0–100](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore). No se descargan ni sustituyen puntuaciones actuales.

Conversión por máximo documentado: `rating_normalizado = Rating × 100 / 5`; `brecha = rating_normalizado − Metacritic Rating`. Positiva: usuarios por encima de prensa; negativa: por debajo. No se trasladan los extremos observados de la muestra a 0 y 100, ni se afirma equivalencia psicométrica.

Rango observado Rating: 0.7–4.8; Metacritic original: 45–99; crítica analítica: 45–99.

## Conciliación comprobable

El bloque JSON permite contrastar el log con la tabla exportada. Toda disminución requiere una razón; ningún otro paso puede añadir o eliminar juegos.

```json
{
  "filas_entrada": 1117,
  "filas_salida": 1117,
  "filas_generos_largo": 2682,
  "pasos": [
    {
      "paso": "1. Validación y conversión de conteos",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución."
    },
    {
      "paso": "2. Fechas",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "0 fechas ausentes y 3 no interpretables; no se eliminan juegos."
    },
    {
      "paso": "3. Géneros",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Primer género no vacío como convención de presentación; tabla larga tras deduplicar."
    },
    {
      "paso": "4. Faltantes y procedencia",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa."
    },
    {
      "paso": "5. Duplicados",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución."
    },
    {
      "paso": "6. Escalas y brecha",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra."
    },
    {
      "paso": "7. Preparación de exportación",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one."
    }
  ]
}
```

## Que debo verificar manualmente

- Representación de cinco estrellas en la extracción histórica, media absoluta/ponderada y origen de cada nota de prensa.
- Fechas numéricas ambiguas: se usa día/mes/año; consultar las marcadas no interpretables.
- Orden de la lista de géneros y posibles plataformas o versiones distintas con igual título/fecha.
- Las ausencias de crítica utilizable incluyen estimaciones excluidas; no significan que el juego no tenga nota fuera del CSV.

## Antecedente de la deduplicación

Estado: verificado. Esta corrida no elimina las 395 filas históricas: ya no están en el maestro de entrada. Ver trazabilidad_historica.md, deduplicacion_historica.csv y conflictos_historicos.csv para decisiones por ID. No confundir 0 descartes actuales con ausencia de decisiones anteriores.

## Que debo verificar manualmente

- Resolver los conflictos heredados y usar id_juego para relacionar tablas.

````

## maestro_reconstruido_solo_auditoria.csv

Ruta: `Final/reports/maestro_reconstruido_solo_auditoria.csv` · Bytes: 2500342 · SHA-256: `71f92cd365674936574fbec253addf1f03ef79c7123f495bc8edf6f7c0083fff`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## manifest.json

Ruta: `Final/reports/manifest.json` · Bytes: 1845 · SHA-256: `aa739070d576a48ff8d888975bb95d0ae857f5ddf99b2aa8d04bd3157f6747a9`

````text
{
  "huella_pipeline": "3f9e936a176da82a4b2a92be4fa565002546a7ee98cdef1901f3d30ee6a907a1",
  "fuente_clustering": "data/clean/dataset_depurado.csv",
  "artefacto_clustering": "data/clean/dataset_con_clusters.csv",
  "modelo_popularidad": "models/modelo_popularidad.joblib",
  "metadata_modelo": "models/metadata.json",
  "sha256_modelo_popularidad": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e",
  "sha256_metadata_modelo": "07ba1ce664747e68c06c7ab9dc799e8ccb565cf71e7222b3a6de9f8548eed2fa",
  "sha256_vecinos": "23d0ad2353a64b567cd1c40d40b70735e4450ae9a2b731519ba5aa65a1f95415",
  "sha256_dataset_depurado": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "sha256_dataset_con_clusters": "d35537b44658aeeefbacd0ebac8c6cd785e73004e5ec0b1ac7baf3c82fd4077a",
  "sha256_reportes_app": {
    "clustering_03_parametros.json": "df298240ede139bee39b1c275e326993fdebc7df6a2250854864a839b8d0089b",
    "clustering_03_correlaciones_catalogo.csv": "73efe968de1a24e4d8f7418e59345b20b71f5730d3c8f7dc9eb65b64b7ee2175",
    "clustering_03_correlaciones_generos.csv": "5869c0c310fe9e29da498effb41c0134dcb473c8d659db8004a7d7b7f5a1cdda",
    "clustering_03_correlaciones_organizaciones.csv": "86304ee58a3749c71dbfed9eded58fee43a3d7dd81232f33082909e42f53cd95",
    "clustering_03_correlaciones_ranking_generos.csv": "149d78bb3b84b1aeb32e3dbdb34cf0eef72ae8e2947d5333a3af132965ce5131",
    "clustering_03_perfiles.csv": "21a24f23191e0353093d3ec65790da70a7398ec27f5c8d158f8acbaf59b01265",
    "clustering_03_alternativas_k.csv": "83a307d8df56e722e89679c47b445303b69b3f23e61a06ec2a51670a85e09391",
    "clustering_03_seleccion_kmeans.csv": "344e5e4cbe1fde8c00e6ad22b368c76fa71d800896b68872e550bd10463ad038",
    "clustering_03_sensibilidad_dbscan.csv": "59c1d25653df3a03d79885db1dca9bda619767e6349516f6b4228578690305e8"
  }
}
````

## modelo.md

Ruta: `Final/reports/modelo.md` · Bytes: 9206 · SHA-256: `1c384f25685efe5bd987fe7249452b892edf120a035f1fbaffb06ee74a5bb96d`

````text
# Modelo supervisado corregido tras la segunda auditoría

## Objetivo y separación de datos

Se mantiene el índice de rangos percentiles de Plays, Wishlist y Backlogs con pesos iguales. Solo Plays es más simple, pero omite interés pendiente; el índice elegido da dos tercios del peso a dos señales de interés correlacionadas. Playing se usa en EDA/clustering, pero no en el target ni como predictor del clasificador.

Antes de calcular etiquetas se divide por grupos de título mediante GroupShuffleSplit con semilla 42: 892 entrenamiento y 222 prueba. La proporción 80/20 es aproximada por grupos; no se fuerza estratificación en clases aún no definidas ni se buscan repartos por rechazo.

En entrenamiento se ajustan los rangos medios/N y sus terciles: [0.3622944693572496, 0.6266816143497758]. La prueba se interpola contra esos mismos valores, con percentil 0 por debajo del mínimo y 1 sobre el máximo de entrenamiento. Los empates comparten etiqueta. La referencia tiene N=892; nunca usa los conteos de prueba.

La CV de diez pliegues agrupa títulos y organiza estratos con las etiquetas externas de entrenamiento. Dentro de cada fit se recalculan referencia, cortes, etiquetas, categorías e imputación usando solo el subentrenamiento; score construye las etiquetas de validación con esa referencia local. GridSearchCV recibe un estimador de contexto que separa las tres señales del objetivo de las cinco entradas predictivas. Las referencias e IDs se guardan en models/referencias_folds.json.

## Entradas y Naive Bayes

Predictores: ['generos', 'estudio', 'decada', 'Metacritic Rating', 'Rating']. Ningún conteo, índice, cluster, componente PCA, indicador de procedencia o bandera de ausencia entra al Pipeline final.

Géneros frecuentes: multi-hot de hasta 15 con frecuencia mínima 20 en cada ajuste. Estudio representa organizaciones de Team con mínimo 10; Otro se activa solo cuando no existe ninguna organización frecuente en la lista. Las listas vacías usan Sin dato; no se atribuye rol desarrollador por posición.

Notas: mediana ajustada solo con entrenamiento, sin MissingIndicator. StandardScaler se aplica exclusivamente a las dos notas continuas para árboles/bosque/referencia; los otros indicadores se mantienen en 0/1. La curación de Metacritic sigue siendo una fuente posible de sesgo no aleatorio, aun sin bandera explícita.

Se reemplaza GaussianNB por CategoricalNB: la mayoría de atributos son indicadores categóricos y las dos notas se discretizan en cinco intervalos de ancho uniforme entre los extremos de entrenamiento de cada fold. min_categories=5 permite códigos nuevos dentro del rango; alpha se ajusta en tres valores. Se reconoce pérdida de resolución por discretización e independencia condicional aproximada; no se ajustan gaussianas a decenas de dummies raras.

## Comparación y selección

| modelo | f1_macro_cv | desviacion_cv | exactitud_prueba | f1_macro_prueba | balanced_accuracy_prueba | mejores_parametros |
| --- | --- | --- | --- | --- | --- | --- |
| DummyClassifier | 0.1678 | 0.0031 | 0.3018 | 0.1546 | 0.3333 | {} |
| CategoricalNB | 0.5490 | 0.0625 | 0.5090 | 0.4925 | 0.5192 | {"pipeline__clasificar__alpha": 5.0} |
| DecisionTreeClassifier | 0.5053 | 0.0458 | 0.5315 | 0.5119 | 0.5433 | {"pipeline__clasificar__max_depth": 8, "pipeline__clasificar__min_samples_leaf": 10} |
| RandomForestClassifier | 0.5567 | 0.0451 | 0.5676 | 0.5577 | 0.5753 | {"pipeline__clasificar__max_depth": null, "pipeline__clasificar__min_samples_leaf": 5} |

Ganador por F1 macro media de CV: **RandomForestClassifier**. Supera al modelo de referencia en esta partición; no se ha probado significancia estadística de la diferencia. Diferencia en prueba frente a referencia: 0.4031. No se usa la prueba para ajustar parámetros o cambiar ganador.

**Limitación visible del ganador:** recall de la clase medio = 33.8%. Una exactitud global razonable no permite afirmar que identifique bien esa clase; no se hizo una nueva búsqueda usando estos errores de prueba.

Dummy usa la clase realmente más frecuente en cada ajuste, con etiquetas locales; si hay empate, sklearn desempata por orden de clases. Los terciles tienden a equilibrar por construcción incluso sin fuga, por lo que una referencia mayoritaria cercana a F1 macro 1/6 es esperable y no un modelo comercial inteligente.

## Matrices y análisis de error por clase

Filas reales y columnas predichas: bajo, medio, alto.

### DummyClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 67 | 0 | 0 |
| medio | 80 | 0 | 0 |
| alto | 75 | 0 | 0 |

### CategoricalNB

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 42 | 12 | 13 |
| medio | 35 | 19 | 26 |
| alto | 11 | 12 | 52 |

### DecisionTreeClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 45 | 13 | 9 |
| medio | 34 | 18 | 28 |
| alto | 8 | 12 | 55 |

### RandomForestClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 43 | 14 | 10 |
| medio | 32 | 27 | 21 |
| alto | 9 | 10 | 56 |

| modelo | clase | n | aciertos | recall |
| --- | --- | --- | --- | --- |
| DummyClassifier | bajo | 67 | 67 | 1.0000 |
| DummyClassifier | medio | 80 | 0 | 0.0000 |
| DummyClassifier | alto | 75 | 0 | 0.0000 |
| CategoricalNB | bajo | 67 | 42 | 0.6269 |
| CategoricalNB | medio | 80 | 19 | 0.2375 |
| CategoricalNB | alto | 75 | 52 | 0.6933 |
| DecisionTreeClassifier | bajo | 67 | 45 | 0.6716 |
| DecisionTreeClassifier | medio | 80 | 18 | 0.2250 |
| DecisionTreeClassifier | alto | 75 | 55 | 0.7333 |
| RandomForestClassifier | bajo | 67 | 43 | 0.6418 |
| RandomForestClassifier | medio | 80 | 27 | 0.3375 |
| RandomForestClassifier | alto | 75 | 56 | 0.7467 |

La clase media se evalúa explícitamente: sus notas y géneros pueden solaparse con ambos extremos y sus fronteras son cortes artificiales de un continuo. Es una hipótesis interpretativa, no una causa demostrada; el recall observado no se oculta bajo la exactitud global. El rendimiento de CategoricalNB se informa por clase y no se presenta la antigua matriz de GaussianNB como resultado vigente.

## Permutation importance

| variable_cruda | caida_f1_macro_media | desviacion |
| --- | --- | --- |
| Rating | 0.0832 | 0.0221 |
| Metacritic Rating | 0.0817 | 0.0226 |
| generos | 0.0753 | 0.0211 |
| estudio | 0.0276 | 0.0164 |
| decada | 0.0193 | 0.0149 |

Caída de F1 macro sobre la prueba al permutar cada entrada cruda (listas completas para género/estudio), con 30 repeticiones y semilla 42. No es efecto causal ni intervalo de confianza; las variables correlacionadas comparten información. No se reoptimiza después de verla.

## Diagnóstico de cobertura de prensa y categoría Otro

{
  "prevalencia_otro": [
    {
      "particion": "entrenamiento",
      "fraccion_estudio_otro": 0.3968609865470852
    },
    {
      "particion": "prueba",
      "fraccion_estudio_otro": 0.44144144144144143
    }
  ],
  "n_criticas_ocultadas": 180,
  "delta_probabilidad_bajo_media": 0.03884582502696399,
  "delta_probabilidad_bajo_mediana": 0.008101477935920781,
  "f1_macro_ablacion_sin_critica": 0.5149234278266537,
  "limitacion": "La imputación puede seguir codificando cobertura; eliminar el indicador no garantiza ausencia de sesgo MNAR. Ablación de prueba solo diagnóstica, no reselección."
}

Las tablas modelo_ausencia_entrenamiento/prueba.csv muestran distribución de clases con y sin crítica. modelo_sensibilidad_critica.csv cuantifica el cambio de probabilidad baja al ocultar notas conocidas manteniendo los otros datos. La ablación sin crítica reutiliza parámetros elegidos y es diagnóstica: no selecciona otro modelo ni demuestra equidad. No se concluye que un Otro frecuente causara una importancia baja solo por observar ambos.

## Uso y reproducibilidad

models/modelo_popularidad.joblib contiene directamente el Pipeline y acepta un DataFrame con las cinco columnas crudas, listas o textos para categorías y nulos para notas. Las clases propias se serializan por valor con cloudpickle, compatible con joblib.load desde un proceso limpio sin src en PYTHONPATH; se conserva la dependencia de versiones de sklearn/pandas/numpy/cloudpickle.

models/metadata.json conserva referencia de entrenamiento, cortes, versiones, clases, fecha y métricas. models/vecinos_popularidad.joblib guarda NearestNeighbors ajustado únicamente al espacio predictivo de entrenamiento: las etiquetas de clusters solo se adjuntan por ID después de buscar, no intervienen en las distancias ni en la clasificación.

Fecha: 2026-11-09T08:35:00-06:00; sklearn 1.9.1; Python 3.15.2. Las métricas previas de objetivo global están archivadas y no son directamente comparables con las nuevas.

## Que debo verificar manualmente

- Pesos y redundancia del índice, antigüedad y representatividad de Backloggd.
- Procedencia de notas y sesgo de cobertura; la mediana puede conservar señales indirectas de ausencia.
- Identidad de juegos homónimos y roles de Team; los tres conflictos históricos siguen excluidos.
- Vecinos como similitud de atributos declarados, no recomendaciones de éxito ni causalidad.
- Probabilidades no calibradas y límites de la clase media.

````

## modelo_ausencia_entrenamiento.csv

Ruta: `Final/reports/modelo_ausencia_entrenamiento.csv` · Bytes: 199 · SHA-256: `e71eff4b1c50ce8b117a3452e01b5d3a6f9ed03c607ebb9cf123e5685306fbed`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_ausencia_prueba.csv

Ruta: `Final/reports/modelo_ausencia_prueba.csv` · Bytes: 170 · SHA-256: `d71c889b9e4f0808b06c72fe6687041c3541750ef4af501c7ecb36b703673f7e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_comparacion.csv

Ruta: `Final/reports/modelo_comparacion.csv` · Bytes: 804 · SHA-256: `e29e9984a2a4db275cc02c9c4537e8a4417b10fbc0340bb5c3ac36f2fcf18eb7`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_confusion_CategoricalNB.csv

Ruta: `Final/reports/modelo_confusion_CategoricalNB.csv` · Bytes: 75 · SHA-256: `8790218792d11544a9aaae236e6bbd9a175534ae7c4a3766ac35afed36ad5ddf`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_confusion_DecisionTreeClassifier.csv

Ruta: `Final/reports/modelo_confusion_DecisionTreeClassifier.csv` · Bytes: 73 · SHA-256: `8fa606d4f41c317c07ac0ffedcdb683f36e9f58ebb3f844f10a38c7a83cba5d9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_confusion_DummyClassifier.csv

Ruta: `Final/reports/modelo_confusion_DummyClassifier.csv` · Bytes: 69 · SHA-256: `f374dbc71336d72e07924480fff03af8fc598f0c84eb8835386e45fb3ca23608`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_confusion_RandomForestClassifier.csv

Ruta: `Final/reports/modelo_confusion_RandomForestClassifier.csv` · Bytes: 74 · SHA-256: `6e8923011f35fbe970d2569dba66daf31d6b737b7f1923dcf0ab2433ea7ae6d1`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_error_por_clase.csv

Ruta: `Final/reports/modelo_error_por_clase.csv` · Bytes: 539 · SHA-256: `8bf4ef9e1881b4d8055e5937f015272e3890cd5ea8bab6d89e699c726f0c4ca5`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_etiquetas_validacion_locales.csv

Ruta: `Final/reports/modelo_etiquetas_validacion_locales.csv` · Bytes: 10530 · SHA-256: `cb6e26a253dd4b6d51e09fec4edb14f75b76bd2ae4052503215a30bdf2875147`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_grid_cv.csv

Ruta: `Final/reports/modelo_grid_cv.csv` · Bytes: 16579 · SHA-256: `d0e823f28f0986d56bcd2fc864972ea081bb5a9168127d7857e871f4f6eda26e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_permutaciones_repeticiones.csv

Ruta: `Final/reports/modelo_permutaciones_repeticiones.csv` · Bytes: 3082 · SHA-256: `f564deb6980e5af2275ca2e9ebcce2501539d8a2c2eca406afa54c9804044ce6`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_permutation_importance.csv

Ruta: `Final/reports/modelo_permutation_importance.csv` · Bytes: 299 · SHA-256: `252e443a21922e0962fafe1269f4c8b757921f59bf0fe918857c299b22ae050c`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_predicciones_prueba.csv

Ruta: `Final/reports/modelo_predicciones_prueba.csv` · Bytes: 6814 · SHA-256: `366838a783ce7da31a39be2968a41a4413d5bf2b33194267a57425a45f044d18`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_sensibilidad_critica.csv

Ruta: `Final/reports/modelo_sensibilidad_critica.csv` · Bytes: 4358 · SHA-256: `800ccbc0a2b2b4e1c0eb1ec775889b58683951ff1d9075a0a3de2db350b360b9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## trazabilidad_historica.json

Ruta: `Final/reports/trazabilidad_historica.json` · Bytes: 688 · SHA-256: `9d4ca38697409a6673cdc8ffdecb5712b70144469eafa791c72204a8084edc2d`

````text
{
  "estado": "verificado",
  "sha256_historico": "6073f43d0c0bd5722b03789ff51c97c4ecd53686cdedbef93fc69d0c990245b6",
  "sha256_maestro": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
  "filas_historicas": 1512,
  "filas_maestro": 1117,
  "descartes_heredados": 395,
  "grupos_con_diferencias": 13,
  "grupos_con_conflicto_analitico": 3,
  "ids_analiticos_pendientes": [
    117,
    140,
    296
  ],
  "columnas_reconstruidas": 42,
  "diferencias_reconstruccion": [],
  "critica_estimada_maestro": 218,
  "estimaciones_con_rating": 214,
  "coeficientes_ajuste_sintetico": [
    8.583326609989347,
    50.95839691488483
  ],
  "residuo_maximo_tras_redondear": 0.0
}
````

## trazabilidad_historica.md

Ruta: `Final/reports/trazabilidad_historica.md` · Bytes: 1744 · SHA-256: `59ab6b572a61f5b3b2eba4dbde7a599a47e9f02cbc5c239e6daf1094fc2f2a9a`

````text
# Trazabilidad histórica

El maestro designado sigue siendo games_curated.csv y no se modifica. El antecedente de data/historical permite reproducir sus decisiones heredadas, no aprobarlas como correctas.

Se reconstruyen 1512 → 1117 registros, con 395 descartes documentados individualmente en deduplicacion_historica.csv. Estado de comparación de las 42 columnas: **verificado**; diferencias: [].

Hay 13 grupos con alguna diferencia, pero solo 3 con conflicto analítico. Los IDs conservados por la regla histórica y pendientes de resolución son [117, 140, 296]. Se preservan en el dataset con indicador y se excluyen del análisis principal y del entrenamiento hasta revisión, sin elegir el máximo ni promediar versiones desconocidas.

conflictos_historicos.csv identifica campos e IDs; variantes_historicas.csv conserva todas las alternativas de esos grupos. maestro_reconstruido_solo_auditoria.csv permite comparar sin escribir sobre raw.

La procedencia crítica se reconstruye a partir de Origen_calificacion: 218 notas propias se dejan sin critic_score_final. En 214 estimaciones con Rating, el ajuste es 8.583327 × Rating + 50.958397; residuo máximo tras redondear: 0.0. Esta relación corrobora dependencia sintética; no demuestra por sí sola el algoritmo histórico exacto ni verifica las notas marcadas Metacritic.

Los conteos se obtienen con un lector CSV: wc -l no cuenta registros cuando Reviews o Summary contienen saltos de línea.

## Que debo verificar manualmente

- Plataformas, versiones y fecha de captura de las tres discrepancias numéricas.
- Procedencia de las notas críticas y decisiones heredadas de la deduplicación.
- No interpretar una reconstrucción exacta como aprobación del criterio first.

````

## variantes_historicas.csv

Ruta: `Final/reports/variantes_historicas.csv` · Bytes: 68909 · SHA-256: `46323af2f92e799509ad167146a5eff72c65dc31dec481536d5c2b57ff5467e3`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## verificacion_independiente.json

Ruta: `Final/reports/verificacion_independiente.json` · Bytes: 550 · SHA-256: `acddeb63f69e204756722b28b1624f3c2fe2ec3602d2c949d8d35b3c94e14dda`

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

## verificar_integridad.py

Ruta: `Final/reports/verificar_integridad.py` · Bytes: 4987 · SHA-256: `fa84515eef53c5e7e70af632c03ff44f2e5dd059aa87e2776043f9c2feb4813f`

````text
"""Comprobación independiente; desde Final: python reports/verificar_integridad.py."""
from pathlib import Path
import hashlib
import json

import joblib
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.preprocessing import StandardScaler

raiz = Path(__file__).resolve().parents[1]
limpio = pd.read_csv(raiz / 'data/clean/dataset_depurado.csv')
clusters = pd.read_csv(raiz / 'data/clean/dataset_con_clusters.csv')
juegos = pd.read_csv(raiz / 'data/clean/juegos_modelo.csv')
meta = json.loads((raiz / 'models/metadata.json').read_text())
manifest = json.loads((raiz / 'reports/manifest.json').read_text())
salida = {}

original = raiz.parent / 'Proyecto/data/processed/games_curated.csv'
maestro = raiz / 'data/raw/games_curated.csv'
assert hashlib.sha256(maestro.read_bytes()).hexdigest() == 'b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd'
if original.exists():
    assert original.read_bytes() == maestro.read_bytes()
salida['original_intacto'] = True

archivos = {'modelo_popularidad': 'models/modelo_popularidad.joblib',
            'metadata_modelo': 'models/metadata.json', 'vecinos': 'models/vecinos_popularidad.joblib',
            'dataset_depurado': 'data/clean/dataset_depurado.csv',
            'dataset_con_clusters': 'data/clean/dataset_con_clusters.csv'}
for clave, ruta in archivos.items():
    assert hashlib.sha256((raiz / ruta).read_bytes()).hexdigest() == manifest['sha256_' + clave], ruta
for nombre, huella in manifest['sha256_reportes_app'].items():
    assert hashlib.sha256((raiz / 'reports' / nombre).read_bytes()).hexdigest() == huella, nombre
salida['artefactos_y_reportes_concuerdan'] = True

assert len(limpio) == len(clusters) == 1117
assert limpio.id_juego.is_unique and clusters.id_juego.is_unique
campos = ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Rating', 'Metacritic Rating']
mascara = limpio.elegible_analisis & limpio[campos].notna().all(axis=1)
assert set(clusters.loc[clusters.incluido_clustering, 'id_juego']) == set(limpio.loc[mascara, 'id_juego'])
assert clusters.loc[~clusters.incluido_clustering, ['cluster_kmeans', 'cluster_dbscan']].isna().all().all()
assert set(limpio.loc[~limpio.elegible_analisis, 'id_juego']) == {117, 140, 296}
assert not set(juegos.id_juego) & {117, 140, 296}
# Rating / 5 * 100 y Rating * 20 pueden diferir por redondeo de coma flotante.
np.testing.assert_allclose(limpio.brecha, limpio.Rating * 20 - limpio['Metacritic Rating'], equal_nan=True, atol=1e-10)
salida['filas_y_brecha'] = {'conservadas': len(limpio), 'agrupadas': int(mascara.sum()), 'no_agrupadas': int((~mascara).sum())}

pares = limpio.loc[limpio.elegible_analisis, ['Rating', 'Metacritic Rating']].dropna()
r, p = pearsonr(pares.Rating, pares['Metacritic Rating'])
rho, ps = spearmanr(pares.Rating, pares['Metacritic Rating'])
guardado = pd.read_csv(raiz / 'reports/clustering_03_correlaciones_catalogo.csv').iloc[0]
assert int(guardado['n']) == len(pares)
np.testing.assert_allclose([r, p, rho, ps], guardado[['pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']].astype(float), rtol=1e-10, atol=0)
salida['correlacion_recalculada'] = {'n': len(pares), 'pearson_r': float(r), 'pearson_p': float(p), 'spearman_rho': float(rho), 'spearman_p': float(ps)}

bundle = joblib.load(raiz / 'models/clustering_03.joblib')
x = clusters.loc[clusters.incluido_clustering, campos].copy()
conteos = campos[:4]
x[conteos] = np.log1p(x[conteos])
z = StandardScaler().fit_transform(x)
np.testing.assert_allclose(z, pd.read_csv(raiz / 'data/clean/clustering_espacio.csv'), atol=1e-12)
np.testing.assert_array_equal(bundle['kmeans'].predict(z), clusters.loc[clusters.incluido_clustering, 'cluster_kmeans'].astype(int))
np.testing.assert_array_equal(bundle['dbscan'].labels_, clusters.loc[clusters.incluido_clustering, 'cluster_dbscan'].astype(int))
salida['clusters_y_espacio_concordantes'] = True

prueba = juegos[juegos.particion.eq('prueba')].copy()
entrenamiento = juegos[juegos.particion.eq('entrenamiento')]
assert set(prueba.grupo_titulo).isdisjoint(entrenamiento.grupo_titulo)
for campo in ['generos', 'estudio']:
    prueba[campo] = prueba[campo].map(json.loads)
modelo = joblib.load(raiz / 'models/modelo_popularidad.joblib')
pred = modelo.predict(prueba[meta['variables']])
f1 = f1_score(prueba.nivel_popularidad, pred, average='macro')
acc = accuracy_score(prueba.nivel_popularidad, pred)
np.testing.assert_allclose([f1, acc], [meta['metricas']['f1_macro'], meta['metricas']['exactitud']])
np.testing.assert_array_equal(confusion_matrix(prueba.nivel_popularidad, pred, labels=meta['clases']), meta['metricas']['matriz_confusion'])
salida['metricas_recalculadas'] = {'n_prueba': len(prueba), 'f1_macro': f1, 'exactitud': acc}
(raiz / 'reports/verificacion_independiente.json').write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(salida, ensure_ascii=False, indent=2))

````

## weka_prueba_salida.txt

Ruta: `Final/reports/weka_prueba_salida.txt` · Bytes: 6238 · SHA-256: `a64f49b86a8e56c6abcb5a5dcc39d8e58c8c24ce1c51d181b648975e77f8cd34`

````text
WARNING: core mtj jar files are not available as resources to this classloader (jdk.internal.loader.ClassLoaders$AppClassLoader@7a8c5397)
0 1 
1 1 
2 1 
3 1 
4 1 
5 1 
6 1 
7 1 
8 1 
9 1 
10 1 
11 1 
12 1 
13 1 
14 1 
15 1 
16 1 
17 1 
18 1 
19 1 
20 1 
21 1 
22 1 
23 1 
24 1 
25 1 
26 1 
27 1 
28 1 
29 1 
30 1 
31 1 
32 1 
33 1 
34 1 
35 1 
36 1 
37 1 
38 1 
39 1 
40 1 
41 1 
42 1 
43 1 
44 1 
45 1 
46 1 
47 1 
48 1 
49 1 
50 1 
51 1 
52 1 
53 1 
54 1 
55 1 
56 0 
57 1 
58 1 
59 1 
60 1 
61 1 
62 1 
63 1 
64 1 
65 1 
66 1 
67 1 
68 1 
69 1 
70 1 
71 1 
72 1 
73 1 
74 1 
75 1 
76 1 
77 1 
78 1 
79 1 
80 1 
81 1 
82 1 
83 1 
84 1 
85 1 
86 1 
87 1 
88 1 
89 1 
90 1 
91 1 
92 1 
93 1 
94 1 
95 1 
96 1 
97 1 
98 1 
99 0 
100 1 
101 1 
102 1 
103 1 
104 1 
105 1 
106 1 
107 1 
108 1 
109 1 
110 1 
111 1 
112 1 
113 1 
114 1 
115 1 
116 1 
117 1 
118 1 
119 1 
120 1 
121 1 
122 1 
123 1 
124 1 
125 0 
126 1 
127 1 
128 1 
129 1 
130 1 
131 1 
132 1 
133 1 
134 1 
135 1 
136 1 
137 1 
138 1 
139 1 
140 0 
141 1 
142 1 
143 1 
144 1 
145 1 
146 1 
147 1 
148 1 
149 1 
150 1 
151 1 
152 1 
153 1 
154 1 
155 1 
156 1 
157 1 
158 1 
159 1 
160 1 
161 1 
162 1 
163 1 
164 0 
165 1 
166 1 
167 1 
168 1 
169 1 
170 1 
171 1 
172 1 
173 1 
174 1 
175 1 
176 1 
177 1 
178 1 
179 1 
180 1 
181 1 
182 1 
183 1 
184 1 
185 0 
186 1 
187 1 
188 1 
189 1 
190 1 
191 1 
192 1 
193 1 
194 1 
195 0 
196 1 
197 1 
198 1 
199 1 
200 1 
201 1 
202 0 
203 1 
204 1 
205 1 
206 1 
207 1 
208 1 
209 0 
210 1 
211 1 
212 1 
213 1 
214 0 
215 1 
216 1 
217 1 
218 1 
219 0 
220 1 
221 1 
222 1 
223 0 
224 1 
225 0 
226 1 
227 1 
228 0 
229 0 
230 0 
231 1 
232 1 
233 1 
234 1 
235 1 
236 1 
237 1 
238 0 
239 1 
240 1 
241 1 
242 1 
243 1 
244 1 
245 1 
246 1 
247 1 
248 1 
249 1 
250 0 
251 1 
252 1 
253 0 
254 1 
255 1 
256 0 
257 1 
258 1 
259 1 
260 1 
261 1 
262 0 
263 1 
264 1 
265 0 
266 0 
267 0 
268 0 
269 0 
270 0 
271 0 
272 0 
273 1 
274 1 
275 1 
276 1 
277 1 
278 1 
279 1 
280 1 
281 1 
282 1 
283 1 
284 1 
285 1 
286 1 
287 1 
288 1 
289 1 
290 1 
291 1 
292 0 
293 1 
294 0 
295 0 
296 1 
297 0 
298 1 
299 1 
300 1 
301 1 
302 1 
303 1 
304 0 
305 1 
306 1 
307 1 
308 0 
309 1 
310 1 
311 1 
312 0 
313 0 
314 1 
315 1 
316 1 
317 0 
318 0 
319 0 
320 0 
321 1 
322 0 
323 1 
324 0 
325 1 
326 1 
327 0 
328 0 
329 1 
330 1 
331 1 
332 1 
333 0 
334 1 
335 0 
336 1 
337 0 
338 1 
339 0 
340 0 
341 0 
342 0 
343 0 
344 1 
345 1 
346 1 
347 0 
348 1 
349 1 
350 0 
351 0 
352 0 
353 1 
354 0 
355 0 
356 1 
357 0 
358 1 
359 1 
360 0 
361 1 
362 1 
363 0 
364 0 
365 0 
366 1 
367 0 
368 0 
369 1 
370 0 
371 0 
372 1 
373 1 
374 0 
375 1 
376 0 
377 0 
378 1 
379 0 
380 1 
381 0 
382 1 
383 0 
384 0 
385 1 
386 0 
387 0 
388 0 
389 0 
390 0 
391 1 
392 0 
393 1 
394 0 
395 0 
396 0 
397 1 
398 1 
399 1 
400 1 
401 0 
402 0 
403 0 
404 0 
405 0 
406 1 
407 1 
408 0 
409 0 
410 0 
411 0 
412 1 
413 0 
414 0 
415 0 
416 0 
417 1 
418 0 
419 1 
420 0 
421 0 
422 0 
423 0 
424 0 
425 0 
426 0 
427 0 
428 0 
429 0 
430 0 
431 0 
432 0 
433 0 
434 0 
435 1 
436 0 
437 1 
438 0 
439 0 
440 1 
441 0 
442 0 
443 0 
444 0 
445 0 
446 0 
447 0 
448 0 
449 0 
450 0 
451 0 
452 0 
453 0 
454 0 
455 0 
456 1 
457 1 
458 1 
459 1 
460 1 
461 1 
462 1 
463 1 
464 1 
465 1 
466 1 
467 1 
468 1 
469 1 
470 1 
471 1 
472 1 
473 0 
474 0 
475 1 
476 1 
477 1 
478 0 
479 1 
480 1 
481 1 
482 1 
483 1 
484 1 
485 1 
486 1 
487 1 
488 1 
489 1 
490 1 
491 1 
492 1 
493 1 
494 0 
495 1 
496 0 
497 1 
498 0 
499 1 
500 1 
501 1 
502 1 
503 1 
504 1 
505 1 
506 1 
507 0 
508 1 
509 1 
510 1 
511 1 
512 1 
513 1 
514 1 
515 1 
516 1 
517 1 
518 1 
519 1 
520 0 
521 1 
522 1 
523 1 
524 1 
525 1 
526 0 
527 1 
528 1 
529 1 
530 0 
531 1 
532 0 
533 1 
534 0 
535 1 
536 1 
537 0 
538 1 
539 1 
540 1 
541 1 
542 1 
543 1 
544 1 
545 1 
546 1 
547 1 
548 0 
549 1 
550 1 
551 1 
552 1 
553 1 
554 1 
555 0 
556 1 
557 1 
558 0 
559 0 
560 1 
561 1 
562 0 
563 0 
564 0 
565 0 
566 1 
567 0 
568 1 
569 1 
570 1 
571 0 
572 1 
573 0 
574 0 
575 1 
576 1 
577 0 
578 1 
579 0 
580 1 
581 0 
582 1 
583 1 
584 0 
585 0 
586 0 
587 1 
588 0 
589 1 
590 1 
591 1 
592 1 
593 0 
594 0 
595 1 
596 0 
597 1 
598 1 
599 0 
600 0 
601 0 
602 0 
603 1 
604 0 
605 1 
606 1 
607 0 
608 1 
609 0 
610 1 
611 1 
612 1 
613 1 
614 1 
615 1 
616 0 
617 1 
618 0 
619 1 
620 1 
621 0 
622 0 
623 0 
624 0 
625 0 
626 1 
627 0 
628 0 
629 1 
630 0 
631 0 
632 1 
633 1 
634 0 
635 0 
636 0 
637 1 
638 0 
639 0 
640 0 
641 0 
642 0 
643 0 
644 1 
645 1 
646 0 
647 0 
648 0 
649 0 
650 0 
651 0 
652 1 
653 0 
654 0 
655 0 
656 0 
657 0 
658 0 
659 0 
660 0 
661 0 
662 0 
663 0 
664 1 
665 1 
666 0 
667 0 
668 0 
669 1 
670 0 
671 0 
672 0 
673 0 
674 1 
675 0 
676 0 
677 0 
678 0 
679 0 
680 0 
681 0 
682 0 
683 0 
684 0 
685 0 
686 0 
687 0 
688 0 
689 0 
690 1 
691 0 
692 0 
693 0 
694 0 
695 0 
696 0 
697 1 
698 0 
699 0 
700 1 
701 1 
702 0 
703 0 
704 0 
705 0 
706 0 
707 0 
708 0 
709 0 
710 0 
711 0 
712 0 
713 0 
714 0 
715 1 
716 0 
717 0 
718 0 
719 0 
720 0 
721 1 
722 0 
723 0 
724 0 
725 0 
726 0 
727 0 
728 0 
729 0 
730 0 
731 0 
732 0 
733 0 
734 0 
735 0 
736 0 
737 0 
738 0 
739 0 
740 0 
741 0 
742 0 
743 0 
744 0 
745 0 
746 0 
747 0 
748 0 
749 0 
750 0 
751 0 
752 0 
753 1 
754 0 
755 0 
756 0 
757 0 
758 0 
759 0 
760 0 
761 0 
762 0 
763 0 
764 0 
765 0 
766 0 
767 0 
768 0 
769 0 
770 0 
771 0 
772 0 
773 0 
774 0 
775 0 
776 0 
777 0 
778 0 
779 0 
780 0 
781 0 
782 0 
783 0 
784 0 
785 0 
786 0 
787 0 
788 0 
789 0 
790 0 
791 0 
792 0 
793 0 
794 0 
795 0 
796 0 
797 0 
798 0 
799 0 
800 0 
801 0 
802 0 
803 0 
804 0 
805 0 
806 0 
807 0 
808 0 
809 0 
810 0 
811 0 
812 0 
813 0 
814 0 
815 0 
816 0 
817 0 
818 0 
819 0 
820 0 
821 0 
822 0 
823 0 
824 0 
825 0 
826 0 
827 0 
828 0 
829 0 
830 0 
831 0 
832 0 
833 0 
834 0 
835 0 
836 0 
837 0 
838 0 
839 0 
840 0 
841 0 
842 0 
843 0 
844 0 
845 0 
846 0 
847 0 
848 0 
849 0 
850 0 
851 0 
852 0 
853 0 
854 0 
855 0 
856 0 
857 0 
858 0 
859 0 
860 0 
861 0 
862 0 
863 0 
864 0 
865 0 
866 0 
867 0 
868 0 
869 0 
870 0 
871 0 
872 0 
873 0 
874 0 
875 0 
876 0 
877 0 
878 0 
879 0 
880 0 
881 0 
882 0 
883 0 
884 0 
885 0 
886 0 


````

