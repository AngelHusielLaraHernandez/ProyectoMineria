"""Presentación adaptable para las gráficas de Streamlit."""

import streamlit as st

from src.ui import p5_plotly_layout

_MOD_VERSION = 'p5-v14-menu'


def mostrar_grafica(figura, titulo, *, alto=400, **opciones):
    """Coloca el título fuera del lienzo y aplica el tema accesible de Plotly."""
    st.subheader(titulo)
    p5_plotly_layout(figura, height=alto)
    top_margin = max(48, getattr(figura.layout.margin, 't', None) or 48)
    figura.update_layout(
        margin=dict(l=52, r=24, t=top_margin, b=64),
        legend=dict(orientation='h', x=0, y=-0.22, yanchor='top', font_size=12),
    )
    figura.update_xaxes(automargin=True)
    figura.update_yaxes(automargin=True)
    config = dict(displaylogo=False, responsive=True)
    return st.plotly_chart(figura, width='stretch', config=config, **opciones)
