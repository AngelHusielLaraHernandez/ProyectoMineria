# Documento final

El [PDF](main.pdf) se compila con la plantilla del anteproyecto. Incluye las pruebas estadísticas, los resultados de Random Forest, las corridas gráficas de Weka, los escenarios de predicción y el plan respaldado por fechas de Git. La bibliografía usa biblatex con estilo APA.

## Compilar

Desde esta carpeta, con LaTeX y biber instalados:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Regenerar desde el repositorio local

Desde la raíz, con el entorno Python de Final activo:

```bash
Final/.venv/bin/python DocumentoFinal/analizar_escenarios.py
python3 DocumentoFinal/ajustar_formato_redaccion.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd DocumentoFinal/main.tex
python3 herramientas/empaquetar_documento.py
```

Las tablas se alimentan de `Final/reports/tables/` y `Final/models/metadata.json`. Los escenarios son hipotéticos y los contraejemplos proceden de la prueba histórica ya observada. El registro de Git acredita la primera evidencia disponible, con independencia de cuándo se terminó cada actividad. La aplicación se ejecuta localmente.
