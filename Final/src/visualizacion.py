"""Tokens y etiquetas compartidos; no transforma datos ni escalas estadísticas."""

_MOD_VERSION = 'p5-v14-menu'

PALETA = {
    'bg-primary': '#050D22', 'bg-panel': '#15254A',
    'bg-chart': '#170D37', 'bg-chart-deep': '#100B29',
    'primary': '#00CFFF', 'primary-dark': '#0E7490',
    'secondary': '#8B9CFF',
    'purple-neon': '#A56BFF', 'purple-deep': '#6D42D8',
    'purple-banner': '#3B2386',
    'accent': '#FFD166', 'text-primary': '#F5F7FF',
    'text-secondary': '#C8CDEB', 'border-primary': '#00CFFF',
    'border-purple': '#A56BFF', 'grid-color': 'rgba(165, 107, 255, 0.36)',
}
FONT_SANS = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
COLOR_SENALES = {'Plays': PALETA['primary'], 'Backlogs': PALETA['secondary'], 'Wishlist': PALETA['accent']}
COLORWAY = [PALETA[k] for k in ('primary', 'secondary', 'accent', 'purple-neon', 'purple-deep')]


def etiquetas_fuera_del_error(fig, indice_traza=0, desplazamiento_categoria=0.0, sufijo=''):
    """Ubica cada cifra más allá del extremo positivo de su barra de error.

    El desplazamiento categórico reproduce la posición del grupo de barras;
    los 10 píxeles adicionales separan texto e intervalo a cualquier escala.
    """
    traza = fig.data[indice_traza]
    horizontal = traza.orientation == 'h'
    valores = traza.x if horizontal else traza.y
    categorias = traza.y if horizontal else traza.x
    error = traza.error_x if horizontal else traza.error_y
    errores = error.array if error.array is not None else [0.0] * len(valores)
    traza.text = None
    for i, (valor, categoria, desviacion) in enumerate(zip(valores, categorias, errores)):
        extremo = float(valor) + float(desviacion)
        etiqueta = f'{float(valor):.4f}{sufijo}' if horizontal else f'{float(valor):.3f}{sufijo}'
        fig.add_annotation(
            x=extremo if horizontal else i + desplazamiento_categoria,
            y=categoria if horizontal else extremo,
            text=etiqueta, showarrow=False,
            xanchor='left' if horizontal else 'center',
            yanchor='middle' if horizontal else 'bottom',
            xshift=10 if horizontal else 0, yshift=0 if horizontal else 10,
            font=dict(family=FONT_SANS, size=13, color=PALETA['text-primary']),
            bgcolor=PALETA['bg-chart'], borderpad=2,
        )
    return fig
