# Carpeta: DocumentoFinal/evidencias

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `DocumentoFinal/evidencias/BITACORA_UNIFICADA.md` · Bytes: 1265 · SHA-256: `9e2c60880eb9761c3d68d33e0955be14856d39029ad99cc391db1f6ba85bc4f1`

`````text
# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: DocumentoFinal/evidencias/pruebas.txt

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

`````

## auditoria.json

Ruta: `DocumentoFinal/evidencias/auditoria.json` · Bytes: 690 · SHA-256: `32b012b07dc1ceb64c76dbce53f2edd2b63d9322a23962af7f8019405d11edc2`

````text
{
  "n_entrenamiento": 892,
  "n_prueba": 222,
  "exactitud_prueba": 0.5675675675675675,
  "f1_macro_prueba": 0.5577027296634777,
  "f1_ponderado_prueba": 0.5539995111974958,
  "recall_por_clase": {
    "bajo": 0.6417910447761194,
    "medio": 0.3375,
    "alto": 0.7466666666666667
  },
  "matriz_confusion": [
    [
      43,
      14,
      10
    ],
    [
      32,
      27,
      21
    ],
    [
      9,
      10,
      56
    ]
  ],
  "paridad_predicciones_guardadas": true,
  "probabilidades_validas": true,
  "vecinos_solo_entrenamiento_y_mismo_espacio": true,
  "objetivo_reproducido": true,
  "sha256_modelo": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e"
}
````

## clustering.md

Ruta: `DocumentoFinal/evidencias/clustering.md` · Bytes: 21886 · SHA-256: `9f9f8a377f6920035fb8388546e68118bb28dc9e35924c4de2c5b6b8f944193d`

````text
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

````

## comparativo_herramientas.csv

Ruta: `DocumentoFinal/evidencias/comparativo_herramientas.csv` · Bytes: 14198 · SHA-256: `16e8e53c939be9db1802c5da0d55f5c474484408a5b3dc5aa4f3ac5413066893`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## decision.json

Ruta: `DocumentoFinal/evidencias/decision.json` · Bytes: 1000 · SHA-256: `cd3c19e80e1eef1cd9b55801e659edd5d653e8dc0450b2cf2ef08ed5dfcf9e38`

````text
{
  "ganador_cv": "Vigente",
  "mejora_f1_cv": 0.0,
  "pliegues_superiores": 0,
  "criterio_predefinido": "Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.",
  "recomienda_promocion": false,
  "parametros": {
    "bootstrap": true,
    "ccp_alpha": 0.0,
    "class_weight": null,
    "criterion": "gini",
    "max_depth": null,
    "max_features": "sqrt",
    "max_leaf_nodes": null,
    "max_samples": null,
    "min_impurity_decrease": 0.0,
    "min_samples_leaf": 5,
    "min_samples_split": 2,
    "min_weight_fraction_leaf": 0.0,
    "monotonic_cst": null,
    "n_estimators": 200,
    "n_jobs": 1,
    "oob_score": false,
    "random_state": 42,
    "verbose": 0,
    "warm_start": false
  },
  "limitacion": "Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva."
}
````

## inspeccion.md

Ruta: `DocumentoFinal/evidencias/inspeccion.md` · Bytes: 3232 · SHA-256: `52ae5a3d981eb4808a1107714f45469794e804b3222ab3a0e0c18b2e27a12c2b`

````text
# Inspección reproducible del maestro

Generado por src/01_inspeccion.py. Fuente: data/raw/games_curated.csv; 1117 filas y 42 columnas. SHA-256: b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd.
El maestro es el original designado, ya curado. El antecedente de 1,512 filas se conserva separado en data/historical y se audita en trazabilidad_historica.md; no se reemplaza el maestro.

Rating observado: 0.7–4.8, 13 ausencias. Metacritic original: 45–99; crítica utilizable: 899; estimaciones excluidas: 218.

Los seis conteos ya son numéricos en el maestro: esta fase no afirma haber convertido textos K/M. Su formato y la cuenta real de conversiones quedan en limpieza_log.md. El esquema completo está en inspeccion.json.

Hay 35 registros de 17 títulos compartidos en fechas distintas. No se presume que sean el mismo juego: relaciones por id_juego, nunca por Title. Los 3 casos numéricos heredados sin resolver se mantienen señalados y no participan del análisis principal.

## Seis figuras del EDA

![rating](figures/eda_rating.png)

![metacritic](figures/eda_metacritic.png)

![plays_log](figures/eda_plays_log.png)

![decadas](figures/eda_decadas.png)

![generos_top15](figures/eda_generos_top15.png)

![rating_vs_metacritic](figures/eda_rating_vs_metacritic.png)

Las distribuciones describen el maestro completo disponible; la inferencia y el clustering aplican además la elegibilidad histórica. Los géneros se cuentan como pertenencias múltiples; faltan tres fechas, sin inventar década. Team no acredita roles de desarrollo.

# Evidencia documental de escalas

## Escalas verificadas antes de calcular la brecha

Consulta de documentación primaria: **8 de noviembre de 2026**. No se reemplazaron notas ni conteos del CSV por valores actuales del sitio.

