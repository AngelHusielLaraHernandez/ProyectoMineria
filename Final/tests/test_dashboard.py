from streamlit.testing.v1 import AppTest

from src.config import ROOT


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
