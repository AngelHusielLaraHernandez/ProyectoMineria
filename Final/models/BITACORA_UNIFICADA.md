# Modelos guardados

- El bosque aleatorio se carga en la web con sus metadatos. El archivo de vecinos se usa para mostrar ejemplos comparables del entrenamiento.
- La web aplica escalado de temperatura a las probabilidades del bosque. El ajuste usa predicciones fuera de pliegue de 892 juegos de entrenamiento. En 222 juegos de prueba, Brier pasó de 0.5570 a 0.5508 y log-loss de 0.9274 a 0.9102. Los metadatos guardan la temperatura y las métricas de la web. La tabla `calibracion_ajustada.csv` guarda los puntos de la curva ajustada por nivel.
