# Revisión del anteproyecto v2.0 contra la rúbrica

> Revisión documental previa a las correcciones de implementación. Para el estado vigente de Final, consultar correcciones_auditoria.md; las cifras históricas de esta revisión no sustituyen los artefactos regenerados.

Fecha de revisión: 8 de noviembre de 2026. Esta es una revisión; no se modificaron ni reescribieron el anteproyecto, su fuente LaTeX o la rúbrica.

## Fuentes, alcance y criterio

- Anteproyecto evaluado: `Proyecto/Anteproyecto_v2_320317264_320060829_320206968.pdf`, 25 páginas PDF. Portada: versión 2.0 actualizada el 08/11/2026.
- Rúbrica: `Proyecto/instruct/ProyectoMineríaDatos.pdf`, diapositiva 5. Las instrucciones de entrega final están en su diapositiva 4.
- Maestro de datos designado por el usuario: `Proyecto/data/processed/games_curated.csv`, 1,117 filas y 42 columnas. Es la fuente original para el trabajo actual de Final; el archivo de 1,512 filas es su antecedente histórico, no la entrada actual del modelo.
- Para distinguir planificación de ejecución se consultaron los artefactos existentes en `Final`. Su presencia no se contabiliza como evidencia ya incluida en el anteproyecto.
- Las referencias de página siguientes usan la **numeración impresa del anteproyecto**: p. 1 corresponde a la página PDF 3; p. 23, a la página PDF 25. La portada no tiene número impreso.
- No se asigna una nota numérica: la rúbrica no da ponderaciones y la evaluación final corresponde al profesor. Las brechas describen qué evidencia permitiría defender el nivel excelente, no una garantía de obtenerlo.
- La revisión bibliográfica es de trazabilidad interna. No se verificaron en internet las cifras de industria, la situación de Marathon ni los contenidos de los artículos citados.

**Diagnóstico:** el documento tiene una planificación extensa y una auditoría inicial útil, pero promete explicar éxito comercial y clasificar perfiles de mercado sin una definición verificable de esas etiquetas. La implementación actual responde una pregunta más acotada: clasificación contemporánea de popularidad relativa dentro de Backloggd. La principal corrección pendiente es acordar y registrar ese alcance, no añadir más algoritmos.

## 1. Matriz de los nueve rubros

