# Carpeta: Final/data/export

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## README.md

Ruta: `Final/data/export/README.md` · Bytes: 1256 · SHA-256: `b6c0e9a51b285f279e5b5407b4fc931ee8dc3ab3237228d6decbb77ee2a01130`

````text
# Entradas de las corridas gráficas

- clustering.csv: 887 casos completos elegibles, seis columnas, mismo espacio guardado de log1p de los cuatro conteos y StandardScaler de las seis variables. Sin ID, título ni etiquetas de cluster entre los atributos.
- clasificacion.csv: 892 casos de entrenamiento exterior, 52 atributos numéricos del preprocesador guardado y última columna nominal nivel_popularidad. No incluye los 222 casos reservados de prueba, IDs ni conteos del objetivo.
- Se conservaron valores y orden de las fuentes; procedencia.json contiene sus SHA-256. Los originales no se modifican.

Las corridas gráficas de CV sobre este CSV preprocesado no replican el ajuste del objetivo y del preprocesamiento dentro de cada fold que usa Python. Se registrará el protocolo de cada programa sin reinterpretar sus cifras. El preprocesamiento externo y la selección original de hiperparámetros del modelo quedan documentados; no se presentan estas corridas como evaluación independiente de la prueba de Python.

## Que debo verificar manualmente

- Clase nominal nivel_popularidad, última columna de clasificacion.csv.
- Normalización adicional y valores predeterminados de cada herramienta, y la definición de F1 que su interfaz muestre.

````

## clasificacion.arff

Ruta: `Final/data/export/clasificacion.arff` · Bytes: 222285 · SHA-256: `487963cb9dcd5937ffe5ebb2135db544dfdf00d56223e8bf7c8fccd1ed46c0a9`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clasificacion.csv

Ruta: `Final/data/export/clasificacion.csv` · Bytes: 219278 · SHA-256: `f1040a9670bf08c0a717d39951971c3ec0335bf605b2b69b228f26b0d38c9908`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clasificacion.tab

Ruta: `Final/data/export/clasificacion.tab` · Bytes: 219913 · SHA-256: `aef344720fd3ae26f3de15cb607983beb5da44e289687fc640645ba8c3120130`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering.arff

Ruta: `Final/data/export/clustering.arff` · Bytes: 104463 · SHA-256: `17b890b65e6231eabd16a864cf8e3691394b9d203e5c5d80e61ea297df1dbbce`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## clustering.csv

Ruta: `Final/data/export/clustering.csv` · Bytes: 104242 · SHA-256: `9b0627ba170dba5eed9b1fc22fe02020d175f07d71addd91280279cfe43f8a1d`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## procedencia.json

Ruta: `Final/data/export/procedencia.json` · Bytes: 517 · SHA-256: `308b9b1ccdee3bb3893811e9f728558e1a0c7df999c4b0b4d1a6842102f09409`

````text
{
  "clustering.csv": {
    "fuente": "data/clean/clustering_espacio.csv",
    "sha256_fuente": "9b0627ba170dba5eed9b1fc22fe02020d175f07d71addd91280279cfe43f8a1d",
    "sha256_export": "9b0627ba170dba5eed9b1fc22fe02020d175f07d71addd91280279cfe43f8a1d"
  },
  "clasificacion.csv": {
    "fuente": "data/clean/entrenamiento_orange.csv",
    "sha256_fuente": "f1040a9670bf08c0a717d39951971c3ec0335bf605b2b69b228f26b0d38c9908",
    "sha256_export": "f1040a9670bf08c0a717d39951971c3ec0335bf605b2b69b228f26b0d38c9908"
  }
}
````

## procedencia_arff.json

Ruta: `Final/data/export/procedencia_arff.json` · Bytes: 721 · SHA-256: `c4f04f6eb9a09996254dbcf51015019e1b522963fe3b284cb25a9a1a3bc8691c`

````text
{
  "clustering": {
    "origen": "data/export/clustering.csv",
    "copia": "data/export/clustering.arff",
    "filas": 887,
    "atributos": 6,
    "valores_verificados": true,
    "sha256_csv": "9b0627ba170dba5eed9b1fc22fe02020d175f07d71addd91280279cfe43f8a1d",
    "sha256_arff": "17b890b65e6231eabd16a864cf8e3691394b9d203e5c5d80e61ea297df1dbbce"
  },
  "clasificacion": {
    "origen": "data/export/clasificacion.csv",
    "copia": "data/export/clasificacion.arff",
    "filas": 892,
    "atributos": 53,
    "valores_verificados": true,
    "sha256_csv": "f1040a9670bf08c0a717d39951971c3ec0335bf605b2b69b228f26b0d38c9908",
    "sha256_arff": "487963cb9dcd5937ffe5ebb2135db544dfdf00d56223e8bf7c8fccd1ed46c0a9"
  }
}

````

