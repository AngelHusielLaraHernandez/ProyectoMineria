"""Regresiones de la fase 04: target explícito, folds, categorías y artefacto crudo."""
import importlib
import json
from math import ceil

import joblib
import numpy as np
import pandas as pd
import pytest
from sklearn.pipeline import Pipeline

from src.config import FEATURES, ROOT
from src.features import CategoriasFrecuentes
from src.objetivo import CAMPOS_OBJETIVO, definir_objetivo

modulo = importlib.import_module('src.04_modelo')


def test_objetivo_es_promedio_de_rangos_y_no_de_escalas():
    df = pd.DataFrame({'Plays': [10, 10, 20, 40, 80, 160], 'Wishlist': [1, 2, 3, 4, 5, 6], 'Backlogs': [1, 2, 3, 4, 5, 6]})
    out, meta = definir_objetivo(df)
    np.testing.assert_allclose(out.popularidad_indice, df.rank(method='average', pct=True).mean(axis=1))
    assert out.percentil_plays.iloc[0] == out.percentil_plays.iloc[1]
    assert meta['campos'] == CAMPOS_OBJETIVO
    assert set(out.nivel_popularidad) == {'bajo', 'medio', 'alto'}


def test_objetivo_con_empates_sin_tres_niveles_es_error():
    with pytest.raises(ValueError, match='empates'):
        definir_objetivo(pd.DataFrame({c: [1]*10 for c in CAMPOS_OBJETIVO}))


def test_categorias_raras_y_nuevas_se_agrupan_en_otro():
    encoder = CategoriasFrecuentes(min_frecuencia=2).fit(pd.DataFrame({'estudio': [['A'], ['A', 'B'], []]}))
    assert encoder.vocabulario_ == ['A']
    z = encoder.transform(pd.DataFrame({'estudio': [['B'], ['Nuevo'], [], '["A"]']}))
    np.testing.assert_array_equal(z, [[0, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]])


def test_holdout_y_diez_folds_respetan_estratos_y_titulos():
    df = pd.read_csv(ROOT / 'data/clean/juegos_modelo.csv')
    train = df[df.particion.eq('entrenamiento')]
    test = df[df.particion.eq('prueba')]
    assert abs(len(test)/len(df) - .2) < .02
    assert not set(train.grupo_titulo) & set(test.grupo_titulo)
    assert train.fold_validacion.nunique() == 10
    for fold in range(1, 11):
        a = train[train.fold_validacion.ne(fold)]
        b = train[train.fold_validacion.eq(fold)]
        assert set(b.nivel_popularidad) == {'bajo', 'medio', 'alto'}
        assert not set(a.grupo_titulo) & set(b.grupo_titulo)
    assert set(test.nivel_popularidad) == {'bajo', 'medio', 'alto'}


def test_archivo_guardado_es_pipeline_y_recibe_formulario_crudo():
    modelo = joblib.load(ROOT / 'models/modelo_popularidad.joblib')
    assert isinstance(modelo, Pipeline)
    fila = pd.DataFrame([{'generos': '["RPG", "Género nuevo"]', 'estudio': 'Estudio nuevo',
                          'decada': 2030, 'Metacritic Rating': np.nan, 'Rating': np.nan}])
    assert modelo.predict(fila)[0] in ['bajo', 'medio', 'alto']
    assert np.isfinite(modelo.predict_proba(fila)).all()
    assert set(FEATURES).isdisjoint(CAMPOS_OBJETIVO + ['Playing', 'cluster_kmeans', 'cluster_dbscan'])


def test_ganador_se_elige_por_cv_y_permuta_solo_campos_crudos():
    tabla = pd.read_csv(ROOT / 'reports/modelo_comparacion.csv')
    meta = json.loads((ROOT / 'models/metadata.json').read_text())
    assert meta['modelo'] == 'RandomForestClassifier'
    externa = pd.read_csv(ROOT / 'reports/tables/cv_externa_folds.csv')
    assert externa.groupby('modelo').size().eq(50).all()
    medias = externa.groupby('modelo').f1_macro.mean()
    assert np.allclose(tabla.set_index('modelo').f1_macro_cv, medias.reindex(tabla.modelo))
    assert set(tabla.modelo) == {'DummyClassifier', 'CategoricalNB', 'DecisionTreeClassifier', 'RandomForestClassifier', 'MLPClassifier'}
    perm = pd.read_csv(ROOT / 'reports/modelo_permutation_importance.csv')
    assert set(perm.variable_cruda) == set(FEATURES)
    assert len(pd.read_csv(ROOT / 'reports/modelo_permutaciones_repeticiones.csv')) == 30
    assert np.asarray(meta['metricas']['matriz_confusion']).sum() == meta['n_prueba']


def test_metadata_declara_referencia_de_entrenamiento_y_fuentes():
    meta = json.loads((ROOT / 'models/metadata.json').read_text())
    assert meta['version_sklearn']
    assert meta['fecha'] and meta['clases'] == ['bajo', 'medio', 'alto']
    assert 'solo en entrenamiento' in meta['definicion_objetivo']['momento_definicion']
    assert meta['definicion_objetivo']['poblacion_referencia_n'] == meta['n_entrenamiento']
    assert meta['validacion']['pliegues'] == 10


def test_imputacion_y_vocabulario_se_ajustan_solo_con_entrenamiento():
    df = pd.read_csv(ROOT / 'data/clean/juegos_modelo.csv')
    train = df[df.particion.eq('entrenamiento')]
    modelo = joblib.load(ROOT / 'models/modelo_popularidad.joblib')
    notas = modelo.named_steps['preparar'].named_transformers_['notas']
    np.testing.assert_allclose(notas.named_steps['imputar'].statistics_, train[['Metacritic Rating', 'Rating']].median())
    assert 'Estudio nuevo' not in modelo.named_steps['preparar'].named_transformers_['estudio'].vocabulario_
