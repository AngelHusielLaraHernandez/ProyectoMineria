# Pearson usuarios vs. crítica: antes y después de depurar

Generado por `src/curate.py` con los datos del repositorio.

| Escenario | N pares | Pearson r | Media de la brecha (rating×20 − Metacritic) |
|---|---|---|---|
| 1. Crudo (1,512, con duplicados y estimados) | 1499 | 0.6193 | -8.97 |
| 2. Limpio (1,117, con estimados) | 1104 | 0.6002 | -9.18 |
| 3. Solo estimados en crudo | 261 | 0.9985 | -8.72 |
| 4. Solo estimados en limpio | 214 | 0.9986 | -9.12 |
| 5. Crudo, solo Metacritic real | 1238 | 0.5740 | -9.02 |
| 6. Limpio, solo Metacritic real (línea base) | 890 | 0.5444 | -9.20 |

## Hallazgo sobre los estimados
En las 261 filas estimadas con Rating, Metacritic ≈ 8.5851·Rating + 50.9504 (residuo máximo tras redondear con estos coeficientes: 0.0). No es una calificación de crítica independiente: es una función del Rating y se marca con `metacritic_real = False` y `critic_score_final = NaN` para excluirla de la comparación usuarios–crítica.
