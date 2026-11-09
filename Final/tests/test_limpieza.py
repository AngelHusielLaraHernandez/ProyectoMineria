"""Comprueba transformaciones, procedencia y conciliación de filas del log."""
import hashlib
import importlib
import json
import re

import numpy as np
import pandas as pd
import pytest

limpieza = importlib.import_module('src.02_limpieza')


@pytest.mark.parametrize('valor,esperado', [('999', 999), ('1K', 1000), ('1.5M', 1500000),
                                         (' 1.2 K ', 1200), (' 3m ', 3000000), ('1,200', 1200), ('1,500', 1500), (999, 999), (0, 0)])
def test_conversion_k_m(valor, esperado):
    assert limpieza.convertir_conteo(valor) == esperado


@pytest.mark.parametrize('valor', ['', '   ', None, pd.NA, np.nan])
def test_conversion_nulos(valor):
    assert pd.isna(limpieza.convertir_conteo(valor))


@pytest.mark.parametrize('valor', ['texto invalido', '1KK', '-4', '1,5K', 'inf', np.inf])
def test_conversion_invalida_no_imputa(valor):
    with pytest.raises(ValueError, match='Conteo inválido'):
        limpieza.convertir_conteo(valor)


def ejemplo():
    return pd.DataFrame([
        {'ID Original': 1, 'Title': 'Juego A', 'Release Date': 'Feb 25, 2022',
         'Genres': "['RPG', 'Adventure', 'RPG']", 'Rating': 4.5,
         'Metacritic Rating': 90, 'critic_score_final': 90,
         'critic_source': 'metacritic_csv', 'Origen_calificacion': 'Metacritic',
         **{c: '1.2K' for c in limpieza.CONTEOS}},
        {'ID Original': 2, 'Title': 'Juego B', 'Release Date': '10/12/2019',
         'Genres': '[]', 'Rating': np.nan, 'Metacritic Rating': 80,
         'critic_score_final': 80, 'critic_source': 'metacritic_csv',
         'Origen_calificacion': 'Metacritic', **{c: '999' for c in limpieza.CONTEOS}},
        {'ID Original': 3, 'Title': 'Juego C', 'Release Date': 'releases on TBD',
         'Genres': "['Indie']", 'Rating': 4, 'Metacritic Rating': 85,
         'critic_score_final': np.nan, 'critic_source': 'none',
         'Origen_calificacion': 'Estimacion propia', **{c: '0' for c in limpieza.CONTEOS}},
    ])


def test_fechas_mezcladas_y_decadas():
    df = ejemplo()
    df.loc[2, 'Release Date'] = '2020-01-31'
    resultado, _, _, _ = limpieza.limpiar(df)
    assert resultado.anio.tolist() == [2022, 2019, 2020]
    assert resultado.decada.tolist() == [2020, 2010, 2020]
    assert resultado.loc[1, 'fecha_lanzamiento'] == pd.Timestamp('2019-12-10')
    assert limpieza.interpretar_fecha('31/01/2020') == limpieza.interpretar_fecha('January 31, 2020')
    assert limpieza.interpretar_fecha('2020/01/31') == pd.Timestamp('2020-01-31')
    assert pd.isna(limpieza.interpretar_fecha('31/02/2020'))
    assert pd.isna(limpieza.interpretar_fecha('TBD'))
    assert pd.isna(limpieza.interpretar_fecha('Januarchy 31, 2020'))


def test_tbd_no_elimina_ni_inventa_anio():
    resultado, _, _, bitacora = limpieza.limpiar(ejemplo())
    assert pd.isna(resultado.loc[2, 'anio'])
    assert bool(resultado.loc[2, 'fecha_no_interpretable'])
    assert len(resultado) == 3
    assert all(p['antes'] == p['despues'] for p in bitacora.pasos)


def test_genero_principal_conserva_orden_y_largo_no_duplica_pertenencias():
    resultado, largo, _, _ = limpieza.limpiar(ejemplo())
    assert resultado.loc[0, 'genero_principal'] == 'RPG'
    assert pd.isna(resultado.loc[1, 'genero_principal'])
    assert largo.columns.tolist() == ['id_juego', 'juego', 'genero']
    assert largo.loc[largo.id_juego.eq(1), 'genero'].tolist() == ['RPG', 'Adventure']
    assert not largo.duplicated(['id_juego', 'genero']).any()
    assert set(largo.id_juego).issubset(set(resultado.id_juego))


def test_faltantes_no_se_imputan_y_estimada_no_crea_brecha():
    resultado, _, _, _ = limpieza.limpiar(ejemplo())
    assert resultado.loc[0, 'rating_normalizado'] == 90
    assert resultado.loc[0, 'brecha'] == 0
    assert pd.isna(resultado.loc[1, 'Rating']) and bool(resultado.loc[1, 'rating_faltante'])
    assert resultado.loc[2, 'metacritic_rating_original'] == 85
    assert pd.isna(resultado.loc[2, 'Metacritic Rating'])
    assert bool(resultado.loc[2, 'metacritic_rating_faltante'])
    assert not bool(resultado.loc[2, 'metacritic_rating_faltante_original'])
    assert pd.isna(resultado.loc[2, 'brecha'])


