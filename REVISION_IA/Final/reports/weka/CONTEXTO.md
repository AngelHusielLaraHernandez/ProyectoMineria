# Carpeta: Final/reports/weka

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/weka/BITACORA_UNIFICADA.md` · Bytes: 13576 · SHA-256: `04d259e72c3cebba3aa8c2b8a72eafc04da2d4838a7931ed2fbe20376e058a6f`

`````text
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

`````

## J48.png

Ruta: `Final/reports/weka/J48.png` · Bytes: 630962 · SHA-256: `72296d14f03af1520c8e07ca86310cb171b5a1b7f46b189701f3df514e184afd`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## J48.txt

Ruta: `Final/reports/weka/J48.txt` · Bytes: 17362 · SHA-256: `88ceace97d84c7c67628688f9876a4d3de22c07935e6111dd954f3c401a88c8c`

````text
=== Run information ===

Scheme:       weka.classifiers.trees.J48 -C 0.25 -M 2
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

J48 pruned tree
------------------

generos__Fighting <= 0
|   generos__Otro <= 0
|   |   notas__Metacritic Rating <= 0.1679
|   |   |   notas__Rating <= -2.152384
|   |   |   |   estudio__Capcom <= 0: bajo (18.0/1.0)
|   |   |   |   estudio__Capcom > 0: alto (3.0/1.0)
|   |   |   notas__Rating > -2.152384
|   |   |   |   generos__Adventure <= 0
|   |   |   |   |   estudio__Atlus <= 0
|   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   generos__Brawler <= 0
|   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   estudio__Nintendo <= 0
|   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 <= 0: bajo (61.0/19.0)
|   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 > 0
|   |   |   |   |   |   |   |   |   |   |   generos__Shooter <= 0: medio (11.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Shooter > 0: bajo (5.0/1.0)
|   |   |   |   |   |   |   |   |   estudio__Nintendo > 0: medio (20.0/9.0)
|   |   |   |   |   |   |   |   generos__Puzzle > 0
|   |   |   |   |   |   |   |   |   generos__Indie <= 0: bajo (9.0)
|   |   |   |   |   |   |   |   |   generos__Indie > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   generos__Brawler > 0
|   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   generos__Arcade <= 0
|   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -1.47338: medio (2.0)
|   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -1.47338: alto (3.0)
|   |   |   |   |   |   |   |   |   generos__Arcade > 0: bajo (2.0/1.0)
|   |   |   |   |   |   |   |   generos__RPG > 0: bajo (4.0/1.0)
|   |   |   |   |   |   estudio__Square Enix > 0: medio (8.0/2.0)
|   |   |   |   |   estudio__Atlus > 0
|   |   |   |   |   |   decada__decada_1990.0 <= 0: alto (5.0/1.0)
|   |   |   |   |   |   decada__decada_1990.0 > 0: bajo (2.0/1.0)
|   |   |   |   generos__Adventure > 0
|   |   |   |   |   decada__decada_2010.0 <= 0
|   |   |   |   |   |   estudio__Game Freak <= 0
|   |   |   |   |   |   |   estudio__Konami <= 0
|   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.379193
|   |   |   |   |   |   |   |   |   estudio__Sonic Team <= 0: bajo (53.0/22.0)
|   |   |   |   |   |   |   |   |   estudio__Sonic Team > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.379193
|   |   |   |   |   |   |   |   |   estudio__Square <= 0
|   |   |   |   |   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   |   |   |   |   generos__Turn Based Strategy <= 0
|   |   |   |   |   |   |   |   |   |   |   |   generos__Brawler <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Nintendo <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Annapurna Interactive <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Capcom <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.24242
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_2000.0 <= 0: alto (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_2000.0 > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.106347: bajo (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.106347: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.24242
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.031127: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.031127
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel <= 0: bajo (13.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel > 0: medio (8.0/3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: bajo (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 > 0: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Capcom > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= 0.079656: bajo (13.0/5.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > 0.079656: alto (5.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Annapurna Interactive > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Nintendo > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= 0.079656: medio (9.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > 0.079656: alto (5.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   generos__Brawler > 0: alto (8.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Turn Based Strategy > 0: alto (5.0/1.0)
|   |   |   |   |   |   |   |   |   |   estudio__Square Enix > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   estudio__Square > 0: alto (3.0)
|   |   |   |   |   |   |   estudio__Konami > 0
|   |   |   |   |   |   |   |   generos__Platform <= 0: bajo (3.0)
|   |   |   |   |   |   |   |   generos__Platform > 0: medio (4.0)
|   |   |   |   |   |   estudio__Game Freak > 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (7.0/2.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (2.0)
|   |   |   |   |   decada__decada_2010.0 > 0
|   |   |   |   |   |   estudio__Sony Interactive Entertainment <= 0
|   |   |   |   |   |   |   notas__Metacritic Rating <= -1.8837
|   |   |   |   |   |   |   |   generos__Simulator <= 0: medio (6.0)
|   |   |   |   |   |   |   |   generos__Simulator > 0
|   |   |   |   |   |   |   |   |   notas__Rating <= -0.85036: bajo (2.0)
|   |   |   |   |   |   |   |   |   notas__Rating > -0.85036: medio (3.0)
|   |   |   |   |   |   |   notas__Metacritic Rating > -1.8837
|   |   |   |   |   |   |   |   generos__Turn Based Strategy <= 0
|   |   |   |   |   |   |   |   |   estudio__Sony Computer Entertainment <= 0
|   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.85036
|   |   |   |   |   |   |   |   |   |   |   estudio__Ubisoft Entertainment <= 0: medio (24.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Ubisoft Entertainment > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   notas__Rating > -0.85036
|   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel <= 0
|   |   |   |   |   |   |   |   |   |   |   |   estudio__Otro <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Activision <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0: alto (32.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Strategy <= 0: medio (8.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Strategy > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Activision > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   estudio__Otro > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0: medio (19.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__RPG > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.926287: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.926287: alto (10.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel > 0
|   |   |   |   |   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__Indie <= 0: bajo (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__Indie > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   generos__RPG > 0: bajo (2.0)
|   |   |   |   |   |   |   |   |   estudio__Sony Computer Entertainment > 0: alto (4.0/1.0)
|   |   |   |   |   |   |   |   generos__Turn Based Strategy > 0
|   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.031127: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.031127: medio (3.0)
|   |   |   |   |   |   estudio__Sony Interactive Entertainment > 0: alto (7.0/1.0)
|   |   notas__Metacritic Rating > 0.1679
|   |   |   generos__Racing <= 0
|   |   |   |   generos__Strategy <= 0
|   |   |   |   |   decada__decada_1990.0 <= 0
|   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   notas__Rating <= 0.079656
|   |   |   |   |   |   |   |   estudio__Activision <= 0
|   |   |   |   |   |   |   |   |   decada__decada_2000.0 <= 0
|   |   |   |   |   |   |   |   |   |   generos__Arcade <= 0
|   |   |   |   |   |   |   |   |   |   |   estudio__Electronic Arts <= 0: alto (36.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Electronic Arts > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   generos__Arcade > 0: bajo (2.0/1.0)
|   |   |   |   |   |   |   |   |   decada__decada_2000.0 > 0
|   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   |   |   estudio__Microsoft Game Studios <= 0
|   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.106347
|   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.292351
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Adventure <= 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.441447: bajo (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.441447: medio (8.0/3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.292351: medio (7.0)
|   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.106347: alto (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Microsoft Game Studios > 0: medio (3.0)
|   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: bajo (2.0)
|   |   |   |   |   |   |   |   estudio__Activision > 0: medio (3.0/1.0)
|   |   |   |   |   |   |   notas__Rating > 0.079656: alto (155.0/37.0)
|   |   |   |   |   |   estudio__Square Enix > 0
|   |   |   |   |   |   |   decada__decada_2020.0 <= 0
|   |   |   |   |   |   |   |   notas__Rating <= 1.195676: alto (5.0)
|   |   |   |   |   |   |   |   notas__Rating > 1.195676: medio (3.0)
|   |   |   |   |   |   |   decada__decada_2020.0 > 0: medio (6.0/1.0)
|   |   |   |   |   decada__decada_1990.0 > 0
|   |   |   |   |   |   generos__Adventure <= 0: medio (3.0)
|   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (5.0/1.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (6.0)
|   |   |   |   generos__Strategy > 0
|   |   |   |   |   decada__decada_2020.0 <= 0
|   |   |   |   |   |   generos__Adventure <= 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (7.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (3.0/1.0)
|   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   notas__Rating <= -0.478354: medio (3.0/1.0)
|   |   |   |   |   |   |   notas__Rating > -0.478354: alto (4.0/1.0)
|   |   |   |   |   decada__decada_2020.0 > 0: bajo (3.0/1.0)
|   |   |   generos__Racing > 0
|   |   |   |   generos__Adventure <= 0
|   |   |   |   |   notas__Rating <= -0.478354: bajo (2.0)
|   |   |   |   |   notas__Rating > -0.478354: medio (9.0/3.0)
|   |   |   |   generos__Adventure > 0: alto (2.0)
|   generos__Otro > 0
|   |   estudio__Capcom <= 0
|   |   |   decada__decada_1990.0 <= 0
|   |   |   |   generos__Visual Novel <= 0
|   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   estudio__Nintendo <= 0: bajo (52.0/13.0)
|   |   |   |   |   |   estudio__Nintendo > 0
|   |   |   |   |   |   |   decada__decada_2010.0 <= 0
|   |   |   |   |   |   |   |   notas__Rating <= -0.106347: bajo (5.0)
|   |   |   |   |   |   |   |   notas__Rating > -0.106347: medio (4.0/1.0)
|   |   |   |   |   |   |   decada__decada_2010.0 > 0: medio (2.0)
|   |   |   |   |   generos__RPG > 0
|   |   |   |   |   |   decada__decada_2010.0 <= 0: medio (5.0/1.0)
|   |   |   |   |   |   decada__decada_2010.0 > 0
|   |   |   |   |   |   |   generos__Puzzle <= 0: bajo (2.0)
|   |   |   |   |   |   |   generos__Puzzle > 0: alto (2.0)
|   |   |   |   generos__Visual Novel > 0
|   |   |   |   |   decada__decada_2010.0 <= 0: medio (4.0)
|   |   |   |   |   decada__decada_2010.0 > 0: alto (2.0/1.0)
|   |   |   decada__decada_1990.0 > 0: bajo (4.0)
|   |   estudio__Capcom > 0: medio (3.0/1.0)
generos__Fighting > 0
|   estudio__Ubisoft Entertainment <= 0
|   |   estudio__WB Games <= 0
|   |   |   estudio__Nintendo <= 0: bajo (43.0/9.0)
|   |   |   estudio__Nintendo > 0: medio (4.0/2.0)
|   |   estudio__WB Games > 0: medio (5.0/1.0)
|   estudio__Ubisoft Entertainment > 0: medio (2.0)

Number of Leaves  : 	101

Size of the tree : 	201


Time taken to build model: 0.17 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         455               51.009  %
Incorrectly Classified Instances       437               48.991  %
Kappa statistic                          0.2651
Mean absolute error                      0.3572
Root mean squared error                  0.4979
Relative absolute error                 80.3698 %
Root relative squared error            105.6156 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.650    0.224    0.592      0.650    0.620      0.417    0.744     0.549     alto
                 0.537    0.224    0.546      0.537    0.541      0.314    0.677     0.492     bajo
                 0.343    0.287    0.374      0.343    0.358      0.057    0.527     0.360     medio
Weighted Avg.    0.510    0.245    0.504      0.510    0.506      0.263    0.649     0.467     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 193  29  75 |   a = alto
  42 160  96 |   b = bajo
  91 104 102 |   c = medio

````

## NaiveBayes.png

Ruta: `Final/reports/weka/NaiveBayes.png` · Bytes: 623033 · SHA-256: `ef00fe5af3442fbbaa129aeef2a23c3c42e642d69773f6924fd261ada6056928`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## NaiveBayes.txt

Ruta: `Final/reports/weka/NaiveBayes.txt` · Bytes: 20846 · SHA-256: `5aac3e1f7f662eb504b71c7f77d1e31f2121a15ba7771c97b630a65bfd3027c6`

````text
=== Run information ===

Scheme:       weka.classifiers.bayes.NaiveBayes 
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

Naive Bayes Classifier

                                                      Class
Attribute                                              alto    bajo   medio
                                                     (0.33)  (0.33)  (0.33)
============================================================================
generos__Adventure
  mean                                                0.8148  0.4866   0.633
  std. dev.                                           0.3884  0.4998   0.482
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__RPG
  mean                                                0.3906  0.2282  0.3468
  std. dev.                                           0.4879  0.4197   0.476
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Shooter
  mean                                                0.2896  0.1846  0.1886
  std. dev.                                           0.4536  0.3879  0.3912
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Platform
  mean                                                0.2458  0.1946  0.2189
  std. dev.                                           0.4306  0.3959  0.4135
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Indie
  mean                                                 0.165  0.1946  0.1852
  std. dev.                                           0.3712  0.3959  0.3884
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Puzzle
  mean                                                0.1246  0.1275  0.1077
  std. dev.                                           0.3302  0.3336  0.3101
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Strategy
  mean                                                0.0471  0.1443  0.1044
  std. dev.                                           0.2119  0.3514  0.3057
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Brawler
  mean                                                0.1212  0.0839  0.0842
  std. dev.                                           0.3264  0.2772  0.2777
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Simulator
  mean                                                0.0572  0.1074  0.0774
  std. dev.                                           0.2323  0.3096  0.2673
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Fighting
  mean                                                0.0067  0.1208  0.0539
  std. dev.                                           0.1667  0.3259  0.2258
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Turn Based Strategy
  mean                                                 0.064  0.0336  0.0808
  std. dev.                                           0.2447  0.1801  0.2725
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Arcade
  mean                                                0.0236  0.0973  0.0505
  std. dev.                                           0.1667  0.2964   0.219
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Visual Novel
  mean                                                0.0303  0.0403  0.0572
  std. dev.                                           0.1714  0.1966  0.2323
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Racing
  mean                                                0.0101  0.0436  0.0505
  std. dev.                                           0.1667  0.2043   0.219
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Tactical
  mean                                                0.0202  0.0403  0.0438
  std. dev.                                           0.1667  0.1966  0.2046
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Otro
  mean                                                0.0202  0.1812  0.0875
  std. dev.                                           0.1667  0.3852  0.2826
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Sin dato
  mean                                                     0  0.0034  0.0034
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Nintendo
  mean                                                0.1785  0.0973  0.2121
  std. dev.                                           0.3829  0.2964  0.4088
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Capcom
  mean                                                0.0707  0.0638   0.037
  std. dev.                                           0.2563  0.2443  0.1889
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Square Enix
  mean                                                0.0438  0.0235  0.0774
  std. dev.                                           0.2046  0.1667  0.2673
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sega
  mean                                                0.0303   0.057  0.0337
  std. dev.                                           0.1714  0.2319  0.1804
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Electronic Arts
  mean                                                0.0337  0.0436   0.037
  std. dev.                                           0.1804  0.2043  0.1889
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Konami
  mean                                                0.0269  0.0302  0.0303
  std. dev.                                           0.1667  0.1711  0.1714
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Bandai Namco Entertainment
  mean                                                0.0337  0.0336  0.0168
  std. dev.                                           0.1804  0.1801  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Activision
  mean                                                0.0168  0.0369  0.0236
  std. dev.                                           0.1667  0.1885  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Ubisoft Entertainment
  mean                                                0.0404  0.0168  0.0202
  std. dev.                                           0.1969  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Atlus
  mean                                                 0.037  0.0134  0.0168
  std. dev.                                           0.1889  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Interactive Entertainment
  mean                                                0.0572       0  0.0101
  std. dev.                                           0.2323  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Nintendo EAD
  mean                                                0.0303  0.0067  0.0269
  std. dev.                                           0.1714  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Game Freak
  mean                                                0.0202  0.0034  0.0337
  std. dev.                                           0.1667  0.1667  0.1804
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__WB Games
  mean                                                0.0101  0.0168  0.0269
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Bethesda Softworks
  mean                                                0.0269  0.0101  0.0101
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Computer Entertainment
  mean                                                0.0269  0.0101  0.0101
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Square
  mean                                                0.0168  0.0067  0.0236
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Ubisoft Montreal
  mean                                                0.0236  0.0034  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Intelligent Systems Co., Ltd.
  mean                                                0.0101  0.0101  0.0202
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sonic Team
  mean                                                0.0101  0.0168  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Computer Entertainment, Inc. (SCEI)
  mean                                                0.0135  0.0101  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Devolver Digital
  mean                                                0.0168  0.0067  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__FromSoftware
  mean                                                0.0202  0.0168       0
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Annapurna Interactive
  mean                                                0.0101  0.0101  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Microsoft Game Studios
  mean                                                0.0168       0  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Otro
  mean                                                0.3098  0.5168  0.3636
  std. dev.                                           0.4624  0.4997   0.481
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sin dato
  mean                                                     0  0.0034       0
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_-1.0
  mean                                                     0  0.0067  0.0034
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_1980.0
  mean                                                0.0067  0.0235  0.0202
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_1990.0
  mean                                                0.0572  0.1208  0.1178
  std. dev.                                           0.2323  0.3259  0.3224
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2000.0
  mean                                                0.2323  0.2517  0.2559
  std. dev.                                           0.4223   0.434  0.4364
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2010.0
  mean                                                0.5387   0.349  0.4141
  std. dev.                                           0.4985  0.4767  0.4926
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2020.0
  mean                                                 0.165  0.2483  0.1886
  std. dev.                                           0.3712   0.432  0.3912
  weight sum                                             297     298     297
  precision                                                1       1       1

notas__Metacritic Rating
  mean                                                0.4438 -0.4334 -0.0818
  std. dev.                                           0.8149  1.0414  0.9321
  weight sum                                             297     298     297
  precision                                           0.1396  0.1396  0.1396

notas__Rating
  mean                                                0.4396 -0.3885 -0.0202
  std. dev.                                           0.7624  1.1617  0.8605
  weight sum                                             297     298     297
  precision                                           0.2311  0.2311  0.2311



Time taken to build model: 0.01 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         454               50.8969 %
Incorrectly Classified Instances       438               49.1031 %
Kappa statistic                          0.2635
Mean absolute error                      0.3457
Root mean squared error                  0.4616
Relative absolute error                 77.7914 %
Root relative squared error             97.9278 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.650    0.249    0.566      0.650    0.605      0.389    0.786     0.624     alto
                 0.550    0.214    0.564      0.550    0.557      0.339    0.744     0.591     bajo
                 0.327    0.274    0.373      0.327    0.348      0.055    0.585     0.407     medio
Weighted Avg.    0.509    0.245    0.501      0.509    0.503      0.261    0.705     0.541     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 193  28  76 |   a = alto
  47 164  87 |   b = bajo
 101  99  97 |   c = medio

````

## RESPALDO_UNIFICADO.zip

Ruta: `Final/reports/weka/RESPALDO_UNIFICADO.zip` · Bytes: 11472033 · SHA-256: `82a3b7217c62eff0fdf74c070608479239659bc0af71e8546d47c91d77d70b03`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## RandomForest.png

Ruta: `Final/reports/weka/RandomForest.png` · Bytes: 675186 · SHA-256: `75fd874d38afb1b00f10cf700ec2a5adede66120ac7d87f702d4d0c7a6367d8c`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## RandomForest.txt

Ruta: `Final/reports/weka/RandomForest.txt` · Bytes: 3521 · SHA-256: `bed5274c54f92bc20ff70c7d64d600839b65e76ea4860e88d8e003dcd5bb47df`

````text
=== Run information ===

Scheme:       weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

RandomForest

Bagging with 100 iterations and base learner

weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

Time taken to build model: 0.2 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         477               53.4753 %
Incorrectly Classified Instances       415               46.5247 %
Kappa statistic                          0.3021
Mean absolute error                      0.3619
Root mean squared error                  0.4355
Relative absolute error                 81.4156 %
Root relative squared error             92.3813 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.657    0.215    0.604      0.657    0.629      0.433    0.816     0.679     alto
                 0.587    0.219    0.574      0.587    0.580      0.366    0.769     0.613     bajo
                 0.360    0.264    0.405      0.360    0.381      0.100    0.596     0.402     medio
Weighted Avg.    0.535    0.233    0.528      0.535    0.530      0.300    0.727     0.565     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 195  29  73 |   a = alto
  39 175  84 |   b = bajo
  89 101 107 |   c = medio

````

## ZeroR.png

Ruta: `Final/reports/weka/ZeroR.png` · Bytes: 597808 · SHA-256: `b7859929328baea3540730ab9e0494eec18e983a56f8fb5d1c26ddb77f91766f`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## ZeroR.txt

Ruta: `Final/reports/weka/ZeroR.txt` · Bytes: 3346 · SHA-256: `abc7807ce09733680834ddcfcbf72f7a71f72e62ad1d519db547385bc4fe1cad`

````text
=== Run information ===

Scheme:       weka.classifiers.rules.ZeroR 
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

ZeroR predicts class value: bajo

Time taken to build model: 0 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         295               33.0717 %
Incorrectly Classified Instances       597               66.9283 %
Kappa statistic                         -0.0045
Mean absolute error                      0.4444
Root mean squared error                  0.4714
Relative absolute error                100      %
Root relative squared error            100      %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.293    0.303    0.326      0.293    0.309      -0.010   0.494     0.330     alto
                 0.698    0.702    0.333      0.698    0.451      -0.004   0.495     0.332     bajo
                 0.000    0.000    ?          0.000    ?          ?        0.494     0.330     medio
Weighted Avg.    0.331    0.335    ?          0.331    ?          ?        0.495     0.331     

=== Confusion Matrix ===

   a   b   c   <-- classified as
  87 210   0 |   a = alto
  90 208   0 |   b = bajo
  90 207   0 |   c = medio

````

## auditoria_cierre_2026_11_09.json

Ruta: `Final/reports/weka/auditoria_cierre_2026_11_09.json` · Bytes: 1641 · SHA-256: `e40d7fd52f04c7f67a654c8f0cfe301d0e34bfedba7b8de7ddf424c99e539549`

````text
{
  "estado": "Sin pendientes en los entregables solicitados de Weka",
  "clases": {
    "alto": 297,
    "medio": 297,
    "bajo": 298
  },
  "comprobaciones": [
    {
      "elemento": "clustering",
      "filas": 887,
      "columnas": 6,
      "CSV_ARFF_identicos": true
    },
    {
      "elemento": "clasificacion",
      "filas": 892,
      "columnas": 53,
      "CSV_ARFF_identicos": true
    },
    {
      "elemento": "ZeroR",
      "salida_completa": true,
      "matriz_verificada": true,
      "comparativo_exacto": true,
      "captura_valida": true
    },
    {
      "elemento": "NaiveBayes",
      "salida_completa": true,
      "matriz_verificada": true,
      "comparativo_exacto": true,
      "captura_valida": true
    },
    {
      "elemento": "J48",
      "salida_completa": true,
      "matriz_verificada": true,
      "comparativo_exacto": true,
      "captura_valida": true
    },
    {
      "elemento": "RandomForest",
      "salida_completa": true,
      "matriz_verificada": true,
      "comparativo_exacto": true,
      "captura_valida": true
    },
    {
      "elemento": "SimpleKMeans",
      "k": 2,
      "semilla": 42,
      "centroides_seis_variables": true,
      "tamanos": [
        477,
        410
      ]
    },
    {
      "elemento": "DBSCAN",
      "epsilon": 1.666296,
      "minPoints": 12,
      "asignaciones": 887,
      "etiquetas": {
        "0": 887
      }
    }
  ],
  "nota": "Se verificaron las corridas guardadas; esta revisión no ejecutó nuevos entrenamientos. Explorer quedó abierto con clasificacion.arff, 892 instancias, 53 atributos y clase nominal nivel_popularidad."
}

````

## ayuda_simplekmeans.txt

Ruta: `Final/reports/weka/ayuda_simplekmeans.txt` · Bytes: 3011 · SHA-256: `58ad204090c1a112e8c658001e8d33bc5f2dbefd7501bcd7d66500ebf42d2ccc`

````text
Help requested.

General options:

-h or -help
	Output help information.
-synopsis or -info
	Output synopsis for clusterer (use in conjunction  with -h)
-t <name of training file>
	Sets training file.
-T <name of test file>
	Sets test file.
-force-batch-training
	Always train the clusterer in batch mode, never incrementally.
-l <name of input file>
	Sets model input file.
-d <name of output file>
	Sets model output file.
-p <attribute range>
	Output predictions. Predictions are for training file
	if only training file is specified,
	otherwise predictions are for the test file.
	The range specifies attribute values to be output
	with the predictions. Use '-p 0' for none.
-x <number of folds>
	Only Distribution Clusterers can be cross validated.
-s <random number seed>
	Sets the seed for randomizing the data in cross-validation
-c <class index>
	Set class attribute. If supplied, class is ignored
	during clustering but is used in a classes to
	clusters evaluation.

Options specific to weka.clusterers.SimpleKMeans:

-N <num>
	Number of clusters.
	(default 2).
-init
	Initialization method to use.
	0 = random, 1 = k-means++, 2 = canopy, 3 = farthest first.
	(default = 0)
-C
	Use canopies to reduce the number of distance calculations.
-max-candidates <num>
	Maximum number of candidate canopies to retain in memory
	at any one time when using canopy clustering.
	T2 distance plus, data characteristics,
	will determine how many candidate canopies are formed before
	periodic and final pruning are performed, which might result
	in exceess memory consumption. This setting avoids large numbers
	of candidate canopies consuming memory. (default = 100)
-periodic-pruning <num>
	How often to prune low density canopies when using canopy clustering. 
	(default = every 10,000 training instances)
-min-density
	Minimum canopy density, when using canopy clustering, below which
	 a canopy will be pruned during periodic pruning. (default = 2 instances)
-t2
	The T2 distance to use when using canopy clustering. Values < 0 indicate that
	a heuristic based on attribute std. deviation should be used to set this.
	(default = -1.0)
-t1
	The T1 distance to use when using canopy clustering. A value < 0 is taken as a
	positive multiplier for T2. (default = -1.5)
-V
	Display std. deviations for centroids.

-M
	Don't replace missing values with mean/mode.

-A <classname and options>
	Distance function to use.
	(default: weka.core.EuclideanDistance)
-I <num>
	Maximum number of iterations.

-O
	Preserve order of instances.

-fast
	Enables faster distance calculations, using cut-off values.
	Disables the calculation/output of squared errors/distances.

-num-slots <num>
	Number of execution slots.
	(default 1 - i.e. no parallelism)
-S <num>
	Random number seed.
	(default 10)
-output-debug-info
	If set, clusterer is run in debug mode and
	may output additional info to the console
-do-not-check-capabilities
	If set, clusterer capabilities are not checked before clusterer is built
	(use with caution).


````

## bloqueo_selector_reanudacion.png

Ruta: `Final/reports/weka/bloqueo_selector_reanudacion.png` · Bytes: 131964 · SHA-256: `85965f2266409001768b0c002be1b480c60b9602795d2c180e67987ca9d60215`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clic_weka.js

Ruta: `Final/reports/weka/clic_weka.js` · Bytes: 1778 · SHA-256: `a18f25837076eaf480e513a9f0f678a35b2eaf9805b14458b690ba6f430755e1`

````text
// Control gráfico local de Weka; autorizado expresamente por el usuario.
ObjC.import('ApplicationServices');
function run(argumentos) {
    if (argumentos.length < 2 || argumentos.length > 3) throw new Error('Indica x, y y opcionalmente la ventana de Weka.');
    var nombreVentana = argumentos.length === 3 ? argumentos[2] : 'Weka Explorer';
    var permitidas = ['Weka Explorer', 'Package Manager', 'Weka Package Manager', 'weka.gui.GenericObjectEditor', 'Weka GUI Chooser', 'Abrir'];
    if (permitidas.indexOf(nombreVentana) < 0) throw new Error('Ventana fuera del alcance autorizado de Weka.');
    var x = Number(argumentos[0]);
    var y = Number(argumentos[1]);
    var sistema = Application('System Events');
    var proceso = sistema.processes.byName('weka-3.8.7');
    var ventana = proceso.windows.byName(nombreVentana);
    var posicion = ventana.position();
    var tamano = ventana.size();
    if (!Number.isFinite(x) || !Number.isFinite(y) ||
        x < posicion[0] || x >= posicion[0] + tamano[0] ||
        y < posicion[1] || y >= posicion[1] + tamano[1]) {
        throw new Error('El clic debe quedar dentro de la ventana autorizada de Weka.');
    }
    proceso.frontmost = true;
    delay(0.3);
    var punto = $.CGPointMake(x, y);
    var pulsar = $.CGEventCreateMouseEvent(null, $.kCGEventLeftMouseDown, punto, $.kCGMouseButtonLeft);
    var soltar = $.CGEventCreateMouseEvent(null, $.kCGEventLeftMouseUp, punto, $.kCGMouseButtonLeft);
    $.CGEventSetIntegerValueField(pulsar, $.kCGMouseEventClickState, 1);
    $.CGEventSetIntegerValueField(soltar, $.kCGMouseEventClickState, 1);
    $.CGEventPost($.kCGHIDEventTap, pulsar);
    $.CGEventPost($.kCGHIDEventTap, soltar);
    return 'Clic gráfico enviado dentro de la ventana autorizada de Weka.';
}

````

## comparacion.csv

Ruta: `Final/reports/weka/comparacion.csv` · Bytes: 704 · SHA-256: `70d69fdb4c4945ab54fec101100c11700af1d04db90b09376b26cef6dfa956a1`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## conversion_capturas.json

Ruta: `Final/reports/weka/conversion_capturas.json` · Bytes: 5286 · SHA-256: `faa3a6f86b515d59e45a1f383580bf405eeeff13f3a68d45da111685d9d0b7bd`

````text
{
  "motivo": "La herramienta entregó JPEG bajo nombres .png; se conservaron los originales y se corrigió únicamente la codificación, sin alterar los píxeles.",
  "capturas": [
    {
      "png": "reports/weka/kmeans_resultado.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/kmeans_resultado.jpg",
      "sha256_jpeg_original": "0b8e0b0cbf449189b3e9e1003676ad081605321116834da5ee59b1346ff32af2",
      "sha256_png": "a6f5223cb9b6f6d0cbeb70cc3da84f89396cd8fc68fa2195d4e8f7fc63548e00",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/dbscan_resultado.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/dbscan_resultado.jpg",
      "sha256_jpeg_original": "764cab40e6644b9f38d3db5e999cb46efa59847754796ab7af598f7e61c55839",
      "sha256_png": "a5b1fd50d6f42054ceff60a26a5528d8813b86d1efebff71e5d0053d85f30ee2",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/ZeroR.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/ZeroR.jpg",
      "sha256_jpeg_original": "5bf5855dbbfabc490600a2b84b17daad9634618f25b6e7bc3d9379bb1ec6b322",
      "sha256_png": "b7859929328baea3540730ab9e0494eec18e983a56f8fb5d1c26ddb77f91766f",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/NaiveBayes.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/NaiveBayes.jpg",
      "sha256_jpeg_original": "3183edf0097177d334337adae81965d64b6745681817a9130eee0e2a26c3db6f",
      "sha256_png": "ef00fe5af3442fbbaa129aeef2a23c3c42e642d69773f6924fd261ada6056928",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/J48.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/J48.jpg",
      "sha256_jpeg_original": "2cf229718717fc3574bc2af3c45de908c0ddfc74a4273c560ebfdff745fbefa2",
      "sha256_png": "72296d14f03af1520c8e07ca86310cb171b5a1b7f46b189701f3df514e184afd",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/RandomForest.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/RandomForest.jpg",
      "sha256_jpeg_original": "17df8a4eb2e4bfc4b3fa628b4a94265ce9c36fd8c7d0922c4b938ea201bc86e6",
      "sha256_png": "75fd874d38afb1b00f10cf700ec2a5adede66120ac7d87f702d4d0c7a6367d8c",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/kmeans_parametros.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/kmeans_parametros.jpg",
      "sha256_jpeg_original": "2ff878e825f3e6fcb0055d9a40a69d57016a8074007afb72febc748b07414dfd",
      "sha256_png": "02701adf007ea00754e5a08b072612409728475c99ad457ce314f52f1bd78f27",
      "dimensiones": [
        982,
        1584
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/dbscan_parametros.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/dbscan_parametros.jpg",
      "sha256_jpeg_original": "078094306545235ed1c67e4468cee9bad306737338cc4ebeb5d38395cfb61451",
      "sha256_png": "0893afea5b536cf905d0d8d1d2a212e68370679a22cc5ab5d25d1d83b5ccaa3e",
      "dimensiones": [
        982,
        726
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/dbscan_paquete_instalado.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/dbscan_paquete_instalado.jpg",
      "sha256_jpeg_original": "1555840562cc1419d058e30801225e554784bb42e370f0ff4dfa58a7d34d74e4",
      "sha256_png": "d116101ee2b08af4959b56657aceebbc52e1708afbe6c2cfef50ec082b55761f",
      "dimensiones": [
        2736,
        1778
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/preprocess_887_6.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/preprocess_887_6.jpg",
      "sha256_jpeg_original": "ddd1c3c24514a7ceca94436e617187d1a0612c22544d6c8df476dae5ad46df25",
      "sha256_png": "4a12b27fee62542fd9e54b8a1a0f0860013d9a9b9d17eadb01afc3cf06c17e9e",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/preprocess_clasificacion_892_53.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/preprocess_clasificacion_892_53.jpg",
      "sha256_jpeg_original": "777b212a752b5a8e951352cf07a10fac9983ad477db5b92a6033994a7e60da47",
      "sha256_png": "3528c55e62a3c2c4756a4c20a396350944a355ef5094a225e4023b394bf2da93",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    },
    {
      "png": "reports/weka/verificacion_final_ventana.png",
      "jpeg_original": "reports/weka/capturas_originales_jpeg/verificacion_final_ventana.jpg",
      "sha256_jpeg_original": "521b7bdc5119b1c28295646d2e41cb7b242b0d994ce3a2e7fec17a7da82da6f0",
      "sha256_png": "db55f2c6708c8697f387317f5753d787c2132ebcf87b75c995378729edd6cde4",
      "dimensiones": [
        2048,
        1536
      ],
      "pixeles_identicos": true
    }
  ]
}

````

## dbscan.txt

Ruta: `Final/reports/weka/dbscan.txt` · Bytes: 76228 · SHA-256: `7d0866476ee480a90daee39e1469861c532b52da9dbef7bfb9c05eedcf11de94`

````text
=== Run information ===

Scheme:       weka.clusterers.DBSCAN -E 1.666296 -M 12 -A "weka.core.EuclideanDistance -R first-last"
Relation:     clustering
Instances:    887
Attributes:   6
              Plays
              Playing
              Backlogs
              Wishlist
              Rating
              Metacritic Rating
Test mode:    evaluate on training data


=== Clustering model (full training set) ===

DBSCAN clustering results
========================================================================================

Clustered DataObjects: 887
Number of attributes: 6
Epsilon: 1.666296; minPoints: 12
Distance-type: 
Number of generated clusters: 1
Elapsed time: .05

(  0.) 1.453174,2.79742,1.684415,2.272893,1.624324,1.673091                   -->  0
(  1.) 1.642703,2.667802,1.995272,2.007855,1.239142,1.305726                  -->  0
(  2.) 1.96262,2.48162,1.766831,1.708074,1.431733,1.795546                    -->  0
(  3.) 1.900737,1.499038,1.746862,1.369369,1.04655,1.183271                   -->  0
(  4.) 1.642703,2.450834,2.267802,1.595141,1.431733,0.570996                  -->  0
(  5.) 2.048109,2.233892,0.270636,-0.523116,1.239142,1.305726                 -->  0
(  6.) 0.682622,1.862601,1.662691,2.057665,1.04655,0.693451                   -->  0
(  7.) 0.902465,1.582954,1.385651,1.927696,1.239142,0.693451                  -->  0
(  8.) 1.799088,1.221971,-0.073931,-1.074392,-1.264545,0.326086               -->  0
(  9.) 1.504441,1.862601,1.979456,2.007855,1.239142,0.693451                  -->  0
( 10.) 1.140772,2.418738,1.786404,1.839895,1.431733,1.550636                  -->  0
( 11.) 0.742837,1.623537,1.08177,1.955198,0.083594,0.081176                   -->  0
( 12.) 1.642703,1.862601,1.726482,1.708074,1.04655,1.428181                   -->  0
( 13.) 1.932212,1.223571,1.521253,0.995985,1.431733,1.550636                  -->  0
( 14.) 1.453174,1.862601,1.878849,1.927696,1.624324,1.183271                  -->  0
( 15.) 1.598942,1.928191,1.930431,1.466409,1.04655,1.183271                   -->  0
( 16.) 1.552935,2.190792,1.861038,1.808665,1.431733,1.795546                  -->  0
( 17.) 1.900737,0.728852,1.157826,0.915873,0.853959,0.938361                  -->  0
( 18.) 1.799088,1.532671,1.228446,1.466409,1.04655,1.795546                   -->  0
( 19.) 0.892663,2.145081,1.08177,1.511347,0.083594,0.081176                   -->  0
( 20.) -0.10248,1.682333,0.577022,1.466409,1.239142,0.570996                  -->  0
( 21.) 1.279031,1.256413,1.594499,1.466409,0.853959,-0.286188                 -->  0
( 22.) 1.96262,1.649428,1.325734,0.45126,0.276185,1.795546                    -->  0
( 23.) 1.212563,2.09642,1.705672,1.808665,-0.686771,0.448541                  -->  0
( 24.) 0.407856,1.623537,0.861265,1.927696,1.431733,1.428181                  -->  0
( 25.) 0.132786,1.617871,0.909476,1.554196,1.431733,0.815906                  -->  0
( 26.) 0.504036,1.756058,1.08177,1.870101,1.04655,0.326086                    -->  0
( 27.) 0.519109,1.928191,1.766831,1.742838,1.816916,0.815906                  -->  0
( 28.) 1.642703,1.376422,1.228446,1.554196,0.853959,0.570996                  -->  0
( 29.) 1.552935,1.669165,1.617757,1.554196,1.04655,0.815906                   -->  0
( 30.) 0.618073,1.694418,1.570682,2.033096,1.04655,0.081176                   -->  0
( 31.) 1.642703,1.210674,1.08177,0.593509,0.853959,1.428181                   -->  0
( 32.) 1.799088,1.928191,0.270636,0.623878,0.853959,1.305726                  -->  0
( 33.) 1.504441,1.928191,1.662691,1.708074,0.853959,0.448541                  -->  0
( 34.) 1.279031,1.727099,1.726482,1.955198,1.431733,0.938361                  -->  0
( 35.) 1.340912,1.862601,1.766831,1.20146,1.04655,1.183271                    -->  0
( 36.) 1.212563,2.09642,1.805598,1.554196,1.04655,1.305726                    -->  0
( 37.) 1.279031,2.539662,0.435651,-0.342559,-2.034911,-0.163733               -->  0
( 38.) -0.380573,1.135507,0.810581,1.554196,1.04655,-0.163733                 -->  0
( 39.) 0.968235,0.962648,1.193767,1.776339,0.468776,0.203631                  -->  0
( 40.) 1.642703,1.218761,1.294357,0.995985,1.239142,1.795546                  -->  0
( 41.) 1.398798,1.57997,1.766831,1.137927,1.239142,0.203631                   -->  0
( 42.) 0.742837,1.478797,1.726482,1.870101,1.816916,0.326086                  -->  0
( 43.) 1.340912,1.386793,1.442142,1.419166,1.239142,1.060816                  -->  0
( 44.) 1.504441,1.327904,1.546276,1.137927,0.661368,0.326086                  -->  0
( 45.) 0.177633,1.790761,1.385651,1.708074,0.276185,0.203631                  -->  0
( 46.) 1.212563,1.423236,1.766831,1.595141,0.468776,0.938361                  -->  0
( 47.) 1.598942,2.313341,1.442142,0.915873,0.853959,0.815906                  -->  0
( 48.) 1.212563,1.225168,1.193767,1.671945,0.853959,1.305726                  -->  0
( 49.) 0.841978,0.837637,1.228446,1.511347,1.624324,0.815906                  -->  0
( 50.) 1.453174,1.928191,1.963383,1.260895,1.239142,1.183271                  -->  0
( 51.) 1.398798,1.442613,1.193767,1.316727,0.853959,1.305726                  -->  0
( 52.) 1.140772,1.561813,1.684415,1.634343,1.04655,0.693451                   -->  0
( 53.) 1.684429,1.391926,1.261951,0.828127,0.083594,1.673091                  -->  0
( 54.) -0.132878,1.296641,0.757159,1.595141,0.853959,0.815906                 -->  0
( 55.) 1.140772,1.303861,1.570682,1.634343,1.239142,0.570996                  -->  0
( 56.) 0.604586,1.862601,-1.038099,-0.794891,-1.842319,-0.776008              -->  0
( 57.) 1.279031,1.021298,1.261951,0.995985,1.239142,1.673091                  -->  0
( 58.) 1.140772,1.709677,1.594499,1.554196,0.853959,0.570996                  -->  0
( 59.) -0.132878,1.254881,0.435651,1.369369,-0.108998,-1.510738               -->  0
( 60.) 0.424619,1.349854,0.999372,1.595141,0.853959,0.326086                  -->  0
( 61.) 0.009754,1.251808,1.041429,1.708074,0.468776,0.326086                  -->  0
( 62.) 1.279031,1.184199,1.08177,1.137927,1.239142,0.815906                   -->  0
( 63.) 1.453174,1.160245,1.261951,1.137927,1.239142,2.040456                  -->  0
( 64.) 0.977249,0.416757,1.120529,1.137927,1.431733,1.673091                  -->  0
( 65.) 0.921753,1.7393,1.726482,1.634343,0.468776,-0.041278                   -->  0
( 66.) 0.968235,1.045969,1.193767,1.776339,0.468776,0.326086                  -->  0
( 67.) 1.062732,1.609292,1.120529,1.260895,1.239142,0.203631                  -->  0
( 68.) 0.892663,0.923235,1.385651,1.316727,1.431733,1.305726                  -->  0
( 69.) 1.212563,0.993627,1.521253,1.369369,1.431733,1.550636                  -->  0
( 70.) 1.212563,1.563852,1.469222,1.069686,0.083594,-0.408643                 -->  0
( 71.) 1.453174,0.59804,0.861265,1.137927,1.04655,1.550636                    -->  0
( 72.) 1.504441,1.492351,0.955446,0.347214,0.661368,0.081176                  -->  0
( 73.) 1.212563,0.946668,1.294357,1.069686,0.468776,0.448541                  -->  0
( 74.) 1.279031,1.273062,1.662691,0.995985,0.276185,1.305726                  -->  0
( 75.) 1.552935,1.165443,-0.701128,-0.589262,-0.879363,1.060816               -->  0
( 76.) 1.340912,0.767859,1.4143,0.828127,1.04655,1.673091                     -->  0
( 77.) 1.140772,1.862601,1.4143,1.20146,0.661368,0.815906                     -->  0
( 78.) 1.552935,0.804948,1.041429,0.553463,0.853959,1.550636                  -->  0
( 79.) 0.085578,1.215536,1.356146,1.671945,1.431733,0.326086                  -->  0
( 80.) 0.820874,1.385505,1.228446,1.20146,0.853959,0.815906                   -->  0
( 81.) 0.977249,0.848226,1.08177,0.915873,-0.301589,1.428181                  -->  0
( 82.) 1.552935,1.527347,-0.06759,0.410171,0.661368,1.183271                  -->  0
( 83.) -0.666067,1.689262,0.103768,0.915873,0.468776,-0.286188                -->  0
( 84.) 0.009754,1.684071,-0.111535,0.563332,-0.301589,-1.388283               -->  0
( 85.) 1.279031,0.640758,1.041429,0.75934,0.661368,0.326086                   -->  0
( 86.) -0.923924,0.944357,-0.072659,1.069686,1.624324,0.815906                -->  0
( 87.) 0.220345,0.920851,1.193767,1.595141,1.04655,0.570996                   -->  0
( 88.) -1.001904,1.397023,0.270636,1.137927,1.624324,1.428181                 -->  0
( 89.) 0.576989,1.445001,0.640785,0.789588,-0.686771,0.570996                 -->  0
( 90.) 1.453174,0.690962,0.999372,0.462279,0.468776,1.183271                  -->  0
( 91.) 1.279031,1.106203,1.356146,0.828127,0.083594,1.183271                  -->  0
( 92.) 0.707195,1.667392,1.442142,1.419166,1.239142,0.815906                  -->  0
( 93.) 1.212563,0.937382,1.228446,0.72292,0.661368,1.673091                   -->  0
( 94.) 0.373359,1.158505,0.909476,1.069686,0.276185,-0.286188                 -->  0
( 95.) -0.164344,1.334832,0.640785,1.511347,-0.108998,-0.041278               -->  0
( 96.) 1.140772,1.098696,1.4143,0.60648,0.661368,0.448541                     -->  0
( 97.) 1.212563,1.510052,1.546276,1.137927,-0.108998,0.815906                 -->  0
( 98.) 1.552935,0.829597,0.577022,-0.116818,0.468776,0.815906                 -->  0
( 99.) 1.212563,1.928191,-0.935626,-1.879694,-2.997867,-0.531098              -->  0
(100.) 0.940636,1.394479,1.805598,1.069686,-0.108998,-0.041278                -->  0
(101.) 1.279031,0.262247,0.577022,0.113629,-0.686771,-0.531098                -->  0
(102.) 1.398798,0.54886,1.157826,0.433067,0.853959,1.428181                   -->  0
(103.) 0.94993,1.170604,1.385651,0.828127,0.083594,-0.286188                  -->  0
(104.) 1.140772,1.133708,0.810581,0.828127,0.853959,-0.163733                 -->  0
(105.) 1.398798,1.27605,-0.44656,-0.867313,0.468776,1.183271                  -->  0
(106.) 0.707195,1.194236,1.157826,1.20146,0.468776,0.081176                   -->  0
(107.) 0.912161,0.53704,0.909476,1.20146,0.853959,0.081176                    -->  0
(108.) 1.340912,0.61255,0.909476,0.642081,-0.49418,0.326086                   -->  0
(109.) 1.062732,1.177432,1.157826,0.822587,-0.301589,0.570996                 -->  0
(110.) 0.199243,1.079595,1.041429,1.419166,-0.301589,0.693451                 -->  0
(111.) 0.977249,0.279202,1.228446,1.316727,1.431733,1.060816                  -->  0
(112.) 0.035747,0.67128,0.04463,0.655502,0.276185,0.203631                    -->  0
(113.) -0.196953,0.840298,0.700683,1.595141,0.276185,-0.163733                -->  0
(114.) 1.279031,0.799359,1.294357,0.695692,0.468776,0.693451                  -->  0
(115.) 0.902465,0.184025,1.041429,1.069686,1.624324,1.060816                  -->  0
(116.) 1.140772,0.014084,1.157826,1.316727,0.468776,1.183271                  -->  0
(117.) 1.140772,0.793728,0.909476,0.828127,-0.108998,0.326086                 -->  0
(118.) 1.140772,0.426015,0.909476,0.440107,0.853959,0.815906                  -->  0
(119.) -1.001904,0.700615,0.700683,1.419166,0.853959,-0.163733                -->  0
(120.) 1.140772,0.770777,0.757159,0.475871,1.239142,1.550636                  -->  0
(121.) 1.453174,1.35926,-0.178517,-1.173904,-0.49418,0.326086                 -->  0
(122.) 1.212563,0.829597,1.385651,0.571882,0.083594,0.570996                  -->  0
(123.) -0.666067,0.700615,0.640785,1.554196,0.083594,0.448541                 -->  0
(124.) 0.15549,1.234678,1.193767,1.419166,1.816916,1.060816                   -->  0
(125.) 1.504441,-0.638529,-0.947869,-1.351667,0.083594,-0.776008              -->  0
(126.) -0.785761,1.589871,-0.195636,1.260895,-0.301589,0.203631               -->  0
(127.) 1.552935,-0.035138,-0.58789,-0.811106,0.468776,-0.041278               -->  0
(128.) 0.820874,0.397895,1.041429,1.260895,-0.879363,-0.408643                -->  0
(129.) 0.337482,0.637289,0.172542,1.069686,-0.108998,0.081176                 -->  0
(130.) 1.212563,0.644211,1.041429,1.260895,1.04655,1.550636                   -->  0
(131.) -0.073078,1.36855,0.999372,1.419166,-0.108998,0.570996                 -->  0
(132.) -0.852185,0.74107,0.161574,1.419166,1.239142,0.815906                  -->  0
(133.) 1.340912,0.479293,1.157826,0.204904,-0.301589,0.448541                 -->  0
(134.) 1.212563,0.215077,1.08177,1.069686,1.239142,1.918001                   -->  0
(135.) 0.841978,-0.30788,0.955446,1.069686,0.661368,0.693451                  -->  0
(136.) 0.473108,1.862601,0.757159,1.069686,0.661368,0.693451                  -->  0
(137.) 1.398798,0.647648,0.176501,-0.071736,0.661368,-0.776008                -->  0
(138.) -0.265958,1.015002,1.041429,1.466409,1.04655,-0.286188                 -->  0
(139.) 1.398798,0.31201,0.577022,0.228144,0.276185,0.938361                   -->  0
(140.) -0.230792,1.380328,-0.529719,0.182919,-0.301589,-1.265828              -->  0
(141.) 0.940636,0.889157,1.157826,0.915873,0.661368,0.815906                  -->  0
(142.) 1.398798,0.117801,-0.01467,-0.319884,-0.301589,0.815906                -->  0
(143.) 0.754409,0.722667,1.325734,1.260895,0.853959,1.060816                  -->  0
(144.) -0.196953,1.355243,0.909476,1.595141,0.276185,0.693451                 -->  0
(145.) 1.062732,0.402655,0.577022,0.727039,-0.108998,1.428181                 -->  0
(146.) 1.062732,0.637289,0.955446,1.069686,-0.301589,-0.531098                -->  0
(147.) 1.062732,1.050004,1.325734,0.915873,-0.686771,-0.163733                -->  0
(148.) 0.373359,1.602551,1.442142,1.260895,0.083594,0.081176                  -->  0
(149.) 1.212563,0.250728,0.955446,0.68069,-0.301589,0.938361                  -->  0
(150.) 1.279031,0.759034,0.435651,0.115625,0.853959,0.081176                  -->  0
(151.) -0.666067,0.500428,0.435651,1.137927,-0.108998,-1.265828               -->  0
(152.) -0.164344,0.706981,1.08177,1.069686,1.239142,-1.020918                 -->  0
(153.) 1.279031,0.770777,0.810581,0.527043,0.276185,1.918001                  -->  0
(154.) 0.719234,0.353646,0.577022,0.499842,0.661368,0.815906                  -->  0
(155.) 0.831488,0.955841,1.228446,0.818875,0.853959,1.183271                  -->  0
(156.) 0.63136,1.000104,1.442142,0.995985,1.239142,1.428181                   -->  0
(157.) 1.140772,0.067723,0.577022,0.24042,1.04655,1.428181                    -->  0
(158.) 0.765835,0.34345,0.861265,0.621577,0.661368,1.183271                   -->  0
(159.) 0.424619,1.220368,1.193767,1.20146,0.853959,-0.653553                  -->  0
(160.) 0.902465,1.560792,1.193767,1.137927,0.276185,0.815906                  -->  0
(161.) 1.279031,0.533059,0.810581,0.4457,0.083594,0.693451                    -->  0
(162.) -0.044609,0.317342,0.270636,1.069686,0.853959,0.938361                 -->  0
(163.) 1.140772,0.021984,0.700683,0.669823,0.083594,-0.041278                 -->  0
(164.) 1.279031,0.177658,-0.521681,-1.466352,0.083594,0.570996                -->  0
(165.) 0.765835,0.776581,1.228446,1.137927,0.468776,0.693451                  -->  0
(166.) 0.177633,1.106203,1.041429,1.511347,0.468776,1.183271                  -->  0
(167.) 0.424619,0.586972,1.120529,0.828127,0.083594,-0.163733                 -->  0
(168.) 0.731113,1.075716,1.193767,1.466409,0.468776,0.570996                  -->  0
(169.) 1.212563,0.184025,0.356582,0.182919,-1.457137,-0.163733                -->  0
(170.) -0.073078,1.017106,0.999372,1.260895,0.853959,-0.286188                -->  0
(171.) 1.279031,-0.549665,-0.309922,-0.225678,0.083594,0.570996               -->  0
(172.) 0.085578,0.644211,0.577022,1.316727,0.661368,0.693451                  -->  0
(173.) 1.140772,0.525033,0.270636,0.115625,0.661368,0.570996                  -->  0
(174.) 0.977249,-0.516857,0.435651,0.659932,0.276185,0.693451                 -->  0
(175.) -0.723919,0.30664,-0.001576,0.635297,0.468776,0.326086                 -->  0
(176.) 0.061009,0.358693,0.757159,0.995985,1.431733,0.081176                  -->  0
(177.) 0.300111,1.571954,1.294357,0.995985,1.04655,1.060816                   -->  0
(178.) 0.618073,0.529056,1.228446,1.20146,1.431733,0.570996                   -->  0
(179.) 0.912161,-0.026708,0.435651,0.482593,0.661368,1.305726                 -->  0
(180.) 0.940636,0.110847,0.810581,0.424547,1.239142,1.673091                  -->  0
(181.) 0.280824,1.391926,-0.158912,0.348764,0.276185,1.183271                 -->  0
(182.) 0.931244,-0.41211,0.700683,0.276294,-0.686771,-0.898463                -->  0
(183.) -0.666067,0.124691,0.577022,1.137927,0.468776,-0.898463                -->  0
(184.) 0.707195,0.59804,0.909476,0.581557,0.661368,1.183271                   -->  0
(185.) 0.473108,-0.087797,-0.837261,-0.450277,0.661368,0.081176               -->  0
(186.) 1.212563,-0.358196,-0.285984,-0.323089,0.276185,0.081176               -->  0
(187.) 0.085578,1.17913,0.999372,1.069686,0.276185,-0.163733                  -->  0
(188.) 0.682622,0.967152,1.228446,0.775076,0.276185,0.570996                  -->  0
(189.) -0.30256,1.155012,0.757159,1.260895,0.661368,0.448541                  -->  0
(190.) 1.212563,-0.061008,-0.181349,-0.480248,-0.301589,0.570996              -->  0
(191.) -0.923924,0.262247,0.089851,0.627319,0.853959,-0.041278                -->  0
(192.) 0.820874,0.358693,0.955446,0.528318,-0.108998,-0.408643                -->  0
(193.) 0.109493,0.53704,1.157826,0.788628,1.431733,0.938361                   -->  0
(194.) 0.892663,0.082373,1.356146,0.487935,-0.108998,0.693451                 -->  0
(195.) -1.34506,0.677898,0.106952,0.915873,-1.071954,-1.020918                -->  0
(196.) 0.872731,1.106203,1.041429,0.074844,-0.108998,-0.041278                -->  0
(197.) 0.831488,0.28477,0.810581,0.995985,0.661368,0.326086                   -->  0
(198.) 0.754409,0.052783,0.640785,0.995985,0.083594,-0.163733                 -->  0
(199.) 0.618073,0.244902,0.508861,0.661036,-0.686771,1.060816                 -->  0
(200.) 0.199243,1.098696,1.120529,0.828127,0.083594,-0.653553                 -->  0
(201.) -0.923924,0.021984,-0.349472,0.301089,0.468776,0.570996                -->  0
(202.) 0.754409,0.53704,0.757159,0.281306,-2.227502,-1.878103                 -->  0
(203.) 0.533933,0.171237,0.640785,0.428817,1.04655,0.203631                   -->  0
(204.) -0.785761,0.262247,-0.207216,0.915873,1.431733,0.815906                -->  0
(205.) 0.977249,0.378548,0.757159,0.192143,-0.301589,0.938361                 -->  0
(206.) -0.164344,1.400824,1.041429,0.761322,1.624324,0.570996                 -->  0
(207.) 0.94993,0.886663,0.098438,0.190306,-1.457137,-0.286188                 -->  0
(208.) 0.742837,1.029612,1.120529,0.815148,0.276185,-0.286188                 -->  0
(209.) 0.799262,1.466156,-1.041479,-1.198479,-2.227502,-0.286188              -->  0
(210.) 0.940636,0.0061,-0.060033,0.055887,0.468776,1.305726                   -->  0
(211.) 1.062732,-0.320148,0.577022,0.146999,-0.108998,1.183271                -->  0
(212.) 0.604586,0.466322,0.640785,0.392618,1.431733,-0.163733                 -->  0
(213.) 0.562865,0.075084,0.577022,0.553463,0.468776,0.815906                  -->  0
(214.) 0.820874,-0.516857,-0.745292,-0.822076,-1.457137,-0.531098             -->  0
(215.) 0.882752,0.164761,-0.168665,-0.37595,0.853959,0.570996                 -->  0
(216.) 0.719234,-0.018372,0.508861,-0.012568,-0.686771,-0.286188              -->  0
(217.) -0.017016,0.722667,0.577022,0.995985,0.853959,0.570996                 -->  0
(218.) -0.852185,0.43516,0.508861,0.915873,-0.301589,-0.776008                -->  0
(219.) 1.062732,-1.240976,-1.231251,-1.198479,-0.301589,1.183271              -->  0
(220.) 0.109493,-0.144409,0.176501,0.748364,-0.108998,-1.020918               -->  0
(221.) -0.852185,1.06593,0.577022,0.505086,1.04655,0.326086                   -->  0
(222.) 0.473108,0.402655,0.176501,0.356476,0.661368,0.938361                  -->  0
(223.) 0.810133,1.161982,-0.223363,-1.198479,-1.264545,-1.510738              -->  0
(224.) 0.831488,-0.018372,0.435651,0.076927,-0.879363,0.326086                -->  0
(225.) 0.3556,-0.583965,-0.143776,-0.597874,-3.38305,-3.102652                -->  0
(226.) 0.300111,-0.249365,0.640785,0.75636,0.468776,-0.163733                 -->  0
(227.) 0.280824,1.322316,0.861265,0.995985,0.661368,0.203631                  -->  0
(228.) 0.959129,-1.124675,-1.082966,-0.619764,-0.49418,-0.408643              -->  0
(229.) 0.892663,-0.26071,-0.415521,-0.768485,-0.108998,0.326086               -->  0
(230.) 0.731113,-0.358196,0.356582,-0.35245,-1.264545,0.570996                -->  0
(231.) 0.820874,0.103829,0.700683,0.148925,-0.49418,0.203631                  -->  0
(232.) 0.15549,1.45917,0.810581,0.598247,1.239142,-0.163733                   -->  0
(233.) 0.731113,-0.195063,0.435651,0.317256,-0.49418,-0.286188                -->  0
(234.) 0.407856,0.500428,0.999372,0.506392,1.04655,1.428181                   -->  0
(235.) -0.044609,-0.227173,0.577022,0.683925,-0.301589,0.203631               -->  0
(236.) 0.488705,-0.500973,-0.077755,0.045184,1.239142,-0.776008               -->  0
(237.) 0.177633,-0.320148,0.176501,0.576732,1.04655,0.448541                  -->  0
(238.) 0.457234,-0.533083,-0.132912,0.036531,-2.420093,-4.572111              -->  0
(239.) -0.017016,0.935042,1.294357,0.995985,1.04655,0.938361                  -->  0
(240.) 0.132786,0.358693,0.508861,0.481252,-0.108998,0.326086                 -->  0
(241.) -0.340719,0.233113,0.018326,0.915873,-0.108998,-0.163733               -->  0
(242.) 0.731113,0.256509,0.270636,0.091374,1.04655,-0.286188                  -->  0
(243.) 0.892663,0.0452,0.356582,0.093419,-1.071954,0.203631                   -->  0
(244.) 0.132786,0.871522,0.435651,-0.104073,1.624324,0.815906                 -->  0
(245.) 0.318991,0.416757,1.193767,0.501156,-0.686771,-0.898463                -->  0
(246.) 0.604586,0.021984,0.577022,0.401436,1.04655,0.938361                   -->  0
(247.) -0.017016,0.457549,0.700683,0.60296,-0.301589,-0.163733                -->  0
(248.) 0.604586,0.227149,0.810581,0.099529,-0.686771,-0.041278                -->  0
(249.) 0.694993,-0.115572,0.577022,0.156588,0.083594,1.305726                 -->  0
(250.) 0.820874,-1.05604,-0.523684,-1.081676,-2.420093,-2.490377              -->  0
(251.) 0.590894,1.050004,0.435651,-0.222793,0.661368,-0.163733                -->  0
(252.) 0.604586,0.453124,0.356582,0.133404,-1.264545,-0.163733                -->  0
(253.) 0.977249,-0.907628,-0.523684,-0.674523,-0.879363,0.693451              -->  0
(254.) 0.240961,-0.227173,0.10483,0.382222,1.816916,0.570996                  -->  0
(255.) -1.001904,0.89659,-0.093203,0.320456,-0.108998,-0.286188               -->  0
(256.) 0.977249,-1.02393,-1.104381,-1.322716,-0.686771,0.326086               -->  0
(257.) 0.061009,0.616134,0.999372,1.137927,-0.108998,0.570996                 -->  0
(258.) 0.562865,-0.295808,0.356582,0.089324,-1.264545,0.448541                -->  0
(259.) 0.533933,0.353646,0.700683,0.250813,0.661368,0.448541                  -->  0
(260.) -1.087314,-0.332619,0.640785,0.719819,0.661368,1.183271                -->  0
(261.) 0.300111,-0.052286,0.757159,0.001084,-0.301589,0.326086                -->  0
(262.) -1.001904,0.796549,-0.926542,-0.476448,1.239142,0.448541               -->  0
(263.) 0.604586,0.158228,-0.290725,0.111628,0.083594,0.693451                 -->  0
(264.) 0.132786,0.402655,0.356582,-0.012568,0.083594,0.693451                 -->  0
(265.) 0.519109,-0.26071,-0.341101,-1.074392,-0.108998,-0.286188              -->  0
(266.) 0.373359,-0.549665,-0.189896,-0.158832,-0.49418,-0.531098              -->  0
(267.) 0.765835,-0.154271,-0.244303,-0.507296,-0.686771,0.570996              -->  0
(268.) 0.670079,-0.184656,-0.496001,-1.089019,-0.301589,-0.163733             -->  0
(269.) 0.604586,-0.783667,-1.086503,-1.011298,0.468776,-1.265828              -->  0
(270.) -0.380573,-0.332619,-0.590032,0.411619,-0.301589,-0.776008             -->  0
(271.) 0.424619,-0.426212,0.270636,0.233425,-1.842319,-1.510738               -->  0
(272.) -1.794543,0.353646,-0.45963,0.361072,-0.49418,-1.510738                -->  0
(273.) -0.340719,1.00439,0.577022,0.749367,0.468776,0.203631                  -->  0
(274.) -0.265958,-0.125062,0.356582,1.20146,0.661368,-0.041278                -->  0
(275.) -0.196953,-0.144409,0.508861,0.408721,0.083594,-0.776008               -->  0
(276.) -0.073078,-0.677228,-0.146511,0.609986,0.468776,0.203631               -->  0
(277.) 0.132786,0.117801,0.640785,-0.410598,-0.108998,0.938361                -->  0
(278.) 0.533933,1.747327,-0.194198,0.00559,0.083594,0.448541                  -->  0
(279.) 0.670079,1.077658,1.594499,0.995985,0.661368,0.693451                  -->  0
(280.) 1.398798,1.113636,1.228446,0.565783,-1.071954,0.570996                 -->  0
(281.) 1.279031,0.487818,1.157826,0.995985,0.853959,1.305726                  -->  0
(282.) 0.63136,0.810495,0.999372,1.260895,0.853959,0.448541                   -->  0
(283.) 1.552935,-0.440583,-0.486299,-0.446599,0.276185,1.305726               -->  0
(284.) 1.398798,0.987095,1.157826,0.179203,-0.301589,0.815906                 -->  0
(285.) 0.457234,0.832286,1.120529,1.369369,0.661368,0.081176                  -->  0
(286.) 0.831488,1.508958,1.4143,1.870101,0.853959,0.081176                    -->  0
(287.) 0.441075,-0.398266,0.270636,0.353399,1.04655,0.815906                  -->  0
(288.) 0.132786,0.208968,0.955446,0.664341,0.661368,0.203631                  -->  0
(289.) 0.799262,0.964903,0.270636,0.411619,0.661368,0.693451                  -->  0
(290.) 0.457234,0.916061,0.955446,1.069686,0.276185,0.448541                  -->  0
(291.) 0.220345,0.575739,0.435651,0.213912,0.853959,0.570996                  -->  0
(292.) 0.977249,-0.332619,-0.899781,-0.971514,-0.301589,0.326086              -->  0
(293.) 0.921753,0.014084,0.111181,-0.535162,-0.108998,-0.041278               -->  0
(294.) -1.001904,0.457549,0.508861,0.816081,0.853959,-2.857742                -->  0
(295.) 0.109493,0.244902,-0.920532,0.099529,0.083594,-0.286188                -->  0
(296.) 0.618073,-0.106199,0.435651,0.585159,0.468776,0.570996                 -->  0
(297.) 0.94993,-1.089577,-0.75538,-0.679237,-0.301589,0.081176                -->  0
(298.) -2.299963,0.807726,-0.426365,0.726011,1.431733,0.326086                -->  0
(299.) -1.277222,-0.035138,-0.247331,0.296183,0.468776,0.815906               -->  0
(300.) 0.15549,0.0061,0.270636,0.133404,1.239142,1.060816                     -->  0
(301.) 0.63136,1.163714,0.861265,0.558411,-0.49418,0.081176                   -->  0
(302.) 0.457234,0.466322,1.228446,0.489265,0.276185,0.081176                  -->  0
(303.) 0.318991,0.31201,0.757159,0.647697,-0.49418,-0.898463                  -->  0
(304.) -0.923924,0.03754,-0.682115,0.038702,0.083594,-0.408643                -->  0
(305.) 0.373359,1.025466,0.435651,0.119606,1.04655,0.326086                   -->  0
(306.) 0.300111,-0.440583,0.435651,0.568227,0.276185,0.203631                 -->  0
(307.) 0.220345,-0.371318,0.128957,0.182919,0.276185,1.060816                 -->  0
(308.) 0.407856,0.804948,-0.439169,0.001084,-0.686771,-1.633193               -->  0
(309.) 0.061009,-0.26071,0.176501,0.199457,0.276185,0.693451                  -->  0
(310.) -0.196953,0.067723,0.090928,0.26109,0.083594,-0.531098                 -->  0
(311.) -0.132878,-0.238187,0.175512,0.682848,1.04655,-1.878103                -->  0
(312.) 0.618073,-0.71802,-0.150627,-0.403563,-0.301589,-0.286188              -->  0
(313.) -2.320987,-0.783667,-1.202945,0.675273,-2.612685,-2.245467             -->  0
(314.) 0.177633,-0.677228,0.270636,0.12159,0.853959,0.448541                  -->  0
(315.) -0.265958,0.383432,0.139266,0.395567,0.661368,0.693451                 -->  0
(316.) 0.085578,0.363706,0.700683,0.166079,0.661368,0.570996                  -->  0
(317.) -1.841071,-0.358196,-0.856728,0.175472,0.083594,-0.408643              -->  0
(318.) 0.731113,-0.164264,-0.334455,-0.523116,-0.686771,0.570996              -->  0
(319.) -0.422281,0.700615,-1.713287,-2.288781,-0.879363,-0.286188             -->  0
(320.) 0.670079,-1.240976,-0.503832,-1.182023,-1.264545,-0.163733             -->  0
(321.) -0.044609,0.834966,0.999372,0.4691,0.853959,0.326086                   -->  0
(322.) 0.670079,-0.56662,-0.324569,-0.991191,-0.686771,0.081176               -->  0
(323.) -0.466024,0.579502,0.810581,0.747359,0.853959,-0.531098                -->  0
(324.) 0.707195,-0.455234,-0.015869,-0.137586,-0.879363,-1.143373             -->  0
(325.) -0.56048,0.767859,0.169563,0.38966,1.04655,0.570996                    -->  0
(326.) 0.407856,-0.238187,0.270636,0.079004,0.468776,0.570996                 -->  0
(327.) 0.085578,-0.195063,-1.075929,-0.642186,1.04655,0.203631                -->  0
(328.) -1.642578,-0.195063,-0.757918,0.00559,0.661368,0.570996                -->  0
(329.) 0.488705,-0.26071,0.700683,0.167965,0.276185,0.815906                  -->  0
(330.) 0.261114,0.837637,0.909476,0.631886,0.468776,-0.041278                 -->  0
(331.) -1.101767,0.233113,0.07792,0.812343,0.853959,0.938361                  -->  0
(332.) -0.666067,0.202809,-0.090611,0.292898,1.624324,-0.041278               -->  0
(333.) 0.533933,-0.500973,-0.347792,-0.507296,-1.457137,-0.531098             -->  0
(334.) 0.300111,-0.052286,0.577022,0.466378,-0.301589,0.570996                -->  0
(335.) 0.912161,-0.426212,-0.658852,-0.800264,-0.108998,0.326086              -->  0
(336.) 0.009754,0.267941,0.700683,0.305969,0.468776,0.938361                  -->  0
(337.) -1.236099,0.74107,-2.6919,-2.648968,0.083594,0.326086                  -->  0
(338.) -0.164344,0.684458,0.270636,0.247361,1.431733,1.060816                 -->  0
(339.) 0.424619,-1.124675,-1.111623,-1.126637,-1.264545,-2.490377             -->  0
(340.) 0.3556,0.052783,-0.308308,-0.255027,-0.49418,-0.041278                 -->  0
(341.) -2.349808,0.089593,-1.273148,-0.345844,1.624324,-0.163733              -->  0
(342.) -0.785761,0.483568,-0.088027,0.70626,-1.071954,-0.776008               -->  0
(343.) -0.422281,-0.26071,0.156548,0.653279,0.083594,-1.388283                -->  0
(344.) -0.017016,0.866407,1.041429,0.441508,0.083594,-0.408643                -->  0
(345.) -0.923924,0.262247,0.143359,0.828127,0.276185,0.448541                 -->  0
(346.) 0.441075,-0.677228,0.270636,0.032174,-0.108998,1.183271                -->  0
(347.) 0.457234,0.03754,0.577022,0.023398,-1.264545,-0.776008                 -->  0
(348.) 0.061009,-0.00197,0.356582,0.111628,-0.301589,-0.163733                -->  0
(349.) 0.15549,-0.227173,0.435651,0.304345,-0.301589,0.815906                 -->  0
(350.) -0.017016,0.684458,0.640785,0.395567,-1.264545,-1.510738               -->  0
(351.) -1.150416,-0.71802,-1.243635,-0.021784,-1.842319,-1.143373             -->  0
(352.) -1.75031,-1.546886,-1.726737,-1.157877,-0.686771,-1.143373             -->  0
(353.) -0.164344,0.483568,0.020641,0.368681,0.853959,0.815906                 -->  0
(354.) -2.183223,-0.164264,-1.693447,-0.610946,-0.301589,-0.653553            -->  0
(355.) -0.132878,-0.272229,0.356582,-0.010279,-1.264545,0.081176              -->  0
(356.) 0.009754,-0.184656,0.861265,0.109622,-0.301589,0.203631                -->  0
(357.) 0.644453,-1.089577,-1.54762,-1.511868,0.468776,0.326086                -->  0
(358.) 0.280824,0.619701,0.1454,-0.708036,0.083594,0.693451                   -->  0
(359.) -0.785761,0.363706,0.270636,0.326822,0.661368,0.326086                 -->  0
(360.) 0.407856,-0.677228,-0.422737,-0.258015,-0.301589,1.428181              -->  0
(361.) -0.422281,-0.174391,0.640785,0.474521,1.04655,0.081176                 -->  0
(362.) -0.852185,-0.078761,-0.573023,0.383714,1.239142,0.448541               -->  0
(363.) 0.199243,-1.430585,-1.179312,-0.732743,0.468776,1.673091               -->  0
(364.) -0.666067,0.397895,-0.079033,0.613479,-1.842319,-1.143373              -->  0
(365.) -2.027319,-0.018372,-1.747263,-1.84556,1.431733,0.570996               -->  0
(366.) -0.923924,0.082373,0.435651,0.318858,0.083594,0.081176                 -->  0
(367.) -0.785761,-0.144409,-0.128868,0.083146,0.276185,-0.163733              -->  0
(368.) 0.390773,0.470671,-0.138329,-0.674523,-0.49418,0.081176                -->  0
(369.) 0.035747,-0.115572,0.270636,0.212118,0.083594,-0.408643                -->  0
(370.) -0.196953,-0.619899,-0.226327,-0.480248,0.661368,-0.163733             -->  0
(371.) 0.657357,-0.761144,-0.998417,-1.067164,0.083594,-0.041278              -->  0
(372.) 0.085578,0.221137,0.356582,-0.026426,0.083594,0.326086                 -->  0
(373.) 0.220345,0.295784,0.435651,-0.222793,0.853959,0.448541                 -->  0
(374.) -2.483816,0.03754,-1.904279,-1.433633,0.661368,-0.163733               -->  0
(375.) -0.56048,-0.164264,0.577022,0.430236,0.661368,0.326086                 -->  0
(376.) 0.390773,0.131519,-1.471535,-2.927523,-2.034911,-1.020918              -->  0
(377.) -0.044609,-0.485416,0.176501,-0.042861,-2.034911,-0.531098             -->  0
(378.) -0.380573,0.373633,0.270636,-0.084039,0.468776,-0.653553               -->  0
(379.) -3.793439,-0.619899,-1.937236,-0.194437,0.661368,-0.286188             -->  0
(380.) -0.132878,0.28477,-0.03281,0.364123,0.083594,0.203631                  -->  0
(381.) -3.144654,-1.32984,-2.151576,-0.597874,-2.034911,-2.980197             -->  0
(382.) 0.220345,-0.227173,0.270636,0.0256,-0.686771,0.448541                  -->  0
(383.) -0.466024,-0.806883,-0.566719,-0.057185,0.276185,0.203631              -->  0
(384.) -2.450436,-0.783667,-0.879456,0.238676,-1.264545,-2.123013             -->  0
(385.) -0.466024,-0.154271,0.139266,0.26109,0.661368,0.326086                 -->  0
(386.) -0.785761,-0.485416,0.167572,0.399972,0.468776,-1.755648               -->  0
(387.) 0.280824,-0.601718,-0.018272,-1.031853,-0.301589,-0.408643             -->  0
(388.) -2.150385,-1.240976,-2.043261,-1.149967,-0.108998,-0.041278            -->  0
(389.) 0.15549,-0.935066,-0.492109,-0.597874,-0.879363,0.570996               -->  0
(390.) 0.337482,0.0061,0.176501,-0.884866,-1.071954,-1.020918                 -->  0
(391.) -1.001904,-0.583965,0.435651,0.435889,1.431733,-0.041278               -->  0
(392.) 0.519109,-1.089577,-0.720513,-0.568077,-0.108998,1.550636              -->  0
(393.) -0.164344,0.267941,0.757159,0.314046,0.468776,0.448541                 -->  0
(394.) -0.340719,-0.549665,-0.496001,-0.576493,-2.227502,-1.633193            -->  0
(395.) -0.512009,0.029802,-0.03281,0.537197,-0.108998,-0.408643               -->  0
(396.) -1.609898,-0.470174,-1.367374,-0.261011,-0.49418,-0.531098             -->  0
(397.) -0.196953,-0.41211,0.164577,0.190306,0.853959,0.938361                 -->  0
(398.) -0.30256,0.533059,0.356582,0.518065,-0.301589,-0.286188                -->  0
(399.) -0.196953,-0.638529,0.0801,0.195807,-0.108998,1.183271                 -->  0
(400.) -0.56048,-0.216317,0.270636,0.184771,0.661368,-0.531098                -->  0
(401.) -0.666067,0.06029,-0.600813,-1.341915,-1.071954,-1.265828              -->  0
(402.) 0.177633,-0.549665,-0.969666,-0.708036,0.661368,-0.286188              -->  0
(403.) 0.035747,-0.935066,-0.066326,-0.049995,-0.49418,1.305726               -->  0
(404.) 0.085578,-0.470174,0.270636,-0.547368,-0.301589,-0.653553              -->  0
(405.) 0.407856,-0.739274,-1.227157,-0.722781,-1.649728,-0.776008             -->  0
(406.) -0.923924,0.244902,0.356582,0.669823,0.853959,0.448541                 -->  0
(407.) -0.265958,-0.010126,0.132061,0.195807,1.04655,0.448541                 -->  0
(408.) -0.785761,-0.65763,-0.469072,0.007835,1.239142,0.448541                -->  0
(409.) -2.726407,-0.052286,-1.122588,0.131446,-0.49418,-1.143373              -->  0
(410.) -0.56048,-0.601718,0.508861,-0.13235,-0.108998,-0.041278               -->  0
(411.) -0.230792,0.110847,0.114341,0.42169,-0.686771,-0.531098                -->  0
(412.) -0.10248,-0.855575,0.356582,0.162294,0.276185,0.938361                 -->  0
(413.) 0.061009,-0.371318,-0.040161,-0.693524,0.083594,-0.163733              -->  0
(414.) -1.359508,0.31201,-0.575133,0.255965,-0.49418,-0.531098                -->  0
(415.) -1.818517,-1.089577,-0.701128,-0.389653,1.431733,-0.898463             -->  0
(416.) 0.373359,-0.697348,-0.080313,-0.965047,-0.879363,-0.163733             -->  0
(417.) -0.785761,-0.500973,-0.063804,0.424547,1.239142,0.693451               -->  0
(418.) 0.280824,-0.144409,-0.143776,-1.157877,-0.301589,-0.531098             -->  0
(419.) -0.56048,0.124691,0.577022,0.408721,-0.108998,0.203631                 -->  0
(420.) -0.196953,0.738034,-0.737793,-0.683975,-0.301589,-1.143373             -->  0
(421.) 0.261114,-0.830836,-0.259536,-0.237306,-1.264545,-0.531098             -->  0
(422.) -3.473509,-1.763933,-2.573462,-0.914885,-0.49418,-0.776008             -->  0
(423.) -1.236099,-0.830836,-0.207216,-0.679237,-1.842319,-0.776008            -->  0
(424.) -0.56048,0.131519,0.508861,-0.177833,-0.108998,-0.776008               -->  0
(425.) -0.230792,-0.272229,0.143359,-0.593558,0.276185,-0.653553              -->  0
(426.) -1.192738,-0.371318,-1.686922,-2.236109,1.431733,-0.408643             -->  0
(427.) -1.737269,-1.05604,-0.957152,-1.165856,-0.879363,-0.286188             -->  0
(428.) -0.10248,0.184025,-0.966523,-0.773706,0.853959,0.448541                -->  0
(429.) -2.368303,-2.069843,-2.439459,-1.547544,-0.49418,-2.123013             -->  0
(430.) 0.240961,-1.089577,-0.213057,-0.156149,0.083594,0.081176               -->  0
(431.) -2.596935,-0.881153,-2.130979,-0.503383,0.083594,-0.653553             -->  0
(432.) -2.592126,-1.430585,-1.775311,-0.921008,-2.997867,-3.102652            -->  0
(433.) -0.044609,-0.677228,0.026406,-0.491743,0.661368,-0.041278              -->  0
(434.) -2.074539,-1.124675,-1.796882,-0.35577,-1.457137,-1.633193             -->  0
(435.) -0.422281,-0.010126,-0.119497,0.190306,1.04655,0.448541                -->  0
(436.) -0.380573,0.279202,0.356582,-0.25205,-0.879363,-0.163733               -->  0
(437.) -0.196953,-0.638529,-0.047566,-0.049995,0.661368,0.570996              -->  0
(438.) -0.017016,-1.430585,-1.334957,-1.190214,-1.649728,-3.837382            -->  0
(439.) -1.977612,-0.332619,-1.231251,-0.933377,1.624324,0.815906              -->  0
(440.) -0.30256,0.029802,0.356582,0.201276,0.083594,-0.163733                 -->  0
(441.) -0.10248,-0.935066,-0.394183,-0.480248,-0.879363,1.060816              -->  0
(442.) 0.407856,-0.549665,-1.344111,-2.162349,-2.420093,-1.388283             -->  0
(443.) -0.073078,-1.200184,-0.86519,-0.855794,-3.38305,-1.633193              -->  0
(444.) 0.109493,-0.272229,0.074641,-0.642186,0.276185,0.203631                -->  0
(445.) -1.92366,-1.05604,-0.765572,-0.285343,0.083594,-0.653553               -->  0
(446.) 0.132786,-0.440583,-0.75538,-0.228571,0.468776,0.570996                -->  0
(447.) -0.265958,-0.426212,-0.165869,-0.468894,-2.612685,0.693451             -->  0
(448.) -0.340719,-0.601718,-0.043857,-0.021784,-0.108998,-0.041278            -->  0
(449.) -0.340719,-0.345299,0.508861,0.091374,-0.686771,-0.408643              -->  0
(450.) -1.087314,-0.65763,-0.189896,0.213912,1.04655,-0.163733                -->  0
(451.) 0.261114,0.164761,-1.768224,-1.55975,-0.301589,1.305726                -->  0
(452.) -0.044609,-0.830836,-1.530816,-0.965047,-1.071954,-1.755648            -->  0
(453.) -2.174148,-1.161485,-1.104381,-0.965047,0.083594,-1.020918             -->  0
(454.) 0.177633,-1.200184,-0.3328,-0.382776,-1.649728,-2.612832               -->  0
(455.) 1.453174,1.732817,-0.568816,-1.971007,-1.649728,-0.531098              -->  0
(456.) 1.398798,1.470777,-0.298679,-0.372556,-1.264545,-0.163733              -->  0
(457.) 0.788257,1.790007,1.08177,1.511347,1.04655,0.693451                    -->  0
(458.) 1.453174,0.976081,1.546276,0.995985,0.661368,1.673091                  -->  0
(459.) 1.140772,0.850851,1.261951,1.260895,1.04655,1.428181                   -->  0
(460.) 0.519109,1.665615,1.726482,1.776339,1.239142,0.203631                  -->  0
(461.) 1.598942,2.233892,0.435651,0.915873,-0.108998,0.938361                 -->  0
(462.) 1.504441,0.568157,1.570682,0.779939,-0.301589,1.428181                 -->  0
(463.) 1.140772,0.177658,0.909476,0.637564,-0.301589,-0.408643                -->  0
(464.) 0.519109,0.383432,1.356146,1.466409,0.853959,1.060816                  -->  0
(465.) 0.968235,0.273592,0.700683,0.152764,0.276185,-0.653553                 -->  0
(466.) 0.177633,1.017106,1.08177,1.069686,1.04655,-0.041278                   -->  0
(467.) -0.017016,0.863837,0.700683,1.137927,0.276185,0.326086                 -->  0
(468.) 0.590894,0.483568,0.508861,0.154678,1.431733,0.570996                  -->  0
(469.) 1.212563,0.619701,0.955446,0.520639,0.083594,0.693451                  -->  0
(470.) -0.852185,0.84295,0.176501,1.069686,0.276185,-0.531098                 -->  0
(471.) 0.63136,0.654476,1.157826,0.995985,1.239142,1.795546                   -->  0
(472.) 0.742837,0.014084,1.08177,1.069686,0.468776,1.428181                   -->  0
(473.) -1.102678,0.719556,-0.210132,0.915873,-1.264545,-1.510738              -->  0
(474.) 1.062732,1.281991,-0.698731,-1.433633,1.04655,-2.490377                -->  0
(475.) 0.977249,0.483568,0.640785,0.296183,-1.071954,0.081176                 -->  0
(476.) 0.390773,0.764929,1.193767,1.20146,1.04655,0.693451                    -->  0
(477.) 0.682622,0.932696,1.157826,1.260895,0.661368,-0.408643                 -->  0
(478.) -0.785761,0.06029,-0.111535,0.765273,-1.264545,-1.510738               -->  0
(479.) 0.931244,0.850851,0.861265,0.638696,0.276185,1.183271                  -->  0
(480.) -0.380573,0.383432,0.165576,0.781877,1.239142,0.815906                 -->  0
(481.) 0.519109,0.785203,1.469222,1.554196,1.239142,0.938361                  -->  0
(482.) 0.977249,0.466322,0.861265,0.592321,0.276185,1.060816                  -->  0
(483.) 0.300111,0.560497,1.120529,1.634343,1.239142,0.815906                  -->  0
(484.) 0.788257,0.601694,1.120529,0.915873,-0.301589,0.081176                 -->  0
(485.) 1.140772,0.4214,0.861265,0.340988,-0.49418,1.305726                    -->  0
(486.) 1.140772,0.0452,0.356582,0.113629,-1.071954,0.693451                   -->  0
(487.) 0.533933,0.4214,0.757159,0.819805,1.04655,-0.041278                    -->  0
(488.) -0.611721,0.54886,0.700683,1.260895,1.239142,-0.041278                 -->  0
(489.) 1.140772,0.34345,0.176501,0.115625,-0.301589,0.938361                  -->  0
(490.) 0.604586,0.674596,1.157826,1.20146,-0.108998,0.081176                  -->  0
(491.) 0.337482,0.393104,0.861265,1.137927,1.04655,0.326086                   -->  0
(492.) 1.279031,-0.739274,-0.224844,-0.35577,0.276185,1.428181                -->  0
(493.) 1.140772,0.138285,0.270636,0.127516,0.661368,0.815906                  -->  0
(494.) 1.340912,-0.697348,-0.686834,-0.861535,0.276185,1.060816               -->  0
(495.) 1.140772,1.48786,-0.583619,-1.466352,-1.071954,0.815906                -->  0
(496.) 0.576989,-0.371318,0.640785,0.221056,-3.960824,-1.755648               -->  0
(497.) 1.062732,0.91846,0.810581,0.314046,1.04655,1.428181                    -->  0
(498.) 0.15549,-0.283926,-0.123503,0.623878,-2.420093,-0.776008               -->  0
(499.) 0.441075,0.388283,0.700683,0.995985,0.853959,0.815906                  -->  0
(500.) 0.441075,1.256413,0.757159,0.823513,0.661368,0.815906                  -->  0
(501.) 0.959129,0.487818,0.999372,0.42169,0.661368,1.183271                   -->  0
(502.) 1.140772,0.029802,0.577022,0.217491,0.468776,1.673091                  -->  0
(503.) 0.977249,1.228351,0.999372,0.690362,0.276185,0.938361                  -->  0
(504.) 0.977249,0.448673,1.041429,0.915873,0.853959,1.060816                  -->  0
(505.) -0.265958,1.195896,-0.199962,-0.035781,1.816916,1.183271               -->  0
(506.) 0.852347,0.832286,1.08177,0.742321,0.468776,0.815906                   -->  0
(507.) 1.279031,1.373807,-1.425544,-2.648968,-1.842319,-1.633193              -->  0
(508.) 0.519109,0.89412,1.325734,1.20146,0.661368,0.693451                    -->  0
(509.) 0.220345,1.094914,1.08177,0.915873,0.853959,0.081176                   -->  0
(510.) 0.940636,0.295784,0.640785,0.434479,1.239142,0.570996                  -->  0
(511.) 0.373359,0.158228,0.700683,0.700991,1.04655,1.060816                   -->  0
(512.) 1.062732,0.0452,0.356582,-0.08652,0.661368,1.060816                    -->  0
(513.) 1.140772,0.227149,0.640785,0.236929,0.276185,1.550636                  -->  0
(514.) 0.424619,-0.010126,0.810581,0.828127,0.853959,-0.041278                -->  0
(515.) 1.140772,-0.184656,0.356582,-0.038135,-1.264545,0.203631               -->  0
(516.) -0.132878,0.327894,0.909476,1.069686,1.239142,-0.653553                -->  0
(517.) 0.618073,0.512831,0.700683,0.74131,1.239142,0.938361                   -->  0
(518.) 0.604586,0.764929,1.041429,1.069686,-0.879363,0.326086                 -->  0
(519.) 0.618073,0.54494,0.955446,0.637564,0.853959,0.815906                   -->  0
(520.) -1.360722,-0.295808,-0.486299,0.828127,-1.457137,-1.633193             -->  0
(521.) 0.788257,-0.096942,0.577022,0.470458,0.468776,-0.286188                -->  0
(522.) 0.519109,0.03754,0.810581,0.520639,0.661368,0.938361                   -->  0
(523.) 0.777116,-0.061008,0.356582,0.334719,-0.49418,-0.408643                -->  0
(524.) 0.424619,0.31201,0.700683,0.755364,0.853959,0.081176                   -->  0
(525.) -1.812463,0.677898,-0.354529,0.354938,1.04655,0.938361                 -->  0
(526.) 0.590894,0.184025,0.17155,0.145069,-0.686771,-2.735287                 -->  0
(527.) -0.132878,0.661242,1.041429,0.68069,0.853959,-0.041278                 -->  0
(528.) 0.085578,-0.455234,0.124803,0.415948,1.816916,1.428181                 -->  0
(529.) 0.590894,-0.069833,0.700683,0.474521,-0.108998,0.203631                -->  0
(530.) 0.457234,-0.71802,-0.181349,0.182919,-0.49418,-0.898463                -->  0
(531.) 0.682622,0.889157,0.861265,0.474521,-0.49418,-0.163733                 -->  0
(532.) -0.923924,0.317342,0.270636,0.995985,-1.071954,-0.898463               -->  0
(533.) 0.035747,0.295784,0.909476,0.639826,0.083594,-0.531098                 -->  0
(534.) -0.666067,0.799359,-1.227157,-0.059594,-0.686771,-0.898463             -->  0
(535.) -0.044609,0.866407,0.700683,1.069686,0.276185,0.326086                 -->  0
(536.) 0.754409,-0.035138,0.435651,-0.079098,-0.686771,1.795546               -->  0
(537.) 0.670079,1.298091,-0.139688,-0.669834,-1.264545,-1.388283              -->  0
(538.) 0.424619,-0.332619,0.909476,0.274617,-0.49418,-0.531098                -->  0
(539.) 0.754409,0.227149,0.700683,0.405814,-0.49418,-1.020918                 -->  0
(540.) 0.872731,0.633804,-0.179932,0.027796,0.276185,0.081176                 -->  0
(541.) 0.931244,0.244902,-0.108896,-0.188869,1.04655,0.570996                 -->  0
(542.) -0.466024,0.594369,0.508861,1.316727,-0.108998,-0.163733               -->  0
(543.) 0.373359,0.508719,1.041429,0.519353,-0.108998,0.938361                 -->  0
(544.) 0.788257,0.512831,0.810581,0.299457,0.083594,1.428181                  -->  0
(545.) -0.785761,0.4214,0.356582,0.518065,1.04655,-2.245467                   -->  0
(546.) 0.548516,0.029802,0.861265,0.552222,-0.108998,0.081176                 -->  0
(547.) 0.576989,0.23903,0.120631,0.456786,-0.108998,-0.531098                 -->  0
(548.) 0.862597,-0.087797,0.094154,-0.90276,-0.108998,-0.776008               -->  0
(549.) 0.473108,1.012891,0.955446,0.474521,-0.879363,-0.163733                -->  0
(550.) 0.754409,0.770777,-0.154761,-0.205675,0.083594,0.570996                -->  0
(551.) 0.035747,-0.078761,0.757159,0.995985,0.661368,0.938361                 -->  0
(552.) -0.56048,1.075716,0.861265,1.069686,0.661368,-0.776008                 -->  0
(553.) 0.407856,0.525033,0.909476,0.42169,-0.108998,0.570996                  -->  0
(554.) 0.968235,0.393104,-0.351155,-0.054782,0.661368,0.693451                -->  0
(555.) -1.685178,0.719556,-0.752848,0.534669,-0.301589,-0.286188              -->  0
(556.) -0.30256,0.876603,0.508861,0.611152,1.04655,0.815906                   -->  0
(557.) 0.373359,-0.026708,0.176501,-0.158832,-0.108998,0.815906               -->  0
(558.) 0.852347,1.303861,0.01018,-1.258506,-1.457137,0.326086                 -->  0
(559.) 0.912161,-0.619899,-1.294782,-1.111405,0.468776,0.693451               -->  0
(560.) -0.611721,-0.41211,-0.021886,0.501156,0.468776,0.326086                -->  0
(561.) 0.590894,0.295784,0.435651,0.995985,-0.108998,-0.163733                -->  0
(562.) 0.63136,-0.125062,-0.080313,-0.453971,0.083594,-1.143373               -->  0
(563.) 0.921753,-0.164264,0.049134,-0.606568,-0.49418,0.203631                -->  0
(564.) 0.799262,-0.125062,-0.287562,-0.722781,-1.071954,-0.163733             -->  0
(565.) -1.341484,-0.638529,-1.093615,-0.071736,0.661368,-0.531098             -->  0
(566.) -0.017016,0.633804,0.955446,0.131446,0.276185,-0.653553                -->  0
(567.) 0.261114,0.785203,-1.492683,-1.677549,-1.842319,-1.510738              -->  0
(568.) 0.085578,0.397895,0.700683,0.502468,0.276185,0.448541                  -->  0
(569.) 0.035747,0.144992,0.810581,0.460909,0.083594,-1.510738                 -->  0
(570.) -0.852185,0.388283,0.757159,1.069686,1.239142,-1.510738                -->  0
(571.) -2.230033,0.295784,-0.329499,0.388177,0.853959,0.203631                -->  0
(572.) 0.15549,0.412086,1.120529,0.810468,0.276185,0.203631                   -->  0
(573.) 0.841978,-0.71802,-0.079033,-0.593558,-0.108998,0.815906               -->  0
(574.) -1.343866,-0.227173,0.176501,0.548489,1.431733,-1.755648               -->  0
(575.) 0.390773,0.951268,0.999372,0.197634,-0.108998,0.081176                 -->  0
(576.) -0.044609,-0.078761,0.999372,1.069686,0.083594,-0.041278               -->  0
(577.) -0.512009,0.244902,0.508861,0.777024,0.276185,-2.612832                -->  0
(578.) 0.657357,-0.638529,0.640785,-0.403563,0.083594,0.570996                -->  0
(579.) 0.852347,-0.272229,0.176501,-0.156149,-0.686771,-0.286188              -->  0
(580.) 0.644453,-0.56662,0.757159,-0.276143,0.853959,0.938361                 -->  0
(581.) -0.611721,0.722667,-1.171558,-0.362448,0.083594,-0.898463              -->  0
(582.) -0.10248,0.54886,-0.474781,-0.386208,1.816916,0.938361                 -->  0
(583.) 0.132786,0.623252,0.757159,0.42312,-0.879363,-1.388283                 -->  0
(584.) 0.765835,0.889157,-0.77587,-0.984586,-0.879363,-1.143373               -->  0
(585.) -1.087314,-0.238187,-0.596486,0.08521,-1.842319,-1.388283              -->  0
(586.) 0.820874,-0.806883,-0.613907,-0.393111,0.468776,0.570996               -->  0
(587.) 0.548516,-0.061008,0.356582,0.023398,0.276185,0.570996                 -->  0
(588.) -1.477377,0.190338,-0.390671,0.601784,0.276185,-0.531098               -->  0
(589.) 0.3556,0.430601,0.757159,0.368681,0.661368,-0.041278                   -->  0
(590.) 0.457234,-0.56662,0.176501,0.222833,0.083594,0.448541                  -->  0
(591.) -0.230792,0.373633,0.700683,0.995985,0.276185,-0.163733                -->  0
(592.) 0.061009,-0.087797,0.176501,0.42312,1.04655,-0.163733                  -->  0
(593.) 0.682622,0.117801,-0.119497,-0.914885,-0.49418,0.693451                -->  0
(594.) -1.890145,0.407385,-1.20694,0.213912,1.04655,-0.408643                 -->  0
(595.) -0.666067,0.110847,0.861265,0.821661,0.853959,0.081176                 -->  0
(596.) 0.754409,0.244902,-0.012276,-0.978027,-1.071954,-1.755648              -->  0
(597.) 0.548516,-0.144409,0.577022,0.314046,0.276185,0.326086                 -->  0
(598.) -0.196953,0.317342,0.435651,0.460909,-0.108998,-0.898463               -->  0
(599.) 0.742837,-0.71802,-0.469072,-0.703173,0.661368,0.081176                -->  0
(600.) 0.562865,0.552759,-0.480524,-0.43565,-1.457137,-0.286188               -->  0
(601.) 0.15549,-0.881153,0.435651,-0.180579,-0.301589,0.448541                -->  0
(602.) 0.373359,-0.069833,-0.654265,-0.166927,-0.49418,-0.286188              -->  0
(603.) 0.261114,-0.320148,-0.254941,-0.180579,-0.108998,1.673091              -->  0
(604.) -2.066494,-0.65763,-1.034731,0.208518,-0.686771,-1.143373              -->  0
(605.) -0.422281,0.208968,0.810581,0.828127,0.468776,-0.286188                -->  0
(606.) -0.10248,-0.154271,0.757159,0.339424,0.661368,1.183271                 -->  0
(607.) 0.261114,0.327894,-0.3328,-0.307173,-0.879363,0.081176                 -->  0
(608.) -0.723919,0.626786,0.577022,0.552222,0.661368,0.448541                 -->  0
(609.) 0.682622,-0.272229,-0.075204,-0.768485,-1.071954,0.448541              -->  0
(610.) -0.30256,-0.184656,0.909476,0.17734,0.853959,0.448541                  -->  0
(611.) -0.611721,-0.320148,0.577022,0.585159,0.661368,1.428181                -->  0
(612.) -0.132878,0.388283,0.577022,0.520639,1.04655,0.326086                  -->  0
(613.) 0.199243,0.244902,0.049134,0.001084,0.083594,0.326086                  -->  0
(614.) -0.512009,0.262247,0.270636,0.318858,1.04655,0.326086                  -->  0
(615.) -0.666067,-0.043663,0.435651,0.66544,0.661368,-0.531098                -->  0
(616.) 0.009754,-0.238187,-0.122166,-0.732743,-0.49418,-3.959837              -->  0
(617.) 0.240961,-0.018372,0.577022,0.296183,-0.108998,0.815906                -->  0
(618.) -2.226835,0.3383,-1.090052,0.111628,0.468776,0.081176                  -->  0
(619.) -0.132878,-0.106199,-0.185614,0.257677,0.468776,0.203631               -->  0
(620.) -0.265958,0.416757,0.640785,0.619271,-1.457137,-0.531098               -->  0
(621.) 0.177633,-0.345299,-0.211593,0.00559,0.661368,-0.653553                -->  0
(622.) 0.15549,-0.806883,-0.329499,-0.2792,-0.879363,1.060816                 -->  0
(623.) 0.533933,-0.881153,-0.947869,-0.535162,0.083594,-0.163733              -->  0
(624.) -0.512009,-0.440583,-1.079441,-0.789549,-2.227502,-2.123013            -->  0
(625.) 0.280824,-0.30788,-0.217461,-0.304023,-0.108998,-0.041278              -->  0
(626.) -0.30256,0.28477,0.435651,0.188465,1.431733,1.183271                   -->  0
(627.) 0.3556,0.124691,-0.543944,-0.822076,-1.264545,-0.653553                -->  0
(628.) -1.818517,-1.124675,-1.410678,-0.069295,-1.649728,-1.388283            -->  0
(629.) 0.132786,-0.00197,0.176501,0.107612,0.661368,-0.286188                 -->  0
(630.) 0.407856,0.06029,0.810581,-0.491743,-1.457137,-0.898463                -->  0
(631.) -0.164344,0.151639,0.356582,0.411619,-0.301589,-1.510738               -->  0
(632.) 0.300111,1.083454,0.640785,-0.222793,-0.301589,-0.041278               -->  0
(633.) -0.265958,0.190338,0.508861,0.331568,0.468776,-0.041278                -->  0
(634.) -1.291735,-0.195063,-1.455966,-0.081565,-0.49418,-1.143373             -->  0
(635.) -2.012115,0.3383,-0.742786,0.424547,0.468776,0.326086                  -->  0
(636.) -0.132878,0.295784,-0.529719,-0.177833,-2.227502,-0.653553             -->  0
(637.) -0.512009,0.616134,0.356582,1.137927,1.816916,1.305726                 -->  0
(638.) -2.346154,-0.935066,-1.268878,-0.382776,0.853959,0.693451              -->  0
(639.) 0.604586,-1.161485,-1.048274,-1.118989,-0.108998,0.448541              -->  0
(640.) 0.009754,-0.601718,-0.36643,-0.211346,0.083594,1.060816                -->  0
(641.) 0.590894,-1.684442,-0.851127,-0.914885,-2.420093,-0.531098             -->  0
(642.) -1.087314,-0.761144,-0.642888,-0.231473,1.04655,0.693451               -->  0
(643.) -2.338891,-1.05604,-1.587977,-0.237306,0.853959,0.203631               -->  0
(644.) 0.132786,-0.205615,0.700683,0.091374,-0.108998,-0.286188               -->  0
(645.) 0.337482,0.674596,0.060305,-0.727748,-0.108998,-0.163733               -->  0
(646.) -0.923924,-0.96354,-0.354529,0.404357,1.04655,-0.653553                -->  0
(647.) 0.085578,-0.549665,-0.079033,-0.035781,0.083594,0.448541               -->  0
(648.) -1.134219,0.052783,-0.73035,-0.049995,-0.301589,-0.408643              -->  0
(649.) -2.007104,-0.26071,-0.075204,0.579147,-0.108998,-1.020918              -->  0
(650.) 0.519109,-0.739274,-0.663461,-0.800264,-0.686771,0.203631              -->  0
(651.) -1.001904,-0.806883,-0.373296,-0.017164,1.04655,1.060816               -->  0
(652.) -1.001904,-0.164264,0.270636,0.222833,1.239142,1.060816                -->  0
(653.) 0.240961,-1.32984,0.121676,-0.359103,-0.49418,-0.286188                -->  0
(654.) 0.441075,-0.078761,-0.107578,-0.838781,-0.301589,0.326086              -->  0
(655.) -0.196953,-1.852797,-0.691576,0.160396,0.661368,-0.776008              -->  0
(656.) 0.318991,-0.533083,-0.815473,-1.018099,-0.301589,-0.408643             -->  0
(657.) 0.009754,-0.00197,-0.047566,-0.124551,-1.842319,-1.265828              -->  0
(658.) -1.001904,-0.65763,-0.77587,-0.129743,-0.686771,-0.286188              -->  0
(659.) -1.98246,-0.96354,-1.455966,-0.297754,-0.301589,-1.388283              -->  0
(660.) -1.301922,-1.430585,-0.941729,0.099529,0.661368,-0.041278              -->  0
(661.) -0.422281,-0.295808,-0.118166,-0.369174,-1.264545,1.060816             -->  0
(662.) 0.15549,-0.249365,-0.088027,-0.114255,-0.686771,-0.653553              -->  0
(663.) -1.247811,0.03754,0.176501,-0.001177,0.468776,-0.286188                -->  0
(664.) -0.340719,-0.71802,0.577022,0.401436,0.468776,0.448541                 -->  0
(665.) -0.666067,-0.30788,0.169563,0.179203,0.276185,0.693451                 -->  0
(666.) 0.318991,-1.200184,-0.926542,-0.827611,0.661368,0.693451               -->  0
(667.) -0.164344,-0.078761,-0.135617,0.359542,-0.686771,-0.898463             -->  0
(668.) 0.280824,-0.806883,-0.465285,-0.543281,0.083594,1.305726               -->  0
(669.) -0.017016,0.096745,0.270636,0.184771,-0.49418,-0.163733                -->  0
(670.) -3.423664,-0.533083,-2.01567,-0.461402,-0.879363,-0.408643             -->  0
(671.) -0.196953,-0.907628,-0.287562,-0.134964,-1.457137,-0.286188            -->  0
(672.) -1.33084,-1.02393,0.081188,0.089324,1.239142,-0.163733                 -->  0
(673.) -0.466024,-0.440583,-0.041391,-0.31669,-0.879363,0.570996              -->  0
(674.) -0.380573,-0.184656,0.270636,0.091374,0.276185,-0.041278               -->  0
(675.) -0.265958,0.322636,-1.008189,-0.965047,0.853959,-1.633193              -->  0
(676.) 0.220345,0.110847,-0.042623,-0.410598,-1.842319,0.448541               -->  0
(677.) -1.087314,-0.205615,-0.689202,-0.323089,1.624324,0.815906              -->  0
(678.) 0.390773,-1.430585,-0.985536,-0.908802,-2.227502,-0.163733             -->  0
(679.) 0.085578,-0.993131,-1.167704,-1.2764,-1.649728,1.305726                -->  0
(680.) -0.512009,0.59068,-0.624954,-0.655906,-1.457137,-1.143373              -->  0
(681.) 0.390773,-0.516857,-1.179312,-2.316291,-2.420093,0.448541              -->  0
(682.) -1.37296,-0.761144,-0.048806,0.587552,0.276185,-2.857742               -->  0
(683.) -0.666067,-0.783667,-0.152003,0.493246,-0.49418,-1.510738              -->  0
(684.) 0.504036,-0.295808,-0.929561,-1.059993,0.276185,-0.163733              -->  0
(685.) -0.132878,-0.384671,0.114341,-0.28843,-0.879363,-0.041278              -->  0
(686.) -0.196953,-0.533083,-0.077755,-0.400066,-0.686771,1.060816             -->  0
(687.) -1.667895,0.144992,-3.359345,-2.210861,-2.034911,-0.776008             -->  0
(688.) 0.199243,-1.02393,-0.862362,-1.126637,-0.108998,0.693451               -->  0
(689.) -0.132878,-1.161485,-0.672744,-0.742814,-1.649728,-1.633193            -->  0
(690.) -1.094511,-0.601718,-0.517687,-0.156149,1.239142,1.428181              -->  0
(691.) 0.424619,-0.371318,-0.807424,-0.978027,0.468776,0.938361               -->  0
(692.) -0.512009,-0.125062,-0.034032,-0.503383,-0.879363,-0.163733            -->  0
(693.) 0.009754,-0.332619,-1.514293,-1.02495,0.083594,-1.388283               -->  0
(694.) 0.085578,-0.320148,-0.235274,-0.568077,-0.301589,-0.163733             -->  0
(695.) 0.009754,-1.05604,-0.804756,-0.580729,0.276185,-1.388283               -->  0
(696.) 0.177633,-0.41211,-0.613907,-1.173904,-0.879363,-0.408643              -->  0
(697.) -0.785761,-0.061008,0.176501,0.148925,1.04655,0.203631                 -->  0
(698.) 0.177633,-0.371318,-0.363015,-1.371485,-1.649728,-0.531098             -->  0
(699.) -0.265958,-0.739274,-0.511725,-0.589262,-2.227502,-2.367922            -->  0
(700.) -1.087314,0.34345,0.270636,0.252533,0.853959,0.448541                  -->  0
(701.) -0.196953,0.903951,0.270636,0.493246,-0.301589,-0.531098               -->  0
(702.) -0.132878,-0.677228,-0.042623,-1.173904,-1.071954,-1.143373            -->  0
(703.) -2.335281,-0.993131,-1.51977,-0.597874,-1.457137,-0.898463             -->  0
(704.) -0.073078,-0.638529,-0.533762,-1.2323,1.431733,0.815906                -->  0
(705.) -0.422281,-0.195063,0.176501,-0.747892,-0.879363,-0.531098             -->  0
(706.) 0.035747,-0.806883,-0.324569,-0.421251,-2.227502,0.203631              -->  0
(707.) 0.441075,0.096745,-1.849123,-2.572131,-1.457137,0.693451               -->  0
(708.) 0.085578,-0.96354,-0.773285,-0.342559,-0.108998,-0.653553              -->  0
(709.) -1.76164,-0.078761,-1.260392,-0.712925,-0.879363,-1.020918             -->  0
(710.) -0.230792,-0.619899,-0.383684,-0.180579,-0.879363,-1.143373            -->  0
(711.) -1.549405,-0.855575,-0.287562,0.314046,0.276185,-1.878103              -->  0
(712.) 0.009754,-0.907628,0.028702,-0.191649,-0.879363,-1.265828              -->  0
(713.) -0.196953,-0.549665,0.062524,-0.43565,-1.649728,-0.898463              -->  0
(714.) -6.662579,-3.421667,-3.006729,-0.939625,2.202098,1.428181              -->  0
(715.) -0.611721,-0.096942,0.577022,0.255965,-0.686771,0.203631               -->  0
(716.) -0.044609,-1.05604,-0.361312,-0.372556,-0.108998,0.815906              -->  0
(717.) -2.130097,-1.124675,-0.718069,-0.240236,-0.49418,-0.776008             -->  0
(718.) -0.723919,-0.549665,0.435651,0.043028,-1.071954,-2.000558              -->  0
(719.) -0.611721,-1.32984,-0.760463,-0.789549,0.468776,0.326086               -->  0
(720.) -1.087314,-0.761144,-0.182769,0.146999,0.853959,-0.898463              -->  0
(721.) -0.666067,0.322636,-0.773285,-0.096509,1.04655,0.570996                -->  0
(722.) -0.852185,-0.583965,-0.472875,-0.43565,0.083594,-0.041278              -->  0
(723.) -0.380573,-1.546886,-0.611713,-1.074392,-0.879363,-0.776008            -->  0
(724.) -2.082657,0.453124,-2.071644,-1.004547,-0.301589,-1.510738             -->  0
(725.) -2.606633,-1.124675,-0.747804,-2.236109,-1.649728,-0.653553            -->  0
(726.) -1.890145,-0.907628,-0.944794,-0.610946,1.04655,-3.470017              -->  0
(727.) -0.512009,-0.806883,-0.297083,-0.101544,-0.108998,0.326086             -->  0
(728.) 0.109493,-1.124675,-1.068942,-0.878977,-1.264545,-1.388283             -->  0
(729.) -0.512009,-1.089577,-0.45214,-0.747892,0.083594,-0.163733              -->  0
(730.) -0.422281,-0.205615,-0.346115,-0.559737,-0.49418,0.203631              -->  0
(731.) 0.109493,-1.200184,-1.43055,-1.103882,-1.264545,-2.123013              -->  0
(732.) -1.419747,-0.295808,-0.545993,-0.010279,0.083594,-0.408643             -->  0
(733.) -0.611721,-0.00197,-0.215991,-0.855794,0.083594,0.326086               -->  0
(734.) -0.666067,-0.358196,-0.431832,-0.811106,-1.264545,-0.163733            -->  0
(735.) -0.230792,-0.332619,0.062524,-0.310335,-1.071954,-0.653553             -->  0
(736.) 0.177633,-1.684442,-1.148654,-1.206819,-0.301589,-0.286188             -->  0
(737.) -1.001904,-0.583965,-0.482445,-0.012568,-0.49418,0.326086              -->  0
(738.) -0.164344,-1.02393,-1.400889,-1.004547,-0.686771,1.060816              -->  0
(739.) -2.233242,-1.200184,-1.264625,-1.126637,-0.108998,-0.531098            -->  0
(740.) -0.230792,-0.358196,-3.083803,-3.513593,-2.227502,-1.020918            -->  0
(741.) -3.582367,-2.375753,-1.599817,-2.010227,-0.108998,0.081176             -->  0
(742.) -0.785761,0.221137,0.054735,-0.674523,0.661368,-1.265828               -->  0
(743.) -0.512009,-0.426212,-0.264152,-0.389653,0.083594,1.183271              -->  0
(744.) -1.896748,-0.516857,-0.737793,-0.172364,-1.264545,-0.776008            -->  0
(745.) 0.109493,-0.881153,-0.631641,-0.890792,0.083594,-2.490377              -->  0
(746.) -0.611721,-0.71802,-0.995181,-0.503383,0.468776,-0.531098              -->  0
(747.) 0.085578,-1.02393,-1.277437,-1.597368,-1.457137,-1.633193              -->  0
(748.) 0.035747,-1.32984,-1.082966,-1.285479,-2.612685,0.081176               -->  0
(749.) -0.56048,-0.516857,-0.179932,-0.208506,-0.301589,0.081176              -->  0
(750.) -0.073078,-1.852797,-1.167704,-0.703173,0.468776,0.081176              -->  0
(751.) -0.164344,-1.124675,-0.411932,-0.563898,-0.301589,0.081176             -->  0
(752.) -1.319161,-0.018372,-0.270341,-0.010279,0.853959,0.570996              -->  0
(753.) -0.666067,0.158228,-0.745292,-0.127144,1.04655,0.938361                -->  0
(754.) -0.923924,0.075084,-0.26879,-0.104073,-0.108998,-0.408643              -->  0
(755.) -0.466024,-0.249365,-0.684472,-0.861535,1.04655,0.448541               -->  0
(756.) 0.109493,-2.89871,-3.196912,-3.328673,-1.842319,-0.898463              -->  0
(757.) -0.340719,-0.677228,-0.745292,-0.914885,0.468776,-0.408643             -->  0
(758.) -0.132878,-0.619899,-0.911586,-1.511868,-1.649728,-0.286188            -->  0
(759.) -0.132878,-1.612534,-0.701128,-0.884866,-1.071954,0.203631             -->  0
(760.) -1.001904,-1.2841,-1.34872,-1.535498,1.431733,1.060816                 -->  0
(761.) -0.380573,-0.26071,-0.349472,-0.939625,0.083594,0.815906               -->  0
(762.) -0.340719,-1.02393,-1.247797,-1.84556,-0.49418,0.448541                -->  0
(763.) -0.852185,-0.783667,-0.454007,-0.37595,-0.301589,-0.163733             -->  0
(764.) -0.230792,-2.375753,-1.818934,-1.511868,-2.420093,-1.020918            -->  0
(765.) -0.30256,-0.638529,-0.982341,-1.198479,0.468776,-0.531098              -->  0
(766.) -0.723919,0.267941,-0.629407,-0.778957,1.04655,-0.286188               -->  0
(767.) -0.196953,-1.240976,-2.656588,-2.236109,0.276185,-0.163733             -->  0
(768.) -2.104669,-0.619899,-1.223081,-1.02495,-1.071954,-1.755648             -->  0
(769.) -1.186712,-0.195063,-0.120831,-0.140215,0.853959,0.570996              -->  0
(770.) -0.340719,-1.953542,-1.014758,-1.081676,-0.879363,0.203631             -->  0
(771.) -0.666067,-1.089577,-0.319662,-0.805669,-0.108998,0.693451             -->  0
(772.) -0.073078,-1.240976,-1.339523,-1.052877,-0.49418,-1.143373             -->  0
(773.) -0.10248,-1.852797,-1.654925,-1.173904,-0.301589,-1.510738             -->  0
(774.) -0.164344,-1.953542,-1.58211,-1.096421,0.083594,-1.020918              -->  0
(775.) -0.265958,-1.124675,-1.896209,-2.236109,-0.108998,0.326086             -->  0
(776.) 0.15549,-0.806883,-1.330411,-1.720418,-1.071954,-0.286188              -->  0
(777.) -0.422281,-1.546886,-1.587977,-1.341915,-1.071954,-2.612832            -->  0
(778.) -0.265958,-1.02393,-0.441011,-0.624205,-1.264545,-0.163733             -->  0
(779.) -0.512009,-1.05604,-0.75538,-0.615344,-0.301589,-0.531098              -->  0
(780.) -0.380573,-1.2841,-0.693955,-0.708036,-0.879363,-0.776008              -->  0
(781.) -0.723919,0.164761,-0.124841,0.154678,0.661368,-0.653553               -->  0
(782.) -0.265958,-0.455234,-0.750323,-0.297754,0.468776,0.081176              -->  0
(783.) -0.512009,-1.200184,-0.58789,-1.126637,-2.612685,-2.123013             -->  0
(784.) -0.512009,-1.378532,-0.494053,-0.693524,0.276185,0.938361              -->  0
(785.) -0.265958,-1.486497,-0.710773,-0.747892,-0.879363,-1.633193            -->  0
(786.) -0.611721,-2.5928,-2.453482,-2.40412,-1.457137,-1.265828               -->  0
(787.) -1.384118,-0.096942,-1.605791,-0.372556,0.661368,-0.408643             -->  0
(788.) -0.164344,-0.761144,-0.505799,-1.663692,-1.071954,-0.898463            -->  0
(789.) -1.207985,-0.993131,-0.73035,-0.519136,1.239142,-0.653553              -->  0
(790.) -0.340719,-0.935066,-1.144888,-1.142125,-0.49418,-0.898463             -->  0
(791.) -0.196953,-1.684442,-1.455966,-1.705906,-1.842319,-0.776008            -->  0
(792.) -0.30256,-1.612534,-0.708353,-0.660525,-1.264545,-1.020918             -->  0
(793.) -1.001904,-1.161485,-0.199962,0.074844,-0.301589,-0.163733             -->  0
(794.) -0.132878,-1.763933,-1.235362,-1.103882,-1.649728,-0.041278            -->  0
(795.) -0.611721,-1.089577,-0.376746,-1.165856,-0.879363,-1.143373            -->  0
(796.) -0.230792,-1.378532,-1.508846,-1.572119,1.239142,0.693451              -->  0
(797.) -0.785761,-0.65763,-0.334455,-0.428422,0.276185,-0.531098              -->  0
(798.) -0.512009,-1.05604,-0.969666,-0.794891,-0.49418,0.448541               -->  0
(799.) -0.044609,-2.375753,-1.661242,-1.488829,-0.879363,-0.408643            -->  0
(800.) -0.466024,-1.612534,-2.656588,-2.40412,0.661368,1.183271               -->  0
(801.) -2.320987,-1.32984,-1.264625,-0.844417,0.083594,-2.123013              -->  0
(802.) -1.390377,-1.124675,-0.609523,-0.890792,0.661368,0.815906              -->  0
(803.) -0.30256,-0.855575,-2.216074,-2.648968,-1.842319,0.448541              -->  0
(804.) -0.56048,-0.638529,-0.201409,0.337859,-0.108998,0.326086               -->  0
(805.) -0.340719,-1.430585,-0.873725,-1.004547,0.661368,-2.735287             -->  0
(806.) -0.611721,-2.207399,-1.768224,-1.879694,-1.071954,-1.633193            -->  0
(807.) -0.723919,-0.601718,-0.392425,-0.313507,-0.49418,-0.163733             -->  0
(808.) -1.001904,-0.358196,-0.527703,-0.655906,0.468776,-0.408643             -->  0
(809.) -0.785761,-1.240976,-0.638374,-0.978027,-0.686771,-1.755648            -->  0
(810.) -1.001904,-0.485416,-0.554231,-0.646737,0.468776,-0.163733             -->  0
(811.) -1.001904,-1.684442,-0.331149,-0.688737,-0.301589,-1.020918            -->  0
(812.) -1.087314,-0.500973,-0.223363,-0.156149,0.468776,0.203631              -->  0
(813.) -0.611721,-0.697348,-1.093615,-0.669834,-1.649728,-2.612832            -->  0
(814.) -0.666067,-1.763933,-2.3465,-2.467698,-0.879363,0.326086               -->  0
(815.) -0.852185,-1.2841,-1.079441,-1.126637,-1.264545,0.448541               -->  0
(816.) -0.723919,-0.619899,-0.541899,-1.215234,-1.071954,-0.653553            -->  0
(817.) -0.723919,-0.806883,-0.581491,-0.523116,1.624324,0.815906              -->  0
(818.) -0.611721,-1.953542,-1.719989,-1.735162,-1.457137,-2.245467            -->  0
(819.) -0.30256,-0.134673,-0.950954,-1.828956,-0.686771,0.448541              -->  0
(820.) -0.666067,-1.200184,-0.562539,-0.476448,0.083594,0.326086              -->  0
(821.) -0.56048,-1.763933,-0.802095,-1.02495,-0.301589,0.203631               -->  0
(822.) -0.611721,-0.144409,0.176501,-0.396582,-1.842319,-1.265828             -->  0
(823.) -0.422281,-1.161485,-0.834511,-0.669834,-0.49418,-0.653553             -->  0
(824.) -0.56048,-2.207399,-1.811528,-1.477522,0.083594,-1.633193              -->  0
(825.) -0.512009,-1.684442,-1.733532,-1.206819,-0.49418,-0.408643             -->  0
(826.) -0.852185,-1.05604,-0.003944,-0.197234,0.083594,1.060816               -->  0
(827.) -0.852185,-1.953542,-0.765572,-1.173904,-4.346006,-2.980197            -->  0
(828.) -1.001904,-0.935066,-1.376834,-1.705906,-0.49418,-0.408643             -->  0
(829.) -0.852185,-0.855575,-0.431832,-0.861535,0.083594,-0.776008             -->  0
(830.) -1.311075,-0.830836,-0.525692,-0.096509,0.276185,-0.531098             -->  0
(831.) -1.683435,-1.378532,-1.833913,-1.477522,1.624324,0.203631              -->  0
(832.) -0.380573,-1.486497,-1.420564,-1.65004,-2.034911,-2.612832             -->  0
(833.) -0.723919,-1.2841,-1.183212,-1.361522,-0.686771,-0.163733              -->  0
(834.) -0.666067,-1.05604,-0.457752,-0.487895,-1.457137,-1.510738             -->  0
(835.) -1.099039,-1.684442,-0.486299,-0.737765,-0.686771,-2.367922            -->  0
(836.) -1.115531,-0.371318,0.003143,-0.140215,-1.071954,-0.653553             -->  0
(837.) -1.147536,-2.069843,-1.34872,-0.827611,-0.108998,-0.898463             -->  0
(838.) -0.466024,-1.02393,-1.503429,-1.84556,-0.686771,0.693451               -->  0
(839.) -0.852185,-1.089577,-0.2293,-0.984586,-1.071954,-0.776008              -->  0
(840.) -1.478763,-1.32984,-1.214977,-0.838781,-1.649728,0.203631              -->  0
(841.) -0.466024,-1.430585,-0.698731,-1.547544,-2.420093,-2.245467            -->  0
(842.) -0.723919,-1.612534,-1.055115,-1.157877,-1.649728,0.326086             -->  0
(843.) -0.56048,-2.5928,-1.804178,-1.623327,-0.301589,-1.633193               -->  0
(844.) -0.512009,-1.953542,-1.719989,-1.371485,-0.301589,-0.286188            -->  0
(845.) -0.466024,-0.935066,-1.420564,-1.2323,0.083594,-1.388283               -->  0
(846.) -1.001904,-1.612534,-0.885221,-1.351667,-0.49418,0.570996              -->  0
(847.) -0.785761,-2.069843,-1.093615,-0.90276,-0.686771,-0.408643             -->  0
(848.) -1.001904,-0.65763,-0.174283,-0.763293,-0.879363,-0.898463             -->  0
(849.) -0.666067,-1.763933,-1.558984,-1.584657,-0.686771,-0.041278            -->  0
(850.) -0.666067,-2.5928,-1.740374,-2.609749,-1.457137,-0.408643              -->  0
(851.) -0.380573,-1.763933,-2.728519,-3.10644,-0.879363,0.203631              -->  0
(852.) -0.923924,-1.852797,-1.435581,-1.796619,-1.071954,-0.776008            -->  0
(853.) -0.666067,-1.02393,-1.789639,-1.623327,-0.301589,-0.163733             -->  0
(854.) -0.666067,-2.5928,-3.138741,-3.174731,-0.879363,0.938361               -->  0
(855.) -1.722595,-0.830836,-0.560456,-0.568077,0.468776,0.570996              -->  0
(856.) -1.155236,-1.612534,-1.100779,-0.693524,0.468776,0.326086              -->  0
(857.) -1.001904,-1.612534,-1.849123,-2.316291,-0.108998,0.326086             -->  0
(858.) -5.313454,-2.89871,-2.639394,-0.878977,1.04655,0.448541                -->  0
(859.) -1.686925,-0.806883,-0.768136,-0.188869,-0.301589,-0.408643            -->  0
(860.) -1.109082,-1.161485,-0.585752,-1.198479,-0.108998,-0.531098            -->  0
(861.) -1.143711,-1.200184,-2.439459,-3.10644,0.083594,0.326086               -->  0
(862.) -1.087314,-1.378532,-1.410678,-1.84556,0.468776,-0.041278              -->  0
(863.) -1.329666,-1.2841,-0.238274,-0.153474,-0.49418,-0.408643               -->  0
(864.) -0.785761,-1.953542,-2.162038,-2.467698,-1.457137,-0.531098            -->  0
(865.) -1.087314,-1.852797,-0.957152,-1.096421,-0.49418,1.305726              -->  0
(866.) -0.852185,-2.207399,-1.796882,-2.609749,-1.457137,-1.510738            -->  0
(867.) -0.923924,-1.763933,-2.141224,-2.139019,-1.457137,-3.225107            -->  0
(868.) -1.304201,-2.5928,-2.766548,-2.435361,-2.227502,-3.592472              -->  0
(869.) -1.879246,-0.283926,-1.219021,-0.461402,-0.108998,-0.286188            -->  0
(870.) -2.587342,-1.2841,-3.138741,-2.501211,0.468776,-0.531098               -->  0
(871.) -0.923924,-1.05604,-0.81817,-1.2323,-0.879363,-0.286188                -->  0
(872.) -0.852185,-0.144409,-0.665774,-1.584657,0.276185,0.570996              -->  0
(873.) -1.001904,-3.421667,-2.511653,-2.648968,-0.879363,0.326086             -->  0
(874.) -0.852185,-1.200184,-0.773285,-0.535162,-2.997867,-1.510738            -->  0
(875.) -1.174778,-2.069843,-1.141136,-1.597368,-3.960824,-3.714927            -->  0
(876.) -0.852185,-1.953542,-1.195004,-1.371485,-1.071954,0.203631             -->  0
(877.) -0.785761,-2.89871,-3.138741,-2.927523,-1.071954,-1.388283             -->  0
(878.) -1.37296,-0.398266,-0.765572,-1.004547,-0.49418,-0.041278              -->  0
(879.) -1.001904,-2.5928,-1.43055,-1.004547,-0.108998,-0.653553               -->  0
(880.) -1.29061,-1.486497,-0.941729,-0.597874,-1.071954,-1.388283             -->  0
(881.) -0.611721,-1.852797,-1.761188,-1.332266,0.276185,-0.041278             -->  0
(882.) -0.666067,-1.32984,-2.847296,-3.10644,-0.108998,-0.408643              -->  0
(883.) -1.329666,-2.069843,-1.30357,-1.65004,-0.879363,-2.000558              -->  0
(884.) -0.723919,-0.470174,-0.69634,-1.223728,-1.457137,-1.265828             -->  0
(885.) -1.001904,-0.533083,-0.533762,-0.624205,0.083594,-0.898463             -->  0
(886.) -0.611721,-1.546886,-1.235362,-1.572119,-1.649728,-1.388283            -->  0



Time taken to build model (full training data) : 0.05 seconds

=== Model and evaluation on training set ===

Clustered Instances

0      887 (100%)

````

## dbscan_encabezado.png

Ruta: `Final/reports/weka/dbscan_encabezado.png` · Bytes: 634116 · SHA-256: `49e5a296f7a1c62729338f28b9edcf8de4378e0a70b74c60343d02d3eff68305`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## dbscan_paquete_instalado.png

Ruta: `Final/reports/weka/dbscan_paquete_instalado.png` · Bytes: 744567 · SHA-256: `d116101ee2b08af4959b56657aceebbc52e1708afbe6c2cfef50ec082b55761f`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## dbscan_paquete_pendiente.png

Ruta: `Final/reports/weka/dbscan_paquete_pendiente.png` · Bytes: 231387 · SHA-256: `14033da787cdd22635bd48f4c77c183cabfefa0d30a7d0a98177dea2995b79f6`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## dbscan_parametros.png

Ruta: `Final/reports/weka/dbscan_parametros.png` · Bytes: 193074 · SHA-256: `0893afea5b536cf905d0d8d1d2a212e68370679a22cc5ab5d25d1d83b5ccaa3e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## dbscan_resultado.png

