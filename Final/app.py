"""Página de Inicio: Observatorio de Videojuegos — Edición Phantom Thieves (Persona 5 UI)."""
import importlib
import streamlit as st

import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v8-neon':
    importlib.reload(_ui)

from src.config import SIGNALS
from src.ui import (
    asset_b64,
    manual_checks,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

setup(
    'Observatorio de Videojuegos',
    'Phantom Thieves Edition · Menú Interactivo Persona 5 · Backloggd & Metacritic',
    transition='default',
    menu_idx=0,
    compact_menu=False,
)

df, bundle, analysis = resources()
metricas_modelo = bundle['metricas']

# ---------------------------------------------------------------------------
# 1. CABECERA HERO ("TAKE YOUR HEART" CON ASSETS/IMG/)
# ---------------------------------------------------------------------------
hero_b64 = asset_b64('img/hero.png')
joker_b64 = asset_b64('img/jokerface2.png')
hero_img_html = (
    f'<img class="p5-hero-img" src="data:image/png;base64,{joker_b64}" alt="Phantom Thieves"/>'
    if joker_b64 else ''
)
logo_img_html = (
    f'<img src="data:image/png;base64,{hero_b64}" width="175" '
    f'style="filter:drop-shadow(4px 4px 0 #000);margin-bottom:0.4rem;" alt="Take Your Heart"/>'
    if hero_b64 else ''
)

render_html(
    f"""
    <div class="p5-hero">
        <div>
            {logo_img_html}
            <div class="p5-hero-badge">PHANTOM THIEVES DATA OBSERVATORY // SHUJIN ACADEMY</div>
            <div class="p5-hero-title">TAKE YOUR HEART: BRECHA CRITICA Y POPULARIDAD</div>
            <p class="p5-hero-sub">
                Investigación empírica sobre la industria del videojuego: contrastamos la recepción de la
                comunidad de jugadores (Backloggd) frente a la prensa especializada (Metacritic), evaluamos
                la actividad y el interés registrados, y describimos perfiles de recepción y popularidad.
                El catálogo no permite medir pérdidas ni riesgo comercial de <em>Games as a Service (GaaS)</em>.
            </p>
        </div>
        {hero_img_html}
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. PROPÓSITO DEL PROYECTO — BARRAS DESLIZANTES DE PERSONAJES (Socials.jsx / AboutMe.jsx)
# ---------------------------------------------------------------------------
render_lb_rb_nav('MISSION BRIEFING // PARTY')

char1_b64 = asset_b64('img/char1.png')
char2_b64 = asset_b64('img/char2.png')
char3_b64 = asset_b64('img/char3.png')

render_html(
    f"""
    <div class="sc-root" role="region" aria-label="Propósito Ejecutivo del Proyecto">
        <!-- BAR 1: LEADER // INDUSTRIA -->
        <div class="sc-bar-outer active">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char1_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">LEADER</div>
                    <div class="sc-main">
                        <div class="sc-label">01 // INDUSTRIA &amp; TRACCION</div>
                        <div class="sc-subdesc">
                            Separamos alcance acumulado (Plays) de interés pendiente (Wishlist / Backlogs) sobre los 1,117 registros del maestro games_curated.csv; el antecedente histórico contiene 1,512 registros.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">HIST</span>
                                <span class="sc-stat-num">1,512</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">MAESTRO</span>
                                <span class="sc-stat-num">1,117</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--secondary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- BAR 2: PARTY // BRECHA USUARIOS VS CRITICA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char2_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">PARTY</div>
                    <div class="sc-main">
                        <div class="sc-label">02 // BRECHA COMUNIDAD-PRENSA</div>
                        <div class="sc-subdesc">
                            Correlación moderada (r = 0.544 en 887 pares elegibles según CSV). La brecha y la asociación por género y organización se consultan en Exploración; Team no acredita funciones de desarrollador.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">PAIRS</span>
                                <span class="sc-stat-num">887</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--accent);border-color:var(--accent);">PEARSON</span>
                                <span class="sc-stat-num">0.544</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--accent);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- BAR 3: PARTY // RIESGOS GAAS & INFERENCIA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char3_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">PARTY</div>
                    <div class="sc-main">
                        <div class="sc-label">03 // RIESGO GAAS &amp; MODELADO</div>
                        <div class="sc-subdesc">
                            Estimamos popularidad relativa y consultamos cinco vecinos del entrenamiento. No hay una variable de juegos como servicio ni datos de rentabilidad para cuantificar su riesgo.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">F1 TEST</span>
                                <span class="sc-stat-num">{metricas_modelo['metricas']['f1_macro']:.3f}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">KNN</span>
                                <span class="sc-stat-num">TOP 5</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--secondary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. MÉTRICAS GENERALES (KPIs) — CONFIDANT RANK CARDS & DETAIL PANEL (ResumePage.jsx)