| Rubro de la rúbrica | Evidencia que ya contiene el documento | Qué falta para defender 9.5–10 | Acción concreta |
|---|---|---|---|
| Objetivo | Objetivo general y siete específicos, pp. 1–2. Incluyen limpieza, EDA, Pearson, popularidad, clustering, clasificación y app. | Una definición única de resultado y alcance: se mezclan éxito comercial, recepción, popularidad y perfil de cluster. El maestro carece de ventas verificadas y etiquetas de fracaso/GaaS. | Acordar que la clasificación usa terciles del índice de popularidad y que clustering es una tarea descriptiva separada; registrar la decisión en ESPEC-2.0 o una revisión posterior, sin presentar los terciles como clusters. |
| Contexto | Origen Backloggd/Kaggle, variables y cobertura, p. 3; limitaciones y sesgo, p. 4; trabajos relacionados, p. 5; motivación de negocio, pp. 11–12. | Vincular cada afirmación relevante con una fuente identificable y distinguir contexto industrial de lo observable en esta muestra. Falta documentar fecha de captura, alcance de Team y procedencia/plataforma de cada nota crítica. | Crear una ficha de datos del maestro con dimensiones, hash, campos, ausencias, fecha conocida/desconocida y fuentes; añadir una matriz afirmación–referencia para las cifras del contexto. |
| Estrategia | Seis fases CRISP-DM, pp. 5–7; arquitectura y reglas de coherencia, pp. 7–9; entregables y responsables. | Un protocolo ejecutable y consistente: objetivo supervisado, atributos, tratamiento de listas/ausencias, fórmula de popularidad, cortes, selección de parámetros y separación de entrenamiento/prueba. | Referenciar un protocolo metodológico versionado que corresponda al código real, con una tabla tarea–entrada–salida–criterio de aceptación. |
| Expectativas | Sección específica, p. 13: asociación de notas, popularidad, perfiles, clasificador y aplicación. | Criterios de aceptación observables y límites: no se puede comprobar reducción de pérdidas o riesgo de inversión con esta muestra. Una ausencia de relación o unos clusters poco útiles también deben admitirse como hallazgo. | Para cada expectativa registrar indicador, evidencia y condición de cumplimiento; por ejemplo, informe con n e IC de Pearson, comparación contra base mayoritaria y demo local funcional. No fijar una buena métrica después de observarla. |
| Plan de trabajo (baseline vs. Real) | Cronograma de 19 actividades con fechas y responsables, pp. 9–10; catálogo de CI, pp. 14–22. | El plan es baseline: no hay tabla de ejecución real, desviaciones, causas ni cambios aprobados. También falta explicar dependencias y el efecto de la revisión de noviembre. | Elaborar un registro con fechas previstas/reales comprobables, estado, evidencia, desviación en días, causa y responsable. Marcar como desconocidas las fechas reales sin registro; no reconstruirlas a partir del baseline. |
| Metodología de modelado | Pearson segmentado, K-Means, DBSCAN, Naive Bayes, árbol y MLP; silueta, estabilidad, F1 y validación de 10 pliegues, pp. 6–7. Reconoce riesgo de fuga. | Definir el target y resolver la incompatibilidad entre predecir clusters usando calificaciones y formar clusters con esas mismas calificaciones. Faltan parámetros/rangos, preprocesamiento dentro de folds, base comparativa y protocolo de estabilidad. | Documentar el protocolo que realmente se ejecutará; para Final, terciles calculados en entrenamiento, cinco folds agrupados y prueba reservada. Completar los modelos prometidos o aprobar su sustitución y justificarla antes de atribuir cumplimiento a esta versión. |
| Eficiencia en herramientas MD | Python, Orange y Weka, propuesta propia y demo están previstos; CI específicos y arquitectura de integración, pp. 6–9 y 17–19. | Evidencia de uso efectivo de herramientas de la materia y explicación de la aportación del equipo. Exportar CSV/ARFF no prueba que se hayan ejecutado Orange/Weka; usar asistentes tampoco demuestra dominio del equipo. | Guardar flujos/configuraciones, versiones, capturas y resultados de Orange/Weka con las mismas particiones y atributos; preparar una demo donde los integrantes expliquen y reproduzcan las decisiones del pipeline Python. |
| Resultados y Conclusiones | Auditoría preliminar: duplicados, estimaciones y cambio de Pearson, p. 4. No incluye resultados finales de clustering/clasificación ni conclusiones del proyecto. | Resultados que respondan cada objetivo, interpretación crítica y límites. La rúbrica exige llegar a resultados y concluir; una lista de actividades futuras no acredita ese rubro. | Integrar, en la futura entrega final, tablas y gráficos calculados, matriz de confusión, comparación con la base y conclusiones ligadas a cada objetivo. Explicar también el cluster dominante de DBSCAN y el bajo desempeño de la clase media. |
| Fuentes | Bibliografía final de 15 entradas, p. 23; citas autor–año visibles para CRISP-DM y Streamlit. CONFIGTEC-1.0 declara biblatex APA. | Uso de citas en el cuerpo, no solo lista final; correspondencia entre las afirmaciones y las referencias, datos bibliográficos completos y trazabilidad de las notas agregadas. Una configuración APA no acredita por sí sola el cumplimiento. | Auditar afirmación por afirmación: identificar el artículo de 1,642 juegos/680,000 reseñas, la fuente de los datos Newzoo vía Game World Observer, Wall Street Journal y los casos GaaS; completar o retirar lo no sustentado y comprobar el formato APA. |

La rúbrica es de proyecto final. Que un anteproyecto aún no contenga resultados o fechas reales no equivale a que el documento sea inválido como planificación; sí significa que esa evidencia deberá aportarse para defender esos rubros en la entrega final.