Ruta: `Final/reports/weka/dbscan_resultado.png` · Bytes: 955565 · SHA-256: `a5b1fd50d6f42054ceff60a26a5528d8813b86d1efebff71e5d0053d85f30ee2`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## ejecucion.json

Ruta: `Final/reports/weka/ejecucion.json` · Bytes: 2118 · SHA-256: `2201928e6ce9a51ec63c47386436056bcf8ae31ff2c6a77027e43d76fd52604a`

````text
{
  "java": "openjdk version \"25.0.3\" 2026-04-21 LTS\nOpenJDK Runtime Environment Temurin-25.0.3+9 (build 25.0.3+9-LTS)\nOpenJDK 64-Bit Server VM Temurin-25.0.3+9 (build 25.0.3+9-LTS, mixed mode, sharing)",
  "sha256_dataset_depurado": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "comandos": [
    [
      "java",
      "-Dweka.packageManager.offline=true",
      "-DWEKA_HOME=.cache/weka/home",
      "-cp",
      ".cache/weka/*",
      "weka.clusterers.SimpleKMeans",
      "-t",
      "data/clean/clustering_weka.arff",
      "-N",
      "2",
      "-S",
      "42",
      "-I",
      "300",
      "-init",
      "1",
      "-A",
      "weka.core.EuclideanDistance -D",
      "-p",
      "0"
    ],
    [
      "java",
      "-Dweka.packageManager.offline=true",
      "-DWEKA_HOME=.cache/weka/home",
      "-cp",
      ".cache/weka/*",
      "weka.clusterers.SimpleKMeans",
      "-t",
      "data/clean/clustering_weka.arff",
      "-N",
      "3",
      "-S",
      "42",
      "-I",
      "300",
      "-init",
      "1",
      "-A",
      "weka.core.EuclideanDistance -D",
      "-p",
      "0"
    ],
    [
      "java",
      "-Dweka.packageManager.offline=true",
      "-DWEKA_HOME=.cache/weka/home",
      "-cp",
      ".cache/weka/*",
      "weka.clusterers.SimpleKMeans",
      "-t",
      "data/clean/clustering_weka.arff",
      "-N",
      "4",
      "-S",
      "42",
      "-I",
      "300",
      "-init",
      "1",
      "-A",
      "weka.core.EuclideanDistance -D",
      "-p",
      "0"
    ]
  ],
  "sha256_arff": "78e7c49499f1f2112d22a991a5edcc0400b5778fe7413011b71413c34433aea7",
  "jars": {
    "weka-stable-3.8.6.jar": {
      "url": "https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/weka-stable/3.8.6/weka-stable-3.8.6.jar",
      "sha256": "932ea2f342b58fe45736389e9c426d5b5955e610d1f5f6485117f532068915e9"
    },
    "bounce-0.18.jar": {
      "url": "https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/thirdparty/bounce/0.18/bounce-0.18.jar",
      "sha256": "bffff1505335c02256b7ab2ccffbe4aa4d3ac9fe14c17557809b7c9d99d666ca"
    }
  }
}
````

