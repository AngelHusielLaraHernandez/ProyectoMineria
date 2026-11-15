"""Pruebas de regresión de lógica web, seguridad HTML, UI y artefactos corruptos."""
import hashlib
import inspect
import json
import pickle
import re
import shutil
import sys

import joblib
import numpy as np
import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

import src.data as data_mod
import src.inferencia as inferencia_mod
import src.pipeline as pipeline_mod
import src.similitud as similitud_mod
import src.ui as ui
import src.visualizacion as vis_mod
import vista_graficas as vg_mod
from src.config import CLEAN, MODELS, REPORTS, ROOT
from src.similitud import cinco_vecinos
from src.visualizacion import FONT_SANS, PALETA


class _PrepProxy:
    """Expone vocabulario de géneros extendido delegando transform() al preprocesador real."""

    def __init__(self, real_prep, extra_generos):
        self._real = real_prep
        gen_real = real_prep.named_transformers_['generos']
        self.named_transformers_ = {
            **real_prep.named_transformers_,
            'generos': type('_GenVocab', (), {'vocabulario_': [*gen_real.vocabulario_, *extra_generos]})(),
        }

    def transform(self, X):
        return self._real.transform(X)


class _PipelineProxy:
    """Envuelve el Pipeline real para habilitar opciones extra en AppTest sin mutar el modelo."""

    def __init__(self, real_pipeline, extra_generos):
        self._real = real_pipeline
        self.classes_ = real_pipeline.classes_
        self.named_steps = {
            **real_pipeline.named_steps,
            'preparar': _PrepProxy(real_pipeline.named_steps['preparar'], extra_generos),
        }

    def predict_proba(self, X):
        return self._real.predict_proba(X)


# ---------------------------------------------------------------------------
# 1. Similitud (src/similitud.py)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    'fila_dict',
    [
        {'generos': ['RPG', 'Adventure'], 'estudio': ['Nintendo'], 'decada': 2020, 'Rating': 4.2, 'Metacritic Rating': 88.0},
        {'generos': ['Indie'], 'estudio': ['Otro'], 'decada': -1, 'Rating': 3.5, 'Metacritic Rating': np.nan},
    ],
)
def test_cinco_vecinos_dos_args_coincide_con_bundle_y_df_clusters(monkeypatch, fila_dict):
    modelo = joblib.load(MODELS / 'modelo_popularidad.joblib')
    vecinos_bundle = joblib.load(MODELS / 'vecinos_popularidad.joblib')
    df_clusters = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
    fila = pd.DataFrame([fila_dict])

    res_2args = cinco_vecinos(fila, modelo)
    res_con_vecinos = cinco_vecinos(fila, modelo, vecinos=vecinos_bundle)

    # Con vecinos y df_clusters explícitos no debe releer artefactos de disco.
    monkeypatch.setattr(similitud_mod.joblib, 'load', lambda *a, **k: (_ for _ in ()).throw(AssertionError('joblib.load inesperado')))
    monkeypatch.setattr(similitud_mod.pd, 'read_csv', lambda *a, **k: (_ for _ in ()).throw(AssertionError('pd.read_csv inesperado')))
    res_4args = cinco_vecinos(fila, modelo, vecinos=vecinos_bundle, df_clusters=df_clusters)

    assert len(res_2args) == 5
    pd.testing.assert_frame_equal(res_2args, res_con_vecinos)
    pd.testing.assert_frame_equal(res_2args, res_4args)