## 2. Inconsistencias y problemas de trazabilidad

### 2.1 Dentro del PDF

| Hallazgo | Localización y evidencia | Implicación y acción recomendada |
|---|---|---|
| Fechas de entrega sin distinguir hitos | Portada: 30/09/2026; cronograma: redacción 01–05/10; ANTE-2.0: 08/11; entrega final: 25/11. | No es necesariamente una contradicción si son entrega original, revisión y entrega final, pero la portada no lo explica. Identificar cada fecha por su tipo; no cambiar todas a noviembre sin conservar la historia. |
| Dependencias de versiones posteriores | ANTE-2.0 del 08/11 es base de DATA-RAW-1.0 del 01/10, p. 14; ESPEC-2.0 del 08/11 orienta CLEAN-SCRIPT-1.0 del 08/10 y EDA-REPORT-1.0 del 22/10, p. 15. | Las relaciones pueden ser retrospectivas por revisión, pero falta ese registro. Distinguir dependencia histórica de validación o actualización posterior y registrar el cambio de baseline. |
| Reporte de correlación fechado antes de terminar el análisis | EDA-REPORT-1.0 incluye correlación por género/estudio y fecha 22/10, p. 17; cronograma sitúa correlaciones del 22 al 29/10, p. 10. | El CI no puede ser un reporte final completo el día que empieza parte de su contenido, salvo que sea versión parcial. Separar EDA y correlación o establecer revisiones y fechas de cierre. |
| Reporte de clustering antes de su interpretación | CLUSTER-REPORT-1.0 promete resultados identificados e interpretados el 05/11, p. 17; interpretación programada del 05 al 10/11, p. 10. | Aclarar si el 05/11 es ejecución preliminar y el 10/11 la versión interpretada. No usar la misma fecha como cierre de ambas cosas. |
| Responsable de correlaciones ambiguo | Actividad 9: García Cortés, p. 10; EDA-REPORT-1.0, que incluye correlación: Lara Hernández, p. 17; RH-ANALISTA atribuye generación de EDA a Lugo Manzano, p. 22. | Puede haber colaboración, pero no se distinguen autor, ejecutor y aprobador. Registrar esos tres roles para el entregable; evitar tres responsables únicos implícitos. |
| Script fechado dentro de su desarrollo sin tipo de hito | CLEAN-SCRIPT-1.0: 08/10, p. 15; desarrollo: 06–10/10, p. 10. | Es una ambigüedad, no un error probado: el 08/10 podría ser primera versión. Etiquetar creación, validación y cierre. |
| Referencia de código inexistente en el árbol propuesto | Figura 1 usa `src/models`, p. 8; el árbol de esa misma página propone `src/clustering.py` y `src/classification.py`, sin `src/models`. | Elegir una referencia coherente para el nodo de modelado; la figura no debe apuntar a un módulo no definido. |
| Falta el CI de la curación que se cita como evidencia | Auditoría atribuida a `src/cleaning.py` y `src/curate.py`, p. 4; el árbol y CLEAN-SCRIPT-1.0 solo describen cleaning, pp. 8 y 15. | Incorporar curate como componente del CI o identificar un CI propio, y declarar qué archivo genera. Sin ello no se reproduce la exclusión de crítica sintética a partir de la arquitectura descrita. |
| “Todos los registros” no identifica la población correcta | P. 4 llama así a r=0.600 con 1,104 pares; el documento también maneja 1,512 registros originales y 1,117 únicos. | Ese cálculo corresponde a juegos únicos con ambos valores, incluyendo estimaciones, no a las 1,512 filas. Rotular población, deduplicación, filtro y n en cada estimación. |
| Uso de crítica sintética no resuelto en todas las tareas | P. 4 excluye estimaciones para usuarios–crítica; pp. 6 y 13 vuelven a mencionar `Metacritic Rating` para derivados, clustering y supervisión sin el mismo filtro explícito. | La regla de exclusión debe cubrir todas las tareas que interpreten esa variable como prensa. Especificar `critic_score_final` y su procedencia, sin imputar la nota sintética como observación real. |
| Cuatro señales frente a tres en expectativas | Objetivo de popularidad, p. 1: Plays, Playing, Backlogs, Wishlist; expectativas, p. 13: Plays, Wishlist y Backlogs. | La omisión de Playing cambia la operacionalización de actividad. Declarar las cuatro señales y justificar si una tarea usa solo algunas. |
| Predictoras y construcción de clusters incompatibles | P. 6 promete excluir de los predictores lo usado para formar clusters; p. 13 propone clusters con calificaciones, popularidad y género, y después clasificación mediante género y calificaciones. | No se pueden mantener simultáneamente esas tres afirmaciones sin especificar qué tarea usa qué campo. Separar la clasificación de terciles de la segmentación o rediseñar explícitamente el objetivo supervisado. |
| “Asociación” se interpreta como “parecido” de notas | Objetivo de discrepancia, p. 1, y expectativas, p. 13: Pearson se utiliza para inferir notas más parecidas o diferentes. | Correlación alta no acredita acuerdo ni brecha pequeña. Conservar Pearson para asociación; una diferencia requiere escala confirmada y una medida específica de brecha/acuerdo. |
| Alcance causal/comercial frente a limitaciones admitidas | P. 4 limita conclusiones y reconoce ausencia de fracasos y de finanzas empíricas; pp. 1, 3, 11 y 13 hablan de factores determinantes, éxito comercial y reducción de pérdidas por elección de género. | El contexto puede motivar el estudio, pero no convertirse en un resultado que el dataset no identifica. Limitar conclusiones a asociaciones observadas y no atribuir causas de fracaso a la falta de análisis empresarial. |
| Fuentes narradas sin referencia identificable | Pp. 3, 5 y 11 mencionan Game World Observer, un estudio en ScienceDirect con 1,642 juegos y 680,000 reseñas y Wall Street Journal; p. 23 no permite identificar inequívocamente esas fuentes. | Añadir autor, fecha, título y cita vinculada. “ScienceDirect” es una plataforma, no la identificación de un estudio. Revisar también fecha y soporte de las afirmaciones sobre Marathon. |

