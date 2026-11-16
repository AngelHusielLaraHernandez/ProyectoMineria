# Hallazgos de Weka y validación web

Informe técnico de avance • 9 de noviembre de 2026 • Versión 1

El modelo de la web reproduce correctamente las predicciones almacenadas y conserva la separación entre entrenamiento y prueba. Su capacidad predictiva es moderada: obtiene 56.76 % de exactitud y F1 macro de 0.5577 en 222 casos de prueba. La clase media sigue siendo la principal debilidad. Siete variantes nuevas del bosque no mejoraron la validación cruzada del modelo vigente, por lo que se conservó ese artefacto.

Este informe integra las corridas gráficas existentes de Weka, su contraste metodológico con Python y las verificaciones de la aplicación Streamlit. Los resultados describen popularidad relativa en un catálogo curado, no ventas, rentabilidad ni probabilidad de éxito comercial de un lanzamiento.

| Población comprobada | Registros | Uso |
| --- | --- | --- |
| Antecedente histórico | 1,512 | Auditoría de decisiones heredadas |
| Maestro games_curated.csv | 1,117 | Original designado con 42 columnas |
| Cohorte elegible | 1,114 | Análisis principal y clasificación |
| Casos completos de clustering | 887 | Seis variables sin ausencias |
| Entrenamiento y prueba | 892 y 222 | Partición por grupos de título |

El archivo en data/raw ya es un maestro curado. El antecedente de 1,512 filas se conserva aparte; no debe presentarse como si la limpieza actual hubiera recibido 1,512 filas. La web se aclaró para distinguir HIST y MAESTRO.

En los 887 pares elegibles con ambas notas, Pearson es 0.5439 con p = 1.936 × 10⁻⁶⁹ y Spearman es 0.5242. Es evidencia de asociación entre recepción de usuarios y prensa, no de acuerdo exacto ni de causalidad.

Fuentes: reports/inspeccion.md; reports/trazabilidad_historica.md; reports/clustering.md; reports/revision_predicciones/auditoria.json.

## Clasificación observada en Weka

Weka Explorer 3.8.7 evaluó 892 registros con 53 atributos, incluida la clase nominal nivel_popularidad, mediante validación cruzada de diez pliegues. Se verificaron las cuatro matrices originales: sus sumas son 892 y sus diagonales reproducen la exactitud publicada por el programa.

| Herramienta | Modelo | Exactitud % | F1 macro | F1 pond |
| --- | --- | --- | --- | --- |
| Weka | ZeroR | 33.0717 | 0.2533 | 0.2533 |
| Weka | NaiveBayes | 50.8969 | 0.5033 | 0.5030 |
| Weka | J48 | 51.0090 | 0.5063 | 0.5060 |
| Weka | RandomForest | 53.4753 | 0.5300 | 0.5300 |
| Python enlace | Dummy | 33.0717 | 0.2531 | 0.2533 |
| Python enlace | GaussianNB | 47.4215 | 0.4437 | 0.4438 |
| Python enlace | Árbol CART | 46.9731 | 0.4693 | 0.4694 |
| Python enlace | Random Forest | 54.8206 | 0.5442 | 0.5442 |

RandomForest fue el mejor clasificador de las cuatro corridas de Weka, con 477 aciertos de 892. Su F1 para la clase medio fue 0.381 y su recall 0.360, por debajo de los otros dos niveles; la dificultad de la clase central también aparece en Python.

El F1 macro de Weka promedia los F Measure por clase impresos a tres decimales. En ZeroR el valor no definido de medio se resolvió desde la matriz con la convención de cero; el F1 ponderado de 0.2533 también se calculó desde la matriz porque Weka imprimió un signo de interrogación. Los otros ponderados son los reportados por Weka.

Python enlace usa los mismos 892 registros y 52 predictores numéricos exportados, pero no los mismos pliegues de Java. NaiveBayes y GaussianNB tienen tratamientos distintos; J48 y CART son árboles diferentes. Weka usa 100 árboles y semilla del estimador 1; Python enlace usa 100 y semilla 42. La semilla de los pliegues de la sesión Weka no pudo recuperarse. El preprocesamiento de esta comparación se hizo antes de CV; no sustituye la evaluación de producción con preprocesamiento por pliegue.

Fuentes: reports/weka/ZeroR.txt, NaiveBayes.txt, J48.txt y RandomForest.txt; reports/tables/comparativo_herramientas.csv; revision_predicciones/weka_recalculado.json.

## Segmentación observada en Weka

SimpleKMeans utilizó k = 2 y semilla 42 sobre 887 instancias y seis atributos. Convergió en nueve iteraciones y produjo grupos de 477 y 410 juegos. Los centroides siguientes están en las unidades transformadas del archivo exportado, no en conteos originales ni puntos de calificación.

