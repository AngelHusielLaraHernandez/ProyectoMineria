# Carpeta: Final/tests

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## test_auditoria.py

Ruta: `Final/tests/test_auditoria.py` · Bytes: 4119 · SHA-256: `f48de30c66b70472f8af5d85902f55e556cda8af37e21af7a3c1b693294c8ada`

````text
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
    assert 'clustering_03_perfiles.csv' in app


def test_comparacion_weka_es_ejecucion_y_misma_fuente():
    manifest = json.loads((REPORTS / 'weka/ejecucion.json').read_text())
    tabla = pd.read_csv(REPORTS / 'weka/comparacion.csv')
    assert set(tabla.herramienta) == {'Weka 3.8.6', 'sklearn'}
    assert len(tabla) == 6 and tabla.n.eq(887).all()
    assert manifest['sha256_dataset_depurado'] == hashlib.sha256((CLEAN / 'dataset_depurado.csv').read_bytes()).hexdigest()
    assert (REPORTS / 'weka/k2_stdout.txt').stat().st_size > 1000

````

## test_auditoria2.py

Ruta: `Final/tests/test_auditoria2.py` · Bytes: 9418 · SHA-256: `272c725d250f6c74b89e84c94b4dffbb7129447f5c59c73476e1bdb0f90eef85`

````text
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


def test_pantalla_error_tematica_cuando_falta_artefacto(monkeypatch):
    import src.ui as ui
    mensajes_error = []
    detenidos = []
    monkeypatch.setattr(ui, '_resources', lambda huella, estado: (_ for _ in ()).throw(FileNotFoundError('Falta modelo_popularidad.joblib')))
    monkeypatch.setattr(ui.st, 'error', lambda msg: mensajes_error.append(msg))
    monkeypatch.setattr(ui.st, 'stop', lambda: detenidos.append(True))
    ui.resources()
    assert detenidos == [True]
    assert any('CRITICAL ALERT / MISSION FAILED' in m and 'python -m src.pipeline' in m for m in mensajes_error)


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

````

## test_clustering.py

Ruta: `Final/tests/test_clustering.py` · Bytes: 4024 · SHA-256: `99f28c00c7328cad44fd3b87656d83bf3d48dddf6393932e69dedb700f8917a2`

````text
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

````

## test_dashboard.py

Ruta: `Final/tests/test_dashboard.py` · Bytes: 839 · SHA-256: `0256d739058db5a2af565a9c0f0f684b6d06517d9b073bd8b51387d9c310c555`

````text
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

````

## test_inferencia.py

Ruta: `Final/tests/test_inferencia.py` · Bytes: 2246 · SHA-256: `30235d88ef5acc7071ea03646fd7d447cca5b86c3acfb73a115264f2c0dccc3c`

````text
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

````

## test_limpieza.py

Ruta: `Final/tests/test_limpieza.py` · Bytes: 8464 · SHA-256: `ececa278a6d9d0c76c574d8c1b24ad191e9ed420713334e48b5da47d888f63ff`

````text
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

````

## test_modelo.py

Ruta: `Final/tests/test_modelo.py` · Bytes: 4564 · SHA-256: `b6f5c81f43ad7e047696b06aac9083a5e79902b9dd35bfd2016070e24700504f`

````text
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
    assert meta['modelo'] == tabla.sort_values('f1_macro_cv', ascending=False).iloc[0].modelo
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

````

## test_pipeline.py

Ruta: `Final/tests/test_pipeline.py` · Bytes: 4625 · SHA-256: `b8c010effa91fc3edb8823da62132dc9d40325cda7d192f18433019e62dc014e`

````text
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
    pendientes = df.loc[df.conflicto_historico_pendiente]
    assert set(pendientes.id_juego) == {117, 140, 296}
    assert not pendientes.elegible_analisis.any()
    assert not any(c.endswith('_USD') or c == 'unidades_vendidas_estimadas' for c in df.columns)
    assert len(df) == json.loads((REPORTS / 'inspeccion.json').read_text())['filas_limpias']
    assert not set(['rating_100', 'gap', 'gap_real', 'studio_main', 'publisher_main']) & set(df.columns)
    original = ROOT.parent / 'Proyecto' / 'data' / 'processed' / 'games_curated.csv'
    if original.exists():
        assert RAW.read_bytes() == original.read_bytes()


def test_objetivo_fijo_y_predictores_no_contienen_senales():
    from src.objetivo import ajustar_referencia, aplicar_referencia
    from collections import Counter
    df = pd.read_csv(CLEAN / 'juegos_modelo.csv')
    train = df[df.particion.eq('entrenamiento')]
    test = df[df.particion.eq('prueba')]
    model = joblib.load(MODELS / 'modelo_popularidad.joblib')
    metadata = json.loads((MODELS / 'metadata.json').read_text())
    assert set(train.grupo_titulo).isdisjoint(test.grupo_titulo)
    definicion = ajustar_referencia(train)
    esperado = aplicar_referencia(df, definicion)
    np.testing.assert_allclose(metadata['definicion_objetivo']['cortes'], definicion['cortes'])
    assert (esperado.nivel_popularidad.to_numpy() == df.nivel_popularidad.to_numpy()).all()
    assert set(FEATURES).isdisjoint(SIGNALS + ['popularidad_indice', 'nivel_popularidad'])
    encoder = model.named_steps['preparar'].named_transformers_['estudio']
    conteos = Counter(v for row in train.estudio.map(json.loads) for v in row)
    assert set(encoder.vocabulario_) == {v for v, n in conteos.items() if n >= 10}


