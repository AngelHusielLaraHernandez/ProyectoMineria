# Documento final

El [PDF](main.pdf) usa la plantilla del anteproyecto. Explica las gráficas, los resultados de Random Forest y Weka, y la configuración del formulario de predicción con capturas de la web vigente. La bibliografía usa biblatex con estilo APA.

Las secciones 4.1 y 4.2 incorporan evidencia publicada por las editoras y el diseño para evaluar pérdidas por género. El datasheet del apéndice A describe el catálogo y sus cambios. La [tabla de evidencia comercial](tablas/evidencia_comercial.csv) se incluye en el paquete LaTeX.

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
