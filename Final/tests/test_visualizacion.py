"""Verifica que la presentación conserve datos, errores y escalas."""
import plotly.graph_objects as go
import pytest
from src.visualizacion import etiquetas_fuera_del_error, COLOR_SENALES


def test_etiqueta_vertical_separa_error_sin_cambiar_datos():
    fig = go.Figure(go.Bar(x=['NB', 'RF'], y=[.549, .557], error_y=dict(array=[.06, .04])))
    fig.update_yaxes(range=[0, .72])
    etiquetas_fuera_del_error(fig, desplazamiento_categoria=-.8/3)
    assert list(fig.data[0].y) == [.549, .557]
    assert list(fig.data[0].error_y.array) == [.06, .04]
    assert list(fig.layout.yaxis.range) == [0, .72]
    assert fig.layout.annotations[0].y == pytest.approx(.609)
    assert fig.layout.annotations[0].x == pytest.approx(-.8/3)
    assert fig.layout.annotations[0].yshift > 0


def test_etiqueta_horizontal_queda_despues_del_intervalo():
    fig = go.Figure(go.Bar(x=[.0833], y=['Rating'], orientation='h', error_x=dict(array=[.022])))
    fig.update_xaxes(range=[0, .115])
    etiquetas_fuera_del_error(fig, sufijo=' F1')
    etiqueta = fig.layout.annotations[0]
    assert etiqueta.x == pytest.approx(.1053)
    assert etiqueta.xanchor == 'left' and etiqueta.xshift > 0
    assert etiqueta.text == '0.0833 F1'
    assert list(fig.data[0].x) == [.0833]
    assert list(fig.data[0].error_x.array) == [.022]
    assert list(fig.layout.xaxis.range) == [0, .115]


def test_colores_semanticos_consistentes():
    assert COLOR_SENALES == {'Plays': '#00CFFF', 'Backlogs': '#8B9CFF', 'Wishlist': '#FFD166'}


def test_tema_logaritmico_conserva_escala_datos_y_rango():
    from src.ui import p5_plotly_layout
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[10, 100, 1000]))
    fig.update_yaxes(type='log', range=[1, 3])
    p5_plotly_layout(fig, title='Comprobación de escala')
    assert fig.layout.yaxis.type == 'log'
    assert fig.layout.yaxis.dtick == 1
    assert list(fig.layout.yaxis.range) == [1, 3]
    assert list(fig.data[0].y) == [10, 100, 1000]


def test_p5_plotly_layout_usa_font_sans_y_margen_superior_minimo():
    from src.ui import p5_plotly_layout
    from src.visualizacion import FONT_SANS

    fig_sin_titulo = p5_plotly_layout(go.Figure(go.Scatter(x=[1, 2], y=[3, 4])), title='')
    assert fig_sin_titulo.layout.margin.t >= 44
    assert fig_sin_titulo.layout.font.family == FONT_SANS
    assert fig_sin_titulo.layout.title.font.family == FONT_SANS
    assert fig_sin_titulo.layout.legend.font.family == FONT_SANS
    assert fig_sin_titulo.layout.hoverlabel.font.family == FONT_SANS
    assert fig_sin_titulo.layout.xaxis.tickfont.family == FONT_SANS
    assert fig_sin_titulo.layout.xaxis.title.font.family == FONT_SANS
    assert fig_sin_titulo.layout.yaxis.tickfont.family == FONT_SANS
    assert fig_sin_titulo.layout.yaxis.title.font.family == FONT_SANS

    titulo_largo = 'Distribución comparativa de señales de popularidad en el catálogo completo'
    fig_con_titulo = p5_plotly_layout(go.Figure(go.Bar(x=['A'], y=[1])), title=titulo_largo)
    assert fig_con_titulo.layout.margin.t >= 48 >= 44
    assert fig_con_titulo.layout.font.family == FONT_SANS


def test_vista_graficas_mostrar_grafica_preserva_fuente_margen_y_toimage(monkeypatch):
    import vista_graficas
    from src.visualizacion import FONT_SANS

    capturado = {}
    monkeypatch.setattr(vista_graficas.st, 'subheader', lambda texto: capturado.setdefault('titulo', texto))
    monkeypatch.setattr(
        vista_graficas.st,
        'plotly_chart',
        lambda fig, **kwargs: capturado.update({'fig': fig, 'kwargs': kwargs}) or 'ok',
    )

    fig = go.Figure(go.Bar(x=[10, 20], y=['A', 'B'], orientation='h'))
    resultado = vista_graficas.mostrar_grafica(fig, 'Gráfica de prueba', alto=390)

    assert resultado == 'ok'
    assert capturado['titulo'] == 'Gráfica de prueba'
    fig_out = capturado['fig']
    assert fig_out.layout.font.family == FONT_SANS
    assert fig_out.layout.xaxis.tickfont.family == FONT_SANS
    assert fig_out.layout.yaxis.tickfont.family == FONT_SANS
    assert fig_out.layout.xaxis.automargin is True
    assert fig_out.layout.yaxis.automargin is True
    assert fig_out.layout.margin.t >= 48 >= 44
    assert fig_out.layout.legend.font.size == 12
    config = capturado['kwargs']['config']
    assert config['displaylogo'] is False
    assert config['responsive'] is True
    assert 'toImage' not in config.get('modeBarButtonsToRemove', [])
