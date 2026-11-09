# Evaluación comparable Python / Weka

Fecha: 2026-11-09T11:41:15.431069-06:00.

## Resultado sobre todo el dataset

Se evaluaron los 1117 registros del archivo depurado mediante StratifiedKFold de 10 pliegues, shuffle=True y semilla 42. Cada registro recibió exactamente una predicción fuera de muestra por modelo. Las métricas del CSV agrupan todas las predicciones OOF, igual que el resumen de CV de Weka; las medias y resultados de cada fold también están en comparativo_detalle.json.

| Modelo | Exactitud (%) | F1 macro | F1 ponderado |
| --- | --- | --- | --- |
| DummyClassifier | 33.840645 | 0.168562 | 0.171127 |
| GaussianNB | 45.568487 | 0.395571 | 0.393336 |
| DecisionTreeClassifier | 47.627574 | 0.475348 | 0.474665 |
| RandomForestClassifier | 55.684870 | 0.555518 | 0.554818 |

## Método y trazabilidad

- Se conserva además la evaluación sobre los 1114 registros elegibles y una evaluación de enlace sobre los mismos 892 registros, etiquetas y atributos exportados a Weka. Los tres esquemas están diferenciados en el CSV.
- El catálogo completo incluye los tres conflictos históricos por la instrucción de evaluar todo el archivo. Su inclusión es descriptiva y no cambia la exclusión del entrenamiento de producción.
- Las etiquetas usan la referencia y los cortes existentes de models/metadata.json para mantener su definición; no se redefine el objetivo por fold. El preprocesamiento del catálogo completo/elegible se ajusta en cada fold. La corrida de enlace usa el preprocesamiento externo ya aplicado para Weka.
- Se usan Dummy mayoritario, GaussianNB, CART y RandomForest de 100 árboles con semilla 42 donde aplica; no hay búsqueda de hiperparámetros ni selección sobre esta evaluación. El modelo de producción y su prueba reservada original no se sobrescriben.
- Weka conserva las salidas gráficas existentes: CV estratificada de 10 pliegues sobre 892 registros. El F1 macro se calcula como promedio simple de los F-Measure por clase mostrados, por lo que puede diferir unas diezmilésimas de calcularlo desde la matriz sin redondeo.
- En ZeroR, Weka muestra ? para la clase medio y para Weighted Avg. La matriz permite resolver F1_medio=2TP/(2TP+FP+FN)=0; su F1 macro promedia las clases mostradas con ese valor resuelto. El ponderado se calcula con los soportes de la matriz. Ambas excepciones quedan identificadas en notas; no se atribuyen a Weka como números reportados.
- Las diferencias de población, referencias, particiones Java/sklearn, semilla CV no recuperada de Weka, semilla del bosque, estimación de Naive Bayes y CART/J48 quedan dentro de notas del CSV. No se declara equivalencia exacta entre implementaciones.
- Orange permanece descartado: no existen evaluaciones verificadas que permitan calcular F1 macro ni ponderado. No se inventan filas ni métricas para esa herramienta.

## Verificaciones ejecutadas

- 28 pruebas existentes de modelo, segunda auditoría y clustering aprobadas (pruebas_comparabilidad.txt).
- 3 pruebas independientes nuevas aprobadas (pruebas_metricas_comparables.txt): métricas derivadas de matrices, cobertura OOF sin duplicados, reproducción exacta de folds con semilla 42, predicción mayoritaria Dummy por fold, redondeo Weka y lectura válida de las seis capturas.
- Las cuatro matrices Weka suman 892 y sus diagonales reproducen los porcentajes reportados dentro de su precisión impresa.
- El CSV tiene exactamente el esquema solicitado, 20 filas y solo Python/Weka: 12 evaluaciones Python, cuatro evaluaciones Weka y cuatro filas descriptivas de clustering sin métricas de clasificación.

Reproducción desde Final: `.venv/bin/python reports/tables/evaluar_comparabilidad.py`. Prueba independiente: `.venv/bin/python -m pytest reports/tables/test_comparabilidad.py -q`. Predicciones, particiones y matrices se guardan junto al comparativo.
