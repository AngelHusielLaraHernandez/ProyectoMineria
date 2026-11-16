"""Pruebas de cobertura, asociación y espacio del análisis de seis variables."""
import importlib
import json

import numpy as np
import pandas as pd
import pytest

modulo = importlib.import_module('src.03_clustering')


def test_minimo_20_se_aplica_a_pares_y_no_solo_titulos():
    df = pd.DataFrame({'Rating': np.arange(25, dtype=float), 'Metacritic Rating': np.arange(25, dtype=float)})
    df.loc[:5, 'Rating'] = np.nan
    resultado = modulo.asociacion(df)
    assert resultado['n_juegos'] == 25 and resultado['n'] == 19
    assert resultado['estado'].startswith('excluido')
    assert pd.isna(resultado['pearson_r']) and pd.isna(resultado['pearson_p'])
    df.loc[5, 'Rating'] = 5
    resultado = modulo.asociacion(df)
    assert resultado['n'] == 20 and resultado['estado'] == 'incluido'
    assert np.isfinite(resultado['pearson_p']) and np.isfinite(resultado['spearman_p'])


def test_correlacion_alta_no_equivale_a_brecha_pequena():
    rating = np.linspace(1, 4, 30)
    df = pd.DataFrame({'Rating': rating, 'Metacritic Rating': rating * 20 + 10,
                       'brecha': np.full(30, -10), 'generos': [['RPG']] * 30})
    tabla = modulo.correlaciones_por_grupo(df, 'generos')
    assert tabla.iloc[0]['pearson_r'] == pytest.approx(1)
    assert tabla.iloc[0]['brecha_absoluta_media'] == pytest.approx(10)


def test_variables_constantes_no_generan_p_valores_enganosos():
    df = pd.DataFrame({'Rating': [4] * 25, 'Metacritic Rating': np.arange(25)})
    resultado = modulo.asociacion(df)
    assert resultado['estado'] == 'excluido: variable constante'
    assert pd.isna(resultado['spearman_p'])


def datos():
    rng = np.random.default_rng(42)
    df = pd.DataFrame(rng.uniform(1, 1000, size=(40, 4)), columns=modulo.CONTEOS)
    df['Rating'] = rng.uniform(1, 5, 40)
    df['Metacritic Rating'] = rng.uniform(45, 99, 40)
    return df


def test_log_y_escalado_solo_en_casos_completos_sin_genero():
    df = datos()
    df.loc[0, 'Rating'] = np.nan
    df['genero'] = 'No entra a la distancia'
    mascara, espacio, escalador = modulo.preparar_espacio(df)
    assert mascara.sum() == 39 and espacio.shape == (39, 6)
    np.testing.assert_allclose(espacio.mean(axis=0), 0, atol=1e-12)
    np.testing.assert_allclose(espacio.std(axis=0), 1, atol=1e-12)
    np.testing.assert_allclose(escalador.mean_[:4], np.log1p(df.loc[mascara, modulo.CONTEOS]).mean())
    np.testing.assert_allclose(escalador.mean_[4:], df.loc[mascara, ['Rating', 'Metacritic Rating']].mean())


def test_eps_se_extrae_de_la_curva_usada_y_es_reproducible():
    _, espacio, _ = modulo.preparar_espacio(datos())
    eps, indice, distancias, motivo = modulo.elegir_eps(espacio, 12)
    assert eps > 0 and eps == distancias[indice]
    assert np.all(np.diff(distancias) >= 0)
    assert eps == modulo.elegir_eps(espacio, 12)[0]
    assert motivo


def test_ruido_no_se_presenta_como_silhouette_de_un_cluster():
    _, espacio, _ = modulo.preparar_espacio(datos())
    assert modulo.silueta_sin_ruido(espacio, np.full(40, -1)) is None
    assert modulo.silueta_sin_ruido(espacio, np.zeros(40, dtype=int)) is None


def test_salida_real_conserva_juegos_y_distingue_ausencias_de_ruido():
    entrada = pd.read_csv(modulo.RAIZ / 'data/clean/dataset_depurado.csv')
    salida = pd.read_csv(modulo.RAIZ / 'data/clean/dataset_con_clusters.csv')
    parametros = json.loads((modulo.RAIZ / 'reports/clustering_03_parametros.json').read_text())
    assert len(entrada) == len(salida) == parametros['n_entrada']
    assert entrada.id_juego.tolist() == salida.id_juego.tolist()
    completos = entrada[modulo.VARIABLES].notna().all(axis=1)
    if 'elegible_analisis' in entrada:
        completos &= entrada.elegible_analisis
    assert salida.incluido_clustering.equals(completos)
    assert salida.loc[~completos, ['cluster_kmeans', 'cluster_dbscan']].isna().all().all()
    assert salida.loc[completos, ['cluster_kmeans', 'cluster_dbscan']].notna().all().all()
    assert int(salida.cluster_dbscan.eq(-1).sum()) == parametros['dbscan_ruido']
