# Carpeta: Final/reports/archivo_modelo_pre_auditoria2/reports

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## modelo.md

Ruta: `Final/reports/archivo_modelo_pre_auditoria2/reports/modelo.md` · Bytes: 7957 · SHA-256: `2f283598f1a8883190899e141b891666c22442dc5cac059c491dc2ba198ab93b`

````text
# Modelo supervisado de nivel de popularidad

## Diseño del objetivo

| Opción | Qué mide | Ventaja | Límite |
|---|---|---|---|
| Solo Plays | Alcance acumulado por terciles | Simple e interpretable | Favorece antigüedad y omite intención |
| Promedio de percentiles de Plays, Wishlist y Backlogs | Actividad e interés declarados | Evita que una escala domine | Dos señales de interés correlacionadas reciben dos tercios del peso |

**Elección.** Se recomienda el índice de tres percentiles porque la pregunta del proyecto es multidimensional. Es una definición operativa de popularidad relativa de Backloggd, no una medida de ventas o rentabilidad; Playing no forma parte de este objetivo ni de sus predictores.

Fórmula: (rango_percentil(Plays) + rango_percentil(Wishlist) + rango_percentil(Backlogs)) / 3. Se usa rango medio para empates dividido por N. Cortes: [0.36280670257330944, 0.6237283064033513]. bajo: índice <= corte1; medio: corte1 < índice <= corte2; alto: índice > corte2. Los empates nunca se dividen artificialmente y los tamaños pueden diferir.

Cohorte elegible: 1114 juegos. Concordancia de categorías con usar solo Plays: 60.6%.

**Alcance de las etiquetas.** La referencia y los terciles se definen y congelan en el catálogo completo elegible antes de dividir. Por tanto la prueba evalúa categorías descriptivas de ese catálogo, no cortes futuros independientes. Las distribuciones de la prueba sí forman parte de la definición del target: no se presenta este procedimiento como si sus cortes se hubieran estimado solo en entrenamiento.

## Entradas y preprocesamiento

Variables crudas esperadas por el Pipeline guardado: ['generos', 'estudio', 'decada', 'Metacritic Rating', 'Rating']. No incluyen Plays, Wishlist, Backlogs, Playing, percentiles, índice ni etiquetas de clustering.

**Géneros.** Multi-hot de hasta los 15 géneros con al menos 20 juegos en el entrenamiento de cada fold; el resto y los nuevos van a Otro. Se preservan pertenencias múltiples y no se selecciona un género principal arbitrario.

**Estudio.** Se conservan miembros de Team con al menos diez juegos en el entrenamiento de cada fold; los raros o desconocidos van a Otro y las ausencias a Sin dato. Team no distingue desarrolladores de editores: la entrada estudio representa organizaciones sin rol verificado, sin asignar el último elemento como desarrollador.

**Notas y década.** Notas con mediana e indicador de ausencia y después StandardScaler; década con categoría de ausencia -1 y one-hot. ColumnTransformer y todos sus ajustes viven dentro del Pipeline: reciben las listas, notas y década crudas del formulario y se reajustan en cada fold.

**Naive Bayes.** Se usa GaussianNB porque la salida combina indicadores binarios y variables numéricas continuas. MultinomialNB exigiría características no negativas tras el escalado y BernoulliNB descartaría la magnitud de las notas al binarizarlas; GaussianNB admite la matriz densa, aunque normalidad de indicadores e independencia de géneros/organizaciones son aproximaciones fuertes.

## Partición, validación y selección

80/20 estratificado con semilla 42: 891 entrenamiento y 223 prueba. Se aceptó el primer reparto sin títulos compartidos tras 1258 candidatos deterministas; no se eligió por métricas.

Validación de diez pliegues con StratifiedGroupKFold, shuffle=True y semilla 42 sobre entrenamiento. La estratificación se aproxima por fold respetando títulos indivisibles; las distribuciones reales y los IDs/folds se guardan en juegos_modelo.csv. GridSearchCV usa F1 macro y los mismos folds para todos los modelos; la prueba no selecciona ni hiperparámetros ni ganador.

Búsqueda ligera: Dummy sin ajuste; GaussianNB con tres var_smoothing; árbol con tres profundidades y dos tamaños mínimos de hoja; bosque de 200 árboles con dos profundidades y dos tamaños mínimos de hoja. Todos los algoritmos aleatorios usan random_state=42.

| modelo | f1_macro_cv | desviacion_cv | exactitud_prueba | f1_macro_prueba | balanced_accuracy_prueba | mejores_parametros |
| --- | --- | --- | --- | --- | --- | --- |
| DummyClassifier | 0.1641 | 0.0008 | 0.3318 | 0.1661 | 0.3333 | {} |
| GaussianNB | 0.4324 | 0.0308 | 0.4395 | 0.3914 | 0.4394 | {"clasificar__var_smoothing": 1e-05} |
| DecisionTreeClassifier | 0.4982 | 0.0303 | 0.4709 | 0.4612 | 0.4712 | {"clasificar__max_depth": 8, "clasificar__min_samples_leaf": 3} |
| RandomForestClassifier | 0.5356 | 0.0456 | 0.5919 | 0.5814 | 0.5917 | {"clasificar__max_depth": null, "clasificar__min_samples_leaf": 2} |