**Comprobaciones que no deben convertirse en errores inventados:** las fases del texto y de la tabla 1 mantienen la secuencia 1–6. Los números 1–19 del cronograma son actividades, no una segunda numeración de fases. Se cuentan siete objetivos específicos, de acuerdo con ESPEC-2.0. El 25/11/2026 sí cae en miércoles. Los identificadores ANTE-2.0, ESPEC-2.0, CLEAN-SCRIPT-1.0, DATA-CLEAN-1.0, CP-1.0, CLUSTER-REPORT-1.0 y MODEL-SUP-1.0 no cambian de escritura en las fichas revisadas. No detecté un identificador de CI mal escrito; los problemas son de fechas, dependencias, alcance y referencias de archivos. Los 382 duplicados exactos salvo ID también coinciden con el antecedente histórico comprobado.

### 2.2 Diferencias con las instrucciones y la implementación actuales

Estas diferencias **no son contradicciones internas del PDF**. Se registran para no presentar una demo distinta de la que el documento promete.

| Tema | Anteproyecto | Estado actual / decisión del usuario | Acción pendiente |
|---|---|---|---|
| Fuente original | DATA-RAW-1.0 describe 1,512 filas sin depurar; la versión de trabajo es games_actualizado_metacritic.csv. | El usuario designó `games_curated.csv` como original del trabajo en Final: 1,117 filas y 42 columnas. | Registrar la procedencia histórica y una versión del insumo actual. No describir la copia curada como si nunca hubiese sido depurada. |
| Objetivo supervisado | Perfil obtenido del clustering; MODEL-SUP depende de CLUSTER-REPORT. | Nivel bajo/medio/alto por terciles del índice de cuatro señales; no depende de la etiqueta de cluster. | Acordar una sola definición y reflejarla en objetivos, expectativas, CI, diagrama y demo. |
| Algoritmos y evaluación | Naive Bayes, árbol, MLP y 10 pliegues en Orange/Weka/Python. | Python compara base mayoritaria, regresión logística y bosque, con cinco folds agrupados y prueba reservada. | Completar los modelos prometidos o justificar una revisión de alcance. No renombrar el bosque como árbol único ni afirmar que se usaron 10 folds. |
| Estructura de carpetas | `app/Inicio.py`, `data/processed`, `artifacts`. | La estructura sugerida por el usuario usa `app.py`, `data/clean`, `models`; Final sigue esta segunda organización con nombres propios de módulos y artefactos. | Crear un mapa CI–ruta–archivo real. La estructura sugerida no obliga a renombrar carpetas durante esta revisión. |
| Evidencia de otras herramientas | Comparación ejecutada de Orange y Weka contra Python. | Hay exportaciones CSV/ARFF e instrucciones; no evidencia de ejecución gráfica de Orange/Weka en Final. | Ejecutar y registrar las herramientas antes de afirmar cumplimiento. |
| Publicación | Streamlit Community Cloud en DEPLOY-1.0 y demo que lo valida. | El usuario pidió conservar todo localmente, sin push ni despliegue público. | Registrar el cambio de alcance y confirmar si la demo local cumple la evaluación del curso; no marcar DEPLOY-1.0 como realizado. |
| Power BI | Se descarta expresamente, pp. 6 y 16. | Se mencionó entre las herramientas iniciales y Final ofrece instrucciones de importación. | Acordar el alcance; no tratar la ausencia de Power BI como incumplimiento de este PDF, que lo excluye. |