## error_csv_sin_origen.png

Ruta: `Final/reports/weka/error_csv_sin_origen.png` · Bytes: 38368 · SHA-256: `8f603c2c51a0c9cd5fb7983e98c5e1c11128890657a09a6e063d1f424f59e077`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## estado_antes_cierre.jpg

Ruta: `Final/reports/weka/estado_antes_cierre.jpg` · Bytes: 367766 · SHA-256: `4abf224a8f1570b588c2c9491c3b3db787e3d4fa05322d15994b7bd185bdd91d`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## gui_chooser_3_8_7.png

Ruta: `Final/reports/weka/gui_chooser_3_8_7.png` · Bytes: 119632 · SHA-256: `48b27f446204ea43447766801f0467df5441e8d20d5a78215220f503326944a9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## k2_asignaciones.csv

Ruta: `Final/reports/weka/k2_asignaciones.csv` · Bytes: 25869 · SHA-256: `6011fea6e55d662fbc2f367280161352f207d47c1c00f6e9e469641c01739be9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## k2_stderr.txt

Ruta: `Final/reports/weka/k2_stderr.txt` · Bytes: 0 · SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````text

````

## k2_stdout.txt

Ruta: `Final/reports/weka/k2_stdout.txt` · Bytes: 6238 · SHA-256: `a64f49b86a8e56c6abcb5a5dcc39d8e58c8c24ce1c51d181b648975e77f8cd34`

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