# ---------------------------------------------------------------------------
# 2. Página de predicción (pages/2_Prediccion.py)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize('genero_excluido,n_esperado', [('Pinball', 1), ('Music', 18)])
def test_prediccion_muestra_resultados_en_orden_con_menos_de_20_pares(monkeypatch, genero_excluido, n_esperado):
    corr_real = pd.read_csv(REPORTS / 'tables/correlacion_generos.csv')
    fila_csv = corr_real.loc[corr_real['grupo'] == genero_excluido].iloc[0]
    assert fila_csv['estado'] != 'incluido'
    assert pd.notna(fila_csv['brecha_absoluta_media'])

    df_real, bundle_real, analysis_real = ui.resources()
    bundle_proxy = {**bundle_real, 'pipeline': _PipelineProxy(bundle_real['pipeline'], [genero_excluido])}
    monkeypatch.setattr(ui, 'resources', lambda: (df_real, bundle_proxy, analysis_real))

    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    assert not app.exception

    app.multiselect[0].set_value([genero_excluido])
    app.button[0].click().run(timeout=60)
    assert not app.exception

    html_total = '\n'.join(m.value for m in app.main.markdown)
    assert f'(n = {n_esperado} pares) hacen falta al menos 20 juegos con ambas notas' in html_total

    posiciones = [
        html_total.index('PROBABILIDAD CALIBRADA POR NIVEL'),
        html_total.index('GRUPO DE JUEGOS PARECIDOS'),
        html_total.index('DIFERENCIA ENTRE NOTAS'),
        html_total.index('Cinco juegos parecidos'),
    ]
    assert posiciones == sorted(posiciones)


def test_prediccion_escapa_html_en_title_y_generos_especiales(monkeypatch):
    genero_xss = 'RPG <script>alert(1)</script> & Acción'
    titulo_xss = 'Juego <img src=x onerror=alert(2)> & "Prueba"'
    genero_vecino_xss = 'Acción & <Aventura>'
    perfil_xss = 'Perfil <b onclick=evil()>Especial & Único</b>'

    df_real, bundle_real, analysis_real = ui.resources()
    df_mod = df_real.copy()
    bundle_proxy = {**bundle_real, 'pipeline': _PipelineProxy(bundle_real['pipeline'], [genero_xss])}

    def _cinco_vecinos_xss(fila, pipeline_arg, vecinos=None, df_clusters=None):
        res = cinco_vecinos(fila, bundle_real['pipeline'], vecinos=bundle_real['vecinos']).copy()
        id_objetivo = int(res.iloc[0]['id_juego'])
        res.loc[res.index[0], 'Title'] = titulo_xss
        df_mod.loc[df_mod['id_juego'] == id_objetivo, 'generos'] = pd.Series(
            [[genero_vecino_xss]], index=df_mod.index[df_mod['id_juego'] == id_objetivo]
        )
        return res

    orig_cached_report = ui._cached_report

    def _cached_report_xss(name, file_hash):
        df_rep = orig_cached_report(name, file_hash).copy()
        if name == 'tables/perfiles_clusters.csv':
            df_rep['perfil_propuesto'] = perfil_xss
        return df_rep

    monkeypatch.setattr(ui, 'resources', lambda: (df_mod, bundle_proxy, analysis_real))
    monkeypatch.setattr(similitud_mod, 'cinco_vecinos', _cinco_vecinos_xss)
    monkeypatch.setattr(ui, '_cached_report', _cached_report_xss)

    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    app.multiselect[0].set_value([genero_xss])
    app.button[0].click().run(timeout=60)
    assert not app.exception

    html_total = '\n'.join(m.value for m in app.main.markdown)
    assert '&lt;script&gt;alert(1)&lt;/script&gt; &amp; Acción' in html_total
    assert '&lt;SCRIPT&gt;ALERT(1)&lt;/SCRIPT&gt; &amp; ACCIÓN' in html_total
    assert '&lt;img src=x onerror=alert(2)&gt; &amp; &quot;Prueba&quot;' in html_total
    assert 'Acción &amp; &lt;Aventura&gt;' in html_total
    assert 'Perfil &lt;b onclick=evil()&gt;Especial &amp; Único&lt;/b&gt;' in html_total
    for crudo in ['<script>alert(1)</script>', '<img src=x', '<Aventura>', '<b onclick=evil()>']:
        assert crudo not in html_total


