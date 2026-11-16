"""Pruebas de interacción y regresiones del tablero de exploración (Página 1)."""
import base64
import io
import json

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.testing.v1 import AppTest

import src.ui as ui
from src.config import REPORTS, ROOT
from src.visualizacion import FONT_SANS, PALETA


def _valores_plotly(raw):
    if isinstance(raw, dict) and 'bdata' in raw:
        return np.frombuffer(base64.b64decode(raw['bdata']), dtype=np.dtype(raw['dtype'])).tolist()
    return list(raw)


def _especificaciones_plotly(app):
    return [json.loads(pc.proto.spec) for pc in app.get('plotly_chart')]


def _grafica_brecha(app):
    for spec in _especificaciones_plotly(app):
        xaxis = spec.get('layout', {}).get('xaxis', {})
        if xaxis.get('title', {}).get('text') == 'Brecha (pts)':
            return spec
    raise AssertionError('No se encontró la gráfica de brecha en 1_Exploracion.py')


def test_dashboard_filtra_restablece_y_admite_consulta_vacia():
    app = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    total = app.metric[0].value
    app.multiselect(key='eda_generos_0').set_value(['Pinball']).run()
    assert not app.exception
    assert app.metric[0].value == f'1 / {total.split(" / ")[1]}'
    app.slider(key='eda_rating_0').set_value((0.0, 0.1)).run()
    assert not app.exception
    assert app.metric[0].value.startswith('0 / ')
    next(boton for boton in app.button if boton.label == 'Restablecer filtros').click().run()
    assert not app.exception
    assert app.metric[0].value == total
    assert not app.multiselect(key='eda_generos_1').value
    assert app.slider(key='eda_rating_1').value == (0.0, 5.0)


def test_dashboard_cuatro_pestanas_graficas_y_descarga_csv(monkeypatch):
    descargas = []
    orig_download = st.download_button

    def _spy_download(label, data, file_name=None, mime=None, **kwargs):
        descargas.append((label, data, file_name, mime, kwargs.get('disabled', False)))
        return orig_download(label, data, file_name=file_name, mime=mime, **kwargs)

    monkeypatch.setattr(st, 'download_button', _spy_download)

    app = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    assert not app.exception
    assert [tab.label for tab in app.tabs] == [
        'Señales de actividad',
        'Recepción y brecha',
        'Segmentación (Clustering)',
        'Riesgo comercial (GaaS)',
    ]
    assert len(app.dataframe) >= 4
    assert all(not df_el.value.empty for df_el in app.dataframe)

    for pc in app.get('plotly_chart'):
        spec = json.loads(pc.proto.spec)
        config = json.loads(pc.proto.config or '{}')
        assert spec['layout']['font']['family'] == FONT_SANS
        assert spec['layout']['margin']['t'] >= 44
        assert 'toImage' not in config.get('modeBarButtonsToRemove', [])

    assert [(d[2], d[4]) for d in descargas] == [
        ('consulta_dashboard.csv', False),
        ('correlacion_generos.csv', False),
    ]
    for _, payload, nombre, mime, _ in descargas:
        assert not nombre.startswith('tables/')
        assert mime == 'text/csv'
        parsed = pd.read_csv(io.BytesIO(payload))
        assert not parsed.empty

    descargas.clear()
    app.radio[3].set_value('Estudio / Organización (Team)').run(timeout=30)
    assert not app.exception
    assert any(d[2] == 'correlacion_organizaciones.csv' for d in descargas)


def test_dashboard_brecha_con_signo_destaca_tres_mayores_desacuerdos_absolutos():
    app = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    app.selectbox[0].set_value('brecha_media').run(timeout=30)
    assert not app.exception

    corr_gen = pd.read_csv(REPORTS / 'tables/correlacion_generos.csv').query('estado == "incluido"')
    esperados_gen = set(corr_gen.loc[corr_gen['brecha_media'].abs().nlargest(3).index, 'grupo'])

    traza_gen = _grafica_brecha(app)['data'][0]
    destacados_gen = {
        grupo for grupo, color in zip(traza_gen['y'], traza_gen['marker']['color'])
        if color == PALETA['accent']
    }
    assert destacados_gen == esperados_gen == {'Shooter', 'Racing', 'Fighting'}

    app.radio[3].set_value('Estudio / Organización (Team)').run(timeout=30)
    assert not app.exception
    corr_org = pd.read_csv(REPORTS / 'tables/correlacion_organizaciones.csv').query('estado == "incluido"')
    esperados_org = set(corr_org.loc[corr_org['brecha_media'].abs().nlargest(3).index, 'grupo'])

    traza_org = _grafica_brecha(app)['data'][0]
    destacados_org = {
        grupo for grupo, color in zip(traza_org['y'], traza_org['marker']['color'])
        if color == PALETA['accent']
    }
    assert destacados_org == esperados_org == {'Activision', 'Ubisoft Entertainment', 'Electronic Arts'}


def test_dashboard_fig_bar_log_seguro_ante_ceros(monkeypatch):
    app = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    assert not app.exception
    fig_bar_log = next(
        spec for spec in _especificaciones_plotly(app)
        if spec.get('layout', {}).get('barmode') == 'group'
        and spec.get('layout', {}).get('xaxis', {}).get('type') == 'log'
    )
    for traza in fig_bar_log['data']:
        valores_x = [float(v) for v in _valores_plotly(traza['x']) if v is not None and not np.isnan(float(v))]
        assert valores_x and all(v > 0 for v in valores_x)

    df_real, bundle, analysis = ui.resources()
    fila_cero = df_real.loc[df_real['Plays'] == 0].head(1).copy()
    assert not fila_cero.empty
    fila_cero['generos'] = [['Adventure']]
    fila_cero['Wishlist'] = [250.0]
    fila_cero['Backlogs'] = [45.0]
    monkeypatch.setattr(ui, 'resources', lambda: (fila_cero, bundle, analysis))

    app_cero = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    assert not app_cero.exception
    assert any('No hay registros positivos' in info.value for info in app_cero.info)

    app_cero.radio[0].set_value('Wishlist').run(timeout=30)
    assert not app_cero.exception
    fig_solo_positivas = next(
        spec for spec in _especificaciones_plotly(app_cero)
        if spec.get('layout', {}).get('barmode') == 'group'
        and spec.get('layout', {}).get('xaxis', {}).get('type') == 'log'
    )
    nombres_trazas = {t['name'] for t in fig_solo_positivas['data']}
    assert 'Plays' not in nombres_trazas
    assert nombres_trazas == {'Backlogs', 'Wishlist'}
    for traza in fig_solo_positivas['data']:
        valores_x = [float(v) for v in _valores_plotly(traza['x']) if v is not None and not np.isnan(float(v))]
        assert valores_x and all(v > 0 for v in valores_x)


def test_dashboard_fig_pca_y_metodos_seguros_con_filtros_vacios():
    app = AppTest.from_file(str(ROOT / 'pages/1_Exploracion.py')).run(timeout=30)
    app.slider(key='eda_rating_0').set_value((0.0, 0.1)).run(timeout=30)
    assert not app.exception
    assert app.metric[0].value.startswith('0 / ')
    assert any('La consulta no contiene juegos con coordenadas PCA.' in info.value for info in app.info)
    assert app.get('download_button')[0].proto.disabled

    for metodo in ['Ward', 'DBSCAN']:
        app.radio[4].set_value(metodo).run(timeout=30)
        assert not app.exception
        assert any('La consulta no contiene juegos con coordenadas PCA.' in info.value for info in app.info)