## k3_asignaciones.csv

Ruta: `Final/reports/weka/k3_asignaciones.csv` · Bytes: 25869 · SHA-256: `3a6a05c3e79f47d3c4858dfe61a2444abd406684590fb498fa79594b7246546d`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## k3_stderr.txt

Ruta: `Final/reports/weka/k3_stderr.txt` · Bytes: 0 · SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````text

````

## k3_stdout.txt

Ruta: `Final/reports/weka/k3_stdout.txt` · Bytes: 6238 · SHA-256: `c2ab96b9573386de5db92f96b1715774fea55fd2afe31bfd2bfc2bd778b82d1d`

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
8 0 
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
75 0 
76 1 
77 1 
78 1 
79 1 
80 1 
81 1 
82 1 
83 1 
84 0 
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
99 2 
100 1 
101 0 
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
112 0 
113 1 
114 1 
115 1 
116 1 
117 1 
118 1 
119 1 
120 1 
121 0 
122 1 
123 1 
124 1 
125 0 
126 1 
127 0 
128 1 
129 1 
130 1 
131 1 
132 1 
133 1 
134 1 
135 1 
136 1 
137 0 
138 1 
139 1 
140 0 
141 1 
142 0 
143 1 
144 1 
145 1 
146 1 
147 1 
148 1 
149 1 
150 1 
151 0 
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
169 0 
170 1 
171 0 
172 1 
173 1 
174 1 
175 0 
176 1 
177 1 
178 1 
179 1 
180 1 
181 1 
182 0 
183 0 
184 1 
185 0 
186 0 
187 1 
188 1 
189 1 
190 0 
191 0 
192 1 
193 1 
194 1 
195 0 
196 1 
197 1 
198 1 
199 1 
200 1 
201 0 
202 0 
203 1 
204 1 
205 1 
206 1 
207 0 
208 1 
209 0 
210 1 
211 1 
212 1 
213 1 
214 0 
215 0 
216 0 
217 1 
218 0 
219 0 
220 0 
221 1 
222 1 
223 0 
224 0 
225 2 
226 0 
227 1 
228 0 
229 0 
230 0 
231 0 
232 1 
233 0 
234 1 
235 0 
236 0 
237 0 
238 2 
239 1 
240 0 
241 0 
242 0 
243 0 
244 1 
245 0 
246 1 
247 0 
248 0 
249 1 
250 2 
251 1 
252 0 
253 0 
254 1 
255 0 
256 0 
257 1 
258 0 
259 1 
260 0 
261 0 
262 0 
263 0 
264 0 
265 0 
266 0 
267 0 
268 0 
269 0 
270 0 
271 0 
272 0 
273 1 
274 0 
275 0 
276 0 
277 0 
278 1 
279 1 
280 1 
281 1 
282 1 
283 0 
284 1 
285 1 
286 1 
287 0 
288 1 
289 1 
290 1 
291 1 
292 0 
293 0 
294 0 
295 0 
296 1 
297 0 
298 0 
299 0 
300 1 
301 1 
302 1 
303 0 
304 0 
305 1 
306 0 
307 0 
308 0 
309 0 
310 0 
311 0 
312 0 
313 2 
314 0 
315 0 
316 1 
317 0 
318 0 
319 2 
320 2 
321 1 
322 0 
323 1 
324 0 
325 1 
326 0 
327 0 
328 0 
329 0 
330 1 
331 0 
332 0 
333 0 
334 0 
335 0 
336 1 
337 2 
338 1 
339 2 
340 0 
341 0 
342 0 
343 0 
344 1 
345 0 
346 0 
347 0 
348 0 
349 0 
350 0 
351 2 
352 2 
353 1 
354 2 
355 0 
356 0 
357 0 
358 0 
359 0 
360 0 
361 0 
362 0 
363 0 
364 0 
365 2 
366 0 
367 0 
368 0 
369 0 
370 0 
371 0 
372 0 
373 0 
374 2 
375 0 
376 2 
377 0 
378 0 
379 2 
380 0 
381 2 
382 0 
383 0 
384 2 
385 0 
386 0 
387 0 
388 2 
389 0 
390 0 
391 0 
392 0 
393 1 
394 2 
395 0 
396 2 
397 0 
398 0 
399 0 
400 0 
401 2 
402 0 
403 0 
404 0 
405 2 
406 0 
407 0 
408 0 
409 2 
410 0 
411 0 
412 0 
413 0 
414 0 
415 0 
416 0 
417 0 
418 0 
419 0 
420 0 
421 0 
422 2 
423 2 
424 0 
425 0 
426 2 
427 2 
428 0 
429 2 
430 0 
431 2 
432 2 
433 0 
434 2 
435 0 
436 0 
437 0 
438 2 
439 0 
440 0 
441 0 
442 2 
443 2 
444 0 
445 2 
446 0 
447 0 
448 0 
449 0 
450 0 
451 0 
452 2 
453 2 
454 2 
455 0 
456 0 
457 1 
458 1 
459 1 
460 1 
461 1 
462 1 
463 1 
464 1 
465 0 
466 1 
467 1 
468 1 
469 1 
470 0 
471 1 
472 1 
473 0 
474 0 
475 0 
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
486 0 
487 1 
488 1 
489 1 
490 1 
491 1 
492 0 
493 1 
494 0 
495 0 
496 2 
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
507 2 
508 1 
509 1 
510 1 
511 1 
512 1 
513 1 
514 1 
515 0 
516 1 
517 1 
518 1 
519 1 
520 2 
521 0 
522 1 
523 0 
524 1 
525 0 
526 0 
527 1 
528 1 
529 0 
530 0 
531 1 
532 0 
533 0 
534 0 
535 1 
536 0 
537 0 
538 0 
539 0 
540 0 
541 0 
542 1 
543 1 
544 1 
545 0 
546 1 
547 0 
548 0 
549 1 
550 0 
551 1 
552 1 
553 1 
554 0 
555 0 
556 1 
557 0 
558 0 
559 0 
560 0 
561 1 
562 0 
563 0 
564 0 
565 0 
566 0 
567 2 
568 1 
569 0 
570 0 
571 0 
572 1 
573 0 
574 0 
575 1 
576 1 
577 0 
578 0 
579 0 
580 0 
581 0 
582 0 
583 0 
584 0 
585 2 
586 0 
587 0 
588 0 
589 1 
590 0 
591 1 
592 0 
593 0 
594 0 
595 1 
596 0 
597 0 
598 0 
599 0 
600 0 
601 0 
602 0 
603 0 
604 2 
605 0 
606 1 
607 0 
608 1 
609 0 
610 0 
611 0 
612 1 
613 0 
614 0 
615 0 
616 2 
617 0 
618 0 
619 0 
620 0 
621 0 
622 0 
623 0 
624 2 
625 0 
626 1 
627 0 
628 2 
629 0 
630 0 
631 0 
632 0 
633 0 
634 2 
635 0 
636 0 
637 1 
638 0 
639 0 
640 0 
641 2 
642 0 
643 2 
644 0 
645 0 
646 0 
647 0 
648 0 
649 0 
650 0 
651 0 
652 0 
653 0 
654 0 
655 0 
656 0 
657 0 
658 0 
659 2 
660 0 
661 0 
662 0 
663 0 
664 0 
665 0 
666 0 
667 0 
668 0 
669 0 
670 2 
671 0 
672 0 
673 0 
674 0 
675 0 
676 0 
677 0 
678 2 
679 2 
680 2 
681 2 
682 0 
683 0 
684 0 
685 0 
686 0 
687 2 
688 0 
689 2 
690 0 
691 0 
692 0 
693 2 
694 0 
695 0 
696 0 
697 0 
698 2 
699 2 
700 0 
701 0 
702 2 
703 2 
704 0 
705 0 
706 2 
707 2 
708 0 
709 2 
710 0 
711 0 
712 0 
713 0 
714 2 
715 0 
716 0 
717 2 
718 0 
719 0 
720 0 
721 0 
722 0 
723 2 
724 2 
725 2 
726 2 
727 0 
728 2 
729 0 
730 0 
731 2 
732 0 
733 0 
734 2 
735 0 
736 2 
737 0 
738 2 
739 2 
740 2 
741 2 
742 0 
743 0 
744 2 
745 2 
746 0 
747 2 
748 2 
749 0 
750 0 
751 0 
752 0 
753 0 
754 0 
755 0 
756 2 
757 0 
758 2 
759 2 
760 0 
761 0 
762 2 
763 0 
764 2 
765 0 
766 0 
767 2 
768 2 
769 0 
770 2 
771 0 
772 2 
773 2 
774 2 
775 2 
776 2 
777 2 
778 2 
779 2 
780 2 
781 0 
782 0 
783 2 
784 0 
785 2 
786 2 
787 0 
788 2 
789 0 
790 2 
791 2 
792 2 
793 0 
794 2 
795 2 
796 0 
797 0 
798 0 
799 2 
800 2 
801 2 
802 0 
803 2 
804 0 
805 2 
806 2 
807 0 
808 0 
809 2 
810 0 
811 2 
812 0 
813 2 
814 2 
815 2 
816 2 
817 0 
818 2 
819 2 
820 0 
821 2 
822 2 
823 2 
824 2 
825 2 
826 0 
827 2 
828 2 
829 0 
830 0 
831 2 
832 2 
833 2 
834 2 
835 2 
836 0 
837 2 
838 2 
839 2 
840 2 
841 2 
842 2 
843 2 
844 2 
845 2 
846 2 
847 2 
848 2 
849 2 
850 2 
851 2 
852 2 
853 2 
854 2 
855 0 
856 2 
857 2 
858 2 
859 2 
860 2 
861 2 
862 2 
863 2 
864 2 
865 2 
866 2 
867 2 
868 2 
869 2 
870 2 
871 2 
872 0 
873 2 
874 2 
875 2 
876 2 
877 2 
878 2 
879 2 
880 2 
881 2 
882 2 
883 2 
884 2 
885 0 
886 2 


