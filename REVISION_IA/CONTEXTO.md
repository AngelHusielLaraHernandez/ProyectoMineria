# Carpeta: .

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## .gitignore

Ruta: `.gitignore` · Bytes: 854 · SHA-256: `aad6d0d5ba7ea3f16c751406489e0b2cdc75d3c49a272c4211ce3ebc46f6a215`

````text
# Archivos generados por LaTeX
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.lof
*.log
*.lot
*.out
*.run.xml
*.synctex.gz
*.toc
*.xdv

# Bibliografía y archivos auxiliares generados
*-blx.bib

# Documento compilado
*.pdf
!DocumentoFinal/main.pdf
!DocumentoFinal/evidencias/rubrica_proyecto.pdf

# Intermedios de revisión y preferencias locales; las evidencias finales sí se conservan.
DocumentoFinal/revision/cache_matplotlib/
DocumentoFinal/revision/revisada/*.png
Final/reports/revision_predicciones/render_documento/
Final/reports/weka/.home/
Final/reports/weka/.preferencias/

# Archivos temporales de editores y del sistema
.DS_Store
.idea/
.vscode/
*.swp
*.swo
*~

# Claves y respuestas crudas de APIs
.env
Proyecto/data/external/
.venv/
.venv314/
__pycache__/
.pytest_cache/
.cache/
node_modules/
.streamlit/secrets.toml
.repositorios_locales/

````

## README.md

Ruta: `README.md` · Bytes: 2234 · SHA-256: `7bbaa11ec0377d49bf7940581098710baeffb688a504300a6d5691f462f25068`

````text
# Proyecto de minería de datos: videojuegos

La implementación vigente está en **Final/** y el documento de entrega en **DocumentoFinal/**. Todo se conserva localmente en la rama main; no hay publicación ni subida de datos.

- [Guía de ejecución de la web y del pipeline](Final/README.md).
- [Documento LaTeX y compilación](DocumentoFinal/README.md).
- [PDF final](DocumentoFinal/main.pdf).
- [Índice para revisión por otras IAs](REVISION_IA/INDICE.md).
- [Registro consolidado de cierre](Final/reports/BITACORA_UNIFICADA.md).

Desde Final, ejecutar `.venv/bin/python -m streamlit run app.py` para la web y `.venv/bin/python -m pytest -q` para las pruebas. La suite de cierre tiene 101 pruebas aprobadas. El equipo declara cumplido el calendario técnico; no se inventan fechas exactas de terminación.

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

````

