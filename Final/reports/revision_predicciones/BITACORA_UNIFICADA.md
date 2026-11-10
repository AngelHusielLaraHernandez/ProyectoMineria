# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/revision_predicciones/ejecucion.txt

SHA-256: `4e8c4bbd9f547365a4641a6e14668a1d4d7cf84f27d7d534628b52a4df4ea28d`

````text
Auditoría de integridad completada.
Vigente: F1 CV=0.5567
RF_revision_1: F1 CV=0.5403
RF_revision_2: F1 CV=0.5508
RF_revision_3: F1 CV=0.5510
RF_revision_4: F1 CV=0.5427
RF_revision_5: F1 CV=0.5374
RF_revision_6: F1 CV=0.5300
RF_revision_7: F1 CV=0.5368
{"ganador_cv": "Vigente", "mejora_f1_cv": 0.0, "pliegues_superiores": 0, "criterio_predefinido": "Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.", "recomienda_promocion": false, "parametros": {"bootstrap": true, "ccp_alpha": 0.0, "class_weight": null, "criterion": "gini", "max_depth": null, "max_features": "sqrt", "max_leaf_nodes": null, "max_samples": null, "min_impurity_decrease": 0.0, "min_samples_leaf": 5, "min_samples_split": 2, "min_weight_fraction_leaf": 0.0, "monotonic_cst": null, "n_estimators": 200, "n_jobs": 1, "oob_score": false, "random_state": 42, "verbose": 0, "warm_start": false}, "limitacion": "Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva."}

````

## Origen: Final/reports/revision_predicciones/pruebas.txt

SHA-256: `a31747bb2f56fc4588546a71b681c00e1f4f82bc0018e97fa60077a1f45a0134`

````text
.......................................                                  [100%]
=============================== warnings summary ===============================
tests/test_inferencia.py::test_interfaz_envia_valores_del_formulario
  /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/.venv/lib/python3.15/site-packages/joblib/externals/loky/backend/context.py:134: UserWarning: Could not find the number of physical cores for the following reason:
  invalid literal for int() with base 10: ''
  Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
39 passed, 1 warning in 15.20s

````

## Origen: Final/reports/revision_predicciones/render.log

SHA-256: `d8963fe932f6957b471ee8a0a0f820eaf2f2e75957fe1adb3a0942593e55c1f5`

````text
Pages rendered to /Users/angellara/Documents/NovenoSemestre/ProyectoMineria/Final/reports/revision_predicciones/render_documento

````