````

## k4_asignaciones.csv

Ruta: `Final/reports/weka/k4_asignaciones.csv` · Bytes: 25869 · SHA-256: `eade2a070ff467864e387e3e9dc620726ba815f21eb21978d4487d78e3fa68e6`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## k4_stderr.txt

Ruta: `Final/reports/weka/k4_stderr.txt` · Bytes: 0 · SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````text

````

## k4_stdout.txt

Ruta: `Final/reports/weka/k4_stdout.txt` · Bytes: 6238 · SHA-256: `9f2835ace5f2bf0ca9489e65d77c183baf02ce4cfed7bcce2d60cdb855f13387`

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
8 2 
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
37 2 
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
56 2 
57 1 
58 1 
59 0 
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
75 2 
76 1 
77 1 
78 1 
79 1 
80 1 
81 1 
82 1 
83 0 
84 0 
85 1 
86 0 
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
99 2 
100 1 
101 2 
102 1 
103 1 
104 1 
105 2 
106 1 
107 1 
108 1 
109 1 
110 1 
111 1 
112 0 
113 1 
114 1 
115 1 
116 1 
117 1 
118 1 
119 0 
120 1 
121 2 
122 1 
123 1 
124 1 
125 2 
126 0 
127 2 
128 1 
129 1 
130 1 
131 1 
132 0 
133 1 
134 1 
135 1 
136 1 
137 2 
138 1 
139 1 
140 0 
141 1 
142 2 
143 1 
144 1 
145 1 
146 1 
147 1 
148 1 
149 1 
150 1 
151 0 
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
164 2 
165 1 
166 1 
167 1 
168 1 
169 2 
170 1 
171 2 
172 1 
173 1 
174 1 
175 0 
176 1 
177 1 
178 1 
179 1 
180 1 
181 1 
182 2 
183 0 
184 1 
185 2 
186 2 
187 1 
188 1 
189 1 
190 2 
191 0 
192 1 
193 1 
194 1 
195 0 
196 1 
197 1 
198 1 
199 2 
200 1 
201 0 
202 2 
203 1 
204 0 
205 1 
206 1 
207 2 
208 1 
209 2 
210 2 
211 2 
212 1 
213 1 
214 2 
215 2 
216 2 
217 1 
218 0 
219 2 
220 0 
221 0 
222 1 
223 2 
224 2 
225 3 
226 0 
227 1 
228 2 
229 2 
230 2 
231 2 
232 1 
233 2 
234 1 
235 0 
236 0 
237 0 
238 3 
239 1 
240 2 
241 0 
242 0 
243 2 
244 1 
245 2 
246 1 
247 0 
248 2 
249 1 
250 3 
251 1 
252 2 
253 2 
254 0 
255 0 
256 2 
257 1 
258 2 
259 1 
260 0 
261 2 
262 0 
263 2 
264 2 
265 2 
266 2 
267 2 
268 2 
269 2 
270 0 
271 2 
272 0 
273 1 
274 0 
275 0 
276 0 
277 2 
278 1 
279 1 
280 1 
281 1 
282 1 
283 2 
284 1 
285 1 
286 1 
287 0 
288 1 
289 1 
290 1 
291 1 
292 2 
293 2 
294 0 
295 0 
296 1 
297 2 
298 0 
299 0 
300 0 
301 1 
302 1 
303 2 
304 0 
305 1 
306 0 
307 0 
308 2 
309 0 
310 0 
311 0 
312 2 
313 3 
314 0 
315 0 
316 1 
317 0 
318 2 
319 3 
320 2 
321 1 
322 2 
323 0 
324 2 
325 0 
326 0 
327 0 
328 0 
329 2 
330 1 
331 0 
332 0 
333 2 
334 2 
335 2 
336 1 
337 3 
338 1 
339 3 
340 2 
341 0 
342 0 
343 0 
344 1 
345 0 
346 2 
347 2 
348 2 
349 2 
350 2 
351 3 
352 3 
353 0 
354 3 
355 2 
356 2 
357 2 
358 2 
359 0 
360 2 
361 0 
362 0 
363 2 
364 2 
365 0 
366 0 
367 0 
368 2 
369 0 
370 0 
371 2 
372 2 
373 0 
374 3 
375 0 
376 3 
377 2 
378 0 
379 3 
380 0 
381 3 
382 2 
383 0 
384 3 
385 0 
386 0 
387 2 
388 3 
389 2 
390 2 
391 0 
392 2 
393 0 
394 3 
395 0 
396 3 
397 0 
398 0 
399 0 
400 0 
401 3 
402 0 
403 2 
404 2 
405 3 
406 0 
407 0 
408 0 
409 3 
410 0 
411 2 
412 0 
413 2 
414 0 
415 0 
416 2 
417 0 
418 2 
419 0 
420 2 
421 2 
422 3 
423 3 
424 0 
425 0 
426 3 
427 3 
428 0 
429 3 
430 2 
431 3 
432 3 
433 0 
434 3 
435 0 
436 2 
437 0 
438 3 
439 0 
440 0 
441 2 
442 3 
443 3 
444 2 
445 3 
446 0 
447 2 
448 0 
449 2 
450 0 
451 2 
452 3 
453 3 
454 3 
455 2 
456 2 
457 1 
458 1 
459 1 
460 1 
461 1 
462 1 
463 2 
464 1 
465 2 
466 1 
467 1 
468 1 
469 1 
470 0 
471 1 
472 1 
473 0 
474 2 
475 2 
476 1 
477 1 
478 0 
479 1 
480 0 
481 1 
482 1 
483 1 
484 1 
485 1 
486 2 
487 1 
488 0 
489 2 
490 1 
491 1 
492 2 
493 1 
494 2 
495 2 
496 2 
497 1 
498 2 
499 1 
500 1 
501 1 
502 1 
503 1 
504 1 
505 0 
506 1 
507 2 
508 1 
509 1 
510 1 
511 1 
512 1 
513 1 
514 1 
515 2 
516 0 
517 1 
518 1 
519 1 
520 3 
521 2 
522 1 
523 2 
524 1 
525 0 
526 2 
527 1 
528 0 
529 2 
530 2 
531 1 
532 0 
533 0 
534 0 
535 1 
536 2 
537 2 
538 2 
539 2 
540 2 
541 2 
542 0 
543 1 
544 1 
545 0 
546 2 
547 2 
548 2 
549 2 
550 2 
551 1 
552 0 
553 1 
554 2 
555 0 
556 1 
557 2 
558 2 
559 2 
560 0 
561 1 
562 2 
563 2 
564 2 
565 0 
566 0 
567 3 
568 1 
569 0 
570 0 
571 0 
572 1 
573 2 
574 0 
575 1 
576 0 
577 0 
578 2 
579 2 
580 2 
581 0 
582 0 
583 2 
584 2 
585 3 
586 2 
587 2 
588 0 
589 1 
590 2 
591 0 
592 0 
593 2 
594 0 
595 0 
596 2 
597 2 
598 0 
599 2 
600 2 
601 2 
602 2 
603 2 
604 3 
605 0 
606 0 
607 2 
608 0 
609 2 
610 0 
611 0 
612 0 
613 2 
614 0 
615 0 
616 3 
617 2 
618 0 
619 0 
620 2 
621 0 
622 2 
623 2 
624 3 
625 2 
626 0 
627 2 
628 3 
629 0 
630 2 
631 0 
632 2 
633 0 
634 3 
635 0 
636 2 
637 1 
638 0 
639 2 
640 2 
641 3 
642 0 
643 0 
644 2 
645 2 
646 0 
647 2 
648 0 
649 0 
650 2 
651 0 
652 0 
653 2 
654 2 
655 0 
656 2 
657 2 
658 3 
659 3 
660 0 
661 2 
662 2 
663 0 
664 0 
665 0 
666 2 
667 2 
668 2 
669 2 
670 3 
671 2 
672 0 
673 2 
674 0 
675 0 
676 2 
677 0 
678 3 
679 2 
680 2 
681 3 
682 0 
683 0 
684 2 
685 2 
686 2 
687 3 
688 2 
689 3 
690 0 
691 2 
692 2 
693 3 
694 2 
695 3 
696 2 
697 0 
698 2 
699 3 
700 0 
701 0 
702 3 
703 3 
704 0 
705 2 
706 2 
707 3 
708 2 
709 3 
710 2 
711 0 
712 2 
713 2 
714 3 
715 0 
716 2 
717 3 
718 3 
719 0 
720 0 
721 0 
722 0 
723 3 
724 3 
725 3 
726 3 
727 0 
728 3 
729 0 
730 2 
731 3 
732 0 
733 0 
734 2 
735 2 
736 3 
737 0 
738 2 
739 3 
740 3 
741 3 
742 0 
743 0 
744 3 
745 3 
746 0 
747 3 
748 3 
749 0 
750 3 
751 2 
752 0 
753 0 
754 0 
755 0 
756 3 
757 0 
758 3 
759 3 
760 0 
761 2 
762 3 
763 0 
764 3 
765 3 
766 0 
767 3 
768 3 
769 0 
770 3 
771 0 
772 3 
773 3 
774 3 
775 3 
776 3 
777 3 
778 2 
779 3 
780 3 
781 0 
782 0 
783 3 
784 0 
785 3 
786 3 
787 0 
788 3 
789 0 
790 3 
791 3 
792 3 
793 0 
794 3 
795 3 
796 0 
797 0 
798 3 
799 3 
800 3 
801 3 
802 0 
803 3 
804 0 
805 3 
806 3 
807 0 
808 0 
809 3 
810 0 
811 3 
812 0 
813 3 
814 3 
815 3 
816 3 
817 0 
818 3 
819 2 
820 0 
821 3 
822 2 
823 3 
824 3 
825 3 
826 0 
827 3 
828 3 
829 3 
830 0 
831 3 
832 3 
833 3 
834 3 
835 3 
836 0 
837 3 
838 3 
839 3 
840 3 
841 3 
842 3 
843 3 
844 3 
845 3 
846 3 
847 3 
848 3 
849 3 
850 3 
851 3 
852 3 
853 3 
854 3 
855 0 
856 3 
857 3 
858 3 
859 3 
860 3 
861 3 
862 3 
863 3 
864 3 
865 3 
866 3 
867 3 
868 3 
869 3 
870 3 
871 3 
872 0 
873 3 
874 3 
875 3 
876 3 
877 3 
878 3 
879 3 
880 3 
881 3 
882 3 
883 3 
884 3 
885 0 
886 3 


