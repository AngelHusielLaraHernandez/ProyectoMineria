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

El gestor oficial ofrece optics_dbScan 1.0.6; su versión instalada está vacía. No se instaló ni ejecutó DBSCAN. Se solicitó autorización para la instalación y su posible escritura fuera de Final. Parámetros solicitados para la futura corrida: eps=1.666296 y minPoints=12, según reports/clustering.md.

## Registro de diferencias con Python

Se registran sin modificar las corridas: Python reporta tamaños 465 y 422 para k=2; Weka GUI mostró 477 y 410. El reporte Python indica RandomForest con exactitud 0.5676 y F1 macro 0.5577 sobre el conjunto de prueba; Weka mostró exactitud 53.4753 % y F-Measure ponderada 0.530 en CV de 10 pliegues sobre 892 registros. Se conservan las definiciones y los protocolos de cada salida.

## Que debo verificar manualmente

- No confundir estas corridas GUI 3.8.7 con los artefactos CLI 3.8.6 anteriores de esta carpeta.
- F1 del comparativo Weka es ponderada; no es F1 macro. Exactitud se transcribió en porcentaje.
- Los datos exportados ya contienen transformaciones previas; esta evaluación no es el mismo protocolo de Python con ajuste dentro de cada pliegue.
- DBSCAN permanece pendiente hasta autorizar su paquete; no se ha generado una salida falsa.