def test_metacritic_original_ausente_tiene_indicador():
    df = ejemplo()
    df.loc[1, ['Metacritic Rating', 'critic_score_final']] = np.nan
    resultado, _, _, _ = limpieza.limpiar(df)
    assert bool(resultado.loc[1, 'metacritic_rating_faltante_original'])
    assert bool(resultado.loc[1, 'metacritic_rating_faltante'])


def test_escala_invalida_no_se_normaliza_como_si_fuera_de_cinco():
    df = ejemplo()
    df.loc[0, 'Rating'] = 9
    with pytest.raises(ValueError, match='fuera de la escala documentada'):
        limpieza.limpiar(df)


def test_procedencia_incoherente_es_error():
    df = ejemplo()
    df.loc[2, 'critic_score_final'] = 85
    with pytest.raises(ValueError, match='procedencia coherente'):
        limpieza.limpiar(df)


def con_duplicado():
    df = ejemplo()
    repetido = df.iloc[[0]].copy()
    repetido['ID Original'] = 99
    repetido['Title'] = '  JUEGO   A '
    repetido['Release Date'] = '2022-02-25'
    return pd.concat([df, repetido], ignore_index=True)


def test_duplicados_equivalentes_se_eliminan_con_razon():
    resultado, largo, descartados, bitacora = limpieza.limpiar(con_duplicado())
    assert len(resultado) == 3 and len(descartados) == 1
    cambios = [p for p in bitacora.pasos if p['antes'] != p['despues']]
    assert len(cambios) == 1
    assert cambios[0]['eliminadas'] == 1 and cambios[0]['razon']
    assert not largo.duplicated(['id_juego', 'genero']).any()


def test_mismo_titulo_en_fechas_distintas_no_es_duplicado():
    df = con_duplicado()
    df.loc[3, 'Release Date'] = '2023-02-25'
    resultado, _, descartados, _ = limpieza.limpiar(df)
    assert len(resultado) == 4 and descartados.empty


def test_duplicados_en_conflicto_no_se_descartan_arbitrariamente():
    df = con_duplicado()
    df.loc[3, 'Plays'] = '50K'
    with pytest.raises(ValueError, match='Duplicados en conflicto'):
        limpieza.limpiar(df)


def test_bitacora_rechaza_cambios_sin_razon_o_fuera_de_balance():
    bitacora = limpieza.Bitacora(4)
    with pytest.raises(ValueError, match='razón registrada'):
        bitacora.registrar('Paso', 4, 3, 'Sin explicación', eliminadas=1)
    with pytest.raises(ValueError, match='no coincide'):
        bitacora.registrar('Paso', 4, 3, 'Conteo incorrecto', eliminadas=0)
    with pytest.raises(ValueError, match='fuera del registro'):
        bitacora.registrar('Paso', 3, 3, 'Se perdió una fila antes')
    with pytest.raises(ValueError, match='balance de filas'):
        bitacora.verificar(3)


def test_exportacion_concilia_csv_y_log_sin_modificar_fuente(tmp_path):
    entrada = tmp_path / 'data' / 'raw' / 'games_curated.csv'
    entrada.parent.mkdir(parents=True)
    con_duplicado().to_csv(entrada, index=False)
    huella = hashlib.sha256(entrada.read_bytes()).hexdigest()
    limpieza.ejecutar(tmp_path)
    log = (tmp_path / 'reports' / 'limpieza_log.md').read_text(encoding='utf-8')
    registro = json.loads(re.search(r'```json\n(.*?)\n```', log, re.S)[1])
    datos = pd.read_csv(tmp_path / 'data' / 'clean' / 'dataset_depurado.csv')
    largo = pd.read_csv(tmp_path / 'data' / 'clean' / 'generos_largo.csv')
    assert registro['filas_entrada'] == 4 and registro['filas_salida'] == len(datos) == 3
    assert registro['filas_generos_largo'] == len(largo)
    anterior = registro['filas_entrada']
    for paso in registro['pasos']:
        assert paso['antes'] == anterior
        assert paso['antes'] - paso['despues'] == paso['eliminadas']
        assert paso['antes'] == paso['despues'] or paso['razon']
        anterior = paso['despues']
    assert anterior == len(datos)
    assert registro['filas_entrada'] - sum(p['eliminadas'] for p in registro['pasos']) == len(datos)
    assert hashlib.sha256(entrada.read_bytes()).hexdigest() == huella
    assert huella in log


def test_exportacion_repetida_es_reproducible(tmp_path):
    entrada = tmp_path / 'data' / 'raw' / 'games_curated.csv'
    entrada.parent.mkdir(parents=True)
    ejemplo().to_csv(entrada, index=False)
    limpieza.ejecutar(tmp_path)
    rutas = [tmp_path / 'data' / 'clean' / 'dataset_depurado.csv',
             tmp_path / 'data' / 'clean' / 'generos_largo.csv', tmp_path / 'reports' / 'limpieza_log.md']
    anteriores = [p.read_bytes() for p in rutas]
    limpieza.ejecutar(tmp_path)
    assert anteriores == [p.read_bytes() for p in rutas]