Modelo elegido por CV: **RandomForestClassifier**; parámetros: {'clasificar__max_depth': None, 'clasificar__min_samples_leaf': 2}.

**Comparación con referencia.** Supera al modelo de referencia en esta partición; no se ha probado significancia estadística de la diferencia. Diferencia F1 macro: 0.4153. Se definió “apenas” como mejora positiva de hasta 0.02, antes de interpretar el resultado; no es una prueba de significancia.

## Matrices de confusión en prueba

Filas: clase real. Columnas: clase predicha. Orden bajo, medio, alto.

### DummyClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 0 | 0 | 75 |
| medio | 0 | 0 | 74 |
| alto | 0 | 0 | 74 |

### GaussianNB

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 34 | 13 | 28 |
| medio | 24 | 6 | 44 |
| alto | 6 | 10 | 58 |

### DecisionTreeClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 29 | 30 | 16 |
| medio | 22 | 24 | 28 |
| alto | 7 | 15 | 52 |

### RandomForestClassifier

| real | bajo | medio | alto |
| --- | --- | --- | --- |
| bajo | 49 | 15 | 11 |
| medio | 26 | 27 | 21 |
| alto | 3 | 15 | 56 |

## Permutation importance sobre prueba

| variable_cruda | caida_f1_macro_media | desviacion |
| --- | --- | --- |
| Metacritic Rating | 0.1250 | 0.0210 |
| Rating | 0.0660 | 0.0162 |
| generos | 0.0641 | 0.0236 |
| decada | 0.0529 | 0.0149 |
| estudio | 0.0085 | 0.0145 |

Importancia medida como caída de F1 macro al permutar cada variable cruda, con 30 repeticiones y semilla 42. La permutación de géneros/estudio mueve la lista completa de cada fila, no indicadores aislados; media y desviación no son intervalos de confianza.

Es un diagnóstico del modelo elegido, no evidencia causal. Las variables correlacionadas pueden compartir u ocultar importancia y valores negativos pueden aparecer por variación de la muestra. Estos resultados de prueba no se usan para otra búsqueda ni para retirar atributos.

## Uso del artefacto

models/modelo_popularidad.joblib contiene directamente el Pipeline. Se carga con joblib.load y predict recibe un DataFrame con las cinco columnas crudas listadas. Géneros y estudio aceptan listas, listas serializadas o un nombre de texto; no se pide al usuario codificar, imputar ni escalar.

models/metadata.json conserva versión sklearn, clases, fecha de México, variables, definición completa del target, referencias ordenadas, cortes, métricas y parámetros. El Pipeline evaluado se conserva ajustado solo con entrenamiento; no se reajusta con prueba. Las probabilidades no están calibradas.

Fecha de ejecución: 2026-11-08T12:25:51-06:00; Python 3.14.6; sklearn 1.9.1; SHA-256 de dataset_depurado: f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652.

## Que debo verificar manualmente

- Pesos del objetivo y redundancia entre Wishlist y Backlogs; sus terciles son relativos al catálogo observado.
- Identidad y función de organizaciones; títulos compartidos no equivalen a franquicias identificadas.
- Sesgo de selección y antigüedad; no se estima éxito anterior al estreno con notas posteriores.
- Las etiquetas incorporan la distribución del catálogo completo: para un estudio prospectivo se necesita una referencia externa o congelada antes de una nueva cohorte.
- Probabilidades sin calibrar, poca muestra de estudios y posibles cambios de mercado.

````

## modelo_comparacion.csv

Ruta: `Final/reports/archivo_modelo_pre_auditoria2/reports/modelo_comparacion.csv` · Bytes: 764 · SHA-256: `cbc2cc19dbd48c702f3c3b43768c76d5f99418ffd5bfb6fb91a806765d704169`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_confusion_GaussianNB.csv

Ruta: `Final/reports/archivo_modelo_pre_auditoria2/reports/modelo_confusion_GaussianNB.csv` · Bytes: 73 · SHA-256: `dc40bde62d3af2e0926331d4daae307c8c0edf9ab232c2208592b6da16cbd354`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_grid_cv.csv

Ruta: `Final/reports/archivo_modelo_pre_auditoria2/reports/modelo_grid_cv.csv` · Bytes: 14503 · SHA-256: `4cfd46177f999520c86bb0aa647f357a83bde1ae7020d4dc1ef18198c13076b7`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## modelo_permutation_importance.csv

Ruta: `Final/reports/archivo_modelo_pre_auditoria2/reports/modelo_permutation_importance.csv` · Bytes: 299 · SHA-256: `6f0bec02f2971394ea3271a347687a2838189424c7867d6cfe4107e5b490012b`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

