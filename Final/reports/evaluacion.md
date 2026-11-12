# Evaluación del proyecto frente a sus objetivos

Todas las cifras provienen de los reportes de `Final/reports/` y de `models/metadata.json`. No se calculó ningún número nuevo. Donde un dato necesario no existe en los reportes, se indica explícitamente al final de cada sección.

## 1. Objetivos específicos

| # | Objetivo | Evidencia (archivo y cifra) | Estado | Comentario |
|---|---|---|---|---|
| 1 | Depurar y estructurar el maestro | `limpieza_log.md`, `inspeccion.md`: 1,117 filas × 42 columnas (SHA-256 `b23cc1c4…625acd`); `trazabilidad_historica.md`: 1,512 → 1,117 con 395 descartes documentados; 218 notas críticas estimadas excluidas; 1,114 juegos elegibles | Cumplido | Los 3 conflictos históricos (`id_juego` 117, 140, 296) siguen sin resolver y están excluidos del análisis. |
| 2 | EDA (distribuciones, géneros, décadas) | `inspeccion.md`: seis figuras EDA; Rating 0.7–4.8 con 13 ausencias; `clustering_03_correlaciones_generos.csv`: 16 géneros incluidos y 7 excluidos | Cumplido | Los roles de `Team` no se acreditan como desarrolladores, y faltan 3 fechas. |
| 3 | Discrepancia usuarios–prensa | `clustering.md`: n = 887, Pearson r = 0.5439, Spearman ρ = 0.5242; brecha absoluta media por género, de 8.222 (Visual Novel) a 12.82 (Shooter) | Cumplido | Con correcciones BH por género. La conversión Rating/5×100 no implica equivalencia entre plataformas. |
| 4 | Popularidad con interacciones | `clustering_03_correlaciones_senales.csv`: Plays–Rating r = 0.1517; Plays–Metacritic r = 0.4144; Backlogs–Wishlist r = 0.7912 | Parcial | Se mide popularidad en Backloggd, no ventas. Las señales están muy correlacionadas entre sí. |
| 5 | Perfiles (K-Means y Ward) | `clustering.md`: K-Means k = 2, silhouette 0.3188, grupos de 465 y 422; Ward: silueta 0.2807, grupos de 558 y 329 | Parcial | El resultado de K-Means separa principalmente magnitud. K-Means obtiene mejores valores en los tres índices internos. DBSCAN se conserva como corrida histórica. |
| 6 | Clasificador de popularidad | `modelo.md` y `metadata.json`: MLP seleccionada por CV, n prueba = 222, exactitud 0.5090, F1 macro 0.5008, frente a 0.1546 del Dummy | Parcial | Supera la referencia en esta partición, sin prueba de significancia. Recall de la clase media = 0.2875. Random Forest obtiene F1 macro 0.5577 en prueba. |
| 7 | App y comunicación | `pages/2_Prediccion.py`, `pages/3_Acerca_del_modelo.py`; `verificacion_funcional.md`; `pruebas_web.txt` (87 pruebas) | Parcial | App local funcional. No hay despliegue público (`despliegue.md`). |

**Comparación de herramientas (Python, Orange, Weka).** Weka 3.8.7 tiene seis corridas gráficas completas (`weka/resumen_gui.md`). En clasificación, RandomForest alcanzó 53.4753 % y NaiveBayes 50.8969 % (CV de 10 pliegues, n = 892). En K-Means con k = 2 hay ARI = 1.0 contra Python en la ejecución CLI 3.8.6. **Orange no tiene ninguna corrida verificada** (`diagnostico_cierres.md`: cierres con SIGSEGV). Esta comparación queda **parcial**.

## 2. Preguntas de la problemática

**¿Los juegos mejor calificados son los más jugados?** Solo en parte, y depende de quién califica.
- Plays frente a Rating (usuarios): r = 0.1517 y ρ = 0.08737. La asociación es débil.
- Plays frente a Metacritic: r = 0.4144 y ρ = 0.423. La asociación es moderada.
- Wishlist frente a Rating: r = 0.4232 y ρ = 0.5035.

Una asociación no implica causalidad.

