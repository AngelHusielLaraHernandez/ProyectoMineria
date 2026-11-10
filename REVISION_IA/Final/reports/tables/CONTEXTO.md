# Carpeta: Final/reports/tables

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/tables/BITACORA_UNIFICADA.md` · Bytes: 9462 · SHA-256: `5f890fdb219c06c1c044791635f54f9a6b047f39a9bfa9d01b312f081d2613b7`

`````text
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

`````

## comparativo_detalle.json

Ruta: `Final/reports/tables/comparativo_detalle.json` · Bytes: 31092 · SHA-256: `0316b13e1db7522ddaa97aa671c773f02f5116bf9096fbaef4334f0071d91304`

````text
{
  "catalogo_completo/DummyClassifier": {
    "n": 1117,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        0,
        0,
        374
      ],
      [
        0,
        0,
        365
      ],
      [
        0,
        0,
        378
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 33.84064458370636,
      "f1_macro": 0.168561872909699,
      "f1_ponderado": 0.17112727294503013
    },
    "media_metricas_folds": {
      "exactitud_pct": 33.84169884169884,
      "f1_macro": 0.1685607755406413,
      "f1_ponderado": 0.1711516502120529
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 33.035714285714285,
        "f1_macro": 0.16554809843400448,
        "f1_ponderado": 0.16406999041227227
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 33.035714285714285,
        "f1_macro": 0.16554809843400448,
        "f1_ponderado": 0.16406999041227227
      },
      {
        "fold": 5,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 6,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 7,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      }
    ]
  },
  "catalogo_completo/GaussianNB": {
    "n": 1117,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        182,
        175,
        17
      ],
      [
        53,
        300,
        12
      ],
      [
        105,
        246,
        27
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 45.568487018800354,
      "f1_macro": 0.39557135751585726,
      "f1_ponderado": 0.39333606382696396
    },
    "media_metricas_folds": {
      "exactitud_pct": 45.57673745173746,
      "f1_macro": 0.39184825398779877,
      "f1_ponderado": 0.3896025631359
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 41.964285714285715,
        "f1_macro": 0.36329866731161586,
        "f1_ponderado": 0.36070093048102764
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 43.75,
        "f1_macro": 0.37575499042931365,
        "f1_ponderado": 0.3727506152584086
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 43.75,
        "f1_macro": 0.3860049773093251,
        "f1_ponderado": 0.38644049187527446
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 46.42857142857143,
        "f1_macro": 0.3779755466971561,
        "f1_ponderado": 0.378865157354311
      },
      {
        "fold": 5,
        "n": 112,
        "exactitud_pct": 40.17857142857143,
        "f1_macro": 0.3253968253968254,
        "f1_ponderado": 0.32334183673469397
      },
      {
        "fold": 6,
        "n": 112,
        "exactitud_pct": 46.42857142857143,
        "f1_macro": 0.38699459878799214,
        "f1_ponderado": 0.38397482993992865
      },
      {
        "fold": 7,
        "n": 112,
        "exactitud_pct": 47.32142857142857,
        "f1_macro": 0.4084339774557166,
        "f1_ponderado": 0.40558089630779853
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 48.64864864864865,
        "f1_macro": 0.4315961719640997,
        "f1_ponderado": 0.4281242615154451
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 50.45045045045045,
        "f1_macro": 0.4441890166028097,
        "f1_ponderado": 0.44038521279900594
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 46.846846846846844,
        "f1_macro": 0.4188377679231338,
        "f1_ponderado": 0.4158613990931064
      }
    ]
  },
  "catalogo_completo/DecisionTreeClassifier": {
    "n": 1117,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        201,
        70,
        103
      ],
      [
        60,
        193,
        112
      ],
      [
        121,
        119,
        138
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 47.62757385854969,
      "f1_macro": 0.4753482040990488,
      "f1_ponderado": 0.4746645859511323
    },
    "media_metricas_folds": {
      "exactitud_pct": 47.625482625482626,
      "f1_macro": 0.4744449078866033,
      "f1_ponderado": 0.4739333126961943
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 48.214285714285715,
        "f1_macro": 0.48128965178631594,
        "f1_ponderado": 0.4814254632373874
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 48.214285714285715,
        "f1_macro": 0.48265726043503826,
        "f1_ponderado": 0.4815759637188209
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 49.107142857142854,
        "f1_macro": 0.4968734968734969,
        "f1_ponderado": 0.4971139971139971
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 47.32142857142857,
        "f1_macro": 0.46328733962720897,
        "f1_ponderado": 0.46422139226060793
      },
      {
        "fold": 5,
        "n": 112,
        "exactitud_pct": 45.535714285714285,
        "f1_macro": 0.45480171355078275,
        "f1_ponderado": 0.4548097000595405
      },
      {
        "fold": 6,
        "n": 112,
        "exactitud_pct": 47.32142857142857,
        "f1_macro": 0.47285948546141277,
        "f1_ponderado": 0.47258001185513626
      },
      {
        "fold": 7,
        "n": 112,
        "exactitud_pct": 50.0,
        "f1_macro": 0.4949723479135244,
        "f1_ponderado": 0.4939668174962293
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 44.14414414414414,
        "f1_macro": 0.441682327867657,
        "f1_ponderado": 0.44022446780806873
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 50.45045045045045,
        "f1_macro": 0.5045045045045046,
        "f1_ponderado": 0.5035305575846116
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 45.94594594594595,
        "f1_macro": 0.45152095084609184,
        "f1_ponderado": 0.4498847558275439
      }
    ]
  },
  "catalogo_completo/RandomForestClassifier": {
    "n": 1117,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        241,
        41,
        92
      ],
      [
        50,
        218,
        97
      ],
      [
        105,
        110,
        163
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 55.68487018800358,
      "f1_macro": 0.55551827267702,
      "f1_ponderado": 0.5548180432114216
    },
    "media_metricas_folds": {
      "exactitud_pct": 55.68211068211068,
      "f1_macro": 0.5541961352041618,
      "f1_ponderado": 0.5537302760288823
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 52.67857142857143,
        "f1_macro": 0.5256217756217757,
        "f1_ponderado": 0.5249346186846187
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 60.71428571428571,
        "f1_macro": 0.6099182299182299,
        "f1_ponderado": 0.609381055452484
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 56.25,
        "f1_macro": 0.5521119781989348,
        "f1_ponderado": 0.5527379625205712
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 57.14285714285714,
        "f1_macro": 0.5623004640221283,
        "f1_ponderado": 0.5633774851403976
      },
      {
        "fold": 5,
        "n": 112,
        "exactitud_pct": 53.57142857142857,
        "f1_macro": 0.5365666602353848,
        "f1_ponderado": 0.5364633864832833
      },
      {
        "fold": 6,
        "n": 112,
        "exactitud_pct": 50.0,
        "f1_macro": 0.5024245140130325,
        "f1_ponderado": 0.5017812571632326
      },
      {
        "fold": 7,
        "n": 112,
        "exactitud_pct": 62.5,
        "f1_macro": 0.6124412338034629,
        "f1_ponderado": 0.6109412624699002
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 49.549549549549546,
        "f1_macro": 0.49571163136380525,
        "f1_ponderado": 0.4938732712645756
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 57.65765765765766,
        "f1_macro": 0.5762962962962962,
        "f1_ponderado": 0.5760960960960961
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 56.75675675675676,
        "f1_macro": 0.5685685685685686,
        "f1_ponderado": 0.5677163650136623
      }
    ]
  },
  "catalogo_elegible/DummyClassifier": {
    "n": 1114,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        0,
        0,
        372
      ],
      [
        0,
        0,
        365
      ],
      [
        0,
        0,
        377
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 33.84201077199282,
      "f1_macro": 0.16856695729935167,
      "f1_ponderado": 0.17113934354180138
    },
    "media_metricas_folds": {
      "exactitud_pct": 33.84330759330759,
      "f1_macro": 0.16856524981357196,
      "f1_ponderado": 0.171170402425436
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 33.035714285714285,
        "f1_macro": 0.16554809843400448,
        "f1_ponderado": 0.16406999041227227
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 33.035714285714285,
        "f1_macro": 0.16554809843400448,
        "f1_ponderado": 0.16406999041227227
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 33.92857142857143,
        "f1_macro": 0.1688888888888889,
        "f1_ponderado": 0.17190476190476192
      },
      {
        "fold": 5,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 6,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 7,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 34.234234234234236,
        "f1_macro": 0.17002237136465326,
        "f1_ponderado": 0.17461757059072497
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 33.33333333333333,
        "f1_macro": 0.16666666666666666,
        "f1_ponderado": 0.16666666666666666
      }
    ]
  },
  "catalogo_elegible/GaussianNB": {
    "n": 1114,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        156,
        201,
        15
      ],
      [
        48,
        303,
        14
      ],
      [
        91,
        258,
        28
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 43.71633752244165,
      "f1_macro": 0.37816970382484855,
      "f1_ponderado": 0.37604899066748126
    },
    "media_metricas_folds": {
      "exactitud_pct": 43.7234555984556,
      "f1_macro": 0.3731428853411214,
      "f1_ponderado": 0.37098003826919024
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 41.964285714285715,
        "f1_macro": 0.3614469821366373,
        "f1_ponderado": 0.3620076557268676
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 37.5,
        "f1_macro": 0.28920634920634924,
        "f1_ponderado": 0.2894812925170068
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 41.964285714285715,
        "f1_macro": 0.3639985095497668,
        "f1_ponderado": 0.3622682796962639
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 45.535714285714285,
        "f1_macro": 0.37618365512703233,
        "f1_ponderado": 0.37324015488399614
      },
      {
        "fold": 5,
        "n": 111,
        "exactitud_pct": 45.04504504504504,
        "f1_macro": 0.3968136123763469,
        "f1_ponderado": 0.39334464588793705
      },
      {
        "fold": 6,
        "n": 111,
        "exactitud_pct": 46.846846846846844,
        "f1_macro": 0.3872175397102083,
        "f1_ponderado": 0.38261662601838553
      },
      {
        "fold": 7,
        "n": 111,
        "exactitud_pct": 41.44144144144144,
        "f1_macro": 0.35127031438506845,
        "f1_ponderado": 0.34777277810064694
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 43.24324324324324,
        "f1_macro": 0.3662637301981564,
        "f1_ponderado": 0.3628439169422776
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 46.846846846846844,
        "f1_macro": 0.4281716279138959,
        "f1_ponderado": 0.42536850011076816
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 46.846846846846844,
        "f1_macro": 0.4108565328077523,
        "f1_ponderado": 0.41085653280775236
      }
    ]
  },
  "catalogo_elegible/DecisionTreeClassifier": {
    "n": 1114,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        197,
        63,
        112
      ],
      [
        44,
        196,
        125
      ],
      [
        96,
        128,
        153
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 49.012567324955114,
      "f1_macro": 0.49198194725893063,
      "f1_ponderado": 0.49138034277100057
    },
    "media_metricas_folds": {
      "exactitud_pct": 49.008204633204635,
      "f1_macro": 0.4913450155836407,
      "f1_ponderado": 0.4906946830796087
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 50.0,
        "f1_macro": 0.502983026363308,
        "f1_ponderado": 0.5040253056802352
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 48.214285714285715,
        "f1_macro": 0.48679098679098676,
        "f1_ponderado": 0.48758533133533133
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 49.107142857142854,
        "f1_macro": 0.48959865416967085,
        "f1_ponderado": 0.4884072767535277
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 53.57142857142857,
        "f1_macro": 0.5380078858339729,
        "f1_ponderado": 0.5369148191353161
      },
      {
        "fold": 5,
        "n": 111,
        "exactitud_pct": 45.04504504504504,
        "f1_macro": 0.454072697975137,
        "f1_ponderado": 0.45391235305539857
      },
      {
        "fold": 6,
        "n": 111,
        "exactitud_pct": 44.14414414414414,
        "f1_macro": 0.44813055037049604,
        "f1_ponderado": 0.4466017859026513
      },
      {
        "fold": 7,
        "n": 111,
        "exactitud_pct": 54.95495495495496,
        "f1_macro": 0.5437131890675667,
        "f1_ponderado": 0.5415131629544971
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 45.04504504504504,
        "f1_macro": 0.44941119923095413,
        "f1_ponderado": 0.4473846593529362
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 48.64864864864865,
        "f1_macro": 0.48704580411897486,
        "f1_ponderado": 0.4869059747108528
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 51.35135135135135,
        "f1_macro": 0.5136961619153401,
        "f1_ponderado": 0.51369616191534
      }
    ]
  },
  "catalogo_elegible/RandomForestClassifier": {
    "n": 1114,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        246,
        41,
        85
      ],
      [
        46,
        221,
        98
      ],
      [
        106,
        126,
        145
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 54.937163375224415,
      "f1_macro": 0.5457646494859345,
      "f1_ponderado": 0.5449023237635472
    },
    "media_metricas_folds": {
      "exactitud_pct": 54.93886743886744,
      "f1_macro": 0.5452778356774489,
      "f1_ponderado": 0.5444262902526396
    },
    "folds": [
      {
        "fold": 1,
        "n": 112,
        "exactitud_pct": 52.67857142857143,
        "f1_macro": 0.521781045751634,
        "f1_ponderado": 0.5223603816526611
      },
      {
        "fold": 2,
        "n": 112,
        "exactitud_pct": 57.14285714285714,
        "f1_macro": 0.5762290341237709,
        "f1_ponderado": 0.5777167850946047
      },
      {
        "fold": 3,
        "n": 112,
        "exactitud_pct": 56.25,
        "f1_macro": 0.5524866711703612,
        "f1_ponderado": 0.5507520487065534
      },
      {
        "fold": 4,
        "n": 112,
        "exactitud_pct": 51.78571428571429,
        "f1_macro": 0.5058398714678717,
        "f1_ponderado": 0.5037221647263542
      },
      {
        "fold": 5,
        "n": 111,
        "exactitud_pct": 53.153153153153156,
        "f1_macro": 0.5299034299034299,
        "f1_ponderado": 0.52997272997273
      },
      {
        "fold": 6,
        "n": 111,
        "exactitud_pct": 53.153153153153156,
        "f1_macro": 0.5301514822062767,
        "f1_ponderado": 0.528506980561775
      },
      {
        "fold": 7,
        "n": 111,
        "exactitud_pct": 59.45945945945946,
        "f1_macro": 0.5879261700157222,
        "f1_ponderado": 0.5859540486406158
      },
      {
        "fold": 8,
        "n": 111,
        "exactitud_pct": 50.45045045045045,
        "f1_macro": 0.5014141414141414,
        "f1_ponderado": 0.5000803400803401
      },
      {
        "fold": 9,
        "n": 111,
        "exactitud_pct": 57.65765765765766,
        "f1_macro": 0.576113813317996,
        "f1_ponderado": 0.5742647256874748
      },
      {
        "fold": 10,
        "n": 111,
        "exactitud_pct": 57.65765765765766,
        "f1_macro": 0.5709326974032857,
        "f1_ponderado": 0.5709326974032857
      }
    ]
  },
  "enlace_exportacion_weka/DummyClassifier": {
    "n": 892,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
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
    "metricas_oof": {
      "exactitud_pct": 33.07174887892377,
      "f1_macro": 0.25307162121666166,
      "f1_ponderado": 0.25329318243206017
    },
    "media_metricas_folds": {
      "exactitud_pct": 33.07116104868915,
      "f1_macro": 0.16567440535536246,
      "f1_ponderado": 0.16440000490769532
    },
    "folds": [
      {
        "fold": 1,
        "n": 90,
        "exactitud_pct": 33.33333333333333,
        "f1_macro": 0.16666666666666666,
        "f1_ponderado": 0.16666666666666666
      },
      {
        "fold": 2,
        "n": 90,
        "exactitud_pct": 33.33333333333333,
        "f1_macro": 0.16666666666666666,
        "f1_ponderado": 0.16666666666666666
      },
      {
        "fold": 3,
        "n": 89,
        "exactitud_pct": 32.58426966292135,
        "f1_macro": 0.16384180790960454,
        "f1_ponderado": 0.16015996952961342
      },
      {
        "fold": 4,
        "n": 89,
        "exactitud_pct": 32.58426966292135,
        "f1_macro": 0.16384180790960454,
        "f1_ponderado": 0.16015996952961342
      },
      {
        "fold": 5,
        "n": 89,
        "exactitud_pct": 33.70786516853933,
        "f1_macro": 0.1680672268907563,
        "f1_ponderado": 0.1699556226985176
      },
      {
        "fold": 6,
        "n": 89,
        "exactitud_pct": 33.70786516853933,
        "f1_macro": 0.1680672268907563,
        "f1_ponderado": 0.1699556226985176
      },
      {
        "fold": 7,
        "n": 89,
        "exactitud_pct": 33.70786516853933,
        "f1_macro": 0.1680672268907563,
        "f1_ponderado": 0.1699556226985176
      },
      {
        "fold": 8,
        "n": 89,
        "exactitud_pct": 32.58426966292135,
        "f1_macro": 0.16384180790960454,
        "f1_ponderado": 0.16015996952961342
      },
      {
        "fold": 9,
        "n": 89,
        "exactitud_pct": 32.58426966292135,
        "f1_macro": 0.16384180790960454,
        "f1_ponderado": 0.16015996952961342
      },
      {
        "fold": 10,
        "n": 89,
        "exactitud_pct": 32.58426966292135,
        "f1_macro": 0.16384180790960454,
        "f1_ponderado": 0.16015996952961342
      }
    ]
  },
  "enlace_exportacion_weka/GaussianNB": {
    "n": 892,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        190,
        64,
        43
      ],
      [
        80,
        184,
        34
      ],
      [
        129,
        119,
        49
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 47.421524663677125,
      "f1_macro": 0.44367965237950174,
      "f1_ponderado": 0.4438026387093977
    },
    "media_metricas_folds": {
      "exactitud_pct": 47.43071161048689,
      "f1_macro": 0.4329188261260576,
      "f1_ponderado": 0.43361470353512865
    },
    "folds": [
      {
        "fold": 1,
        "n": 90,
        "exactitud_pct": 44.44444444444444,
        "f1_macro": 0.4025219298245613,
        "f1_ponderado": 0.4025219298245614
      },
      {
        "fold": 2,
        "n": 90,
        "exactitud_pct": 42.22222222222222,
        "f1_macro": 0.38284513604240905,
        "f1_ponderado": 0.38284513604240916
      },
      {
        "fold": 3,
        "n": 89,
        "exactitud_pct": 48.31460674157304,
        "f1_macro": 0.47854742827604024,
        "f1_ponderado": 0.4780755123554848
      },
      {
        "fold": 4,
        "n": 89,
        "exactitud_pct": 51.68539325842697,
        "f1_macro": 0.48442760942760943,
        "f1_ponderado": 0.48362841902167747
      },
      {
        "fold": 5,
        "n": 89,
        "exactitud_pct": 50.56179775280899,
        "f1_macro": 0.42152872003618275,
        "f1_ponderado": 0.4255840308162965
      },
      {
        "fold": 6,
        "n": 89,
        "exactitud_pct": 50.56179775280899,
        "f1_macro": 0.45739348370927324,
        "f1_ponderado": 0.4607586381684549
      },
      {
        "fold": 7,
        "n": 89,
        "exactitud_pct": 48.31460674157304,
        "f1_macro": 0.430887120542293,
        "f1_ponderado": 0.4345761432162053
      },
      {
        "fold": 8,
        "n": 89,
        "exactitud_pct": 46.06741573033708,
        "f1_macro": 0.4033087633087633,
        "f1_ponderado": 0.40205210317569867
      },
      {
        "fold": 9,
        "n": 89,
        "exactitud_pct": 43.82022471910113,
        "f1_macro": 0.39107827038861526,
        "f1_ponderado": 0.3900481540930979
      },
      {
        "fold": 10,
        "n": 89,
        "exactitud_pct": 48.31460674157304,
        "f1_macro": 0.4766497997048282,
        "f1_ponderado": 0.47605696863740055
      }
    ]
  },
  "enlace_exportacion_weka/DecisionTreeClassifier": {
    "n": 892,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        165,
        49,
        83
      ],
      [
        45,
        149,
        104
      ],
      [
        86,
        106,
        105
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 46.97309417040359,
      "f1_macro": 0.4693485084364956,
      "f1_ponderado": 0.46937728433656195
    },
    "media_metricas_folds": {
      "exactitud_pct": 46.96878901373283,
      "f1_macro": 0.4692195338604785,
      "f1_ponderado": 0.4693494106660851
    },
    "folds": [
      {
        "fold": 1,
        "n": 90,
        "exactitud_pct": 44.44444444444444,
        "f1_macro": 0.4436063218390805,
        "f1_ponderado": 0.44360632183908044
      },
      {
        "fold": 2,
        "n": 90,
        "exactitud_pct": 53.333333333333336,
        "f1_macro": 0.5339578454332553,
        "f1_ponderado": 0.5339578454332552
      },
      {
        "fold": 3,
        "n": 89,
        "exactitud_pct": 42.69662921348314,
        "f1_macro": 0.42336051947035935,
        "f1_ponderado": 0.42293155382914466
      },
      {
        "fold": 4,
        "n": 89,
        "exactitud_pct": 51.68539325842697,
        "f1_macro": 0.5220774642244764,
        "f1_ponderado": 0.5220492316434657
      },
      {
        "fold": 5,
        "n": 89,
        "exactitud_pct": 47.19101123595505,
        "f1_macro": 0.4746291959406714,
        "f1_ponderado": 0.4755414046259506
      },
      {
        "fold": 6,
        "n": 89,
        "exactitud_pct": 41.57303370786517,
        "f1_macro": 0.4170921269810746,
        "f1_ponderado": 0.41851650390619727
      },
      {
        "fold": 7,
        "n": 89,
        "exactitud_pct": 47.19101123595505,
        "f1_macro": 0.4706352019877808,
        "f1_ponderado": 0.4721144396410428
      },
      {
        "fold": 8,
        "n": 89,
        "exactitud_pct": 52.80898876404494,
        "f1_macro": 0.5229999710874028,
        "f1_ponderado": 0.5222453198139329
      },
      {
        "fold": 9,
        "n": 89,
        "exactitud_pct": 43.82022471910113,
        "f1_macro": 0.4375478927203065,
        "f1_ponderado": 0.43684618364974814
      },
      {
        "fold": 10,
        "n": 89,
        "exactitud_pct": 44.9438202247191,
        "f1_macro": 0.44628879892037787,
        "f1_ponderado": 0.4456853022790338
      }
    ]
  },
  "enlace_exportacion_weka/RandomForestClassifier": {
    "n": 892,
    "clases": [
      "alto",
      "bajo",
      "medio"
    ],
    "matriz": [
      [
        198,
        34,
        65
      ],
      [
        37,
        176,
        85
      ],
      [
        93,
        89,
        115
      ]
    ],
    "metricas_oof": {
      "exactitud_pct": 54.82062780269058,
      "f1_macro": 0.544155803135885,
      "f1_ponderado": 0.5442067660700024
    },
    "media_metricas_folds": {
      "exactitud_pct": 54.81897627965044,
      "f1_macro": 0.5431195411610464,
      "f1_ponderado": 0.543289128740895
    },
    "folds": [
      {
        "fold": 1,
        "n": 90,
        "exactitud_pct": 60.0,
        "f1_macro": 0.585381127254304,
        "f1_ponderado": 0.5853811272543041
      },
      {
        "fold": 2,
        "n": 90,
        "exactitud_pct": 51.11111111111111,
        "f1_macro": 0.5097187412976886,
        "f1_ponderado": 0.5097187412976887
      },
      {
        "fold": 3,
        "n": 89,
        "exactitud_pct": 49.43820224719101,
        "f1_macro": 0.4905000998955192,
        "f1_ponderado": 0.49050801204752115
      },
      {
        "fold": 4,
        "n": 89,
        "exactitud_pct": 60.67415730337079,
        "f1_macro": 0.591764705882353,
        "f1_ponderado": 0.5916721744877727
      },
      {
        "fold": 5,
        "n": 89,
        "exactitud_pct": 56.17977528089888,
        "f1_macro": 0.5583453168440226,
        "f1_ponderado": 0.5602821753222621
      },
      {
        "fold": 6,
        "n": 89,
        "exactitud_pct": 53.93258426966292,
        "f1_macro": 0.5351436871044714,
        "f1_ponderado": 0.5357466332350668
      },
      {
        "fold": 7,
        "n": 89,
        "exactitud_pct": 59.55056179775281,
        "f1_macro": 0.5865641312993718,
        "f1_ponderado": 0.588490758172144
      },
      {
        "fold": 8,
        "n": 89,
        "exactitud_pct": 49.43820224719101,
        "f1_macro": 0.4960194375516956,
        "f1_ponderado": 0.49527246493991695
      },
      {
        "fold": 9,
        "n": 89,
        "exactitud_pct": 59.55056179775281,
        "f1_macro": 0.5901392645637523,
        "f1_ponderado": 0.5887715663366072
      },
      {
        "fold": 10,
        "n": 89,
        "exactitud_pct": 48.31460674157304,
        "f1_macro": 0.487618899917287,
        "f1_ponderado": 0.4870476343156662
      }
    ]
  },
  "Weka/ZeroR": {
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
    "f1_clases_usados": [
      0.309,
      0.451,
      0.0
    ],
    "macro_desde_matriz_sin_redondeo": 0.25307162121666166,
    "ponderado_desde_matriz_sin_redondeo": 0.25329318243206017,
    "ponderado_mostrado": "?"
  },
  "Weka/NaiveBayes": {
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
    "f1_clases_usados": [
      0.605,
      0.557,
      0.348
    ],
    "macro_desde_matriz_sin_redondeo": 0.5033953898573705,
    "ponderado_desde_matriz_sin_redondeo": 0.5034553457668585,
    "ponderado_mostrado": "0.503"
  },
  "Weka/J48": {
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
    "f1_clases_usados": [
      0.62,
      0.541,
      0.358
    ],
    "macro_desde_matriz_sin_redondeo": 0.5063108540376969,
    "ponderado_desde_matriz_sin_redondeo": 0.5063502534846777,
    "ponderado_mostrado": "0.506"
  },
  "Weka/RandomForest": {
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
    "f1_clases_usados": [
      0.629,
      0.58,
      0.381
    ],
    "macro_desde_matriz_sin_redondeo": 0.5303083703633139,
    "ponderado_desde_matriz_sin_redondeo": 0.5303645618510748,
    "ponderado_mostrado": "0.530"
  }
}

````

## comparativo_folds.csv

Ruta: `Final/reports/tables/comparativo_folds.csv` · Bytes: 97207 · SHA-256: `4efe3a7a75dd2e00310a38045a9be880f4b289ab7be505e82e7fb05fc60dbd32`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## comparativo_herramientas.csv

Ruta: `Final/reports/tables/comparativo_herramientas.csv` · Bytes: 14198 · SHA-256: `16e8e53c939be9db1802c5da0d55f5c474484408a5b3dc5aa4f3ac5413066893`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## comparativo_predicciones_oof.csv

Ruta: `Final/reports/tables/comparativo_predicciones_oof.csv` · Bytes: 657427 · SHA-256: `70cbe0ea4d0175e36f9be3e23347f49a8bcf586227ea7bfcb4063adf7eab1822`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## detector_revision_graficas.json

Ruta: `Final/reports/tables/detector_revision_graficas.json` · Bytes: 2843 · SHA-256: `ca77f8404b01b5d8fe3707eb8a20cc9a72957891ffecc8d01d0aa31b065917c9`

````text
[
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 172,
    "snippet": "border-right: 4px solid var(--p5-red) !important"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1438,
    "snippet": "border-left: 7px solid var(--p5-red)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1447,
    "snippet": "border-left: 9px solid var(--p5-yellow)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1590,
    "snippet": "border-right: 3px solid var(--p5-yellow)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1614,
    "snippet": "border-left: 6px solid var(--p5-red)"
  },
  {
    "antipattern": "bounce-easing",
    "name": "Bounce or elastic easing",
    "description": "Bounce and elastic easing feel dated and tacky. Real objects decelerate smoothly — use exponential easing (ease-out-quart/quint/expo) instead.",
    "severity": "advisory",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 316,
    "snippet": "cubic-bezier(0.34, 1.56, 0.64, 1)",
    "advisory": true
  }
]

````

## evaluar_comparabilidad.py

Ruta: `Final/reports/tables/evaluar_comparabilidad.py` · Bytes: 8880 · SHA-256: `1f0c178f4dba03c4922e5cf948770211637a01e7d47a9044b2bbcd57af0178cd`

````text
"""Desde Final: .venv/bin/python reports/tables/evaluar_comparabilidad.py."""
from pathlib import Path
import sys, importlib.util, json, re, csv
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import clone
RAIZ=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(RAIZ))
from src.objetivo import aplicar_referencia, CAMPOS_OBJETIVO
from src.features import lista_cruda
from src.config import FEATURES
spec=importlib.util.spec_from_file_location('modelo_original',RAIZ/'src/04_modelo.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
SALIDA=RAIZ/'reports/tables'; W=RAIZ/'reports/weka'; SEMILLA=42
CLASES=['alto','bajo','medio']
def metricas(y,p):
 return {'exactitud_pct':float(accuracy_score(y,p)*100),'f1_macro':float(f1_score(y,p,labels=CLASES,average='macro',zero_division=0)), 'f1_ponderado':float(f1_score(y,p,labels=CLASES,average='weighted',zero_division=0))}
def desde_matriz(m):
 tp=np.diag(m); reales=m.sum(axis=1); predichas=m.sum(axis=0)
 f=np.divide(2*tp,reales+predichas,out=np.zeros(3),where=(reales+predichas)!=0)
 return f,float(f.mean()),float(np.average(f,weights=reales))
def ejecutar():
 meta=json.loads((RAIZ/'models/metadata.json').read_text())
 df=pd.read_csv(RAIZ/'data/clean/dataset_depurado.csv')
 assert not df[CAMPOS_OBJETIVO].isna().any().any(), 'Faltan señales para construir el objetivo sobre todo el dataset.'
 df=df.reset_index(drop=True)
 df['generos']=df.generos.map(lista_cruda); df['estudio']=df.Team.map(lista_cruda)
 y=aplicar_referencia(df,meta['definicion_objetivo']).nivel_popularidad.to_numpy()
 exportado=pd.read_csv(RAIZ/'data/export/clasificacion.csv')
 modelos={'DummyClassifier':DummyClassifier(strategy='most_frequent',random_state=SEMILLA),'GaussianNB':GaussianNB(),'DecisionTreeClassifier':DecisionTreeClassifier(random_state=SEMILLA),'RandomForestClassifier':RandomForestClassifier(n_estimators=100,random_state=SEMILLA,n_jobs=1)}
 filas=[]; folds_guardados=[]; pred_guardadas=[]; detalle={}
 for cohorte,X,etiquetas,crudas in [('catalogo_completo',df[FEATURES],y,True),('catalogo_elegible',df.loc[df.elegible_analisis.eq(True),FEATURES].reset_index(drop=True),y[df.elegible_analisis.eq(True).to_numpy()],True),('enlace_exportacion_weka',exportado.iloc[:,:-1],exportado.iloc[:,-1].to_numpy(),False)]:
  folds=list(StratifiedKFold(n_splits=10,shuffle=True,random_state=SEMILLA).split(X,etiquetas))
  visitas=np.zeros(len(X),int)
  for numero,(a,b) in enumerate(folds,1):
   assert set(a).isdisjoint(b); visitas[b]+=1
   folds_guardados.extend({'cohorte':cohorte,'fila':int(i),'fold':numero,'clase':etiquetas[i]} for i in b)
  assert np.all(visitas==1)
  for nombre,modelo in modelos.items():
   pred=np.empty(len(X),dtype=object); resultados_folds=[]
   for numero,(a,b) in enumerate(folds,1):
    estimador=mod.construir_pipeline(clone(modelo)) if crudas else clone(modelo)
    estimador.fit(X.iloc[a],etiquetas[a]); pred[b]=estimador.predict(X.iloc[b])
    resultados_folds.append({'fold':numero,'n':len(b),**metricas(etiquetas[b],pred[b])})
   valores=metricas(etiquetas,pred); matriz=confusion_matrix(etiquetas,pred,labels=CLASES)
   fs,macro,ponderado=desde_matriz(matriz)
   assert np.isclose(macro,valores['f1_macro']) and np.isclose(ponderado,valores['f1_ponderado'])
   assert matriz.sum()==len(X)
   medias={k:float(np.mean([f[k] for f in resultados_folds])) for k in valores}
   esquema=f'CV estratificada 10 pliegues; shuffle=True; semilla=42; n={len(X)}; {cohorte}; métricas OOF agrupadas'
   notas=('Toda la cohorte elegible, incluidos los casos antes reservados; no modifica la evaluación original de prueba ni el modelo guardado. Etiquetas fijas con referencia existente de entrenamiento; no se redefine el target por fold. Preprocesamiento ajustado dentro de cada fold. ' if crudas else 'Mismos 892 registros, etiquetas y 52 atributos numéricos que Weka; transformaciones previas al CV, sin nuevo ajuste por fold. ')
   notas+=('Incluye los 1117 registros, incluidos los tres conflictos históricos, como evaluación descriptiva solicitada de todo el archivo; no cambia su exclusión en el modelo de producción. ' if cohorte=='catalogo_completo' else '')
   notas+='CV sin agrupación por título, a diferencia de la evaluación original de producción. Las particiones de sklearn y Java no son idénticas; no se conoce la semilla CV de la sesión Weka guardada. GaussianNB y Weka NaiveBayes no garantizan estimadores numéricos idénticos; CART y J48 difieren en algoritmo/poda; RandomForest usa 100 árboles, semilla 42 frente a S=1 en Weka. No se ajustan hiperparámetros en esta comparación.'
   filas.append({'herramienta':'Python','modelo':nombre,'esquema_evaluacion':esquema,**valores,'notas':notas})
   clave=cohorte+'/'+nombre; detalle[clave]={'n':len(X),'clases':CLASES,'matriz':matriz.tolist(),'metricas_oof':valores,'media_metricas_folds':medias,'folds':resultados_folds}
   pred_guardadas.extend({'cohorte':cohorte,'modelo':nombre,'fila':i,'real':etiquetas[i],'predicha':pred[i]} for i in range(len(X)))
   print(cohorte,nombre,valores,flush=True)
 for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
  texto=(W/f'{nombre}.txt').read_text(); seccion=texto.split('=== Detailed Accuracy By Class ===')[1].split('=== Confusion Matrix ===')[0]
  matriz=np.array([list(map(int,g)) for g in re.findall(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s*\|',texto.split('=== Confusion Matrix ===')[1],re.M)])
  assert matriz.shape==(3,3) and matriz.sum()==892
  fs,macro_exacto,ponderado_exacto=desde_matriz(matriz)
  valores=[]; soportes=[]; derivados=[]
  for i,clase in enumerate(CLASES):
   linea=next(l for l in seccion.splitlines() if l.strip().endswith(' '+clase)); partes=linea.split(); valor=partes[4]
   if valor=='?': valores.append(float(fs[i])); derivados.append(clase)
   else:
    valores.append(float(valor)); assert abs(float(valor)-fs[i])<=0.00051
  ponderado=seccion.split('Weighted Avg.')[1].split()[4]
  fpond=ponderado_exacto if ponderado=='?' else float(ponderado)
  if ponderado!='?': assert abs(fpond-ponderado_exacto)<=0.00051
  exactitud=float(re.search(r'^Correctly Classified Instances\s+\d+\s+([\d.]+)\s*%',texto,re.M).group(1))
  assert abs(exactitud-np.trace(matriz)/matriz.sum()*100)<=0.000051
  notas='Salida GUI existente; F1 macro = promedio simple de F-Measure por clase mostrado, con redondeo de tres decimales; F1 ponderado tomado de Weighted Avg. Diferencia de población respecto al catálogo completo: Weka usa 892 registros exportados; comparar también con enlace_exportacion_weka de Python. Particiones Java distintas; preprocesamiento anterior al CV.'
  if derivados: notas+=f' F-Measure ? de {derivados} resuelto desde matriz con 2TP/(2TP+FP+FN); no se copia otra herramienta.'
  if ponderado=='?': notas+=' Weighted Avg. original=?; F1 ponderado calculado desde la matriz, no reportado por Weka.'
  filas.append({'herramienta':'Weka','modelo':nombre,'esquema_evaluacion':'CV estratificada 10 pliegues; n=892; GUI 3.8.7; particiones y semilla CV no recuperadas', 'exactitud_pct':exactitud,'f1_macro':float(np.mean(valores)),'f1_ponderado':fpond,'notas':notas})
  detalle['Weka/'+nombre]={'matriz':matriz.tolist(),'f1_clases_usados':valores,'macro_desde_matriz_sin_redondeo':macro_exacto,'ponderado_desde_matriz_sin_redondeo':ponderado_exacto,'ponderado_mostrado':ponderado}
 # El clustering se conserva, sin atribuirle métricas de clasificación.
 for herramienta,nombre in [('Python','KMeans'),('Python','DBSCAN'),('Weka','SimpleKMeans'),('Weka','DBSCAN')]:
  filas.append({'herramienta':herramienta,'modelo':nombre,'esquema_evaluacion':'Clustering descriptivo; n=887; sin validación de clasificación','exactitud_pct':'','f1_macro':'','f1_ponderado':'','notas':'No aplican métricas de clasificación. Resultados existentes en reports/clustering.md (Python) y reports/weka/kmeans.txt o dbscan.txt (Weka); no se reejecutó clustering.'})
 pd.DataFrame(filas,columns=['herramienta','modelo','esquema_evaluacion','exactitud_pct','f1_macro','f1_ponderado','notas']).to_csv(SALIDA/'comparativo_herramientas.csv',index=False)
 pd.DataFrame(folds_guardados).to_csv(SALIDA/'comparativo_folds.csv',index=False)
 pd.DataFrame(pred_guardadas).to_csv(SALIDA/'comparativo_predicciones_oof.csv',index=False)
 (SALIDA/'comparativo_detalle.json').write_text(json.dumps(detalle,ensure_ascii=False,indent=2)+'\n')
 assert set(pd.read_csv(SALIDA/'comparativo_herramientas.csv').herramienta)=={'Python','Weka'}
 print('Verificaciones de matrices, métricas y particiones: correctas.',flush=True)
if __name__=='__main__': ejecutar()

````

## graficas_comparacion_corregida.jpg

Ruta: `Final/reports/tables/graficas_comparacion_corregida.jpg` · Bytes: 111632 · SHA-256: `892d698cf3d396c3b073baf9f26b4f475a5294bb1ac6e4e6eb3a9a9e4f960c05`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## graficas_logaritmicas_corregidas.jpg

Ruta: `Final/reports/tables/graficas_logaritmicas_corregidas.jpg` · Bytes: 120421 · SHA-256: `996ea8350196b45432fab66f31facd042b0c8d620f734a94e1da6114c08d9d7d`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## graficas_movil_corregidas.jpg

Ruta: `Final/reports/tables/graficas_movil_corregidas.jpg` · Bytes: 43548 · SHA-256: `82b2455e83ab4e2dfef1dd9839f2b66bf22f4503c96a4c208025b1eb7bb67e5d`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## graficas_permutacion_corregida.jpg

Ruta: `Final/reports/tables/graficas_permutacion_corregida.jpg` · Bytes: 120924 · SHA-256: `ff7bb67d0b45a90155873507e0b08446e8b53efedee89267c876cd5e48f027ea`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## integridad_visual_antes.json

Ruta: `Final/reports/tables/integridad_visual_antes.json` · Bytes: 2083 · SHA-256: `5d825727e56e27d23954ed0c918a86376e0cb8003ed1e4cbebed11a7b830bad5`

````text
{
  "data/raw/games_curated.csv": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
  "data/clean/diccionario_weka.csv": "c3cf64a5d5c74e02c4a7f7fb0f78b66cfaf5d25ccc155dcbb4461093a4bbaf4d",
  "data/clean/clustering_weka.arff": "78e7c49499f1f2112d22a991a5edcc0400b5778fe7413011b71413c34433aea7",
  "data/clean/clustering_espacio.csv": "9b0627ba170dba5eed9b1fc22fe02020d175f07d71addd91280279cfe43f8a1d",
  "data/clean/prueba_weka.arff": "75bf00752c63bbedce8e533ba8733ffe53a85a4847057000831007d7ec51f3bd",
  "data/clean/games_curated.csv": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
  "data/clean/entrenamiento_orange.csv": "f1040a9670bf08c0a717d39951971c3ec0335bf605b2b69b228f26b0d38c9908",
  "data/clean/dataset_con_clusters.csv": "d35537b44658aeeefbacd0ebac8c6cd785e73004e5ec0b1ac7baf3c82fd4077a",
  "data/clean/entrenamiento_weka.arff": "05f32bfce2ee083011da37866380b53a2beb6d79f627a991ec87ff29a1f04138",
  "data/clean/dataset_depurado.csv": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "data/clean/prueba_orange.csv": "1c6f667c3c34904f1ade594308cfc8efc5f25609589b74b55f3e2220608160b9",
  "data/clean/clustering_orden.csv": "e70aea9dd1d83f78ce7b5b0aeaa7f4d7d5b85baf9cf686860cbbaba418a0128d",
  "data/clean/juegos_modelo.csv": "cfc50959cc9e65ba6ba50004d84215e5eb06d58ce67df31cf1c8671e80457685",
  "data/clean/duplicados_limpieza.csv": "50ce0e30026c21e4892332b916a924b85703fb494815dba160431a84a49efa6a",
  "data/clean/generos_largo.csv": "22d1c569bad95b50f0c880296a0ac85e5c44d4939b7c2d54c72276574e30beb0",
  "models/clustering_03.joblib": "a84cced97483f68cde7884d2422bd1e12d85d3e15edf350246417deeb43d36ff",
  "models/modelo_popularidad.joblib": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e",
  "models/metadata.json": "07ba1ce664747e68c06c7ab9dc799e8ccb565cf71e7222b3a6de9f8548eed2fa",
  "models/referencias_folds.json": "68a602b49e37bba5d190b571b7afcd4f876957780a02bae1456635d14e4a0cf8",
  "models/vecinos_popularidad.joblib": "23d0ad2353a64b567cd1c40d40b70735e4450ae9a2b731519ba5aa65a1f95415"
}
````

## integridad_visual_resultado.json

Ruta: `Final/reports/tables/integridad_visual_resultado.json` · Bytes: 114 · SHA-256: `9d2d590cd5306c91c13a911c98a217e7c447c4da2498559806e10976ee0895c6`

````text
{
  "archivos_verificados": 20,
  "archivos_modificados": 0,
  "resultado": "Datos y modelos sin modificaciones"
}
````

## revision_tipografia.json

Ruta: `Final/reports/tables/revision_tipografia.json` · Bytes: 2843 · SHA-256: `ca77f8404b01b5d8fe3707eb8a20cc9a72957891ffecc8d01d0aa31b065917c9`

````text
[
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 172,
    "snippet": "border-right: 4px solid var(--p5-red) !important"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1438,
    "snippet": "border-left: 7px solid var(--p5-red)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1447,
    "snippet": "border-left: 9px solid var(--p5-yellow)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1590,
    "snippet": "border-right: 3px solid var(--p5-yellow)"
  },
  {
    "antipattern": "side-tab",
    "name": "Side-tab accent border",
    "description": "Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. Use a subtler accent or remove it entirely.",
    "severity": "warning",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 1614,
    "snippet": "border-left: 6px solid var(--p5-red)"
  },
  {
    "antipattern": "bounce-easing",
    "name": "Bounce or elastic easing",
    "description": "Bounce and elastic easing feel dated and tacky. Real objects decelerate smoothly — use exponential easing (ease-out-quart/quint/expo) instead.",
    "severity": "advisory",
    "category": "slop",
    "file": "/Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/assets/css/persona5.css",
    "line": 316,
    "snippet": "cubic-bezier(0.34, 1.56, 0.64, 1)",
    "advisory": true
  }
]

````

## test_comparabilidad.py

Ruta: `Final/reports/tables/test_comparabilidad.py` · Bytes: 2664 · SHA-256: `844c10c6186a711cef430c8ac193c3241792482ee3e20e458c6cab824cd10f52`

````text
"""Verificación independiente de métricas, cobertura OOF y evidencia gráfica."""
from pathlib import Path
import json, re
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
B=Path(__file__).resolve().parents[2]; T=B/'reports/tables'; C=['alto','bajo','medio']
def test_predicciones_y_metricas_independientes():
 tabla=pd.read_csv(T/'comparativo_herramientas.csv'); pred=pd.read_csv(T/'comparativo_predicciones_oof.csv')
 assert set(tabla.herramienta)=={'Python','Weka'}
 for (cohorte,modelo),g in pred.groupby(['cohorte','modelo']):
  n={'catalogo_completo':1117,'catalogo_elegible':1114,'enlace_exportacion_weka':892}[cohorte]
  assert len(g)==n and g.fila.nunique()==n
  m=confusion_matrix(g.real,g.predicha,labels=C); tp=np.diag(m)
  den=m.sum(0)+m.sum(1); f=np.divide(2*tp,den,out=np.zeros(3),where=den!=0)
  r=tabla[(tabla.herramienta=='Python')&(tabla.modelo==modelo)&tabla.esquema_evaluacion.str.contains('; '+cohorte+';')].iloc[0]
  assert np.isclose(r.exactitud_pct,100*tp.sum()/n)
  assert np.isclose(r.f1_macro,f.mean()) and np.isclose(r.f1_ponderado,np.average(f,weights=m.sum(1)))
def test_folds_reproducibles_y_dummy():
 folds=pd.read_csv(T/'comparativo_folds.csv'); pred=pd.read_csv(T/'comparativo_predicciones_oof.csv')
 for cohorte,g in folds.groupby('cohorte'):
  g=g.sort_values('fila'); assert g.fila.nunique()==len(g) and g.fold.nunique()==10
  y=g.clase.to_numpy(); esperado=np.zeros(len(g),int)
  for numero,(a,b) in enumerate(StratifiedKFold(10,shuffle=True,random_state=42).split(np.zeros(len(g)),y),1):
   esperado[b]=numero
   clases,cuentas=np.unique(y[a],return_counts=True); mayor=clases[np.argmax(cuentas)]
   p=pred[(pred.cohorte==cohorte)&(pred.modelo=='DummyClassifier')].sort_values('fila')
   assert (p.predicha.to_numpy()[b]==mayor).all()
  assert np.array_equal(g.fold.to_numpy(),esperado)
def test_weka_redondeo_y_capturas():
 tabla=pd.read_csv(T/'comparativo_herramientas.csv'); d=json.loads((T/'comparativo_detalle.json').read_text())
 for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
  r=tabla[(tabla.herramienta=='Weka')&(tabla.modelo==nombre)].iloc[0]; evidencia=d['Weka/'+nombre]
  assert np.isclose(r.f1_macro,np.mean(evidencia['f1_clases_usados']))
  assert abs(r.f1_macro-evidencia['macro_desde_matriz_sin_redondeo'])<=.00051
  assert abs(r.f1_ponderado-evidencia['ponderado_desde_matriz_sin_redondeo'])<=.00051
 for nombre in ['ZeroR.png','NaiveBayes.png','J48.png','RandomForest.png','kmeans_resultado.png','dbscan_resultado.png']:
  with Image.open(B/'reports/weka'/nombre) as im: im.verify()

````

## tipografia_comic_formulario.jpg

Ruta: `Final/reports/tables/tipografia_comic_formulario.jpg` · Bytes: 102549 · SHA-256: `d41bfd03033b1b007844a5291077275ba789d1b48858797436884addb9112549`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## tipografia_comic_inicio.jpg

Ruta: `Final/reports/tables/tipografia_comic_inicio.jpg` · Bytes: 142160 · SHA-256: `d4e01c5f34a91e7146074c4458c69f042d598badeb8c004cad42f81f53a67fb0`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## tipografia_comic_movil.jpg

Ruta: `Final/reports/tables/tipografia_comic_movil.jpg` · Bytes: 65153 · SHA-256: `a6a6c99c92c81c72bce17aeddb669d3d768004d3caabf2bad144e618de14372c`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## web_prediccion.png

Ruta: `Final/reports/tables/web_prediccion.png` · Bytes: 146425 · SHA-256: `b16916293898e32cebd824b6bea9b4803e396c84bd3fc951005a5f86dc890049`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## web_submenu_modelo.png

Ruta: `Final/reports/tables/web_submenu_modelo.png` · Bytes: 132979 · SHA-256: `8a870bf65a05cbd28bfb6c1588aa355f573f6d1e2843fd45f5e88637238c81f2`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## web_submenu_tras_filtro.png

Ruta: `Final/reports/tables/web_submenu_tras_filtro.png` · Bytes: 141664 · SHA-256: `dbf2c64ac33c32e07da3302e6b672685bbc9f1fb9011245caaf55b9f0c76d1c8`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

