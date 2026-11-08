"""Pruebas de los riesgos científicos y de integración principales."""
import json

import joblib
import numpy as np
import pandas as pd
import pytest
from scipy.io import arff
from streamlit.testing.v1 import AppTest

from src.analysis import grouped_correlations
from src.config import CLEAN, FEATURES, MODELS, REPORTS, ROOT, SIGNALS, RAW
from src.data import load_clean, parse_count, parse_list
from src.modeling import levels, thresholds


@pytest.mark.parametrize('raw,expected', [('3.9K', 3900), ('1.2M', 1200000), ('850', 850), ('0', 0)])
def test_suffix(raw, expected):
    assert parse_count(raw) == expected


@pytest.mark.parametrize('raw', ['-5', 'desconocido', '1KK'])
def test_reject_invalid_counts(raw):
    with pytest.raises(ValueError):
        parse_count(raw)


def test_literal_lists_and_missing():
    assert parse_list("['RPG', 'RPG', 'Adventure']") == ['Adventure', 'RPG']
    assert parse_list(np.nan) == []
    with pytest.raises((ValueError, SyntaxError)):
        parse_list('__import__("os").system("false")')


def test_estimates_and_conflicts_excluded():
    df = load_clean()
    assert not df.duplicated(['Title', 'Release Date']).any()
    assert df.loc[df['Origen_calificacion'].ne('Metacritic'), 'critica_verificada_csv'].isna().all()
    conflicts = pd.read_csv(CLEAN / 'conflictos_duplicados.csv')
    assert not set(zip(df['Title'], df['Release Date'])) & set(zip(conflicts['Title'], conflicts['Release Date']))
    assert not any('estimad' in c.lower() for c in df.columns)
    assert len(df) == json.loads((REPORTS / 'inspeccion.json').read_text())['filas_limpias']
    assert not set(['rating_100', 'gap', 'gap_real', 'studio_main', 'publisher_main']) & set(df.columns)
    original = ROOT.parent / 'Proyecto' / 'data' / 'processed' / 'games_curated.csv'
    if original.exists():
        assert RAW.read_bytes() == original.read_bytes()


def test_test_set_does_not_define_terciles_or_features():
    df = pd.read_csv(CLEAN / 'juegos_modelo.csv')
    train = df[df.particion.eq('entrenamiento')]
    test = df[df.particion.eq('prueba')]
    bundle = joblib.load(MODELS / 'popularidad.joblib')
    assert set(train.grupo_titulo).isdisjoint(test.grupo_titulo)
    np.testing.assert_allclose(bundle['cortes'], thresholds(train.popularidad_indice))
    assert (levels(test.popularidad_indice, bundle['cortes']) == test.nivel_popularidad).all()
    assert set(FEATURES).isdisjoint(SIGNALS + ['popularidad_indice', 'nivel_popularidad', 'Metacritic Rating'])
    encoder = bundle['pipeline'].named_steps['preparar'].named_transformers_['organizaciones'].encoder_
    seen_train = {v for row in train.organizaciones.map(json.loads) for v in row}
    assert set(encoder.classes_) == seen_train


def test_small_groups_do_not_produce_correlations():
    df = pd.DataFrame({'generos': [['RPG']] * 5, 'Rating': [1, 2, 3, 4, 5],
                       'critica_verificada_csv': [30, 50, 60, 80, 90]})
    row = grouped_correlations(df, 'generos').iloc[0]
    assert row['n'] == 5 and pd.isna(row['r'])


def test_unknown_organizations_and_missing_ratings():
    bundle = joblib.load(MODELS / 'popularidad.joblib')
    row = pd.DataFrame([{'generos': ['Género desconocido'], 'organizaciones': ['Estudio nuevo'],
                         'decada': 2030, 'Rating': np.nan, 'critica_verificada_csv': np.nan}])
    assert bundle['pipeline'].predict(row)[0] in ['bajo', 'medio', 'alto']


def test_arff_partitions_readable():
    for name in ['entrenamiento', 'prueba']:
        data, meta = arff.loadarff(CLEAN / f'{name}_weka.arff')
        exported = pd.read_csv(CLEAN / f'{name}_orange.csv')
        assert len(data) == len(exported)
        assert len(meta.names()) == len(exported.columns)


@pytest.mark.parametrize('page', ['app.py', 'pages/1_Usuarios_y_prensa.py',
                                  'pages/2_Perfiles.py', 'pages/3_Consultar_modelo.py'])
def test_app_pages(page):
    app = AppTest.from_file(str(ROOT / page)).run(timeout=60)
    assert not app.exception, [x.message for x in app.exception]
    if 'Consultar' in page:
        app.button[0].click().run(timeout=30)
        assert not app.exception
        assert any('Nivel estimado' in x.value for x in app.subheader)
    if page == 'app.py':
        app.text_input[0].set_value('NINGUN_JUEGO_123456').run()
        assert not app.exception
        assert app.info
