# Corridas en Weka

| Ubicación | Qué contiene |
| --- | --- |
| `data/export/` | Entradas para Explorer. Clustering tiene 887 juegos y seis atributos. Clasificación tiene 892 juegos, 52 atributos y la clase nominal `nivel_popularidad` al final. Los CSV son los que se cargaron en las corridas gráficas y los ARFF conservan tipos explícitos. |
| `data/clean/` | Espacio transformado y orden para el K-Means por consola. Incluye también las exportaciones ARFF de entrenamiento y prueba del proyecto. |
| `reports/weka/` | Salidas de SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Contiene las capturas de Explorer 3.8.7, las asignaciones de CLI 3.8.6 y un respaldo histórico utilizado para verificar las huellas de las evidencias. |
| `reports/tables/` | Comparativo Python–Weka y verificación de las entradas. |
| `Figuras/` | Figuras usadas en el informe, dibujadas con resultados de Weka. |

## Repetir las corridas en Explorer

Abre **Weka 3.8.7 Explorer**. Para agrupamiento, carga `data/export/clustering.csv` en **Preprocess**. En **Cluster**, configura **SimpleKMeans** con dos grupos, semilla 42 y hasta 500 iteraciones. Para la corrida de **DBSCAN** usa epsilon **1.666296** y mínimo **12** puntos. Si tu instalación no muestra DBSCAN, requiere el paquete `optics_dbScan`. Las opciones completas se guardaron en `kmeans.txt` y `dbscan.txt`.

Para clasificación, carga `data/export/clasificacion.csv`. Selecciona `nivel_popularidad` como clase y elige **Cross-validation** con **10 pliegues**. Ejecuta ZeroR, NaiveBayes, J48 y RandomForest. Los encabezados de las salidas guardadas muestran las opciones con que se ejecutó cada uno.

## Verificación y comparación desde Python

Para ejecutar las comprobaciones en una **copia de ArchivospythonMineria**, copia las carpetas `Weka/data/export` y `Weka/reports/weka` dentro de `data/` y `reports/`, respectivamente. Conserva los nombres `export` y `weka`. Desde la raíz de la copia puedes ejecutar:

```text
python -X utf8 reports/revision_predicciones/verificar_weka.py
python -X utf8 -m src.comparativo_integral
```

Para repetir la corrida de K-Means de **Weka 3.8.6 por consola**, instala Java y, desde la raíz de la copia de análisis, usa `python -X utf8 -m src.comparar_weka --descargar`. El script descarga los JAR de Maven Central, valida sus huellas y guarda la comparación para 2, 3 y 4 grupos.