# ---------------------------------------------------------------------------
# 3. Página Acerca del modelo (pages/3_Acerca_del_modelo.py)
# ---------------------------------------------------------------------------
def test_acerca_modelo_activo_y_contraste_matriz_confusion():
    app = AppTest.from_file(str(ROOT / 'pages/3_Acerca_del_modelo.py')).run(timeout=60)
    assert not app.exception

    shell_html = next(m.value for m in app.main.markdown if '<div class="sp-shell"' in m.value)
    assert '<div class="sp-right" data-sp-id="alg-0" style="display:block;">\n<div class="sp-tag">MODELO ACTIVO</div>\n<div class="sp-right-title">RANDOM FOREST</div>' in shell_html
    assert '<div class="sp-tag">CANDIDATO COMPARADO</div>\n<div class="sp-right-title">RED NEURONAL MLP</div>' in shell_html

    assert len(app.dataframe) == 5
    assert all(not df_el.value.empty for df_el in app.dataframe)

    charts = app.get('plotly_chart')
    assert len(charts) == 4
    for pc in charts:
        spec = json.loads(pc.proto.spec)
        config = json.loads(pc.proto.config or '{}')
        assert spec['layout']['font']['family'] == FONT_SANS
        assert spec['layout']['margin']['t'] >= 44
        assert 'toImage' not in config.get('modeBarButtonsToRemove', [])

    cm_spec = json.loads(charts[1].proto.spec)
    annotations = cm_spec['layout']['annotations']
    assert len(annotations) == 9
    max_val = max(int(a['text']) for a in annotations)
    for ann in annotations:
        esperado = PALETA['bg-primary'] if int(ann['text']) >= 0.45 * max_val else PALETA['text-primary']
        assert ann['font']['color'] == esperado


def test_acerca_modelo_maneja_campos_faltantes_y_escapa_mejores_parametros(monkeypatch):
    df_real, bundle_real, analysis_real = ui.resources()
    metricas_sin_diag = json.loads(json.dumps(bundle_real['metricas']))
    metricas_sin_diag.pop('diagnostico_ausencia', None)
    metricas_sin_diag['modelo'] = 'ModeloCustom_X'
    metricas_sin_diag['metricas']['matriz_confusion'] = [[45, 44, 0], [0, 100, 0], [0, 0, 10]]
    bundle_mod = {**bundle_real, 'metricas': metricas_sin_diag}

    orig_cached_report = ui._cached_report
    payload_xss = '{"param": "<script>alert(9)</script> & \'test\'"}'

    def _cached_report_mod(name, file_hash):
        df_rep = orig_cached_report(name, file_hash).copy()
        if name == 'tables/comparacion_prueba_actual_e_historica.csv':
            fila_extra = df_rep.iloc[-1].copy()
            fila_extra['modelo'] = 'ModeloCustom_X'
            fila_extra['f1_macro_cv'] = 0.40
            fila_extra['mejores_parametros'] = payload_xss
            df_rep = pd.concat([df_rep, pd.DataFrame([fila_extra])], ignore_index=True)
        return df_rep

    monkeypatch.setattr(ui, 'resources', lambda: (df_real, bundle_mod, analysis_real))
    monkeypatch.setattr(ui, '_cached_report', _cached_report_mod)

    app = AppTest.from_file(str(ROOT / 'pages/3_Acerca_del_modelo.py')).run(timeout=60)
    assert not app.exception

    html_total = '\n'.join(m.value for m in app.main.markdown)
    assert '<div class="sp-tag">MODELO ACTIVO</div>\n<div class="sp-right-title">ModeloCustom_X</div>' in html_total
    assert '&lt;script&gt;alert(9)&lt;/script&gt; &amp; &#x27;test&#x27;' in html_total
    assert '<script>alert(9)</script>' not in html_total
    assert all('Diagnóstico de Imputación' not in expander.label for expander in app.expander)

    cm_spec = json.loads(app.get('plotly_chart')[1].proto.spec)
    colores_por_texto = {ann['text']: ann['font']['color'] for ann in cm_spec['layout']['annotations']}
    assert colores_por_texto['45'] == PALETA['bg-primary']
    assert colores_por_texto['44'] == PALETA['text-primary']


