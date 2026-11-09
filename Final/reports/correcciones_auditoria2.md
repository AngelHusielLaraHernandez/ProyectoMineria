# Segunda auditoría: correcciones y límites vigentes

Se revisaron los hallazgos contra la implementación y se regeneró la fase 4B. Las correcciones previas de EDA, historia, maestro y clustering se conservan; los datos originales siguen intactos y no hay publicación autorizada.

## Cambios comprobables

| Hallazgo | Corrección / decisión | Evidencia |
|---|---|---|
| Target transductivo | Se retira la definición global usada antes de la partición. Primero se divide por título con GroupShuffleSplit, una sola vez y semilla 42; se ajustan percentiles y terciles en los 892 juegos de entrenamiento. Los 222 de prueba se interpolan contra esa referencia congelada. | src/objetivo.py, src/04_modelo.py, models/metadata.json y juegos_modelo.csv. Mutar señales solo en prueba deja intacta la referencia, comprobado por tests. |
| Target dentro de cada fold | GridSearchCV usa ClasificadorObjetivoLocal: fit recibe el contexto y ajusta una referencia local; el Pipeline solo recibe las cinco entradas predictivas. score calcula la verdad de validación con la referencia de ese mismo subentrenamiento, ignorando las etiquetas externas para entrenar y puntuar. | models/referencias_folds.json guarda diez referencias e IDs; modelo_etiquetas_validacion_locales.csv conserva las clases efectivas de validación. Se verifican referencias, separación de IDs y ausencia de casos de prueba en los folds. |
| Búsqueda por 1,258 rechazos | Se elimina el bucle y su máximo de intentos. Se usa aproximadamente 80/20 por grupos, sin etiquetas globales. La CV sigue estratificada por títulos usando etiquetas del entrenamiento exterior solo para organizar estratos. | Metadata declara holdout no estratificado y aproximado, un solo reparto y diez folds. Se cambia explícitamente el contrato anterior: no se fuerza una estratificación del target antes de que exista una referencia de entrenamiento. |
| Escalado de banderas de ausencia | El modelo principal no incluye MissingIndicator de ninguna nota. El scaler se aplica solo a las dos notas continuas; géneros, organizaciones y década conservan indicadores 0/1. | construir_pipeline y tests que inspeccionan nombres y valores transformados. Los indicadores de limpieza siguen en el CSV para auditoría, no entre las cinco entradas. |
| Cobertura de Metacritic como proxy de curación | Se retira la bandera explícita del predictor y la ausencia deja de estar marcada por defecto. Se agregan tablas de cobertura/clase, ocultamiento de notas conocidas y ablación sin crítica, sin reseleccionar modelos por esos resultados. | modelo_ausencia_*.csv, modelo_sensibilidad_critica.csv y diagnostico_ausencia en metadata. El sesgo residual se declara, no se da por resuelto. |
| Otro activado por cualquier miembro raro de Team | En estudio, Otro solo se activa cuando ninguna organización de la lista pertenece al vocabulario frecuente; una combinación frecuente+rara mantiene la frecuente sin Otro. Las listas vacías usan Sin dato. Género conserva su regla independiente de pertenencias múltiples. | CategoriasFrecuentes(otro_solo_si_ninguna=True); prueba con frecuente+raro, solo nuevo y lista vacía. Otro aparece ahora en 39.69 % de entrenamiento y 44.14 % de prueba; las muestras han cambiado, por lo que no es un experimento causal de la diferencia de porcentajes. |
| GaussianNB sobre dummies escasas | Se sustituye por CategoricalNB: notas imputadas y discretizadas en cinco intervalos de ancho uniforme aprendidos dentro de entrenamiento; el resto son indicadores categóricos. Se ajusta alpha con GridSearchCV. | modelo_comparacion.csv, matrices vigentes de CategoricalNB y explicación en modelo.md. La matriz antigua de GaussianNB se archiva. |
| Clase media mal reconocida | Se informa soporte, aciertos y recall de todas las clases de cada candidato y se destaca la debilidad del ganador. No se reoptimiza con los errores de prueba. | modelo_error_por_clase.csv y advertencia en modelo.md: el bosque acierta 27/80 medios, recall 33.75 %. Esta limitación sigue abierta. |
| Dummy elegido por desempate | Se documenta que los terciles tienden a balancear por construcción aun ajustados correctamente, y sklearn desempata si es necesario. En el nuevo entrenamiento hay 298 bajos, 297 medios y 297 altos; la clase mayoritaria es bajo sin empate triple. | Metadata y matriz del Dummy. La referencia continúa siendo most_frequent, no se manipulan los cortes para fortalecerla o debilitarla. |
| Playing e índice mezclados en la app | Se mantiene Playing como contexto del EDA/clustering, no como objetivo ni predictor del modelo. El índice de tres señales y su referencia de entrenamiento aparecen explícitamente junto a la tabla, además de en la metodología. | app.py, fase_1_alcance.md y README. Es una diferencia intencional entre tareas, no una columna oculta del target. |
| pytest directo no importa src | Se agrega pytest.ini con pythonpath=. y testpaths=tests. | Se ejecuta .venv314/bin/pytest desde Final, además de python -m pytest. |
| Pipeline no cargable fuera del repositorio | Las clases propias del preprocesamiento se serializan por valor con cloudpickle. El archivo sigue conteniendo un Pipeline compatible con joblib.load, sin importación previa de src; requiere las versiones documentadas de las bibliotecas. | Test en subproceso con cwd temporal y sin PYTHONPATH: carga, predice y comprueba que src no está en sys.modules. No se trata solo de una prueba dentro de pytest con rutas ya añadidas. |
| Nota ausente por defecto y vecinos faltantes | Checkbox por defecto False, entrada sin valor inventado; para predecir se exige una nota o marcar ausencia explícita. Se agregan cinco vecinos ajustados solo en el espacio predictivo del entrenamiento; sus clusters se adjuntan después por id_juego. | pages/3_Consultar_modelo.py, src/similitud.py y models/vecinos_popularidad.joblib; pruebas de validación del formulario, cinco IDs distintos y pertenencia exclusiva al entrenamiento. |

