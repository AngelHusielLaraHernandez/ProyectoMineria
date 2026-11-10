# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/weka/cierre_weka_2026_11_09.md

SHA-256: `cfe77d950e13a3887e238074f93ad985bd62fd9870a262c0d29cf23ff53ee1c4`

````text
# Cierre de pendientes de Weka — 9 de noviembre de 2026

Se revisaron los entregables pedidos para Weka 3.8.7. No se encontraron corridas ni archivos pendientes dentro de ese alcance. Las seis corridas ya realizadas conservan sus salidas completas, capturas y valores; no se volvieron a entrenar durante esta revisión.

| Entregable | Comprobación | Estado |
| --- | --- | --- |
| Entradas de clustering | 887 filas, seis variables; CSV y ARFF idénticos valor por valor | Completo |
| SimpleKMeans | k=2, semilla 42, seis centroides por variable, tamaños 477/410 y captura | Completo |
| DBSCAN | eps=1.666296, minPoints=12, 887 asignaciones verificadas y captura | Completo |
| Clasificación | 892 filas, 53 atributos; último atributo nivel_popularidad nominal; CSV y ARFF idénticos | Completo |
| ZeroR, NaiveBayes, J48, RandomForest | Diez pliegues estratificados, salidas completas y matrices que suman 892 | Completo |
| Comparativo | Exactitud y F-Measure ponderada transcritas sin diferencias frente a las salidas | Completo |
| Capturas y respaldo | Imágenes válidas, hashes e integridad del ZIP verificados | Completo |

Se volvió a abrir Explorer y se cargó clasificacion.arff. La interfaz confirmó 892 instancias, 53 atributos y Class: nivel_popularidad (Nom). Evidencia nueva: [captura actual de Explorer](revision_explorer_2026_11_09.jpg). Las clases del archivo contienen alto=297, medio=297 y bajo=298.

Auditoría detallada: [auditoria_cierre_2026_11_09.json](auditoria_cierre_2026_11_09.json). Los resultados de rendimiento siguen en [resumen_gui.md](resumen_gui.md).

## Que debo verificar manualmente

- Estas comprobaciones corresponden a Weka; Orange se descartó como desviación técnica documentada en reports/codex_log.md.
- Weka muestra F1 ponderado y exactitud en porcentaje; no confundirlos con F1 macro y el conjunto de prueba de Python.
- Las diferencias de clustering frente a Python se conservan registradas; no se ajustaron parámetros para igualarlas.

````

## Origen: Final/reports/weka/explorer_3_8_7_ventana.log

SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````text

````

## Origen: Final/reports/weka/gui_inicio.log

SHA-256: `3444a826f909213311f78da6fad3d45060f1482635f03bf95d0f7897d7a5b52e`

````text
Unable to create WEKA_HOME (/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/weka/.home/wekafiles)
Unable to create packages directory (/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/weka/.home/wekafiles/packages)
Unable to create native libs directory (/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/weka/.home/wekafiles/native)
Unable to create repository cache directory (/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/weka/.home/wekafiles/repCache)
WARNING: core mtj jar files are not available as resources to this classloader (jdk.internal.loader.ClassLoaders$AppClassLoader@7a8c5397)

````

## Origen: Final/reports/weka/gui_inicio_reanudado.log

SHA-256: `ed7859a6b5bfa1c87681b47c4a322373a541415f41f4e1072aa12a8eb8e437b9`

````text
WARNING: core mtj jar files are not available as resources to this classloader (jdk.internal.loader.ClassLoaders$AppClassLoader@7a8c5397)
java.lang.ClassNotFoundException: com.formdev.flatlaf.FlatLightLaf
	java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	java.base/java.lang.Class.forName0(Native Method)
	java.base/java.lang.Class.forName(Class.java:547)
	java.desktop/javax.swing.SwingUtilities.loadSystemClass(SwingUtilities.java:2027)
	java.desktop/javax.swing.UIManager.setLookAndFeel(UIManager.java:629)
	weka.gui.LookAndFeel.setLookAndFeel(LookAndFeel.java:110)
	weka.gui.LookAndFeel.setLookAndFeel(LookAndFeel.java:158)
	weka.gui.GUIChooserApp.main(GUIChooserApp.java:1663)
	java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
	java.base/java.lang.reflect.Method.invoke(Method.java:565)
	weka.gui.SplashWindow.invokeMain(SplashWindow.java:306)
	weka.gui.GUIChooser.main(GUIChooser.java:92)

	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:580)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:547)
	at java.desktop/javax.swing.SwingUtilities.loadSystemClass(SwingUtilities.java:2027)
	at java.desktop/javax.swing.UIManager.setLookAndFeel(UIManager.java:629)
	at weka.gui.LookAndFeel.setLookAndFeel(LookAndFeel.java:110)
	at weka.gui.LookAndFeel.setLookAndFeel(LookAndFeel.java:158)
	at weka.gui.GUIChooserApp.main(GUIChooserApp.java:1663)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
	at java.base/java.lang.reflect.Method.invoke(Method.java:565)
	at weka.gui.SplashWindow.invokeMain(SplashWindow.java:306)
	at weka.gui.GUIChooser.main(GUIChooser.java:92)
