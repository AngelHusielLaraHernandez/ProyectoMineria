"""Módulo UI/UX Persona 5 (Port fiel de PruebasMenu/persona5-website-theme) y caché de artefactos."""
import base64
import hashlib
import json
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

ASSETS = ROOT / 'assets'
FONTS_DIR = ASSETS / 'fonts'
AUDIO_DIR = ASSETS / 'audio'
IMG_DIR = ASSETS / 'img'
CSS_DIR = ASSETS / 'css'

P5_COLORS = {
    'black': '#0d0d0d',
    'surface': '#141414',
    'red': '#d92323',
    'dark_red': '#732424',
    'white': '#ffffff',
    'gray': '#7b7b7b',
    'yellow': '#ffe600',
    'cyan': '#0dd9ff',
}

P5_COLORWAY = ['#d92323', '#ffffff', '#ffe600', '#0dd9ff', '#7b7b7b', '#732424']
_UI_VERSION = 'p5-v7-delegated'


def _p5_ascii(text: str) -> str:
    """Normaliza cadenas para la fuente Persona5Main (contiene glifos ASCII sin tildes)."""
    norm = unicodedata.normalize('NFKD', str(text))
    sin_tildes = ''.join(c for c in norm if not unicodedata.combining(c))
    return sin_tildes.replace('–', '-').replace('—', '-')


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
def _build_global_css(css_hash: str) -> str:
    """Construye la hoja de estilo global con Persona5main.ttf registrada como Persona5 y Persona5Main."""
    font_b64 = asset_b64('fonts/Persona5main.ttf')
    font_face = ''
    if font_b64:
        font_face = (
            "@font-face { font-family: 'Persona5'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; } "
            "@font-face { font-family: 'Persona5Main'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; }"
        )
    css_file = CSS_DIR / 'persona5.css'
    base_css = css_file.read_text(encoding='utf-8') if css_file.exists() else ''
    return f'<style>{font_face}\n{base_css}</style>'


def inject_p5_css() -> None:
    """Inyecta el tema visual Persona 5 y la tipografía Base64 en la vista actual."""
    css_file = CSS_DIR / 'persona5.css'
    css_hash = hashlib.sha256(css_file.read_bytes()).hexdigest() if css_file.exists() else 'v0'
    st.markdown(_build_global_css(css_hash), unsafe_allow_html=True)


