"""Adaptador de compatibilidad; el único clustering vive en 03_clustering.py."""
import importlib
import json
from .config import REPORTS


def grouped_correlations(df, column):
    modulo = importlib.import_module('src.03_clustering')
    d = df.rename(columns={'critica_verificada_csv': 'Metacritic Rating'}).copy()
    d['brecha'] = d['Rating'] * 20 - d['Metacritic Rating']
    return modulo.correlaciones_por_grupo(d, column).rename(columns={'pearson_r': 'r', 'pearson_p': 'p'})


def analyze(df=None):
    resultado = importlib.import_module('src.03_clustering').ejecutar()
    (REPORTS / 'analisis.json').write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
    return resultado
