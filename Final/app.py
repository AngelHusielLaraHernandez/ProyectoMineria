"""Página de inicio del Observatorio de Videojuegos."""
import importlib
import json
import sys
import streamlit as st

import src.data as _data

if getattr(_data, '_MOD_VERSION', None) != 'p5-v14-menu':
    if 'src.config' in sys.modules:
        importlib.reload(sys.modules['src.config'])
    _data = importlib.reload(_data)
    _data.asegurar_modulos_vigentes(config_recargado=True)
else:
    _data.asegurar_modulos_vigentes()

from src.config import REPORTS, SIGNALS
from src.ui import (
    asset_b64,
    read_report,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

setup(
    'Observatorio de Videojuegos',
    'Actividad y calificaciones en Backloggd y Metacritic',
    transition='default',
    menu_idx=0,
    compact_menu=False,
)

df, bundle, analysis = resources()
metricas_modelo = bundle['metricas']
linaje = read_report('tables/procedencia_datos.csv').set_index('etapa')
n_maestro = int(linaje.loc['Maestro curado', 'filas'])
n_antecedente = int(linaje.loc['Antecedente enriquecido', 'filas'])
n_elegibles = int(df['elegible_analisis'].sum())
n_fechas_no_interp = (
    int(df['fecha_no_interpretable'].sum())
    if 'fecha_no_interpretable' in df
    else int(df['decada'].isna().sum())
)
asociacion = read_report('tables/correlacion_catalogo.csv').iloc[0]
catalogo = json.loads((REPORTS / 'tables/catalogo_resumen.json').read_text(encoding='utf-8'))
umbral_pares = read_report('tables/parametros_clustering.csv').iloc[0].minimo_pares_correlacion
preparador = bundle['pipeline'].named_steps['preparar'].named_transformers_
decadas = [int(x) for x in preparador['decada'].named_steps['codificar'].categories_[0] if x >= 0]

st.page_link('pages/1_Exploracion.py', label='Abrir panel interactivo de exploración')
st.info(
    'La predicción toma como referencia los juegos registrados en Backloggd y puede representar menos a los '
    'géneros de nicho. '
    'Los casos publicados por editoras se pueden consultar en Exploración.'
)

# ---------------------------------------------------------------------------
# 1. CABECERA PRINCIPAL
# ---------------------------------------------------------------------------
halo_b64 = asset_b64('img/juegos/halo.webp')
hero_img_html = (
    f'<img class="p5-hero-img" src="data:image/webp;base64,{halo_b64}" alt="Master Chief en Halo Infinite"/>'
    if halo_b64 else ''
)

render_html(
    f"""
    <div class="p5-hero">
        <div>
            <div class="p5-hero-title">Notas y popularidad de los videojuegos</div>
            <p class="p5-hero-sub">
                Comparamos las notas de los jugadores con las de la prensa. Después revisamos qué juegos
                aparecen más como jugados, cuáles siguen pendientes y cuáles están en las listas de deseos.
            </p>
        </div>
        {hero_img_html}
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. PROPÓSITO DEL PROYECTO
# ---------------------------------------------------------------------------
render_lb_rb_nav('QUÉ REVISAMOS')

zelda_b64 = asset_b64('img/juegos/zelda.webp')
kratos_b64 = asset_b64('img/juegos/god-of-war.webp')
mario_b64 = asset_b64('img/juegos/mario.webp')

render_html(
    f"""
    <div class="sc-root" role="region" aria-label="Temas del observatorio">
        <!-- BAR 1: LÍDER // INDUSTRIA -->
        <div class="sc-bar-outer active">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <img class="sc-char sc-art-zelda" src="data:image/webp;base64,{zelda_b64}" alt=""/>
                    <div class="sc-main">
                        <div class="sc-label">ACTIVIDAD E INTERÉS</div>
                        <div class="sc-subdesc">
                            Para el análisis usamos {n_elegibles:,} de los {n_maestro:,} juegos del catálogo. Separamos los que la gente marcó como jugados de los que guardó en pendientes o en su lista de deseos.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">ANTES</span>
                                <span class="sc-stat-num">{n_antecedente:,}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">CATÁLOGO</span>
                                <span class="sc-stat-num">{n_maestro:,}</span>
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

        <!-- BAR 2: ALIADO // BRECHA USUARIOS VS CRÍTICA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <img class="sc-char sc-art-kratos" src="data:image/webp;base64,{kratos_b64}" alt=""/>
                    <div class="sc-main">
                        <div class="sc-label">NOTAS DE JUGADORES Y PRENSA</div>
                        <div class="sc-subdesc">
                            En los {int(asociacion.n):,} juegos con las dos notas, cuando una sube la otra suele subir también. En Exploración se puede ver cuánto se separan por género y por organización.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">PARES</span>
                                <span class="sc-stat-num">{int(asociacion.n):,}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--accent);border-color:var(--accent);">PEARSON</span>
                                <span class="sc-stat-num">{asociacion.pearson_r:.3f}</span>
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

        <!-- BAR 3: ALIADO // RIESGOS GAAS E INFERENCIA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <img class="sc-char sc-art-mario" src="data:image/webp;base64,{mario_b64}" alt=""/>
                    <div class="sc-main">
                        <div class="sc-label">ESTIMACIÓN DE POPULARIDAD</div>
                        <div class="sc-subdesc">
                            En Predicción puedes cambiar los datos de un lanzamiento, ver qué nivel estima el modelo y consultar cinco juegos parecidos.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">F1 PRUEBA</span>
                                <span class="sc-stat-num">{metricas_modelo['metricas']['f1_macro']:.3f}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">VECINOS</span>
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
# 2. MÉTRICAS GENERALES (INDICADORES) — TARJETAS Y PANEL DE DETALLE
# ---------------------------------------------------------------------------
rango_temporal = f"{catalogo['anio_min']}–{catalogo['anio_max']}"
generos_unicos = sorted({g for row in df['generos'] for g in row})
top_generos = catalogo['top_generos']
top_org = catalogo['top_organizaciones']

def formato_grupo(fila):
    return f"{fila['grupo']} ({fila['n']})"

render_html(
    f"""
    <div class="resume-grid">
        <div class="resume-stack">
            <div class="resume-list-tag">LISTA // INDICADORES</div>

            <div class="resume-card-wrap active" data-detail-target="kpi-1">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">I</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">CATÁLOGO</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">JUEGOS</div>
                            <div class="resume-rank-number">{len(df):,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">{n_elegibles:,} JUEGOS INCLUIDOS EN EL ANÁLISIS</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-2">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">II</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">HORIZONTE</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">RANGO</div>
                            <div class="resume-rank-number">{rango_temporal}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">COBERTURA HISTÓRICA {rango_temporal}</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-3">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">III</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">GÉNEROS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TOTAL</div>
                            <div class="resume-rank-number">{catalogo['n_generos']}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">MULTI-ETIQUETA CON {len(preparador['generos'].vocabulario_)} GÉNEROS FRECUENTES EN EL MODELO</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-4">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">IV</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">ESTUDIOS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">EQUIPOS</div>
                            <div class="resume-rank-number">{catalogo['n_organizaciones']:,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">ESTUDIOS Y EDITORAS EN BACKLOGGD</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PANELES DE DETALLE DINÁMICOS -->
        <div>
            <div class="resume-detail-panel" data-detail-id="kpi-1" style="display:block;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">01</div>
                    <div class="resume-detail-top-title">LOS JUEGOS DEL CATÁLOGO</div>
                    <div class="resume-detail-top-progress">{n_maestro:,}</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Registros antes de revisar los repetidos</div>
                        <div class="resume-detail-status">{n_antecedente:,} FILAS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Títulos Únicos por Nombre y Fecha</div>
                        <div class="resume-detail-status">{n_maestro:,} JUEGOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Juegos que usamos para el análisis</div>
                        <div class="resume-detail-status">{metricas_modelo['n_cohorte']:,} CASOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Juegos con las dos notas</div>
                        <div class="resume-detail-status">{int(asociacion.n):,} PARES</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-2" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">02</div>
                    <div class="resume-detail-top-title">COBERTURA TEMPORAL</div>
                    <div class="resume-detail-top-progress">{rango_temporal}</div>
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
                        <div class="resume-detail-status">{rango_temporal}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Décadas Codificadas One-Hot</div>
                        <div class="resume-detail-status">{decadas[0]}s a {decadas[-1]}s</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Fechas no Interpretables</div>
                        <div class="resume-detail-status">{n_fechas_no_interp} CASOS · DÉCADA -1</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-3" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">03</div>
                    <div class="resume-detail-top-title">TAXONOMÍA DE GÉNEROS</div>
                    <div class="resume-detail-top-progress">{catalogo['n_generos']} GÉN</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Género con más juegos en el catálogo ({n_maestro:,})</div>
                        <div class="resume-detail-status">{formato_grupo(top_generos[0])}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Segundo y Tercer Género</div>
                        <div class="resume-detail-status">{' / '.join(map(formato_grupo, top_generos[1:]))}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Umbral de Correlación por Grupo</div>
                        <div class="resume-detail-status">MÍNIMO {umbral_pares} PARES</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Codificación en Clasificador</div>
                        <div class="resume-detail-status">MULTI-ETIQUETA + OTRO</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-4" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">04</div>
                    <div class="resume-detail-top-title">ESTUDIOS Y EDITORAS</div>
                    <div class="resume-detail-top-progress">{catalogo['n_organizaciones']} ORG</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Organización con más juegos ({n_maestro:,})</div>
                        <div class="resume-detail-status">{formato_grupo(top_org[0])}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Siguientes por Volumen</div>
                        <div class="resume-detail-status">{' / '.join(map(formato_grupo, top_org[1:]))}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Frecuencia Mínima en Modelo</div>
                        <div class="resume-detail-status">&gt;= {preparador['estudio'].min_frecuencia} TÍTULOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Organizaciones con pocos juegos en el catálogo</div>
                        <div class="resume-detail-status">OPCIÓN «OTRO»</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 3. EXPLORADOR DEL CATÁLOGO
# ---------------------------------------------------------------------------
section_banner('Busca un juego en el catálogo', 'Filtra por género o escribe parte del título')

a, b = st.columns([2, 1])
query = a.text_input('Buscar título', placeholder='Escribe parte del nombre (ej. Halo, Zelda, Elden Ring)')
genre = b.selectbox('Género', ['Todos', *generos_unicos])

view = df[df['Title'].str.contains(query, case=False, regex=False, na=False)]
if genre != 'Todos':
    view = view[view['generos'].map(lambda row: genre in row)]

labels = {
    'popularidad_indice': 'Índice de popularidad',
    'critica_verificada_csv': 'Nota de prensa (Metacritic)',
    'Rating': 'Valoración de usuarios (0–5)',
    'Plays': 'Marcados como jugados',
    'Playing': 'Jugando actualmente',
    'Backlogs': 'Pendientes',
    'Wishlist': 'Lista de deseos',
}
order = st.selectbox(
    'Ordenar por',
    ['popularidad_indice', *SIGNALS, 'Rating', 'critica_verificada_csv'],
    format_func=labels.get,
)

st.caption(f'Se muestran {len(view):,} de {len(df):,} juegos del catálogo.')

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
    columnas_visibles = [
        'Title',
        'anio',
        'Rating',
        'critica_verificada_csv',
        *SIGNALS,
        'popularidad_indice',
    ]
    st.dataframe(
        shown,
        hide_index=True,
        width='stretch',
        column_order=columnas_visibles,
        column_config={
            'Title': 'Videojuego',
            'anio': st.column_config.NumberColumn('Año', format='%d'),
            'Rating': st.column_config.NumberColumn('Usuarios (0–5)', format='%.2f'),
            'critica_verificada_csv': st.column_config.NumberColumn('Nota de prensa', format='%d'),
            'Plays': st.column_config.NumberColumn('Marcados como jugados', format='%d'),
            'Playing': st.column_config.NumberColumn('Jugando actualmente', format='%d'),
            'Backlogs': st.column_config.NumberColumn('Pendientes', format='%d'),
            'Wishlist': st.column_config.NumberColumn('Lista de deseos', format='%d'),
            'popularidad_indice': st.column_config.NumberColumn('Índice de popularidad', format='%.3f'),
        },
    )
    st.download_button(
        'Descargar esta consulta (CSV)',
        shown.to_csv(index=False).encode('utf-8'),
        'consulta_catalogo_videojuegos.csv',
        'text/csv',
    )
else:
    st.info('No hay coincidencias. Cambia el título o selecciona Todos en género.')

with st.expander('Cómo calculamos la popularidad'):
    st.write(
        'Primero ordenamos los juegos por cuántas veces se marcaron como jugados, cuántas veces '
        'se guardaron en pendientes y cuántas veces aparecieron en listas de deseos. Después '
        'sacamos el promedio del lugar que ocupó cada juego en esas tres listas. Usamos los '
        'juegos de entrenamiento como referencia para que todos se comparen en la misma escala.'
    )
