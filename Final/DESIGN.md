# Interfaz del Observatorio de Videojuegos (Identidad Persona 5 accesible)

Modo: consulta e inferencia académica con temática visual oscura Persona 5 (azul medianoche y neón cian/morado). La navegación principal reside exclusivamente en la barra lateral personalizada (`showSidebarNavigation = false` en `.streamlit/config.toml`), con encabezados semánticos y tareas delimitadas por página.
Las tablas, selectores y formularios conservan la semántica nativa, teclado, foco visible (`:focus-visible` sin recorte de `clip-path`) y adaptación responsiva de Streamlit. Los gráficos muestran unidades, marcadores/símbolos diferenciados y margen superior suficiente para no quedar cubiertos por la barra de herramientas.

## Tokens y tipografía

- **Tipografía**: `'ComicProyecto'` (`Persona5main.ttf`) reservada exclusivamente para encabezados display (`.p5-banner-title`, `.p5-hero-title`, `.sc-role`, `.p5-row`); `sans-serif` del sistema con `tabular-nums` en cuerpo, tablas, formularios, tarjetas KPI y ejes/hover de Plotly.
- **Paleta y contraste WCAG AA (>= 4.5:1)**:
  - Fondo principal `#050D22`, panel `#15254A`, lienzo de gráficas `#170D37` / `#100B29`.
  - Acento cian neón `#00CFFF` sobre fondos oscuros (10.46:1); variante `#0E7490` para rellenos interactivos con texto blanco (`primaryColor` en `config.toml`, 5.36:1) y cifras sobre fondos claros (5.01:1).
  - Acentos secundarios `#8B9CFF`, `#A56BFF`, `#3B2386` (gradiente de banners), `#FFD166`, texto `#F5F7FF` y secundario `#C8CDEB`.
- **Movimiento y preferencias del sistema**: Transiciones de página ejecutadas únicamente al cambiar de vista (`session_state`), animaciones activadas de forma explícita con `@media (prefers-reduced-motion: no-preference)`, barras de desplazamiento adaptadas (`scrollbar-color`, `scrollbar-width: auto`, `scrollbar-gutter: stable`) y soporte para `@media (prefers-contrast: more)` y `@media (forced-colors: active)`.

## Estados y evidencia

Filtros con estado vacío; errores de preparación con recuperación explícita (`CRITICAL ALERT / MISSION FAILED`); audio unificado y accesible en la barra lateral sin paneles flotantes superpuestos; predicción solicitada mediante formulario.
Se prueban las cuatro páginas, búsqueda vacía, caché de recursos y predicción con valores ausentes mediante `AppTest` y `pytest`.
