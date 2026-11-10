# Carpeta: Final/reports/archivo_pre_auditoria/reports

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/archivo_pre_auditoria/reports/BITACORA_UNIFICADA.md` · Bytes: 2583 · SHA-256: `daf5239785d15f3dca90ab72fa883ba7d966d816c829bd629a32dc6daf08a02c`

`````text
# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/archivo_pre_auditoria/reports/ejecucion.txt

SHA-256: `65aad5431c101ded61f6c64fb735dce72305f8769058e42469cd48c36cf8a790`

````text
# Hallazgos calculados

Fuente original designada: `Proyecto/data/processed/games_curated.csv`.
Copia inmutable: `data/raw/games_curated.csv`. SHA-256: `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`.
Se observaron 1117 filas, 42 columnas y 0 repeticiones de título y fecha.
Títulos con conflictos analíticos en esta fuente: 0; filas en conflicto: 0.
Quedan 1117 videojuegos por título y fecha; años [1980, 2025].

Pearson usuarios–prensa: n=890, r=0.5444, IC95 % [0.4965, 0.5891].
Es asociación lineal, no diferencia de medias ni causalidad. La procedencia Metacritic es una etiqueta del CSV, no una auditoría externa.
Los grupos con menos de 10 pares o sin variación quedan sin estimación; los CSV por grupo incluyen n, IC y q de Benjamini–Hochberg.

K-Means eligió k=2 por silhouette entre 2 y 8. DBSCAN usa eps=1.0 y min_samples=5.
Su selección cumplió el criterio de cobertura y silhouette: True. Ver tablas completas y medianas antes de nombrar perfiles.

Clasificador elegido en validación interna: bosque_aleatorio.
Prueba reservada: 222 juegos; accuracy=0.5856, balanced accuracy=0.5732, F1 macro=0.5649.
F1 macro de la base mayoritaria: 0.1846. Los cortes del índice son [5.836372019227446, 6.6798754404763105].

La popularidad es relativa a esta muestra de Backloggd. No mide ventas, ingresos, rentabilidad ni fracaso de juegos como servicio.
Las notas son posteriores al lanzamiento; el clasificador describe popularidad contemporánea y no constituye un pronóstico previo al estreno.

## Que debo verificar manualmente

- Escala teórica de Rating y enlaces de procedencia de Metacritic, incluyendo plataforma y fecha de cada nota.
- Roles reales de Team: no se puede atribuir un resultado a desarrolladores con esta columna sin curarla.
- Fecha del scrape, redondeo de conteos, títulos con versiones distintas y fechas TBD.
- Sesgo de selección de juegos populares y dependencia entre juegos de una misma franquicia o estudio.
- Sensibilidad del índice a sus pesos iguales y estabilidad de clusters en otras muestras.


````

`````

## pearson_generos.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/pearson_generos.csv` · Bytes: 3055 · SHA-256: `922a566dd0c119575b4337190bd6be8ee172bce175c57a423fa919a48bef45dc`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## pearson_global.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/pearson_global.csv` · Bytes: 194 · SHA-256: `ab41027f13b2bc57d23119b471e7ca0c40e3ca07defe00c745a2beead29707d9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## pearson_organizaciones.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/pearson_organizaciones.csv` · Bytes: 25263 · SHA-256: `21a5d6c43cb207e40d1332e684935615ccce1a304506fa76df7eab54efc39fce`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## perfiles_dbscan.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/perfiles_dbscan.csv` · Bytes: 194 · SHA-256: `7f76688f383a50c65a557b931e1827f28771dd126d5f5969e6689ff90bdaa588`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## perfiles_kmeans.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/perfiles_kmeans.csv` · Bytes: 157 · SHA-256: `c801ae6995bbc27e09c85f58371faf9c3902c6621a86666689b2377b60c36b64`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## seleccion_dbscan.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/seleccion_dbscan.csv` · Bytes: 595 · SHA-256: `f15852560c5cc1f724ed3013a2f04d0e2c772df04ee7c502a8d58f9ec9c7ab5e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## seleccion_kmeans.csv

Ruta: `Final/reports/archivo_pre_auditoria/reports/seleccion_kmeans.csv` · Bytes: 300 · SHA-256: `7c57f3d2b6cce06c1c9b923aebee8ab8d6d8afb15211d21e41576f1644cc8524`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