**¿Hay géneros con muchos jugadores y calificaciones bajas, o al revés?** Los reportes **no contienen Plays por género**, así que no puedo responderlo con datos del género. Hay evidencia indirecta en K-Means k = 4: el cluster 0 (n = 238) tiene Plays = 6319 con Rating = 3.356, y el cluster 3 (n = 192) tiene Plays = 1640 con Rating = 3.949. Existen perfiles cruzados, pero eso no los asocia a un género. **Si lo necesitas, pídeme que calcule Plays y Rating medios por género.**

**¿El Metascore funciona igual en todos los géneros?** No. Entre los 16 géneros con n ≥ 20:
- Fuerte: Arcade (r = 0.7548, n = 39), Point-and-Click (r = 0.6546) y Platform (r = 0.6428).
- Débil o no significativa: Visual Novel (r = −0.1042, p = 0.605) y Turn Based Strategy (r = 0.2514, p = 0.0752).
- Brecha absoluta media: Shooter (12.82), Fighting (12.02) y Racing (12.0), frente a Visual Novel (8.222).

Las diferencias entre r de distintos géneros no están probadas como diferencias significativas entre grupos.

## 3. Análisis de errores del clasificador

Matriz de la MLP (filas reales, columnas predichas bajo / medio / alto):

| real | bajo | medio | alto |
|---|---|---|---|
| bajo | 40 | 17 | 10 |
| medio | 31 | 23 | 26 |
| alto | 10 | 15 | 50 |

- **Recall por clase:** bajo 0.5970, medio 0.2875, alto 0.6667.
- **Confusión principal:** medio → bajo (31 de 80) y medio → alto (26 de 80).
- **Por qué es plausible:** la clase media es un tramo de un continuo, delimitado por cortes artificiales en los terciles [0.3623, 0.6267]. Sus notas y géneros pueden solaparse con ambos extremos (`modelo.md`). Es una hipótesis interpretativa, no una causa demostrada.
- **Otros modelos:** DecisionTree tiene recall medio 0.225 y CategoricalNB 0.2375. Todos fallan sobre todo en esa clase.
- **Cobertura de prensa:** al ocultar las 180 notas críticas conocidas de prueba, la probabilidad de "bajo" baja 0.01602 en promedio. La ablación sin crítica da F1 macro 0.5098. Esto es diagnóstico, no una prueba causal.

## 4. Limitaciones

- **Tamaño del catálogo:** 1,117 juegos (1,114 elegibles). Solo 887 tienen ambas notas, y 16 géneros alcanzan n ≥ 20. La prueba del clasificador tiene 222 casos.
- **Popularidad medida con Backloggd:** Plays, Playing, Backlogs y Wishlist son interacciones declaradas, no ventas ni usuarios únicos. El índice de popularidad usa pesos iguales, y esa elección es discutible.
- **Sin datos de juegos como servicio (GaaS):** el maestro no tiene etiquetas de fracaso, modelo de negocio ni ingresos. Los resultados no permiten hablar de riesgo comercial GaaS.
- **Sesgo de selección:** el catálogo contiene sobre todo juegos conocidos, y los fracasos están poco representados.
- **Notas de prensa:** 218 de 1,117 son estimaciones propias y se excluyen. La cobertura de Metacritic puede no ser aleatoria.
- **Posible review bombing en Rating:** los reportes no incluyen datos temporales ni de volumen de reseñas. No puedo confirmarlo ni descartarlo. La brecha media es negativa en casi todos los géneros, pero eso no demuestra manipulación.
- **Otras limitaciones:**
  - Orange no se ejecutó.
  - Weka y Python usan protocolos distintos (K-Means: 477/410 frente a 465/422; DBSCAN: 887 frente a 866 + 21 de ruido).
  - Hay tres conflictos históricos sin resolver.
  - Las probabilidades del modelo no están calibradas.

## 5. Conclusión

Este trabajo puede orientar a una desarrolladora sobre qué asociaciones aparecen entre recepción de usuarios, prensa e interés declarado en Backloggd, y sobre qué géneros muestran mayor o menor acuerdo entre usuarios y crítica. Un clasificador de popularidad relativa supera a la referencia en esta partición, con un F1 macro de 0.5008. Es modesto y falla sobre todo en la clase media. No puede afirmar que una nota alta cause más juego, ni predecir ventas o éxito comercial, ni evaluar riesgos de juegos como servicio. Tampoco acredita segmentos de mercado a partir de DBSCAN y K-Means. Tampoco sirve como predicción previa al lanzamiento, porque usa notas ya publicadas.

