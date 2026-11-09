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