- [Backloggd: página oficial de Elden Ring](https://backloggd.com/games/elden-ring/) muestra la media junto al gráfico de estrellas cuyo extremo superior es **5 estrellas**. [Su FAQ](https://backloggd.com/about/) distingue la media del juego y el promedio ponderado utilizado para ordenar. Esta evidencia respalda el denominador cinco; no prueba por sí sola cómo se extrajo cada fila histórica.
- [Metacritic: interpretación del Metascore](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore) documenta una escala de **0–100** para prensa.
- Los rangos del CSV son compatibles con esas escalas. El derivado heredado `rating_100` coincide con multiplicar por 20, pero se usa solo como corroboración y no como prueba independiente de la escala.

Se aplicará una conversión por el máximo documentado: `rating_normalizado = Rating / 5 × 100`; `brecha = rating_normalizado − Metacritic Rating` solo cuando la nota crítica tenga procedencia válida según el maestro.
No se usa normalización min–max de la muestra: convertir 0.7 y 4.8 en los extremos produciría una brecha dependiente de los juegos incluidos. La conversión tampoco afirma equivalencia psicométrica entre ambas plataformas.


## Que debo verificar manualmente

- Procedencia de notas, escala histórica y decisiones de deduplicación.
- Roles de Team, fechas TBD y títulos iguales en versiones distintas.

````

## integridad_final.json

Ruta: `DocumentoFinal/evidencias/integridad_final.json` · Bytes: 169 · SHA-256: `90e1137d1c8fcc542b15d7f84670248c35134f5288086b6c057dc1ab4667a7b5`

````text
{
  "archivos_verificados": 20,
  "modificados": [],
  "modelo_conservado": true,
  "sha256_modelo": "ee362dae946d18981714171de2d66c0b93fc00a364e6990f698ed3b68ae8550e"
}
````

## limpieza_log.md

Ruta: `DocumentoFinal/evidencias/limpieza_log.md` · Bytes: 7436 · SHA-256: `dd4b45eb48ce4f385f86d51166ea06cc0347fe85bf67370a74a70b86f8ae8d45`

````text
# Log de limpieza

SHA-256 del insumo inmutable: `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`.

Fuente: `data/raw/games_curated.csv`. Decisiones previas: `reports/inspeccion.md`.

| Paso | Filas antes | Filas después | Eliminadas | Razón del cambio | Detalle |
|---|---:|---:|---:|---|---|
| 1. Validación y conversión de conteos | 1117 | 1117 | 0 | Sin cambio de filas | En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución. |
| 2. Fechas | 1117 | 1117 | 0 | Sin cambio de filas | 0 fechas ausentes y 3 no interpretables; no se eliminan juegos. |
| 3. Géneros | 1117 | 1117 | 0 | Sin cambio de filas | Primer género no vacío como convención de presentación; tabla larga tras deduplicar. |
| 4. Faltantes y procedencia | 1117 | 1117 | 0 | Sin cambio de filas | Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa. |
| 5. Duplicados | 1117 | 1117 | 0 | Sin cambio de filas | Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución. |
| 6. Escalas y brecha | 1117 | 1117 | 0 | Sin cambio de filas | Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra. |
| 7. Preparación de exportación | 1117 | 1117 | 0 | Sin cambio de filas | Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one. |

## Decisiones y justificación

**Conteos y fechas.** Se convierten solo formatos numéricos reconocidos; los inválidos causan un error con columna y fila. Las fechas desconocidas o imposibles se conservan como NaT con indicador: inventar un año alteraría el análisis por década.

**Faltantes.** No se imputan notas ni se eliminan juegos por ausencia. La imputación estadística pertenece al entrenamiento dentro de cada fold; en análisis descriptivo se usan pares completos e indicadores para mostrar la cobertura.

**Procedencia.** Se conserva Metacritic original en metacritic_rating_original y se usa critic_score_final con su etiqueta de fuente para la columna analítica. Una nota derivada de Rating no aporta evidencia independiente de prensa; la etiqueta del CSV no demuestra verificación externa.

**Géneros.** El primer elemento no vacío es una convención de presentación, no un género dominante acreditado. La tabla larga conserva cada género distinto y el ID; sus filas no se suman para contar juegos únicos.

**Duplicados.** Solo se descartan equivalencias analíticas bajo la clave documentada y se guardan las filas eliminadas. Un conflicto impide exportar para evitar seleccionar una cifra sin fundamento.

## Verificación de escalas previa a la brecha

Fuentes primarias consultadas el 08/11/2026: [Backloggd, extremo superior de cinco estrellas](https://backloggd.com/games/elden-ring/) y [Metacritic, escala 0–100](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore). No se descargan ni sustituyen puntuaciones actuales.

Conversión por máximo documentado: `rating_normalizado = Rating × 100 / 5`; `brecha = rating_normalizado − Metacritic Rating`. Positiva: usuarios por encima de prensa; negativa: por debajo. No se trasladan los extremos observados de la muestra a 0 y 100, ni se afirma equivalencia psicométrica.

Rango observado Rating: 0.7–4.8; Metacritic original: 45–99; crítica analítica: 45–99.

## Conciliación comprobable

El bloque JSON permite contrastar el log con la tabla exportada. Toda disminución requiere una razón; ningún otro paso puede añadir o eliminar juegos.

```json
{
  "filas_entrada": 1117,
  "filas_salida": 1117,
  "filas_generos_largo": 2682,
  "pasos": [
    {
      "paso": "1. Validación y conversión de conteos",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución."
    },
    {
      "paso": "2. Fechas",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "0 fechas ausentes y 3 no interpretables; no se eliminan juegos."
    },
    {
      "paso": "3. Géneros",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Primer género no vacío como convención de presentación; tabla larga tras deduplicar."
    },
    {
      "paso": "4. Faltantes y procedencia",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa."
    },
    {
      "paso": "5. Duplicados",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución."
    },
    {
      "paso": "6. Escalas y brecha",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra."
    },
    {
      "paso": "7. Preparación de exportación",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one."
    }
  ]
}
```

## Que debo verificar manualmente

- Representación de cinco estrellas en la extracción histórica, media absoluta/ponderada y origen de cada nota de prensa.
- Fechas numéricas ambiguas: se usa día/mes/año; consultar las marcadas no interpretables.
- Orden de la lista de géneros y posibles plataformas o versiones distintas con igual título/fecha.
- Las ausencias de crítica utilizable incluyen estimaciones excluidas; no significan que el juego no tenga nota fuera del CSV.

## Antecedente de la deduplicación

Estado: verificado. Esta corrida no elimina las 395 filas históricas: ya no están en el maestro de entrada. Ver trazabilidad_historica.md, deduplicacion_historica.csv y conflictos_historicos.csv para decisiones por ID. No confundir 0 descartes actuales con ausencia de decisiones anteriores.

## Que debo verificar manualmente

- Resolver los conflictos heredados y usar id_juego para relacionar tablas.

````

## metadata.json

Ruta: `DocumentoFinal/evidencias/metadata.json` · Bytes: 63731 · SHA-256: `07ba1ce664747e68c06c7ab9dc799e8ccb565cf71e7222b3a6de9f8548eed2fa`

````text
{
  "version_sklearn": "1.9.1",
  "python": "3.15.2",
  "fecha": "2026-11-09T08:35:00-06:00",
  "zona_horaria": "America/Mexico_City",
  "semilla": 42,
  "modelo": "RandomForestClassifier",
  "variables": [
    "generos",
    "estudio",
    "decada",
    "Metacritic Rating",
    "Rating"
  ],
  "clases": [
    "bajo",
    "medio",
    "alto"
  ],
  "orden_probabilidades": [
    "alto",
    "bajo",
    "medio"
  ],
  "definicion_objetivo": {
    "version": "INDICE-PERCENTILES-TRAIN-2.0",
    "opcion": "indice_percentiles",
    "campos": [
      "Plays",
      "Wishlist",
      "Backlogs"
    ],
    "formula": "(P_train(Plays) + P_train(Wishlist) + P_train(Backlogs)) / 3",
    "referencias": {
      "Plays": {
        "valores": [
          0.0,
          1.0,
          2.0,
          3.0,
          5.0,
          13.0,
          16.0,
          20.0,
          26.0,
          37.0,
          55.0,
          59.0,
          61.0,
          67.0,
          69.0,
          72.0,
          73.0,
          104.0,
          106.0,
          130.0,
          160.0,
          164.0,
          167.0,
          183.0,
          185.0,
          186.0,
          187.0,
          195.0,
          199.0,
          218.0,
          225.0,
          239.0,
          244.0,
          248.0,
          252.0,
          253.0,
          258.0,
          265.0,
          269.0,
          294.0,
          297.0,
          305.0,
          308.0,
          321.0,
          329.0,
          332.0,
          335.0,
          340.0,
          350.0,
          356.0,
          370.0,
          393.0,
          397.0,
          408.0,
          413.0,
          424.0,
          431.0,
          442.0,
          445.0,
          477.0,
          484.0,
          492.0,
          512.0,
          513.0,
          514.0,
          523.0,
          538.0,
          544.0,
          547.0,
          555.0,
          558.0,
          561.0,
          577.0,
          625.0,
          634.0,
          646.0,
          647.0,
          648.0,
          676.0,
          713.0,
          718.0,
          727.0,
          737.0,
          750.0,
          751.0,
          753.0,
          762.0,
          763.0,
          772.0,
          779.0,
          785.0,
          787.0,
          796.0,
          797.0,
          820.0,
          847.0,
          848.0,
          859.0,
          871.0,
          874.0,
          889.0,
          891.0,
          895.0,
          907.0,
          927.0,
          932.0,
          933.0,
          935.0,
          939.0,
          949.0,
          969.0,
          976.0,
          983.0,
          984.0,
          986.0,
          987.0,
          992.0,
          1000.0,
          1100.0,
          1200.0,
          1300.0,
          1400.0,
          1500.0,
          1600.0,
          1700.0,
          1800.0,
          1900.0,
          2000.0,
          2100.0,
          2200.0,
          2300.0,
          2400.0,
          2500.0,
          2600.0,
          2700.0,
          2800.0,
          2900.0,
          3000.0,
          3100.0,
          3200.0,
          3300.0,
          3400.0,
          3500.0,
          3600.0,
          3700.0,
          3800.0,
          3900.0,
          4000.0,
          4100.0,
          4200.0,
          4300.0,
          4400.0,
          4500.0,
          4600.0,
          4700.0,
          4800.0,
          4900.0,
          5000.0,
          5100.0,
          5200.0,
          5300.0,
          5400.0,
          5500.0,
          5600.0,
          5700.0,
          5800.0,
          5900.0,
          6000.0,
          6100.0,
          6200.0,
          6300.0,
          6400.0,
          6500.0,
          6600.0,
          6700.0,
          6800.0,
          6900.0,
          7000.0,
          7100.0,
          7200.0,
          7300.0,
          7400.0,
          7500.0,
          7600.0,
          7700.0,
          7800.0,
          7900.0,
          8000.0,
          8100.0,
          8200.0,
          8300.0,
          8400.0,
          8500.0,
          8600.0,
          8700.0,
          8800.0,
          8900.0,
          9000.0,
          9100.0,
          9200.0,
          9300.0,
          9400.0,
          9500.0,
          9600.0,
          9700.0,
          9800.0,
          9900.0,
          10000.0,
          11000.0,
          12000.0,
          13000.0,
          14000.0,
          15000.0,
          16000.0,
          17000.0,
          18000.0,
          19000.0,
          20000.0,
          21000.0,
          22000.0,
          25000.0,
          28000.0,
          30000.0,
          33000.0
        ],
        "percentiles": [
          0.0011210762331838565,
          0.003923766816143498,
          0.006726457399103139,
          0.008408071748878924,
          0.010089686098654708,
          0.011210762331838564,
          0.01289237668161435,
          0.014573991031390135,
          0.01569506726457399,
          0.016816143497757848,
          0.017937219730941704,
          0.01905829596412556,
          0.020179372197309416,
          0.021300448430493273,
          0.02242152466367713,
          0.023542600896860985,
          0.02466367713004484,
          0.0257847533632287,
          0.026905829596412557,
          0.028026905829596414,
          0.02914798206278027,
          0.030269058295964126,
          0.03139013452914798,
          0.032511210762331835,
          0.033632286995515695,
          0.034753363228699555,
          0.03587443946188341,
          0.03699551569506727,
          0.03811659192825112,
          0.03923766816143498,
          0.04035874439461883,
          0.04147982062780269,
          0.042600896860986545,
          0.043721973094170405,
          0.04540358744394619,
          0.04708520179372197,
          0.04820627802690583,
          0.04932735426008968,
          0.05044843049327354,
          0.0515695067264574,
          0.052690582959641255,
          0.053811659192825115,
          0.05493273542600897,
          0.05605381165919283,
          0.05717488789237668,
          0.05829596412556054,
          0.05941704035874439,
          0.06053811659192825,
          0.061659192825112105,
          0.06278026905829596,
          0.06390134529147982,
          0.06502242152466367,
          0.06614349775784753,
          0.06782511210762332,
          0.06950672645739911,
          0.07062780269058296,
          0.07174887892376682,
          0.0734304932735426,
          0.07511210762331838,
          0.07623318385650224,
          0.0773542600896861,
          0.07847533632286996,
          0.0795964125560538,
          0.08071748878923767,
          0.08183856502242152,
          0.08295964125560538,
          0.08408071748878924,
          0.08520179372197309,
          0.08632286995515695,
          0.08744394618834081,
          0.08856502242152467,
          0.08968609865470852,
          0.09080717488789238,
          0.09192825112107623,
          0.0930493273542601,
          0.09417040358744394,
          0.0952914798206278,
          0.09641255605381166,
          0.09753363228699552,
          0.09865470852017937,
          0.09977578475336323,
          0.10089686098654709,
          0.10201793721973094,
          0.1031390134529148,
          0.10426008968609865,
          0.10538116591928251,
          0.10650224215246637,
          0.10818385650224215,
          0.10986547085201794,
          0.1109865470852018,
          0.11210762331838565,
          0.1132286995515695,
          0.11434977578475336,
          0.11547085201793722,
          0.11659192825112108,
          0.11827354260089686,
          0.11995515695067265,
          0.1210762331838565,
          0.12219730941704036,
          0.12331838565022421,
          0.12443946188340807,
          0.12556053811659193,
          0.1266816143497758,
          0.12780269058295965,
          0.1289237668161435,
          0.13004484304932734,
          0.1311659192825112,
          0.13228699551569506,
          0.13396860986547085,
          0.13565022421524664,
          0.1367713004484305,
          0.13789237668161436,
          0.13901345291479822,
          0.14013452914798205,
          0.1412556053811659,
          0.14237668161434977,
          0.14349775784753363,
          0.148542600896861,
          0.16367713004484305,
          0.18497757847533633,
          0.2068385650224215,
          0.22869955156950672,
          0.24663677130044842,
          0.2673766816143498,
          0.2914798206278027,
          0.31053811659192826,
          0.32903587443946186,
          0.34417040358744394,
          0.3570627802690583,
          0.3688340807174888,
          0.38004484304932734,
          0.3957399103139013,
          0.4108744394618834,
          0.42376681614349776,
          0.4383408071748879,
          0.4523542600896861,
          0.46524663677130046,
          0.476457399103139,
          0.4854260089686099,
          0.4960762331838565,
          0.5044843049327354,
          0.5123318385650224,
          0.5213004484304933,
          0.5285874439461884,
          0.5397982062780269,
          0.5510089686098655,
          0.5610986547085202,
          0.5728699551569507,
          0.5840807174887892,
          0.5924887892376681,
          0.5980941704035875,
          0.6048206278026906,
          0.6121076233183856,
          0.6188340807174888,
          0.625,
          0.6311659192825112,
          0.6356502242152466,
          0.6384529147982063,
          0.6451793721973094,
          0.6541479820627802,
          0.6631165919282511,
          0.6737668161434978,
          0.6821748878923767,
          0.6889013452914798,
          0.695067264573991,
          0.6984304932735426,
          0.6995515695067265,
          0.7068385650224215,
          0.7169282511210763,
          0.7219730941704036,
          0.7253363228699552,
          0.7286995515695067,
          0.7320627802690582,
          0.7387892376681614,
          0.7477578475336323,
          0.7539237668161435,
          0.7572869955156951,
          0.7595291479820628,
          0.7640134529147982,
          0.7690582959641256,
          0.7718609865470852,
          0.7746636771300448,
          0.7785874439461884,
          0.7836322869955157,
          0.7892376681614349,
          0.7942825112107623,
          0.7982062780269058,
          0.8004484304932735,
          0.8026905829596412,
          0.8054932735426009,
          0.8071748878923767,
          0.8105381165919282,
          0.8155829596412556,
          0.8195067264573991,
          0.8234304932735426,
          0.8262331838565022,
          0.827354260089686,
          0.8290358744394619,
          0.8335201793721974,
          0.8380044843049327,
          0.8419282511210763,
          0.8464125560538116,
          0.8497757847533632,
          0.8542600896860987,
          0.8587443946188341,
          0.8615470852017937,
          0.8643497757847534,
          0.8727578475336323,
          0.8856502242152466,
          0.9030269058295964,
          0.922645739910314,
          0.9389013452914798,
          0.9495515695067265,
          0.9568385650224215,
          0.9641255605381166,
          0.9714125560538116,
          0.9798206278026906,
          0.9848654708520179,
          0.9893497757847534,
          0.9932735426008968,
          0.9949551569506726,
          0.9966367713004485,
          0.9983183856502242,
          1.0
        ]
      },
      "Wishlist": {
        "valores": [
          2.0,
          3.0,
          4.0,
          5.0,
          6.0,
          7.0,
          8.0,
          9.0,
          12.0,
          13.0,
          14.0,
          15.0,
          16.0,
          21.0,
          22.0,
          23.0,
          24.0,
          26.0,
          27.0,
          28.0,
          29.0,
          31.0,
          32.0,
          33.0,
          35.0,
          36.0,
          38.0,
          39.0,
          41.0,
          42.0,
          45.0,
          50.0,
          51.0,
          52.0,
          54.0,
          55.0,
          57.0,
          61.0,
          62.0,
          63.0,
          66.0,
          67.0,
          69.0,
          71.0,
          72.0,
          73.0,
          74.0,
          75.0,
          76.0,
          78.0,
          80.0,
          81.0,
          82.0,
          85.0,
          87.0,
          88.0,
          89.0,
          90.0,
          91.0,
          92.0,
          93.0,
          94.0,
          95.0,
          96.0,
          97.0,
          99.0,
          100.0,
          101.0,
          103.0,
          106.0,
          107.0,
          109.0,
          110.0,
          111.0,
          112.0,
          113.0,
          114.0,
          115.0,
          116.0,
          117.0,
          119.0,
          120.0,
          121.0,
          123.0,
          124.0,
          125.0,
          126.0,
          127.0,
          129.0,
          132.0,
          133.0,
          134.0,
          135.0,
          136.0,
          138.0,
          139.0,
          140.0,
          141.0,
          142.0,
          146.0,
          147.0,
          149.0,
          150.0,
          151.0,
          152.0,
          154.0,
          155.0,
          156.0,
          159.0,
          160.0,
          162.0,
          163.0,
          165.0,
          166.0,
          167.0,
          168.0,
          169.0,
          170.0,
          171.0,
          172.0,
          174.0,
          175.0,
          176.0,
          177.0,
          178.0,
          179.0,
          180.0,
          181.0,
          182.0,
          183.0,
          184.0,
          185.0,
          188.0,
          189.0,
          191.0,
          192.0,
          193.0,
          194.0,
          195.0,
          196.0,
          198.0,
          199.0,
          201.0,
          206.0,
          207.0,
          208.0,
          209.0,
          210.0,
          212.0,
          213.0,
          214.0,
          216.0,
          217.0,
          219.0,
          220.0,
          221.0,
          224.0,
          225.0,
          227.0,
          228.0,
          230.0,
          231.0,
          235.0,
          236.0,
          237.0,
          238.0,
          239.0,
          241.0,
          242.0,
          243.0,
          244.0,
          246.0,
          248.0,
          253.0,
          255.0,
          257.0,
          260.0,
          262.0,
          263.0,
          264.0,
          265.0,
          266.0,
          267.0,
          268.0,
          269.0,
          270.0,
          271.0,
          272.0,
          274.0,
          275.0,
          276.0,
          277.0,
          279.0,
          280.0,
          283.0,
          286.0,
          287.0,
          288.0,
          289.0,
          290.0,
          291.0,
          294.0,
          297.0,
          298.0,
          299.0,
          300.0,
          301.0,
          306.0,
          307.0,
          314.0,
          316.0,
          317.0,
          319.0,
          323.0,
          324.0,
          325.0,
          328.0,
          329.0,
          330.0,
          331.0,
          333.0,
          334.0,
          335.0,
          339.0,
          342.0,
          343.0,
          344.0,
          349.0,
          350.0,
          351.0,
          352.0,
          353.0,
          354.0,
          355.0,
          356.0,
          358.0,
          359.0,
          360.0,
          362.0,
          363.0,
          365.0,
          366.0,
          370.0,
          372.0,
          373.0,
          376.0,
          377.0,
          379.0,
          380.0,
          381.0,
          383.0,
          385.0,
          388.0,
          390.0,
          391.0,
          395.0,
          397.0,
          401.0,
          402.0,
          407.0,
          409.0,
          410.0,
          417.0,
          418.0,
          420.0,
          421.0,
          424.0,
          426.0,
          427.0,
          432.0,
          434.0,
          435.0,
          437.0,
          441.0,
          442.0,
          443.0,
          445.0,
          446.0,
          448.0,
          449.0,
          450.0,
          453.0,
          455.0,
          457.0,
          458.0,
          459.0,
          460.0,
          461.0,
          463.0,
          467.0,
          469.0,
          470.0,
          471.0,
          476.0,
          477.0,
          478.0,
          480.0,
          481.0,
          482.0,
          484.0,
          485.0,
          487.0,
          489.0,
          491.0,
          492.0,
          493.0,
          494.0,
          496.0,
          497.0,
          499.0,
          500.0,
          503.0,
          504.0,
          505.0,
          506.0,
          508.0,
          510.0,
          511.0,
          512.0,
          513.0,
          514.0,
          515.0,
          517.0,
          518.0,
          521.0,
          524.0,
          527.0,
          528.0,
          529.0,
          532.0,
          534.0,
          537.0,
          538.0,
          540.0,
          548.0,
          549.0,
          550.0,
          552.0,
          559.0,
          561.0,
          563.0,
          564.0,
          567.0,
          572.0,
          574.0,
          575.0,
          576.0,
          585.0,
          586.0,
          587.0,
          588.0,
          590.0,
          593.0,
          594.0,
          597.0,
          598.0,
          599.0,
          600.0,
          601.0,
          602.0,
          604.0,
          607.0,
          617.0,
          621.0,
          623.0,
          625.0,
          628.0,
          629.0,
          631.0,
          634.0,
          635.0,
          636.0,
          639.0,
          643.0,
          644.0,
          645.0,
          648.0,
          649.0,
          651.0,
          653.0,
          656.0,
          664.0,
          668.0,
          675.0,
          677.0,
          681.0,
          682.0,
          686.0,
          687.0,
          691.0,
          692.0,
          693.0,
          695.0,
          700.0,
          701.0,
          704.0,
          705.0,
          714.0,
          715.0,
          716.0,
          721.0,
          727.0,
          729.0,
          732.0,
          738.0,
          741.0,
          742.0,
          746.0,
          750.0,
          752.0,
          753.0,
          754.0,
          761.0,
          768.0,
          770.0,
          774.0,
          775.0,
          779.0,
          782.0,
          783.0,
          789.0,
          790.0,
          792.0,
          797.0,
          799.0,
          801.0,
          804.0,
          808.0,
          813.0,
          814.0,
          815.0,
          817.0,
          822.0,
          827.0,
          829.0,
          833.0,
          834.0,
          837.0,
          838.0,
          842.0,
          847.0,
          852.0,
          854.0,
          855.0,
          858.0,
          861.0,
          866.0,
          871.0,
          889.0,
          892.0,
          895.0,
          896.0,
          904.0,
          907.0,
          910.0,
          911.0,
          918.0,
          924.0,
          925.0,
          928.0,
          934.0,
          939.0,
          949.0,
          951.0,
          959.0,
          981.0,
          983.0,
          986.0,
          987.0,
          990.0,
          1000.0,
          1100.0,
          1200.0,
          1300.0,
          1400.0,
          1500.0,
          1600.0,
          1700.0,
          1800.0,
          1900.0,
          2000.0,
          2100.0,
          2200.0,
          2300.0,
          2400.0,
          2500.0,
          2600.0,
          2700.0,
          2800.0,
          2900.0,
          3000.0,
          3100.0,
          3300.0,
          3400.0,
          3600.0,
          3700.0,
          3800.0,
          4800.0,
          5400.0
        ],
        "percentiles": [
          0.0011210762331838565,
          0.002242152466367713,
          0.003923766816143498,
          0.005605381165919282,
          0.006726457399103139,
          0.007847533632286996,
          0.008968609865470852,
          0.010089686098654708,
          0.01233183856502242,
          0.014573991031390135,
          0.016255605381165918,
          0.017937219730941704,
          0.01961883408071749,
          0.021860986547085202,
          0.0257847533632287,
          0.030829596412556053,
          0.033632286995515695,
          0.034753363228699555,
          0.03643497757847534,
          0.03811659192825112,
          0.0397982062780269,
          0.04147982062780269,
          0.043161434977578475,
          0.04484304932735426,
          0.0476457399103139,
          0.05044843049327354,
          0.052690582959641255,
          0.05493273542600897,
          0.05605381165919283,
          0.05773542600896861,
          0.05997757847533632,
          0.061659192825112105,
          0.06278026905829596,
          0.06446188340807175,
          0.06782511210762332,
          0.07174887892376682,
          0.07511210762331838,
          0.0773542600896861,
          0.07847533632286996,
          0.08015695067264574,
          0.08239910313901345,
          0.08408071748878924,
          0.08576233183856502,
          0.08856502242152467,
          0.09080717488789238,
          0.09360986547085202,
          0.09641255605381166,
          0.09809417040358745,
          0.09977578475336323,
          0.10201793721973094,
          0.10426008968609865,
          0.10650224215246637,
          0.10986547085201794,
          0.11210762331838565,
          0.1132286995515695,
          0.11434977578475336,
          0.11547085201793722,
          0.11659192825112108,
          0.11883408071748879,
          0.12163677130044843,
          0.12387892376681614,
          0.12612107623318386,
          0.12780269058295965,
          0.12948430493273544,
          0.1311659192825112,
          0.13228699551569506,
          0.13396860986547085,
          0.1367713004484305,
          0.13901345291479822,
          0.1412556053811659,
          0.14349775784753363,
          0.14573991031390135,
          0.1491031390134529,
          0.15134529147982062,
          0.15246636771300448,
          0.15582959641255606,
          0.1591928251121076,
          0.16143497757847533,
          0.16367713004484305,
          0.1647982062780269,
          0.1664798206278027,
          0.1681614349775785,
          0.16928251121076232,
          0.1709641255605381,
          0.1726457399103139,
          0.17376681614349776,
          0.17600896860986548,
          0.17825112107623317,
          0.17937219730941703,
          0.18105381165919282,
          0.18385650224215247,
          0.1860986547085202,
          0.18721973094170405,
          0.18946188340807174,
          0.19170403587443946,
          0.19394618834080718,
          0.1984304932735426,
          0.20179372197309417,
          0.2040358744394619,
          0.20739910313901344,
          0.20964125560538116,
          0.21076233183856502,
          0.21300448430493274,
          0.21524663677130046,
          0.21748878923766815,
          0.2202914798206278,
          0.2219730941704036,
          0.22309417040358745,
          0.22533632286995517,
          0.2281390134529148,
          0.2303811659192825,
          0.23318385650224216,
          0.23598654708520178,
          0.2382286995515695,
          0.24047085201793722,
          0.24271300448430494,
          0.24439461883408073,
          0.2460762331838565,
          0.2483183856502242,
          0.2505605381165919,
          0.2528026905829596,
          0.25504484304932734,
          0.25672645739910316,
          0.257847533632287,
          0.2595291479820628,
          0.26121076233183854,
          0.2640134529147982,
          0.26681614349775784,
          0.2679372197309417,
          0.2701793721973094,
          0.27298206278026904,
          0.27522421524663676,
          0.2774663677130045,
          0.2802690582959641,
          0.2836322869955157,
          0.2858744394618834,
          0.2875560538116592,
          0.289237668161435,
          0.2920403587443946,
          0.29596412556053814,
          0.29876681614349776,
          0.3004484304932735,
          0.30213004484304934,
          0.30437219730941706,
          0.3060538116591928,
          0.3071748878923767,
          0.30885650224215244,
          0.31109865470852016,
          0.31446188340807174,
          0.3183856502242152,
          0.3211883408071749,
          0.3234304932735426,
          0.32567264573991034,
          0.32847533632286996,
          0.3307174887892377,
          0.33183856502242154,
          0.3329596412556054,
          0.33408071748878926,
          0.3374439461883408,
          0.34080717488789236,
          0.34360986547085204,
          0.34641255605381166,
          0.3486547085201794,
          0.3508968609865471,
          0.35201793721973096,
          0.3536995515695067,
          0.35538116591928254,
          0.3576233183856502,
          0.3609865470852018,
          0.3632286995515695,
          0.3649103139013453,
          0.367152466367713,
          0.3688340807174888,
          0.3710762331838565,
          0.3744394618834081,
          0.37668161434977576,
          0.3778026905829596,
          0.37948430493273544,
          0.3811659192825112,
          0.38228699551569506,
          0.3834080717488789,
          0.3850896860986547,
          0.3867713004484305,
          0.38789237668161436,
          0.3890134529147982,
          0.390695067264574,
          0.39405829596412556,
          0.3968609865470852,
          0.39798206278026904,
          0.3991031390134529,
          0.4013452914798206,
          0.40358744394618834,
          0.4047085201793722,
          0.40582959641255606,
          0.4069506726457399,
          0.4086322869955157,
          0.4103139013452915,
          0.41199551569506726,
          0.413677130044843,
          0.41535874439461884,
          0.41760089686098656,
          0.4192825112107623,
          0.4204035874439462,
          0.422085201793722,
          0.42376681614349776,
          0.4248878923766816,
          0.4260089686098655,
          0.42713004484304934,
          0.4282511210762332,
          0.42993273542600896,
          0.4316143497757848,
          0.4327354260089686,
          0.4344170403587444,
          0.43609865470852016,
          0.437219730941704,
          0.4383408071748879,
          0.43946188340807174,
          0.4405829596412556,
          0.44170403587443946,
          0.4433856502242152,
          0.44506726457399104,
          0.44730941704035876,
          0.4495515695067265,
          0.45067264573991034,
          0.4523542600896861,
          0.4551569506726457,
          0.45739910313901344,
          0.45908071748878926,
          0.460762331838565,
          0.4618834080717489,
          0.46300448430493274,
          0.4641255605381166,
          0.46580717488789236,
          0.4674887892376682,
          0.46860986547085204,
          0.4697309417040359,
          0.47085201793721976,
          0.4725336322869955,
          0.4742152466367713,
          0.4758968609865471,
          0.47757847533632286,
          0.4792600896860987,
          0.48094170403587444,
          0.4820627802690583,
          0.48318385650224216,
          0.4848654708520179,
          0.48654708520179374,
          0.4876681614349776,
          0.48878923766816146,
          0.4899103139013453,
          0.4910313901345291,
          0.4938340807174888,
          0.4966367713004484,
          0.4977578475336323,
          0.49887892376681614,
          0.5,
          0.5016816143497758,
          0.5044843049327354,
          0.5072869955156951,
          0.5100896860986547,
          0.5134529147982063,
          0.515695067264574,
          0.5173766816143498,
          0.5190582959641256,
          0.5201793721973094,
          0.5213004484304933,
          0.5224215246636771,
          0.523542600896861,
          0.5246636771300448,
          0.5263452914798207,
          0.5280269058295964,
          0.5291479820627802,
          0.5302690582959642,
          0.531390134529148,
          0.5325112107623319,
          0.5336322869955157,
          0.5347533632286996,
          0.5358744394618834,
          0.5375560538116592,
          0.5397982062780269,
          0.5414798206278026,
          0.5437219730941704,
          0.54652466367713,
          0.5482062780269058,
          0.5493273542600897,
          0.5515695067264574,
          0.554932735426009,
          0.5588565022421524,
          0.5622197309417041,
          0.5644618834080718,
          0.5667040358744395,
          0.5683856502242153,
          0.5695067264573991,
          0.570627802690583,
          0.5723094170403588,
          0.5745515695067265,
          0.5762331838565022,
          0.577354260089686,
          0.57847533632287,
          0.5795964125560538,
          0.5807174887892377,
          0.5818385650224215,
          0.5829596412556054,
          0.5840807174887892,
          0.5857623318385651,
          0.5880044843049327,
          0.5902466367713004,
          0.5930493273542601,
          0.5952914798206278,
          0.5964125560538116,
          0.5986547085201793,
          0.600896860986547,
          0.602017937219731,
          0.6031390134529148,
          0.6042600896860987,
          0.6053811659192825,
          0.6065022421524664,
          0.6076233183856502,
          0.6087443946188341,
          0.6104260089686099,
          0.6126681614349776,
          0.6143497757847534,
          0.6154708520179372,
          0.617152466367713,
          0.6188340807174888,
          0.6199551569506726,
          0.6210762331838565,
          0.6221973094170403,
          0.6233183856502242,
          0.624439461883408,
          0.625560538116592,
          0.6266816143497758,
          0.6278026905829597,
          0.6294843049327354,
          0.6317264573991032,
          0.6334080717488789,
          0.6345291479820628,
          0.6356502242152466,
          0.6367713004484304,
          0.6384529147982063,
          0.6401345291479821,
          0.6412556053811659,
          0.6429372197309418,
          0.6457399103139013,
          0.648542600896861,
          0.6502242152466368,
          0.6513452914798207,
          0.6524663677130045,
          0.6535874439461884,
          0.6547085201793722,
          0.6569506726457399,
          0.6591928251121076,
          0.6603139013452914,
          0.6614349775784754,
          0.6625560538116592,
          0.6636771300448431,
          0.6647982062780269,
          0.6659192825112108,
          0.6670403587443946,
          0.6681614349775785,
          0.6692825112107623,
          0.6704035874439462,
          0.67152466367713,
          0.672645739910314,
          0.6737668161434978,
          0.6748878923766816,
          0.6760089686098655,
          0.6771300448430493,
          0.6782511210762332,
          0.679932735426009,
          0.6816143497757847,
          0.6838565022421524,
          0.6860986547085202,
          0.6883408071748879,
          0.6917040358744395,
          0.695067264573991,
          0.6973094170403588,
          0.6984304932735426,
          0.7006726457399103,
          0.702914798206278,
          0.7040358744394619,
          0.7051569506726457,
          0.7062780269058296,
          0.7073991031390134,
          0.7085201793721974,
          0.7107623318385651,
          0.7135650224215246,
          0.7152466367713004,
          0.7163677130044843,
          0.7174887892376681,
          0.718609865470852,
          0.7197309417040358,
          0.7208520179372198,
          0.7219730941704036,
          0.7242152466367713,
          0.726457399103139,
          0.7275784753363229,
          0.7292600896860987,
          0.7309417040358744,
          0.7337443946188341,
          0.7365470852017937,
          0.7382286995515696,
          0.7399103139013453,
          0.7410313901345291,
          0.742152466367713,
          0.7438340807174888,
          0.7460762331838565,
          0.7477578475336323,
          0.7488789237668162,
          0.75,
          0.7511210762331838,
          0.7522421524663677,
          0.7533632286995515,
          0.7550448430493274,
          0.7567264573991032,
          0.757847533632287,
          0.7589686098654709,
          0.7600896860986547,
          0.7612107623318386,
          0.7623318385650224,
          0.7634529147982063,
          0.7645739910313901,
          0.765695067264574,
          0.7668161434977578,
          0.7679372197309418,
          0.7696188340807175,
          0.7713004484304933,
          0.7724215246636771,
          0.774103139013453,
          0.7757847533632287,
          0.7769058295964125,
          0.7780269058295964,
          0.7791479820627802,
          0.7802690582959642,
          0.781390134529148,
          0.7825112107623319,
          0.7836322869955157,
          0.7847533632286996,
          0.7858744394618834,
          0.7875560538116592,
          0.7892376681614349,
          0.7909192825112108,
          0.7926008968609866,
          0.7937219730941704,
          0.7948430493273543,
          0.7959641255605381,
          0.797085201793722,
          0.7982062780269058,
          0.7993273542600897,
          0.8004484304932735,
          0.8015695067264574,
          0.8026905829596412,
          0.8038116591928252,
          0.804932735426009,
          0.8060538116591929,
          0.8071748878923767,
          0.8082959641255605,
          0.8094170403587444,
          0.8105381165919282,
          0.8116591928251121,
          0.8127802690582959,
          0.8139013452914798,
          0.8155829596412556,
          0.8172645739910314,
          0.8183856502242153,
          0.8195067264573991,
          0.820627802690583,
          0.8217488789237668,
          0.8228699551569507,
          0.8239910313901345,
          0.8307174887892377,
          0.844170403587444,
          0.8587443946188341,
          0.8794843049327354,
          0.9013452914798207,
          0.9142376681614349,
          0.9237668161434978,
          0.9316143497757847,
          0.9366591928251121,
          0.9433856502242153,
          0.9495515695067265,
          0.9540358744394619,
          0.9607623318385651,
          0.9669282511210763,
          0.9714125560538116,
          0.9742152466367713,
          0.9775784753363229,
          0.9809417040358744,
          0.9826233183856502,
          0.9848654708520179,
          0.9865470852017937,
          0.9882286995515696,
          0.9904708520179372,
          0.9927130044843049,
          0.9949551569506726,
          0.9966367713004485,
          0.9977578475336323,
          0.9988789237668162,
          1.0
        ]
      },
      "Backlogs": {
        "valores": [
          1.0,
          5.0,
          6.0,
          10.0,
          13.0,
          21.0,
          24.0,
          26.0,
          27.0,
          28.0,
          30.0,
          34.0,
          36.0,
          39.0,
          40.0,
          42.0,
          44.0,
          45.0,
          50.0,
          54.0,
          55.0,
          56.0,
          61.0,
          64.0,
          67.0,
          69.0,
          70.0,
          74.0,
          76.0,
          77.0,
          82.0,
          83.0,
          85.0,
          88.0,
          89.0,
          92.0,
          93.0,
          95.0,
          96.0,
          102.0,
          103.0,
          105.0,
          108.0,
          110.0,
          117.0,
          120.0,
          122.0,
          127.0,
          128.0,
          130.0,
          132.0,
          133.0,
          134.0,
          135.0,
          136.0,
          137.0,
          138.0,
          139.0,
          140.0,
          142.0,
          143.0,
          144.0,
          145.0,
          146.0,
          147.0,
          148.0,
          150.0,
          151.0,
          154.0,
          155.0,
          156.0,
          158.0,
          164.0,
          165.0,
          167.0,
          173.0,
          174.0,
          175.0,
          179.0,
          181.0,
          182.0,
          188.0,
          191.0,
          195.0,
          197.0,
          198.0,
          199.0,
          200.0,
          202.0,
          205.0,
          207.0,
          209.0,
          211.0,
          213.0,
          214.0,
          215.0,
          216.0,
          217.0,
          223.0,
          224.0,
          225.0,
          229.0,
          230.0,
          232.0,
          234.0,
          236.0,
          237.0,
          239.0,
          240.0,
          241.0,
          242.0,
          243.0,
          244.0,
          246.0,
          247.0,
          249.0,
          252.0,
          253.0,
          255.0,
          256.0,
          259.0,
          260.0,
          261.0,
          262.0,
          263.0,
          268.0,
          271.0,
          273.0,
          274.0,
          275.0,
          276.0,
          278.0,
          279.0,
          280.0,
          283.0,
          287.0,
          289.0,
          292.0,
          293.0,
          299.0,
          301.0,
          304.0,
          305.0,
          308.0,
          309.0,
          313.0,
          314.0,
          317.0,
          319.0,
          320.0,
          321.0,
          322.0,
          323.0,
          324.0,
          326.0,
          327.0,
          329.0,
          332.0,
          333.0,
          336.0,
          338.0,
          341.0,
          343.0,
          345.0,
          348.0,
          351.0,
          354.0,
          355.0,
          359.0,
          361.0,
          365.0,
          366.0,
          367.0,
          369.0,
          370.0,
          371.0,
          374.0,
          377.0,
          381.0,
          382.0,
          384.0,
          385.0,
          387.0,
          388.0,
          389.0,
          390.0,
          392.0,
          393.0,
          394.0,
          396.0,
          399.0,
          403.0,
          407.0,
          408.0,
          411.0,
          412.0,
          413.0,
          414.0,
          415.0,
          416.0,
          417.0,
          418.0,
          422.0,
          426.0,
          427.0,
          429.0,
          431.0,
          434.0,
          436.0,
          438.0,
          441.0,
          442.0,
          449.0,
          450.0,
          451.0,
          452.0,
          455.0,
          457.0,
          460.0,
          461.0,
          462.0,
          463.0,
          464.0,
          466.0,
          468.0,
          470.0,
          473.0,
          474.0,
          477.0,
          480.0,
          482.0,
          485.0,
          487.0,
          489.0,
          490.0,
          491.0,
          492.0,
          493.0,
          495.0,
          496.0,
          498.0,
          499.0,
          501.0,
          502.0,
          503.0,
          506.0,
          507.0,
          511.0,
          513.0,
          514.0,
          517.0,
          518.0,
          520.0,
          522.0,
          526.0,
          528.0,
          529.0,
          535.0,
          536.0,
          539.0,
          540.0,
          542.0,
          543.0,
          545.0,
          549.0,
          551.0,
          554.0,
          556.0,
          561.0,
          562.0,
          563.0,
          567.0,
          572.0,
          577.0,
          579.0,
          580.0,
          582.0,
          584.0,
          586.0,
          587.0,
          589.0,
          592.0,
          596.0,
          597.0,
          598.0,
          599.0,
          602.0,
          605.0,
          606.0,
          607.0,
          618.0,
          623.0,
          625.0,
          626.0,
          630.0,
          636.0,
          637.0,
          640.0,
          643.0,
          646.0,
          655.0,
          656.0,
          657.0,
          659.0,
          663.0,
          664.0,
          665.0,
          666.0,
          667.0,
          670.0,
          672.0,
          674.0,
          675.0,
          676.0,
          678.0,
          682.0,
          683.0,
          686.0,
          687.0,
          690.0,
          691.0,
          693.0,
          694.0,
          695.0,
          696.0,
          697.0,
          698.0,
          701.0,
          702.0,
          705.0,
          707.0,
          712.0,
          714.0,
          715.0,
          717.0,
          718.0,
          721.0,
          723.0,
          726.0,
          727.0,
          729.0,
          732.0,
          733.0,
          738.0,
          739.0,
          740.0,
          741.0,
          742.0,
          747.0,
          749.0,
          750.0,
          761.0,
          763.0,
          765.0,
          767.0,
          771.0,
          772.0,
          773.0,
          776.0,
          777.0,
          781.0,
          782.0,
          784.0,
          787.0,
          796.0,
          797.0,
          800.0,
          801.0,
          802.0,
          803.0,
          804.0,
          808.0,
          809.0,
          818.0,
          821.0,
          823.0,
          824.0,
          826.0,
          828.0,
          833.0,
          836.0,
          838.0,
          839.0,
          845.0,
          852.0,
          859.0,
          861.0,
          863.0,
          868.0,
          869.0,
          875.0,
          877.0,
          878.0,
          879.0,
          883.0,
          884.0,
          889.0,
          891.0,
          899.0,
          905.0,
          907.0,
          908.0,
          916.0,
          917.0,
          920.0,
          924.0,
          929.0,
          932.0,
          936.0,
          939.0,
          945.0,
          946.0,
          949.0,
          963.0,
          964.0,
          967.0,
          980.0,
          985.0,
          988.0,
          989.0,
          991.0,
          993.0,
          995.0,
          996.0,
          999.0,
          1000.0,
          1100.0,
          1200.0,
          1300.0,
          1400.0,
          1500.0,
          1600.0,
          1700.0,
          1800.0,
          1900.0,
          2000.0,
          2100.0,
          2200.0,
          2300.0,
          2400.0,
          2500.0,
          2600.0,
          2700.0,
          2800.0,
          2900.0,
          3000.0,
          3100.0,
          3200.0,
          3300.0,
          3400.0,
          3500.0,
          3600.0,
          3700.0,
          4000.0,
          4100.0,
          4200.0,
          4300.0,
          4500.0,
          4600.0,
          4700.0,
          4800.0,
          4900.0,
          5000.0,
          5100.0,
          5200.0,
          5500.0,
          5900.0,
          6100.0,
          6200.0,
          6300.0,
          8300.0
        ],
        "percentiles": [
          0.0016816143497757848,
          0.0033632286995515697,
          0.004484304932735426,
          0.005605381165919282,
          0.006726457399103139,
          0.007847533632286996,
          0.008968609865470852,
          0.010650224215246636,
          0.01233183856502242,
          0.013452914798206279,
          0.014573991031390135,
          0.016816143497757848,
          0.01905829596412556,
          0.020739910313901346,
          0.02242152466367713,
          0.023542600896860985,
          0.02466367713004484,
          0.0257847533632287,
          0.026905829596412557,
          0.02858744394618834,
          0.030269058295964126,
          0.03195067264573991,
          0.034192825112107625,
          0.03587443946188341,
          0.03699551569506727,
          0.03811659192825112,
          0.0397982062780269,
          0.04147982062780269,
          0.043161434977578475,
          0.04484304932735426,
          0.04596412556053812,
          0.04708520179372197,
          0.04820627802690583,
          0.04932735426008968,
          0.05044843049327354,
          0.0515695067264574,
          0.053251121076233185,
          0.05493273542600897,
          0.05605381165919283,
          0.05773542600896861,
          0.05941704035874439,
          0.06053811659192825,
          0.062219730941704035,
          0.06390134529147982,
          0.06502242152466367,
          0.06614349775784753,
          0.06726457399103139,
          0.06838565022421525,
          0.07006726457399103,
          0.07174887892376682,
          0.07286995515695067,
          0.07399103139013453,
          0.07511210762331838,
          0.07679372197309417,
          0.07847533632286996,
          0.0795964125560538,
          0.08071748878923767,
          0.08239910313901345,
          0.08408071748878924,
          0.08520179372197309,
          0.08688340807174888,
          0.08856502242152467,
          0.09024663677130045,
          0.09192825112107623,
          0.0930493273542601,
          0.09417040358744394,
          0.09585201793721973,
          0.09753363228699552,
          0.09865470852017937,
          0.09977578475336323,
          0.10089686098654709,
          0.10201793721973094,
          0.1031390134529148,
          0.10426008968609865,
          0.10538116591928251,
          0.1070627802690583,
          0.10874439461883408,
          0.10986547085201794,
          0.11154708520179372,
          0.11434977578475336,
          0.11659192825112108,
          0.11771300448430494,
          0.11995515695067265,
          0.12219730941704036,
          0.12331838565022421,
          0.12443946188340807,
          0.12556053811659193,
          0.1266816143497758,
          0.12780269058295965,
          0.1289237668161435,
          0.13004484304932734,
          0.13172645739910313,
          0.13340807174887892,
          0.13452914798206278,
          0.13565022421524664,
          0.13733183856502243,
          0.13901345291479822,
          0.14013452914798205,
          0.1412556053811659,
          0.14237668161434977,
          0.14405829596412556,
          0.14573991031390135,
          0.14742152466367714,
          0.1491031390134529,
          0.15022421524663676,
          0.15134529147982062,
          0.1530269058295964,
          0.1547085201793722,
          0.15582959641255606,
          0.15751121076233185,
          0.15975336322869954,
          0.16143497757847533,
          0.1625560538116592,
          0.16367713004484305,
          0.1647982062780269,
          0.16591928251121077,
          0.16704035874439463,
          0.1681614349775785,
          0.16928251121076232,
          0.1709641255605381,
          0.1726457399103139,
          0.17376681614349776,
          0.17488789237668162,
          0.17600896860986548,
          0.17713004484304934,
          0.17825112107623317,
          0.17937219730941703,
          0.18105381165919282,
          0.1827354260089686,
          0.18385650224215247,
          0.1860986547085202,
          0.18834080717488788,
          0.19002242152466367,
          0.1922645739910314,
          0.19394618834080718,
          0.19562780269058297,
          0.19730941704035873,
          0.1984304932735426,
          0.19955156950672645,
          0.2006726457399103,
          0.20179372197309417,
          0.20291479820627803,
          0.2040358744394619,
          0.20515695067264575,
          0.2062780269058296,
          0.20795964125560537,
          0.20964125560538116,
          0.21132286995515695,
          0.21356502242152467,
          0.2158071748878924,
          0.21748878923766815,
          0.21917040358744394,
          0.22085201793721973,
          0.2219730941704036,
          0.22309417040358745,
          0.22477578475336324,
          0.226457399103139,
          0.2281390134529148,
          0.22982062780269058,
          0.23094170403587444,
          0.2320627802690583,
          0.23318385650224216,
          0.23486547085201795,
          0.2365470852017937,
          0.23766816143497757,
          0.23878923766816143,
          0.2399103139013453,
          0.24103139013452915,
          0.242152466367713,
          0.24327354260089687,
          0.24439461883408073,
          0.24551569506726456,
          0.24663677130044842,
          0.24775784753363228,
          0.24887892376681614,
          0.25,
          0.25112107623318386,
          0.2522421524663677,
          0.2539237668161435,
          0.2561659192825112,
          0.257847533632287,
          0.2595291479820628,
          0.26121076233183854,
          0.26289237668161436,
          0.265695067264574,
          0.2679372197309417,
          0.26905829596412556,
          0.2713004484304933,
          0.273542600896861,
          0.27466367713004486,
          0.2769058295964126,
          0.27914798206278024,
          0.2802690582959641,
          0.28139013452914796,
          0.28419282511210764,
          0.2875560538116592,
          0.289237668161435,
          0.29035874439461884,
          0.2914798206278027,
          0.29260089686098656,
          0.2937219730941704,
          0.2954035874439462,
          0.297085201793722,
          0.2982062780269058,
          0.29932735426008966,
          0.3004484304932735,
          0.3015695067264574,
          0.30269058295964124,
          0.3038116591928251,
          0.30493273542600896,
          0.3060538116591928,
          0.3071748878923767,
          0.30885650224215244,
          0.31053811659192826,
          0.3116591928251121,
          0.3133408071748879,
          0.3150224215246637,
          0.31614349775784756,
          0.3172645739910314,
          0.3189461883408072,
          0.32062780269058294,
          0.3217488789237668,
          0.32286995515695066,
          0.3239910313901345,
          0.3251121076233184,
          0.32623318385650224,
          0.3273542600896861,
          0.32847533632286996,
          0.3295964125560538,
          0.3307174887892377,
          0.33183856502242154,
          0.3329596412556054,
          0.33464125560538116,
          0.336322869955157,
          0.3374439461883408,
          0.3391255605381166,
          0.34080717488789236,
          0.3419282511210762,
          0.3430493273542601,
          0.34417040358744394,
          0.3452914798206278,
          0.34641255605381166,
          0.3480941704035874,
          0.34977578475336324,
          0.351457399103139,
          0.3531390134529148,
          0.3542600896860987,
          0.35594170403587444,
          0.3576233183856502,
          0.35874439461883406,
          0.3598654708520179,
          0.3609865470852018,
          0.3626681614349776,
          0.36434977578475336,
          0.3654708520179372,
          0.3665919282511211,
          0.36827354260089684,
          0.36995515695067266,
          0.3710762331838565,
          0.3721973094170404,
          0.37387892376681614,
          0.3755605381165919,
          0.3772421524663677,
          0.37948430493273544,
          0.3811659192825112,
          0.38228699551569506,
          0.3834080717488789,
          0.3845291479820628,
          0.38565022421524664,
          0.3867713004484305,
          0.38789237668161436,
          0.3890134529147982,
          0.3901345291479821,
          0.39125560538116594,
          0.3923766816143498,
          0.39349775784753366,
          0.39461883408071746,
          0.3968609865470852,
          0.3991031390134529,
          0.4007847533632287,
          0.4024663677130045,
          0.40358744394618834,
          0.4052690582959641,
          0.4075112107623318,
          0.40919282511210764,
          0.4103139013452915,
          0.41199551569506726,
          0.413677130044843,
          0.4147982062780269,
          0.41591928251121074,
          0.4170403587443946,
          0.41816143497757846,
          0.4198430493273543,
          0.42152466367713004,
          0.4226457399103139,
          0.42376681614349776,
          0.4254484304932735,
          0.42713004484304934,
          0.4282511210762332,
          0.42937219730941706,
          0.4304932735426009,
          0.4316143497757848,
          0.4327354260089686,
          0.43385650224215244,
          0.4349775784753363,
          0.4366591928251121,
          0.4383408071748879,
          0.43946188340807174,
          0.4405829596412556,
          0.44170403587443946,
          0.4428251121076233,
          0.4439461883408072,
          0.44506726457399104,
          0.4461883408071749,
          0.44730941704035876,
          0.4489910313901345,
          0.45067264573991034,
          0.4517937219730942,
          0.452914798206278,
          0.4545964125560538,
          0.4562780269058296,
          0.45739910313901344,
          0.4585201793721973,
          0.45964125560538116,
          0.461322869955157,
          0.46300448430493274,
          0.4641255605381166,
          0.46524663677130046,
          0.4663677130044843,
          0.4674887892376682,
          0.46917040358744394,
          0.47085201793721976,
          0.47197309417040356,
          0.4730941704035874,
          0.4742152466367713,
          0.47533632286995514,
          0.47701793721973096,
          0.4786995515695067,
          0.4798206278026906,
          0.48094170403587444,
          0.4820627802690583,
          0.48374439461883406,
          0.4854260089686099,
          0.48710762331838564,
          0.48878923766816146,
          0.4899103139013453,
          0.4915919282511211,
          0.49327354260089684,
          0.49495515695067266,
          0.4966367713004484,
          0.49831838565022424,
          0.5,
          0.5011210762331838,
          0.5022421524663677,
          0.5033632286995515,
          0.5056053811659192,
          0.5084080717488789,
          0.5106502242152466,
          0.5128923766816144,
          0.5145739910313901,
          0.515695067264574,
          0.5168161434977578,
          0.5179372197309418,
          0.5190582959641256,
          0.5207399103139013,
          0.522982062780269,
          0.5246636771300448,
          0.5257847533632287,
          0.5269058295964125,
          0.5280269058295964,
          0.5291479820627802,
          0.5302690582959642,
          0.5319506726457399,
          0.5336322869955157,
          0.5347533632286996,
          0.5358744394618834,
          0.5369955156950673,
          0.5381165919282511,
          0.5392376681614349,
          0.5403587443946188,
          0.5414798206278026,
          0.5426008968609866,
          0.5437219730941704,
          0.5448430493273543,
          0.5459641255605381,
          0.547085201793722,
          0.5482062780269058,
          0.5493273542600897,
          0.5504484304932735,
          0.5515695067264574,
          0.5526905829596412,
          0.5538116591928252,
          0.554932735426009,
          0.5566143497757847,
          0.5582959641255605,
          0.5594170403587444,
          0.5605381165919282,
          0.5622197309417041,
          0.5639013452914798,
          0.5650224215246636,
          0.5661434977578476,
          0.5672645739910314,
          0.5683856502242153,
          0.5695067264573991,
          0.570627802690583,
          0.5717488789237668,
          0.5728699551569507,
          0.5739910313901345,
          0.5751121076233184,
          0.5767937219730942,
          0.57847533632287,
          0.5795964125560538,
          0.5807174887892377,
          0.5818385650224215,
          0.5829596412556054,
          0.5846412556053812,
          0.5863228699551569,
          0.5874439461883408,
          0.5885650224215246,
          0.5896860986547086,
          0.5908071748878924,
          0.5924887892376681,
          0.594170403587444,
          0.5952914798206278,
          0.5964125560538116,
          0.6070627802690582,
          0.6294843049327354,
          0.6541479820627802,
          0.679932735426009,
          0.6995515695067265,
          0.7230941704035875,
          0.750560538116592,
          0.772982062780269,
          0.7926008968609866,
          0.8082959641255605,
          0.8223094170403588,
          0.8352017937219731,
          0.8480941704035875,
          0.8609865470852018,
          0.874439461883408,
          0.8873318385650224,
          0.898542600896861,
          0.9075112107623319,
          0.9164798206278026,
          0.9260089686098655,
          0.9332959641255605,
          0.9377802690582959,
          0.9422645739910314,
          0.9473094170403588,
          0.952354260089686,
          0.9557174887892377,
          0.9585201793721974,
          0.9613228699551569,
          0.9641255605381166,
          0.9674887892376681,
          0.9697309417040358,
          0.9708520179372198,
          0.9725336322869955,
          0.9747757847533632,
          0.976457399103139,
          0.9803811659192825,
          0.9848654708520179,
          0.9882286995515696,
          0.9910313901345291,
          0.9927130044843049,
          0.9943946188340808,
          0.9955156950672646,
          0.9966367713004485,
          0.9977578475336323,
          0.9988789237668162,
          1.0
        ]
      }
    },
    "poblacion_referencia_n": 892,
    "percentil": "Rango medio/N en entrenamiento; interpolación lineal entre valores distintos, 0 bajo mínimo y 1 sobre máximo.",
    "momento_definicion": "Referencia y terciles ajustados solo en entrenamiento; cada fold repite el ajuste sin su validación.",
    "clases_ordenadas": [
      "bajo",
      "medio",
      "alto"
    ],
    "regla": "bajo: índice <= corte1; medio: corte1 < índice <= corte2; alto: índice > corte2",
    "cortes": [
      0.3622944693572496,
      0.6266816143497758
    ]
  },
  "alternativa_solo_plays": {
    "cortes": [
      1900.0,
      5300.0
    ],
    "fraccion_etiquetas_coincidentes": 0.6113105924596051
  },
  "n_cohorte": 1114,
  "n_entrenamiento": 892,
  "n_prueba": 222,
  "particion": {
    "test_size": 0.2,
    "estratificada": false,
    "sin_titulos_compartidos": true,
    "regla": "GroupShuffleSplit, una partición independiente de los conteos/etiquetas; aproximadamente 80/20 por grupos.",
    "intentos": 1
  },
  "validacion": {
    "pliegues": 10,
    "estratificada": true,
    "agrupacion": "grupo_titulo",
    "metodo": "StratifiedGroupKFold",
    "seleccion": "Mayor F1 macro media en CV; referencia del target y preprocesador ajustados por fold.",
    "etiquetas_para_organizar_estratos": "Referencia externa de entrenamiento; no se usa para fit/score de los folds."
  },
  "distribuciones": {
    "catalogo": {
      "medio": 377,
      "alto": 372,
      "bajo": 365
    },
    "entrenamiento": {
      "bajo": 298,
      "alto": 297,
      "medio": 297
    },
    "prueba": {
      "medio": 80,
      "alto": 75,
      "bajo": 67
    }
  },
  "mejores_parametros": {
    "pipeline__clasificar__max_depth": null,
    "pipeline__clasificar__min_samples_leaf": 5
  },
  "metricas": {
    "exactitud": 0.5675675675675675,
    "f1_macro": 0.5577027296634777,
    "balanced_accuracy": 0.5753192371475954,
    "f1_macro_referencia": 0.15455594002306805,
    "diferencia_f1_referencia": 0.4031467896404096,
    "f1_macro_cv": 0.5566561802699771,
    "matriz_confusion": [
      [
        43,
        14,
        10
      ],
      [
        32,
        27,
        21
      ],
      [
        9,
        10,
        56
      ]
    ],
    "reporte_clases": {
      "bajo": {
        "precision": 0.5119047619047619,
        "recall": 0.6417910447761194,
        "f1-score": 0.5695364238410596,
        "support": 67.0
      },
      "medio": {
        "precision": 0.5294117647058824,
        "recall": 0.3375,
        "f1-score": 0.4122137404580153,
        "support": 80.0
      },
      "alto": {
        "precision": 0.6436781609195402,
        "recall": 0.7466666666666667,
        "f1-score": 0.691358024691358,
        "support": 75.0
      },
      "accuracy": 0.5675675675675675,
      "macro avg": {
        "precision": 0.5616648958433949,
        "recall": 0.5753192371475954,
        "f1-score": 0.5577027296634777,
        "support": 222.0
      },
      "weighted avg": {
        "precision": 0.5627316319506989,
        "recall": 0.5675675675675675,
        "f1-score": 0.5539995111974958,
        "support": 222.0
      }
    }
  },
  "comparacion_modelos": [
    {
      "modelo": "DummyClassifier",
      "f1_macro_cv": 0.16776371135838186,
      "desviacion_cv": 0.0031079390068919897,
      "exactitud_prueba": 0.30180180180180183,
      "f1_macro_prueba": 0.15455594002306805,
      "balanced_accuracy_prueba": 0.3333333333333333,
      "mejores_parametros": "{}"
    },
    {
      "modelo": "CategoricalNB",
      "f1_macro_cv": 0.5490076772558734,
      "desviacion_cv": 0.06247316133182854,
      "exactitud_prueba": 0.509009009009009,
      "f1_macro_prueba": 0.49246153246608254,
      "balanced_accuracy_prueba": 0.5192330016583748,
      "mejores_parametros": "{\"pipeline__clasificar__alpha\": 5.0}"
    },
    {
      "modelo": "DecisionTreeClassifier",
      "f1_macro_cv": 0.5053348598452977,
      "desviacion_cv": 0.04576945678704888,
      "exactitud_prueba": 0.5315315315315315,
      "f1_macro_prueba": 0.5119270486584638,
      "balanced_accuracy_prueba": 0.5433250414593699,
      "mejores_parametros": "{\"pipeline__clasificar__max_depth\": 8, \"pipeline__clasificar__min_samples_leaf\": 10}"
    },
    {
      "modelo": "RandomForestClassifier",
      "f1_macro_cv": 0.5566561802699771,
      "desviacion_cv": 0.045090449320740876,
      "exactitud_prueba": 0.5675675675675675,
      "f1_macro_prueba": 0.5577027296634777,
      "balanced_accuracy_prueba": 0.5753192371475954,
      "mejores_parametros": "{\"pipeline__clasificar__max_depth\": null, \"pipeline__clasificar__min_samples_leaf\": 5}"
    }
  ],
  "evaluacion_referencia": "Supera al modelo de referencia en esta partición; no se ha probado significancia estadística de la diferencia.",
  "preprocesamiento": {
    "generos": "Multi-hot: hasta 15 con frecuencia >=20 en cada entrenamiento; resto/nuevos a Otro.",
    "estudio": "Miembros de Team con frecuencia >=10; Otro solo si no hay miembro frecuente; no se acredita rol desarrollador.",
    "notas": "Mediana ajustada en entrenamiento, sin indicadores de ausencia; scaler solo de notas, o bins para CategoricalNB.",
    "decada": "Ausencia -1 y one-hot; categorías nuevas sin indicadores activos."
  },
  "sha256_dataset_depurado": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "probabilidades_calibradas": false,
  "diagnostico_ausencia": {
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
  },
  "formato_artefacto": "Pipeline serializado por valor con cloudpickle; compatible con joblib.load sin src en PYTHONPATH.",
  "cloudpickle": "3.1.2"
}
````

## modelo.md

Ruta: `DocumentoFinal/evidencias/modelo.md` · Bytes: 9206 · SHA-256: `1c384f25685efe5bd987fe7249452b892edf120a035f1fbaffb06ee74a5bb96d`

````text
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

Fecha: 2026-11-09T08:35:00-06:00; sklearn 1.9.1; Python 3.15.2. Las métricas previas de objetivo global están archivadas y no son directamente comparables con las nuevas.

## Que debo verificar manualmente

- Pesos y redundancia del índice, antigüedad y representatividad de Backloggd.
- Procedencia de notas y sesgo de cobertura; la mediana puede conservar señales indirectas de ausencia.
- Identidad de juegos homónimos y roles de Team; los tres conflictos históricos siguen excluidos.
- Vecinos como similitud de atributos declarados, no recomendaciones de éxito ni causalidad.
- Probabilidades no calibradas y límites de la clase media.

````

## rubrica_proyecto.pdf

Ruta: `DocumentoFinal/evidencias/rubrica_proyecto.pdf` · Bytes: 81737 · SHA-256: `dd62ef24a2822d83205eb0352095519af4d94900e146df55d207b23b0c892dbc`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## trazabilidad_historica.md

Ruta: `DocumentoFinal/evidencias/trazabilidad_historica.md` · Bytes: 1744 · SHA-256: `59ab6b572a61f5b3b2eba4dbde7a599a47e9f02cbc5c239e6daf1094fc2f2a9a`

````text
# Trazabilidad histórica

El maestro designado sigue siendo games_curated.csv y no se modifica. El antecedente de data/historical permite reproducir sus decisiones heredadas, no aprobarlas como correctas.

Se reconstruyen 1512 → 1117 registros, con 395 descartes documentados individualmente en deduplicacion_historica.csv. Estado de comparación de las 42 columnas: **verificado**; diferencias: [].

Hay 13 grupos con alguna diferencia, pero solo 3 con conflicto analítico. Los IDs conservados por la regla histórica y pendientes de resolución son [117, 140, 296]. Se preservan en el dataset con indicador y se excluyen del análisis principal y del entrenamiento hasta revisión, sin elegir el máximo ni promediar versiones desconocidas.

conflictos_historicos.csv identifica campos e IDs; variantes_historicas.csv conserva todas las alternativas de esos grupos. maestro_reconstruido_solo_auditoria.csv permite comparar sin escribir sobre raw.

La procedencia crítica se reconstruye a partir de Origen_calificacion: 218 notas propias se dejan sin critic_score_final. En 214 estimaciones con Rating, el ajuste es 8.583327 × Rating + 50.958397; residuo máximo tras redondear: 0.0. Esta relación corrobora dependencia sintética; no demuestra por sí sola el algoritmo histórico exacto ni verifica las notas marcadas Metacritic.

Los conteos se obtienen con un lector CSV: wc -l no cuenta registros cuando Reviews o Summary contienen saltos de línea.

## Que debo verificar manualmente

- Plataformas, versiones y fecha de captura de las tres discrepancias numéricas.
- Procedencia de las notas críticas y decisiones heredadas de la deduplicación.
- No interpretar una reconstrucción exacta como aprobación del criterio first.

````

## weka_J48.txt

Ruta: `DocumentoFinal/evidencias/weka_J48.txt` · Bytes: 17362 · SHA-256: `88ceace97d84c7c67628688f9876a4d3de22c07935e6111dd954f3c401a88c8c`

````text
=== Run information ===

Scheme:       weka.classifiers.trees.J48 -C 0.25 -M 2
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

J48 pruned tree
------------------

generos__Fighting <= 0
|   generos__Otro <= 0
|   |   notas__Metacritic Rating <= 0.1679
|   |   |   notas__Rating <= -2.152384
|   |   |   |   estudio__Capcom <= 0: bajo (18.0/1.0)
|   |   |   |   estudio__Capcom > 0: alto (3.0/1.0)
|   |   |   notas__Rating > -2.152384
|   |   |   |   generos__Adventure <= 0
|   |   |   |   |   estudio__Atlus <= 0
|   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   generos__Brawler <= 0
|   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   estudio__Nintendo <= 0
|   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 <= 0: bajo (61.0/19.0)
|   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 > 0
|   |   |   |   |   |   |   |   |   |   |   generos__Shooter <= 0: medio (11.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Shooter > 0: bajo (5.0/1.0)
|   |   |   |   |   |   |   |   |   estudio__Nintendo > 0: medio (20.0/9.0)
|   |   |   |   |   |   |   |   generos__Puzzle > 0
|   |   |   |   |   |   |   |   |   generos__Indie <= 0: bajo (9.0)
|   |   |   |   |   |   |   |   |   generos__Indie > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   generos__Brawler > 0
|   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   generos__Arcade <= 0
|   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -1.47338: medio (2.0)
|   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -1.47338: alto (3.0)
|   |   |   |   |   |   |   |   |   generos__Arcade > 0: bajo (2.0/1.0)
|   |   |   |   |   |   |   |   generos__RPG > 0: bajo (4.0/1.0)
|   |   |   |   |   |   estudio__Square Enix > 0: medio (8.0/2.0)
|   |   |   |   |   estudio__Atlus > 0
|   |   |   |   |   |   decada__decada_1990.0 <= 0: alto (5.0/1.0)
|   |   |   |   |   |   decada__decada_1990.0 > 0: bajo (2.0/1.0)
|   |   |   |   generos__Adventure > 0
|   |   |   |   |   decada__decada_2010.0 <= 0
|   |   |   |   |   |   estudio__Game Freak <= 0
|   |   |   |   |   |   |   estudio__Konami <= 0
|   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.379193
|   |   |   |   |   |   |   |   |   estudio__Sonic Team <= 0: bajo (53.0/22.0)
|   |   |   |   |   |   |   |   |   estudio__Sonic Team > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.379193
|   |   |   |   |   |   |   |   |   estudio__Square <= 0
|   |   |   |   |   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   |   |   |   |   generos__Turn Based Strategy <= 0
|   |   |   |   |   |   |   |   |   |   |   |   generos__Brawler <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Nintendo <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Annapurna Interactive <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Capcom <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.24242
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_2000.0 <= 0: alto (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_2000.0 > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.106347: bajo (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.106347: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.24242
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.031127: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.031127
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel <= 0: bajo (13.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel > 0: medio (8.0/3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: bajo (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   decada__decada_1990.0 > 0: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Capcom > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= 0.079656: bajo (13.0/5.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > 0.079656: alto (5.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Annapurna Interactive > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Nintendo > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= 0.079656: medio (9.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > 0.079656: alto (5.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   generos__Brawler > 0: alto (8.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Turn Based Strategy > 0: alto (5.0/1.0)
|   |   |   |   |   |   |   |   |   |   estudio__Square Enix > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   estudio__Square > 0: alto (3.0)
|   |   |   |   |   |   |   estudio__Konami > 0
|   |   |   |   |   |   |   |   generos__Platform <= 0: bajo (3.0)
|   |   |   |   |   |   |   |   generos__Platform > 0: medio (4.0)
|   |   |   |   |   |   estudio__Game Freak > 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (7.0/2.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (2.0)
|   |   |   |   |   decada__decada_2010.0 > 0
|   |   |   |   |   |   estudio__Sony Interactive Entertainment <= 0
|   |   |   |   |   |   |   notas__Metacritic Rating <= -1.8837
|   |   |   |   |   |   |   |   generos__Simulator <= 0: medio (6.0)
|   |   |   |   |   |   |   |   generos__Simulator > 0
|   |   |   |   |   |   |   |   |   notas__Rating <= -0.85036: bajo (2.0)
|   |   |   |   |   |   |   |   |   notas__Rating > -0.85036: medio (3.0)
|   |   |   |   |   |   |   notas__Metacritic Rating > -1.8837
|   |   |   |   |   |   |   |   generos__Turn Based Strategy <= 0
|   |   |   |   |   |   |   |   |   estudio__Sony Computer Entertainment <= 0
|   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.85036
|   |   |   |   |   |   |   |   |   |   |   estudio__Ubisoft Entertainment <= 0: medio (24.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Ubisoft Entertainment > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   notas__Rating > -0.85036
|   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel <= 0
|   |   |   |   |   |   |   |   |   |   |   |   estudio__Otro <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Activision <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0: alto (32.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Platform > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Strategy <= 0: medio (8.0/2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Strategy > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   estudio__Activision > 0: alto (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   estudio__Otro > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0: medio (19.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__RPG > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= -0.926287: medio (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > -0.926287: alto (10.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   generos__Visual Novel > 0
|   |   |   |   |   |   |   |   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__Indie <= 0: bajo (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   generos__Indie > 0: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   generos__RPG > 0: bajo (2.0)
|   |   |   |   |   |   |   |   |   estudio__Sony Computer Entertainment > 0: alto (4.0/1.0)
|   |   |   |   |   |   |   |   generos__Turn Based Strategy > 0
|   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.031127: alto (3.0/1.0)
|   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.031127: medio (3.0)
|   |   |   |   |   |   estudio__Sony Interactive Entertainment > 0: alto (7.0/1.0)
|   |   notas__Metacritic Rating > 0.1679
|   |   |   generos__Racing <= 0
|   |   |   |   generos__Strategy <= 0
|   |   |   |   |   decada__decada_1990.0 <= 0
|   |   |   |   |   |   estudio__Square Enix <= 0
|   |   |   |   |   |   |   notas__Rating <= 0.079656
|   |   |   |   |   |   |   |   estudio__Activision <= 0
|   |   |   |   |   |   |   |   |   decada__decada_2000.0 <= 0
|   |   |   |   |   |   |   |   |   |   generos__Arcade <= 0
|   |   |   |   |   |   |   |   |   |   |   estudio__Electronic Arts <= 0: alto (36.0/10.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Electronic Arts > 0: medio (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   generos__Arcade > 0: bajo (2.0/1.0)
|   |   |   |   |   |   |   |   |   decada__decada_2000.0 > 0
|   |   |   |   |   |   |   |   |   |   generos__Puzzle <= 0
|   |   |   |   |   |   |   |   |   |   |   estudio__Microsoft Game Studios <= 0
|   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.106347
|   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating <= -0.292351
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Adventure <= 0: alto (2.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating <= 0.441447: bajo (2.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   notas__Metacritic Rating > 0.441447: medio (8.0/3.0)
|   |   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.292351: medio (7.0)
|   |   |   |   |   |   |   |   |   |   |   |   notas__Rating > -0.106347: alto (4.0/1.0)
|   |   |   |   |   |   |   |   |   |   |   estudio__Microsoft Game Studios > 0: medio (3.0)
|   |   |   |   |   |   |   |   |   |   generos__Puzzle > 0: bajo (2.0)
|   |   |   |   |   |   |   |   estudio__Activision > 0: medio (3.0/1.0)
|   |   |   |   |   |   |   notas__Rating > 0.079656: alto (155.0/37.0)
|   |   |   |   |   |   estudio__Square Enix > 0
|   |   |   |   |   |   |   decada__decada_2020.0 <= 0
|   |   |   |   |   |   |   |   notas__Rating <= 1.195676: alto (5.0)
|   |   |   |   |   |   |   |   notas__Rating > 1.195676: medio (3.0)
|   |   |   |   |   |   |   decada__decada_2020.0 > 0: medio (6.0/1.0)
|   |   |   |   |   decada__decada_1990.0 > 0
|   |   |   |   |   |   generos__Adventure <= 0: medio (3.0)
|   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (5.0/1.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (6.0)
|   |   |   |   generos__Strategy > 0
|   |   |   |   |   decada__decada_2020.0 <= 0
|   |   |   |   |   |   generos__Adventure <= 0
|   |   |   |   |   |   |   notas__Rating <= 0.451663: medio (7.0)
|   |   |   |   |   |   |   notas__Rating > 0.451663: alto (3.0/1.0)
|   |   |   |   |   |   generos__Adventure > 0
|   |   |   |   |   |   |   notas__Rating <= -0.478354: medio (3.0/1.0)
|   |   |   |   |   |   |   notas__Rating > -0.478354: alto (4.0/1.0)
|   |   |   |   |   decada__decada_2020.0 > 0: bajo (3.0/1.0)
|   |   |   generos__Racing > 0
|   |   |   |   generos__Adventure <= 0
|   |   |   |   |   notas__Rating <= -0.478354: bajo (2.0)
|   |   |   |   |   notas__Rating > -0.478354: medio (9.0/3.0)
|   |   |   |   generos__Adventure > 0: alto (2.0)
|   generos__Otro > 0
|   |   estudio__Capcom <= 0
|   |   |   decada__decada_1990.0 <= 0
|   |   |   |   generos__Visual Novel <= 0
|   |   |   |   |   generos__RPG <= 0
|   |   |   |   |   |   estudio__Nintendo <= 0: bajo (52.0/13.0)
|   |   |   |   |   |   estudio__Nintendo > 0
|   |   |   |   |   |   |   decada__decada_2010.0 <= 0
|   |   |   |   |   |   |   |   notas__Rating <= -0.106347: bajo (5.0)
|   |   |   |   |   |   |   |   notas__Rating > -0.106347: medio (4.0/1.0)
|   |   |   |   |   |   |   decada__decada_2010.0 > 0: medio (2.0)
|   |   |   |   |   generos__RPG > 0
|   |   |   |   |   |   decada__decada_2010.0 <= 0: medio (5.0/1.0)
|   |   |   |   |   |   decada__decada_2010.0 > 0
|   |   |   |   |   |   |   generos__Puzzle <= 0: bajo (2.0)
|   |   |   |   |   |   |   generos__Puzzle > 0: alto (2.0)
|   |   |   |   generos__Visual Novel > 0
|   |   |   |   |   decada__decada_2010.0 <= 0: medio (4.0)
|   |   |   |   |   decada__decada_2010.0 > 0: alto (2.0/1.0)
|   |   |   decada__decada_1990.0 > 0: bajo (4.0)
|   |   estudio__Capcom > 0: medio (3.0/1.0)
generos__Fighting > 0
|   estudio__Ubisoft Entertainment <= 0
|   |   estudio__WB Games <= 0
|   |   |   estudio__Nintendo <= 0: bajo (43.0/9.0)
|   |   |   estudio__Nintendo > 0: medio (4.0/2.0)
|   |   estudio__WB Games > 0: medio (5.0/1.0)
|   estudio__Ubisoft Entertainment > 0: medio (2.0)

Number of Leaves  : 	101

Size of the tree : 	201


Time taken to build model: 0.17 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         455               51.009  %
Incorrectly Classified Instances       437               48.991  %
Kappa statistic                          0.2651
Mean absolute error                      0.3572
Root mean squared error                  0.4979
Relative absolute error                 80.3698 %
Root relative squared error            105.6156 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.650    0.224    0.592      0.650    0.620      0.417    0.744     0.549     alto
                 0.537    0.224    0.546      0.537    0.541      0.314    0.677     0.492     bajo
                 0.343    0.287    0.374      0.343    0.358      0.057    0.527     0.360     medio
Weighted Avg.    0.510    0.245    0.504      0.510    0.506      0.263    0.649     0.467     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 193  29  75 |   a = alto
  42 160  96 |   b = bajo
  91 104 102 |   c = medio

````

## weka_NaiveBayes.txt

Ruta: `DocumentoFinal/evidencias/weka_NaiveBayes.txt` · Bytes: 20846 · SHA-256: `5aac3e1f7f662eb504b71c7f77d1e31f2121a15ba7771c97b630a65bfd3027c6`

````text
=== Run information ===

Scheme:       weka.classifiers.bayes.NaiveBayes 
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

Naive Bayes Classifier

                                                      Class
Attribute                                              alto    bajo   medio
                                                     (0.33)  (0.33)  (0.33)
============================================================================
generos__Adventure
  mean                                                0.8148  0.4866   0.633
  std. dev.                                           0.3884  0.4998   0.482
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__RPG
  mean                                                0.3906  0.2282  0.3468
  std. dev.                                           0.4879  0.4197   0.476
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Shooter
  mean                                                0.2896  0.1846  0.1886
  std. dev.                                           0.4536  0.3879  0.3912
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Platform
  mean                                                0.2458  0.1946  0.2189
  std. dev.                                           0.4306  0.3959  0.4135
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Indie
  mean                                                 0.165  0.1946  0.1852
  std. dev.                                           0.3712  0.3959  0.3884
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Puzzle
  mean                                                0.1246  0.1275  0.1077
  std. dev.                                           0.3302  0.3336  0.3101
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Strategy
  mean                                                0.0471  0.1443  0.1044
  std. dev.                                           0.2119  0.3514  0.3057
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Brawler
  mean                                                0.1212  0.0839  0.0842
  std. dev.                                           0.3264  0.2772  0.2777
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Simulator
  mean                                                0.0572  0.1074  0.0774
  std. dev.                                           0.2323  0.3096  0.2673
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Fighting
  mean                                                0.0067  0.1208  0.0539
  std. dev.                                           0.1667  0.3259  0.2258
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Turn Based Strategy
  mean                                                 0.064  0.0336  0.0808
  std. dev.                                           0.2447  0.1801  0.2725
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Arcade
  mean                                                0.0236  0.0973  0.0505
  std. dev.                                           0.1667  0.2964   0.219
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Visual Novel
  mean                                                0.0303  0.0403  0.0572
  std. dev.                                           0.1714  0.1966  0.2323
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Racing
  mean                                                0.0101  0.0436  0.0505
  std. dev.                                           0.1667  0.2043   0.219
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Tactical
  mean                                                0.0202  0.0403  0.0438
  std. dev.                                           0.1667  0.1966  0.2046
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Otro
  mean                                                0.0202  0.1812  0.0875
  std. dev.                                           0.1667  0.3852  0.2826
  weight sum                                             297     298     297
  precision                                                1       1       1

generos__Sin dato
  mean                                                     0  0.0034  0.0034
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Nintendo
  mean                                                0.1785  0.0973  0.2121
  std. dev.                                           0.3829  0.2964  0.4088
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Capcom
  mean                                                0.0707  0.0638   0.037
  std. dev.                                           0.2563  0.2443  0.1889
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Square Enix
  mean                                                0.0438  0.0235  0.0774
  std. dev.                                           0.2046  0.1667  0.2673
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sega
  mean                                                0.0303   0.057  0.0337
  std. dev.                                           0.1714  0.2319  0.1804
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Electronic Arts
  mean                                                0.0337  0.0436   0.037
  std. dev.                                           0.1804  0.2043  0.1889
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Konami
  mean                                                0.0269  0.0302  0.0303
  std. dev.                                           0.1667  0.1711  0.1714
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Bandai Namco Entertainment
  mean                                                0.0337  0.0336  0.0168
  std. dev.                                           0.1804  0.1801  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Activision
  mean                                                0.0168  0.0369  0.0236
  std. dev.                                           0.1667  0.1885  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Ubisoft Entertainment
  mean                                                0.0404  0.0168  0.0202
  std. dev.                                           0.1969  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Atlus
  mean                                                 0.037  0.0134  0.0168
  std. dev.                                           0.1889  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Interactive Entertainment
  mean                                                0.0572       0  0.0101
  std. dev.                                           0.2323  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Nintendo EAD
  mean                                                0.0303  0.0067  0.0269
  std. dev.                                           0.1714  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Game Freak
  mean                                                0.0202  0.0034  0.0337
  std. dev.                                           0.1667  0.1667  0.1804
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__WB Games
  mean                                                0.0101  0.0168  0.0269
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Bethesda Softworks
  mean                                                0.0269  0.0101  0.0101
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Computer Entertainment
  mean                                                0.0269  0.0101  0.0101
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Square
  mean                                                0.0168  0.0067  0.0236
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Ubisoft Montreal
  mean                                                0.0236  0.0034  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Intelligent Systems Co., Ltd.
  mean                                                0.0101  0.0101  0.0202
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sonic Team
  mean                                                0.0101  0.0168  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sony Computer Entertainment, Inc. (SCEI)
  mean                                                0.0135  0.0101  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Devolver Digital
  mean                                                0.0168  0.0067  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__FromSoftware
  mean                                                0.0202  0.0168       0
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Annapurna Interactive
  mean                                                0.0101  0.0101  0.0135
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Microsoft Game Studios
  mean                                                0.0168       0  0.0168
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Otro
  mean                                                0.3098  0.5168  0.3636
  std. dev.                                           0.4624  0.4997   0.481
  weight sum                                             297     298     297
  precision                                                1       1       1

estudio__Sin dato
  mean                                                     0  0.0034       0
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_-1.0
  mean                                                     0  0.0067  0.0034
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_1980.0
  mean                                                0.0067  0.0235  0.0202
  std. dev.                                           0.1667  0.1667  0.1667
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_1990.0
  mean                                                0.0572  0.1208  0.1178
  std. dev.                                           0.2323  0.3259  0.3224
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2000.0
  mean                                                0.2323  0.2517  0.2559
  std. dev.                                           0.4223   0.434  0.4364
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2010.0
  mean                                                0.5387   0.349  0.4141
  std. dev.                                           0.4985  0.4767  0.4926
  weight sum                                             297     298     297
  precision                                                1       1       1

decada__decada_2020.0
  mean                                                 0.165  0.2483  0.1886
  std. dev.                                           0.3712   0.432  0.3912
  weight sum                                             297     298     297
  precision                                                1       1       1

notas__Metacritic Rating
  mean                                                0.4438 -0.4334 -0.0818
  std. dev.                                           0.8149  1.0414  0.9321
  weight sum                                             297     298     297
  precision                                           0.1396  0.1396  0.1396

notas__Rating
  mean                                                0.4396 -0.3885 -0.0202
  std. dev.                                           0.7624  1.1617  0.8605
  weight sum                                             297     298     297
  precision                                           0.2311  0.2311  0.2311



Time taken to build model: 0.01 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         454               50.8969 %
Incorrectly Classified Instances       438               49.1031 %
Kappa statistic                          0.2635
Mean absolute error                      0.3457
Root mean squared error                  0.4616
Relative absolute error                 77.7914 %
Root relative squared error             97.9278 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.650    0.249    0.566      0.650    0.605      0.389    0.786     0.624     alto
                 0.550    0.214    0.564      0.550    0.557      0.339    0.744     0.591     bajo
                 0.327    0.274    0.373      0.327    0.348      0.055    0.585     0.407     medio
Weighted Avg.    0.509    0.245    0.501      0.509    0.503      0.261    0.705     0.541     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 193  28  76 |   a = alto
  47 164  87 |   b = bajo
 101  99  97 |   c = medio

````

## weka_RandomForest.txt

Ruta: `DocumentoFinal/evidencias/weka_RandomForest.txt` · Bytes: 3521 · SHA-256: `bed5274c54f92bc20ff70c7d64d600839b65e76ea4860e88d8e003dcd5bb47df`

````text
=== Run information ===

Scheme:       weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

RandomForest

Bagging with 100 iterations and base learner

weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -do-not-check-capabilities

Time taken to build model: 0.2 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         477               53.4753 %
Incorrectly Classified Instances       415               46.5247 %
Kappa statistic                          0.3021
Mean absolute error                      0.3619
Root mean squared error                  0.4355
Relative absolute error                 81.4156 %
Root relative squared error             92.3813 %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.657    0.215    0.604      0.657    0.629      0.433    0.816     0.679     alto
                 0.587    0.219    0.574      0.587    0.580      0.366    0.769     0.613     bajo
                 0.360    0.264    0.405      0.360    0.381      0.100    0.596     0.402     medio
Weighted Avg.    0.535    0.233    0.528      0.535    0.530      0.300    0.727     0.565     

=== Confusion Matrix ===

   a   b   c   <-- classified as
 195  29  73 |   a = alto
  39 175  84 |   b = bajo
  89 101 107 |   c = medio

````

## weka_ZeroR.txt

Ruta: `DocumentoFinal/evidencias/weka_ZeroR.txt` · Bytes: 3346 · SHA-256: `abc7807ce09733680834ddcfcbf72f7a71f72e62ad1d519db547385bc4fe1cad`

````text
=== Run information ===

Scheme:       weka.classifiers.rules.ZeroR 
Relation:     clasificacion
Instances:    892
Attributes:   53
              generos__Adventure
              generos__RPG
              generos__Shooter
              generos__Platform
              generos__Indie
              generos__Puzzle
              generos__Strategy
              generos__Brawler
              generos__Simulator
              generos__Fighting
              generos__Turn Based Strategy
              generos__Arcade
              generos__Visual Novel
              generos__Racing
              generos__Tactical
              generos__Otro
              generos__Sin dato
              estudio__Nintendo
              estudio__Capcom
              estudio__Square Enix
              estudio__Sega
              estudio__Electronic Arts
              estudio__Konami
              estudio__Bandai Namco Entertainment
              estudio__Activision
              estudio__Ubisoft Entertainment
              estudio__Atlus
              estudio__Sony Interactive Entertainment
              estudio__Nintendo EAD
              estudio__Game Freak
              estudio__WB Games
              estudio__Bethesda Softworks
              estudio__Sony Computer Entertainment
              estudio__Square
              estudio__Ubisoft Montreal
              estudio__Intelligent Systems Co., Ltd.
              estudio__Sonic Team
              estudio__Sony Computer Entertainment, Inc. (SCEI)
              estudio__Devolver Digital
              estudio__FromSoftware
              estudio__Annapurna Interactive
              estudio__Microsoft Game Studios
              estudio__Otro
              estudio__Sin dato
              decada__decada_-1.0
              decada__decada_1980.0
              decada__decada_1990.0
              decada__decada_2000.0
              decada__decada_2010.0
              decada__decada_2020.0
              notas__Metacritic Rating
              notas__Rating
              nivel_popularidad
Test mode:    10-fold cross-validation

=== Classifier model (full training set) ===

ZeroR predicts class value: bajo

Time taken to build model: 0 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         295               33.0717 %
Incorrectly Classified Instances       597               66.9283 %
Kappa statistic                         -0.0045
Mean absolute error                      0.4444
Root mean squared error                  0.4714
Relative absolute error                100      %
Root relative squared error            100      %
Total Number of Instances              892     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.293    0.303    0.326      0.293    0.309      -0.010   0.494     0.330     alto
                 0.698    0.702    0.333      0.698    0.451      -0.004   0.495     0.332     bajo
                 0.000    0.000    ?          0.000    ?          ?        0.494     0.330     medio
Weighted Avg.    0.331    0.335    ?          0.331    ?          ?        0.495     0.331     

=== Confusion Matrix ===

   a   b   c   <-- classified as
  87 210   0 |   a = alto
  90 208   0 |   b = bajo
  90 207   0 |   c = medio

````

## weka_dbscan.txt

Ruta: `DocumentoFinal/evidencias/weka_dbscan.txt` · Bytes: 76228 · SHA-256: `7d0866476ee480a90daee39e1469861c532b52da9dbef7bfb9c05eedcf11de94`

````text
=== Run information ===

Scheme:       weka.clusterers.DBSCAN -E 1.666296 -M 12 -A "weka.core.EuclideanDistance -R first-last"
Relation:     clustering
Instances:    887
Attributes:   6
              Plays
              Playing
              Backlogs
              Wishlist
              Rating
              Metacritic Rating
Test mode:    evaluate on training data


=== Clustering model (full training set) ===

DBSCAN clustering results
========================================================================================

Clustered DataObjects: 887
Number of attributes: 6
Epsilon: 1.666296; minPoints: 12
Distance-type: 
Number of generated clusters: 1
Elapsed time: .05

(  0.) 1.453174,2.79742,1.684415,2.272893,1.624324,1.673091                   -->  0
(  1.) 1.642703,2.667802,1.995272,2.007855,1.239142,1.305726                  -->  0
(  2.) 1.96262,2.48162,1.766831,1.708074,1.431733,1.795546                    -->  0
(  3.) 1.900737,1.499038,1.746862,1.369369,1.04655,1.183271                   -->  0
(  4.) 1.642703,2.450834,2.267802,1.595141,1.431733,0.570996                  -->  0
(  5.) 2.048109,2.233892,0.270636,-0.523116,1.239142,1.305726                 -->  0
(  6.) 0.682622,1.862601,1.662691,2.057665,1.04655,0.693451                   -->  0
(  7.) 0.902465,1.582954,1.385651,1.927696,1.239142,0.693451                  -->  0
(  8.) 1.799088,1.221971,-0.073931,-1.074392,-1.264545,0.326086               -->  0
(  9.) 1.504441,1.862601,1.979456,2.007855,1.239142,0.693451                  -->  0
( 10.) 1.140772,2.418738,1.786404,1.839895,1.431733,1.550636                  -->  0
( 11.) 0.742837,1.623537,1.08177,1.955198,0.083594,0.081176                   -->  0
( 12.) 1.642703,1.862601,1.726482,1.708074,1.04655,1.428181                   -->  0
( 13.) 1.932212,1.223571,1.521253,0.995985,1.431733,1.550636                  -->  0
( 14.) 1.453174,1.862601,1.878849,1.927696,1.624324,1.183271                  -->  0
( 15.) 1.598942,1.928191,1.930431,1.466409,1.04655,1.183271                   -->  0
( 16.) 1.552935,2.190792,1.861038,1.808665,1.431733,1.795546                  -->  0
( 17.) 1.900737,0.728852,1.157826,0.915873,0.853959,0.938361                  -->  0
( 18.) 1.799088,1.532671,1.228446,1.466409,1.04655,1.795546                   -->  0
( 19.) 0.892663,2.145081,1.08177,1.511347,0.083594,0.081176                   -->  0
( 20.) -0.10248,1.682333,0.577022,1.466409,1.239142,0.570996                  -->  0
( 21.) 1.279031,1.256413,1.594499,1.466409,0.853959,-0.286188                 -->  0
( 22.) 1.96262,1.649428,1.325734,0.45126,0.276185,1.795546                    -->  0
( 23.) 1.212563,2.09642,1.705672,1.808665,-0.686771,0.448541                  -->  0
( 24.) 0.407856,1.623537,0.861265,1.927696,1.431733,1.428181                  -->  0
( 25.) 0.132786,1.617871,0.909476,1.554196,1.431733,0.815906                  -->  0
( 26.) 0.504036,1.756058,1.08177,1.870101,1.04655,0.326086                    -->  0
( 27.) 0.519109,1.928191,1.766831,1.742838,1.816916,0.815906                  -->  0
( 28.) 1.642703,1.376422,1.228446,1.554196,0.853959,0.570996                  -->  0
( 29.) 1.552935,1.669165,1.617757,1.554196,1.04655,0.815906                   -->  0
( 30.) 0.618073,1.694418,1.570682,2.033096,1.04655,0.081176                   -->  0
( 31.) 1.642703,1.210674,1.08177,0.593509,0.853959,1.428181                   -->  0
( 32.) 1.799088,1.928191,0.270636,0.623878,0.853959,1.305726                  -->  0
( 33.) 1.504441,1.928191,1.662691,1.708074,0.853959,0.448541                  -->  0
( 34.) 1.279031,1.727099,1.726482,1.955198,1.431733,0.938361                  -->  0
( 35.) 1.340912,1.862601,1.766831,1.20146,1.04655,1.183271                    -->  0
( 36.) 1.212563,2.09642,1.805598,1.554196,1.04655,1.305726                    -->  0
( 37.) 1.279031,2.539662,0.435651,-0.342559,-2.034911,-0.163733               -->  0
( 38.) -0.380573,1.135507,0.810581,1.554196,1.04655,-0.163733                 -->  0
( 39.) 0.968235,0.962648,1.193767,1.776339,0.468776,0.203631                  -->  0
( 40.) 1.642703,1.218761,1.294357,0.995985,1.239142,1.795546                  -->  0
( 41.) 1.398798,1.57997,1.766831,1.137927,1.239142,0.203631                   -->  0
( 42.) 0.742837,1.478797,1.726482,1.870101,1.816916,0.326086                  -->  0
( 43.) 1.340912,1.386793,1.442142,1.419166,1.239142,1.060816                  -->  0
( 44.) 1.504441,1.327904,1.546276,1.137927,0.661368,0.326086                  -->  0
( 45.) 0.177633,1.790761,1.385651,1.708074,0.276185,0.203631                  -->  0
( 46.) 1.212563,1.423236,1.766831,1.595141,0.468776,0.938361                  -->  0
( 47.) 1.598942,2.313341,1.442142,0.915873,0.853959,0.815906                  -->  0
( 48.) 1.212563,1.225168,1.193767,1.671945,0.853959,1.305726                  -->  0
( 49.) 0.841978,0.837637,1.228446,1.511347,1.624324,0.815906                  -->  0
( 50.) 1.453174,1.928191,1.963383,1.260895,1.239142,1.183271                  -->  0
( 51.) 1.398798,1.442613,1.193767,1.316727,0.853959,1.305726                  -->  0
( 52.) 1.140772,1.561813,1.684415,1.634343,1.04655,0.693451                   -->  0
( 53.) 1.684429,1.391926,1.261951,0.828127,0.083594,1.673091                  -->  0
( 54.) -0.132878,1.296641,0.757159,1.595141,0.853959,0.815906                 -->  0
( 55.) 1.140772,1.303861,1.570682,1.634343,1.239142,0.570996                  -->  0
( 56.) 0.604586,1.862601,-1.038099,-0.794891,-1.842319,-0.776008              -->  0
( 57.) 1.279031,1.021298,1.261951,0.995985,1.239142,1.673091                  -->  0
( 58.) 1.140772,1.709677,1.594499,1.554196,0.853959,0.570996                  -->  0
( 59.) -0.132878,1.254881,0.435651,1.369369,-0.108998,-1.510738               -->  0
( 60.) 0.424619,1.349854,0.999372,1.595141,0.853959,0.326086                  -->  0
( 61.) 0.009754,1.251808,1.041429,1.708074,0.468776,0.326086                  -->  0
( 62.) 1.279031,1.184199,1.08177,1.137927,1.239142,0.815906                   -->  0
( 63.) 1.453174,1.160245,1.261951,1.137927,1.239142,2.040456                  -->  0
( 64.) 0.977249,0.416757,1.120529,1.137927,1.431733,1.673091                  -->  0
( 65.) 0.921753,1.7393,1.726482,1.634343,0.468776,-0.041278                   -->  0
( 66.) 0.968235,1.045969,1.193767,1.776339,0.468776,0.326086                  -->  0
( 67.) 1.062732,1.609292,1.120529,1.260895,1.239142,0.203631                  -->  0
( 68.) 0.892663,0.923235,1.385651,1.316727,1.431733,1.305726                  -->  0
( 69.) 1.212563,0.993627,1.521253,1.369369,1.431733,1.550636                  -->  0
( 70.) 1.212563,1.563852,1.469222,1.069686,0.083594,-0.408643                 -->  0
( 71.) 1.453174,0.59804,0.861265,1.137927,1.04655,1.550636                    -->  0
( 72.) 1.504441,1.492351,0.955446,0.347214,0.661368,0.081176                  -->  0
( 73.) 1.212563,0.946668,1.294357,1.069686,0.468776,0.448541                  -->  0
( 74.) 1.279031,1.273062,1.662691,0.995985,0.276185,1.305726                  -->  0
( 75.) 1.552935,1.165443,-0.701128,-0.589262,-0.879363,1.060816               -->  0
( 76.) 1.340912,0.767859,1.4143,0.828127,1.04655,1.673091                     -->  0
( 77.) 1.140772,1.862601,1.4143,1.20146,0.661368,0.815906                     -->  0
( 78.) 1.552935,0.804948,1.041429,0.553463,0.853959,1.550636                  -->  0
( 79.) 0.085578,1.215536,1.356146,1.671945,1.431733,0.326086                  -->  0
( 80.) 0.820874,1.385505,1.228446,1.20146,0.853959,0.815906                   -->  0
( 81.) 0.977249,0.848226,1.08177,0.915873,-0.301589,1.428181                  -->  0
( 82.) 1.552935,1.527347,-0.06759,0.410171,0.661368,1.183271                  -->  0
( 83.) -0.666067,1.689262,0.103768,0.915873,0.468776,-0.286188                -->  0
( 84.) 0.009754,1.684071,-0.111535,0.563332,-0.301589,-1.388283               -->  0
( 85.) 1.279031,0.640758,1.041429,0.75934,0.661368,0.326086                   -->  0
( 86.) -0.923924,0.944357,-0.072659,1.069686,1.624324,0.815906                -->  0
( 87.) 0.220345,0.920851,1.193767,1.595141,1.04655,0.570996                   -->  0
( 88.) -1.001904,1.397023,0.270636,1.137927,1.624324,1.428181                 -->  0
( 89.) 0.576989,1.445001,0.640785,0.789588,-0.686771,0.570996                 -->  0
( 90.) 1.453174,0.690962,0.999372,0.462279,0.468776,1.183271                  -->  0
( 91.) 1.279031,1.106203,1.356146,0.828127,0.083594,1.183271                  -->  0
( 92.) 0.707195,1.667392,1.442142,1.419166,1.239142,0.815906                  -->  0
( 93.) 1.212563,0.937382,1.228446,0.72292,0.661368,1.673091                   -->  0
( 94.) 0.373359,1.158505,0.909476,1.069686,0.276185,-0.286188                 -->  0
( 95.) -0.164344,1.334832,0.640785,1.511347,-0.108998,-0.041278               -->  0
( 96.) 1.140772,1.098696,1.4143,0.60648,0.661368,0.448541                     -->  0
( 97.) 1.212563,1.510052,1.546276,1.137927,-0.108998,0.815906                 -->  0
( 98.) 1.552935,0.829597,0.577022,-0.116818,0.468776,0.815906                 -->  0
( 99.) 1.212563,1.928191,-0.935626,-1.879694,-2.997867,-0.531098              -->  0
(100.) 0.940636,1.394479,1.805598,1.069686,-0.108998,-0.041278                -->  0
(101.) 1.279031,0.262247,0.577022,0.113629,-0.686771,-0.531098                -->  0
(102.) 1.398798,0.54886,1.157826,0.433067,0.853959,1.428181                   -->  0
(103.) 0.94993,1.170604,1.385651,0.828127,0.083594,-0.286188                  -->  0
(104.) 1.140772,1.133708,0.810581,0.828127,0.853959,-0.163733                 -->  0
(105.) 1.398798,1.27605,-0.44656,-0.867313,0.468776,1.183271                  -->  0
(106.) 0.707195,1.194236,1.157826,1.20146,0.468776,0.081176                   -->  0
(107.) 0.912161,0.53704,0.909476,1.20146,0.853959,0.081176                    -->  0
(108.) 1.340912,0.61255,0.909476,0.642081,-0.49418,0.326086                   -->  0
(109.) 1.062732,1.177432,1.157826,0.822587,-0.301589,0.570996                 -->  0
(110.) 0.199243,1.079595,1.041429,1.419166,-0.301589,0.693451                 -->  0
(111.) 0.977249,0.279202,1.228446,1.316727,1.431733,1.060816                  -->  0
(112.) 0.035747,0.67128,0.04463,0.655502,0.276185,0.203631                    -->  0
(113.) -0.196953,0.840298,0.700683,1.595141,0.276185,-0.163733                -->  0
(114.) 1.279031,0.799359,1.294357,0.695692,0.468776,0.693451                  -->  0
(115.) 0.902465,0.184025,1.041429,1.069686,1.624324,1.060816                  -->  0
(116.) 1.140772,0.014084,1.157826,1.316727,0.468776,1.183271                  -->  0
(117.) 1.140772,0.793728,0.909476,0.828127,-0.108998,0.326086                 -->  0
(118.) 1.140772,0.426015,0.909476,0.440107,0.853959,0.815906                  -->  0
(119.) -1.001904,0.700615,0.700683,1.419166,0.853959,-0.163733                -->  0
(120.) 1.140772,0.770777,0.757159,0.475871,1.239142,1.550636                  -->  0
(121.) 1.453174,1.35926,-0.178517,-1.173904,-0.49418,0.326086                 -->  0
(122.) 1.212563,0.829597,1.385651,0.571882,0.083594,0.570996                  -->  0
(123.) -0.666067,0.700615,0.640785,1.554196,0.083594,0.448541                 -->  0
(124.) 0.15549,1.234678,1.193767,1.419166,1.816916,1.060816                   -->  0
(125.) 1.504441,-0.638529,-0.947869,-1.351667,0.083594,-0.776008              -->  0
(126.) -0.785761,1.589871,-0.195636,1.260895,-0.301589,0.203631               -->  0
(127.) 1.552935,-0.035138,-0.58789,-0.811106,0.468776,-0.041278               -->  0
(128.) 0.820874,0.397895,1.041429,1.260895,-0.879363,-0.408643                -->  0
(129.) 0.337482,0.637289,0.172542,1.069686,-0.108998,0.081176                 -->  0
(130.) 1.212563,0.644211,1.041429,1.260895,1.04655,1.550636                   -->  0
(131.) -0.073078,1.36855,0.999372,1.419166,-0.108998,0.570996                 -->  0
(132.) -0.852185,0.74107,0.161574,1.419166,1.239142,0.815906                  -->  0
(133.) 1.340912,0.479293,1.157826,0.204904,-0.301589,0.448541                 -->  0
(134.) 1.212563,0.215077,1.08177,1.069686,1.239142,1.918001                   -->  0
(135.) 0.841978,-0.30788,0.955446,1.069686,0.661368,0.693451                  -->  0
(136.) 0.473108,1.862601,0.757159,1.069686,0.661368,0.693451                  -->  0
(137.) 1.398798,0.647648,0.176501,-0.071736,0.661368,-0.776008                -->  0
(138.) -0.265958,1.015002,1.041429,1.466409,1.04655,-0.286188                 -->  0
(139.) 1.398798,0.31201,0.577022,0.228144,0.276185,0.938361                   -->  0
(140.) -0.230792,1.380328,-0.529719,0.182919,-0.301589,-1.265828              -->  0
(141.) 0.940636,0.889157,1.157826,0.915873,0.661368,0.815906                  -->  0
(142.) 1.398798,0.117801,-0.01467,-0.319884,-0.301589,0.815906                -->  0
(143.) 0.754409,0.722667,1.325734,1.260895,0.853959,1.060816                  -->  0
(144.) -0.196953,1.355243,0.909476,1.595141,0.276185,0.693451                 -->  0
(145.) 1.062732,0.402655,0.577022,0.727039,-0.108998,1.428181                 -->  0
(146.) 1.062732,0.637289,0.955446,1.069686,-0.301589,-0.531098                -->  0
(147.) 1.062732,1.050004,1.325734,0.915873,-0.686771,-0.163733                -->  0
(148.) 0.373359,1.602551,1.442142,1.260895,0.083594,0.081176                  -->  0
(149.) 1.212563,0.250728,0.955446,0.68069,-0.301589,0.938361                  -->  0
(150.) 1.279031,0.759034,0.435651,0.115625,0.853959,0.081176                  -->  0
(151.) -0.666067,0.500428,0.435651,1.137927,-0.108998,-1.265828               -->  0
(152.) -0.164344,0.706981,1.08177,1.069686,1.239142,-1.020918                 -->  0
(153.) 1.279031,0.770777,0.810581,0.527043,0.276185,1.918001                  -->  0
(154.) 0.719234,0.353646,0.577022,0.499842,0.661368,0.815906                  -->  0
(155.) 0.831488,0.955841,1.228446,0.818875,0.853959,1.183271                  -->  0
(156.) 0.63136,1.000104,1.442142,0.995985,1.239142,1.428181                   -->  0
(157.) 1.140772,0.067723,0.577022,0.24042,1.04655,1.428181                    -->  0
(158.) 0.765835,0.34345,0.861265,0.621577,0.661368,1.183271                   -->  0
(159.) 0.424619,1.220368,1.193767,1.20146,0.853959,-0.653553                  -->  0
(160.) 0.902465,1.560792,1.193767,1.137927,0.276185,0.815906                  -->  0
(161.) 1.279031,0.533059,0.810581,0.4457,0.083594,0.693451                    -->  0
(162.) -0.044609,0.317342,0.270636,1.069686,0.853959,0.938361                 -->  0
(163.) 1.140772,0.021984,0.700683,0.669823,0.083594,-0.041278                 -->  0
(164.) 1.279031,0.177658,-0.521681,-1.466352,0.083594,0.570996                -->  0
(165.) 0.765835,0.776581,1.228446,1.137927,0.468776,0.693451                  -->  0
(166.) 0.177633,1.106203,1.041429,1.511347,0.468776,1.183271                  -->  0
(167.) 0.424619,0.586972,1.120529,0.828127,0.083594,-0.163733                 -->  0
(168.) 0.731113,1.075716,1.193767,1.466409,0.468776,0.570996                  -->  0
(169.) 1.212563,0.184025,0.356582,0.182919,-1.457137,-0.163733                -->  0
(170.) -0.073078,1.017106,0.999372,1.260895,0.853959,-0.286188                -->  0
(171.) 1.279031,-0.549665,-0.309922,-0.225678,0.083594,0.570996               -->  0
(172.) 0.085578,0.644211,0.577022,1.316727,0.661368,0.693451                  -->  0
(173.) 1.140772,0.525033,0.270636,0.115625,0.661368,0.570996                  -->  0
(174.) 0.977249,-0.516857,0.435651,0.659932,0.276185,0.693451                 -->  0
(175.) -0.723919,0.30664,-0.001576,0.635297,0.468776,0.326086                 -->  0
(176.) 0.061009,0.358693,0.757159,0.995985,1.431733,0.081176                  -->  0
(177.) 0.300111,1.571954,1.294357,0.995985,1.04655,1.060816                   -->  0
(178.) 0.618073,0.529056,1.228446,1.20146,1.431733,0.570996                   -->  0
(179.) 0.912161,-0.026708,0.435651,0.482593,0.661368,1.305726                 -->  0
(180.) 0.940636,0.110847,0.810581,0.424547,1.239142,1.673091                  -->  0
(181.) 0.280824,1.391926,-0.158912,0.348764,0.276185,1.183271                 -->  0
(182.) 0.931244,-0.41211,0.700683,0.276294,-0.686771,-0.898463                -->  0
(183.) -0.666067,0.124691,0.577022,1.137927,0.468776,-0.898463                -->  0
(184.) 0.707195,0.59804,0.909476,0.581557,0.661368,1.183271                   -->  0
(185.) 0.473108,-0.087797,-0.837261,-0.450277,0.661368,0.081176               -->  0
(186.) 1.212563,-0.358196,-0.285984,-0.323089,0.276185,0.081176               -->  0
(187.) 0.085578,1.17913,0.999372,1.069686,0.276185,-0.163733                  -->  0
(188.) 0.682622,0.967152,1.228446,0.775076,0.276185,0.570996                  -->  0
(189.) -0.30256,1.155012,0.757159,1.260895,0.661368,0.448541                  -->  0
(190.) 1.212563,-0.061008,-0.181349,-0.480248,-0.301589,0.570996              -->  0
(191.) -0.923924,0.262247,0.089851,0.627319,0.853959,-0.041278                -->  0
(192.) 0.820874,0.358693,0.955446,0.528318,-0.108998,-0.408643                -->  0
(193.) 0.109493,0.53704,1.157826,0.788628,1.431733,0.938361                   -->  0
(194.) 0.892663,0.082373,1.356146,0.487935,-0.108998,0.693451                 -->  0
(195.) -1.34506,0.677898,0.106952,0.915873,-1.071954,-1.020918                -->  0
(196.) 0.872731,1.106203,1.041429,0.074844,-0.108998,-0.041278                -->  0
(197.) 0.831488,0.28477,0.810581,0.995985,0.661368,0.326086                   -->  0
(198.) 0.754409,0.052783,0.640785,0.995985,0.083594,-0.163733                 -->  0
(199.) 0.618073,0.244902,0.508861,0.661036,-0.686771,1.060816                 -->  0
(200.) 0.199243,1.098696,1.120529,0.828127,0.083594,-0.653553                 -->  0
(201.) -0.923924,0.021984,-0.349472,0.301089,0.468776,0.570996                -->  0
(202.) 0.754409,0.53704,0.757159,0.281306,-2.227502,-1.878103                 -->  0
(203.) 0.533933,0.171237,0.640785,0.428817,1.04655,0.203631                   -->  0
(204.) -0.785761,0.262247,-0.207216,0.915873,1.431733,0.815906                -->  0
(205.) 0.977249,0.378548,0.757159,0.192143,-0.301589,0.938361                 -->  0
(206.) -0.164344,1.400824,1.041429,0.761322,1.624324,0.570996                 -->  0
(207.) 0.94993,0.886663,0.098438,0.190306,-1.457137,-0.286188                 -->  0
(208.) 0.742837,1.029612,1.120529,0.815148,0.276185,-0.286188                 -->  0
(209.) 0.799262,1.466156,-1.041479,-1.198479,-2.227502,-0.286188              -->  0
(210.) 0.940636,0.0061,-0.060033,0.055887,0.468776,1.305726                   -->  0
(211.) 1.062732,-0.320148,0.577022,0.146999,-0.108998,1.183271                -->  0
(212.) 0.604586,0.466322,0.640785,0.392618,1.431733,-0.163733                 -->  0
(213.) 0.562865,0.075084,0.577022,0.553463,0.468776,0.815906                  -->  0
(214.) 0.820874,-0.516857,-0.745292,-0.822076,-1.457137,-0.531098             -->  0
(215.) 0.882752,0.164761,-0.168665,-0.37595,0.853959,0.570996                 -->  0
(216.) 0.719234,-0.018372,0.508861,-0.012568,-0.686771,-0.286188              -->  0
(217.) -0.017016,0.722667,0.577022,0.995985,0.853959,0.570996                 -->  0
(218.) -0.852185,0.43516,0.508861,0.915873,-0.301589,-0.776008                -->  0
(219.) 1.062732,-1.240976,-1.231251,-1.198479,-0.301589,1.183271              -->  0
(220.) 0.109493,-0.144409,0.176501,0.748364,-0.108998,-1.020918               -->  0
(221.) -0.852185,1.06593,0.577022,0.505086,1.04655,0.326086                   -->  0
(222.) 0.473108,0.402655,0.176501,0.356476,0.661368,0.938361                  -->  0
(223.) 0.810133,1.161982,-0.223363,-1.198479,-1.264545,-1.510738              -->  0
(224.) 0.831488,-0.018372,0.435651,0.076927,-0.879363,0.326086                -->  0
(225.) 0.3556,-0.583965,-0.143776,-0.597874,-3.38305,-3.102652                -->  0
(226.) 0.300111,-0.249365,0.640785,0.75636,0.468776,-0.163733                 -->  0
(227.) 0.280824,1.322316,0.861265,0.995985,0.661368,0.203631                  -->  0
(228.) 0.959129,-1.124675,-1.082966,-0.619764,-0.49418,-0.408643              -->  0
(229.) 0.892663,-0.26071,-0.415521,-0.768485,-0.108998,0.326086               -->  0
(230.) 0.731113,-0.358196,0.356582,-0.35245,-1.264545,0.570996                -->  0
(231.) 0.820874,0.103829,0.700683,0.148925,-0.49418,0.203631                  -->  0
(232.) 0.15549,1.45917,0.810581,0.598247,1.239142,-0.163733                   -->  0
(233.) 0.731113,-0.195063,0.435651,0.317256,-0.49418,-0.286188                -->  0
(234.) 0.407856,0.500428,0.999372,0.506392,1.04655,1.428181                   -->  0
(235.) -0.044609,-0.227173,0.577022,0.683925,-0.301589,0.203631               -->  0
(236.) 0.488705,-0.500973,-0.077755,0.045184,1.239142,-0.776008               -->  0
(237.) 0.177633,-0.320148,0.176501,0.576732,1.04655,0.448541                  -->  0
(238.) 0.457234,-0.533083,-0.132912,0.036531,-2.420093,-4.572111              -->  0
(239.) -0.017016,0.935042,1.294357,0.995985,1.04655,0.938361                  -->  0
(240.) 0.132786,0.358693,0.508861,0.481252,-0.108998,0.326086                 -->  0
(241.) -0.340719,0.233113,0.018326,0.915873,-0.108998,-0.163733               -->  0
(242.) 0.731113,0.256509,0.270636,0.091374,1.04655,-0.286188                  -->  0
(243.) 0.892663,0.0452,0.356582,0.093419,-1.071954,0.203631                   -->  0
(244.) 0.132786,0.871522,0.435651,-0.104073,1.624324,0.815906                 -->  0
(245.) 0.318991,0.416757,1.193767,0.501156,-0.686771,-0.898463                -->  0
(246.) 0.604586,0.021984,0.577022,0.401436,1.04655,0.938361                   -->  0
(247.) -0.017016,0.457549,0.700683,0.60296,-0.301589,-0.163733                -->  0
(248.) 0.604586,0.227149,0.810581,0.099529,-0.686771,-0.041278                -->  0
(249.) 0.694993,-0.115572,0.577022,0.156588,0.083594,1.305726                 -->  0
(250.) 0.820874,-1.05604,-0.523684,-1.081676,-2.420093,-2.490377              -->  0
(251.) 0.590894,1.050004,0.435651,-0.222793,0.661368,-0.163733                -->  0
(252.) 0.604586,0.453124,0.356582,0.133404,-1.264545,-0.163733                -->  0
(253.) 0.977249,-0.907628,-0.523684,-0.674523,-0.879363,0.693451              -->  0
(254.) 0.240961,-0.227173,0.10483,0.382222,1.816916,0.570996                  -->  0
(255.) -1.001904,0.89659,-0.093203,0.320456,-0.108998,-0.286188               -->  0
(256.) 0.977249,-1.02393,-1.104381,-1.322716,-0.686771,0.326086               -->  0
(257.) 0.061009,0.616134,0.999372,1.137927,-0.108998,0.570996                 -->  0
(258.) 0.562865,-0.295808,0.356582,0.089324,-1.264545,0.448541                -->  0
(259.) 0.533933,0.353646,0.700683,0.250813,0.661368,0.448541                  -->  0
(260.) -1.087314,-0.332619,0.640785,0.719819,0.661368,1.183271                -->  0
(261.) 0.300111,-0.052286,0.757159,0.001084,-0.301589,0.326086                -->  0
(262.) -1.001904,0.796549,-0.926542,-0.476448,1.239142,0.448541               -->  0
(263.) 0.604586,0.158228,-0.290725,0.111628,0.083594,0.693451                 -->  0
(264.) 0.132786,0.402655,0.356582,-0.012568,0.083594,0.693451                 -->  0
(265.) 0.519109,-0.26071,-0.341101,-1.074392,-0.108998,-0.286188              -->  0
(266.) 0.373359,-0.549665,-0.189896,-0.158832,-0.49418,-0.531098              -->  0
(267.) 0.765835,-0.154271,-0.244303,-0.507296,-0.686771,0.570996              -->  0
(268.) 0.670079,-0.184656,-0.496001,-1.089019,-0.301589,-0.163733             -->  0
(269.) 0.604586,-0.783667,-1.086503,-1.011298,0.468776,-1.265828              -->  0
(270.) -0.380573,-0.332619,-0.590032,0.411619,-0.301589,-0.776008             -->  0
(271.) 0.424619,-0.426212,0.270636,0.233425,-1.842319,-1.510738               -->  0
(272.) -1.794543,0.353646,-0.45963,0.361072,-0.49418,-1.510738                -->  0
(273.) -0.340719,1.00439,0.577022,0.749367,0.468776,0.203631                  -->  0
(274.) -0.265958,-0.125062,0.356582,1.20146,0.661368,-0.041278                -->  0
(275.) -0.196953,-0.144409,0.508861,0.408721,0.083594,-0.776008               -->  0
(276.) -0.073078,-0.677228,-0.146511,0.609986,0.468776,0.203631               -->  0
(277.) 0.132786,0.117801,0.640785,-0.410598,-0.108998,0.938361                -->  0
(278.) 0.533933,1.747327,-0.194198,0.00559,0.083594,0.448541                  -->  0
(279.) 0.670079,1.077658,1.594499,0.995985,0.661368,0.693451                  -->  0
(280.) 1.398798,1.113636,1.228446,0.565783,-1.071954,0.570996                 -->  0
(281.) 1.279031,0.487818,1.157826,0.995985,0.853959,1.305726                  -->  0
(282.) 0.63136,0.810495,0.999372,1.260895,0.853959,0.448541                   -->  0
(283.) 1.552935,-0.440583,-0.486299,-0.446599,0.276185,1.305726               -->  0
(284.) 1.398798,0.987095,1.157826,0.179203,-0.301589,0.815906                 -->  0
(285.) 0.457234,0.832286,1.120529,1.369369,0.661368,0.081176                  -->  0
(286.) 0.831488,1.508958,1.4143,1.870101,0.853959,0.081176                    -->  0
(287.) 0.441075,-0.398266,0.270636,0.353399,1.04655,0.815906                  -->  0
(288.) 0.132786,0.208968,0.955446,0.664341,0.661368,0.203631                  -->  0
(289.) 0.799262,0.964903,0.270636,0.411619,0.661368,0.693451                  -->  0
(290.) 0.457234,0.916061,0.955446,1.069686,0.276185,0.448541                  -->  0
(291.) 0.220345,0.575739,0.435651,0.213912,0.853959,0.570996                  -->  0
(292.) 0.977249,-0.332619,-0.899781,-0.971514,-0.301589,0.326086              -->  0
(293.) 0.921753,0.014084,0.111181,-0.535162,-0.108998,-0.041278               -->  0
(294.) -1.001904,0.457549,0.508861,0.816081,0.853959,-2.857742                -->  0
(295.) 0.109493,0.244902,-0.920532,0.099529,0.083594,-0.286188                -->  0
(296.) 0.618073,-0.106199,0.435651,0.585159,0.468776,0.570996                 -->  0
(297.) 0.94993,-1.089577,-0.75538,-0.679237,-0.301589,0.081176                -->  0
(298.) -2.299963,0.807726,-0.426365,0.726011,1.431733,0.326086                -->  0
(299.) -1.277222,-0.035138,-0.247331,0.296183,0.468776,0.815906               -->  0
(300.) 0.15549,0.0061,0.270636,0.133404,1.239142,1.060816                     -->  0
(301.) 0.63136,1.163714,0.861265,0.558411,-0.49418,0.081176                   -->  0
(302.) 0.457234,0.466322,1.228446,0.489265,0.276185,0.081176                  -->  0
(303.) 0.318991,0.31201,0.757159,0.647697,-0.49418,-0.898463                  -->  0
(304.) -0.923924,0.03754,-0.682115,0.038702,0.083594,-0.408643                -->  0
(305.) 0.373359,1.025466,0.435651,0.119606,1.04655,0.326086                   -->  0
(306.) 0.300111,-0.440583,0.435651,0.568227,0.276185,0.203631                 -->  0
(307.) 0.220345,-0.371318,0.128957,0.182919,0.276185,1.060816                 -->  0
(308.) 0.407856,0.804948,-0.439169,0.001084,-0.686771,-1.633193               -->  0
(309.) 0.061009,-0.26071,0.176501,0.199457,0.276185,0.693451                  -->  0
(310.) -0.196953,0.067723,0.090928,0.26109,0.083594,-0.531098                 -->  0
(311.) -0.132878,-0.238187,0.175512,0.682848,1.04655,-1.878103                -->  0
(312.) 0.618073,-0.71802,-0.150627,-0.403563,-0.301589,-0.286188              -->  0
(313.) -2.320987,-0.783667,-1.202945,0.675273,-2.612685,-2.245467             -->  0
(314.) 0.177633,-0.677228,0.270636,0.12159,0.853959,0.448541                  -->  0
(315.) -0.265958,0.383432,0.139266,0.395567,0.661368,0.693451                 -->  0
(316.) 0.085578,0.363706,0.700683,0.166079,0.661368,0.570996                  -->  0
(317.) -1.841071,-0.358196,-0.856728,0.175472,0.083594,-0.408643              -->  0
(318.) 0.731113,-0.164264,-0.334455,-0.523116,-0.686771,0.570996              -->  0
(319.) -0.422281,0.700615,-1.713287,-2.288781,-0.879363,-0.286188             -->  0
(320.) 0.670079,-1.240976,-0.503832,-1.182023,-1.264545,-0.163733             -->  0
(321.) -0.044609,0.834966,0.999372,0.4691,0.853959,0.326086                   -->  0
(322.) 0.670079,-0.56662,-0.324569,-0.991191,-0.686771,0.081176               -->  0
(323.) -0.466024,0.579502,0.810581,0.747359,0.853959,-0.531098                -->  0
(324.) 0.707195,-0.455234,-0.015869,-0.137586,-0.879363,-1.143373             -->  0
(325.) -0.56048,0.767859,0.169563,0.38966,1.04655,0.570996                    -->  0
(326.) 0.407856,-0.238187,0.270636,0.079004,0.468776,0.570996                 -->  0
(327.) 0.085578,-0.195063,-1.075929,-0.642186,1.04655,0.203631                -->  0
(328.) -1.642578,-0.195063,-0.757918,0.00559,0.661368,0.570996                -->  0
(329.) 0.488705,-0.26071,0.700683,0.167965,0.276185,0.815906                  -->  0
(330.) 0.261114,0.837637,0.909476,0.631886,0.468776,-0.041278                 -->  0
(331.) -1.101767,0.233113,0.07792,0.812343,0.853959,0.938361                  -->  0
(332.) -0.666067,0.202809,-0.090611,0.292898,1.624324,-0.041278               -->  0
(333.) 0.533933,-0.500973,-0.347792,-0.507296,-1.457137,-0.531098             -->  0
(334.) 0.300111,-0.052286,0.577022,0.466378,-0.301589,0.570996                -->  0
(335.) 0.912161,-0.426212,-0.658852,-0.800264,-0.108998,0.326086              -->  0
(336.) 0.009754,0.267941,0.700683,0.305969,0.468776,0.938361                  -->  0
(337.) -1.236099,0.74107,-2.6919,-2.648968,0.083594,0.326086                  -->  0
(338.) -0.164344,0.684458,0.270636,0.247361,1.431733,1.060816                 -->  0
(339.) 0.424619,-1.124675,-1.111623,-1.126637,-1.264545,-2.490377             -->  0
(340.) 0.3556,0.052783,-0.308308,-0.255027,-0.49418,-0.041278                 -->  0
(341.) -2.349808,0.089593,-1.273148,-0.345844,1.624324,-0.163733              -->  0
(342.) -0.785761,0.483568,-0.088027,0.70626,-1.071954,-0.776008               -->  0
(343.) -0.422281,-0.26071,0.156548,0.653279,0.083594,-1.388283                -->  0
(344.) -0.017016,0.866407,1.041429,0.441508,0.083594,-0.408643                -->  0
(345.) -0.923924,0.262247,0.143359,0.828127,0.276185,0.448541                 -->  0
(346.) 0.441075,-0.677228,0.270636,0.032174,-0.108998,1.183271                -->  0
(347.) 0.457234,0.03754,0.577022,0.023398,-1.264545,-0.776008                 -->  0
(348.) 0.061009,-0.00197,0.356582,0.111628,-0.301589,-0.163733                -->  0
(349.) 0.15549,-0.227173,0.435651,0.304345,-0.301589,0.815906                 -->  0
(350.) -0.017016,0.684458,0.640785,0.395567,-1.264545,-1.510738               -->  0
(351.) -1.150416,-0.71802,-1.243635,-0.021784,-1.842319,-1.143373             -->  0
(352.) -1.75031,-1.546886,-1.726737,-1.157877,-0.686771,-1.143373             -->  0
(353.) -0.164344,0.483568,0.020641,0.368681,0.853959,0.815906                 -->  0
(354.) -2.183223,-0.164264,-1.693447,-0.610946,-0.301589,-0.653553            -->  0
(355.) -0.132878,-0.272229,0.356582,-0.010279,-1.264545,0.081176              -->  0
(356.) 0.009754,-0.184656,0.861265,0.109622,-0.301589,0.203631                -->  0
(357.) 0.644453,-1.089577,-1.54762,-1.511868,0.468776,0.326086                -->  0
(358.) 0.280824,0.619701,0.1454,-0.708036,0.083594,0.693451                   -->  0
(359.) -0.785761,0.363706,0.270636,0.326822,0.661368,0.326086                 -->  0
(360.) 0.407856,-0.677228,-0.422737,-0.258015,-0.301589,1.428181              -->  0
(361.) -0.422281,-0.174391,0.640785,0.474521,1.04655,0.081176                 -->  0
(362.) -0.852185,-0.078761,-0.573023,0.383714,1.239142,0.448541               -->  0
(363.) 0.199243,-1.430585,-1.179312,-0.732743,0.468776,1.673091               -->  0
(364.) -0.666067,0.397895,-0.079033,0.613479,-1.842319,-1.143373              -->  0
(365.) -2.027319,-0.018372,-1.747263,-1.84556,1.431733,0.570996               -->  0
(366.) -0.923924,0.082373,0.435651,0.318858,0.083594,0.081176                 -->  0
(367.) -0.785761,-0.144409,-0.128868,0.083146,0.276185,-0.163733              -->  0
(368.) 0.390773,0.470671,-0.138329,-0.674523,-0.49418,0.081176                -->  0
(369.) 0.035747,-0.115572,0.270636,0.212118,0.083594,-0.408643                -->  0
(370.) -0.196953,-0.619899,-0.226327,-0.480248,0.661368,-0.163733             -->  0
(371.) 0.657357,-0.761144,-0.998417,-1.067164,0.083594,-0.041278              -->  0
(372.) 0.085578,0.221137,0.356582,-0.026426,0.083594,0.326086                 -->  0
(373.) 0.220345,0.295784,0.435651,-0.222793,0.853959,0.448541                 -->  0
(374.) -2.483816,0.03754,-1.904279,-1.433633,0.661368,-0.163733               -->  0
(375.) -0.56048,-0.164264,0.577022,0.430236,0.661368,0.326086                 -->  0
(376.) 0.390773,0.131519,-1.471535,-2.927523,-2.034911,-1.020918              -->  0
(377.) -0.044609,-0.485416,0.176501,-0.042861,-2.034911,-0.531098             -->  0
(378.) -0.380573,0.373633,0.270636,-0.084039,0.468776,-0.653553               -->  0
(379.) -3.793439,-0.619899,-1.937236,-0.194437,0.661368,-0.286188             -->  0
(380.) -0.132878,0.28477,-0.03281,0.364123,0.083594,0.203631                  -->  0
(381.) -3.144654,-1.32984,-2.151576,-0.597874,-2.034911,-2.980197             -->  0
(382.) 0.220345,-0.227173,0.270636,0.0256,-0.686771,0.448541                  -->  0
(383.) -0.466024,-0.806883,-0.566719,-0.057185,0.276185,0.203631              -->  0
(384.) -2.450436,-0.783667,-0.879456,0.238676,-1.264545,-2.123013             -->  0
(385.) -0.466024,-0.154271,0.139266,0.26109,0.661368,0.326086                 -->  0
(386.) -0.785761,-0.485416,0.167572,0.399972,0.468776,-1.755648               -->  0
(387.) 0.280824,-0.601718,-0.018272,-1.031853,-0.301589,-0.408643             -->  0
(388.) -2.150385,-1.240976,-2.043261,-1.149967,-0.108998,-0.041278            -->  0
(389.) 0.15549,-0.935066,-0.492109,-0.597874,-0.879363,0.570996               -->  0
(390.) 0.337482,0.0061,0.176501,-0.884866,-1.071954,-1.020918                 -->  0
(391.) -1.001904,-0.583965,0.435651,0.435889,1.431733,-0.041278               -->  0
(392.) 0.519109,-1.089577,-0.720513,-0.568077,-0.108998,1.550636              -->  0
(393.) -0.164344,0.267941,0.757159,0.314046,0.468776,0.448541                 -->  0
(394.) -0.340719,-0.549665,-0.496001,-0.576493,-2.227502,-1.633193            -->  0
(395.) -0.512009,0.029802,-0.03281,0.537197,-0.108998,-0.408643               -->  0
(396.) -1.609898,-0.470174,-1.367374,-0.261011,-0.49418,-0.531098             -->  0
(397.) -0.196953,-0.41211,0.164577,0.190306,0.853959,0.938361                 -->  0
(398.) -0.30256,0.533059,0.356582,0.518065,-0.301589,-0.286188                -->  0
(399.) -0.196953,-0.638529,0.0801,0.195807,-0.108998,1.183271                 -->  0
(400.) -0.56048,-0.216317,0.270636,0.184771,0.661368,-0.531098                -->  0
(401.) -0.666067,0.06029,-0.600813,-1.341915,-1.071954,-1.265828              -->  0
(402.) 0.177633,-0.549665,-0.969666,-0.708036,0.661368,-0.286188              -->  0
(403.) 0.035747,-0.935066,-0.066326,-0.049995,-0.49418,1.305726               -->  0
(404.) 0.085578,-0.470174,0.270636,-0.547368,-0.301589,-0.653553              -->  0
(405.) 0.407856,-0.739274,-1.227157,-0.722781,-1.649728,-0.776008             -->  0
(406.) -0.923924,0.244902,0.356582,0.669823,0.853959,0.448541                 -->  0
(407.) -0.265958,-0.010126,0.132061,0.195807,1.04655,0.448541                 -->  0
(408.) -0.785761,-0.65763,-0.469072,0.007835,1.239142,0.448541                -->  0
(409.) -2.726407,-0.052286,-1.122588,0.131446,-0.49418,-1.143373              -->  0
(410.) -0.56048,-0.601718,0.508861,-0.13235,-0.108998,-0.041278               -->  0
(411.) -0.230792,0.110847,0.114341,0.42169,-0.686771,-0.531098                -->  0
(412.) -0.10248,-0.855575,0.356582,0.162294,0.276185,0.938361                 -->  0
(413.) 0.061009,-0.371318,-0.040161,-0.693524,0.083594,-0.163733              -->  0
(414.) -1.359508,0.31201,-0.575133,0.255965,-0.49418,-0.531098                -->  0
(415.) -1.818517,-1.089577,-0.701128,-0.389653,1.431733,-0.898463             -->  0
(416.) 0.373359,-0.697348,-0.080313,-0.965047,-0.879363,-0.163733             -->  0
(417.) -0.785761,-0.500973,-0.063804,0.424547,1.239142,0.693451               -->  0
(418.) 0.280824,-0.144409,-0.143776,-1.157877,-0.301589,-0.531098             -->  0
(419.) -0.56048,0.124691,0.577022,0.408721,-0.108998,0.203631                 -->  0
(420.) -0.196953,0.738034,-0.737793,-0.683975,-0.301589,-1.143373             -->  0
(421.) 0.261114,-0.830836,-0.259536,-0.237306,-1.264545,-0.531098             -->  0
(422.) -3.473509,-1.763933,-2.573462,-0.914885,-0.49418,-0.776008             -->  0
(423.) -1.236099,-0.830836,-0.207216,-0.679237,-1.842319,-0.776008            -->  0
(424.) -0.56048,0.131519,0.508861,-0.177833,-0.108998,-0.776008               -->  0
(425.) -0.230792,-0.272229,0.143359,-0.593558,0.276185,-0.653553              -->  0
(426.) -1.192738,-0.371318,-1.686922,-2.236109,1.431733,-0.408643             -->  0
(427.) -1.737269,-1.05604,-0.957152,-1.165856,-0.879363,-0.286188             -->  0
(428.) -0.10248,0.184025,-0.966523,-0.773706,0.853959,0.448541                -->  0
(429.) -2.368303,-2.069843,-2.439459,-1.547544,-0.49418,-2.123013             -->  0
(430.) 0.240961,-1.089577,-0.213057,-0.156149,0.083594,0.081176               -->  0
(431.) -2.596935,-0.881153,-2.130979,-0.503383,0.083594,-0.653553             -->  0
(432.) -2.592126,-1.430585,-1.775311,-0.921008,-2.997867,-3.102652            -->  0
(433.) -0.044609,-0.677228,0.026406,-0.491743,0.661368,-0.041278              -->  0
(434.) -2.074539,-1.124675,-1.796882,-0.35577,-1.457137,-1.633193             -->  0
(435.) -0.422281,-0.010126,-0.119497,0.190306,1.04655,0.448541                -->  0
(436.) -0.380573,0.279202,0.356582,-0.25205,-0.879363,-0.163733               -->  0
(437.) -0.196953,-0.638529,-0.047566,-0.049995,0.661368,0.570996              -->  0
(438.) -0.017016,-1.430585,-1.334957,-1.190214,-1.649728,-3.837382            -->  0
(439.) -1.977612,-0.332619,-1.231251,-0.933377,1.624324,0.815906              -->  0
(440.) -0.30256,0.029802,0.356582,0.201276,0.083594,-0.163733                 -->  0
(441.) -0.10248,-0.935066,-0.394183,-0.480248,-0.879363,1.060816              -->  0
(442.) 0.407856,-0.549665,-1.344111,-2.162349,-2.420093,-1.388283             -->  0
(443.) -0.073078,-1.200184,-0.86519,-0.855794,-3.38305,-1.633193              -->  0
(444.) 0.109493,-0.272229,0.074641,-0.642186,0.276185,0.203631                -->  0
(445.) -1.92366,-1.05604,-0.765572,-0.285343,0.083594,-0.653553               -->  0
(446.) 0.132786,-0.440583,-0.75538,-0.228571,0.468776,0.570996                -->  0
(447.) -0.265958,-0.426212,-0.165869,-0.468894,-2.612685,0.693451             -->  0
(448.) -0.340719,-0.601718,-0.043857,-0.021784,-0.108998,-0.041278            -->  0
(449.) -0.340719,-0.345299,0.508861,0.091374,-0.686771,-0.408643              -->  0
(450.) -1.087314,-0.65763,-0.189896,0.213912,1.04655,-0.163733                -->  0
(451.) 0.261114,0.164761,-1.768224,-1.55975,-0.301589,1.305726                -->  0
(452.) -0.044609,-0.830836,-1.530816,-0.965047,-1.071954,-1.755648            -->  0
(453.) -2.174148,-1.161485,-1.104381,-0.965047,0.083594,-1.020918             -->  0
(454.) 0.177633,-1.200184,-0.3328,-0.382776,-1.649728,-2.612832               -->  0
(455.) 1.453174,1.732817,-0.568816,-1.971007,-1.649728,-0.531098              -->  0
(456.) 1.398798,1.470777,-0.298679,-0.372556,-1.264545,-0.163733              -->  0
(457.) 0.788257,1.790007,1.08177,1.511347,1.04655,0.693451                    -->  0
(458.) 1.453174,0.976081,1.546276,0.995985,0.661368,1.673091                  -->  0
(459.) 1.140772,0.850851,1.261951,1.260895,1.04655,1.428181                   -->  0
(460.) 0.519109,1.665615,1.726482,1.776339,1.239142,0.203631                  -->  0
(461.) 1.598942,2.233892,0.435651,0.915873,-0.108998,0.938361                 -->  0
(462.) 1.504441,0.568157,1.570682,0.779939,-0.301589,1.428181                 -->  0
(463.) 1.140772,0.177658,0.909476,0.637564,-0.301589,-0.408643                -->  0
(464.) 0.519109,0.383432,1.356146,1.466409,0.853959,1.060816                  -->  0
(465.) 0.968235,0.273592,0.700683,0.152764,0.276185,-0.653553                 -->  0
(466.) 0.177633,1.017106,1.08177,1.069686,1.04655,-0.041278                   -->  0
(467.) -0.017016,0.863837,0.700683,1.137927,0.276185,0.326086                 -->  0
(468.) 0.590894,0.483568,0.508861,0.154678,1.431733,0.570996                  -->  0
(469.) 1.212563,0.619701,0.955446,0.520639,0.083594,0.693451                  -->  0
(470.) -0.852185,0.84295,0.176501,1.069686,0.276185,-0.531098                 -->  0
(471.) 0.63136,0.654476,1.157826,0.995985,1.239142,1.795546                   -->  0
(472.) 0.742837,0.014084,1.08177,1.069686,0.468776,1.428181                   -->  0
(473.) -1.102678,0.719556,-0.210132,0.915873,-1.264545,-1.510738              -->  0
(474.) 1.062732,1.281991,-0.698731,-1.433633,1.04655,-2.490377                -->  0
(475.) 0.977249,0.483568,0.640785,0.296183,-1.071954,0.081176                 -->  0
(476.) 0.390773,0.764929,1.193767,1.20146,1.04655,0.693451                    -->  0
(477.) 0.682622,0.932696,1.157826,1.260895,0.661368,-0.408643                 -->  0
(478.) -0.785761,0.06029,-0.111535,0.765273,-1.264545,-1.510738               -->  0
(479.) 0.931244,0.850851,0.861265,0.638696,0.276185,1.183271                  -->  0
(480.) -0.380573,0.383432,0.165576,0.781877,1.239142,0.815906                 -->  0
(481.) 0.519109,0.785203,1.469222,1.554196,1.239142,0.938361                  -->  0
(482.) 0.977249,0.466322,0.861265,0.592321,0.276185,1.060816                  -->  0
(483.) 0.300111,0.560497,1.120529,1.634343,1.239142,0.815906                  -->  0
(484.) 0.788257,0.601694,1.120529,0.915873,-0.301589,0.081176                 -->  0
(485.) 1.140772,0.4214,0.861265,0.340988,-0.49418,1.305726                    -->  0
(486.) 1.140772,0.0452,0.356582,0.113629,-1.071954,0.693451                   -->  0
(487.) 0.533933,0.4214,0.757159,0.819805,1.04655,-0.041278                    -->  0
(488.) -0.611721,0.54886,0.700683,1.260895,1.239142,-0.041278                 -->  0
(489.) 1.140772,0.34345,0.176501,0.115625,-0.301589,0.938361                  -->  0
(490.) 0.604586,0.674596,1.157826,1.20146,-0.108998,0.081176                  -->  0
(491.) 0.337482,0.393104,0.861265,1.137927,1.04655,0.326086                   -->  0
(492.) 1.279031,-0.739274,-0.224844,-0.35577,0.276185,1.428181                -->  0
(493.) 1.140772,0.138285,0.270636,0.127516,0.661368,0.815906                  -->  0
(494.) 1.340912,-0.697348,-0.686834,-0.861535,0.276185,1.060816               -->  0
(495.) 1.140772,1.48786,-0.583619,-1.466352,-1.071954,0.815906                -->  0
(496.) 0.576989,-0.371318,0.640785,0.221056,-3.960824,-1.755648               -->  0
(497.) 1.062732,0.91846,0.810581,0.314046,1.04655,1.428181                    -->  0
(498.) 0.15549,-0.283926,-0.123503,0.623878,-2.420093,-0.776008               -->  0
(499.) 0.441075,0.388283,0.700683,0.995985,0.853959,0.815906                  -->  0
(500.) 0.441075,1.256413,0.757159,0.823513,0.661368,0.815906                  -->  0
(501.) 0.959129,0.487818,0.999372,0.42169,0.661368,1.183271                   -->  0
(502.) 1.140772,0.029802,0.577022,0.217491,0.468776,1.673091                  -->  0
(503.) 0.977249,1.228351,0.999372,0.690362,0.276185,0.938361                  -->  0
(504.) 0.977249,0.448673,1.041429,0.915873,0.853959,1.060816                  -->  0
(505.) -0.265958,1.195896,-0.199962,-0.035781,1.816916,1.183271               -->  0
(506.) 0.852347,0.832286,1.08177,0.742321,0.468776,0.815906                   -->  0
(507.) 1.279031,1.373807,-1.425544,-2.648968,-1.842319,-1.633193              -->  0
(508.) 0.519109,0.89412,1.325734,1.20146,0.661368,0.693451                    -->  0
(509.) 0.220345,1.094914,1.08177,0.915873,0.853959,0.081176                   -->  0
(510.) 0.940636,0.295784,0.640785,0.434479,1.239142,0.570996                  -->  0
(511.) 0.373359,0.158228,0.700683,0.700991,1.04655,1.060816                   -->  0
(512.) 1.062732,0.0452,0.356582,-0.08652,0.661368,1.060816                    -->  0
(513.) 1.140772,0.227149,0.640785,0.236929,0.276185,1.550636                  -->  0
(514.) 0.424619,-0.010126,0.810581,0.828127,0.853959,-0.041278                -->  0
(515.) 1.140772,-0.184656,0.356582,-0.038135,-1.264545,0.203631               -->  0
(516.) -0.132878,0.327894,0.909476,1.069686,1.239142,-0.653553                -->  0
(517.) 0.618073,0.512831,0.700683,0.74131,1.239142,0.938361                   -->  0
(518.) 0.604586,0.764929,1.041429,1.069686,-0.879363,0.326086                 -->  0
(519.) 0.618073,0.54494,0.955446,0.637564,0.853959,0.815906                   -->  0
(520.) -1.360722,-0.295808,-0.486299,0.828127,-1.457137,-1.633193             -->  0
(521.) 0.788257,-0.096942,0.577022,0.470458,0.468776,-0.286188                -->  0
(522.) 0.519109,0.03754,0.810581,0.520639,0.661368,0.938361                   -->  0
(523.) 0.777116,-0.061008,0.356582,0.334719,-0.49418,-0.408643                -->  0
(524.) 0.424619,0.31201,0.700683,0.755364,0.853959,0.081176                   -->  0
(525.) -1.812463,0.677898,-0.354529,0.354938,1.04655,0.938361                 -->  0
(526.) 0.590894,0.184025,0.17155,0.145069,-0.686771,-2.735287                 -->  0
(527.) -0.132878,0.661242,1.041429,0.68069,0.853959,-0.041278                 -->  0
(528.) 0.085578,-0.455234,0.124803,0.415948,1.816916,1.428181                 -->  0
(529.) 0.590894,-0.069833,0.700683,0.474521,-0.108998,0.203631                -->  0
(530.) 0.457234,-0.71802,-0.181349,0.182919,-0.49418,-0.898463                -->  0
(531.) 0.682622,0.889157,0.861265,0.474521,-0.49418,-0.163733                 -->  0
(532.) -0.923924,0.317342,0.270636,0.995985,-1.071954,-0.898463               -->  0
(533.) 0.035747,0.295784,0.909476,0.639826,0.083594,-0.531098                 -->  0
(534.) -0.666067,0.799359,-1.227157,-0.059594,-0.686771,-0.898463             -->  0
(535.) -0.044609,0.866407,0.700683,1.069686,0.276185,0.326086                 -->  0
(536.) 0.754409,-0.035138,0.435651,-0.079098,-0.686771,1.795546               -->  0
(537.) 0.670079,1.298091,-0.139688,-0.669834,-1.264545,-1.388283              -->  0
(538.) 0.424619,-0.332619,0.909476,0.274617,-0.49418,-0.531098                -->  0
(539.) 0.754409,0.227149,0.700683,0.405814,-0.49418,-1.020918                 -->  0
(540.) 0.872731,0.633804,-0.179932,0.027796,0.276185,0.081176                 -->  0
(541.) 0.931244,0.244902,-0.108896,-0.188869,1.04655,0.570996                 -->  0
(542.) -0.466024,0.594369,0.508861,1.316727,-0.108998,-0.163733               -->  0
(543.) 0.373359,0.508719,1.041429,0.519353,-0.108998,0.938361                 -->  0
(544.) 0.788257,0.512831,0.810581,0.299457,0.083594,1.428181                  -->  0
(545.) -0.785761,0.4214,0.356582,0.518065,1.04655,-2.245467                   -->  0
(546.) 0.548516,0.029802,0.861265,0.552222,-0.108998,0.081176                 -->  0
(547.) 0.576989,0.23903,0.120631,0.456786,-0.108998,-0.531098                 -->  0
(548.) 0.862597,-0.087797,0.094154,-0.90276,-0.108998,-0.776008               -->  0
(549.) 0.473108,1.012891,0.955446,0.474521,-0.879363,-0.163733                -->  0
(550.) 0.754409,0.770777,-0.154761,-0.205675,0.083594,0.570996                -->  0
(551.) 0.035747,-0.078761,0.757159,0.995985,0.661368,0.938361                 -->  0
(552.) -0.56048,1.075716,0.861265,1.069686,0.661368,-0.776008                 -->  0
(553.) 0.407856,0.525033,0.909476,0.42169,-0.108998,0.570996                  -->  0
(554.) 0.968235,0.393104,-0.351155,-0.054782,0.661368,0.693451                -->  0
(555.) -1.685178,0.719556,-0.752848,0.534669,-0.301589,-0.286188              -->  0
(556.) -0.30256,0.876603,0.508861,0.611152,1.04655,0.815906                   -->  0
(557.) 0.373359,-0.026708,0.176501,-0.158832,-0.108998,0.815906               -->  0
(558.) 0.852347,1.303861,0.01018,-1.258506,-1.457137,0.326086                 -->  0
(559.) 0.912161,-0.619899,-1.294782,-1.111405,0.468776,0.693451               -->  0
(560.) -0.611721,-0.41211,-0.021886,0.501156,0.468776,0.326086                -->  0
(561.) 0.590894,0.295784,0.435651,0.995985,-0.108998,-0.163733                -->  0
(562.) 0.63136,-0.125062,-0.080313,-0.453971,0.083594,-1.143373               -->  0
(563.) 0.921753,-0.164264,0.049134,-0.606568,-0.49418,0.203631                -->  0
(564.) 0.799262,-0.125062,-0.287562,-0.722781,-1.071954,-0.163733             -->  0
(565.) -1.341484,-0.638529,-1.093615,-0.071736,0.661368,-0.531098             -->  0
(566.) -0.017016,0.633804,0.955446,0.131446,0.276185,-0.653553                -->  0
(567.) 0.261114,0.785203,-1.492683,-1.677549,-1.842319,-1.510738              -->  0
(568.) 0.085578,0.397895,0.700683,0.502468,0.276185,0.448541                  -->  0
(569.) 0.035747,0.144992,0.810581,0.460909,0.083594,-1.510738                 -->  0
(570.) -0.852185,0.388283,0.757159,1.069686,1.239142,-1.510738                -->  0
(571.) -2.230033,0.295784,-0.329499,0.388177,0.853959,0.203631                -->  0
(572.) 0.15549,0.412086,1.120529,0.810468,0.276185,0.203631                   -->  0
(573.) 0.841978,-0.71802,-0.079033,-0.593558,-0.108998,0.815906               -->  0
(574.) -1.343866,-0.227173,0.176501,0.548489,1.431733,-1.755648               -->  0
(575.) 0.390773,0.951268,0.999372,0.197634,-0.108998,0.081176                 -->  0
(576.) -0.044609,-0.078761,0.999372,1.069686,0.083594,-0.041278               -->  0
(577.) -0.512009,0.244902,0.508861,0.777024,0.276185,-2.612832                -->  0
(578.) 0.657357,-0.638529,0.640785,-0.403563,0.083594,0.570996                -->  0
(579.) 0.852347,-0.272229,0.176501,-0.156149,-0.686771,-0.286188              -->  0
(580.) 0.644453,-0.56662,0.757159,-0.276143,0.853959,0.938361                 -->  0
(581.) -0.611721,0.722667,-1.171558,-0.362448,0.083594,-0.898463              -->  0
(582.) -0.10248,0.54886,-0.474781,-0.386208,1.816916,0.938361                 -->  0
(583.) 0.132786,0.623252,0.757159,0.42312,-0.879363,-1.388283                 -->  0
(584.) 0.765835,0.889157,-0.77587,-0.984586,-0.879363,-1.143373               -->  0
(585.) -1.087314,-0.238187,-0.596486,0.08521,-1.842319,-1.388283              -->  0
(586.) 0.820874,-0.806883,-0.613907,-0.393111,0.468776,0.570996               -->  0
(587.) 0.548516,-0.061008,0.356582,0.023398,0.276185,0.570996                 -->  0
(588.) -1.477377,0.190338,-0.390671,0.601784,0.276185,-0.531098               -->  0
(589.) 0.3556,0.430601,0.757159,0.368681,0.661368,-0.041278                   -->  0
(590.) 0.457234,-0.56662,0.176501,0.222833,0.083594,0.448541                  -->  0
(591.) -0.230792,0.373633,0.700683,0.995985,0.276185,-0.163733                -->  0
(592.) 0.061009,-0.087797,0.176501,0.42312,1.04655,-0.163733                  -->  0
(593.) 0.682622,0.117801,-0.119497,-0.914885,-0.49418,0.693451                -->  0
(594.) -1.890145,0.407385,-1.20694,0.213912,1.04655,-0.408643                 -->  0
(595.) -0.666067,0.110847,0.861265,0.821661,0.853959,0.081176                 -->  0
(596.) 0.754409,0.244902,-0.012276,-0.978027,-1.071954,-1.755648              -->  0
(597.) 0.548516,-0.144409,0.577022,0.314046,0.276185,0.326086                 -->  0
(598.) -0.196953,0.317342,0.435651,0.460909,-0.108998,-0.898463               -->  0
(599.) 0.742837,-0.71802,-0.469072,-0.703173,0.661368,0.081176                -->  0
(600.) 0.562865,0.552759,-0.480524,-0.43565,-1.457137,-0.286188               -->  0
(601.) 0.15549,-0.881153,0.435651,-0.180579,-0.301589,0.448541                -->  0
(602.) 0.373359,-0.069833,-0.654265,-0.166927,-0.49418,-0.286188              -->  0
(603.) 0.261114,-0.320148,-0.254941,-0.180579,-0.108998,1.673091              -->  0
(604.) -2.066494,-0.65763,-1.034731,0.208518,-0.686771,-1.143373              -->  0
(605.) -0.422281,0.208968,0.810581,0.828127,0.468776,-0.286188                -->  0
(606.) -0.10248,-0.154271,0.757159,0.339424,0.661368,1.183271                 -->  0
(607.) 0.261114,0.327894,-0.3328,-0.307173,-0.879363,0.081176                 -->  0
(608.) -0.723919,0.626786,0.577022,0.552222,0.661368,0.448541                 -->  0
(609.) 0.682622,-0.272229,-0.075204,-0.768485,-1.071954,0.448541              -->  0
(610.) -0.30256,-0.184656,0.909476,0.17734,0.853959,0.448541                  -->  0
(611.) -0.611721,-0.320148,0.577022,0.585159,0.661368,1.428181                -->  0
(612.) -0.132878,0.388283,0.577022,0.520639,1.04655,0.326086                  -->  0
(613.) 0.199243,0.244902,0.049134,0.001084,0.083594,0.326086                  -->  0
(614.) -0.512009,0.262247,0.270636,0.318858,1.04655,0.326086                  -->  0
(615.) -0.666067,-0.043663,0.435651,0.66544,0.661368,-0.531098                -->  0
(616.) 0.009754,-0.238187,-0.122166,-0.732743,-0.49418,-3.959837              -->  0
(617.) 0.240961,-0.018372,0.577022,0.296183,-0.108998,0.815906                -->  0
(618.) -2.226835,0.3383,-1.090052,0.111628,0.468776,0.081176                  -->  0
(619.) -0.132878,-0.106199,-0.185614,0.257677,0.468776,0.203631               -->  0
(620.) -0.265958,0.416757,0.640785,0.619271,-1.457137,-0.531098               -->  0
(621.) 0.177633,-0.345299,-0.211593,0.00559,0.661368,-0.653553                -->  0
(622.) 0.15549,-0.806883,-0.329499,-0.2792,-0.879363,1.060816                 -->  0
(623.) 0.533933,-0.881153,-0.947869,-0.535162,0.083594,-0.163733              -->  0
(624.) -0.512009,-0.440583,-1.079441,-0.789549,-2.227502,-2.123013            -->  0
(625.) 0.280824,-0.30788,-0.217461,-0.304023,-0.108998,-0.041278              -->  0
(626.) -0.30256,0.28477,0.435651,0.188465,1.431733,1.183271                   -->  0
(627.) 0.3556,0.124691,-0.543944,-0.822076,-1.264545,-0.653553                -->  0
(628.) -1.818517,-1.124675,-1.410678,-0.069295,-1.649728,-1.388283            -->  0
(629.) 0.132786,-0.00197,0.176501,0.107612,0.661368,-0.286188                 -->  0
(630.) 0.407856,0.06029,0.810581,-0.491743,-1.457137,-0.898463                -->  0
(631.) -0.164344,0.151639,0.356582,0.411619,-0.301589,-1.510738               -->  0
(632.) 0.300111,1.083454,0.640785,-0.222793,-0.301589,-0.041278               -->  0
(633.) -0.265958,0.190338,0.508861,0.331568,0.468776,-0.041278                -->  0
(634.) -1.291735,-0.195063,-1.455966,-0.081565,-0.49418,-1.143373             -->  0
(635.) -2.012115,0.3383,-0.742786,0.424547,0.468776,0.326086                  -->  0
(636.) -0.132878,0.295784,-0.529719,-0.177833,-2.227502,-0.653553             -->  0
(637.) -0.512009,0.616134,0.356582,1.137927,1.816916,1.305726                 -->  0
(638.) -2.346154,-0.935066,-1.268878,-0.382776,0.853959,0.693451              -->  0
(639.) 0.604586,-1.161485,-1.048274,-1.118989,-0.108998,0.448541              -->  0
(640.) 0.009754,-0.601718,-0.36643,-0.211346,0.083594,1.060816                -->  0
(641.) 0.590894,-1.684442,-0.851127,-0.914885,-2.420093,-0.531098             -->  0
(642.) -1.087314,-0.761144,-0.642888,-0.231473,1.04655,0.693451               -->  0
(643.) -2.338891,-1.05604,-1.587977,-0.237306,0.853959,0.203631               -->  0
(644.) 0.132786,-0.205615,0.700683,0.091374,-0.108998,-0.286188               -->  0
(645.) 0.337482,0.674596,0.060305,-0.727748,-0.108998,-0.163733               -->  0
(646.) -0.923924,-0.96354,-0.354529,0.404357,1.04655,-0.653553                -->  0
(647.) 0.085578,-0.549665,-0.079033,-0.035781,0.083594,0.448541               -->  0
(648.) -1.134219,0.052783,-0.73035,-0.049995,-0.301589,-0.408643              -->  0
(649.) -2.007104,-0.26071,-0.075204,0.579147,-0.108998,-1.020918              -->  0
(650.) 0.519109,-0.739274,-0.663461,-0.800264,-0.686771,0.203631              -->  0
(651.) -1.001904,-0.806883,-0.373296,-0.017164,1.04655,1.060816               -->  0
(652.) -1.001904,-0.164264,0.270636,0.222833,1.239142,1.060816                -->  0
(653.) 0.240961,-1.32984,0.121676,-0.359103,-0.49418,-0.286188                -->  0
(654.) 0.441075,-0.078761,-0.107578,-0.838781,-0.301589,0.326086              -->  0
(655.) -0.196953,-1.852797,-0.691576,0.160396,0.661368,-0.776008              -->  0
(656.) 0.318991,-0.533083,-0.815473,-1.018099,-0.301589,-0.408643             -->  0
(657.) 0.009754,-0.00197,-0.047566,-0.124551,-1.842319,-1.265828              -->  0
(658.) -1.001904,-0.65763,-0.77587,-0.129743,-0.686771,-0.286188              -->  0
(659.) -1.98246,-0.96354,-1.455966,-0.297754,-0.301589,-1.388283              -->  0
(660.) -1.301922,-1.430585,-0.941729,0.099529,0.661368,-0.041278              -->  0
(661.) -0.422281,-0.295808,-0.118166,-0.369174,-1.264545,1.060816             -->  0
(662.) 0.15549,-0.249365,-0.088027,-0.114255,-0.686771,-0.653553              -->  0
(663.) -1.247811,0.03754,0.176501,-0.001177,0.468776,-0.286188                -->  0
(664.) -0.340719,-0.71802,0.577022,0.401436,0.468776,0.448541                 -->  0
(665.) -0.666067,-0.30788,0.169563,0.179203,0.276185,0.693451                 -->  0
(666.) 0.318991,-1.200184,-0.926542,-0.827611,0.661368,0.693451               -->  0
(667.) -0.164344,-0.078761,-0.135617,0.359542,-0.686771,-0.898463             -->  0
(668.) 0.280824,-0.806883,-0.465285,-0.543281,0.083594,1.305726               -->  0
(669.) -0.017016,0.096745,0.270636,0.184771,-0.49418,-0.163733                -->  0
(670.) -3.423664,-0.533083,-2.01567,-0.461402,-0.879363,-0.408643             -->  0
(671.) -0.196953,-0.907628,-0.287562,-0.134964,-1.457137,-0.286188            -->  0
(672.) -1.33084,-1.02393,0.081188,0.089324,1.239142,-0.163733                 -->  0
(673.) -0.466024,-0.440583,-0.041391,-0.31669,-0.879363,0.570996              -->  0
(674.) -0.380573,-0.184656,0.270636,0.091374,0.276185,-0.041278               -->  0
(675.) -0.265958,0.322636,-1.008189,-0.965047,0.853959,-1.633193              -->  0
(676.) 0.220345,0.110847,-0.042623,-0.410598,-1.842319,0.448541               -->  0
(677.) -1.087314,-0.205615,-0.689202,-0.323089,1.624324,0.815906              -->  0
(678.) 0.390773,-1.430585,-0.985536,-0.908802,-2.227502,-0.163733             -->  0
(679.) 0.085578,-0.993131,-1.167704,-1.2764,-1.649728,1.305726                -->  0
(680.) -0.512009,0.59068,-0.624954,-0.655906,-1.457137,-1.143373              -->  0
(681.) 0.390773,-0.516857,-1.179312,-2.316291,-2.420093,0.448541              -->  0
(682.) -1.37296,-0.761144,-0.048806,0.587552,0.276185,-2.857742               -->  0
(683.) -0.666067,-0.783667,-0.152003,0.493246,-0.49418,-1.510738              -->  0
(684.) 0.504036,-0.295808,-0.929561,-1.059993,0.276185,-0.163733              -->  0
(685.) -0.132878,-0.384671,0.114341,-0.28843,-0.879363,-0.041278              -->  0
(686.) -0.196953,-0.533083,-0.077755,-0.400066,-0.686771,1.060816             -->  0
(687.) -1.667895,0.144992,-3.359345,-2.210861,-2.034911,-0.776008             -->  0
(688.) 0.199243,-1.02393,-0.862362,-1.126637,-0.108998,0.693451               -->  0
(689.) -0.132878,-1.161485,-0.672744,-0.742814,-1.649728,-1.633193            -->  0
(690.) -1.094511,-0.601718,-0.517687,-0.156149,1.239142,1.428181              -->  0
(691.) 0.424619,-0.371318,-0.807424,-0.978027,0.468776,0.938361               -->  0
(692.) -0.512009,-0.125062,-0.034032,-0.503383,-0.879363,-0.163733            -->  0
(693.) 0.009754,-0.332619,-1.514293,-1.02495,0.083594,-1.388283               -->  0
(694.) 0.085578,-0.320148,-0.235274,-0.568077,-0.301589,-0.163733             -->  0
(695.) 0.009754,-1.05604,-0.804756,-0.580729,0.276185,-1.388283               -->  0
(696.) 0.177633,-0.41211,-0.613907,-1.173904,-0.879363,-0.408643              -->  0
(697.) -0.785761,-0.061008,0.176501,0.148925,1.04655,0.203631                 -->  0
(698.) 0.177633,-0.371318,-0.363015,-1.371485,-1.649728,-0.531098             -->  0
(699.) -0.265958,-0.739274,-0.511725,-0.589262,-2.227502,-2.367922            -->  0
(700.) -1.087314,0.34345,0.270636,0.252533,0.853959,0.448541                  -->  0
(701.) -0.196953,0.903951,0.270636,0.493246,-0.301589,-0.531098               -->  0
(702.) -0.132878,-0.677228,-0.042623,-1.173904,-1.071954,-1.143373            -->  0
(703.) -2.335281,-0.993131,-1.51977,-0.597874,-1.457137,-0.898463             -->  0
(704.) -0.073078,-0.638529,-0.533762,-1.2323,1.431733,0.815906                -->  0
(705.) -0.422281,-0.195063,0.176501,-0.747892,-0.879363,-0.531098             -->  0
(706.) 0.035747,-0.806883,-0.324569,-0.421251,-2.227502,0.203631              -->  0
(707.) 0.441075,0.096745,-1.849123,-2.572131,-1.457137,0.693451               -->  0
(708.) 0.085578,-0.96354,-0.773285,-0.342559,-0.108998,-0.653553              -->  0
(709.) -1.76164,-0.078761,-1.260392,-0.712925,-0.879363,-1.020918             -->  0
(710.) -0.230792,-0.619899,-0.383684,-0.180579,-0.879363,-1.143373            -->  0
(711.) -1.549405,-0.855575,-0.287562,0.314046,0.276185,-1.878103              -->  0
(712.) 0.009754,-0.907628,0.028702,-0.191649,-0.879363,-1.265828              -->  0
(713.) -0.196953,-0.549665,0.062524,-0.43565,-1.649728,-0.898463              -->  0
(714.) -6.662579,-3.421667,-3.006729,-0.939625,2.202098,1.428181              -->  0
(715.) -0.611721,-0.096942,0.577022,0.255965,-0.686771,0.203631               -->  0
(716.) -0.044609,-1.05604,-0.361312,-0.372556,-0.108998,0.815906              -->  0
(717.) -2.130097,-1.124675,-0.718069,-0.240236,-0.49418,-0.776008             -->  0
(718.) -0.723919,-0.549665,0.435651,0.043028,-1.071954,-2.000558              -->  0
(719.) -0.611721,-1.32984,-0.760463,-0.789549,0.468776,0.326086               -->  0
(720.) -1.087314,-0.761144,-0.182769,0.146999,0.853959,-0.898463              -->  0
(721.) -0.666067,0.322636,-0.773285,-0.096509,1.04655,0.570996                -->  0
(722.) -0.852185,-0.583965,-0.472875,-0.43565,0.083594,-0.041278              -->  0
(723.) -0.380573,-1.546886,-0.611713,-1.074392,-0.879363,-0.776008            -->  0
(724.) -2.082657,0.453124,-2.071644,-1.004547,-0.301589,-1.510738             -->  0
(725.) -2.606633,-1.124675,-0.747804,-2.236109,-1.649728,-0.653553            -->  0
(726.) -1.890145,-0.907628,-0.944794,-0.610946,1.04655,-3.470017              -->  0
(727.) -0.512009,-0.806883,-0.297083,-0.101544,-0.108998,0.326086             -->  0
(728.) 0.109493,-1.124675,-1.068942,-0.878977,-1.264545,-1.388283             -->  0
(729.) -0.512009,-1.089577,-0.45214,-0.747892,0.083594,-0.163733              -->  0
(730.) -0.422281,-0.205615,-0.346115,-0.559737,-0.49418,0.203631              -->  0
(731.) 0.109493,-1.200184,-1.43055,-1.103882,-1.264545,-2.123013              -->  0
(732.) -1.419747,-0.295808,-0.545993,-0.010279,0.083594,-0.408643             -->  0
(733.) -0.611721,-0.00197,-0.215991,-0.855794,0.083594,0.326086               -->  0
(734.) -0.666067,-0.358196,-0.431832,-0.811106,-1.264545,-0.163733            -->  0
(735.) -0.230792,-0.332619,0.062524,-0.310335,-1.071954,-0.653553             -->  0
(736.) 0.177633,-1.684442,-1.148654,-1.206819,-0.301589,-0.286188             -->  0
(737.) -1.001904,-0.583965,-0.482445,-0.012568,-0.49418,0.326086              -->  0
(738.) -0.164344,-1.02393,-1.400889,-1.004547,-0.686771,1.060816              -->  0
(739.) -2.233242,-1.200184,-1.264625,-1.126637,-0.108998,-0.531098            -->  0
(740.) -0.230792,-0.358196,-3.083803,-3.513593,-2.227502,-1.020918            -->  0
(741.) -3.582367,-2.375753,-1.599817,-2.010227,-0.108998,0.081176             -->  0
(742.) -0.785761,0.221137,0.054735,-0.674523,0.661368,-1.265828               -->  0
(743.) -0.512009,-0.426212,-0.264152,-0.389653,0.083594,1.183271              -->  0
(744.) -1.896748,-0.516857,-0.737793,-0.172364,-1.264545,-0.776008            -->  0
(745.) 0.109493,-0.881153,-0.631641,-0.890792,0.083594,-2.490377              -->  0
(746.) -0.611721,-0.71802,-0.995181,-0.503383,0.468776,-0.531098              -->  0
(747.) 0.085578,-1.02393,-1.277437,-1.597368,-1.457137,-1.633193              -->  0
(748.) 0.035747,-1.32984,-1.082966,-1.285479,-2.612685,0.081176               -->  0
(749.) -0.56048,-0.516857,-0.179932,-0.208506,-0.301589,0.081176              -->  0
(750.) -0.073078,-1.852797,-1.167704,-0.703173,0.468776,0.081176              -->  0
(751.) -0.164344,-1.124675,-0.411932,-0.563898,-0.301589,0.081176             -->  0
(752.) -1.319161,-0.018372,-0.270341,-0.010279,0.853959,0.570996              -->  0
(753.) -0.666067,0.158228,-0.745292,-0.127144,1.04655,0.938361                -->  0
(754.) -0.923924,0.075084,-0.26879,-0.104073,-0.108998,-0.408643              -->  0
(755.) -0.466024,-0.249365,-0.684472,-0.861535,1.04655,0.448541               -->  0
(756.) 0.109493,-2.89871,-3.196912,-3.328673,-1.842319,-0.898463              -->  0
(757.) -0.340719,-0.677228,-0.745292,-0.914885,0.468776,-0.408643             -->  0
(758.) -0.132878,-0.619899,-0.911586,-1.511868,-1.649728,-0.286188            -->  0
(759.) -0.132878,-1.612534,-0.701128,-0.884866,-1.071954,0.203631             -->  0
(760.) -1.001904,-1.2841,-1.34872,-1.535498,1.431733,1.060816                 -->  0
(761.) -0.380573,-0.26071,-0.349472,-0.939625,0.083594,0.815906               -->  0
(762.) -0.340719,-1.02393,-1.247797,-1.84556,-0.49418,0.448541                -->  0
(763.) -0.852185,-0.783667,-0.454007,-0.37595,-0.301589,-0.163733             -->  0
(764.) -0.230792,-2.375753,-1.818934,-1.511868,-2.420093,-1.020918            -->  0
(765.) -0.30256,-0.638529,-0.982341,-1.198479,0.468776,-0.531098              -->  0
(766.) -0.723919,0.267941,-0.629407,-0.778957,1.04655,-0.286188               -->  0
(767.) -0.196953,-1.240976,-2.656588,-2.236109,0.276185,-0.163733             -->  0
(768.) -2.104669,-0.619899,-1.223081,-1.02495,-1.071954,-1.755648             -->  0
(769.) -1.186712,-0.195063,-0.120831,-0.140215,0.853959,0.570996              -->  0
(770.) -0.340719,-1.953542,-1.014758,-1.081676,-0.879363,0.203631             -->  0
(771.) -0.666067,-1.089577,-0.319662,-0.805669,-0.108998,0.693451             -->  0
(772.) -0.073078,-1.240976,-1.339523,-1.052877,-0.49418,-1.143373             -->  0
(773.) -0.10248,-1.852797,-1.654925,-1.173904,-0.301589,-1.510738             -->  0
(774.) -0.164344,-1.953542,-1.58211,-1.096421,0.083594,-1.020918              -->  0
(775.) -0.265958,-1.124675,-1.896209,-2.236109,-0.108998,0.326086             -->  0
(776.) 0.15549,-0.806883,-1.330411,-1.720418,-1.071954,-0.286188              -->  0
(777.) -0.422281,-1.546886,-1.587977,-1.341915,-1.071954,-2.612832            -->  0
(778.) -0.265958,-1.02393,-0.441011,-0.624205,-1.264545,-0.163733             -->  0
(779.) -0.512009,-1.05604,-0.75538,-0.615344,-0.301589,-0.531098              -->  0
(780.) -0.380573,-1.2841,-0.693955,-0.708036,-0.879363,-0.776008              -->  0
(781.) -0.723919,0.164761,-0.124841,0.154678,0.661368,-0.653553               -->  0
(782.) -0.265958,-0.455234,-0.750323,-0.297754,0.468776,0.081176              -->  0
(783.) -0.512009,-1.200184,-0.58789,-1.126637,-2.612685,-2.123013             -->  0
(784.) -0.512009,-1.378532,-0.494053,-0.693524,0.276185,0.938361              -->  0
(785.) -0.265958,-1.486497,-0.710773,-0.747892,-0.879363,-1.633193            -->  0
(786.) -0.611721,-2.5928,-2.453482,-2.40412,-1.457137,-1.265828               -->  0
(787.) -1.384118,-0.096942,-1.605791,-0.372556,0.661368,-0.408643             -->  0
(788.) -0.164344,-0.761144,-0.505799,-1.663692,-1.071954,-0.898463            -->  0
(789.) -1.207985,-0.993131,-0.73035,-0.519136,1.239142,-0.653553              -->  0
(790.) -0.340719,-0.935066,-1.144888,-1.142125,-0.49418,-0.898463             -->  0
(791.) -0.196953,-1.684442,-1.455966,-1.705906,-1.842319,-0.776008            -->  0
(792.) -0.30256,-1.612534,-0.708353,-0.660525,-1.264545,-1.020918             -->  0
(793.) -1.001904,-1.161485,-0.199962,0.074844,-0.301589,-0.163733             -->  0
(794.) -0.132878,-1.763933,-1.235362,-1.103882,-1.649728,-0.041278            -->  0
(795.) -0.611721,-1.089577,-0.376746,-1.165856,-0.879363,-1.143373            -->  0
(796.) -0.230792,-1.378532,-1.508846,-1.572119,1.239142,0.693451              -->  0
(797.) -0.785761,-0.65763,-0.334455,-0.428422,0.276185,-0.531098              -->  0
(798.) -0.512009,-1.05604,-0.969666,-0.794891,-0.49418,0.448541               -->  0
(799.) -0.044609,-2.375753,-1.661242,-1.488829,-0.879363,-0.408643            -->  0
(800.) -0.466024,-1.612534,-2.656588,-2.40412,0.661368,1.183271               -->  0
(801.) -2.320987,-1.32984,-1.264625,-0.844417,0.083594,-2.123013              -->  0
(802.) -1.390377,-1.124675,-0.609523,-0.890792,0.661368,0.815906              -->  0
(803.) -0.30256,-0.855575,-2.216074,-2.648968,-1.842319,0.448541              -->  0
(804.) -0.56048,-0.638529,-0.201409,0.337859,-0.108998,0.326086               -->  0
(805.) -0.340719,-1.430585,-0.873725,-1.004547,0.661368,-2.735287             -->  0
(806.) -0.611721,-2.207399,-1.768224,-1.879694,-1.071954,-1.633193            -->  0
(807.) -0.723919,-0.601718,-0.392425,-0.313507,-0.49418,-0.163733             -->  0
(808.) -1.001904,-0.358196,-0.527703,-0.655906,0.468776,-0.408643             -->  0
(809.) -0.785761,-1.240976,-0.638374,-0.978027,-0.686771,-1.755648            -->  0
(810.) -1.001904,-0.485416,-0.554231,-0.646737,0.468776,-0.163733             -->  0
(811.) -1.001904,-1.684442,-0.331149,-0.688737,-0.301589,-1.020918            -->  0
(812.) -1.087314,-0.500973,-0.223363,-0.156149,0.468776,0.203631              -->  0
(813.) -0.611721,-0.697348,-1.093615,-0.669834,-1.649728,-2.612832            -->  0
(814.) -0.666067,-1.763933,-2.3465,-2.467698,-0.879363,0.326086               -->  0
(815.) -0.852185,-1.2841,-1.079441,-1.126637,-1.264545,0.448541               -->  0
(816.) -0.723919,-0.619899,-0.541899,-1.215234,-1.071954,-0.653553            -->  0
(817.) -0.723919,-0.806883,-0.581491,-0.523116,1.624324,0.815906              -->  0
(818.) -0.611721,-1.953542,-1.719989,-1.735162,-1.457137,-2.245467            -->  0
(819.) -0.30256,-0.134673,-0.950954,-1.828956,-0.686771,0.448541              -->  0
(820.) -0.666067,-1.200184,-0.562539,-0.476448,0.083594,0.326086              -->  0
(821.) -0.56048,-1.763933,-0.802095,-1.02495,-0.301589,0.203631               -->  0
(822.) -0.611721,-0.144409,0.176501,-0.396582,-1.842319,-1.265828             -->  0
(823.) -0.422281,-1.161485,-0.834511,-0.669834,-0.49418,-0.653553             -->  0
(824.) -0.56048,-2.207399,-1.811528,-1.477522,0.083594,-1.633193              -->  0
(825.) -0.512009,-1.684442,-1.733532,-1.206819,-0.49418,-0.408643             -->  0
(826.) -0.852185,-1.05604,-0.003944,-0.197234,0.083594,1.060816               -->  0
(827.) -0.852185,-1.953542,-0.765572,-1.173904,-4.346006,-2.980197            -->  0
(828.) -1.001904,-0.935066,-1.376834,-1.705906,-0.49418,-0.408643             -->  0
(829.) -0.852185,-0.855575,-0.431832,-0.861535,0.083594,-0.776008             -->  0
(830.) -1.311075,-0.830836,-0.525692,-0.096509,0.276185,-0.531098             -->  0
(831.) -1.683435,-1.378532,-1.833913,-1.477522,1.624324,0.203631              -->  0
(832.) -0.380573,-1.486497,-1.420564,-1.65004,-2.034911,-2.612832             -->  0
(833.) -0.723919,-1.2841,-1.183212,-1.361522,-0.686771,-0.163733              -->  0
(834.) -0.666067,-1.05604,-0.457752,-0.487895,-1.457137,-1.510738             -->  0
(835.) -1.099039,-1.684442,-0.486299,-0.737765,-0.686771,-2.367922            -->  0
(836.) -1.115531,-0.371318,0.003143,-0.140215,-1.071954,-0.653553             -->  0
(837.) -1.147536,-2.069843,-1.34872,-0.827611,-0.108998,-0.898463             -->  0
(838.) -0.466024,-1.02393,-1.503429,-1.84556,-0.686771,0.693451               -->  0
(839.) -0.852185,-1.089577,-0.2293,-0.984586,-1.071954,-0.776008              -->  0
(840.) -1.478763,-1.32984,-1.214977,-0.838781,-1.649728,0.203631              -->  0
(841.) -0.466024,-1.430585,-0.698731,-1.547544,-2.420093,-2.245467            -->  0
(842.) -0.723919,-1.612534,-1.055115,-1.157877,-1.649728,0.326086             -->  0
(843.) -0.56048,-2.5928,-1.804178,-1.623327,-0.301589,-1.633193               -->  0
(844.) -0.512009,-1.953542,-1.719989,-1.371485,-0.301589,-0.286188            -->  0
(845.) -0.466024,-0.935066,-1.420564,-1.2323,0.083594,-1.388283               -->  0
(846.) -1.001904,-1.612534,-0.885221,-1.351667,-0.49418,0.570996              -->  0
(847.) -0.785761,-2.069843,-1.093615,-0.90276,-0.686771,-0.408643             -->  0
(848.) -1.001904,-0.65763,-0.174283,-0.763293,-0.879363,-0.898463             -->  0
(849.) -0.666067,-1.763933,-1.558984,-1.584657,-0.686771,-0.041278            -->  0
(850.) -0.666067,-2.5928,-1.740374,-2.609749,-1.457137,-0.408643              -->  0
(851.) -0.380573,-1.763933,-2.728519,-3.10644,-0.879363,0.203631              -->  0
(852.) -0.923924,-1.852797,-1.435581,-1.796619,-1.071954,-0.776008            -->  0
(853.) -0.666067,-1.02393,-1.789639,-1.623327,-0.301589,-0.163733             -->  0
(854.) -0.666067,-2.5928,-3.138741,-3.174731,-0.879363,0.938361               -->  0
(855.) -1.722595,-0.830836,-0.560456,-0.568077,0.468776,0.570996              -->  0
(856.) -1.155236,-1.612534,-1.100779,-0.693524,0.468776,0.326086              -->  0
(857.) -1.001904,-1.612534,-1.849123,-2.316291,-0.108998,0.326086             -->  0
(858.) -5.313454,-2.89871,-2.639394,-0.878977,1.04655,0.448541                -->  0
(859.) -1.686925,-0.806883,-0.768136,-0.188869,-0.301589,-0.408643            -->  0
(860.) -1.109082,-1.161485,-0.585752,-1.198479,-0.108998,-0.531098            -->  0
(861.) -1.143711,-1.200184,-2.439459,-3.10644,0.083594,0.326086               -->  0
(862.) -1.087314,-1.378532,-1.410678,-1.84556,0.468776,-0.041278              -->  0
(863.) -1.329666,-1.2841,-0.238274,-0.153474,-0.49418,-0.408643               -->  0
(864.) -0.785761,-1.953542,-2.162038,-2.467698,-1.457137,-0.531098            -->  0
(865.) -1.087314,-1.852797,-0.957152,-1.096421,-0.49418,1.305726              -->  0
(866.) -0.852185,-2.207399,-1.796882,-2.609749,-1.457137,-1.510738            -->  0
(867.) -0.923924,-1.763933,-2.141224,-2.139019,-1.457137,-3.225107            -->  0
(868.) -1.304201,-2.5928,-2.766548,-2.435361,-2.227502,-3.592472              -->  0
(869.) -1.879246,-0.283926,-1.219021,-0.461402,-0.108998,-0.286188            -->  0
(870.) -2.587342,-1.2841,-3.138741,-2.501211,0.468776,-0.531098               -->  0
(871.) -0.923924,-1.05604,-0.81817,-1.2323,-0.879363,-0.286188                -->  0
(872.) -0.852185,-0.144409,-0.665774,-1.584657,0.276185,0.570996              -->  0
(873.) -1.001904,-3.421667,-2.511653,-2.648968,-0.879363,0.326086             -->  0
(874.) -0.852185,-1.200184,-0.773285,-0.535162,-2.997867,-1.510738            -->  0
(875.) -1.174778,-2.069843,-1.141136,-1.597368,-3.960824,-3.714927            -->  0
(876.) -0.852185,-1.953542,-1.195004,-1.371485,-1.071954,0.203631             -->  0
(877.) -0.785761,-2.89871,-3.138741,-2.927523,-1.071954,-1.388283             -->  0
(878.) -1.37296,-0.398266,-0.765572,-1.004547,-0.49418,-0.041278              -->  0
(879.) -1.001904,-2.5928,-1.43055,-1.004547,-0.108998,-0.653553               -->  0
(880.) -1.29061,-1.486497,-0.941729,-0.597874,-1.071954,-1.388283             -->  0
(881.) -0.611721,-1.852797,-1.761188,-1.332266,0.276185,-0.041278             -->  0
(882.) -0.666067,-1.32984,-2.847296,-3.10644,-0.108998,-0.408643              -->  0
(883.) -1.329666,-2.069843,-1.30357,-1.65004,-0.879363,-2.000558              -->  0
(884.) -0.723919,-0.470174,-0.69634,-1.223728,-1.457137,-1.265828             -->  0
(885.) -1.001904,-0.533083,-0.533762,-0.624205,0.083594,-0.898463             -->  0
(886.) -0.611721,-1.546886,-1.235362,-1.572119,-1.649728,-1.388283            -->  0



Time taken to build model (full training data) : 0.05 seconds

=== Model and evaluation on training set ===

Clustered Instances

0      887 (100%)

````

## weka_kmeans.txt

Ruta: `DocumentoFinal/evidencias/weka_kmeans.txt` · Bytes: 1554 · SHA-256: `b6be17cf0eaf134d171be3850e8e4c683ef631592cb3e142195ae0358191983a`

````text
=== Run information ===

Scheme:       weka.clusterers.SimpleKMeans -init 0 -max-candidates 100 -periodic-pruning 10000 -min-density 2.0 -t1 -1.25 -t2 -1.0 -N 2 -A "weka.core.EuclideanDistance -R first-last" -I 500 -num-slots 1 -S 42
Relation:     clustering
Instances:    887
Attributes:   6
              Plays
              Playing
              Backlogs
              Wishlist
              Rating
              Metacritic Rating
Test mode:    evaluate on training data


=== Clustering model (full training set) ===


kMeans
======

Number of iterations: 9
Within cluster sum of squared errors: 76.63099068257982

Initial starting points (random):

Cluster 0: -0.196953,1.355243,0.909476,1.595141,0.276185,0.693451
Cluster 1: 0.261114,-0.830836,-0.259536,-0.237306,-1.264545,-0.531098

Missing values globally replaced with mean/mode

Final cluster centroids:
                                 Cluster#
Attribute            Full Data          0          1
                       (887.0)    (477.0)    (410.0)
====================================================
Plays                        0       0.41     -0.477
Playing                      0     0.6189      -0.72
Backlogs                     0     0.7093    -0.8252
Wishlist                    -0     0.6912    -0.8042
Rating                       0     0.4797    -0.5581
Metacritic Rating           -0      0.427    -0.4968




Time taken to build model (full training data) : 0.02 seconds

=== Model and evaluation on training set ===

Clustered Instances

0      477 ( 54%)
1      410 ( 46%)

````