## Resultados regenerados

| Modelo | Exactitud en prueba | F1 macro en prueba |
|---|---:|---:|
| DummyClassifier | 0.3018 | 0.1546 |
| CategoricalNB | 0.5090 | 0.4925 |
| DecisionTreeClassifier | 0.5315 | 0.5119 |
| RandomForestClassifier | 0.5676 | 0.5577 |

El bosque se eligió por la mayor F1 macro media de validación (0.5567), no por la tabla de prueba. Su recall es 64.18 % en bajo, 33.75 % en medio y 74.67 % en alto. El target y el reparto han cambiado: no se atribuye causalmente la diferencia frente a F1=0.5814 del protocolo global anterior.

## Sesgo residual: resultado, no promesa

Al ocultar las 180 notas conocidas de prueba, manteniendo los demás atributos, la probabilidad de bajo aumenta en promedio 0.03885 y su mediana cambia 0.00810. La ablación diagnóstica sin crítica obtiene F1 macro 0.5149. Se retiró la bandera explícita, pero el patrón de imputación y la cobertura no aleatoria pueden seguir influyendo; estos cálculos no son una prueba causal ni de equidad.

La referencia correcta del target y las distribuciones reales están en metadata. Los terciles de entrenamiento casi equilibrados son una propiedad esperable de la definición, no prueba de fuga por sí misma. Lo que se corrigió es usar la prueba y la validación para ajustar referencias.

## Matices técnicos de la auditoría

- Centrar y escalar una variable de manera invertible no distorsiona por sí solo las comparaciones gaussianas ideales: el factor jacobiano común se cancela entre clases. El problema relevante era mezclar indicadores escasos con un supuesto gaussiano y suavizado, y ofrecer explícitamente un proxy de cobertura. Se corrigió el diseño sin afirmar una causa matemática que no se demostró.
- Que Otro sea frecuente y tenga poca importancia no demuestra que una cosa cause la otra. Se cambió la semántica y se informa su prevalencia nueva sin prometer una mejora causal.
- La matriz antigua de GaussianNB no indicaba que predijera siempre medio; indicaba que reconocía mal los medios. Se sustituye el supuesto inapropiado y se conserva un análisis de error explícito del candidato actual.
- La clase media puede solaparse en los predictores con ambos extremos y los cortes introducen fronteras artificiales. Es una explicación plausible, no una causa verificada; el recall bajo permanece como limitación.

## Reproducción

Desde Final: python -m src.pipeline regenera los artefactos canónicos; python src/04_modelo.py regenera solo el modelo desde dataset_depurado. El manifiesto valida modelo, metadata, vecinos y datasets. Las métricas globales antiguas se conservan en archivo_modelo_pre_auditoria2, fuera del flujo activo.

Los registros de las dos entradas de pytest están en pruebas_auditoria2.txt y pruebas_auditoria2_modulo.txt. La prueba de portabilidad usa un proceso limpio y la app se valida con notas explícitas y vecinos.

## Validación final ejecutada

- 82 pruebas aprobadas con pytest directo y 82 con python -m pytest; registros conservados.
- Carga del Pipeline en subproceso limpio sin src en PYTHONPATH y predicción cruda comprobadas.
- Verificación en Chrome: nota de prensa habilitada y ausencia desmarcada al abrir; al proporcionar 85 y enviar se obtuvo una predicción y cinco vecinos con sus etiquetas disponibles por ID.
- Hashes de datasets, modelo, metadata y vecinos concordantes con el manifiesto; maestro y antecedente histórico intactos.

## Que debo verificar manualmente

- Roles de Team y los tres conflictos históricos pendientes de identidad/plataforma.
- Pesos y redundancia del índice; antigüedad y representatividad de los juegos.
- Sesgo residual de cobertura de prensa y desempeño insuficiente de la clase medio.
- Similitud de vecinos como descripción de atributos, sin inferir causalidad ni éxito comercial.
- Dependencias de versión para cargar el Pipeline portátil; no se requiere src, pero sí las bibliotecas registradas.