def test_small_groups_do_not_produce_correlations():
    df = pd.DataFrame({'generos': [['RPG']] * 5, 'Rating': [1, 2, 3, 4, 5],
                       'critica_verificada_csv': [30, 50, 60, 80, 90]})
    row = grouped_correlations(df, 'generos').iloc[0]
    assert row['n'] == 5 and pd.isna(row['r'])


def test_unknown_organizations_and_missing_ratings():
    model = joblib.load(MODELS / 'modelo_popularidad.joblib')
    row = pd.DataFrame([{'generos': ['Género desconocido'], 'estudio': ['Estudio nuevo'],
                         'decada': 2030, 'Rating': np.nan, 'Metacritic Rating': np.nan}])
    assert model.predict(row)[0] in ['bajo', 'medio', 'alto']


def test_arff_partitions_readable():
    for name in ['entrenamiento', 'prueba']:
        data, meta = arff.loadarff(CLEAN / f'{name}_weka.arff')
        exported = pd.read_csv(CLEAN / f'{name}_orange.csv')
        assert len(data) == len(exported)
        assert len(meta.names()) == len(exported.columns)


@pytest.mark.parametrize('page', ['app.py', 'pages/1_Exploracion.py',
                                  'pages/2_Prediccion.py', 'pages/3_Acerca_del_modelo.py'])
def test_app_pages(page):
    app = AppTest.from_file(str(ROOT / page)).run(timeout=60)
    assert not app.exception, [x.message for x in app.exception]
    if 'Prediccion' in page:
        app.button[0].click().run(timeout=30)
        assert not app.exception
        assert any('Nivel estimado' in x.value for x in app.subheader)
    if page == 'app.py':
        app.text_input[0].set_value('NINGUN_JUEGO_123456').run()
        assert not app.exception
        assert app.info

````

## test_visualizacion.py

Ruta: `Final/tests/test_visualizacion.py` · Bytes: 1955 · SHA-256: `15673f94de9e3f85a948e14c049a14ecd489b129350cd3e8ae0624b6b10d5c51`

````text
"""Verifica que la presentación conserve datos, errores y escalas."""
import plotly.graph_objects as go
import pytest
from src.visualizacion import etiquetas_fuera_del_error, COLOR_SENALES


def test_etiqueta_vertical_separa_error_sin_cambiar_datos():
    fig = go.Figure(go.Bar(x=['NB', 'RF'], y=[.549, .557], error_y=dict(array=[.06, .04])))
    fig.update_yaxes(range=[0, .72])
    etiquetas_fuera_del_error(fig, desplazamiento_categoria=-.8/3)
    assert list(fig.data[0].y) == [.549, .557]
    assert list(fig.data[0].error_y.array) == [.06, .04]
    assert list(fig.layout.yaxis.range) == [0, .72]
    assert fig.layout.annotations[0].y == pytest.approx(.609)
    assert fig.layout.annotations[0].x == pytest.approx(-.8/3)
    assert fig.layout.annotations[0].yshift > 0


def test_etiqueta_horizontal_queda_despues_del_intervalo():
    fig = go.Figure(go.Bar(x=[.0833], y=['Rating'], orientation='h', error_x=dict(array=[.022])))
    fig.update_xaxes(range=[0, .115])
    etiquetas_fuera_del_error(fig, sufijo=' F1')
    etiqueta = fig.layout.annotations[0]
    assert etiqueta.x == pytest.approx(.1053)
    assert etiqueta.xanchor == 'left' and etiqueta.xshift > 0
    assert etiqueta.text == '0.0833 F1'
    assert list(fig.data[0].x) == [.0833]
    assert list(fig.data[0].error_x.array) == [.022]
    assert list(fig.layout.xaxis.range) == [0, .115]


def test_colores_semanticos_consistentes():
    assert COLOR_SENALES == {'Plays': '#00CFFF', 'Backlogs': '#8B9CFF', 'Wishlist': '#FFD166'}


def test_tema_logaritmico_conserva_escala_datos_y_rango():
    from src.ui import p5_plotly_layout
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[10, 100, 1000]))
    fig.update_yaxes(type='log', range=[1, 3])
    p5_plotly_layout(fig, title='Comprobación de escala')
    assert fig.layout.yaxis.type == 'log'
    assert fig.layout.yaxis.dtick == 1
    assert list(fig.layout.yaxis.range) == [1, 3]
    assert list(fig.data[0].y) == [10, 100, 1000]

````

