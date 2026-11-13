"""Regresiones metodológicas y de portabilidad de la segunda auditoría."""
import importlib
import json
import os
import subprocess
import sys

import joblib
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from streamlit.testing.v1 import AppTest

from src.config import ROOT, FEATURES
from src.features import CategoriasFrecuentes
from src.objetivo import ajustar_referencia, aplicar_referencia, ClasificadorObjetivoLocal

modulo = importlib.import_module('src.04_modelo')


def datos_y_metadata():
    return (pd.read_csv(ROOT / 'data/clean/juegos_modelo.csv'),
            json.loads((ROOT / 'models/metadata.json').read_text()))


def test_otro_estudio_es_respaldo_y_no_bandera_de_cualquier_socio_raro():
    encoder = CategoriasFrecuentes(min_frecuencia=2, otro_solo_si_ninguna=True)
    encoder.fit(pd.DataFrame({'estudio': [['A'], ['A', 'Raro'], ['B']]}))
    z = encoder.transform(pd.DataFrame({'estudio': [['A', 'Nuevo'], ['Nuevo'], [], ['A']]}))
    np.testing.assert_array_equal(z, [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]])


def test_referencia_no_cambia_al_alterar_solo_prueba():
    df, meta = datos_y_metadata()
    train = df[df.particion.eq('entrenamiento')]
    original = ajustar_referencia(train)
    mutado = df.copy()
    mutado.loc[mutado.particion.eq('prueba'), ['Plays', 'Wishlist', 'Backlogs']] = 10**12
    nueva = ajustar_referencia(mutado[mutado.particion.eq('entrenamiento')])
    assert nueva == original == meta['definicion_objetivo']
    esperado = aplicar_referencia(df, original)
    assert esperado.nivel_popularidad.tolist() == df.nivel_popularidad.tolist()


def test_cada_fold_usa_referencia_y_etiquetas_de_su_subentrenamiento():
    df, _ = datos_y_metadata()
    folds = json.loads((ROOT / 'models/referencias_folds.json').read_text())
    etiquetas = pd.read_csv(ROOT / 'reports/modelo_etiquetas_validacion_locales.csv')
    assert len(folds) == 10
    por_id = df.set_index('id_juego', drop=False)
    test_ids = set(df.loc[df.particion.eq('prueba'), 'id_juego'])
    for f in folds:
        assert not set(f['ids_ajuste']) & set(f['ids_validacion'])
        assert not (set(f['ids_ajuste']) | set(f['ids_validacion'])) & test_ids
        ref = ajustar_referencia(por_id.loc[f['ids_ajuste']])
        assert f['referencia'] == ref
        esperado = aplicar_referencia(por_id.loc[f['ids_validacion']], ref).nivel_popularidad.tolist()
        assert esperado == etiquetas.loc[etiquetas.fold.eq(f['fold']), 'nivel_popularidad_local'].tolist()


def test_estimador_grid_aprende_objetivo_sin_etiquetas_globales():
    df, _ = datos_y_metadata()
    muestra = df[df.particion.eq('entrenamiento')].head(90).copy()
    for c in ['generos', 'estudio']:
        muestra[c] = muestra[c].map(json.loads)
    modelo = ClasificadorObjetivoLocal(modulo.construir_pipeline(DecisionTreeClassifier(max_depth=3, random_state=42)))
    # y intencionalmente falso: fit debe usar la referencia de sus propias señales.
    modelo.fit(muestra, ['alto']*len(muestra))
    assert set(modelo.classes_) == {'bajo', 'medio', 'alto'}
    assert modelo.referencia_['poblacion_referencia_n'] == len(muestra)
    assert modelo.pipeline_.named_steps['preparar'].feature_names_in_.tolist() == FEATURES


def test_indicadores_categoricos_son_binarios_y_no_hay_missingindicator():
    df, _ = datos_y_metadata()
    train = df[df.particion.eq('entrenamiento')].copy()
    for c in ['generos', 'estudio']:
        train[c] = train[c].map(json.loads)
    modelo = joblib.load(ROOT / 'models/modelo_popularidad.joblib')
    prep = modelo.named_steps['preparar']
    nombres = prep.get_feature_names_out()
    z = prep.transform(train[FEATURES])
    assert not any('missingindicator' in n for n in nombres)
    categoricas = [i for i, n in enumerate(nombres) if not n.startswith('notas__')]
    assert set(np.unique(z[:, categoricas])) <= {0., 1.}
    assert not prep.named_transformers_['notas'].named_steps['imputar'].add_indicator


def test_joblib_carga_y_predice_desde_proceso_limpio_sin_src(tmp_path):
    codigo = '''import sys,joblib,pandas as pd
p=joblib.load(sys.argv[1])
fila=pd.DataFrame([{'generos':['RPG'],'estudio':'Nuevo','decada':2020,'Rating':4.0,'Metacritic Rating':85.0}])
assert p.predict(fila)[0] in ['bajo','medio','alto']
assert 'src' not in sys.modules
print('CARGA_PORTATIL_CORRECTA')
'''
    env = dict(os.environ)
    env.pop('PYTHONPATH', None)
    salida = subprocess.run([sys.executable, '-c', codigo, str(ROOT / 'models/modelo_popularidad.joblib')],
                            cwd=tmp_path, env=env, capture_output=True, text=True, timeout=30)
    assert salida.returncode == 0, salida.stderr
    assert 'CARGA_PORTATIL_CORRECTA' in salida.stdout


