# Documento final

Compilar desde esta carpeta con `latexmk -pdf -interaction=nonstopmode main.tex`. Requiere LaTeX, biblatex APA y biber.

`ajustar_formato_redaccion.py` reconstruye la versión revisada usando el generador base y la plantilla original; la compilación de main.tex es autónoma con las figuras incluidas. Fecha de corte: 11 de noviembre de 2026. No se atribuye entrega formal ni publicación pública.

## Versión revisada con el formato del anteproyecto

El archivo vigente es `main.tex`, con portada en `Portada.tex` y escudos en `portada_img`. Su preámbulo procede de `Proyecto/main.tex`: conserva encabezados, márgenes, estilos del índice, numeración y espaciado del anteproyecto. La copia anterior se conserva en `version_anterior` y no es la versión vigente.

Para regenerar desde el workspace, ejecutar primero `Final/.venv/bin/python DocumentoFinal/analizar_escenarios.py` y después `python3 DocumentoFinal/ajustar_formato_redaccion.py`. Este último utiliza el generador base, restaura la plantilla y aplica la redacción y escenarios revisados. No ejecutar solo `generar_documento.py` para reconstruir la versión final: ese archivo es el generador base de la versión previa.

La compilación es autónoma: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` desde esta carpeta, sin regenerar nada. Requiere la distribución TeX y biber.

Los escenarios hipotéticos no tienen una clase real conocida; los contraejemplos corresponden a seis registros de la prueba histórica y se seleccionaron después de observar errores y aciertos. No constituyen una validación independiente. Los ocho escenarios y la rejilla se recalcularon con la MLP. La captura de la página Predicción documenta una ejecución del formulario. No se reentrenó ni cambió el modelo para acomodar los ejemplos.

## Cierre y revisión por otras IAs

El equipo declara cumplido el calendario técnico, sin asignar fechas exactas no registradas. La suite completa aprobó 102 pruebas en el cierre. Los logs históricos de cada carpeta se reúnen en BITACORA_UNIFICADA.md; los resultados cuantitativos y las capturas se conservan separados. El paquete REVISION_IA, en la raíz, contiene una ficha por carpeta con código y documentación para revisión.
