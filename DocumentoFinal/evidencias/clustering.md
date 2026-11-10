# Correlaciones y clustering de videojuegos

Entrada: `data/clean/dataset_depurado.csv`, SHA-256 `f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652`. Semilla: 42. La fuente permanece intacta.

Universo: 1117 juegos. Cohorte histórica elegible: 1114; conflictos pendientes excluidos: 3. Casos completos elegibles: 887; no agrupados por ausencias o conflictos: 230. La salida conserva todos los juegos.

## 1. Correlaciones

**Poblaciones y cobertura.** Las correlaciones usan pares completos para cada comparación. Se excluyen grupos con menos de 20 pares válidos, criterio más conservador que contar 20 juegos aunque falten notas; los n y las exclusiones se muestran explícitamente.

**Procedencia.** Metacritic Rating es la columna analítica producida por la fase 02: excluye estimaciones propias. Se valida la coherencia con critic_source y la brecha antes de calcular; las etiquetas del CSV no son una comprobación externa de cada nota.

### Catálogo: usuarios frente a prensa

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Catálogo | 1114 | 887 | 0.5439 | 1.936e-69 | 0.5242 | 9.34e-64 |

Pearson estima asociación lineal y Spearman asociación monótona basada en rangos; ninguno mide acuerdo ni causalidad. No se interpretan las diferencias entre coeficientes de grupos superpuestos como diferencias estadísticamente probadas.

### Géneros incluidos

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Adventure | 724 | 598 | 0.5746 | 7.923e-54 | 0.5443 | 1.975e-47 |
| RPG | 366 | 286 | 0.5014 | 1.305e-19 | 0.5175 | 5.464e-21 |
| Shooter | 260 | 223 | 0.5596 | 8.892e-20 | 0.5286 | 1.886e-17 |
| Platform | 239 | 188 | 0.6428 | 2.68e-23 | 0.5525 | 2.029e-16 |
| Indie | 207 | 166 | 0.5383 | 7.452e-14 | 0.5536 | 1.034e-14 |
| Puzzle | 133 | 110 | 0.3601 | 0.0001118 | 0.45 | 8.137e-07 |
| Strategy | 116 | 94 | 0.434 | 1.241e-05 | 0.3373 | 0.0008857 |
| Brawler | 106 | 97 | 0.616 | 1.874e-11 | 0.615 | 2.06e-11 |
| Simulator | 94 | 79 | 0.5347 | 3.846e-07 | 0.5026 | 2.356e-06 |
| Turn Based Strategy | 71 | 51 | 0.2514 | 0.0752 | 0.382 | 0.005668 |
| Fighting | 62 | 46 | 0.6188 | 4.577e-06 | 0.5826 | 2.159e-05 |
| Arcade | 61 | 39 | 0.7548 | 2.832e-08 | 0.6229 | 2.289e-05 |
| Visual Novel | 54 | 27 | -0.1042 | 0.605 | -0.1382 | 0.4917 |
| Tactical | 42 | 37 | 0.3467 | 0.03554 | 0.3602 | 0.02852 |
| Racing | 37 | 31 | 0.4916 | 0.004976 | 0.4357 | 0.01428 |
| Point-and-Click | 36 | 27 | 0.6546 | 0.0002117 | 0.6395 | 0.0003293 |

Cada juego participa una vez en cada género declarado, no solo en genero_principal. Los grupos se superponen y sus n no se suman para contar juegos.

### Géneros excluidos

| grupo | n_juegos | n | estado |
| --- | --- | --- | --- |
| Music | 21 | 18 | excluido: menos de 20 pares completos |
| Sport | 20 | 18 | excluido: menos de 20 pares completos |
| Card & Board Game | 13 | 10 | excluido: menos de 20 pares completos |
| Real Time Strategy | 9 | 9 | excluido: menos de 20 pares completos |
| Quiz/Trivia | 3 | 2 | excluido: menos de 20 pares completos |
| MOBA | 2 | 2 | excluido: menos de 20 pares completos |
| Pinball | 1 | 1 | excluido: menos de 20 pares completos |

### Organizaciones con más juegos

Se seleccionan las 15 organizaciones con más títulos antes de observar los coeficientes y luego se aplica el mínimo de 20 pares. Team mezcla desarrolladores y editores: esta tabla no acredita que todas estas organizaciones sean estudios desarrolladores.

