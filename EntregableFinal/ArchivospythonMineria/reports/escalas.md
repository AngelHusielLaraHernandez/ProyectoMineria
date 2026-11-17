# Evidencia documental de escalas

## Escalas verificadas antes de calcular la brecha

Consulta de documentación primaria: **8 de noviembre de 2026**. No se reemplazaron notas ni conteos del CSV por valores actuales del sitio.

- [Backloggd: página oficial de Elden Ring](https://backloggd.com/games/elden-ring/) muestra la media junto al gráfico de estrellas cuyo extremo superior es **5 estrellas**. [Su FAQ](https://backloggd.com/about/) distingue la media del juego y el promedio ponderado utilizado para ordenar. Esta evidencia respalda el denominador cinco; no prueba por sí sola cómo se extrajo cada fila histórica.
- [Metacritic: interpretación del Metascore](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore) documenta una escala de **0–100** para prensa.
- Los rangos del CSV son compatibles con esas escalas. El derivado heredado `rating_100` coincide con multiplicar por 20, pero se usa solo como corroboración y no como prueba independiente de la escala.

Se aplicará una conversión por el máximo documentado: `rating_normalizado = Rating / 5 × 100`; `brecha = rating_normalizado − Metacritic Rating` solo cuando la nota crítica tenga procedencia válida según el maestro.
No se usa normalización min–max de la muestra: convertir 0.7 y 4.8 en los extremos produciría una brecha dependiente de los juegos incluidos. La conversión tampoco afirma equivalencia psicométrica entre ambas plataformas.

