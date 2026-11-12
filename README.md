# Proyecto de minería de datos: videojuegos

La implementación vigente está en **Final/** y el documento de entrega en **DocumentoFinal/**. Todo se conserva localmente en la rama main; no hay publicación ni subida de datos.

- [Guía de ejecución de la web y del pipeline](Final/README.md).
- [Documento LaTeX y compilación](DocumentoFinal/README.md).
- [PDF final](DocumentoFinal/main.pdf).
- [Índice para revisión por otras IAs](REVISION_IA/INDICE.md).
- [Registro consolidado de cierre](Final/reports/BITACORA_UNIFICADA.md).

Desde la raíz, ejecuta `Final/.venv/bin/python -m streamlit run Final/app.py` para abrir la web. El entorno validado es Python 3.14.6 y el modelo activo es Random Forest. La [evaluación externa de los cinco modelos](Final/reports/tables/comparativo_modelos.csv), la [prueba del bosque](Final/reports/tables/metricas_prueba.csv) y los [metadatos](Final/models/metadata.json) respaldan las cifras del informe.

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
| REVISION_IA | Un documento por carpeta, con fuentes de texto e inventario de binarios. |

## Criterio de limpieza

Los logs y auditorías de texto se reúnen, conservando contenido y procedencia, en una BITACORA_UNIFICADA.md por carpeta. Los reportes analíticos vigentes, tablas, JSON de resultados, capturas y salidas originales de Weka permanecen como evidencia verificable. El log de limpieza se conserva por ser una salida contractual del pipeline. No se modifican data/raw ni los modelos para ordenar la entrega.

La publicación pública permanece sin autorización. Orange no tiene resultados y su descarte queda documentado. Los archivos de revisión por IA se generan con `python3 herramientas/preparar_revision_ia.py`; la consolidación se repite con `python3 herramientas/consolidar_bitacoras.py`.
