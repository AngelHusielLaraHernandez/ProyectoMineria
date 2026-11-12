"""Regresiones de trazabilidad, coherencia entre fases y prevención de circularidad."""
import hashlib
import importlib
import json

import pandas as pd
import pytest

from src.config import ROOT, CLEAN, REPORTS
from src.data import load_clean
from src.modeling import train
from src.procedencia import auditar_historia


def test_historia_se_reconstruye_sin_modificar_maestro():
    origen = ROOT / 'data/raw/games_curated.csv'
    antes = origen.read_bytes()
    historia, pendientes = auditar_historia(ROOT)
    assert historia['filas_historicas'] == 1512
    assert historia['descartes_heredados'] == 395
    assert historia['grupos_con_diferencias'] == 13
    assert historia['grupos_con_conflicto_analitico'] == 3
    assert historia['diferencias_reconstruccion'] == []
    assert pendientes == {117, 140, 296}
    assert origen.read_bytes() == antes


def test_seis_figuras_eda_y_script_reproducible_presentes():
    assert (ROOT / 'src/01_inspeccion.py').exists()
    for nombre in ['rating', 'metacritic', 'plays_log', 'decadas', 'generos_top15', 'rating_vs_metacritic']:
        assert (REPORTS / f'figures/eda_{nombre}.png').stat().st_size > 1000


def test_join_de_generos_exige_id_y_preserva_pertenencias():
    juegos = pd.read_csv(CLEAN / 'dataset_depurado.csv')
    generos = pd.read_csv(CLEAN / 'generos_largo.csv')
    unido = generos.merge(juegos[['id_juego', 'Release Date']], on='id_juego', validate='many_to_one')
    assert len(unido) == len(generos)
    assert juegos.titulo_compartido.sum() == 35
    assert juegos.loc[juegos.titulo_compartido, 'grupo_titulo'].nunique() == 17
    with pytest.raises(pd.errors.MergeError):
        generos.merge(juegos[['Title', 'Release Date']], left_on='juego', right_on='Title', validate='many_to_one')


def test_correlaciones_con_casos_historicos_senalados_excluidos():
    parametros = json.loads((REPORTS / 'clustering_03_parametros.json').read_text())
    assert parametros['n_completos'] == 887
    assert parametros['n_conflictos_historicos'] == 3
    tabla = pd.read_csv(REPORTS / 'clustering_03_correlaciones_catalogo.csv')
    assert tabla.iloc[0]['n'] == parametros['n_completos']


def test_modelo_rechaza_etiquetas_y_proyecciones_de_clusters():
    for campo in ['cluster_kmeans', 'cluster_dbscan', 'componente_1']:
        with pytest.raises(ValueError, match='no acepta'):
            train(pd.DataFrame({campo: [0]}))


def test_modelo_usa_solo_depurado_y_excluye_conflictos():
    modelo = pd.read_csv(CLEAN / 'juegos_modelo.csv')
    assert len(modelo) == len(load_clean().query('elegible_analisis')) == 1114
    assert not set(modelo.id_juego) & {117, 140, 296}
    assert not any(c.startswith(('cluster_', 'componente_')) for c in modelo)
    metadata = json.loads((ROOT / 'models/metadata.json').read_text())
    assert metadata['definicion_objetivo']['version'] == 'INDICE-PERCENTILES-TRAIN-2.0'


def test_log_no_atribuye_conversiones_km_inexistentes():
    log = (REPORTS / 'limpieza_log.md').read_text()
    assert '0 textos K/M convertidos' in log
    assert '395 filas históricas' in log
    assert 'ya no están en el maestro' in log


def test_manifest_app_y_reporte_comparten_artefactos():
    manifest = json.loads((REPORTS / 'manifest.json').read_text())
    for nombre in ['dataset_depurado', 'dataset_con_clusters']:
        assert manifest[f'sha256_{nombre}'] == hashlib.sha256((CLEAN / f'{nombre}.csv').read_bytes()).hexdigest()
    app = (ROOT / 'pages/1_Exploracion.py').read_text()
    assert 'dataset_con_clusters.csv' in app
    assert "CLEAN / 'perfiles.csv'" not in app
    assert "tables/perfiles_clusters.csv" in app


def test_comparacion_weka_es_ejecucion_y_misma_fuente():
    manifest = json.loads((REPORTS / 'weka/ejecucion.json').read_text())
    tabla = pd.read_csv(REPORTS / 'weka/comparacion.csv')
    assert set(tabla.herramienta) == {'Weka 3.8.6', 'sklearn'}
    assert len(tabla) == 6 and tabla.n.eq(887).all()
    assert manifest['sha256_dataset_depurado'] == hashlib.sha256((CLEAN / 'dataset_depurado.csv').read_bytes()).hexdigest()
    assert (REPORTS / 'weka/k2_stdout.txt').stat().st_size > 1000
