# Carpeta: Final/reports/archivo_modelo_anterior/reports

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## comparacion_modelos.csv

Ruta: `Final/reports/archivo_modelo_anterior/reports/comparacion_modelos.csv` · Bytes: 188 · SHA-256: `461b85b883863f0d8af535702a0f7caa191be33accc19db96d5d3a8143dd6bb2`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## matriz_confusion.csv

Ruta: `Final/reports/archivo_modelo_anterior/reports/matriz_confusion.csv` · Bytes: 73 · SHA-256: `f82204bede4be9bf74d657477eb94d470d87647e8c0fb531801f968b910b71f2`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## metricas.json

Ruta: `Final/reports/archivo_modelo_anterior/reports/metricas.json` · Bytes: 1772 · SHA-256: `1f792b4dbee8cfb87e73c61c0f43ae298296062b84c262260596b53b154c7f55`

````text
{
  "modelo": "regresion_logistica",
  "n_entrenamiento": 892,
  "n_prueba": 222,
  "fuente": "games_curated.csv",
  "sha256_fuente": "b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd",
  "objetivo": "terciles_popularidad_independientes_de_clusters",
  "sha256_dataset_depurado": "f0448fccc82b140fec956d8522b8dfa675c029875029bca6f3f8b396a67a7652",
  "cortes_entrenamiento": [
    5.788354050778799,
    6.668765991343139
  ],
  "semilla": 42,
  "accuracy": 0.5675675675675675,
  "balanced_accuracy": 0.5736060910307899,
  "f1_macro": 0.5671726304637698,
  "f1_macro_base": 0.14918414918414918,
  "reporte": {
    "bajo": {
      "precision": 0.5588235294117647,
      "recall": 0.59375,
      "f1-score": 0.5757575757575758,
      "support": 64.0
    },
    "medio": {
      "precision": 0.5070422535211268,
      "recall": 0.43373493975903615,
      "f1-score": 0.4675324675324675,
      "support": 83.0
    },
    "alto": {
      "precision": 0.6265060240963856,
      "recall": 0.6933333333333334,
      "f1-score": 0.6582278481012658,
      "support": 75.0
    },
    "accuracy": 0.5675675675675675,
    "macro avg": {
      "precision": 0.5641239356764257,
      "recall": 0.5736060910307899,
      "f1-score": 0.5671726304637698,
      "support": 222.0
    },
    "weighted avg": {
      "precision": 0.5623295708641233,
      "recall": 0.5675675675675675,
      "f1-score": 0.5631566137895252,
      "support": 222.0
    }
  },
  "distribucion_entrenamiento": {
    "bajo": 298,
    "alto": 297,
    "medio": 297
  },
  "distribucion_prueba": {
    "medio": 83,
    "alto": 75,
    "bajo": 64
  },
  "python": "3.14.6",
  "sklearn": "1.9.1",
  "nota": "Modelo conservado tal como se evaluó; no reajustado con prueba. Probabilidades sin calibrar."
}
````

## validacion_cruzada.csv

Ruta: `Final/reports/archivo_modelo_anterior/reports/validacion_cruzada.csv` · Bytes: 911 · SHA-256: `dc52f71020f960a75ab688a268c529b5bf6298d0922831794276c9e5869b3cc2`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

