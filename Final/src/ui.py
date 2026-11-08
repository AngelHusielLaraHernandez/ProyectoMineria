"""Carga compartida de artefactos para la aplicación."""
import json
import hashlib

import joblib
import pandas as pd
import sklearn
import streamlit as st

from .config import CLEAN, MODELS, REPORTS, RAW
from .data import load_clean


@st.cache_resource
def resources():
    metrics_path = REPORTS / 'metricas.json'
    # En el alojamiento se reconstruye si la versión de sklearn es distinta.
    rebuild = not (MODELS / 'popularidad.joblib').exists() or not metrics_path.exists()
    if not rebuild:
        metadata = json.loads(metrics_path.read_text(encoding='utf-8'))
        rebuild = (metadata['sklearn'] != sklearn.__version__ or
                   metadata.get('sha256_fuente') != hashlib.sha256(RAW.read_bytes()).hexdigest())
    if rebuild:
        from .pipeline import main
        main()
    return (load_clean(), joblib.load(MODELS / 'popularidad.joblib'),
            json.loads((REPORTS / 'analisis.json').read_text(encoding='utf-8')))


def setup(title):
    st.set_page_config(page_title=f'{title} · Videojuegos', layout='wide')
    st.title(title)
    st.caption('Backloggd · muestra de juegos populares · análisis académico')


def manual_checks():
    with st.expander('Que debo verificar manualmente'):
        st.write('Confirma escala de Rating, procedencia y plataforma de Metacritic, roles de Team, '
                 'fecha de captura, versiones duplicadas y licencia antes de interpretar o redistribuir.')


def read_report(name):
    return pd.read_csv(REPORTS / name)