Exception in thread "main" java.lang.Error: Failed to invoke main method
	weka.gui.SplashWindow.invokeMain(SplashWindow.java:319)
	weka.gui.GUIChooser.main(GUIChooser.java:92)

	at weka.gui.SplashWindow.invokeMain(SplashWindow.java:319)
	at weka.gui.GUIChooser.main(GUIChooser.java:92)
Caused by: java.lang.reflect.InvocationTargetException
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:119)
	at java.base/java.lang.reflect.Method.invoke(Method.java:565)
	at weka.gui.SplashWindow.invokeMain(SplashWindow.java:306)
	... 1 more
Caused by: java.lang.UnsupportedOperationException: Setting a Security Manager is not supported
	at java.base/java.lang.System.setSecurityManager(System.java:304)
	at weka.gui.GUIChooserApp.main(GUIChooserApp.java:1675)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
	... 3 more

````

## Origen: Final/reports/weka/resumen_gui.md

SHA-256: `f22bbd098d5928e5a0a0cbe41bc9f8aaea474a31d4bda0df47fd9cf1bc42ec79`

````text
# Corridas gráficas verificadas de Weka 3.8.7

Los modelos se ejecutaron mediante Start en Explorer. Las salidas completas se copiaron del panel de resultados; los scripts de control solo operan la interfaz.

## Clasificación

Dataset: 892 registros y 53 atributos, con nivel_popularidad como clase nominal. Se cargó clasificacion.arff, copia verificada de clasificacion.csv; 52 entradas y una clase. Evaluación: validación cruzada estratificada de 10 pliegues. No se modificaron los parámetros predeterminados de los clasificadores.

| Modelo | Exactitud mostrada (%) | F-Measure ponderada mostrada | Salida | Captura |
| --- | --- | --- | --- | --- |
| ZeroR | 33.0717 | ? | [ZeroR.txt](ZeroR.txt) | [ZeroR.png](ZeroR.png) |
| NaiveBayes | 50.8969 | 0.503 | [NaiveBayes.txt](NaiveBayes.txt) | [NaiveBayes.png](NaiveBayes.png) |
| J48 | 51.009 | 0.506 | [J48.txt](J48.txt) | [J48.png](J48.png) |
| RandomForest | 53.4753 | 0.530 | [RandomForest.txt](RandomForest.txt) | [RandomForest.png](RandomForest.png) |

Se conserva ? cuando Weka lo muestra. No se calculó F1 macro ni se sustituyó una métrica indefinida. Las cuatro matrices tienen tres clases y suman 892; sus diagonales coinciden con los aciertos mostrados.

## K-Means

887 registros, seis atributos; k=2, semilla 42 y demás valores predeterminados de Weka. Se confirmó Use training set. Weka mostró 9 iteraciones y suma de errores cuadrados 76.63099068257982. Tamaños: 477 (54%) y 410 (46%). Los centroides completos están en [kmeans.txt](kmeans.txt).

## DBSCAN

Se verificó en Package Manager que optics_dbScan 1.0.6 está instalado y cargado (Loaded: Yes). El cierre completo y la reapertura de Weka fueron autorizados expresamente por el usuario. La instalación oficial y la posible escritura de sus componentes fuera de Final también fueron autorizadas.

Se cargó de nuevo clustering.arff y se confirmaron 887 instancias y seis atributos. Se seleccionó DBSCAN y se fijaron epsilon=1.666296 y minPoints=12, según reports/clustering.md. Se conservaron las demás opciones predeterminadas de la implementación de Weka: `weka.core.EuclideanDistance -R first-last`.

La corrida mediante Start / Use training set mostró Number of generated clusters: 1 y Clustered Instances: `0 887 (100%)`. Se verificaron las 887 asignaciones de la salida, con identificadores 0–886: todas tienen etiqueta 0 y ninguna tiene etiqueta de ruido. Ruido verificado: 0. No se inventa exactitud, F1 ni silhouette para esta salida.