def render_page_transition(variant: str = 'default') -> None:
    """Renderiza las cortinas de transición animadas exactas de PageTransition.jsx."""
    if variant == 'about':
        panels = [
            ('#0d0d0d', '-12vh', '-18vw', '86vw', '0s', 999),
            ('#ffffff', '24vh', '-10vw', '72vw', '0.05s', 998),
            ('#ffffff', '58vh', '-14vw', '82vw', '0.10s', 997),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-panel" style="background:{c};top:{t};left:{l};width:{w};animation-delay:{d};z-index:{z};"></div>'
            for c, t, l, w, d, z in panels
        )
    elif variant == 'resume':
        cards = [
            ('14vh', '#732424', '0s', 'none', 999),
            ('31vh', '#ffffff', '0.05s', '10px 0 0 #d92323', 998),
            ('48vh', '#ffffff', '0.10s', '10px 0 0 #d92323', 997),
            ('65vh', '#732424', '0.15s', 'none', 996),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-card" style="top:{t};background:{c};animation-delay:{d};box-shadow:{sh};z-index:{z};"></div>'
            for t, c, d, sh, z in cards
        )
    else:
        stripes = [
            ('#0d0d0d', '72vw', '24vw', '0s', 999),
            ('#d92323', '80vw', '14vw', '0.06s', 998),
            ('#ffffff', '88vw', '8vw', '0.12s', 997),
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
    """Renderiza el único menú principal estilo P5Menu.jsx exclusivamente dentro de la barra lateral izquierda."""
    items = [
        {'idx': 0, 'label': 'INICIO',      'font': 38, 'ox': 6,  'oy': 0, 'sx': -6, 'sy': 6},
        {'idx': 1, 'label': 'EXPLORACION', 'font': 24, 'ox': 4, 'oy': 6, 'sx': -9, 'sy': -5},
        {'idx': 2, 'label': 'PREDICCION',  'font': 26, 'ox': 4, 'oy': 6, 'sx': -3, 'sy': -3},
        {'idx': 3, 'label': 'MODELO',      'font': 38, 'ox': 12, 'oy': 6, 'sx': -5, 'sy': 5},
    ]

    joker_b64 = asset_b64('img/P5_Joker_Chain_Chronicle_1.png')
    art_html = (
        f'<img class="p5-stage-art" src="data:image/png;base64,{joker_b64}" alt=""/>'
        if joker_b64 else ''
    )

    rutas = ['/', '/Exploracion', '/Prediccion', '/Acerca_del_modelo']
    rows_html = ''
    for i, item in enumerate(items):
        is_act = 'active' if i == active_idx else ''
        fs = item['font']
        ox = item['ox']
        oy = item['oy']
        delay = i * 80
        rows_html += (
            f'<a href="{rutas[i]}" target="_self" class="p5-row {is_act}" aria-label="{item["label"]}" data-nav-index="{item["idx"]}" '
            f'style="margin-left:{ox}px;margin-top:{oy}px;animation-delay:{delay}ms;">'
            f'<div class="p5-glow"></div>'
            f'<div class="p5-skew-wrap" style="transform:skewX({item["sx"]}deg) skewY({item["sy"]}deg);">'
            f'<div class="p5-shadow-tri"></div>'
            f'<div class="p5-highlight"></div>'
            f'<div class="p5-label-wrap">'
            f'<span class="p5-label-base p5-label-dark" style="font-size:{fs}px;">{item["label"]}</span>'
            f'<span class="p5-label-base p5-label-bright" aria-hidden="true" style="font-size:{fs}px;">{item["label"]}</span>'
            f'</div>'
            f'</div>'
            f'</a>'
        )

    html_block = (
        f'<div class="p5-menu-stage">'
        f'{art_html}'
        f'<div class="p5-name-tag">'
        f'<span>Phantom\'s</span>'
        f'<span>persona</span>'
        f'</div>'
        f'<nav class="p5-menu" aria-label="Persona 5 Sidebar Menu">'
        f'{rows_html}'
        f'</nav>'
        f'<div class="p5-hint">'
        f'<span class="p5-hint-key">HOVER</span><span>SELECT</span>'
        f'<span class="p5-hint-key">CLICK</span><span>GO</span>'
        f'</div>'
        f'</div>'
    )
    with st.sidebar:
        render_html(html_block)


def render_lb_rb_nav(label: str) -> None:
    """Renderiza el cabezal animado ◄ LB [LABEL] RB ► de Socials.jsx / AboutMe.jsx."""
    clean_label = _p5_ascii(label)
    render_html(
        f"""
        <div class="sc-right-nav-bar">
            <span class="sc-nav-arrow left">◄</span>
            <span class="sc-nav-btn">LB</span>
            <span class="sc-nav-label">{clean_label}</span>
            <span class="sc-nav-btn">RB</span>
            <span class="sc-nav-arrow right">►</span>
        </div>
        """
    )


def _inject_parent_interactive_engine() -> None:
    """Inyecta en window.parent el motor de audio (BGM fade 450ms + select.mp3) y eventos de menús P5."""
    select_b64 = asset_b64('audio/select.mp3')
    bgm_b64 = ''
    # Para BGM pesado (7.7 MB), solo lo inyectamos una vez en window.parent para no repetir transferencia
    bgm_path = AUDIO_DIR / 'background.mp3'
    if bgm_path.exists() and not st.session_state.get('_p5_bgm_injected', False):
        bgm_b64 = base64.b64encode(bgm_path.read_bytes()).decode('ascii')
        st.session_state['_p5_bgm_injected'] = True

    motor_interactivo = (ASSETS / "js/interacciones.js").read_text(encoding="utf-8")
    sfx_desactivado = json.dumps(not st.session_state.get('p5_sfx_toggle', True))
    js_code = f"""
    <script>
    (function() {{
      const doc = window.parent.document;
      const win = window.parent;
      win.__p5SfxDisabled = {sfx_desactivado};

      // 1. Registrar select.mp3 y playSelectSound() idéntico a src/utils/audio.js
      if ("{select_b64}" && !win.__p5SelectSrc) {{
        win.__p5SelectSrc = "data:audio/mp3;base64,{select_b64}";
      }}
      if ("{bgm_b64}" && !win.__p5BgmSrc) {{
        win.__p5BgmSrc = "data:audio/mp3;base64,{bgm_b64}";
      }}

      win.playSelectSound = function() {{
        if (win.__p5SfxDisabled) return;
        if (!win.__p5SelectSrc) return;
        try {{
          const a = new win.Audio(win.__p5SelectSrc);
          a.volume = 0.5;
          a.play().catch(function(){{}});
        }} catch (e) {{}}
      }};

      // 2. Montar el panel flotante .bgm-panel de App.jsx en window.parent.document.body
      if (!doc.getElementById('p5-floating-bgm-panel') && win.__p5BgmSrc) {{
        const BGM_STATE_KEY = 'p5-bgm-enabled';
        const BGM_VOLUME_KEY = 'p5-bgm-volume';
        const FADE_MS = 450;
        let savedVol = parseFloat(win.localStorage.getItem(BGM_VOLUME_KEY));
        if (!Number.isFinite(savedVol)) savedVol = 0.45;
        savedVol = Math.min(1, Math.max(0, savedVol));

        const panel = doc.createElement('div');
        panel.id = 'p5-floating-bgm-panel';
        panel.className = 'bgm-panel';
        panel.innerHTML = `
          <audio id="p5-bgm-audio" loop preload="none" src="${{win.__p5BgmSrc}}"></audio>
          <button id="p5-bgm-toggle-btn" class="bgm-toggle" type="button">BGM OFF</button>
          <div class="bgm-slider-wrap" aria-label="Background music volume">
            <span class="bgm-slider-label">VOL</span>
            <input id="p5-bgm-vol-slider" class="bgm-slider" type="range" min="0" max="1" step="0.01" value="${{savedVol}}" />
            <span id="p5-bgm-vol-val" class="bgm-slider-value">${{Math.round(savedVol * 100)}}</span>
          </div>
        `;
        doc.body.appendChild(panel);

        const audio = panel.querySelector('#p5-bgm-audio');
        const btn = panel.querySelector('#p5-bgm-toggle-btn');
        const slider = panel.querySelector('#p5-bgm-vol-slider');
        const valSpan = panel.querySelector('#p5-bgm-vol-val');
        let isPlaying = false;
        let fadeRaf = null;

        function stopFade() {{
          if (fadeRaf) {{
            win.cancelAnimationFrame(fadeRaf);
            fadeRaf = null;
          }}
        }}

        function fadeTo(target, done) {{
          stopFade();
          const start = audio.volume;
          const diff = target - start;
          const begin = win.performance.now();
          function tick(now) {{
            const p = Math.min(1, (now - begin) / FADE_MS);
            audio.volume = Math.min(1, Math.max(0, start + diff * p));
            if (p < 1) {{
              fadeRaf = win.requestAnimationFrame(tick);
              return;
            }}
            fadeRaf = null;
            if (done) done();
          }}
          fadeRaf = win.requestAnimationFrame(tick);
        }}

        btn.addEventListener('click', function() {{
          win.playSelectSound();
          if (isPlaying) {{
            fadeTo(0, function() {{
              audio.pause();
              audio.currentTime = 0;
              isPlaying = false;
              btn.classList.remove('on');
              btn.textContent = 'BGM OFF';
              win.localStorage.setItem(BGM_STATE_KEY, '0');
            }});
          }} else {{
            stopFade();
            audio.volume = 0;
            audio.play().then(function() {{
              fadeTo(parseFloat(slider.value));
              isPlaying = true;
              btn.classList.add('on');
              btn.textContent = 'BGM ON';
              win.localStorage.setItem(BGM_STATE_KEY, '1');
            }}).catch(function(){{}});
          }}
          btn.blur();
        }});

        slider.addEventListener('input', function(e) {{
          const v = parseFloat(e.target.value);
          valSpan.textContent = String(Math.round(v * 100));
          if (isPlaying) audio.volume = v;
          win.localStorage.setItem(BGM_VOLUME_KEY, String(v));
        }});
      }}

      {motor_interactivo}
    }})();
    </script>
    """
    components.html(js_code, height=0, width=0)


def render_sidebar_audio() -> None:
    """Controles de audio compactos en barra lateral sincronizados con el panel flotante BGM."""
    with st.sidebar:
        icon_b64 = asset_b64('img/icon1.png')
        icon_html = (
            f'<img src="data:image/png;base64,{icon_b64}" width="22" '
            f'style="vertical-align:middle;margin-right:6px;" alt="P5"/>'
            if icon_b64 else ''
        )
        render_html(
            f"""
            <div style="border-top:2px solid #d92323;padding-top:0.65rem;margin-top:0.2rem;margin-bottom:0.4rem;">
                <div class="p5-font" style="font-size:1.05rem;color:#ffe600;letter-spacing:0.06em;">
                    {icon_html}PHANTOM SOUND
                </div>
            </div>
            """
        )
        sfx_on = st.toggle('SFX de menú (select.mp3)', value=True, key='p5_sfx_toggle')
        bgm_on = st.toggle('Reproductor BGM alternativo', value=False, key='p5_bgm_toggle')
        if bgm_on:
            bgm_path = AUDIO_DIR / 'background.mp3'
            if bgm_path.exists():
                st.audio(bgm_path.read_bytes(), format='audio/mp3', loop=True, autoplay=True)
        if sfx_on and st.session_state.pop('_trigger_select_sfx', False):
            sfx_b64 = asset_b64('audio/select.mp3')
            if sfx_b64:
                render_html(
                    f'<audio autoplay style="display:none">'
                    f'<source src="data:audio/mp3;base64,{sfx_b64}" type="audio/mp3">'
                    f'</audio>'
                )


def trigger_select_sfx() -> None:
    """Marca la reproducción del efecto select.mp3 tras presionar un botón principal."""
    st.session_state['_trigger_select_sfx'] = True


def render_critical_alert(detalle: str) -> None:
    """Pantalla de error temática ('CRITICAL ALERT / MISSION FAILED') cuando faltan artefactos."""
    inject_p5_css()
    char_b64 = asset_b64('img/jokerface2.png')
    img_html = (
        f'<img src="data:image/png;base64,{char_b64}" width="110" '
        f'style="float:right;margin-left:1rem;filter:drop-shadow(4px 4px 0 #000);" alt="Alert"/>'
        if char_b64 else ''
    )
    render_html(
        f"""
        <div class="p5-critical-alert">
            {img_html}
            <div class="p5-critical-title">CRITICAL ALERT // MISSION FAILED</div>
            <p style="font-size:1.05rem;color:#ffffff;margin-bottom:0.6rem;">
                No se encontraron o no pudieron validarse los artefactos de datos o modelos requeridos para iniciar el Observatorio Phantom Thieves.
            </p>
            <p style="font-family:monospace;background:#0d0d0d;padding:0.6rem 0.9rem;border:1px solid #d92323;color:#ffe600;">
                Detalle técnico: {detalle}
            </p>
            <p style="font-size:0.98rem;color:#ffffff;margin-top:0.8rem;margin-bottom:0.3rem;">
                <strong>Instrucciones de recuperación:</strong> Ejecuta el pipeline de entrenamiento desde la carpeta <code>Final/</code>:
            </p>
            <pre style="background:#000000;color:#ffe600;padding:0.75rem;border:2px solid #ffffff;">cd Final · python -m src.pipeline · streamlit run app.py</pre>
        </div>
        """
    )
    st.error(
        f'CRITICAL ALERT / MISSION FAILED — {detalle}. '
        'Ejecuta `python -m src.pipeline` desde la carpeta `Final/` y recarga la página.'
    )


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
    except (ValueError, FileNotFoundError, ImportError, OSError, KeyError) as error:
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
    """Configura la página con transiciones PageTransition.jsx, menú único en barra lateral P5Menu.jsx y motor de audio."""
    st.set_page_config(
        page_title=f'{title} · P5 Data Observatory',
        page_icon='🎭',
        layout='wide',
        initial_sidebar_state='expanded',
    )
    inject_p5_css()
    render_page_transition(transition)
    render_p5_main_menu(active_idx=menu_idx, compact=compact_menu)
    render_sidebar_audio()
    st.title(_p5_ascii(title))
    st.caption(subtitle)
    _inject_parent_interactive_engine()


def section_banner(title: str, subtitle: str = '') -> None:
    """Renderiza un banner inclinado estilo cómic Persona 5."""
    clean_title = _p5_ascii(title)
    sub_html = f'<div class="p5-banner-sub">{subtitle}</div>' if subtitle else ''
    render_html(
        f"""
        <div class="p5-banner">
            <div class="p5-banner-title">{clean_title}</div>
            {sub_html}
        </div>
        """
    )


def p5_plotly_layout(fig: go.Figure, title: str = '', height: int = 430) -> go.Figure:
    """Aplica el tema personalizado Persona 5 a cualquier figura de Plotly."""
    fig.update_layout(
        title=dict(
            text=_p5_ascii(title).upper() if title else '',
            font=dict(family='Persona5Main, Bebas Neue, Roboto, sans-serif', size=24, color='#ffffff'),
            x=0.01,
        ),
        paper_bgcolor='#0d0d0d',
        plot_bgcolor='#121212',
        font=dict(family='Roboto, sans-serif', size=13, color='#ffffff'),
        colorway=P5_COLORWAY,
        height=height,
        margin=dict(l=48, r=28, t=58 if title else 28, b=48),
        legend=dict(
            bgcolor='rgba(20, 20, 20, 0.9)',
            bordercolor='#d92323',
            borderwidth=1,
            font=dict(color='#ffffff', size=12),
        ),
        hoverlabel=dict(
            bgcolor='#0d0d0d',
            bordercolor='#d92323',
            font=dict(family='Roboto, sans-serif', size=13, color='#ffffff'),
        ),
    )
    fig.update_xaxes(
        gridcolor='#222222',
        zerolinecolor='#444444',
        linecolor='#d92323',
        tickfont=dict(color='#e6e6e6'),
        title_font=dict(family='Bebas Neue, Roboto, sans-serif', size=16, color='#ffe600'),
    )
    fig.update_yaxes(
        gridcolor='#222222',
        zerolinecolor='#444444',
        linecolor='#d92323',
        tickfont=dict(color='#e6e6e6'),
        title_font=dict(family='Bebas Neue, Roboto, sans-serif', size=16, color='#ffe600'),
    )
    return fig


def manual_checks() -> None:
    """Expander de verificación metodológica manual."""
    with st.expander('Qué debo verificar manualmente (Protocolo de Auditoría)'):
        st.write(
            'Confirma escala de Rating (0–5 vs 0–100), procedencia y plataforma de Metacritic, '
            'roles de Team (desarrollador vs publisher), fecha de captura de Backloggd, '
            'versiones multiplataforma y licencia antes de interpretar o redistribuir.'
        )


@st.cache_data(show_spinner=False)
def _cached_report(name: str, file_hash: str) -> pd.DataFrame:
    return pd.read_csv(REPORTS / name)


def read_report(name: str) -> pd.DataFrame:
    """Lee un CSV de reports/ con @st.cache_data invalidado por hash de contenido."""
    ruta = REPORTS / name
    if not ruta.exists():
        raise FileNotFoundError(f'No existe el reporte {ruta.relative_to(ROOT)}')
    return _cached_report(name, _file_sha256(ruta) or '')
