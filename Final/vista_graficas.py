"""Presentación adaptable para las gráficas de Streamlit."""

import streamlit as st

from src.ui import p5_plotly_layout


def mostrar_grafica(figura, titulo, *, alto=400, **opciones):
    """Coloca el título fuera del lienzo para que pueda ajustarse al ancho."""
    st.subheader(titulo)
    p5_plotly_layout(figura, height=alto)
    figura.update_layout(
        margin=dict(l=20, r=18, t=20, b=40),
        legend=dict(orientation='h', x=0, y=-0.23, yanchor='top', font_size=11),
    )
    figura.update_xaxes(title_font_size=13, tickfont_size=11)
    figura.update_yaxes(title_font_size=13, tickfont_size=11)
    config = dict(displaylogo=False, responsive=True, modeBarButtonsToRemove=['toImage'])
    return st.plotly_chart(figura, width='stretch', config=config, **opciones)
