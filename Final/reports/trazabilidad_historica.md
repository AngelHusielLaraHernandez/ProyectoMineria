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
