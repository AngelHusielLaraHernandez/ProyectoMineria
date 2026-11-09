"""Adaptadores de la fuente canónica producida por la fase 02."""
import importlib
import json
import numpy as np
import pandas as pd
from .config import CLEAN, REPORTS, SIGNALS
from .objetivo import aplicar_referencia
from .config import MODELS


def parse_count(value):
    return importlib.import_module('src.02_limpieza').convertir_conteo(value)


def parse_list(value):
    return sorted(importlib.import_module('src.02_limpieza').interpretar_generos(value))


def load_clean():
    df = pd.read_csv(CLEAN / 'dataset_depurado.csv')
    df['generos'] = df['generos'].map(json.loads)
    df['organizaciones'] = df['Team'].map(parse_list)
    df['estudio'] = df['organizaciones']
    df['critica_verificada_csv'] = df['Metacritic Rating']
    df['popularidad_indice'] = np.nan
    elegibles = df.elegible_analisis & df[['Plays', 'Wishlist', 'Backlogs']].notna().all(axis=1)
    metadata = MODELS / 'metadata.json'
    if metadata.exists():
        referencia = json.loads(metadata.read_text())['definicion_objetivo']
        if referencia.get('version') == 'INDICE-PERCENTILES-TRAIN-2.0':
            objetivo = aplicar_referencia(df.loc[elegibles], referencia)
            df.loc[elegibles, 'popularidad_indice'] = objetivo.popularidad_indice
    return df


def prepare():
    importlib.import_module('src.02_limpieza').ejecutar()
    return load_clean(), json.loads((REPORTS / 'inspeccion.json').read_text())