| grupo | n_juegos | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Nintendo | 170 | 125 | 0.441 | 2.636e-07 | 0.4611 | 6.257e-08 |
| Capcom | 64 | 51 | 0.6717 | 6.802e-08 | 0.541 | 4.152e-05 |
| Square Enix | 59 | 49 | 0.5977 | 5.767e-06 | 0.5985 | 5.569e-06 |
| Sega | 46 | 31 | 0.6937 | 1.509e-05 | 0.6595 | 5.449e-05 |
| Electronic Arts | 43 | 42 | 0.558 | 0.0001233 | 0.5347 | 0.0002643 |
| Konami | 31 | 22 | 0.618 | 0.002175 | 0.4439 | 0.03851 |
| Activision | 30 | 26 | 0.4132 | 0.03587 | 0.3851 | 0.05204 |
| Bandai Namco Entertainment | 28 | 25 | 0.7966 | 1.897e-06 | 0.7371 | 2.636e-05 |
| Ubisoft Entertainment | 27 | 27 | 0.6419 | 0.0003076 | 0.683 | 8.648e-05 |
| Atlus | 26 | 23 | 0.5554 | 0.005934 | 0.4705 | 0.02347 |
| Sony Interactive Entertainment | 24 | 22 | 0.7309 | 0.0001116 | 0.6341 | 0.001529 |

Excluidas dentro de las 15 más frecuentes:

| grupo | n_juegos | n | estado |
| --- | --- | --- | --- |
| Nintendo EAD | 22 | 15 | excluido: menos de 20 pares completos |
| Game Freak | 20 | 16 | excluido: menos de 20 pares completos |
| Sony Computer Entertainment | 18 | 15 | excluido: menos de 20 pares completos |
| Square | 18 | 10 | excluido: menos de 20 pares completos |

El CSV clustering_03_correlaciones_organizaciones.csv conserva el inventario completo, incluidos los grupos pequeños y la razón de exclusión.

### Comprobación por sesgo de las señales

| variable | asimetria_original | asimetria_log1p |
| --- | --- | --- |
| Plays | 1.836 | -1.763 |
| Playing | 4.845 | -0.359 |
| Backlogs | 1.834 | -0.8745 |
| Wishlist | 2.343 | -0.6942 |

Spearman se calcula también para todos los pares de las seis variables, sobre sus valores originales. Es una comprobación útil ante asimetría y relaciones monótonas no lineales; log1p no cambia el orden de los conteos, y por tanto no cambia sus rangos.

| variable_a | variable_b | n | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- |
| Plays | Playing | 1114 | 0.5395 | 3.729e-85 | 0.5471 | 5.442e-88 |
| Plays | Backlogs | 1114 | 0.5959 | 4.68e-108 | 0.5973 | 1.146e-108 |
| Plays | Wishlist | 1114 | 0.3498 | 2.033e-33 | 0.3413 | 8.696e-32 |
| Plays | Rating | 1101 | 0.1517 | 4.282e-07 | 0.08737 | 0.003716 |
| Plays | Metacritic Rating | 896 | 0.4144 | 1.681e-38 | 0.423 | 3.291e-40 |
| Playing | Backlogs | 1114 | 0.654 | 5.851e-137 | 0.7505 | 3.137e-202 |
| Playing | Wishlist | 1114 | 0.6279 | 3.35e-123 | 0.7013 | 1.13e-165 |
| Playing | Rating | 1101 | 0.2375 | 1.392e-15 | 0.4017 | 5.977e-44 |
| Playing | Metacritic Rating | 896 | 0.2634 | 1.103e-15 | 0.3458 | 1.449e-26 |
| Backlogs | Wishlist | 1114 | 0.7912 | 1.028e-239 | 0.8542 | ≈0 (límite numérico) |
| Backlogs | Rating | 1101 | 0.3927 | 6.634e-42 | 0.4133 | 1.137e-46 |
| Backlogs | Metacritic Rating | 896 | 0.4047 | 1.244e-36 | 0.433 | 3.098e-42 |
| Wishlist | Rating | 1101 | 0.4232 | 4.518e-49 | 0.5035 | 7.762e-72 |
| Wishlist | Metacritic Rating | 896 | 0.3273 | 8.158e-24 | 0.3698 | 2.044e-30 |
| Rating | Metacritic Rating | 887 | 0.5439 | 1.936e-69 | 0.5242 | 9.34e-64 |

