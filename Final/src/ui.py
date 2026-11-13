"""Módulo UI/UX Persona 5 accesible y caché de artefactos."""
import base64
import hashlib
import html
import json
import logging
import pickle
import textwrap
import unicodedata
from pathlib import Path

import joblib
import pandas as pd
import plotly.graph_objects as go
import sklearn
import streamlit as st
import streamlit.components.v1 as components

from .config import CLEAN, MODELS, RAW, REPORTS, ROOT
from .data import load_clean
from .visualizacion import COLORWAY, FONT_SANS, PALETA

ASSETS = ROOT / 'assets'
FONTS_DIR = ASSETS / 'fonts'
AUDIO_DIR = ASSETS / 'audio'
IMG_DIR = ASSETS / 'img'
CSS_DIR = ASSETS / 'css'

P5_COLORS = {
    'black': PALETA['bg-primary'], 'surface': PALETA['bg-panel'],
    'red': PALETA['primary'], 'dark_red': PALETA['bg-chart'],
    'white': PALETA['text-primary'], 'gray': PALETA['text-secondary'],
    'yellow': PALETA['accent'], 'cyan': PALETA['primary'],
}
P5_COLORWAY = COLORWAY
_UI_VERSION = 'p5-v12-portadas'


def _p5_ascii(text: str) -> str:
    """Conserva tildes y signos admitidos por la fuente cómic local."""
    return unicodedata.normalize('NFC', str(text))


def clean_html(raw_html: str) -> str:
    """Compacta HTML multilínea eliminando sangrías y líneas vacías para evitar bloques <pre><code> en Markdown."""
    return '\n'.join(line.strip() for line in str(raw_html).splitlines() if line.strip())