Evidencias: [salida completa](dbscan.txt), [parámetros](dbscan_parametros.png), [resultado](dbscan_resultado.png) e [instalación confirmada](dbscan_paquete_instalado.png).

## Registro de diferencias con Python

Se registran sin modificar las corridas: Python reporta tamaños 465 y 422 para k=2; Weka GUI mostró 477 y 410. El reporte Python indica RandomForest con exactitud 0.5676 y F1 macro 0.5577 sobre el conjunto de prueba; Weka mostró exactitud 53.4753 % y F-Measure ponderada 0.530 en CV de 10 pliegues sobre 892 registros. Se conservan las definiciones y los protocolos de cada salida. Para DBSCAN, Python reporta un cluster con 866 juegos y 21 puntos de ruido; Weka GUI mostró un cluster con 887 juegos (100%) y sus 887 asignaciones tienen etiqueta 0. No se modificaron los parámetros para igualar esos resultados.

## Auditoría de cierre — 9 de noviembre de 2026

Se completó la comprobación de los seis entregables de Weka, los archivos de entrada, las capturas y el comparativo. No se encontraron pendientes en ese alcance. Véase [cierre_weka_2026_11_09.md](cierre_weka_2026_11_09.md). Se verificaron las corridas guardadas; no se ejecutaron nuevos entrenamientos durante esta revisión.

## Que debo verificar manualmente

- No confundir estas corridas GUI 3.8.7 con los artefactos CLI 3.8.6 anteriores de esta carpeta.
- F1 del comparativo Weka es ponderada; no es F1 macro. Exactitud se transcribió en porcentaje.
- Los datos exportados ya contienen transformaciones previas; esta evaluación no es el mismo protocolo de Python con ajuste dentro de cada pliegue.
- DBSCAN y K-Means conservan las opciones de distancia de Weka indicadas en sus salidas; registrar sus diferencias frente a Python sin sustituir valores.

## Actualización de comparación

Las salidas gráficas originales de este informe se conservan. El nuevo comparativo calcula F1 macro y resuelve los F1 indefinidos de ZeroR desde su matriz, con procedencia explícita; véase [metodología y verificación](../tables/comparativo_herramientas_notas.md). Los protocolos de evaluación actuales están identificados en el CSV y no deben inferirse del comparativo histórico.

````

## Origen: Final/reports/weka/revision_respaldo.md

SHA-256: `c2ffa83066679bce6ccdbeeaffe992844b6a32d56ac1ef12e83adfcc64abc0ab`

````text
# Revisión del respaldo y las capturas de Weka

Fecha: 2026-11-08T19:35:13.159127-06:00.

Primero se guardó una captura nueva de la ventana actual y un respaldo local; después se verificaron sus contenidos y se actualizó el respaldo final.

## Comprobaciones realizadas

- Se abrieron y revisaron visualmente las seis capturas de resultados: K-Means, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Son legibles y los números visibles corresponden a sus salidas completas.
- Se detectó que las 12 capturas principales tenían contenido JPEG bajo extensión .png. Se corrigió únicamente la codificación a PNG real, conservando sus originales JPEG en capturas_originales_jpeg. Se comprobó igualdad exacta de dimensiones, modo y todos los píxeles antes y después; perfiles de color y EXIF existentes se conservaron. Registro: conversion_capturas.json.
- Las cuatro matrices tienen tres clases, suman 892 y sus diagonales coinciden con los aciertos mostrados. Exactitud y F-Measure ponderada coinciden literalmente con el comparativo, incluido el signo ? de ZeroR.
- K-Means conserva k=2, semilla=42 y tamaños 477/410, que suman 887.
- DBSCAN conserva epsilon=1.666296 y minPoints=12. Sus 887 asignaciones tienen etiqueta 0, con identificadores 0–886 y sin omisiones.
- Se verificaron la integridad CRC del ZIP final, la ausencia de entradas duplicadas y los tamaños y hashes SHA-256 de sus contenidos. No se volvieron a entrenar modelos ni se alteraron sus resultados durante esta revisión.

## Que debo verificar manualmente

- Las capturas muestran la parte visible de cada panel; los TXT conservan las salidas completas.
- El comparativo de Weka usa exactitud en porcentaje y F1 ponderado, no F1 macro.
- Este respaldo acredita las corridas de Weka; Orange se descartó como desviación técnica documentada en reports/codex_log.md.

````

## Cierre de organización

Los 5 respaldos ZIP anteriores se reunieron sin pérdida en RESPALDO_UNIFICADO.zip. Se verificaron las 242 entradas contra sus hashes; las salidas gráficas originales y capturas siguen disponibles fuera del ZIP. El índice del respaldo identifica cada procedencia.
