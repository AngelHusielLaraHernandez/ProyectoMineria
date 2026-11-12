# Evaluación del proyecto

## Datos y resultados descriptivos

La [tabla de procedencia](tables/procedencia_datos.csv) distingue las dimensiones declaradas en el anteproyecto, el antecedente enriquecido y el maestro curado. La reconstrucción coincide con el maestro local. El log de limpieza registra los descartes heredados y las exclusiones analíticas.

La asociación entre la valoración de la comunidad y la de prensa se puede reproducir en [correlación del catálogo](tables/correlacion_catalogo.csv). La [popularidad por género](tables/popularidad_genero.csv) y por [organización](tables/popularidad_estudio.csv) incluye conteos observados, medias y medianas de las cuatro señales y ambas notas. Los grupos y las correlaciones tienen umbrales de cobertura separados. Team identifica las organizaciones registradas en el CSV.

## Agrupamiento

K-Means y Ward seleccionan dos grupos por silueta. La [tabla de métricas internas](tables/metricas_clusters.csv) permite contrastar todos los cortes evaluados y los parámetros de DBSCAN. La [tabla BIC](tables/bic_gmm.csv) favorece tres componentes de mezcla gaussiana. El BIC complementa los índices de agrupamiento y el criterio operativo se conserva. DBSCAN encuentra un núcleo dominante y ruido. Los [perfiles](tables/perfiles_clusters.csv) y la [proyección PCA](figures/pca_tres_metodos.png) describen el catálogo disponible.

## Modelo activo

Random Forest se conserva en producción. En la [validación externa anidada](tables/comparativo_modelos.csv), el F1 macro medio es 0.5495 ± 0.0474 para el bosque y 0.5538 ± 0.0561 para la MLP. La [t corregida de Nadeau–Bengio, Wilcoxon y Nemenyi](tables/comparacion_estadistica.csv) dan p de 0.7597, 0.3876 y 0.9956 para esa pareja. Se conserva el bosque por decisión de proyecto, menor dispersión observada y disponibilidad de diagnóstico por importancia de variables. Los resultados no demuestran equivalencia.

En [prueba](tables/metricas_prueba.csv), Random Forest logra 56.76 % de exactitud, F1 macro 0.5577, F1 ponderado 0.5540, kappa 0.3552 y AUC OvR 0.7379. La [matriz](tables/matriz_confusion.csv) muestra que la clase media se recupera en 27 de 80 juegos (33.75 %). La [prueba histórica de la MLP](tables/prueba_historica_modelos.csv) dio 50.90 % y F1 macro 0.5008. El código anterior seleccionó por CV y luego calculó resultados de prueba de todos los candidatos. La decisión actual conoce esa prueba previa, por lo que falta una muestra independiente para medir la generalización de la decisión.

El Brier multiclase es 0.5570 y el log-loss 0.9274. La [curva por intervalos](tables/calibracion.csv) registra soporte y frecuencia observada. Los escenarios y contraejemplos ilustran sensibilidad y errores del bosque. La auditoría de predicciones comprueba el artefacto, la matriz, la referencia del objetivo y los vecinos.

## Herramientas y aplicación

El [comparativo](tables/comparativo_herramientas.csv) conserva la CV anidada de Python y las corridas gráficas de Weka con sus diferencias de protocolo. Las salidas y capturas de Weka, los hashes y los datos de entrada se contrastaron. Orange quedó sin métricas después de los cierres de Qt/Cocoa y del reintento sin interfaz. [Bitácora de herramientas](codex_log.md).

La app funciona localmente y muestra exploración, inferencia y evaluación. La estimación describe interacciones observadas en Backloggd. Puede favorecer géneros populares y desfavorecer los de nicho. El estudio trabaja a nivel de juego y no de persona. Los datos carecen de ventas observadas y no permiten medir rentabilidad o riesgo de juegos como servicio. [Estado de publicación](despliegue.md).