# ---------------------------------------------------------------------------
# 4. Página Inicio (app.py) y UI (src/ui.py)
# ---------------------------------------------------------------------------
def test_app_busqueda_con_resultado_y_vacia_y_sin_hero_png():
    app = AppTest.from_file(str(ROOT / 'app.py')).run(timeout=60)
    assert not app.exception
    html_inicial = '\n'.join(m.value for m in app.main.markdown)
    assert 'alt="Take Your Heart"' not in html_inicial
    assert '3 CASOS · DÉCADA -1' in html_inicial
    assert any(e.label == 'Cómo calculamos la popularidad' for e in app.expander)

    app.text_input[0].set_value('Persona').run(timeout=60)
    assert not app.exception
    assert len(app.dataframe) == 1
    df_res = app.dataframe[0].value
    assert not df_res.empty
    assert df_res['Title'].str.contains('persona', case=False, na=False).all()
    assert len(app.get('download_button')) == 1
    assert not any('No hay coincidencias' in info.value for info in app.info)

    app.text_input[0].set_value('TITULO_INEXISTENTE_999').run(timeout=60)
    assert not app.exception
    assert len(app.dataframe) == 0
    assert any('No hay coincidencias' in info.value for info in app.info)


def test_ui_escapa_html_y_registra_el_detalle_de_la_alerta(monkeypatch, tmp_path, caplog):
    renderizados = []
    errores = []
    monkeypatch.setattr(ui, 'FONTS_DIR', tmp_path / 'fuentes_inexistentes')
    monkeypatch.setattr(ui.st, 'markdown', lambda txt, **kw: renderizados.append(txt))
    monkeypatch.setattr(ui.st, 'error', lambda msg: errores.append(msg))

    ui.section_banner('<script>s()</script> & Título', '<img src=x onerror=alert(1)> & Sub')
    ui.render_lb_rb_nav('<b>Sección & Nav</b>')
    ui.render_critical_alert('<script>boom()</script> & "fallo"')

    html_combinado = '\n'.join(renderizados)
    assert '&lt;script&gt;s()&lt;/script&gt; &amp; Título' in html_combinado
    assert '&lt;img src=x onerror=alert(1)&gt; &amp; Sub' in html_combinado
    assert '&lt;b&gt;Sección &amp; Nav&lt;/b&gt;' in html_combinado
    assert '<script>s()</script>' not in html_combinado
    assert '<img src=x' not in html_combinado
    assert '<b>Sección' not in html_combinado
    assert '<script>boom()</script>' in caplog.text
    assert errores == ['No se pudo cargar el observatorio. Recarga la página para volver a intentarlo.']


@pytest.mark.parametrize('exc', [EOFError('archivo truncado'), pickle.UnpicklingError('pickle inválido')])
def test_ui_resources_captura_eof_y_unpickling_error_directo(monkeypatch, exc):
    errores = []
    detenidos = []
    monkeypatch.setattr(ui, '_resources', lambda huella, estado: (_ for _ in ()).throw(exc))
    monkeypatch.setattr(ui.st, 'error', lambda msg: errores.append(msg))
    monkeypatch.setattr(ui.st, 'stop', lambda: detenidos.append(True))

    ui.resources()
    assert detenidos == [True]
    assert errores == ['No se pudo cargar el observatorio. Recarga la página para volver a intentarlo.']