| Variable | Centro del grupo 0 | Centro del grupo 1 |
| --- | --- | --- |
| Plays | 0.4100 | −0.4770 |
| Playing | 0.6189 | −0.7200 |
| Backlogs | 0.7093 | −0.8252 |
| Wishlist | 0.6912 | −0.8042 |
| Rating | 0.4797 | −0.5581 |
| Metacritic Rating | 0.4270 | −0.4968 |

Los signos de los centros describen un perfil con mayor actividad, interés y recepción frente a otro con valores inferiores al promedio exportado. Es una interpretación descriptiva del catálogo y no prueba que existan segmentos comerciales naturales. Las etiquetas numéricas de los grupos son arbitrarias.

| Resultado | Python | Weka |
| --- | --- | --- |
| K Means con dos grupos | 465 y 422 | 477 y 410 |
| DBSCAN grupos válidos | 1 | 1 |
| DBSCAN asignados al grupo | 866 | 887 |
| DBSCAN ruido | 21 | 0 |

En Python k = 2 maximizó silhouette entre 2 y 10, con 0.3188. Weka no reportó esa métrica en la corrida guardada; no se le atribuye el valor de Python. Las sumas de cuadrados tampoco se comparan como si provinieran de una configuración de distancias idéntica.

DBSCAN se ejecutó en Weka con eps = 1.666296 y minPoints = 12. Agrupó las 887 instancias en un solo grupo. En Python, los mismos parámetros nominales dejaron 21 casos como ruido. La igualdad de eps no acredita equivalencia de la distancia interna: Weka informa EuclideanDistance con sus opciones y las implementaciones no son una réplica exacta. No se forzaron parámetros ni se corrigieron las salidas para hacerlas coincidir.

Fuentes: reports/weka/kmeans.txt y dbscan.txt; reports/clustering.md; reports/clustering_03_perfiles.csv.

## Hallazgos y correcciones de la web

La aplicación mantiene cuatro páginas: Inicio, Exploración, Predicción y Modelo. Permite consultar señales de popularidad, asociaciones entre notas, perfiles de clustering, predicciones y vecinos del entrenamiento. La identidad azul y morada y la fuente cómic local se aplican sin modificar los datos analíticos.

Se corrigieron las cifras atravesadas por barras de error en los gráficos de desempeño e importancia por permutación. Las cifras se sitúan después del extremo del intervalo; se conservaron sus desviaciones y los rangos estadísticos. Los ejes logarítmicos muestran potencias de diez sin marcas menores amontonadas. En móvil, las figuras densas se desplazan dentro de su panel.

![Predicción comprobada en la interfaz con Adventure y RPG, organización Otro, década de 2020, Metacritic 100 y Rating 5. El modelo devuelve alto con 54.1 % de probabilidad no calibrada.](revision_predicciones/formulario_verificado.jpg)

La revisión del formulario añadió validación explícita de Rating de 0 a 5 y Metacritic de 0 a 100, conservando los nulos para la imputación entrenada. Se eliminó el ancho mínimo artificial de 2 % de las barras. Otro ahora significa organización no frecuente y no presume que sea un estudio independiente.

Fuentes: pages/2_Prediccion.py; src/inferencia.py; reports/BITACORA_UNIFICADA.md; revision_predicciones/casos_formulario.json.

## Verificación de las predicciones

Se compararon las 222 salidas del artefacto guardado con las predicciones de prueba almacenadas y todas coinciden. Las probabilidades son finitas, suman uno y su mayor valor corresponde a la clase mostrada, usando el orden real de pipeline.classes_. También se reprodujeron las etiquetas y los terciles desde la referencia de entrenamiento.

| Métrica en prueba | Resultado |
| --- | --- |
| Exactitud | 56.76 % |
| F1 macro | 0.5577 |
| F1 ponderado | 0.5540 |
| Recall bajo | 64.18 % |
| Recall medio | 33.75 % |
| Recall alto | 74.67 % |

| Clase real | Predice bajo | Predice medio | Predice alto |
| --- | --- | --- | --- |
| bajo | 43 | 14 | 10 |
| medio | 32 | 27 | 21 |
| alto | 9 | 10 | 56 |

Las entradas son géneros, organizaciones de Team, década, Metacritic Rating y Rating. Plays, Wishlist y Backlogs definen el objetivo y no entran al clasificador; Playing tampoco es predictor. Las categorías e imputaciones se ajustan en entrenamiento. Los títulos agrupados de entrenamiento y prueba no se superponen y el índice de vecinos contiene únicamente IDs de entrenamiento en el mismo espacio transformado.

