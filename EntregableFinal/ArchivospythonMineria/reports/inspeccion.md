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