@pytest.mark.parametrize('bytes_corruptos,exc_esperada', [(b'', EOFError), (b'g0\n.', pickle.UnpicklingError)])
def test_ui_resources_captura_joblib_corrupto_end_to_end(monkeypatch, tmp_path, bytes_corruptos, exc_esperada):
    tmp_models = tmp_path / 'models'
    tmp_reports = tmp_path / 'reports'
    tmp_models.mkdir()
    tmp_reports.mkdir()

    shutil.copy2(MODELS / 'metadata.json', tmp_models / 'metadata.json')
    shutil.copy2(MODELS / 'vecinos_popularidad.joblib', tmp_models / 'vecinos_popularidad.joblib')
    modelo_corrupto = tmp_models / 'modelo_popularidad.joblib'
    modelo_corrupto.write_bytes(bytes_corruptos)
    with pytest.raises(exc_esperada):
        joblib.load(modelo_corrupto)
    shutil.copy2(REPORTS / 'clustering_03_parametros.json', tmp_reports / 'clustering_03_parametros.json')

    def _sha(ruta):
        return hashlib.sha256(ruta.read_bytes()).hexdigest()

    manifiesto = {
        'sha256_modelo_popularidad': _sha(tmp_models / 'modelo_popularidad.joblib'),
        'sha256_metadata_modelo': _sha(tmp_models / 'metadata.json'),
        'sha256_vecinos': _sha(tmp_models / 'vecinos_popularidad.joblib'),
        'sha256_dataset_depurado': _sha(CLEAN / 'dataset_depurado.csv'),
        'sha256_dataset_con_clusters': _sha(CLEAN / 'dataset_con_clusters.csv'),
        'sha256_reportes_app': {
            'clustering_03_parametros.json': _sha(tmp_reports / 'clustering_03_parametros.json'),
        },
    }
    (tmp_reports / 'manifest.json').write_text(json.dumps(manifiesto), encoding='utf-8')

    errores = []
    detenidos = []
    monkeypatch.setattr(pipeline_mod, 'REPORTES_APP', ('clustering_03_parametros.json',))
    monkeypatch.setattr(ui, 'MODELS', tmp_models)
    monkeypatch.setattr(ui, 'REPORTS', tmp_reports)
    monkeypatch.setattr(ui.st, 'error', lambda msg: errores.append(msg))
    monkeypatch.setattr(ui.st, 'stop', lambda: detenidos.append(True))

    ui.resources()
    assert detenidos == [True]
    assert errores == ['No se pudo cargar el observatorio. Recarga la página para volver a intentarlo.']


def test_ui_setup_render_page_transition_solo_al_cambiar_de_pagina(monkeypatch):
    estado_sesion = {}
    transiciones = []

    monkeypatch.setattr(ui.st, 'session_state', estado_sesion)
    monkeypatch.setattr(ui.st, 'set_page_config', lambda **kw: None)
    monkeypatch.setattr(ui, 'inject_p5_css', lambda: None)
    monkeypatch.setattr(ui, 'render_page_transition', lambda variant='default': transiciones.append(variant))
    monkeypatch.setattr(ui, 'render_p5_main_menu', lambda **kw: None)
    monkeypatch.setattr(ui, 'render_sidebar_audio', lambda: None)
    monkeypatch.setattr(ui.st, 'title', lambda *a, **kw: None)
    monkeypatch.setattr(ui.st, 'caption', lambda *a, **kw: None)
    monkeypatch.setattr(ui, '_inject_parent_interactive_engine', lambda: None)

    ui.setup('Inicio', transition='default', menu_idx=0)
    ui.setup('Inicio', transition='default', menu_idx=0)
    ui.setup('Exploración', transition='about', menu_idx=1)
    ui.setup('Exploración', transition='about', menu_idx=1)
    assert transiciones == ['default', 'about']