def render_html(raw_html: str) -> None:
    """Renderiza HTML en Streamlit de forma segura sin que CommonMark interprete sangrías como código."""
    st.markdown(clean_html(raw_html), unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def asset_b64(rel_path: str) -> str:
    """Codifica un archivo de assets/ en Base64 usando pathlib.Path relativo a ROOT."""
    ruta = ASSETS / Path(rel_path)
    if not ruta.exists():
        return ''
    return base64.b64encode(ruta.read_bytes()).decode('ascii')


@st.cache_data(show_spinner=False)
def _audio_bytes(rel_path: str) -> bytes:
    """Lee un archivo de audio en caché para evitar lecturas repetidas por rerun."""
    ruta = ASSETS / Path(rel_path)
    return ruta.read_bytes() if ruta.exists() else b''


@st.cache_data(show_spinner=False)
def _build_global_css(css_hash: str, font_hash: str) -> str:
    """Construye el tema con fuente display en caché ligada a sus bytes."""
    font_path = FONTS_DIR / 'Persona5main.ttf'
    font_b64 = base64.b64encode(font_path.read_bytes()).decode('ascii') if font_path.exists() else ''
    font_face = ''
    if font_b64:
        font_face = (
            "@font-face { font-family: 'ComicProyecto'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; } "
            "@font-face { font-family: 'Persona5Main'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; }"
        )
    css_file = CSS_DIR / 'persona5.css'
    base_css = css_file.read_text(encoding='utf-8') if css_file.exists() else ''
    tokens = ':root {' + ''.join(f'--{k}: {v};' for k, v in PALETA.items()) + '}'
    return f'<style>{font_face}\n{tokens}\n{base_css}</style>'


def inject_p5_css() -> None:
    """Inyecta el tema visual Persona 5 y la tipografía Base64 en la vista actual."""
    css_file = CSS_DIR / 'persona5.css'
    font_path = FONTS_DIR / 'Persona5main.ttf'
    css_hash = hashlib.sha256(css_file.read_bytes()).hexdigest() if css_file.exists() else 'v0'
    font_hash = hashlib.sha256(font_path.read_bytes()).hexdigest() if font_path.exists() else 'v0'
    st.markdown(_build_global_css(css_hash, font_hash), unsafe_allow_html=True)


def render_page_transition(variant: str = 'default') -> None:
    """Renderiza las cortinas de transición animadas respetando dvh/dvw y prefers-reduced-motion."""
    if variant == 'about':
        panels = [
            (PALETA['bg-primary'], '-12dvh', '-18dvw', '86dvw', '0s', 999),
            (PALETA['text-primary'], '24dvh', '-10dvw', '72dvw', '0.05s', 998),
            (PALETA['text-primary'], '58dvh', '-14dvw', '82dvw', '0.10s', 997),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-panel" style="background:{c};top:{t};left:{l};width:{w};animation-delay:{d};z-index:{z};"></div>'
            for c, t, l, w, d, z in panels
        )
    elif variant == 'resume':
        cards = [
            ('14dvh', PALETA['bg-chart'], '0s', 'none', 999),
            ('31dvh', PALETA['text-primary'], '0.05s', '10px 0 0 #00CFFF', 998),
            ('48dvh', PALETA['text-primary'], '0.10s', '10px 0 0 #00CFFF', 997),
            ('65dvh', PALETA['bg-chart'], '0.15s', 'none', 996),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-card" style="top:{t};background:{c};animation-delay:{d};box-shadow:{sh};z-index:{z};"></div>'
            for t, c, d, sh, z in cards
        )
    else:
        stripes = [
            (PALETA['bg-primary'], '72dvw', '24dvw', '0s', 999),
            (PALETA['primary'], '80dvw', '14dvw', '0.06s', 998),
            (PALETA['text-primary'], '88dvw', '8dvw', '0.12s', 997),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-stripe" style="background:{c};left:{l};width:{w};animation-delay:{d};z-index:{z};"></div>'
            for c, l, w, d, z in stripes
        )

    render_html(
        f"""
        <div class="p5-stripe" aria-hidden="true"></div>
        <div class="p5-stripe2" aria-hidden="true"></div>
        <div class="p5-transition-layer" aria-hidden="true">{items_html}</div>
        """
    )


def render_p5_main_menu(active_idx: int = 0, compact: bool = False) -> None:
    """Renderiza el único menú principal estilo Persona 5 en la barra lateral izquierda."""
    items = [
        {'idx': 0, 'label': 'INICIO',      'font': '2.15rem', 'ox': 6,  'oy': 0, 'sx': -6, 'sy': 6},
        {'idx': 1, 'label': 'EXPLORACIÓN', 'font': '1.45rem', 'ox': 4,  'oy': 6, 'sx': -9, 'sy': -5},
        {'idx': 2, 'label': 'PREDICCIÓN',  'font': '1.55rem', 'ox': 4,  'oy': 6, 'sx': -3, 'sy': -3},
        {'idx': 3, 'label': 'MODELO',      'font': '2.15rem', 'ox': 12, 'oy': 6, 'sx': -5, 'sy': 5},
    ]

    arte_menu = ('link', 'mario', 'spider-man', 'god-of-war')
    arte_b64 = asset_b64(f'img/juegos/{arte_menu[active_idx]}.webp')
    art_html = (
        f'<img class="p5-stage-art" src="data:image/webp;base64,{arte_b64}" alt="" aria-hidden="true"/>'
        if arte_b64 else ''
    )

    rutas = ['/', '/Exploracion', '/Prediccion', '/Acerca_del_modelo']
    rows_html = ''
    for i, item in enumerate(items):
        is_active = i == active_idx
        is_act = 'active' if is_active else ''
        aria_curr = ' aria-current="page"' if is_active else ''
        fs = item['font']
        ox = item['ox']
        oy = item['oy']
        delay = i * 80
        rows_html += (
            f'<a href="{rutas[i]}" target="_self" class="p5-row {is_act}" aria-label="{item["label"]}"{aria_curr} data-nav-index="{item["idx"]}" '
            f'style="margin-left:{ox}px;margin-top:{oy}px;animation-delay:{delay}ms;">'
            f'<div class="p5-glow"></div>'
            f'<div class="p5-skew-wrap" style="transform:skewX({item["sx"]}deg) skewY({item["sy"]}deg);">'
            f'<div class="p5-shadow-tri"></div>'
            f'<div class="p5-highlight"></div>'
            f'<div class="p5-label-wrap">'
            f'<span class="p5-label-base p5-label-dark" style="font-size:{fs};">{item["label"]}</span>'
            f'<span class="p5-label-base p5-label-bright" aria-hidden="true" style="font-size:{fs};">{item["label"]}</span>'
            f'</div>'
            f'</div>'
            f'</a>'
        )

    compact_attr = 'true' if compact else 'false'
    html_block = (
        f'<div class="p5-menu-stage" data-compact="{compact_attr}">'
        f'{art_html}'
        f'<div class="p5-name-tag" aria-hidden="true">'
        f'<span>Observatorio</span>'
        f'<span>Videojuegos</span>'
        f'</div>'
        f'<nav class="p5-menu" aria-label="Navegación principal">'
        f'{rows_html}'
        f'</nav>'
        f'<div class="p5-hint" aria-hidden="true">'
        f'<span class="p5-hint-key">CURSOR</span><span>ELEGIR</span>'
        f'<span class="p5-hint-key">CLIC</span><span>ABRIR</span>'
        f'</div>'
        f'</div>'
    )
    with st.sidebar:
        render_html(html_block)


def render_lb_rb_nav(label: str) -> None:
    """Renderiza el cabezal decorativo de sección."""
    clean_label = html.escape(_p5_ascii(label))
    render_html(
        f"""
        <div class="sc-right-nav-bar">
            <span class="sc-nav-arrow left" aria-hidden="true">◄</span>
            <span class="sc-nav-btn" aria-hidden="true">LB</span>
            <span class="sc-nav-label">{clean_label}</span>
            <span class="sc-nav-btn" aria-hidden="true">RB</span>
            <span class="sc-nav-arrow right" aria-hidden="true">►</span>
        </div>
        """
    )


def _inject_parent_interactive_engine() -> None:
    """Inyecta en window.parent el motor de SFX (select.mp3) y eventos accesibles de pestañas."""
    select_b64 = asset_b64('audio/select.mp3')
    motor_interactivo = (ASSETS / "js/interacciones.js").read_text(encoding="utf-8")
    sfx_desactivado = json.dumps(not st.session_state.get('p5_sfx_toggle', True))
    js_code = f"""
    <script>
    (function() {{
      try {{
        const win = window.parent;
        const doc = win && win.document;
        if (!win || !doc) return;
        win.__p5SfxDisabled = {sfx_desactivado};

        if ("{select_b64}" && !win.__p5SelectSrc) {{
          win.__p5SelectSrc = "data:audio/mp3;base64,{select_b64}";
        }}

        win.playSelectSound = function() {{
          if (win.__p5SfxDisabled || !win.__p5SelectSrc) return;
          const now = Date.now();
          if (win.__p5LastSfxAt && now - win.__p5LastSfxAt < 120) return;
          win.__p5LastSfxAt = now;
          try {{
            const a = new win.Audio(win.__p5SelectSrc);
            a.volume = 0.45;
            a.play().catch(function(){{}});
          }} catch (e) {{}}
        }};

        const staleFloating = doc.getElementById('p5-floating-bgm-panel');
        if (staleFloating) staleFloating.remove();

        {motor_interactivo}
      }} catch (err) {{}}
    }})();
    </script>
    """
    components.html(js_code, height=0, width=0)


def render_sidebar_audio() -> None:
    """Controles de audio unificados y accesibles dentro de la barra lateral."""
    with st.sidebar:
        render_html(
            f"""
            <div class="p5-audio-section">
                <h2 class="p5-font p5-audio-heading">AUDIO DEL OBSERVATORIO</h2>
            </div>
            """
        )
        st.session_state.setdefault('p5_sfx_toggle', True)
        st.session_state.setdefault('p5_bgm_toggle', False)
        st.toggle('Efectos de sonido (SFX)', key='p5_sfx_toggle')
        bgm_on = st.toggle('Música de fondo (BGM)', key='p5_bgm_toggle')
        if bgm_on:
            bgm_bytes = _audio_bytes('audio/background.mp3')
            if bgm_bytes:
                render_html('<p class="p5-bgm-note">Pista ambiental (usa el control integrado para pausar o ajustar volumen):</p>')
                st.audio(
                    bgm_bytes,
                    format='audio/mp3',
                    loop=True,
                    autoplay=True,
                    alt='Música de fondo del Observatorio',
                )


def trigger_select_sfx() -> None:
    """Mantiene compatibilidad de API; el SFX inmediato se dispara sin duplicados en el clic."""
    return None


def render_critical_alert(detalle: str) -> None:
    logging.getLogger(__name__).error('No se pudo cargar el observatorio: %s', detalle)
    st.error('No se pudo cargar el observatorio. Recarga la página para volver a intentarlo.')


@st.cache_data(show_spinner=False)
def load_curated_datasets(depurado_hash: str, clusters_hash: str, metadata_hash: str):
    """Carga datasets (games_curated.csv, dataset_depurado.csv y dataset_con_clusters.csv) en caché de datos."""
    df_clean = load_clean()
    df_clusters = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
    curated_path = CLEAN / 'games_curated.csv'
    if not curated_path.exists():
        curated_path = RAW
    df_raw = pd.read_csv(curated_path)
    analysis = json.loads((REPORTS / 'clustering_03_parametros.json').read_text(encoding='utf-8'))
    return df_clean, df_clusters, df_raw, analysis


@st.cache_data(show_spinner=False)
def load_metadata(metadata_hash: str) -> dict:
    """Carga models/metadata.json con @st.cache_data."""
    return json.loads((MODELS / 'metadata.json').read_text(encoding='utf-8'))


@st.cache_resource(show_spinner=False)
def load_model_artifacts(model_hash: str, vecinos_hash: str, metadata_hash: str) -> dict:
    """Carga modelos pesados (scikit-learn, joblib y estimador NearestNeighbors) con @st.cache_resource."""
    pipeline = joblib.load(MODELS / 'modelo_popularidad.joblib')
    vecinos = joblib.load(MODELS / 'vecinos_popularidad.joblib')
    metricas = load_metadata(metadata_hash)
    return {'pipeline': pipeline, 'vecinos': vecinos, 'metricas': metricas}


def _file_sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resources():
    """Valida y retorna (df_depurado, bundle_modelo, parametros_clustering) usando cachés separadas."""
    from .pipeline import REPORTES_APP, huella_pipeline
    rutas = [
        REPORTS / 'manifest.json',
        CLEAN / 'dataset_depurado.csv',
        CLEAN / 'dataset_con_clusters.csv',
        MODELS / 'modelo_popularidad.joblib',
        MODELS / 'metadata.json',
        MODELS / 'vecinos_popularidad.joblib',
        *[REPORTS / nombre for nombre in REPORTES_APP],
    ]
    estado = tuple(
        (ruta.name, hashlib.sha256(ruta.read_bytes()).hexdigest() if ruta.exists() else None)
        for ruta in rutas
    )
    try:
        return _resources(huella_pipeline(), estado)
    except (ValueError, FileNotFoundError, ImportError, OSError, KeyError, EOFError, pickle.UnpicklingError) as error:
        render_critical_alert(str(error))
        st.stop()


@st.cache_resource(show_spinner=False)
def _resources(huella, estado):
    """Valida integridad o delega a cachés de datos (@st.cache_data) y modelos (@st.cache_resource)."""
    from .pipeline import REPORTES_APP, main
    requeridos = [
        RAW,
        CLEAN / 'dataset_depurado.csv',
        CLEAN / 'dataset_con_clusters.csv',
        MODELS / 'modelo_popularidad.joblib',
        MODELS / 'metadata.json',
        MODELS / 'vecinos_popularidad.joblib',
        *[REPORTS / nombre for nombre in REPORTES_APP],
    ]
    faltantes = [str(r.relative_to(ROOT)) for r in requeridos if not r.exists()]
    if faltantes:
        raise FileNotFoundError(f"Archivos requeridos faltantes: {', '.join(faltantes)}")

    # Comprobar el manifiesto antes de deserializar: las claves de caché detectan
    # cambios, pero por sí solas no acreditan que los archivos concuerden.
    manifest = json.loads((REPORTS / 'manifest.json').read_text(encoding='utf-8'))
    artefactos = {'modelo_popularidad': MODELS / 'modelo_popularidad.joblib',
                 'metadata_modelo': MODELS / 'metadata.json',
                 'vecinos': MODELS / 'vecinos_popularidad.joblib',
                 'dataset_depurado': CLEAN / 'dataset_depurado.csv',
                 'dataset_con_clusters': CLEAN / 'dataset_con_clusters.csv'}
    for nombre, ruta in artefactos.items():
        if manifest.get(f'sha256_{nombre}') != _file_sha256(ruta):
            raise ValueError(f'Integridad incorrecta en {ruta.relative_to(ROOT)}; no se cargarán artefactos discordantes.')
    for nombre in REPORTES_APP:
        if manifest.get('sha256_reportes_app', {}).get(nombre) != _file_sha256(REPORTS / nombre):
            raise ValueError(f'El reporte {nombre} no coincide con el manifiesto.')

    dep_hash = _file_sha256(CLEAN / 'dataset_depurado.csv') or ''
    clu_hash = _file_sha256(CLEAN / 'dataset_con_clusters.csv') or ''
    mod_hash = _file_sha256(MODELS / 'modelo_popularidad.joblib') or ''
    vec_hash = _file_sha256(MODELS / 'vecinos_popularidad.joblib') or ''
    meta_hash = _file_sha256(MODELS / 'metadata.json') or ''

    metricas = load_metadata(meta_hash)
    if metricas.get('version_sklearn') != sklearn.__version__:
        main()
        dep_hash = _file_sha256(CLEAN / 'dataset_depurado.csv') or ''
        clu_hash = _file_sha256(CLEAN / 'dataset_con_clusters.csv') or ''
        mod_hash = _file_sha256(MODELS / 'modelo_popularidad.joblib') or ''
        vec_hash = _file_sha256(MODELS / 'vecinos_popularidad.joblib') or ''
        meta_hash = _file_sha256(MODELS / 'metadata.json') or ''

    df_clean, _, _, analysis = load_curated_datasets(dep_hash, clu_hash, meta_hash)
    bundle = load_model_artifacts(mod_hash, vec_hash, meta_hash)
    return df_clean, bundle, analysis


def setup(
    title: str,
    subtitle: str = 'Backloggd · muestra curada de videojuegos · análisis minería de datos',
    transition: str = 'default',
    menu_idx: int = 0,
    compact_menu: bool = True,
) -> None:
    """Configura la página con transiciones por cambio de vista, menú único en barra lateral y audio accesible."""
    st.set_page_config(
        page_title=f'{title} · Observatorio de Videojuegos',
        page_icon='🎮',
        layout='wide',
        initial_sidebar_state='auto',
    )
    inject_p5_css()
    if st.session_state.get('_p5_active_page_idx') != menu_idx:
        st.session_state['_p5_active_page_idx'] = menu_idx
        render_page_transition(transition)
    render_p5_main_menu(active_idx=menu_idx, compact=compact_menu)
    render_sidebar_audio()
    st.title(_p5_ascii(title))
    st.caption(subtitle)
    _inject_parent_interactive_engine()


def section_banner(title: str, subtitle: str = '') -> None:
    """Renderiza un banner de sección semántico estilo Persona 5."""
    clean_title = html.escape(_p5_ascii(title))
    clean_sub = html.escape(str(subtitle)) if subtitle else ''
    sub_html = f'<p class="p5-banner-sub">{clean_sub}</p>' if clean_sub else ''
    render_html(
        f"""
        <section class="p5-banner">
            <h2 class="p5-banner-title">{clean_title}</h2>
            {sub_html}
        </section>
        """
    )


def p5_plotly_layout(fig: go.Figure, title: str = '', height: int = 430) -> go.Figure:
    """Aplica el tema personalizado Persona 5 accesible a cualquier figura de Plotly."""
    lineas_titulo = textwrap.wrap(_p5_ascii(title).upper(), width=56) if title else []
    fig.update_layout(
        title=dict(
            text='<br>'.join(lineas_titulo),
            font=dict(family=FONT_SANS, size=18, color=PALETA['text-primary']),
            x=0.01,
        ),
        paper_bgcolor=PALETA['bg-chart-deep'],
        plot_bgcolor=PALETA['bg-chart'],
        font=dict(family=FONT_SANS, size=13, color=PALETA['text-primary']),
        colorway=P5_COLORWAY,
        height=height,
        margin=dict(l=64, r=32, t=max(48, 38 + 24 * len(lineas_titulo)) if title else 44, b=64),
        legend=dict(
            bgcolor=PALETA['bg-panel'],
            bordercolor=PALETA['primary'],
            borderwidth=1,
            font=dict(family=FONT_SANS, color=PALETA['text-primary'], size=12),
        ),
        hoverlabel=dict(
            bgcolor=PALETA['bg-primary'],
            bordercolor=PALETA['primary'],
            font=dict(family=FONT_SANS, size=13, color=PALETA['text-primary']),
        ),
    )
    fig.update_xaxes(
        gridcolor=PALETA['grid-color'],
        zerolinecolor=PALETA['purple-deep'],
        linecolor=PALETA['primary'],
        tickfont=dict(family=FONT_SANS, size=12, color=PALETA['text-secondary']),
        automargin=True,
        title_font=dict(family=FONT_SANS, size=14, color=PALETA['accent']),
    )
    fig.update_yaxes(
        gridcolor=PALETA['grid-color'],
        zerolinecolor=PALETA['purple-deep'],
        linecolor=PALETA['primary'],
        tickfont=dict(family=FONT_SANS, size=12, color=PALETA['text-secondary']),
        automargin=True,
        title_font=dict(family=FONT_SANS, size=14, color=PALETA['accent']),
    )
    # Solo etiquetas de potencias de diez: evita dígitos menores amontonados.
    for eje in list(fig.select_xaxes()) + list(fig.select_yaxes()):
        if eje.type == 'log':
            eje.update(dtick=1, tickformat='~s', minor=dict(showgrid=False, ticks=''))
    return fig


@st.cache_data(show_spinner=False)
def _cached_report(name: str, file_hash: str) -> pd.DataFrame:
    return pd.read_csv(REPORTS / name)


def read_report(name: str) -> pd.DataFrame:
    """Lee un CSV de reports/ con @st.cache_data invalidado por hash de contenido."""
    ruta = REPORTS / name
    if not ruta.exists():
        raise FileNotFoundError(f'No existe el reporte {ruta.relative_to(ROOT)}')
    return _cached_report(name, _file_sha256(ruta) or '')
