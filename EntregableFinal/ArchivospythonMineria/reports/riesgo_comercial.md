# Riesgo comercial, género y juegos como servicio

La [tabla de evidencia comercial](tables/evidencia_comercial.csv) recoge casos documentados por sus editoras. La selección busca mostrar resultados distintos y depende de qué se hizo público. Permite describir cierres, reembolsos, ventas reportadas y efectos en estudios. Para estimar una tasa de fracaso haría falta una cohorte seleccionada antes de conocer su desempeño y un resultado financiero comparable por juego. Las estimaciones financieras heredadas de `games_curated.csv` no se usan para este propósito.

## Comparación por género

Definir una cohorte de lanzamientos, con reglas de inclusión por plataforma y periodo, antes de consultar resultados. Registrar `id_juego`, versión, género, condición GaaS documentada, plataforma, año, presupuesto inicial, tamaño del estudio y pertenencia a una franquicia. Para la condición GaaS se pueden documentar temporadas, operación continua y monetización recurrente, conservando el estado desconocido donde falte evidencia.

Para cada juego, registrar el ingreso neto atribuible al título durante los primeros 24 meses y los costos de desarrollo, marketing y operación imputables hasta ese corte, en moneda y alcance contable compatibles. Conservar la fuente, la fecha, el periodo y la cobertura de cada cifra. Un juego se etiqueta como pérdida cuando los ingresos quedan por debajo de los costos. Si falta alguno de esos importes, el resultado financiero se conserva como desconocido. El cierre del servicio puede estudiarse aparte como un evento operativo.

Comparar las tasas entre géneros dentro de grupos comparables en plataforma, año, presupuesto, tamaño de estudio y franquicia. Estimar diferencias con intervalos de confianza y examinar cuánto varía el resultado al restringir el análisis a GaaS. El resultado de una comparación observacional ajustada sigue sujeto a factores omitidos. La atribución causal requiere un diseño que permita aislar el efecto de la elección del género.

## Decisiones de inversión

Para un modelo de riesgo, usar resultados financieros históricos como etiquetas e información disponible antes de aprobar cada proyecto como entradas. Evaluar el desempeño en lanzamientos posteriores. Medir pérdidas evitadas exigiría además comparar las decisiones apoyadas por el modelo con las que se toman mediante el proceso habitual y seguir los resultados financieros de ambos grupos.