## 3. Objetivos específicos: verificabilidad y redacción propuesta

Las formulaciones siguientes son propuestas para aprobación del equipo, no cambios aplicados al documento. Se numeran en el mismo orden de la sección 1.2. La escala, el origen de las notas y los roles de Team no se dan por verificados.

| Objetivo | Diagnóstico | Formulación verificable propuesta |
|---|---|---|
| 1. Depurar y estructurar | Factible; “garantizar la calidad” es absoluto y no define qué se comprueba. El insumo actual ya está curado. | “Validar el maestro games_curated.csv y generar una vista analítica reproducible, conservando su hash, documentando faltantes, listas, fechas y procedencia crítica, y verificando con pruebas los formatos, la unicidad de título/fecha y la exclusión de estimaciones financieras de los modelos.” |
| 2. EDA | Factible en su mayor parte; la atribución a desarrolladores no está verificada y faltan productos de aceptación. | “Generar tablas de frecuencias por género, organización de Team y década, y estadísticas de distribución de notas y las cuatro señales de popularidad, informando n y ausencias; conservar las tablas y figuras que sustenten cada descripción.” |
| 3. Discrepancia perceptiva | Pearson cuantifica asociación, no discrepancia. “Variaciones significativas” exige una prueba de diferencias entre grupos, no solo r por grupo. | “Estimar Pearson entre Rating y critic_score_final en pares completos, globalmente y por género y organización, informando n, IC95 % y corrección por comparaciones múltiples; omitir estimaciones con menos de diez pares o sin variación y no interpretar diferencias de r como diferencias probadas entre grupos.” |
| 4. Popularidad real | Los datos miden declaraciones en Backloggd, no liderazgo de mercado, usuarios únicos, ventas o retención. | “Describir Plays, Playing, Backlogs y Wishlist en la muestra, construir un índice explícito como el promedio de log(1 + conteo), y comparar sus distribuciones por género y organización junto con las calificaciones, identificando qué conclusiones dependen de los pesos elegidos.” |
| 5. Perfiles de mercado | El agrupamiento es realizable; “culto”, “sobrevalorado”, éxito comercial y causas de pérdidas no son etiquetas disponibles. | “Ajustar K-Means y DBSCAN sobre las cuatro señales transformadas con log1p y estandarizadas, documentar parámetros, silhouette, tamaños, ruido y medianas por grupo, y evaluar estabilidad con un procedimiento declarado antes de nombrar e interpretar los perfiles; usar género para describirlos posteriormente.” |
| 6. Clasificación de perfil | No está definida la etiqueta y puede ser circular si el target se deriva de las mismas notas usadas para predecirlo. Además, usar notas publicadas impide presentarlo como pronóstico previo al estreno. | “Comparar clasificadores que estimen popularidad baja, media o alta, definida por terciles del índice obtenidos solo en entrenamiento, usando género, organizaciones, década, Rating y critic_score_final; reservar prueba por título y evaluar con F1 macro, balanced accuracy y matriz de confusión frente a una base mayoritaria, ajustando el preprocesamiento dentro de cada fold.” |
| 7. App y comunicación | Desarrollar y demostrar es verificable; el despliegue público no está autorizado actualmente. Falta definir pruebas funcionales y accesibilidad de hallazgos. | “Entregar una app Streamlit ejecutable localmente que permita explorar los datos, consultar asociación de notas, perfiles y estimaciones del clasificador, y mostrar sus límites; comprobar carga, filtrado, ausencia de resultados e inferencia con notas faltantes y proporcionar instrucciones reproducibles.” |

