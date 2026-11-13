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
    assert isinstance(fila, pd.DataFrame)
    assert clase == modelo.predict(fila)[0]
    assert sum(p.values()) == pytest.approx(1)
    for etiqueta,valor in zip(modelo.classes_,modelo.predict_proba(fila)[0]):
        assert p[etiqueta] == pytest.approx(valor)
    if meta is None:
        assert fila['Metacritic Rating'].isna().all()


@pytest.mark.parametrize('decada', [-1, -1.0, 0, 1980, 2020])
def test_formulario_acepta_decada_menos_uno_y_multiplos_de_diez(modelo, decada):
    fila, clase, p = predecir_formulario(modelo, ['Adventure', 'RPG'], ['Otro'], decada, 82, 3.9)
    assert fila['decada'].iloc[0] == int(decada)
    assert clase == modelo.predict(fila)[0]
    assert sum(p.values()) == pytest.approx(1)
    for etiqueta, valor in zip(modelo.classes_, modelo.predict_proba(fila)[0]):
        assert p[etiqueta] == pytest.approx(valor)


@pytest.mark.parametrize('decada_invalida', [True, False, np.bool_(True), np.bool_(False), 1985, 2023, -10, -2, 2020.5, np.nan, np.inf])
def test_formulario_rechaza_bool_y_decadas_invalidas(modelo, decada_invalida):
    with pytest.raises(ValueError):
        predecir_formulario(modelo, ['RPG'], ['Otro'], decada_invalida, 82, 3.9)


def test_predecir_formulario_evalua_predict_proba_una_sola_vez(modelo):
    class _PipelineSpy:
        def __init__(self, real):
            self._real = real
            self.classes_ = real.classes_
            self.llamadas_proba = 0

        def predict(self, X):
            raise AssertionError('predecir_formulario no debe invocar predict() por separado')

        def predict_proba(self, X):
            self.llamadas_proba += 1
            return self._real.predict_proba(X)

    espia = _PipelineSpy(modelo)
    fila, clase, p = predecir_formulario(espia, ['RPG'], ['Nintendo'], -1, 88, 4.3)
    assert espia.llamadas_proba == 1
    assert clase == modelo.predict(fila)[0]
    for etiqueta, valor in zip(modelo.classes_, modelo.predict_proba(fila)[0]):
        assert p[etiqueta] == pytest.approx(valor)


@pytest.mark.parametrize('meta,rating', [(101,3.9),(82,5.1),(-1,3.9),(82,np.inf)])
def test_formulario_rechaza_escalas_invalidas(modelo,meta,rating):
    with pytest.raises(ValueError):
        predecir_formulario(modelo,['RPG'],['Otro'],2020,meta,rating)


def test_sin_genero_no_se_predice(modelo):
    with pytest.raises(ValueError,match='género'):
        predecir_formulario(modelo,[],['Otro'],2020,82,3.9)


def test_interfaz_envia_valores_del_formulario(modelo):
    import json
    from streamlit.testing.v1 import AppTest
    app=AppTest.from_file(str(ROOT/'pages/2_Prediccion.py')).run(timeout=60)
    app.multiselect[0].set_value(['RPG'])
    app.selectbox[0].set_value('Nintendo')
    app.selectbox[1].set_value(2010)
    app.slider[0].set_value(91)
    app.slider[1].set_value(4.5)
    app.button[0].click().run(timeout=60)
    temperatura = json.loads((MODELS / 'metadata.json').read_text())['calibracion_web']['temperatura']
    fila, clase, probabilidades = predecir_formulario(
        modelo, ['RPG'], ['Nintendo'], 2010, 91, 4.5, temperatura=temperatura,
    )
    assert not app.exception
    assert any(f'Nivel estimado de popularidad: {clase.upper()}' in e.value for e in app.subheader)
    assert clase == modelo.predict(fila)[0]
    assert sum(probabilidades.values()) == pytest.approx(1)
    original = dict(zip(modelo.classes_, modelo.predict_proba(fila)[0]))
    assert probabilidades[clase] != pytest.approx(original[clase])
    barras = next(b.value for b in app.markdown if '<div class="p5-prob-row">' in b.value)
    for nivel, probabilidad in probabilidades.items():
        assert f'<span>{nivel.upper()}</span>\n<span>{probabilidad:.1%}</span>' in barras
    assert any(e.label == '¿Qué significan alto, medio y bajo?' for e in app.expander)
    app.checkbox[0].set_value(True)
    app.button[0].click().run(timeout=60)
    _,clase,_=predecir_formulario(modelo,['RPG'],['Nintendo'],2010,None,4.5)
    assert not app.exception
    assert any(f'Nivel estimado de popularidad: {clase.upper()}' in e.value for e in app.subheader)


def test_interfaz_envia_decada_menos_uno(modelo):
    from streamlit.testing.v1 import AppTest
    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    assert 'Sin fecha interpretable (Década -1)' in app.selectbox[1].options
    app.multiselect[0].set_value(['RPG'])
    app.selectbox[0].set_value('Nintendo')
    app.selectbox[1].set_value(-1)
    assert app.selectbox[1].value == -1
    app.slider[0].set_value(84)
    app.slider[1].set_value(4.1)
    app.button[0].click().run(timeout=60)
    _, clase, _ = predecir_formulario(modelo, ['RPG'], ['Nintendo'], -1, 84, 4.1)
    assert not app.exception
    assert any(f'Nivel estimado de popularidad: {clase.upper()}' in e.value for e in app.subheader)
    assert len(app.dataframe[0].value) == 5