def test_formulario_exige_nota_o_ausencia_explicita_y_muestra_vecinos():
    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=120)
    assert not app.exception
    # Validar que si no hay géneros seleccionados se muestra advertencia sin excepción
    app.multiselect[0].set_value([])
    app.button[0].click().run()
    assert not app.exception
    assert app.warning and not any('Nivel estimado' in h.value for h in app.subheader)
    # Al seleccionar géneros y ejecutar, muestra predicción y los 5 vecinos
    app.multiselect[0].set_value(['RPG', 'Adventure'])
    app.slider[0].set_value(85)
    app.slider[1].set_value(4.2)
    app.button[0].click().run()
    assert not app.exception
    assert any('Nivel estimado' in h.value for h in app.subheader)
    assert len(app.dataframe[0].value) == 5


def test_ausencia_habilita_campos_sin_enviar_y_acepta_escala_completa():
    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=120)
    app.slider[0].set_value(100)
    app.slider[1].set_value(5.0)
    app.button[0].click().run()
    assert not app.exception
    assert any('Nivel estimado' in h.value for h in app.subheader)
    app.checkbox[0].check().run()
    app.button[0].click().run()
    assert not app.exception
    assert len(app.dataframe[0].value) == 5


def test_cambio_de_artefactos_invalida_clave_de_cache(tmp_path, monkeypatch):
    import src.ui as ui
    import src.pipeline as pipeline
    for nombre in ['CLEAN', 'MODELS', 'REPORTS']:
        monkeypatch.setattr(ui, nombre, tmp_path)
    monkeypatch.setattr(pipeline, 'huella_pipeline', lambda: 'codigo-sin-cambios')
    llamadas = []
    monkeypatch.setattr(ui, '_resources', lambda huella, estado: llamadas.append((huella, estado)))
    archivo = tmp_path / 'metadata.json'
    archivo.write_text('{}')
    ui.resources()
    archivo.write_text('{"cambio": true}')
    ui.resources()
    archivo.unlink()
    ui.resources()
    assert llamadas[0] != llamadas[1] != llamadas[2]


def test_vecinos_no_necesitan_conteos_y_son_solo_entrenamiento():
    from src.similitud import cinco_vecinos
    df, _ = datos_y_metadata()
    modelo = joblib.load(ROOT / 'models/modelo_popularidad.joblib')
    fila = pd.DataFrame([{'generos':['RPG'], 'estudio':[], 'decada':2020, 'Rating':4., 'Metacritic Rating':85.}])
    vecinos = cinco_vecinos(fila, modelo)
    assert len(vecinos) == vecinos.id_juego.nunique() == 5
    assert set(vecinos.id_juego) <= set(df.loc[df.particion.eq('entrenamiento'), 'id_juego'])
    assert {'cluster_kmeans', 'cluster_dbscan'} <= set(vecinos)


def test_pantalla_error_cuando_falta_artefacto(monkeypatch, caplog):
    import src.ui as ui
    mensajes_error = []
    detenidos = []
    monkeypatch.setattr(ui, '_resources', lambda huella, estado: (_ for _ in ()).throw(FileNotFoundError('Falta modelo_popularidad.joblib')))
    monkeypatch.setattr(ui.st, 'error', lambda msg: mensajes_error.append(msg))
    monkeypatch.setattr(ui.st, 'stop', lambda: detenidos.append(True))
    ui.resources()
    assert detenidos == [True]
    assert mensajes_error == ['No se pudo cargar el observatorio. Recarga la página para volver a intentarlo.']
    assert 'Falta modelo_popularidad.joblib' in caplog.text


def test_recarga_automatica_si_src_ui_estaba_en_memoria_antigua(monkeypatch):
    import src.ui as ui
    monkeypatch.delattr(ui, 'asset_b64', raising=False)
    app = AppTest.from_file(str(ROOT / 'app.py')).run(timeout=60)
    assert not app.exception
    assert hasattr(ui, 'asset_b64')


def test_menu_unico_en_sidebar_y_sin_bloques_codigo_html_incrustado():
    paginas = [
        'app.py',
        'pages/1_Exploracion.py',
        'pages/2_Prediccion.py',
        'pages/3_Acerca_del_modelo.py',
    ]
    for rel in paginas:
        app = AppTest.from_file(str(ROOT / rel)).run(timeout=60)
        assert not app.exception, f'Excepción en {rel}: {app.exception}'
        sidebar_mds = [m.value for m in app.sidebar.markdown]
        main_mds = [m.value for m in app.main.markdown]
        # 1. El menú P5Menu (<div class="p5-menu-stage">) DEBE estar en el sidebar y NUNCA en main
        assert sum('<div class="p5-menu-stage"' in m for m in sidebar_mds) == 1, f'Falta menú P5 en sidebar de {rel}'
        assert sum('<div class="p5-menu-stage"' in m for m in main_mds) == 0, f'Menú duplicado en main de {rel}'
        # 2. Ningún bloque HTML (<div ...) debe tener líneas con >= 4 espacios de sangría que CommonMark convierta en <pre><code>
        for m in [*sidebar_mds, *main_mds]:
            if m.lstrip().startswith('<div'):
                for line in m.splitlines():
                    assert not line.startswith('    '), f'Línea con sangría >=4 en HTML de {rel}: {line[:50]}'