# ---------------------------------------------------------------------------
anios_validos = df['anio'].dropna().astype(int)
rango_temporal = f'{int(anios_validos.min())}–{int(anios_validos.max())}' if len(anios_validos) else '1980–2023'
generos_unicos = sorted({g for row in df['generos'] for g in row})
estudios_unicos = sorted({org for row in df['organizaciones'] for org in row})
frecuencias_generos = df['generos'].explode().dropna().value_counts()
top_generos = frecuencias_generos.head(3)

render_html(
    f"""
    <div class="resume-grid">
        <div class="resume-stack">
            <div class="resume-list-tag">LIST // KPIS</div>

            <div class="resume-card-wrap active" data-detail-target="kpi-1">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">I</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">CATALOGO</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TOTAL</div>
                            <div class="resume-rank-number">{len(df):,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">1,117 REGISTROS EN EL MAESTRO CURADO; ANTECEDENTE HISTORICO DE 1,512</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-2">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">II</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">HORIZONTE</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">SPAN</div>
                            <div class="resume-rank-number">1980-25</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">COBERTURA HISTORICA {rango_temporal} (ANALISIS HASTA 2025)</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-3">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">III</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">GENEROS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TAXON</div>
                            <div class="resume-rank-number">{len(generos_unicos)}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">MULTI-ETIQUETA CON 15 GENEROS FRECUENTES EN EL MODELO</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-4">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">IV</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">ESTUDIOS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TEAMS</div>
                            <div class="resume-rank-number">{len(estudios_unicos):,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">ORGANIZACIONES ANALIZADAS EN EL CAMPO TEAM DE BACKLOGGD</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PANELES DE DETALLE DINÁMICOS (ResumePage.jsx .resume-detail-panel) -->
        <div>
            <div class="resume-detail-panel" data-detail-id="kpi-1" style="display:block;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">01</div>
                    <div class="resume-detail-top-title">CATALOGO LOG</div>
                    <div class="resume-detail-top-progress">1,117</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Registros Históricos Originales</div>
                        <div class="resume-detail-status">1,512 FILAS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Títulos Únicos por Nombre y Fecha</div>
                        <div class="resume-detail-status">1,117 JUEGOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Cohorte Elegible Sin Conflicto</div>
                        <div class="resume-detail-status">{metricas_modelo['n_cohorte']:,} CASOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Pares Elegibles con Ambas Notas</div>
                        <div class="resume-detail-status">{analysis['n_completos']:,} PARES</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-2" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">02</div>
                    <div class="resume-detail-top-title">TEMPORAL LOG</div>
                    <div class="resume-detail-top-progress">1980-25</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Rango Observado en Dataset</div>
                        <div class="resume-detail-status">{rango_temporal}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Horizonte Analítico del Proyecto</div>
                        <div class="resume-detail-status">1980–2025</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Décadas Codificadas One-Hot</div>
                        <div class="resume-detail-status">1980s A 2020s</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Títulos sin Fecha Conocida</div>
                        <div class="resume-detail-status">DECADA -1</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-3" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">03</div>
                    <div class="resume-detail-top-title">GENRE TAXONOMY</div>
                    <div class="resume-detail-top-progress">{len(generos_unicos)} GEN</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Género Dominante en Catálogo</div>
                        <div class="resume-detail-status">{top_generos.index[0]} ({top_generos.iloc[0]})</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Segundo y Tercer Género</div>
                        <div class="resume-detail-status">{' / '.join(f'{g} ({n})' for g, n in top_generos.iloc[1:].items())}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Umbral de Correlación por Grupo</div>
                        <div class="resume-detail-status">MINIMO 20 PARES</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Codificación en Clasificador</div>
                        <div class="resume-detail-status">MULTI-HOT + OTRO</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-4" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">04</div>
                    <div class="resume-detail-top-title">STUDIOS &amp; TEAMS</div>
                    <div class="resume-detail-top-progress">{len(estudios_unicos)} ORG</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Organización con Mayor Presencia</div>
                        <div class="resume-detail-status">NINTENDO (170)</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Siguientes por Volumen</div>
                        <div class="resume-detail-status">CAPCOM / SQUARE ENIX</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Frecuencia Mínima en Modelo</div>
                        <div class="resume-detail-status">&gt;= 10 TITULOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Respaldo para Estudios Independientes</div>
                        <div class="resume-detail-status">CLASE OTRO</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 3. AVISO DE LIMITACIONES METODOLÓGICAS (CALLOUT ROJO / OSCURO)
# ---------------------------------------------------------------------------
render_html(
    """
    <div class="p5-callout-warning">
        <div class="p5-callout-title">⚠️ AVISO METODOLOGICO Y LIMITACIONES DEL ESTUDIO (CALLING CARD)</div>
        <ul style="margin:0;padding-left:1.25rem;color:#f2f2f2;line-height:1.55;font-size:0.95rem;">
            <li><strong>Sesgo de supervivencia hacia juegos populares:</strong> La muestra original procede de listados curados de Backloggd con alta visibilidad comunitaria; no representa una muestra aleatoria de todos los lanzamientos comerciales de la industria.</li>
            <li><strong>Ausencia de fracasos comerciales puros:</strong> Los niveles de popularidad (<em>bajo</em>, <em>medio</em>, <em>alto</em>) son <strong>relativos a los terciles del conjunto de entrenamiento</strong> dentro de este catálogo popular, no absolutos respecto al mercado global.</li>
            <li><strong>Advertencia sobre datos de ventas:</strong> Las señales <code>Plays</code>, <code>Playing</code>, <code>Backlogs</code> y <code>Wishlist</code> reflejan registros de actividad en plataforma social en un corte temporal; <strong>no equivalen a unidades vendidas ni a ingresos en USD</strong>.</li>
        </ul>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 4. EXPLORADOR RÁPIDO DEL CATÁLOGO MAESTRO
# ---------------------------------------------------------------------------
section_banner('Explorador Rápido del Catálogo', 'Consulta Directa de Títulos y Señales de Popularidad')

a, b = st.columns([2, 1])
query = a.text_input('Buscar título', placeholder='Escribe parte del nombre (ej. Persona, Zelda, Elden Ring)')
genre = b.selectbox('Género', ['Todos', *generos_unicos])

view = df[df['Title'].str.contains(query, case=False, regex=False, na=False)]
if genre != 'Todos':
    view = view[view['generos'].map(lambda row: genre in row)]

labels = {
    'popularidad_indice': 'Índice de popularidad',
    'critica_verificada_csv': 'Prensa según CSV (Metacritic)',
    'Rating': 'Valoración de usuarios (0–5)',
    'Plays': 'Plays · alcance acumulado',
    'Playing': 'Playing · actividad',
    'Backlogs': 'Backlogs · pendientes',
    'Wishlist': 'Wishlist · deseos',
}
order = st.selectbox(
    'Ordenar por',
    ['popularidad_indice', *SIGNALS, 'Rating', 'critica_verificada_csv'],
    format_func=labels.get,
)

st.caption(
    f'Juegos visibles: {len(view):,} de {len(df):,} registros únicos por título y fecha. '
    'Conteos de una captura; no son ventas.'
)
st.caption(
    'El índice usa solo percentiles de Plays, Wishlist y Backlogs contra la referencia de entrenamiento. '
    'Playing se muestra como contexto y solo interviene en el EDA/clustering.'
)

shown = view.sort_values(order, ascending=False)[
    [
        'id_juego',
        'Title',
        'conflicto_historico_pendiente',
        'anio',
        'Rating',
        'critica_verificada_csv',
        *SIGNALS,
        'popularidad_indice',
    ]
]

if len(shown):
    st.dataframe(
        shown,
        hide_index=True,
        width='stretch',
        column_config={
            'Title': 'Videojuego',
            'anio': st.column_config.NumberColumn('Año', format='%d'),
            'critica_verificada_csv': 'Prensa según CSV',
            'popularidad_indice': st.column_config.NumberColumn('Índice de popularidad', format='%.3f'),
        },
    )
    st.download_button(
        'Descargar esta consulta (CSV)',
        shown.to_csv(index=False).encode('utf-8'),
        'consulta_phantom_thieves.csv',
        'text/csv',
    )
else:
    st.info('No hay coincidencias. Cambia el título o selecciona Todos en género.')

with st.expander('Cómo se define el Índice de Popularidad (Sin Fuga de Información)'):
    st.latex(r'I=\frac{P_{\text{train}}(\text{Plays})+P_{\text{train}}(\text{Wishlist})+P_{\text{train}}(\text{Backlogs})}{3}')
    st.write(
        'P se ajusta con rangos medios/N solo en la partición de entrenamiento (n = 892). '
        'Para los demás juegos se interpola contra esa referencia congelada: 0 por debajo del mínimo '
        'y 1 por encima del máximo de entrenamiento. Las tres señales pesan lo mismo; Wishlist y Backlogs '
        'representan interés pendiente y están correlacionadas. Playing se muestra como contexto, pero no '
        'construye el objetivo ni entra al clasificador. No es una medida de ventas o rentabilidad.'
    )

manual_checks()
