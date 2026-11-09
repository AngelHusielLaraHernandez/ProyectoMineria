# Entradas de las corridas gráficas

- clustering.csv: 887 casos completos elegibles, seis columnas, mismo espacio guardado de log1p de los cuatro conteos y StandardScaler de las seis variables. Sin ID, título ni etiquetas de cluster entre los atributos.
- clasificacion.csv: 892 casos de entrenamiento exterior, 52 atributos numéricos del preprocesador guardado y última columna nominal nivel_popularidad. No incluye los 222 casos reservados de prueba, IDs ni conteos del objetivo.
- Se conservaron valores y orden de las fuentes; procedencia.json contiene sus SHA-256. Los originales no se modifican.

Las corridas gráficas de CV sobre este CSV preprocesado no replican el ajuste del objetivo y del preprocesamiento dentro de cada fold que usa Python. Se registrará el protocolo de cada programa sin reinterpretar sus cifras. El preprocesamiento externo y la selección original de hiperparámetros del modelo quedan documentados; no se presentan estas corridas como evaluación independiente de la prueba de Python.

## Que debo verificar manualmente

- Clase nominal nivel_popularidad, última columna de clasificacion.csv.
- Normalización adicional y valores predeterminados de cada herramienta, y la definición de F1 que su interfaz muestre.
