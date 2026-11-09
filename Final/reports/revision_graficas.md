# Corrección de gráficas e identidad visual

## Cifras e intervalos

Las líneas amarillas son barras de error y se conservan con sus desviaciones originales. Las etiquetas de CV se sitúan encima del extremo superior más 10 píxeles; las de permutación, a la derecha del extremo superior más 10 píxeles. Esto evita que una línea atraviese el valor numérico sin desplazar los datos.

La leyenda comparativa pasa debajo del gráfico para liberar ancho. La matriz y la importancia por permutación usan ancho completo para mantener legibles sus títulos y etiquetas; los rangos estadísticos originales permanecen intactos.

## Ejes logarítmicos

Se conservan los conteos y la escala logarítmica. Se muestran etiquetas en potencias de diez y se ocultan las marcas menores que se amontonaban; cambiar la densidad de etiquetas no transforma los valores.

## Identidad del documento adjunto

La paleta se centraliza en `src/visualizacion.py` y genera variables CSS compartidas. Se aplica en Inicio, Exploración, Predicción y Modelo, conservando la tipografía cómic, las rutas y la navegación existentes.

Plays usa cian; Backlogs, violeta; Wishlist, dorado. Los paneles y gráficos combinan azul marino y morado; la matriz usa una escala de oscuro a claro y texto de contraste adaptado al valor de cada celda.

En pantallas estrechas, las figuras densas conservan un ancho de lectura de 760 px con desplazamiento horizontal dentro de su panel. Se comprobó que el documento mantiene el ancho del viewport de 390 px.

## Archivos de implementación modificados

- `src/visualizacion.py`: nuevo módulo de tokens y etiquetas fuera de intervalos.
- `src/ui.py`: tema Plotly y generación de variables CSS.
- `assets/css/persona5.css`: colores, paneles, foco y contenedores responsivos.
- `app.py`: colores de la página de inicio y versión del tema.
- `pages/1_Exploracion.py`: paleta de señales y boxplots.
- `pages/2_Prediccion.py`: paleta y énfasis cian en el resultado.
- `pages/3_Acerca_del_modelo.py`: intervalos, leyenda, matriz y distribución de figuras.
- `tests/test_visualizacion.py`: comprobaciones de integridad de datos y escalas en la presentación.

## Verificaciones ejecutadas

- 21 pruebas aprobadas: pruebas de visualización y pruebas existentes de pipeline/páginas. Registro: `tables/pruebas_revision_visual.txt`.
- SHA-256 de 20 archivos en `data/raw`, `data/clean` y `models`: todos idénticos antes y después. Evidencias: `tables/integridad_visual_antes.json` y `tables/integridad_visual_resultado.json`.
- Inspección de Inicio, Exploración, Predicción y Modelo en el navegador.
- Selector de señal de Exploración cambiado a Wishlist: estado seleccionado y gráfica actualizados.
- Barras comparativas y permutación: cifras separadas de los intervalos; títulos legibles.
- Gráficas logarítmicas: etiquetas mayores legibles, sin dígitos menores encimados.
- Comprobación móvil: figura de 760 px desplazable dentro del documento de 390 px; cifras visibles al desplazar el panel.
- Compilación Python y comprobación de espacios en el diff: correctas.

El detector de diseño señala bordes inclinados y una curva de animación que ya pertenecían al tema Persona. Se conservan por la indicación de mantener esa identidad; no son errores en las mediciones.

Las visualizaciones Plotly dinámicas y su exportación usan el tema actualizado. No se regeneran las figuras históricas de los reportes de análisis: esta revisión se limita a la presentación de la web y no vuelve a entrenar modelos.

Sin pendientes.