**Límites de estas propuestas:** el umbral n≥10 es una regla operativa usada por Final, no una garantía de potencia estadística. La estabilidad del clustering sigue siendo trabajo pendiente: ejecutar una sola vez con semilla fija no la demuestra. El protocolo de cinco folds actual debe acordarse frente a los diez del anteproyecto. Si el equipo desea conservar Naive Bayes, árbol y MLP como compromiso, debe ejecutarlos y documentarlos; esta revisión no los sustituye automáticamente.

## 4. Cinco preguntas difíciles para la demo

### 1. “¿Dónde demuestran que elegir un género provoca fracasos GaaS o que su modelo reduce pérdidas?”

**Respuesta defendible:** no lo demostramos con este maestro. Analizamos asociaciones entre recepción, actividad e interés en una muestra sesgada de juegos populares. No contiene etiquetas verificadas de fracaso, condición GaaS ni ventas/costos empíricos que permitan medir ese efecto.

**Evidencia para mostrar:** limitaciones del anteproyecto, p. 4; inventario de campos en `Final/reports/inspeccion.json`; fuente `games_curated.csv`; exclusión de finanzas en `Final/src/data.py`. La población complementaria mencionada en el PDF es trabajo futuro y no evidencia incorporada.

### 2. “Si Pearson es 0.544, ¿cuántos puntos discrepan usuarios y críticos? ¿Usaron notas inventadas?”

**Respuesta defendible:** r=0.5444 cuantifica asociación lineal y no se puede convertir en una cantidad de puntos de desacuerdo. Se usaron 890 pares completos, con IC95 % [0.4965, 0.5891]. Las 218 filas sin critic_score_final se conservaron como juegos, pero no aportaron una nota de prensa a Pearson. La etiqueta de procedencia del CSV no equivale a una comprobación externa.

**Evidencia para mostrar:** `Final/reports/pearson_global.csv`, `Final/reports/pearson_generos.csv`, `Final/reports/pearson_organizaciones.csv`, `Final/src/data.py` y la correspondencia `critic_source`–`critic_score_final` del maestro. El rango observado de Rating es 0.7–4.8; no hemos validado externamente los extremos teóricos para calcular una brecha normalizada.

### 3. “¿El clasificador aprende algo o simplemente reconstruye los conteos usados para fabricar su etiqueta?”

**Respuesta defendible:** el target actual son terciles del índice, no clusters. Los conteos y el índice no entran a los predictores. Se reservan títulos completos para prueba antes de definir los cortes; cada fold vuelve a ajustar cortes, codificadores e imputación con entrenamiento. Esto reduce fugas directas, pero no elimina el sesgo del muestreo ni la dependencia entre franquicias.

