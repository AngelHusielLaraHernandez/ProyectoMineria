"""Vecinos descriptivos exclusivamente en el espacio predictivo de entrenamiento."""
import hashlib
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st

from .config import CLEAN, MODELS

_MOD_VERSION = 'p5-v12-portadas'


def _hash_archivo(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


@st.cache_resource(show_spinner=False)
def _cargar_vecinos_cacheados(file_hash: str) -> dict:
    return joblib.load(MODELS / 'vecinos_popularidad.joblib')


@st.cache_data(show_spinner=False)
def _cargar_clusters_cacheados(file_hash: str) -> pd.DataFrame:
    return pd.read_csv(
        CLEAN / 'dataset_con_clusters.csv',
        usecols=['id_juego', 'Title', 'Release Date', 'cluster_kmeans', 'cluster_dbscan'],
    )


def cinco_vecinos(fila, pipeline, vecinos=None, df_clusters=None):
    """Recupera los 5 vecinos de entrenamiento más cercanos sin releer disco si ya vienen cacheados."""
    bundle = vecinos if vecinos is not None else _cargar_vecinos_cacheados(_hash_archivo(MODELS / 'vecinos_popularidad.joblib'))
    espacio = pipeline.named_steps['preparar'].transform(fila)
    distancias, posiciones = bundle['vecinos'].kneighbors(espacio, n_neighbors=5)
    resultado = pd.DataFrame({'id_juego': np.asarray(bundle['ids'])[posiciones[0]], 'distancia': distancias[0]})
    catalogo = (
        df_clusters
        if df_clusters is not None
        else _cargar_clusters_cacheados(_hash_archivo(CLEAN / 'dataset_con_clusters.csv'))
    )
    return resultado.merge(
        catalogo[['id_juego', 'Title', 'Release Date', 'cluster_kmeans', 'cluster_dbscan']],
        on='id_juego',
        how='left',
        validate='one_to_one',
    )
