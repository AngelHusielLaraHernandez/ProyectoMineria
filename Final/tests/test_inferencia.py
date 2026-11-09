"""Paridad entre formulario, datos crudos y artefacto guardado."""
import joblib
import numpy as np
import pandas as pd
import pytest
from src.config import MODELS, ROOT
from src.inferencia import predecir_formulario


@pytest.fixture(scope='module')
def modelo():
    return joblib.load(MODELS / 'modelo_popularidad.joblib')


@pytest.mark.parametrize('meta,rating,estudio', [(82,3.9,['Otro']), (None,3.9,['Otro']), (100,5,['Nintendo']), (0,0,['Organización nueva'])])
def test_formulario_coincide_con_pipeline(modelo, meta, rating, estudio):
    fila, clase, p = predecir_formulario(modelo,['Adventure','RPG'],estudio,2020,meta,rating)
    assert clase == modelo.predict(fila)[0]
    assert sum(p.values()) == pytest.approx(1)
    for etiqueta,valor in zip(modelo.classes_,modelo.predict_proba(fila)[0]):
        assert p[etiqueta] == pytest.approx(valor)
    if meta is None:
        assert fila['Metacritic Rating'].isna().all()


@pytest.mark.parametrize('meta,rating', [(101,3.9),(82,5.1),(-1,3.9),(82,np.inf)])
def test_formulario_rechaza_escalas_invalidas(modelo,meta,rating):
    with pytest.raises(ValueError):
        predecir_formulario(modelo,['RPG'],['Otro'],2020,meta,rating)


def test_sin_genero_no_se_predice(modelo):
    with pytest.raises(ValueError,match='género'):
        predecir_formulario(modelo,[],['Otro'],2020,82,3.9)


def test_interfaz_envia_valores_del_formulario(modelo):
    from streamlit.testing.v1 import AppTest
    app=AppTest.from_file(str(ROOT/'pages/2_Prediccion.py')).run(timeout=60)
    app.multiselect[0].set_value(['RPG'])
    app.selectbox[0].set_value('Nintendo')
    app.selectbox[1].set_value(2010)
    app.slider[0].set_value(91)
    app.slider[1].set_value(4.5)
    app.button[0].click().run(timeout=60)
    _,clase,_=predecir_formulario(modelo,['RPG'],['Nintendo'],2010,91,4.5)
    assert not app.exception
    assert any(f'Nivel estimado de popularidad: {clase.upper()}' in e.value for e in app.subheader)
    app.checkbox[0].set_value(True)
    app.button[0].click().run(timeout=60)
    _,clase,_=predecir_formulario(modelo,['RPG'],['Nintendo'],2010,None,4.5)
    assert not app.exception
    assert any(f'Nivel estimado de popularidad: {clase.upper()}' in e.value for e in app.subheader)
