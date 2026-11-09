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