Los CSV conservan p-valores y q de Benjamini–Hochberg por familia y método. Los p-valores de Spearman usan la aproximación asintótica de SciPy, no permutaciones exactas; con grupos pequeños o muchos empates deben interpretarse con cautela. Cuando SciPy devuelve cero por límite numérico, se muestra ≈0 y no se afirma una probabilidad exactamente nula.

El p-valor es bilateral y contrasta asociación nula, no igualdad de notas; la dependencia entre juegos/franquicias y los grupos superpuestos limita la inferencia.

### Coincidencia y discrepancia por género

**Criterio.** Se ordena por media de la brecha absoluta, en puntos sobre 100: menor valor significa mayor cercanía de puntuaciones. La brecha firmada Rating × 20 − Metacritic informa dirección; una media cercana a cero puede ocultar diferencias opuestas, por eso no se usa para ordenar.

| grupo | n | brecha_absoluta_media | brecha_media | pearson_r | pearson_p | spearman_rho | spearman_p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Visual Novel | 27 | 8.222 | -1.926 | -0.1042 | 0.605 | -0.1382 | 0.4917 |
| Brawler | 97 | 8.959 | -7.99 | 0.616 | 1.874e-11 | 0.615 | 2.06e-11 |
| Point-and-Click | 27 | 9 | -8.259 | 0.6546 | 0.0002117 | 0.6395 | 0.0003293 |
| Arcade | 39 | 9.051 | -8.128 | 0.7548 | 2.832e-08 | 0.6229 | 2.289e-05 |
| RPG | 286 | 9.346 | -7.871 | 0.5014 | 1.305e-19 | 0.5175 | 5.464e-21 |
| Indie | 166 | 9.542 | -8.133 | 0.5383 | 7.452e-14 | 0.5536 | 1.034e-14 |
| Turn Based Strategy | 51 | 9.569 | -7.529 | 0.2514 | 0.0752 | 0.382 | 0.005668 |
| Puzzle | 110 | 9.982 | -7.745 | 0.3601 | 0.0001118 | 0.45 | 8.137e-07 |
| Adventure | 598 | 10.11 | -8.468 | 0.5746 | 7.923e-54 | 0.5443 | 1.975e-47 |
| Simulator | 79 | 10.16 | -7.835 | 0.5347 | 3.846e-07 | 0.5026 | 2.356e-06 |
| Platform | 188 | 10.55 | -9.585 | 0.6428 | 2.68e-23 | 0.5525 | 2.029e-16 |
| Tactical | 37 | 11.03 | -9.946 | 0.3467 | 0.03554 | 0.3602 | 0.02852 |
| Strategy | 94 | 11.89 | -10.28 | 0.434 | 1.241e-05 | 0.3373 | 0.0008857 |
| Racing | 31 | 12 | -12 | 0.4916 | 0.004976 | 0.4357 | 0.01428 |
| Fighting | 46 | 12.02 | -10.67 | 0.6188 | 4.577e-06 | 0.5826 | 2.159e-05 |
| Shooter | 223 | 12.82 | -12.03 | 0.5596 | 8.892e-20 | 0.5286 | 1.886e-17 |

Menor distancia de puntuaciones (sin implicar concordancia de orden): Visual Novel, Brawler, Point-and-Click, Arcade, RPG. Mayores brechas absolutas: Shooter, Fighting, Racing, Strategy, Tactical.

La conversión de la fase 02 usa el máximo de cinco estrellas documentado de Backloggd y la escala 0–100 de prensa; no implica equivalencia psicométrica entre sus sistemas. La incertidumbre y las diferencias de composición impiden interpretar este orden como un ranking poblacional definitivo.

## 2. Preparación del clustering

**Variables.** Se usan Plays, Playing, Backlogs, Wishlist, Rating y Metacritic Rating. Los cuatro conteos reciben log1p para reducir escala y asimetría, conservando ceros; después StandardScaler se ajusta a las seis variables entre los casos completos.

**Faltantes.** No se imputan notas: excluir casos incompletos evita fabricar la recepción de los juegos. Se conservan en el CSV con incluido_clustering=False, motivo_no_agrupado y etiquetas vacías; la cobertura parcial puede sesgar los perfiles hacia títulos con crítica disponible.

