# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/tables/comparativo_herramientas_notas.md

SHA-256: `04d42dea8485c335ebc0f0072228ff91cdf1b77a5168f6859d37e1ea8918ee31`

````text
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

````

## Origen: Final/reports/tables/ejecucion_comparabilidad.txt

SHA-256: `35889d1c98ea3ed200a69fcaf109c3021e4f824fec9bb8ab07c255558ccf35d0`

````text
catalogo_completo DummyClassifier {'exactitud_pct': 33.84064458370636, 'f1_macro': 0.168561872909699, 'f1_ponderado': 0.17112727294503013}
catalogo_completo GaussianNB {'exactitud_pct': 45.568487018800354, 'f1_macro': 0.39557135751585726, 'f1_ponderado': 0.39333606382696396}
catalogo_completo DecisionTreeClassifier {'exactitud_pct': 47.62757385854969, 'f1_macro': 0.4753482040990488, 'f1_ponderado': 0.4746645859511323}
catalogo_completo RandomForestClassifier {'exactitud_pct': 55.68487018800358, 'f1_macro': 0.55551827267702, 'f1_ponderado': 0.5548180432114216}
catalogo_elegible DummyClassifier {'exactitud_pct': 33.84201077199282, 'f1_macro': 0.16856695729935167, 'f1_ponderado': 0.17113934354180138}
catalogo_elegible GaussianNB {'exactitud_pct': 43.71633752244165, 'f1_macro': 0.37816970382484855, 'f1_ponderado': 0.37604899066748126}
catalogo_elegible DecisionTreeClassifier {'exactitud_pct': 49.012567324955114, 'f1_macro': 0.49198194725893063, 'f1_ponderado': 0.49138034277100057}
catalogo_elegible RandomForestClassifier {'exactitud_pct': 54.937163375224415, 'f1_macro': 0.5457646494859345, 'f1_ponderado': 0.5449023237635472}
enlace_exportacion_weka DummyClassifier {'exactitud_pct': 33.07174887892377, 'f1_macro': 0.25307162121666166, 'f1_ponderado': 0.25329318243206017}
enlace_exportacion_weka GaussianNB {'exactitud_pct': 47.421524663677125, 'f1_macro': 0.44367965237950174, 'f1_ponderado': 0.4438026387093977}
enlace_exportacion_weka DecisionTreeClassifier {'exactitud_pct': 46.97309417040359, 'f1_macro': 0.4693485084364956, 'f1_ponderado': 0.46937728433656195}
enlace_exportacion_weka RandomForestClassifier {'exactitud_pct': 54.82062780269058, 'f1_macro': 0.544155803135885, 'f1_ponderado': 0.5442067660700024}
Verificaciones de matrices, métricas y particiones: correctas.

````

## Origen: Final/reports/tables/pruebas_comparabilidad.txt

SHA-256: `2b2ff65dae96389433ca6e86113f21e337d44b0cbe14599aff5e8acc17b21eee`

````text
............................                                             [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
28 passed, 1 warning in 23.10s

````

## Origen: Final/reports/tables/pruebas_metricas_comparables.txt

SHA-256: `d1860236036504b3d533e1a449db7d3961063c3f837f6e99c3ccfc5dfa504fe9`

````text
...                                                                      [100%]
3 passed in 17.05s

````

## Origen: Final/reports/tables/pruebas_revision_visual.txt

SHA-256: `8c5abbacdfc23d41bd705145d4f7c9d8e701ed38ddf88300cab590b3e053d105`

````text
.....................                                                    [100%]
=============================== warnings summary ===============================
tests/test_pipeline.py::test_app_pages[pages/2_Prediccion.py]
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
21 passed, 1 warning in 3.10s

````

## Origen: Final/reports/tables/pruebas_web.txt

SHA-256: `4593e99e56bceac19e2ba3552c99e10b24f8e5513c62a16d8c18a3b297167b3a`

````text
........................................................................ [ 82%]
...............                                                          [100%]
=============================== warnings summary ===============================
tests/test_auditoria2.py::test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv314/lib/python3.14/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
87 passed, 1 warning in 4.82s

````

## Inventario de archivos vigentes vs. evidencia histórica (8–9 de noviembre de 2026)

- **Tablas analíticas y de estado vigentes (12 de noviembre de 2026)**: `bic_gmm.csv`, `calibracion.csv`, `catalogo_resumen.json`, `clase_comparacion_clustering.csv`, `clase_ward_asignaciones.csv`, `clase_ward_cortes.csv`, `clustering_03_alternativas_k.csv`, `clustering_03_correlaciones_ranking_generos.csv`, `clustering_03_perfiles.csv`, `comparacion_estadistica.csv`, `comparacion_prueba_actual_e_historica.csv`, `comparativo_herramientas.csv`, `comparativo_modelos.csv`, `contraejemplos_prediccion.csv`, `correlacion_catalogo.csv`, `correlacion_generos.csv`, `correlacion_organizaciones.csv`, `correlacion_senales.csv`, `cv_externa_folds.csv`, `escenarios_prediccion.csv`, `estado_ci.csv`, `estado_ci_resumen.json`, `evidencia_comercial.csv`, `matriz_confusion.csv`, `metricas_clusters.csv`, `metricas_prueba.csv`, `modelo_error_por_clase.csv`, `modelo_importancia_gini.csv`, `parametros_clustering.csv`, `pca_clusters.csv`, `perfiles_clusters.csv`, `plan_baseline_git.csv`, `popularidad_estudio.csv`, `popularidad_genero.csv`, `procedencia_datos.csv`, `prueba_historica_modelos.csv`, `prueba_historica_predicciones.csv`, `terciles_catalogo.csv`, `verificacion_weka_entradas.csv`, `weka_clustering_cli.csv`.
- **Artefactos del 9 de noviembre conservados por trazabilidad contractual (`reports/weka/manifiesto_evidencias_gui.json`)**: `evaluar_comparabilidad.py`, `test_comparabilidad.py`, `comparativo_detalle.json` (esquema OOF histórico con `GaussianNB`), `comparativo_folds.csv`, `comparativo_predicciones_oof.csv`. `pytest.ini` limita la suite activa a `tests/` (`102` pruebas); esos artefactos no forman parte de la validación anidada vigente del 12 de noviembre.
- **Evidencias visuales y diagnósticos CSS históricos del 8–9 de noviembre**: `graficas_logaritmicas_corregidas.jpg` (referenciada en `DocumentoFinal/main.tex`), `graficas_comparacion_corregida.jpg`, `graficas_movil_corregidas.jpg`, `graficas_permutacion_corregida.jpg`, `integridad_visual_antes.json`, `integridad_visual_resultado.json`, `tipografia_comic_inicio.jpg`, `tipografia_comic_formulario.jpg`, `tipografia_comic_movil.jpg`, `web_prediccion.png`, `web_submenu_modelo.png`, `web_submenu_tras_filtro.png` (citadas en `reports/BITACORA_UNIFICADA.md`), además de los reportes previos del detector de estilos `detector_revision_graficas.json` y `revision_tipografia.json`. Se conservan como historial de auditoría sin mezclarlos con las métricas activas.