````

## kmeans.txt

Ruta: `Final/reports/weka/kmeans.txt` · Bytes: 1554 · SHA-256: `b6be17cf0eaf134d171be3850e8e4c683ef631592cb3e142195ae0358191983a`

````text
=== Run information ===

Scheme:       weka.clusterers.SimpleKMeans -init 0 -max-candidates 100 -periodic-pruning 10000 -min-density 2.0 -t1 -1.25 -t2 -1.0 -N 2 -A "weka.core.EuclideanDistance -R first-last" -I 500 -num-slots 1 -S 42
Relation:     clustering
Instances:    887
Attributes:   6
              Plays
              Playing
              Backlogs
              Wishlist
              Rating
              Metacritic Rating
Test mode:    evaluate on training data


=== Clustering model (full training set) ===


kMeans
======

Number of iterations: 9
Within cluster sum of squared errors: 76.63099068257982

Initial starting points (random):

Cluster 0: -0.196953,1.355243,0.909476,1.595141,0.276185,0.693451
Cluster 1: 0.261114,-0.830836,-0.259536,-0.237306,-1.264545,-0.531098

Missing values globally replaced with mean/mode

Final cluster centroids:
                                 Cluster#
Attribute            Full Data          0          1
                       (887.0)    (477.0)    (410.0)
