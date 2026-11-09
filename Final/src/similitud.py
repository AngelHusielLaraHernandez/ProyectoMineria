"""Vecinos descriptivos exclusivamente en el espacio predictivo de entrenamiento."""
import joblib
import numpy as np
import pandas as pd
from .config import CLEAN, MODELS


def cinco_vecinos(fila, pipeline):
    bundle = joblib.load(MODELS / 'vecinos_popularidad.joblib')
    espacio = pipeline.named_steps['preparar'].transform(fila)
    distancias, posiciones = bundle['vecinos'].kneighbors(espacio, n_neighbors=5)
    resultado = pd.DataFrame({'id_juego': np.asarray(bundle['ids'])[posiciones[0]], 'distancia': distancias[0]})
    catalogo = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
    return resultado.merge(catalogo[['id_juego', 'Title', 'Release Date', 'cluster_kmeans', 'cluster_dbscan']],
                           on='id_juego', how='left', validate='one_to_one')