La ausencia de prensa es una limitación concreta. En el caso comprobado de la página anterior, ocultar Metacritic manteniendo Rating 5 cambia alto a bajo, con 44.2 % para bajo. El cálculo coincide con el Pipeline; no es una inversión de etiquetas del formulario. La web muestra ahora un aviso sobre la imputación. Esto evidencia sensibilidad a la cobertura y no demuestra que un juego sin nota vaya a tener baja popularidad.

Se aprobaron 39 pruebas, incluidas escalas inválidas, valores extremos, organizaciones nuevas, ausencia de crítica y envíos del formulario contrastados con el Pipeline. Las probabilidades no están calibradas y los casos de demostración no constituyen validación externa.

Fuentes: models/metadata.json; revision_predicciones/auditoria.json y casos_formulario.json; tests/test_inferencia.py; revision_predicciones/pruebas.txt.

## Revisión del entrenamiento y decisión

Se reutilizaron exclusivamente los 892 registros de entrenamiento y sus diez pliegues agrupados por título. Cada ajuste recalcula objetivo local, vocabularios e imputación sin consultar su validación. Se entrenaron siete variantes nuevas de Random Forest más la referencia vigente, con 200 árboles y random_state 42: 80 ajustes en total.

| Candidato | Hoja mín | Ponderación | Variables | F1 CV |
| --- | --- | --- | --- | --- |
| Vigente | 5 | Sin ponderar | Raíz | 0.5567 |
| RF 3 | 5 | Balance por muestra | Raíz | 0.5510 |
| RF 2 | 2 | Balance por muestra | Raíz | 0.5508 |
| RF 4 | 10 | Balance por muestra | Raíz | 0.5427 |
| RF 1 | 1 | Sin ponderar | Raíz | 0.5403 |
| RF 5 | 2 | Sin ponderar | 0.5 | 0.5374 |
| RF 7 | 10 | Sin ponderar | 0.5 | 0.5368 |
| RF 6 | 5 | Balance por muestra | 0.5 | 0.5300 |

Raíz indica max_features igual a sqrt; 0.5 usa la mitad de las variables transformadas en cada división. Balance por muestra corresponde a class_weight igual a balanced_subsample. La profundidad se mantiene sin límite en estas variantes.

Antes de consultar sus resultados se fijó un criterio de promoción: mejora de al menos 0.01 en F1 macro y superioridad en seis de diez pliegues. Ninguna variante superó siquiera la media del modelo vigente, 0.5567. Se conservan el artefacto y sus métricas; no se presenta una mejora inexistente ni se selecciona un candidato por la prueba.

El mejor recall medio de alguna variante no basta para reemplazar al modelo si disminuye el F1 macro elegido como criterio. La búsqueda no es una CV anidada y amplía la exploración de hiperparámetros sobre los mismos pliegues; sus medias no son una estimación independiente del rendimiento futuro.

La prueba existente ya fue observada. Sin una muestra externa posterior no se puede afirmar una mejora prospectiva ni validar el uso del sistema para géneros nuevos o resultados comerciales. Estas limitaciones se documentan; no se sustituyen con cifras de entrenamiento.

Reproducción desde Final: python src/05_revision_predicciones.py. Evidencias: revision_predicciones/busqueda_folds.csv, busqueda_resumen.csv, decision.json y ejecucion.txt.

## Evidencias y límites del informe

![Corrida gráfica original de RandomForest en Weka. Las métricas del informe se extrajeron del texto guardado y se contrastaron con su matriz; la imagen aporta la evidencia visual de la sesión.](weka/RandomForest.png)

Las seis corridas gráficas conservan salidas y capturas locales: SimpleKMeans, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Esta revisión no reejecuta Weka ni cambia sus resultados. El script verificar_weka.py recalcula sus matrices de clasificación y conserva los hashes de las fuentes.

Orange se descartó por cierres de la aplicación en Qt y Cocoa al usar selectores de archivos. Se probaron la instalación local, recuperación y reinicio del lienzo, CSV y TAB, además de un lanzador con selectores Qt. No hay métricas de Orange en este informe; no se le atribuye ninguna salida de Weka.

La popularidad se refiere a rangos percentiles relativos de Plays, Wishlist y Backlogs. La muestra tiene sesgo de visibilidad comunitaria; Team no separa desarrolladores y publishers. Las notas con origen estimado se excluyen como evidencia independiente de prensa. Las columnas financieras estimadas del maestro no se utilizan para demostrar éxito comercial.

Trazabilidad principal: data/raw/games_curated.csv; reports/inspeccion.md; reports/trazabilidad_historica.md; reports/weka/; reports/BITACORA_UNIFICADA.md; reports/tables/comparativo_herramientas.csv; reports/revision_predicciones/.