**Género.** No entra a las distancias: se usa únicamente para describir la composición posterior. Así no se impone una distancia arbitraria entre categorías ni se pondera adicionalmente a juegos con múltiples géneros.

**Alcance.** Es segmentación descriptiva de todos los casos completos, por eso no hay partición de entrenamiento/prueba. Estos clusters sí usan calificaciones: no se debe evaluar después un clasificador de sus etiquetas usando las mismas notas como si fuera una validación independiente.

## 3. K-Means: elección de k

| k | inercia | silhouette |
| --- | --- | --- |
| 2 | 3299 | 0.3188 |
| 3 | 2748 | 0.2377 |
| 4 | 2455 | 0.2268 |
| 5 | 2232 | 0.218 |
| 6 | 2052 | 0.1947 |
| 7 | 1914 | 0.1898 |
| 8 | 1803 | 0.1764 |
| 9 | 1706 | 0.1768 |
| 10 | 1630 | 0.1725 |

![Inercia y silhouette](figures/clustering_03_kmeans.png)

**Elección.** k=2 maximiza silhouette entre 2 y 10; ante empate se prefiere el menor k. Se usan 30 inicializaciones y random_state=42; la inercia se muestra como diagnóstico complementario, no como criterio que siempre escogería el k más grande.

La preferencia de silhouette no acredita que existan segmentos comerciales naturales ni estabilidad frente a otra muestra. El género no se utilizó para seleccionar k.

## 4. DBSCAN: k-distancia y ruido

**Parámetros.** Se fija min_samples=12 como convención operativa de dos veces las seis dimensiones. La curva usa ese vecino contando el propio punto, coherente con la definición de densidad de DBSCAN; no se mezclan distancias de la escala original y la estandarizada.

**Selección reproducible.** Máxima separación x−y respecto de la cuerda, tras normalizar ambos ejes a [0,1]. Se obtiene eps=1.666296; no se selecciona el valor para forzar un número de clusters ni maximizar silhouette.

![Curva de k-distancia](figures/clustering_03_dbscan_kdistancia.png)

Resultado: 1 clusters y **21 puntos de ruido** (2.37% de los agrupables). La etiqueta −1 es ruido, no un perfil. Silhouette excluyendo ruido: no definida: no hay al menos dos clusters válidos.

Sensibilidad local a eps (min_samples fijo):

| factor_eps | eps | clusters | ruido | grupo_mayor |
| --- | --- | --- | --- | --- |
| 0.8 | 1.333 | 1 | 67 | 820 |
| 1 | 1.666 | 1 | 21 | 866 |
| 1.2 | 2 | 1 | 11 | 876 |

Esta comparación local no demuestra estabilidad general frente a remuestreo u otros min_samples. Un grupo dominante o muchos puntos de ruido limitan la utilidad de la segmentación, aunque una métrica aislada resulte favorable.

## 5. Interpretación de cada perfil

**Nombres propuestos.** Se describe la posición superior o inferior al promedio de los casos completos mediante la media de z-scores, sin umbral arbitrario de 0.5 ni categorías absolutas de calidad. Los valores medios acompañan los nombres; no se infieren ventas, rentabilidad ni condición de culto.

**Géneros y ejemplos.** Se muestran los tres géneros más frecuentes, con número y porcentaje de juegos del grupo; sus porcentajes pueden sumar más de 100 %. Los cinco ejemplos son los más cercanos al centro descriptivo del grupo en las seis dimensiones transformadas; para ruido se eligen los primeros cinco IDs. Si hay menos de cinco juegos se muestran todos.

### kmeans: etiqueta 0 · Actividad e interés superiores al promedio; recepción superior al promedio