**Evidencia para mostrar:** `Final/src/config.py`, `Final/src/modeling.py`, `Final/tests/test_pipeline.py`, `Final/data/clean/juegos_modelo.csv` y `Final/reports/metricas.json`. Hay 895 juegos en entrenamiento y 222 en prueba. Los cortes del entrenamiento son 5.836372 y 6.679875. Como usa notas publicadas, no debe venderse como predicción antes del lanzamiento.

### 4. “¿Por qué esos clusters son perfiles de mercado útiles y no solo juegos con más o menos actividad?”

**Respuesta defendible:** aún no hay evidencia suficiente para esa etiqueta comercial. K-Means seleccionó dos grupos y principalmente separa magnitudes de las señales. DBSCAN deja 1,083 juegos en el grupo principal, ocho en otro y 26 como ruido; su silhouette sin ruido de 0.637 no demuestra que la segmentación sea útil para tomar decisiones de mercado. Falta comprobar estabilidad y sensibilidad de pesos/parámetros.

**Evidencia para mostrar:** `Final/reports/seleccion_kmeans.csv`, `Final/reports/seleccion_dbscan.csv`, `Final/reports/perfiles_kmeans.csv`, `Final/reports/perfiles_dbscan.csv` y `Final/reports/figures/perfiles.png`. No afirmar que -1 es un perfil ni llamar “fracasos” a los juegos con pocos Plays.

### 5. “¿Qué aporta su propuesta Python, cuánto mejora y dónde está la comparación real con Orange/Weka?”

**Respuesta defendible:** la aportación implementada es un pipeline reproducible con procedencia, listas múltiples, partición por títulos, terciles internos, validación y demo local. En Python se compararon base mayoritaria, regresión logística y bosque; este último obtuvo F1 macro 0.5649 y accuracy 0.5856 en la prueba reservada, frente a F1 macro 0.1846 de la base. Eso es evidencia de esta partición, no de superioridad comercial ni de superioridad estadística frente a Orange/Weka.

**Evidencia para mostrar:** `Final/reports/comparacion_modelos.csv`, `Final/reports/validacion_cruzada.csv`, `Final/reports/metricas.json`, `Final/reports/matriz_confusion.csv`, `Final/src/modeling.py`, pruebas y app local. La clase media tiene F1≈0.386, límite que debe explicarse. Los archivos Orange/Weka son entradas exportadas, no resultados de ejecuciones; completar esa evidencia sigue pendiente.

## Orden de atención recomendado

1. Acordar y registrar alcance: popularidad relativa, target por terciles, fuente curada y demo local. Esta decisión evita que objetivos, CI y demo describan proyectos distintos.
2. Cerrar el protocolo de evaluación y el compromiso de algoritmos/herramientas; después obtener las evidencias faltantes de Orange/Weka y estabilidad.
3. Registrar el plan real contra el baseline con fechas comprobables y cambios aprobados, preservando el historial de octubre.
4. Vincular cada afirmación de contexto a una referencia y cada conclusión a una salida calculada.
5. Preparar la demo para mostrar tanto resultados como límites, incluyendo la clase media y el cluster dominante de DBSCAN.

## Que debo verificar manualmente

- Que el PDF v2.0 encontrado y la rúbrica de cinco diapositivas sean exactamente los documentos que el profesor evaluará; no se eligió main.pdf como sustituto.
- Fechas reales, autores, aprobadores y estado de CI: no se infieren de las fechas previstas ni de la fecha de modificación de archivos.
- Si la demo local satisface el requisito del profesor y cómo registrar la cancelación del despliegue público.
- Escala teórica de Rating, plataforma/fecha de notas, funciones de Team, deduplicación histórica y fecha de captura.
- Fuentes originales de cifras de mercado, casos GaaS y artículos; formato APA de citas en el cuerpo y bibliografía. Esta revisión no hizo comprobación externa de esos hechos.
- Que ninguna exportación CSV/ARFF se presente como ejecución ya realizada de Orange/Weka y que ningún artefacto actual se atribuya al PDF si no está incluido en él.
- Aprobar cualquier cambio de objetivos, folds, algoritmos, estructura o identificadores antes de modificar el anteproyecto; aquí solo se proponen acciones.
