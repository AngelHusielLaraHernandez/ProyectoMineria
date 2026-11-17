# Archivos Python de minería de datos

Los módulos mantienen sus nombres dentro de `src/` para conservar sus importaciones. La tabla permite localizar el código de cada parte.

| Grupo | Archivos | Qué hace |
| --- | --- | --- |
| Inspección y preparación | `01_inspeccion.py`, `02_limpieza.py`, `procedencia.py` | Revisa coberturas, escalas, fechas y duplicados. Prepara el catálogo depurado y la tabla larga de géneros. |
| Correlación y grupos | `03_clustering.py`, `metodos_clase.py`, `analisis_integral.py` | Calcula Pearson y Spearman. Compara K-Means, DBSCAN y Ward, proyecta con PCA y revisa GMM mediante BIC. |
| Clasificación | `04_modelo.py`, `objetivo.py`, `features.py`, `evaluacion_anidada.py` | Construye los niveles de popularidad y prepara las entradas. Compara la referencia mayoritaria, Naive Bayes categórico, árbol CART, Random Forest y MLP. |
| Calibración y revisión | `calibracion.py`, `05_revision_predicciones.py`, `reports/verificar_integridad.py` | Ajusta probabilidades mediante escalado de temperatura y comprueba las predicciones y los artefactos. |
| Comparación con Weka | `comparar_weka.py`, `comparativo_integral.py`, `reports/revision_predicciones/verificar_weka.py`, `reports/tables/evaluar_comparabilidad.py` y `test_comparabilidad.py` | Ejecuta la comparación de K-Means por consola, valida las corridas guardadas y recalcula las métricas de clasificación. |
| Escenarios del informe | `escenarios/analizar_escenarios.py` | Genera los escenarios de sensibilidad y los ejemplos de aciertos y errores con el modelo incluido. |
| Consulta de predicciones | `inferencia.py`, `similitud.py`, `lectura_prediccion.py` | Recibe los datos del formulario, calcula las probabilidades, busca cinco vecinos y redacta la lectura del resultado. |
| Orquestación y soporte | `pipeline.py`, `run_all.py`, `config.py`, `data.py`, `analysis.py`, `modeling.py`, `ui.py`, `visualizacion.py`, `portadas.py`, `__init__.py` | Define rutas y entradas, orquesta las fases y conecta los resultados con la interfaz. La entrada de Streamlit y las páginas están en DemoMineriaWeb. |

## Ejecutar fases por separado

Trabaja desde una copia de esta carpeta. Cada fase vuelve a escribir sus resultados en `data/clean/`, `models/` o `reports/`, según corresponda.

Crea un entorno con Python 3.14 siguiendo la [guía de instalación](../DemoMineriaWeb/README.md), pero desde la carpeta de análisis. En macOS/Linux activa el entorno con `source entorno/bin/activate`. En PowerShell puedes sustituir `python` en cada comando por `.\entorno\Scripts\python.exe`.

```text
python -m pip install -r requirements.txt
python -X utf8 -m src.01_inspeccion
python -X utf8 -m src.02_limpieza
python -X utf8 -m src.03_clustering
python -X utf8 -c "from src.metodos_clase import evaluar_ward; evaluar_ward()"
python -X utf8 -m src.analisis_integral
python -X utf8 -m src.04_modelo
python -X utf8 -m src.05_revision_predicciones --solo-integridad
```

La fase 04 vuelve a entrenar los modelos con validación cruzada y puede tardar. Para comprobar solo el modelo incluido, ejecuta directamente el último comando sobre esta carpeta, antes de regenerar los datos. Los reportes y tablas originales se pueden consultar sin ejecutar las fases.

Para volver a generar los escenarios del informe, ejecuta `python -X utf8 escenarios/analizar_escenarios.py`. El script conserva el método original y guarda sus gráficas dentro de `escenarios/`.

La guía de [Weka](../Weka/README.md) indica qué entradas y salidas copiar a la carpeta de análisis para ejecutar las comprobaciones que cruzan ambos programas.