Tamaño: **465** juegos. Géneros dominantes: Adventure: 352 (75.7%); RPG: 187 (40.2%); Shooter: 129 (27.7%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 7681 |
| Playing | 337.4 |
| Backlogs | 2022 |
| Wishlist | 1053 |
| Rating | 3.909 |
| Metacritic Rating | 86.26 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1056 | The Messenger |
| 304 | Dragon Age: Origins |
| 172 | Metroid: Zero Mission |
| 980 | The Legend of Zelda: Majora's Mask 3D |
| 517 | Luigi's Mansion 3 |

### kmeans: etiqueta 1 · Actividad e interés inferiores al promedio; recepción inferior al promedio

Tamaño: **422** juegos. Géneros dominantes: Adventure: 246 (58.3%); RPG: 99 (23.5%); Shooter: 94 (22.3%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 2981 |
| Playing | 67.96 |
| Backlogs | 476.1 |
| Wishlist | 246.2 |
| Rating | 3.378 |
| Metacritic Rating | 78.01 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1360 | Sonic Rush Adventure |
| 1420 | Black |
| 1375 | Toy Story 2: Buzz Lightyear to the Rescue! |
| 1398 | Shantae: Half-Genie Hero |
| 1338 | Condemned: Criminal Origins |

### dbscan: etiqueta -1 · Atípicos de densidad (ruido; no es un cluster)

Tamaño: **21** juegos. Géneros dominantes: Adventure: 12 (57.1%); Strategy: 7 (33.3%); Shooter: 6 (28.6%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 3348 |
| Playing | 146.1 |
| Backlogs | 280.3 |
| Wishlist | 120.4 |
| Rating | 2.924 |
| Metacritic Rating | 68.05 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 109 | League of Legends |
| 276 | Shadow the Hedgehog |
| 610 | Marvel Snap |
| 661 | Paladins |
| 667 | Wanted: Dead |

### dbscan: etiqueta 0 · Actividad e interés superiores al promedio; recepción superior al promedio

Tamaño: **866** juegos. Géneros dominantes: Adventure: 586 (67.7%); RPG: 283 (32.7%); Shooter: 217 (25.1%).

| variable | media_en_escala_original |
| --- | --- |
| Plays | 5495 |
| Playing | 210.8 |
| Backlogs | 1311 |
| Wishlist | 682.6 |
| Rating | 3.674 |
| Metacritic Rating | 82.68 |

Juegos de ejemplo:

| id_juego | juego |
| --- | --- |
| 1110 | Professor Layton and the Curious Village |
| 656 | Fire Emblem: The Sacred Stones |
| 666 | Persona 4 Arena Ultimax |
| 622 | Sunset Overdrive |
| 758 | Phoenix Wright: Ace Attorney - Spirit of Justice |

### Proyección complementaria

![Proyección PCA](figures/clustering_03_proyeccion.png)

PCA se usa solo para visualizar: las dos componentes conservan 75.1% de la varianza. Las etiquetas se ajustaron en seis dimensiones y no sobre esta proyección.

## 6. Artefactos y límites

`data/clean/dataset_con_clusters.csv` conserva los 1,117 registros de la fuente y agrega cluster_kmeans, cluster_dbscan, perfiles, incluido_clustering y motivo_no_agrupado. Las etiquetas vacías no significan ruido; −1 solo aparece para los casos completos considerados atípicos por DBSCAN.

Las tablas completas, búsqueda de k, curva de distancias, sensibilidad, medias y ejemplos se guardan con prefijo clustering_03_ en reports. El pipeline descriptivo se conserva en models/clustering_03.joblib junto con variables y parámetros; DBSCAN no aporta una regla predict de asignación para juegos nuevos.

Este es el único protocolo de clustering activo: la app y el orquestador leen estos mismos artefactos de seis variables. Los resultados antiguos de cuatro conteos quedan archivados fuera del flujo; las etiquetas descriptivas no se entregan al clasificador supervisado.

## Que debo verificar manualmente

- Procedencia/plataforma de Metacritic y escala histórica de Rating; las estimaciones siguen excluidas.
- Función de las organizaciones de Team: los nombres no acreditan que sean desarrolladores.
- Grupos con n<20 y sesgo por ausencias: los resultados representan los pares/casos disponibles.
- Codo de k-distancia, grupo dominante, ruido y estabilidad frente a otras muestras y parámetros.
- Interpretaciones de nombres y ejemplos: no son etiquetas de éxito comercial ni pruebas de causalidad.
- No usar notas para predecir estas etiquetas sin reconocer la circularidad de su construcción.

## Comparación interpretativa de k=2, k=3 y k=4

k=2 maximiza silhouette, pero resume sobre todo magnitud conjunta. Se presentan también k=3 y k=4 para evaluar perfiles cruzados sin cambiar k por conveniencia narrativa. Sus medias se calculan en las unidades originales; ver clustering_03_ejemplos_alternativas.csv para ejemplos de cada alternativa.

| metodo | cluster | n | perfil_propuesto | generos_dominantes | media_Plays | media_Playing | media_Backlogs | media_Wishlist | media_Rating | media_Metacritic Rating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| kmeans_k2 | 0 | 465 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 352 (75.7%); RPG: 187 (40.2%); Shooter: 129 (27.7%) | 7681 | 337.4 | 2022 | 1053 | 3.909 | 86.26 |
| kmeans_k2 | 1 | 422 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 246 (58.3%); RPG: 99 (23.5%); Shooter: 94 (22.3%) | 2981 | 67.96 | 476.1 | 246.2 | 3.378 | 78.01 |
| kmeans_k3 | 0 | 306 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 244 (79.7%); RPG: 131 (42.8%); Shooter: 87 (28.4%) | 8989 | 444.8 | 2472 | 1310 | 3.998 | 87.74 |
| kmeans_k3 | 1 | 177 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 91 (51.4%); Platform: 38 (21.5%); Shooter: 37 (20.9%) | 1949 | 32.81 | 273.3 | 146.5 | 3.146 | 74.54 |
| kmeans_k3 | 2 | 404 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 263 (65.1%); RPG: 129 (31.9%); Shooter: 99 (24.5%) | 4291 | 108.1 | 832.4 | 413.2 | 3.622 | 81.67 |
| kmeans_k4 | 0 | 238 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 155 (65.1%); Shooter: 77 (32.4%); RPG: 62 (26.1%) | 6319 | 140.5 | 904.3 | 357.2 | 3.356 | 81.55 |
| kmeans_k4 | 1 | 298 | Actividad e interés superiores al promedio; recepción superior al promedio | Adventure: 238 (79.9%); RPG: 127 (42.6%); Shooter: 83 (27.9%) | 9040 | 442.5 | 2504 | 1325 | 4.007 | 87.66 |
| kmeans_k4 | 2 | 159 | Actividad e interés inferiores al promedio; recepción inferior al promedio | Adventure: 76 (47.8%); Platform: 36 (22.6%); Shooter: 36 (22.6%) | 1992 | 31.4 | 265.1 | 140.5 | 3.097 | 73.66 |
| kmeans_k4 | 3 | 192 | Actividad e interés inferiores al promedio; recepción superior al promedio | Adventure: 129 (67.2%); RPG: 78 (40.6%); Indie: 46 (24.0%) | 1640 | 79.6 | 716.2 | 476.8 | 3.949 | 82.23 |

## Sensibilidad a títulos compartidos

Las relaciones entre tablas usan id_juego, nunca Title. Como análisis de sensibilidad, se promedian las dos notas dentro de cada título sobre sus pares completos y se recalculan Pearson/Spearman por título único. Esto reduce el peso de nombres repetidos, pero puede juntar obras distintas: no sustituye la unidad juego ni resuelve remakes. El archivo clustering_03_sensibilidad_titulos.csv incluye géneros y organizaciones.

| grupo | variable_a | variable_b | n_juegos | n | estado | pearson_r | pearson_p | spearman_rho | spearman_p | familia | n_registros_pareados |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Catálogo | Rating | Metacritic Rating | 876 | 876 | incluido | 0.5462 | 2.907e-69 | 0.5242 | 5.352e-63 | catalogo | 887 |

## Diagnóstico de la auditoría

Se excluyen 3 conflictos numéricos históricos señalados; no se cambia el maestro. El grupo Visual Novel puede tener menor brecha absoluta sin concordancia de orden: revisar r, rho y sus p-valores. La cercanía de puntuaciones no prueba que usuarios y críticos ordenen igual los juegos. Tampoco se atribuye una varianza mínima sin comprobarla.

Si DBSCAN devuelve un solo grupo, no se inventa una silhouette ni se fuerza eps para obtener perfiles. Con este protocolo es un detector de núcleo y atípicos; su utilidad como segmentación de mercado queda rechazada. La curva geométrica y la sensibilidad local son diagnósticos, no pruebas de separación natural.

## Que debo verificar manualmente

- Resolver plataformas de conflictos heredados y validar títulos compartidos.
- Elegir entre parsimonia de k=2 y utilidad descriptiva de k=3/4 antes de convertir perfiles en decisiones.
- No usar etiquetas ni scaler descriptivo como entrada de la clasificación supervisada.
