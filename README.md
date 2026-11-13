# Proyecto de minería de datos: videojuegos

La implementación vigente está en **Final/** y el documento de entrega en **DocumentoFinal/**. Todo se conserva localmente en la rama main; no hay publicación ni subida de datos.

- [Guía de ejecución de la web y del pipeline](Final/README.md).
- [Documento LaTeX y compilación](DocumentoFinal/README.md).
- [PDF final](DocumentoFinal/main.pdf).
- [Paquete de revisión](REVISION_IA/Revision_IA.zip), con índice e inventario dentro del ZIP.
- [Registro consolidado de cierre](Final/reports/BITACORA_UNIFICADA.md).

Desde la raíz, ejecuta `Final/.venv/bin/python -m streamlit run Final/app.py` para abrir la web (o desde `Final/`: `.venv/bin/python -m streamlit run app.py`). El entorno validado es Python 3.14.6 y el modelo activo es Random Forest (`RandomForestClassifier`). Para correr las pruebas automatizadas ejecuta `cd Final && .venv/bin/python -m pytest -q`; para regenerar el pipeline completo ejecuta desde `Final/` cualquiera de los dos comandos equivalentes: `.venv/bin/python src/run_all.py` o `.venv/bin/python -m src.pipeline`. En el entorno local `Final/.venv` los paquetes de `site-packages` se reutilizaron sin conexión al índice PyPI (`pip check` pasa), por lo que `Final/.venv/bin/` no incluye wrappers CLI (`pytest`, `streamlit`) y debe usarse `python -m ...`.

La [evaluación externa de los cinco modelos](Final/reports/tables/comparativo_modelos.csv), la [prueba del bosque](Final/reports/tables/metricas_prueba.csv) y los [metadatos](Final/models/metadata.json) respaldan las cifras del informe. Las comparativas con Weka distinguen claramente **Weka 3.8.6 (CLI)** en `Final/src/comparar_weka.py` y **Weka 3.8.7 (Explorer GUI)** en `Final/reports/weka/` ([verificación Weka/Orange](Final/reports/verificacion_weka_orange.md) · [bitácora histórica](Final/reports/BITACORA_UNIFICADA.md)).

La [preparación para Streamlit Community Cloud](Final/reports/despliegue.md) recoge las comprobaciones de licencia y configuración para una eventual publicación autorizada.

## Organización

| Carpeta | Función |
|---|---|
| Final | Código vigente, web, datos, modelos, pruebas y evidencias Python/Weka. |
| DocumentoFinal | Fuente LaTeX, PDF, figuras, tablas y evidencias de la entrega. |
| Proyecto | Anteproyecto y antecedentes del trabajo; conserva la plantilla original. |
| Practicas | Prácticas de la materia, independientes de la aplicación final. |
| PruebasMenu y MenuVersion2 | Prototipos de interfaz conservados como antecedentes e incluidos directamente en main. |
| herramientas | Consolidación reproducible de bitácoras y preparación de la revisión por IA. |
| REVISION_IA | Un ZIP con una ficha por carpeta, las fuentes de texto y un inventario de binarios. |

## Criterio de limpieza

Cada carpeta con registros de trabajo tiene una `BITACORA_UNIFICADA.md`. Los informes analíticos, tablas, capturas y salidas de Weka respaldan los resultados. El log de limpieza se conserva porque el pipeline lo genera y lo verifica. La [bitácora de la raíz](BITACORA_UNIFICADA.md) registra los archivos retirados y dónde recuperar las versiones anteriores.

La publicación pública permanece sin autorización. Orange no tiene resultados y su descarte queda documentado. Los archivos de revisión por IA se generan con `python3 herramientas/preparar_revision_ia.py`; la consolidación se repite con `python3 herramientas/consolidar_bitacoras.py`.