====================================================
Plays                        0       0.41     -0.477
Playing                      0     0.6189      -0.72
Backlogs                     0     0.7093    -0.8252
Wishlist                    -0     0.6912    -0.8042
Rating                       0     0.4797    -0.5581
Metacritic Rating           -0      0.427    -0.4968




Time taken to build model (full training data) : 0.02 seconds

=== Model and evaluation on training set ===

Clustered Instances

0      477 ( 54%)
1      410 ( 46%)

````

## kmeans_parametros.png

Ruta: `Final/reports/weka/kmeans_parametros.png` · Bytes: 315719 · SHA-256: `02701adf007ea00754e5a08b072612409728475c99ad457ce314f52f1bd78f27`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## kmeans_resultado.png

Ruta: `Final/reports/weka/kmeans_resultado.png` · Bytes: 580823 · SHA-256: `a6f5223cb9b6f6d0cbeb70cc3da84f89396cd8fc68fa2195d4e8f7fc63548e00`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## leer_menu_ax.js

Ruta: `Final/reports/weka/leer_menu_ax.js` · Bytes: 1857 · SHA-256: `02f23f39da2f9f4edb082bedacf3d6c903efa26bf05867ce2662e9a50d19f4f6`

````text
// Lectura de accesibilidad limitada al proceso Weka autorizado.
ObjC.import('ApplicationServices');
function atributo(elemento, nombre) {
    var salida = Ref();
    var codigo = $.AXUIElementCopyAttributeValue(elemento, $(nombre), salida);
    return codigo === 0 ? salida[0] : null;
}
function cadena(valor) {
    if (valor === null) return '';
    try { return ObjC.unwrap(valor); } catch (e) { return ''; }
}
function recorrer(elemento, profundidad, salida) {
    if (profundidad > 12 || salida.length > 500) return;
    var rol = cadena(atributo(elemento, 'AXRole'));
    var titulo = cadena(atributo(elemento, 'AXTitle'));
    var descripcion = cadena(atributo(elemento, 'AXDescription'));
    var valor = cadena(atributo(elemento, 'AXValue'));
    salida.push({nivel: profundidad, rol: rol, titulo: titulo, descripcion: descripcion, valor: valor});
    var hijos = atributo(elemento, 'AXChildren');
    if (hijos) {
        for (var i = 0; i < Number(hijos.count); i++) recorrer(hijos.objectAtIndex(i), profundidad + 1, salida);
    }
}
function run() {
    var proceso = Application('System Events').processes.byName('weka-3.8.7');
    var sistema = Application('System Events');
    proceso.frontmost = true;
    delay(0.2);
    sistema.keyCode(53);
    var boton = proceso.windows.byName('Weka Explorer').tabGroups[0].buttons.whose({description: 'Choose'})[0];
    boton.attributes.byName('AXFocused').value = true;
    sistema.keyCode(49);
    delay(0.3);
    var aplicacion = $.AXUIElementCreateApplication(proceso.unixId());
    var ventanas = atributo(aplicacion, 'AXWindows');
    var salida = [];
    for (var i = 0; i < Number(ventanas.count); i++) {
        var ventana = ventanas.objectAtIndex(i);
        if (cadena(atributo(ventana, 'AXTitle')) === '') recorrer(ventana, 0, salida);
    }
    return JSON.stringify(salida, null, 2);
}

