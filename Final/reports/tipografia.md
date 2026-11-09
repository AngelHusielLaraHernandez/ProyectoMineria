# Tipografía cómic de la web

Se usa `assets/fonts/Persona5main.ttf` mediante la familia CSS `ComicProyecto`. Los metadatos del archivo indican Comic Sans MS cursiva. La fuente contiene vocales acentuadas, ñ, ü y signos de apertura españoles; se conserva el texto Unicode en lugar de eliminar sus tildes.

La fuente se integra localmente en CSS, sin descargar tipografías externas. La caché depende de los hashes del CSS y de los bytes de la fuente para que una sustitución del archivo se refleje al recargar la aplicación.

Se aplica a títulos, menús, párrafos, formularios y configuración tipográfica de Plotly. Se conservan las fuentes de iconos y del código. Los valores de los deslizadores no se parten en líneas; los títulos reducen su tamaño en móvil y tienen margen frente al menú contraído.

## Verificaciones ejecutadas

- Compilación de los tres módulos Python modificados: correcta.
- Caracteres españoles y cifras comprobados con fontTools: presentes.
- Inicio y Predicción inspeccionados en navegador: fuente cómic visible, navegación operativa y tildes conservadas.
- Desplegable de década abierto y cerrado: opciones legibles.
- Valores 82 y 3.90 de los deslizadores: visibles completos en una línea.
- Inicio a 390 px: título legible, margen izquierdo de 40 px y ancho del documento igual al viewport, sin desbordamiento horizontal.
- Reinicio del servidor local para descartar la definición anterior de la fuente: completado.

Evidencias: `tables/tipografia_comic_inicio.jpg`, `tables/tipografia_comic_formulario.jpg` y `tables/tipografia_comic_movil.jpg`.
