# Modelo supervisado corregido tras la segunda auditoría

## Objetivo y separación de datos

Se mantiene el índice de rangos percentiles de Plays, Wishlist y Backlogs con pesos iguales. Solo Plays es más simple, pero omite interés pendiente; el índice elegido da dos tercios del peso a dos señales de interés correlacionadas. Playing se usa en EDA/clustering, pero no en el target ni como predictor del clasificador.

Antes de calcular etiquetas se divide por grupos de título mediante GroupShuffleSplit con semilla 42: 892 entrenamiento y 222 prueba. La proporción 80/20 es aproximada por grupos; no se fuerza estratificación en clases aún no definidas ni se buscan repartos por rechazo.

En entrenamiento se ajustan los rangos medios/N y sus terciles: [0.3622944693572496, 0.6266816143497758]. La prueba se interpola contra esos mismos valores, con percentil 0 por debajo del mínimo y 1 sobre el máximo de entrenamiento. Los empates comparten etiqueta. La referencia tiene N=892; nunca usa los conteos de prueba.

La CV de diez pliegues agrupa títulos y organiza estratos con las etiquetas externas de entrenamiento. Dentro de cada fit se recalculan referencia, cortes, etiquetas, categorías e imputación usando solo el subentrenamiento; score construye las etiquetas de validación con esa referencia local. GridSearchCV recibe un estimador de contexto que separa las tres señales del objetivo de las cinco entradas predictivas. Las referencias e IDs se guardan en models/referencias_folds.json.

## Entradas y Naive Bayes

Predictores: ['generos', 'estudio', 'decada', 'Metacritic Rating', 'Rating']. Ningún conteo, índice, cluster, componente PCA, indicador de procedencia o bandera de ausencia entra al Pipeline final.

Géneros frecuentes: multi-hot de hasta 15 con frecuencia mínima 20 en cada ajuste. Estudio representa organizaciones de Team con mínimo 10; Otro se activa solo cuando no existe ninguna organización frecuente en la lista. Las listas vacías usan Sin dato; no se atribuye rol desarrollador por posición.

Notas: mediana ajustada solo con entrenamiento, sin MissingIndicator. StandardScaler se aplica exclusivamente a las dos notas continuas para árboles/bosque/referencia; los otros indicadores se mantienen en 0/1. La curación de Metacritic sigue siendo una fuente posible de sesgo no aleatorio, aun sin bandera explícita.

Se reemplaza GaussianNB por CategoricalNB: la mayoría de atributos son indicadores categóricos y las dos notas se discretizan en cinco intervalos de ancho uniforme entre los extremos de entrenamiento de cada fold. min_categories=5 permite códigos nuevos dentro del rango; alpha se ajusta en tres valores. Se reconoce pérdida de resolución por discretización e independencia condicional aproximada; no se ajustan gaussianas a decenas de dummies raras.

## Comparación y selección

| modelo | f1_macro_cv | desviacion_cv | exactitud_prueba | f1_macro_prueba | balanced_accuracy_prueba | mejores_parametros |
| --- | --- | --- | --- | --- | --- | --- |
| DummyClassifier | 0.1678 | 0.0031 | 0.3018 | 0.1546 | 0.3333 | {} |
| CategoricalNB | 0.5490 | 0.0625 | 0.5090 | 0.4925 | 0.5192 | {"pipeline__clasificar__alpha": 5.0} |
| DecisionTreeClassifier | 0.5053 | 0.0458 | 0.5315 | 0.5119 | 0.5433 | {"pipeline__clasificar__max_depth": 8, "pipeline__clasificar__min_samples_leaf": 10} |
| RandomForestClassifier | 0.5567 | 0.0451 | 0.5676 | 0.5577 | 0.5753 | {"pipeline__clasificar__max_depth": null, "pipeline__clasificar__min_samples_leaf": 5} |

Ganador por F1 macro media de CV: **RandomForestClassifier**. Supera al modelo de referencia en esta partición; no se ha probado significancia estadística de la diferencia. Diferencia en prueba frente a referencia: 0.4031. No se usa la prueba para ajustar parámetros o cambiar ganador.

**Limitación visible del ganador:** recall de la clase medio = 33.8%. Una exactitud global razonable no permite afirmar que identifique bien esa clase; no se hizo una nueva búsqueda usando estos errores de prueba.

Dummy usa la clase realmente más frecuente en cada ajuste, con etiquetas locales; si hay empate, sklearn desempata por orden de clases. Los terciles tienden a equilibrar por construcción incluso sin fuga, por lo que una referencia mayoritaria cercana a F1 macro 1/6 es esperable y no un modelo comercial inteligente.

## Matrices y análisis de error por clase

Filas reales y columnas predichas: bajo, medio, alto.

### DummyClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 67 | 0 | 0 |
| medio | 80 | 0 | 0 |
| alto | 75 | 0 | 0 |

### CategoricalNB

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 42 | 12 | 13 |
| medio | 35 | 19 | 26 |
| alto | 11 | 12 | 52 |

### DecisionTreeClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 45 | 13 | 9 |
| medio | 34 | 18 | 28 |
| alto | 8 | 12 | 55 |

### RandomForestClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 43 | 14 | 10 |
| medio | 32 | 27 | 21 |
| alto | 9 | 10 | 56 |

| modelo | clase | n | aciertos | recall |
| --- | --- | --- | --- | --- |
| DummyClassifier | bajo | 67 | 67 | 1.0000 |
| DummyClassifier | medio | 80 | 0 | 0.0000 |
| DummyClassifier | alto | 75 | 0 | 0.0000 |
| CategoricalNB | bajo | 67 | 42 | 0.6269 |
| CategoricalNB | medio | 80 | 19 | 0.2375 |
| CategoricalNB | alto | 75 | 52 | 0.6933 |
| DecisionTreeClassifier | bajo | 67 | 45 | 0.6716 |
| DecisionTreeClassifier | medio | 80 | 18 | 0.2250 |
| DecisionTreeClassifier | alto | 75 | 55 | 0.7333 |
| RandomForestClassifier | bajo | 67 | 43 | 0.6418 |
| RandomForestClassifier | medio | 80 | 27 | 0.3375 |
| RandomForestClassifier | alto | 75 | 56 | 0.7467 |

La clase media se evalúa explícitamente: sus notas y géneros pueden solaparse con ambos extremos y sus fronteras son cortes artificiales de un continuo. Es una hipótesis interpretativa, no una causa demostrada; el recall observado no se oculta bajo la exactitud global. El rendimiento de CategoricalNB se informa por clase y no se presenta la antigua matriz de GaussianNB como resultado vigente.

## Permutation importance

| variable_cruda | caida_f1_macro_media | desviacion |
| --- | --- | --- |
| Rating | 0.0832 | 0.0221 |
| Metacritic Rating | 0.0817 | 0.0226 |
| generos | 0.0753 | 0.0211 |
| estudio | 0.0276 | 0.0164 |
| decada | 0.0193 | 0.0149 |

Caída de F1 macro sobre la prueba al permutar cada entrada cruda (listas completas para género/estudio), con 30 repeticiones y semilla 42. No es efecto causal ni intervalo de confianza; las variables correlacionadas comparten información. No se reoptimiza después de verla.

## Diagnóstico de cobertura de prensa y categoría Otro

{
  "prevalencia_otro": [
    {
      "particion": "entrenamiento",
      "fraccion_estudio_otro": 0.3968609865470852
    },
    {
      "particion": "prueba",
      "fraccion_estudio_otro": 0.44144144144144143
    }
  ],
  "n_criticas_ocultadas": 180,
  "delta_probabilidad_bajo_media": 0.03884582502696399,
  "delta_probabilidad_bajo_mediana": 0.008101477935920781,
  "f1_macro_ablacion_sin_critica": 0.5149234278266537,
  "limitacion": "La imputación puede seguir codificando cobertura; eliminar el indicador no garantiza ausencia de sesgo MNAR. Ablación de prueba solo diagnóstica, no reselección."
}

Las tablas modelo_ausencia_entrenamiento/prueba.csv muestran distribución de clases con y sin crítica. modelo_sensibilidad_critica.csv cuantifica el cambio de probabilidad baja al ocultar notas conocidas manteniendo los otros datos. La ablación sin crítica reutiliza parámetros elegidos y es diagnóstica: no selecciona otro modelo ni demuestra equidad. No se concluye que un Otro frecuente causara una importancia baja solo por observar ambos.

## Uso y reproducibilidad

models/modelo_popularidad.joblib contiene directamente el Pipeline y acepta un DataFrame con las cinco columnas crudas, listas o textos para categorías y nulos para notas. Las clases propias se serializan por valor con cloudpickle, compatible con joblib.load desde un proceso limpio sin src en PYTHONPATH; se conserva la dependencia de versiones de sklearn/pandas/numpy/cloudpickle.

models/metadata.json conserva referencia de entrenamiento, cortes, versiones, clases, fecha y métricas. models/vecinos_popularidad.joblib guarda NearestNeighbors ajustado únicamente al espacio predictivo de entrenamiento: las etiquetas de clusters solo se adjuntan por ID después de buscar, no intervienen en las distancias ni en la clasificación.

Fecha: 2026-11-08T13:44:14-06:00; sklearn 1.9.1; Python 3.14.6. Las métricas previas de objetivo global están archivadas y no son directamente comparables con las nuevas.

## Que debo verificar manualmente

- Pesos y redundancia del índice, antigüedad y representatividad de Backloggd.
- Procedencia de notas y sesgo de cobertura; la mediana puede conservar señales indirectas de ausencia.
- Identidad de juegos homónimos y roles de Team; los tres conflictos históricos siguen excluidos.
- Vecinos como similitud de atributos declarados, no recomendaciones de éxito ni causalidad.
- Probabilidades no calibradas y límites de la clase media.