````

## manifiesto_evidencias_gui.json

Ruta: `Final/reports/weka/manifiesto_evidencias_gui.json` · Bytes: 9368 · SHA-256: `8e51f08ff5c121c789408e79f40796dfd02fdfb27fb6b1e4c99393e52a46a6c0`

````text
{
  "fecha": "2026-11-09T11:41:15.431069-06:00",
  "alcance": "Respaldo local de evidencias gráficas de Weka; sin resultados de Orange ni algoritmos CLI anteriores.",
  "archivos": [
    {
      "ruta": "reports/weka/kmeans.txt",
      "bytes": 1554,
      "sha256": "b6be17cf0eaf134d171be3850e8e4c683ef631592cb3e142195ae0358191983a"
    },
    {
      "ruta": "reports/weka/dbscan.txt",
      "bytes": 76228,
      "sha256": "7d0866476ee480a90daee39e1469861c532b52da9dbef7bfb9c05eedcf11de94"
    },
    {
      "ruta": "reports/weka/ZeroR.txt",
      "bytes": 3346,
      "sha256": "abc7807ce09733680834ddcfcbf72f7a71f72e62ad1d519db547385bc4fe1cad"
    },
    {
      "ruta": "reports/weka/NaiveBayes.txt",
      "bytes": 20846,
      "sha256": "5aac3e1f7f662eb504b71c7f77d1e31f2121a15ba7771c97b630a65bfd3027c6"
    },
    {
      "ruta": "reports/weka/J48.txt",
      "bytes": 17362,
      "sha256": "88ceace97d84c7c67628688f9876a4d3de22c07935e6111dd954f3c401a88c8c"
    },
    {
      "ruta": "reports/weka/RandomForest.txt",
      "bytes": 3521,
      "sha256": "bed5274c54f92bc20ff70c7d64d600839b65e76ea4860e88d8e003dcd5bb47df"
    },
    {
      "ruta": "reports/weka/kmeans_resultado.png",
      "bytes": 580823,
      "sha256": "a6f5223cb9b6f6d0cbeb70cc3da84f89396cd8fc68fa2195d4e8f7fc63548e00"
    },
    {
      "ruta": "reports/weka/dbscan_resultado.png",
      "bytes": 955565,
      "sha256": "a5b1fd50d6f42054ceff60a26a5528d8813b86d1efebff71e5d0053d85f30ee2"
    },
    {
      "ruta": "reports/weka/ZeroR.png",
      "bytes": 597808,
      "sha256": "b7859929328baea3540730ab9e0494eec18e983a56f8fb5d1c26ddb77f91766f"
    },
    {
      "ruta": "reports/weka/NaiveBayes.png",
      "bytes": 623033,
      "sha256": "ef00fe5af3442fbbaa129aeef2a23c3c42e642d69773f6924fd261ada6056928"
    },
    {
      "ruta": "reports/weka/J48.png",
      "bytes": 630962,
      "sha256": "72296d14f03af1520c8e07ca86310cb171b5a1b7f46b189701f3df514e184afd"
    },
    {
      "ruta": "reports/weka/RandomForest.png",
      "bytes": 675186,
      "sha256": "75fd874d38afb1b00f10cf700ec2a5adede66120ac7d87f702d4d0c7a6367d8c"
    },
    {
      "ruta": "reports/weka/kmeans_parametros.png",
      "bytes": 315719,
      "sha256": "02701adf007ea00754e5a08b072612409728475c99ad457ce314f52f1bd78f27"
    },
    {
      "ruta": "reports/weka/dbscan_parametros.png",
      "bytes": 193074,
      "sha256": "0893afea5b536cf905d0d8d1d2a212e68370679a22cc5ab5d25d1d83b5ccaa3e"
    },
    {
      "ruta": "reports/weka/dbscan_paquete_instalado.png",
      "bytes": 744567,
      "sha256": "d116101ee2b08af4959b56657aceebbc52e1708afbe6c2cfef50ec082b55761f"
    },
    {
      "ruta": "reports/weka/preprocess_887_6.png",
      "bytes": 328737,
      "sha256": "4a12b27fee62542fd9e54b8a1a0f0860013d9a9b9d17eadb01afc3cf06c17e9e"
    },
    {
      "ruta": "reports/weka/preprocess_clasificacion_892_53.png",
      "bytes": 474369,
      "sha256": "3528c55e62a3c2c4756a4c20a396350944a355ef5094a225e4023b394bf2da93"
    },
    {
      "ruta": "reports/weka/verificacion_final_ventana.png",
      "bytes": 925607,
      "sha256": "db55f2c6708c8697f387317f5753d787c2132ebcf87b75c995378729edd6cde4"
    },
    {
      "ruta": "reports/weka/resumen_gui.md",
      "bytes": 4663,
      "sha256": "f22bbd098d5928e5a0a0cbe41bc9f8aaea474a31d4bda0df47fd9cf1bc42ec79"
    },
    {
      "ruta": "reports/weka/verificacion_gui.json",
      "bytes": 3665,
      "sha256": "be902c717117cd70c74115abe9422a476a27290227664fa7c08563b005dbc584"
    },
    {
      "ruta": "reports/weka/clic_weka.js",
      "bytes": 1778,
      "sha256": "a18f25837076eaf480e513a9f0f678a35b2eaf9805b14458b690ba6f430755e1"
    },
    {
      "ruta": "reports/codex_log.md",
      "bytes": 41008,
      "sha256": "80327a2bc336276b80dfa348bf5fa60425122364968c66c5270d91e4d5054dce"
    },
    {
      "ruta": "reports/tables/comparativo_herramientas.csv",
      "bytes": 14198,
      "sha256": "16e8e53c939be9db1802c5da0d55f5c474484408a5b3dc5aa4f3ac5413066893"
    },
    {
      "ruta": "data/export/procedencia_arff.json",
      "bytes": 721,
      "sha256": "c4f04f6eb9a09996254dbcf51015019e1b522963fe3b284cb25a9a1a3bc8691c"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/kmeans_resultado.jpg",
      "bytes": 375510,
      "sha256": "0b8e0b0cbf449189b3e9e1003676ad081605321116834da5ee59b1346ff32af2"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/dbscan_resultado.jpg",
      "bytes": 632626,
      "sha256": "764cab40e6644b9f38d3db5e999cb46efa59847754796ab7af598f7e61c55839"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/ZeroR.jpg",
      "bytes": 369757,
      "sha256": "5bf5855dbbfabc490600a2b84b17daad9634618f25b6e7bc3d9379bb1ec6b322"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/NaiveBayes.jpg",
      "bytes": 388942,
      "sha256": "3183edf0097177d334337adae81965d64b6745681817a9130eee0e2a26c3db6f"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/J48.jpg",
      "bytes": 393832,
      "sha256": "2cf229718717fc3574bc2af3c45de908c0ddfc74a4273c560ebfdff745fbefa2"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/RandomForest.jpg",
      "bytes": 417861,
      "sha256": "17df8a4eb2e4bfc4b3fa628b4a94265ce9c36fd8c7d0922c4b938ea201bc86e6"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/kmeans_parametros.jpg",
      "bytes": 201718,
      "sha256": "2ff878e825f3e6fcb0055d9a40a69d57016a8074007afb72febc748b07414dfd"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/dbscan_parametros.jpg",
      "bytes": 127518,
      "sha256": "078094306545235ed1c67e4468cee9bad306737338cc4ebeb5d38395cfb61451"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/dbscan_paquete_instalado.jpg",
      "bytes": 488781,
      "sha256": "1555840562cc1419d058e30801225e554784bb42e370f0ff4dfa58a7d34d74e4"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/preprocess_887_6.jpg",
      "bytes": 281696,
      "sha256": "ddd1c3c24514a7ceca94436e617187d1a0612c22544d6c8df476dae5ad46df25"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/preprocess_clasificacion_892_53.jpg",
      "bytes": 338311,
      "sha256": "777b212a752b5a8e951352cf07a10fac9983ad477db5b92a6033994a7e60da47"
    },
    {
      "ruta": "reports/weka/capturas_originales_jpeg/verificacion_final_ventana.jpg",
      "bytes": 624234,
      "sha256": "521b7bdc5119b1c28295646d2e41cb7b242b0d994ce3a2e7fec17a7da82da6f0"
    },
    {
      "ruta": "reports/weka/conversion_capturas.json",
      "bytes": 5286,
      "sha256": "faa3a6f86b515d59e45a1f383580bf405eeeff13f3a68d45da111685d9d0b7bd"
    },
    {
      "ruta": "reports/weka/revision_respaldo.md",
      "bytes": 1849,
      "sha256": "c2ffa83066679bce6ccdbeeaffe992844b6a32d56ac1ef12e83adfcc64abc0ab"
    },
    {
      "ruta": "reports/weka/cierre_weka_2026_11_09.md",
      "bytes": 2000,
      "sha256": "cfe77d950e13a3887e238074f93ad985bd62fd9870a262c0d29cf23ff53ee1c4"
    },
    {
      "ruta": "reports/weka/auditoria_cierre_2026_11_09.json",
      "bytes": 1641,
      "sha256": "e40d7fd52f04c7f67a654c8f0cfe301d0e34bfedba7b8de7ddf424c99e539549"
    },
    {
      "ruta": "reports/weka/revision_explorer_2026_11_09.jpg",
      "bytes": 335490,
      "sha256": "c747aaf6b50600ba4fcc166df07612f40ed6e6b60ed5487be8ffd70d275703c4"
    },
    {
      "ruta": "reports/weka/verificacion_comparativo_python_weka.json",
      "bytes": 1469,
      "sha256": "a3bff1c6308093cdae72d550e90b2ae5d732d2565c15800bb0f3ec76545bcd30"
    },
    {
      "ruta": "reports/tables/comparativo_herramientas_notas.md",
      "bytes": 3850,
      "sha256": "04d42dea8485c335ebc0f0072228ff91cdf1b77a5168f6859d37e1ea8918ee31"
    },
    {
      "ruta": "reports/tables/evaluar_comparabilidad.py",
      "bytes": 8880,
      "sha256": "1f0c178f4dba03c4922e5cf948770211637a01e7d47a9044b2bbcd57af0178cd"
    },
    {
      "ruta": "reports/tables/test_comparabilidad.py",
      "bytes": 2664,
      "sha256": "844c10c6186a711cef430c8ac193c3241792482ee3e20e458c6cab824cd10f52"
    },
    {
      "ruta": "reports/tables/comparativo_detalle.json",
      "bytes": 31092,
      "sha256": "0316b13e1db7522ddaa97aa671c773f02f5116bf9096fbaef4334f0071d91304"
    },
    {
      "ruta": "reports/tables/comparativo_folds.csv",
      "bytes": 97207,
      "sha256": "4efe3a7a75dd2e00310a38045a9be880f4b289ab7be505e82e7fb05fc60dbd32"
    },
    {
      "ruta": "reports/tables/comparativo_predicciones_oof.csv",
      "bytes": 657427,
      "sha256": "70cbe0ea4d0175e36f9be3e23347f49a8bcf586227ea7bfcb4063adf7eab1822"
    },
    {
      "ruta": "reports/tables/ejecucion_comparabilidad.txt",
      "bytes": 1796,
      "sha256": "35889d1c98ea3ed200a69fcaf109c3021e4f824fec9bb8ab07c255558ccf35d0"
    },
    {
      "ruta": "reports/tables/pruebas_comparabilidad.txt",
      "bytes": 799,
      "sha256": "2b2ff65dae96389433ca6e86113f21e337d44b0cbe14599aff5e8acc17b21eee"
    },
    {
      "ruta": "reports/tables/pruebas_metricas_comparables.txt",
      "bytes": 99,
      "sha256": "d1860236036504b3d533e1a449db7d3961063c3f837f6e99c3ccfc5dfa504fe9"
    }
  ],
  "capturas": {
    "png_validos": 12,
    "jpeg_originales_conservados": 12,
    "igualdad_de_pixeles_verificada": true
  },
  "revision_cierre": "reports/weka/cierre_weka_2026_11_09.md"
}

````

## menu_clusterers_ax.json

Ruta: `Final/reports/weka/menu_clusterers_ax.json` · Bytes: 3 · SHA-256: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`

````text
[]

````

## preprocess_887_6.png

Ruta: `Final/reports/weka/preprocess_887_6.png` · Bytes: 328737 · SHA-256: `4a12b27fee62542fd9e54b8a1a0f0860013d9a9b9d17eadb01afc3cf06c17e9e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## preprocess_clasificacion_892_53.png

Ruta: `Final/reports/weka/preprocess_clasificacion_892_53.png` · Bytes: 474369 · SHA-256: `3528c55e62a3c2c4756a4c20a396350944a355ef5094a225e4023b394bf2da93`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## revision_explorer_2026_11_09.jpg

Ruta: `Final/reports/weka/revision_explorer_2026_11_09.jpg` · Bytes: 335490 · SHA-256: `c747aaf6b50600ba4fcc166df07612f40ed6e6b60ed5487be8ffd70d275703c4`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## selector_csv_pendiente.png

Ruta: `Final/reports/weka/selector_csv_pendiente.png` · Bytes: 125317 · SHA-256: `4c9736fb48c9067662f1f960e6cb291e5416ef730a95ed3e369e4a35140420f1`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## verificacion_comparativo_python_weka.json

Ruta: `Final/reports/weka/verificacion_comparativo_python_weka.json` · Bytes: 1469 · SHA-256: `a3bff1c6308093cdae72d550e90b2ae5d732d2565c15800bb0f3ec76545bcd30`

````text
{
  "fecha": "2026-11-09T11:32:41.073064-06:00",
  "salidas_y_capturas": [
    {
      "modelo": "kmeans",
      "salida": "reports/weka/kmeans.txt",
      "captura": "reports/weka/kmeans_resultado.png",
      "verificado": true
    },
    {
      "modelo": "dbscan",
      "salida": "reports/weka/dbscan.txt",
      "captura": "reports/weka/dbscan_resultado.png",
      "verificado": true
    },
    {
      "modelo": "ZeroR",
      "salida": "reports/weka/ZeroR.txt",
      "captura": "reports/weka/ZeroR.png",
      "verificado": true
    },
    {
      "modelo": "NaiveBayes",
      "salida": "reports/weka/NaiveBayes.txt",
      "captura": "reports/weka/NaiveBayes.png",
      "verificado": true
    },
    {
      "modelo": "J48",
      "salida": "reports/weka/J48.txt",
      "captura": "reports/weka/J48.png",
      "verificado": true
    },
    {
      "modelo": "RandomForest",
      "salida": "reports/weka/RandomForest.txt",
      "captura": "reports/weka/RandomForest.png",
      "verificado": true
    }
  ],
  "filas_comparativo": 12,
  "herramientas": [
    "Python",
    "Weka Explorer"
  ],
  "fuente_python": "models/metadata.json: comparacion_modelos",
  "exactitud": "Porcentaje para ambas herramientas; Python convertido explícitamente desde proporción; Weka sin conversión.",
  "f1": "Python macro de prueba; Weka F-Measure ponderada en CV; ? de ZeroR conservado.",
  "orange": "Excluido por desviación del plan; sin métricas atribuidas."
}

````

## verificacion_final_ventana.png

Ruta: `Final/reports/weka/verificacion_final_ventana.png` · Bytes: 925607 · SHA-256: `db55f2c6708c8697f387317f5753d787c2132ebcf87b75c995378729edd6cde4`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## verificacion_gui.json

Ruta: `Final/reports/weka/verificacion_gui.json` · Bytes: 3665 · SHA-256: `be902c717117cd70c74115abe9422a476a27290227664fa7c08563b005dbc584`

````text
{
  "fecha": "2026-11-08T19:23:33.499228-06:00",
  "version_weka": "3.8.7",
  "origen": "Salidas del panel de Explorer; no son ejecuciones CLI.",
  "clasificacion": {
    "ZeroR": {
      "exactitud_porcentaje_mostrado": "33.0717",
      "f1_ponderado_mostrado": "?",
      "instancias": 892,
      "aciertos_mostrados": 295,
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
      "matriz_verificada": true,
      "salida": "reports/weka/ZeroR.txt",
      "captura": "reports/weka/ZeroR.png",
      "sha256_salida": "abc7807ce09733680834ddcfcbf72f7a71f72e62ad1d519db547385bc4fe1cad"
    },
    "NaiveBayes": {
      "exactitud_porcentaje_mostrado": "50.8969",
      "f1_ponderado_mostrado": "0.503",
      "instancias": 892,
      "aciertos_mostrados": 454,
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
      "matriz_verificada": true,
      "salida": "reports/weka/NaiveBayes.txt",
      "captura": "reports/weka/NaiveBayes.png",
      "sha256_salida": "5aac3e1f7f662eb504b71c7f77d1e31f2121a15ba7771c97b630a65bfd3027c6"
    },
    "J48": {
      "exactitud_porcentaje_mostrado": "51.009",
      "f1_ponderado_mostrado": "0.506",
      "instancias": 892,
      "aciertos_mostrados": 455,
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
      "matriz_verificada": true,
      "salida": "reports/weka/J48.txt",
      "captura": "reports/weka/J48.png",
      "sha256_salida": "88ceace97d84c7c67628688f9876a4d3de22c07935e6111dd954f3c401a88c8c"
    },
    "RandomForest": {
      "exactitud_porcentaje_mostrado": "53.4753",
      "f1_ponderado_mostrado": "0.530",
      "instancias": 892,
      "aciertos_mostrados": 477,
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
      "matriz_verificada": true,
      "salida": "reports/weka/RandomForest.txt",
      "captura": "reports/weka/RandomForest.png",
      "sha256_salida": "bed5274c54f92bc20ff70c7d64d600839b65e76ea4860e88d8e003dcd5bb47df"
    }
  },
  "kmeans": {
    "n": 887,
    "k": 2,
    "semilla": 42,
    "tamanos": [
      477,
      410
    ],
    "suma_verificada": true
  },
  "dbscan": {
    "paquete": "optics_dbScan",
    "version_paquete": "1.0.6",
    "instalado_y_cargado_verificado_en_gui": true,
    "n": 887,
    "atributos": 6,
    "epsilon": 1.666296,
    "minPoints": 12,
    "opciones_distancia_mostradas": "weka.core.EuclideanDistance -R first-last",
    "clusters_mostrados": 1,
    "instancias_cluster_0_mostradas": 887,
    "porcentaje_mostrado": "100%",
    "asignaciones_verificadas": 887,
    "etiquetas": {
      "0": 887
    },
    "ruido_verificado": 0,
    "criterio_ruido": "Las 887 asignaciones de la salida están etiquetadas 0; no hay etiquetas de ruido. Weka muestra 887 (100%) en Clustered Instances.",
    "salida": "reports/weka/dbscan.txt",
    "captura": "reports/weka/dbscan_resultado.png",
    "sha256_salida": "7d0866476ee480a90daee39e1469861c532b52da9dbef7bfb9c05eedcf11de94"
  },
  "estado_weka": "Seis corridas gráficas completas: SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest."
}

````