def test_ui_apptest_transicion_solo_en_carga_inicial_no_en_rerun():
    app_inicio = AppTest.from_file(str(ROOT / 'app.py')).run(timeout=60)
    assert sum('<div class="p5-transition-layer"' in m.value for m in app_inicio.main.markdown) == 1
    app_inicio.text_input[0].set_value('Zelda').run(timeout=60)
    assert sum('<div class="p5-transition-layer"' in m.value for m in app_inicio.main.markdown) == 0

    app_pred = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    assert sum('<div class="p5-transition-layer"' in m.value for m in app_pred.main.markdown) == 1
    app_pred.button[0].click().run(timeout=60)
    assert sum('<div class="p5-transition-layer"' in m.value for m in app_pred.main.markdown) == 0


def test_recarga_en_caliente_actualiza_modulos_obsoletos(monkeypatch):
    # Simula sesión en vivo con módulos previos en sys.modules (firma antigua de 2 args y v8).
    monkeypatch.setattr(similitud_mod, 'cinco_vecinos', lambda fila, pipeline: None)
    for mod in (data_mod, inferencia_mod, similitud_mod, vis_mod, vg_mod):
        monkeypatch.setattr(mod, '_MOD_VERSION', 'p5-v8-neon', raising=False)
    monkeypatch.setattr(ui, '_UI_VERSION', 'p5-v8-neon', raising=False)
    monkeypatch.delattr(data_mod, 'asegurar_modulos_vigentes')

    app_pred = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    assert not app_pred.exception
    app_pred.button[0].click().run(timeout=60)
    assert not app_pred.exception
    assert len(app_pred.dataframe[0].value) == 5

    sim_vigente = sys.modules['src.similitud']
    assert 'vecinos' in inspect.signature(sim_vigente.cinco_vecinos).parameters
    assert getattr(sys.modules['src.ui'], '_UI_VERSION', None) == 'p5-v14-menu'
    for nombre in ('src.data', 'src.inferencia', 'src.similitud', 'src.visualizacion', 'vista_graficas'):
        assert getattr(sys.modules[nombre], '_MOD_VERSION', None) == 'p5-v14-menu'

    # Incluso si _MOD_VERSION coincidiera, detectar firma antigua de cinco_vecinos debe recargar src.similitud.
    monkeypatch.setattr(sim_vigente, 'cinco_vecinos', lambda fila, pipeline: None)
    recargados = sys.modules['src.data'].asegurar_modulos_vigentes()
    assert 'src.similitud' in recargados
    assert 'vecinos' in inspect.signature(sys.modules['src.similitud'].cinco_vecinos).parameters


def test_prediccion_recarga_la_firma_anterior_a_la_calibracion(monkeypatch):
    def predecir_anterior(pipeline, generos, estudio, decada, metacritic, rating):
        raise AssertionError('Streamlit conservó la función anterior en memoria')

    monkeypatch.setattr(inferencia_mod, 'predecir_formulario', predecir_anterior)
    app = AppTest.from_file(str(ROOT / 'pages/2_Prediccion.py')).run(timeout=60)
    assert not app.exception
    assert any('PROBABILIDAD CALIBRADA POR NIVEL' in m.value for m in app.main.markdown)


def test_css_p5_banner_y_tarjetas_alinean_al_cien_por_ciento():
    css = (ROOT / 'assets/css/persona5.css').read_text(encoding='utf-8')
    bloque_banner = re.search(r'(?m)^\.p5-banner\s*\{([^}]*)\}', css)
    assert bloque_banner is not None
    reglas_banner = bloque_banner.group(1)
    assert 'display: block;' in reglas_banner
    assert 'display: inline-block;' not in reglas_banner
    assert 'width: 100%;' in reglas_banner
    assert 'box-sizing: border-box;' in reglas_banner

    for selector in ('p5-card', 'p5-card-accent', 'p5-callout-warning'):
        bloque = re.search(rf'(?m)^\.{selector}\s*\{{([^}}]*)\}}', css)
        assert bloque is not None
        assert 'width: 100%;' in bloque.group(1)
        assert 'box-sizing: border-box;' in bloque.group(1)
