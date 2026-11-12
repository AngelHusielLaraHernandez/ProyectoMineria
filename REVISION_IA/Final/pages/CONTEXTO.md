# Carpeta: Final/pages

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## 1_Exploracion.py

Ruta: `Final/pages/1_Exploracion.py` · Bytes: 22431 · SHA-256: `6bf9ef0f0717939953fc6a4b52db5b7d969731b61671e295bbd76a48eee05295`

````text
"""Página 1 — Exploración (EDA, Brecha Usuarios-Crítica y Perfiles de Clustering)."""
import hashlib
import importlib
import json
from textwrap import wrap
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.visualizacion import PALETA
import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v8-neon':
    importlib.reload(_ui)

from src.config import CLEAN, REPORTS
from src.visualizacion import COLOR_SENALES
from src.ui import (
    manual_checks,
    read_report,
    resources,
    section_banner,
    setup,
)

from vista_graficas import mostrar_grafica

setup(
    'Dashboard de videojuegos',
    'Explora actividad, recepción y perfiles del catálogo',
    transition='about',
    menu_idx=1,
    compact_menu=True,
)

df, bundle, analysis = resources()
elegibles = df.loc[df['elegible_analisis']].copy()
elegibles['rating_100_vista'] = elegibles['Rating'] * 20.0
elegibles['brecha_vista'] = elegibles['rating_100_vista'] - elegibles['critica_verificada_csv']

def restablecer_filtros():
    st.session_state['eda_revision_filtros'] = revision_filtros + 1
    limpiar_seleccion()


def limpiar_seleccion():
    st.session_state['eda_revision_seleccion'] = st.session_state.get('eda_revision_seleccion', 0) + 1


revision_filtros = st.session_state.get('eda_revision_filtros', 0)
with st.expander('Filtros del dashboard', expanded=True):
    primera, segunda = st.columns(2)
    with primera:
        generos_sel = st.multiselect(
            'Géneros', sorted({g for fila in elegibles['generos'] for g in fila}),
            placeholder='Todos los géneros', key=f'eda_generos_{revision_filtros}',
        )
        rango_rating = st.slider(
            'Rating de usuarios (0–5)', 0.0, 5.0, (0.0, 5.0), .1,
            key=f'eda_rating_{revision_filtros}',
        )
    with segunda:
        decadas_sel = st.multiselect(
            'Décadas', sorted(int(d) for d in elegibles['decada'].dropna().unique() if d > 0),
            format_func=lambda d: f'{d}s', placeholder='Todas las décadas',
            key=f'eda_decadas_{revision_filtros}',
        )
        rango_meta = st.slider(
            'Metacritic (0–100)', 0, 100, (0, 100), key=f'eda_meta_{revision_filtros}',
        )
    st.button('Restablecer filtros', on_click=restablecer_filtros)
    st.caption('Los géneros se combinan por coincidencia con cualquiera de los seleccionados. '
               'Al acotar una escala de calificación se excluyen los juegos sin esa nota.')

filtrado = elegibles.copy()
if generos_sel:
    filtrado = filtrado[filtrado['generos'].map(lambda gs: any(g in gs for g in generos_sel))]
if decadas_sel:
    filtrado = filtrado[filtrado['decada'].isin(decadas_sel)]
if rango_rating != (0.0, 5.0):
    filtrado = filtrado[filtrado['Rating'].between(*rango_rating)]
if rango_meta != (0, 100):
    filtrado = filtrado[filtrado['critica_verificada_csv'].between(*rango_meta)]

pares_filtrados = filtrado.dropna(subset=['Rating', 'critica_verificada_csv']).copy()
mediana_plays = filtrado['Plays'].median() if filtrado['Plays'].notna().any() else None
brecha_absoluta = pares_filtrados['brecha_vista'].abs().mean()
with st.container(key='dashboard_indicadores'):
    indicadores = st.columns(4)
    indicadores[0].metric('Juegos filtrados', f'{len(filtrado):,} / {len(elegibles):,}')
    indicadores[1].metric('Pares con ambas notas', f'{len(pares_filtrados):,}')
    indicadores[2].metric('Mediana de Plays', f'{mediana_plays:,.0f}' if mediana_plays is not None else '—')
    indicadores[3].metric('Brecha absoluta media', f'{brecha_absoluta:.2f} pts' if len(pares_filtrados) else '—')

# ---------------------------------------------------------------------------
# 2. DISTRIBUCIÓN DE INTERACCIÓN (PLAYS, WISHLIST, BACKLOGS) EN ESCALA LOG
# ---------------------------------------------------------------------------
section_banner(
    'Distribución de Interacción por Género (Escala Logarítmica)',
    'Plays · Wishlist · Backlogs Desglosados por Taxonomía',
)

col_sig, col_top = st.columns([2, 1])
with col_sig:
    senal_sel = st.radio(
        'Señal de comunidad a visualizar',
        options=['Plays', 'Wishlist', 'Backlogs'],
        horizontal=True,
    )
with col_top:
    top_n_gen = st.slider('Número de géneros principales', min_value=6, max_value=18, value=12)

filas_gen = []
for _, row in filtrado.dropna(subset=[senal_sel]).iterrows():
    val = float(row[senal_sel])
    if val > 0:
        for g in row['generos']:
            filas_gen.append({'Genero': g, senal_sel: val, 'Title': row['Title']})

if filas_gen:
    df_gen_long = pd.DataFrame(filas_gen)
    orden_gen = (
        df_gen_long.groupby('Genero')[senal_sel]
        .median()
        .sort_values(ascending=False)
        .head(top_n_gen)
        .index.tolist()
    )
    df_gen_top = df_gen_long[df_gen_long['Genero'].isin(orden_gen)]

    fig_box = px.box(
        df_gen_top,
        x=senal_sel,
        y='Genero',
        orientation='h',
        category_orders={'Genero': orden_gen},
        color_discrete_sequence=[PALETA['primary']],
        points='outliers',
        hover_data=['Title'],
    )
    fig_box.update_traces(
        marker=dict(color=PALETA['accent'], size=5, opacity=0.8),
        line=dict(color=PALETA['secondary'], width=1.5),
        fillcolor='rgba(165, 107, 255, 0.75)',
    )
    fig_box.update_xaxes(type='log', title_text=f'{senal_sel} · escala logarítmica')
    fig_box.update_yaxes(autorange='reversed')
    mostrar_grafica(fig_box, f'Distribución de {senal_sel} por género',
                    alto=max(360, 28 * len(orden_gen) + 80))

    # Comparativa simultánea de medianas log10 de Plays, Wishlist y Backlogs
    resumen_tres = []
    for _, row in filtrado.dropna(subset=['Plays', 'Wishlist', 'Backlogs']).iterrows():
        for g in row['generos']:
            if g in orden_gen:
                resumen_tres.append(
                    {
                        'Genero': g,
                        'Plays': row['Plays'],
                        'Wishlist': row['Wishlist'],
                        'Backlogs': row['Backlogs'],
                    }
                )
    if resumen_tres:
        df_med = (
            pd.DataFrame(resumen_tres)
            .groupby('Genero')[['Plays', 'Wishlist', 'Backlogs']]
            .median()
            .reindex(orden_gen)
            .reset_index()
        )
        fig_bar_log = go.Figure()
        colores_bar = COLOR_SENALES
        for senal in ['Plays', 'Backlogs', 'Wishlist']:
            fig_bar_log.add_trace(
                go.Bar(
                    name=senal,
                    x=df_med[senal],
                    y=df_med['Genero'],
                    orientation='h',
                    marker_color=colores_bar[senal],
                    marker_line_color='#000000',
                    marker_line_width=1.5,
                )
            )
        fig_bar_log.update_layout(barmode='group')
        fig_bar_log.update_xaxes(type='log', title_text='Mediana · escala logarítmica')
        fig_bar_log.update_yaxes(categoryorder='array', categoryarray=orden_gen, autorange='reversed')
        mostrar_grafica(fig_bar_log, 'Medianas de Plays, Backlogs y Wishlist',
                        alto=max(380, 33 * len(orden_gen) + 125))

else:
    st.info('No hay registros con los filtros actuales para construir la distribución por género.')

# ---------------------------------------------------------------------------
# 3. DISPERSIÓN / DENSIDAD ENTRE RATING (USUARIOS) Y METACRITIC (PRENSA)
# ---------------------------------------------------------------------------
section_banner(
    'Recepción: Comunidad (Rating) vs. Prensa (Metacritic)',
    'Diagrama de Dispersión y Densidad Conjunta en Pares Elegibles',
)

modo_scatter = st.radio(
    'Modo de visualización conjunta',
    options=['Dispersión + Contornos de Densidad', 'Mapa de Calor 2D (Densidad)', 'Solo Dispersión'],
    horizontal=True,
)

juegos_consulta = filtrado
if len(pares_filtrados):
    if modo_scatter == 'Mapa de Calor 2D (Densidad)':
        fig_sc = px.density_heatmap(
            pares_filtrados,
            x='critica_verificada_csv',
            y='Rating',
            nbinsx=22,
            nbinsy=22,
            color_continuous_scale=[PALETA['bg-primary'], PALETA['bg-chart'], PALETA['primary'], PALETA['secondary'], PALETA['accent'], PALETA['text-primary']],
            labels={
                'critica_verificada_csv': 'Metacritic Rating (0–100)',
                'Rating': 'Rating Usuarios Backloggd (0–5)',
            },
        )
    else:
        fig_sc = go.Figure()
        if modo_scatter == 'Dispersión + Contornos de Densidad' and len(pares_filtrados) >= 15:
            fig_sc.add_trace(
                go.Histogram2dContour(
                    x=pares_filtrados['critica_verificada_csv'],
                    y=pares_filtrados['Rating'],
                    colorscale=[[0, 'rgba(5,13,34,0)'], [0.5, 'rgba(23,13,55,0.55)'], [1, 'rgba(0,207,255,0.65)']],
                    showscale=False,
                    line=dict(color=PALETA['secondary'], width=1),
                    hoverinfo='skip',
                )
            )
        fig_sc.add_trace(
            go.Scatter(
                x=pares_filtrados['critica_verificada_csv'],
                y=pares_filtrados['Rating'],
                mode='markers',
                name='Videojuegos',
                text=pares_filtrados['Title'],
                customdata=np.stack(
                    [
                        pares_filtrados['anio'].fillna(0).astype(int),
                        pares_filtrados['brecha_vista'].round(1),
                        pares_filtrados['id_juego'],
                    ],
                    axis=-1,
                ).tolist(),
                hovertemplate=(
                    '<b>%{text}</b> (%{customdata[0]})<br>'
                    'Metacritic: %{x:.0f} / 100<br>'
                    'Rating Usuarios: %{y:.2f} / 5.0<br>'
                    'Brecha (Rating×20 − Meta): %{customdata[1]:+.1f} pts<extra></extra>'
                ),
                marker=dict(
                    color=PALETA['primary'],
                    size=7,
                    opacity=0.82,
                    line=dict(color=PALETA['text-primary'], width=0.8),
                ),
            )
        )
        # Línea de paridad (Rating * 20 == Metacritic)
        x_ref = np.linspace(
            max(20, float(pares_filtrados['critica_verificada_csv'].min())),
            min(100, float(pares_filtrados['critica_verificada_csv'].max())),
            50,
        )
        fig_sc.add_trace(
            go.Scatter(
                x=x_ref,
                y=x_ref / 20.0,
                mode='lines',
                name='Paridad',
                line=dict(color=PALETA['accent'], width=2, dash='dash'),
            )
        )
        fig_sc.update_xaxes(title_text='Metacritic Rating (Escala 0–100)')
        fig_sc.update_yaxes(title_text='Rating de Usuarios (Escala 0–5)')

    fig_sc.update_xaxes(title_text='Metacritic (0–100)')
    fig_sc.update_yaxes(title_text='Usuarios (0–5)')
    if modo_scatter == 'Mapa de Calor 2D (Densidad)':
        fig_sc.update_coloraxes(colorbar=dict(title='Juegos', thickness=10))
        mostrar_grafica(fig_sc, 'Densidad de calificaciones', alto=430)
    else:
        st.caption('Selecciona puntos, un rectángulo o un lazo para consultar esos juegos en la tabla.')
        huella_pares = hashlib.sha256(pares_filtrados['id_juego'].to_numpy(dtype='int64').tobytes()).hexdigest()[:16]
        revision = st.session_state.get('eda_revision_seleccion', 0)
        seleccion = mostrar_grafica(
            fig_sc, 'Calificaciones de usuarios y prensa', alto=430,
            key=f'recepcion_{modo_scatter}_{huella_pares}_{revision}', on_select='rerun',
            selection_mode=('points', 'box', 'lasso'),
        )
        ids_seleccion = {
            int(datos[2])
            for punto in seleccion.selection.points
            if isinstance(datos := punto.get('customdata'), (list, tuple)) and len(datos) >= 3
        }
        if ids_seleccion:
            st.button('Quitar selección de la gráfica', on_click=limpiar_seleccion)
            juegos_consulta = filtrado[filtrado['id_juego'].isin(ids_seleccion)]
else:
    st.info('No hay pares completos de Rating y Metacritic bajo los filtros seleccionados.')

st.subheader('Juegos de la consulta')
cantidad = len(juegos_consulta)
resultado = 'juego' if cantidad == 1 else 'juegos'
st.caption(f'{cantidad:,} {resultado} en la tabla. La selección del gráfico acota esta consulta y su CSV.')
columnas = ['Title', 'anio', 'Rating', 'critica_verificada_csv', 'brecha_vista', 'Plays', 'Backlogs', 'Wishlist']
consulta = juegos_consulta[columnas].rename(columns={
    'Title': 'Juego', 'anio': 'Año', 'Rating': 'Usuarios', 'critica_verificada_csv': 'Metacritic',
    'brecha_vista': 'Brecha (pts)',
})
st.dataframe(consulta, hide_index=True, width='stretch', height=300)
st.download_button('Descargar juegos de la consulta', consulta.to_csv(index=False).encode('utf-8'),
                   'consulta_dashboard.csv', 'text/csv', disabled=consulta.empty)

# ---------------------------------------------------------------------------
# 4. ANÁLISIS DE LA BRECHA USUARIOS-CRÍTICA POR GÉNERO Y ESTUDIO
# ---------------------------------------------------------------------------
section_banner(
    'Análisis de la Brecha Usuarios–Crítica',
    'Rating Escalado a 100 (Rating × 20) vs. Metacritic por Género y Organización',
)

st.caption('Comparación descriptiva sobre los pares completos del catálogo elegible.')
st.write(
    'Definimos la brecha en escala homogénea de 100 puntos como '
    r'$\text{Brecha} = (\text{Rating} \times 20) - \text{Metacritic}$. '
    'Valores negativos indican que la prensa especializada calificó más alto que el promedio de usuarios; '
    'la **brecha absoluta media** mide la magnitud típica del desacuerdo sin que signos opuestos se cancelen.'
)

dim_brecha = st.radio(
    'Desglosar brecha y correlación por:',
    options=['Género', 'Estudio / Organización (Team)'],
    horizontal=True,
)

archivo_corr = (
    'clustering_03_correlaciones_generos.csv'
    if dim_brecha == 'Género'
    else 'clustering_03_correlaciones_organizaciones.csv'
)
if dim_brecha != 'Género':
    st.warning(
        'Nota de auditoría: El campo `Team` en Backloggd agrupa desarrolladores y publishers sin separar su rol. '
        'Se reportan únicamente organizaciones con al menos 20 pares verificados.'
    )

df_brecha = read_report(archivo_corr).query('estado == "incluido"').copy()
metrica_orden = st.selectbox(
    'Métrica de desacuerdo a graficar',
    options=['brecha_absoluta_media', 'brecha_media'],
    format_func=lambda m: (
        'Brecha absoluta media'
        if m == 'brecha_absoluta_media'
        else 'Brecha media con signo'
    ),
)

df_plot_b = df_brecha.sort_values(metrica_orden, ascending=True)
colores_brecha = [
    PALETA['accent'] if i >= len(df_plot_b) - 3 else PALETA['primary']
    for i in range(len(df_plot_b))
]

fig_gap = go.Figure(
    go.Bar(
        x=df_plot_b[metrica_orden],
        y=df_plot_b['grupo'],
        orientation='h',
        marker=dict(color=colores_brecha, line=dict(color=PALETA['text-primary'], width=1)),
        customdata=np.stack(
            [
                df_plot_b['n'],
                df_plot_b['pearson_r'].round(3),
                df_plot_b['spearman_rho'].round(3),
            ],
            axis=-1,
        ),
        hovertemplate=(
            '<b>%{y}</b> (n = %{customdata[0]})<br>'
            'Valor brecha: %{x:.2f} pts<br>'
            'Pearson r: %{customdata[1]} · Spearman ρ: %{customdata[2]}<extra></extra>'
        ),
    )
)
etiquetas_grupos = [wrap(grupo, width=16) for grupo in df_plot_b['grupo']]
fig_gap.update_xaxes(title_text='Brecha (pts)')
fig_gap.update_yaxes(tickmode='array', tickvals=df_plot_b['grupo'],
                     ticktext=['<br>'.join(lineas) for lineas in etiquetas_grupos])
alto_por_grupo = max(32, 14 * max(map(len, etiquetas_grupos), default=1) + 8)
titulo_brecha = 'Brecha por género' if dim_brecha == 'Género' else 'Brecha por organización'
mostrar_grafica(fig_gap, titulo_brecha, alto=max(420, len(df_plot_b) * alto_por_grupo + 60))

configuracion_corr = {
    'grupo': 'Grupo',
    'n': st.column_config.NumberColumn('Pares (n)', format='%d'),
    'brecha_absoluta_media': st.column_config.NumberColumn('Brecha |Δ| media (pts)', format='%.2f'),
    'brecha_media': st.column_config.NumberColumn('Brecha media (pts)', format='%+.2f'),
    'pearson_r': st.column_config.NumberColumn('Pearson r', format='%.3f'),
    'spearman_rho': st.column_config.NumberColumn('Spearman ρ', format='%.3f'),
    'pearson_p': st.column_config.NumberColumn('p Pearson', format='%.2e'),
    'spearman_p': st.column_config.NumberColumn('p Spearman', format='%.2e'),
    'pearson_q_bh': st.column_config.NumberColumn('q BH Pearson', format='%.2e'),
    'spearman_q_bh': st.column_config.NumberColumn('q BH Spearman', format='%.2e'),
}

with st.expander('Análisis complementario de correlaciones y corrección por comparaciones múltiples'):
    correlacion = read_report('clustering_03_correlaciones_catalogo.csv').iloc[0]
    st.caption(
        f'Catálogo elegible completo: Pearson r = {correlacion["pearson_r"]:.3f}, '
        f'Spearman ρ = {correlacion["spearman_rho"]:.3f} ({int(correlacion["n"]):,} pares). '
        'La comparación por grupo usa este mismo alcance.'
    )
    columnas_tabla = [
        'grupo',
        'n',
        'brecha_absoluta_media',
        'brecha_media',
        'pearson_r',
        'pearson_p',
        'pearson_q_bh',
        'spearman_rho',
        'spearman_p',
        'spearman_q_bh',
    ]
    st.dataframe(
        df_brecha[columnas_tabla],
        hide_index=True,
        width='stretch',
        column_config=configuracion_corr,
    )
    st.download_button(
        'Descargar tabla de correlaciones y brechas (CSV)',
        df_brecha.to_csv(index=False).encode('utf-8'),
        archivo_corr,
        'text/csv',
    )

# ---------------------------------------------------------------------------
# 5. SEGMENTACIÓN NO SUPERVISADA (CLUSTERING K-MEANS Y DBSCAN — FASE 4A)
# ---------------------------------------------------------------------------
section_banner(
    'Perfiles de Popularidad y Recepción (Clustering Fase 4A)',
    'K-Means y agrupamiento jerárquico con enlace de Ward',
)

profiles = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
metodo = st.radio('Método de agrupamiento', ['K-Means', 'Ward'], horizontal=True)
comparacion = read_report('clase_comparacion_clustering.csv')
st.caption('Mismos juegos y variables para ambos métodos. Cada corte se eligió por silueta entre 2 y 10 grupos.')
st.dataframe(comparacion, hide_index=True, width='stretch', column_config={
    'metodo': 'Método', 'k': 'Grupos',
    'silhouette': st.column_config.NumberColumn('Silueta ↑', format='%.3f'),
    'davies_bouldin': st.column_config.NumberColumn('Davies–Bouldin ↓', format='%.3f'),
    'calinski_harabasz': st.column_config.NumberColumn('Calinski–Harabasz ↑', format='%.1f'),
})

agrupados = profiles[profiles.incluido_clustering & profiles['id_juego'].isin(filtrado['id_juego'])].copy()
if metodo == 'Ward':
    asignaciones = read_report('clase_ward_asignaciones.csv')
    agrupados = agrupados.merge(asignaciones, on='id_juego', validate='one_to_one')
    columna = 'cluster_ward'
    resumen = read_report('clase_ward_perfiles.csv')
    arbol = json.loads((REPORTS / 'clase_ward_dendrograma.json').read_text())
    figura_ward = go.Figure()
    for x, y in zip(arbol['x'], arbol['y']):
        figura_ward.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color=PALETA['primary']),
                                         showlegend=False, hovertemplate='Distancia %{y:.2f}<extra></extra>'))
    figura_ward.update_xaxes(tickmode='array', tickvals=[5+10*i for i in range(len(arbol['hojas']))],
                             ticktext=arbol['hojas'], tickangle=-45, title_text='Ramas resumidas')
    figura_ward.update_yaxes(title_text='Distancia de Ward')
    mostrar_grafica(figura_ward, 'Dendrograma de Ward', alto=360)
    st.caption('Vista de las 12 últimas ramas del ajuste completo. Los paréntesis indican cuántos juegos resume cada rama.')
else:
    columna = 'cluster_kmeans'
    resumen = read_report('clustering_03_perfiles.csv').query("metodo == 'kmeans'")

st.caption('La tabla describe los grupos completos. El mapa PCA responde a los filtros del dashboard.')
st.dataframe(resumen, hide_index=True, width='stretch')
agrupados['perfil'] = agrupados[columna].astype(int).astype(str)

fig_pca = px.scatter(
    agrupados,
    x='componente_1',
    y='componente_2',
    color='perfil',
    hover_name='Title',
    hover_data=['Release Date', 'Rating', 'Metacritic Rating', 'Plays'],
    color_discrete_map={'0': PALETA['primary'], '1': PALETA['accent'], '-1': PALETA['secondary']},
    labels={
        'componente_1': 'Componente 1',
        'componente_2': 'Componente 2',
        'perfil': 'Cluster',
    },
)
fig_pca.update_traces(marker=dict(size=7, opacity=0.85, line=dict(width=0.7, color='#000000')))
if agrupados.empty:
    st.info('La consulta no contiene juegos con coordenadas PCA.')
else:
    mostrar_grafica(fig_pca, f'PCA · {metodo} · {sum(analysis["pca_varianza"]):.1%} de varianza explicada', alto=430)

with st.expander('Selección de grupos y comparación de K-Means con Weka'):
    st.markdown('**Comparación de alternativas k=2, k=3 y k=4:**')
    st.dataframe(read_report('clustering_03_alternativas_k.csv'), hide_index=True, width='stretch')
    st.markdown('**Búsqueda de parámetros:**')
    st.dataframe(
        read_report('clustering_03_seleccion_kmeans.csv' if metodo == 'K-Means' else 'clase_ward_cortes.csv'),
        hide_index=True,
        width='stretch',
    )
    try:
        st.markdown('**Comparación reproducible contra Weka 3.8.6:**')
        st.dataframe(read_report('weka/comparacion.csv'), hide_index=True, width='stretch')
    except FileNotFoundError:
        st.info('Reporte de Weka no encontrado en este entorno.')

manual_checks()

````

## 2_Prediccion.py

Ruta: `Final/pages/2_Prediccion.py` · Bytes: 15168 · SHA-256: `f42f62999d259d858107da6d2c42b2748d900dbf418a68b8391f67436a5e4fc6`

````text
"""Página 2 — Predicción e Inferencia: Menú de Batalla Persona 5 y Vecinos Más Cercanos."""
import importlib
import numpy as np
import pandas as pd
import streamlit as st

import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v8-neon':
    importlib.reload(_ui)

from src.similitud import cinco_vecinos
from src.inferencia import predecir_formulario
from src.ui import (
    _p5_ascii,
    asset_b64,
    manual_checks,
    read_report,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
    trigger_select_sfx,
)

setup(
    'Predicción e Inferencia de Popularidad',
    'Menú Táctico de Inferencia · Clasificador Supervisado · NearestNeighbors en Entrenamiento',
    transition='resume',
    menu_idx=2,
    compact_menu=True,
)

render_lb_rb_nav('BATTLE MENU // PREDICCION')

df, bundle, analysis = resources()
pipeline = bundle['pipeline']
metricas = bundle['metricas']

# Taxonomía aprendida por el preprocesador en entrenamiento
prep = pipeline.named_steps['preparar']
taxonomia_generos = sorted(prep.named_transformers_['generos'].vocabulario_)
estudios_frecuentes = sorted(prep.named_transformers_['estudio'].vocabulario_)
opciones_estudio = ['Otro / Organización no frecuente', *estudios_frecuentes]

char_b64 = asset_b64('img/char1.png')
char_html = (
    f'<img src="data:image/png;base64,{char_b64}" width="88" '
    f'style="float:right;margin-left:12px;filter:drop-shadow(4px 4px 0 #000);" alt="Tactical"/>'
    if char_b64 else ''
)

render_html(
    f"""
    <div class="p5-card-accent">
        {char_html}
        <div class="p5-font" style="font-size:1.45rem;color:var(--accent);">
            BATTLE MENU // SIMULADOR DE PROYECTO DE VIDEOJUEGO
        </div>
        <p style="margin:0.35rem 0 0 0;color:#f0f0f0;font-size:0.95rem;line-height:1.5;">
            Configura las 5 variables de entrada del modelo (<code>generos</code>, <code>estudio</code>, <code>decada</code>,
            <code>Metacritic Rating</code> y <code>Rating</code>) para estimar el tercil de popularidad relativa
            (<strong>bajo</strong>, <strong>medio</strong>, <strong>alto</strong>) y recuperar los 5 títulos históricos más cercanos.
        </p>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 1. FORMULARIO DE ENTRADA ESTILO "MENÚ DE BATALLA P5"
# ---------------------------------------------------------------------------
section_banner('Configuración Táctica del Lanzamiento', 'Selecciona Atributos del Videojuego')

with st.form('p5_battle_inference_form'):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        generos_seleccionados = st.multiselect(
            'Géneros del videojuego (Taxonomía del modelo)',
            options=taxonomia_generos,
            default=['Adventure', 'RPG'] if 'Adventure' in taxonomia_generos and 'RPG' in taxonomia_generos else taxonomia_generos[:1],
            help='Selecciona al menos un género incluido en la taxonomía entrenada.',
        )
        estudio_seleccionado = st.selectbox(
            'Estudio / Organización (Team)',
            options=opciones_estudio,
            index=0,
            help='Estudios con presencia frecuente (>= 10 títulos en entrenamiento) u "Otro / Organización no frecuente".',
        )
        decada_seleccionada = st.selectbox(
            'Década de lanzamiento',
            options=[1980, 1990, 2000, 2010, 2020],
            index=4,
            format_func=lambda d: f'Década de {d}s',
        )

    with col_f2:
        metacritic_esperado = st.slider(
            'Metacritic Rating esperado (0 a 100)',
            min_value=0,
            max_value=100,
            value=82,
            step=1,
        )
        rating_esperado = st.slider(
            'Rating de usuarios esperado (0.0 a 5.0)',
            min_value=0.0,
            max_value=5.0,
            value=3.9,
            step=0.1,
        )
        sin_metacritic = st.checkbox(
            'Simular ausencia de calificación en Metacritic (usar imputación por mediana de entrenamiento)',
            value=False,
        )

    submitted = st.form_submit_button('⚔️ ANALIZAR / ENGAGE')

# Validación de al menos un género seleccionado
if not generos_seleccionados:
    st.warning(
        '⚠️ **ALERTA TÁCTICA:** Selecciona al menos un **género** en el menú antes de ejecutar la inferencia.'
    )
else:
    if submitted:
        trigger_select_sfx()

    estudio_valor = (
        ['Otro']
        if estudio_seleccionado == 'Otro / Organización no frecuente'
        else [estudio_seleccionado]
    )
    meta_valor = np.nan if sin_metacritic else float(metacritic_esperado)

    fila, prediccion, mapa_probs = predecir_formulario(
        pipeline, generos_seleccionados, estudio_valor, decada_seleccionada,
        meta_valor, rating_esperado,
    )

    # Vecinos más cercanos en el espacio predictivo de entrenamiento
    vecinos = cinco_vecinos(fila, pipeline)
    meta_df = df[['id_juego', 'anio', 'generos', 'popularidad_indice']].copy()
    meta_df['generos_texto'] = meta_df['generos'].map(lambda gs: ', '.join(gs))
    vecinos = vecinos.merge(
        meta_df[['id_juego', 'anio', 'generos_texto', 'popularidad_indice']],
        on='id_juego',
        how='left',
    )

    # -----------------------------------------------------------------------
    # 2. RESULTADOS DE LA INFERENCIA
    # -----------------------------------------------------------------------
    section_banner('Resultado de la Inferencia Supervisada', f'Modelo Activo: {metricas["modelo"]}')

    st.subheader(f'Nivel estimado de popularidad: {prediccion.upper()}')
    if sin_metacritic:
        st.warning(
            'Sin crítica de prensa: se usa la mediana del entrenamiento. '
            'La clase estimada puede cambiar al incorporar la nota real; '
            'la ausencia de una nota no equivale a mala recepción.'
        )

    col_r1, col_r2 = st.columns([1.25, 1])

    with col_r1:
        st.markdown(
            '<div class="p5-font" style="font-size:1.25rem;color:var(--accent);margin-bottom:0.6rem;">'
            '1 // PROBABILIDADES DE CLASE (MODELO SUPERVISADO)</div>',
            unsafe_allow_html=True,
        )
        barras_html = ''
        for nivel_key, etiqueta in [('alto', 'ALTO (Tercil Superior)'), ('medio', 'MEDIO (Tercil Central)'), ('bajo', 'BAJO (Tercil Inferior)')]:
            pct = mapa_probs.get(nivel_key, 0.0) * 100.0
            destacado = 'color:var(--primary);font-weight:900;' if nivel_key == prediccion else 'color:var(--text-primary);'
            barras_html += f"""
            <div class="p5-prob-row">
                <div class="p5-prob-header" style="{destacado}">
                    <span>{etiqueta}</span>
                    <span>{pct:.1f}%</span>
                </div>
                <div class="p5-prob-track">
                    <div class="p5-prob-fill" style="width:{pct:.4f}%;"></div>
                </div>
            </div>
            """
        render_html(f'<div class="p5-card">{barras_html}</div>')
        st.caption(
            f'Probabilidades de clase estimadas por {metricas["modelo"]}, sin calibración.'
        )

    with col_r2:
        # 2. Perfil de mercado (Cluster asignado por contexto de vecinos K-Means)
        clusters_validos = vecinos['cluster_kmeans'].dropna().astype(int)
        perfiles_tabla = read_report('clustering_03_perfiles.csv').query('metodo == "kmeans"')
        if len(clusters_validos):
            cluster_modal = int(clusters_validos.mode().iloc[0])
            fila_perfil = perfiles_tabla[perfiles_tabla['cluster'].astype(int) == cluster_modal]
            desc_perfil = (
                fila_perfil.iloc[0]['perfil_propuesto']
                if len(fila_perfil)
                else 'Perfil intermedio del catálogo'
            )
            etiqueta_comercial = (
                'Tracción Alta y Recepción Superior (Cluster 0)'
                if cluster_modal == 0
                else 'Nicho / Recepción y Alcance Moderados (Cluster 1)'
            )
        else:
            cluster_modal = -1
            desc_perfil = 'Sin cluster K-Means asignado en vecinos con crítica completa'
            etiqueta_comercial = 'Perfil en evaluación'

        # 4. Brecha típica contextual del género principal seleccionado
        genero_principal = generos_seleccionados[0]
        tabla_gen_corr = read_report('clustering_03_correlaciones_generos.csv')
        fila_gen = tabla_gen_corr[tabla_gen_corr['grupo'] == genero_principal]
        if len(fila_gen) and pd.notna(fila_gen.iloc[0]['brecha_absoluta_media']):
            brecha_abs_gen = float(fila_gen.iloc[0]['brecha_absoluta_media'])
            brecha_med_gen = float(fila_gen.iloc[0]['brecha_media'])
            n_gen = int(fila_gen.iloc[0]['n'])
            texto_brecha = (
                f'En <strong>{genero_principal}</strong> (n = {n_gen} pares verificados), '
                f'la brecha absoluta media es <strong>{brecha_abs_gen:.2f} pts</strong> sobre 100 '
                f'(brecha con signo: <strong>{brecha_med_gen:+.2f} pts</strong>).'
            )
        else:
            texto_brecha = (
                f'El género <strong>{genero_principal}</strong> no supera el umbral de 20 pares '
                'completos para estimar brecha paramétrica.'
            )

        brecha_usuario_input = (
            f'{(rating_esperado * 20.0 - metacritic_esperado):+.1f} pts'
            if not sin_metacritic
            else 'N/D (Metacritic ausente)'
        )

        render_html(
            f"""
            <div class="p5-card">
                <div class="p5-font" style="font-size:1.2rem;color:var(--accent);margin-bottom:0.4rem;">
                    2 // PERFIL DE MERCADO ASOCIADO (CLUSTER)
                </div>
                <div style="font-family:'ComicProyecto',sans-serif;font-size:1.5rem;color:var(--text-primary);">
                    {etiqueta_comercial}
                </div>
                <p style="font-size:0.9rem;color:#dddddd;margin:0.25rem 0 0.9rem 0;">
                    {desc_perfil} (según mayoría de vecinos cercanos en Fase 4A; el cluster no entra como predictor al modelo supervisado).
                </p>
                <hr style="border-color:var(--primary);margin:0.65rem 0;"/>
                <div class="p5-font" style="font-size:1.2rem;color:var(--accent);margin-bottom:0.4rem;">
                    4 // BRECHA TIPICA CONTEXTUAL ({_p5_ascii(genero_principal).upper()})
                </div>
                <p style="font-size:0.92rem;color:#f0f0f0;margin:0;">
                    {texto_brecha}<br/>
                    <span style="color:var(--accent);">Tu configuración actual (Rating×20 − Metacritic): <strong>{brecha_usuario_input}</strong></span>
                </p>
            </div>
            """
        )

    # -----------------------------------------------------------------------
    # 3. TÍTULOS MÁS SIMILARES (NEARESTNEIGHBORS) — BARRAS ANIMADAS + TABLA
    # -----------------------------------------------------------------------
    section_banner(
        '3 // Cinco Títulos Más Similares (NearestNeighbors)',
        'Calculados en el Espacio Predictivo de Entrenamiento (Sin Fuga del Conjunto de Prueba)',
    )

    tabla_vecinos = vecinos[
        ['id_juego', 'Title', 'anio', 'generos_texto', 'cluster_kmeans', 'distancia']
    ].copy()
    tabla_vecinos['anio'] = tabla_vecinos['anio'].fillna(0).astype(int)
    tabla_vecinos['cluster_kmeans'] = tabla_vecinos['cluster_kmeans'].map(
        lambda v: 'Sin cluster (sin crítica CSV)' if pd.isna(v) else f'Cluster {int(v)}'
    )

    chars_b64 = [
        asset_b64('img/char1.png'),
        asset_b64('img/char2.png'),
        asset_b64('img/char3.png'),
    ]
    vecinos_bars_html = ''
    for idx_v, row_v in tabla_vecinos.reset_index(drop=True).iterrows():
        act_cls = 'active' if idx_v == 0 else ''
        c_b64 = chars_b64[idx_v % len(chars_b64)]
        vecinos_bars_html += f"""
        <div class="sc-bar-outer {act_cls}">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{c_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">KNN #{idx_v + 1}</div>
                    <div class="sc-main">
                        <div class="sc-label">{_p5_ascii(row_v['Title'])}</div>
                        <div class="sc-subdesc">
                            Géneros: {row_v['generos_texto']} · {row_v['cluster_kmeans']}
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">YEAR</span>
                                <span class="sc-stat-num">{row_v['anio']}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">DIST</span>
                                <span class="sc-stat-num">{row_v['distancia']:.2f}</span>
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
        """
    render_html(f'<div class="sc-root">{vecinos_bars_html}</div>')

    st.dataframe(
        tabla_vecinos,
        hide_index=True,
        width='stretch',
        column_config={
            'id_juego': st.column_config.NumberColumn('ID', format='%d'),
            'Title': 'Videojuego',
            'anio': st.column_config.NumberColumn('Año', format='%d'),
            'generos_texto': 'Géneros',
            'cluster_kmeans': 'Perfil K-Means (Descriptivo)',
            'distancia': st.column_config.NumberColumn('Distancia Euclídea', format='%.3f'),
        },
    )

    # Leyenda legal obligatoria
    render_html(
        """
        <div class="p5-legal-footer">
            "Estimación orientativa basada en el catálogo curado de videojuegos; no constituye garantía de éxito comercial ni reemplaza un estudio de mercado financiero."
        </div>
        """
    )

manual_checks()


````

## 3_Acerca_del_modelo.py

Ruta: `Final/pages/3_Acerca_del_modelo.py` · Bytes: 14503 · SHA-256: `b3c97e49efba8b8f0bd14a7602a69872954cf61bd2f457b8b094d10f1e3dd225`

````text
"""Página 3 — Acerca del Modelo: Métricas, Comparación de Algoritmos, Matriz de Confusión e Importancia."""
import importlib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.visualizacion import PALETA
import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v8-neon':
    importlib.reload(_ui)

from vista_graficas import mostrar_grafica
from src.ui import (
    manual_checks,
    read_report,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

setup(
    'Acerca del Modelo Supervisado',
    'Evaluación Fase 4B · StratifiedGroupKFold (10 Pliegues) · Matriz de Confusión · Importancia por Gini',
    transition='default',
    menu_idx=3,
    compact_menu=True,
)

render_lb_rb_nav('MODEL LOG // EVALUACION FASE 4B')

df, bundle, analysis = resources()
metricas = bundle['metricas']
resumen_m = metricas['metricas']

# ---------------------------------------------------------------------------
# 1. KPIs DINÁMICOS DESDE models/metadata.json
# ---------------------------------------------------------------------------
section_banner('Ficha Técnica del Modelo Ganador', f'Algoritmo Seleccionado por CV: {metricas["modelo"]}')

render_html(
    f"""
    <div class="p5-kpi-grid">
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">Modelo Activo</div>
            <div class="p5-kpi-value" style="font-size:1.75rem;">{metricas['modelo']}</div>
            <div class="p5-kpi-note">scikit-learn {metricas['version_sklearn']} · Semilla {metricas['semilla']}</div>
        </div>
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">F1 Macro (Prueba)</div>
            <div class="p5-kpi-value">{resumen_m['f1_macro']:.4f}</div>
            <div class="p5-kpi-note">CV 10-fold: {resumen_m['f1_macro_cv']:.4f} (Base Dummy: {resumen_m['f1_macro_referencia']:.4f})</div>
        </div>
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">Exactitud / Bal. Acc</div>
            <div class="p5-kpi-value">{resumen_m['exactitud']:.1%} / {resumen_m['balanced_accuracy']:.1%}</div>
            <div class="p5-kpi-note">Partición 80/20 por grupos (Train: {metricas['n_entrenamiento']} · Test: {metricas['n_prueba']})</div>
        </div>
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">Objetivo (Sin Fuga)</div>
            <div class="p5-kpi-value" style="font-size:1.45rem;">{metricas['definicion_objetivo']['version']}</div>
            <div class="p5-kpi-note">Cortes terciles: {metricas['definicion_objetivo']['cortes'][0]:.3f} y {metricas['definicion_objetivo']['cortes'][1]:.3f}</div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. COMPARACIÓN DE ALGORITMOS (reports/modelo_comparacion.csv)
# ---------------------------------------------------------------------------
section_banner(
    'Comparación de Algoritmos Supervisados',
    'Naive Bayes · CART · Random Forest · Red neuronal MLP · Referencia mayoritaria',
)

tabla_comp = read_report('modelo_comparacion.csv').copy()
nombres_legibles = {
    'DummyClassifier': 'DummyClassifier (Base Mayoritaria)',
    'CategoricalNB': 'Naive Bayes (CategoricalNB Discretizado)',
    'DecisionTreeClassifier': 'Árbol de Decisión (CART)',
    'RandomForestClassifier': 'Random Forest',
    'MLPClassifier': 'Red neuronal MLP',
}
nombres_cortos = {'DummyClassifier': 'REFERENCIA MAYORITARIA', 'CategoricalNB': 'NAIVE BAYES',
                 'DecisionTreeClassifier': 'ARBOL DE DECISION', 'RandomForestClassifier': 'RANDOM FOREST',
                 'MLPClassifier': 'RED NEURONAL MLP'}
tabla_comp['Algoritmo'] = tabla_comp['modelo'].map(lambda m: nombres_legibles.get(m, m))

# Interactive SideProjectsPage.jsx Split Shell (.sp-shell) for the 4 evaluated algorithms
sp_left_html = '<div class="sp-title">ALGORITHM LOG</div>'
sp_right_html = ''
orden_sp = tabla_comp.sort_values('f1_macro_cv', ascending=False).reset_index(drop=True)
for idx_m, row_m in orden_sp.iterrows():
    act_cls = 'active' if idx_m == 0 else ''
    disp_style = 'block' if idx_m == 0 else 'none'
    tag_txt = 'WINNER // CV 10-FOLD' if idx_m == 0 else f'CANDIDATE #{idx_m + 1}'
    sp_left_html += f"""
    <div class="sp-item {act_cls}" data-sp-target="alg-{idx_m}">
        <div class="sp-item-title">{nombres_cortos[row_m['modelo']]}</div>
        <div class="sp-item-stack">F1 CV: {row_m['f1_macro_cv']:.4f} · F1 TEST: {row_m['f1_macro_prueba']:.4f}</div>
    </div>
    """
    sp_right_html += f"""
    <div class="sp-right" data-sp-id="alg-{idx_m}" style="display:{disp_style};">
        <div class="sp-tag">{tag_txt}</div>
        <div class="sp-right-title">{nombres_cortos[row_m['modelo']]}</div>
        <div class="sp-right-summary">
            <strong>{row_m['Algoritmo']}</strong><br/>
            F1 Macro CV (10-fold): {row_m['f1_macro_cv']:.4f} (±{row_m['desviacion_cv']:.4f})<br/>
            F1 Macro Prueba (Holdout n={metricas["n_prueba"]}): {row_m['f1_macro_prueba']:.4f}<br/>
            Exactitud Prueba: {row_m['exactitud_prueba']:.1%} · Balanced Accuracy: {row_m['balanced_accuracy_prueba']:.1%}<br/>
        </div>
        <div class="sp-link">PARAMS: {row_m['mejores_parametros']}</div>
    </div>
    """

render_html(
    f'<div class="sp-shell"><div class="sp-left">{sp_left_html}</div><div>{sp_right_html}</div></div>'
)

st.dataframe(
    tabla_comp[
        [
            'Algoritmo',
            'f1_macro_cv',
            'desviacion_cv',
            'exactitud_prueba',
            'f1_macro_prueba',
            'balanced_accuracy_prueba',
            'mejores_parametros',
        ]
    ],
    hide_index=True,
    width='stretch',
    column_config={
        'f1_macro_cv': st.column_config.NumberColumn('F1 Macro CV (10-fold)', format='%.4f'),
        'desviacion_cv': st.column_config.NumberColumn('Desv. Est. CV', format='%.4f'),
        'exactitud_prueba': st.column_config.NumberColumn('Exactitud (Test)', format='%.4f'),
        'f1_macro_prueba': st.column_config.NumberColumn('F1 Macro (Test)', format='%.4f'),
        'balanced_accuracy_prueba': st.column_config.NumberColumn('Balanced Accuracy (Test)', format='%.4f'),
        'mejores_parametros': 'Hiperparámetros Óptimos (CV)',
    },
)

fig_comp = go.Figure()
filas_modelos = np.arange(len(tabla_comp))
etiquetas_modelos = {
    'DummyClassifier': 'Referencia<br>mayoritaria',
    'CategoricalNB': 'Naive Bayes',
    'DecisionTreeClassifier': 'Árbol de<br>decisión',
    'RandomForestClassifier': 'Random Forest',
    'MLPClassifier': 'Red neuronal<br>MLP',
}
for desplazamiento, etiqueta, campo, color in [
    (-.22, 'F1 macro CV', 'f1_macro_cv', PALETA['primary']),
    (0, 'F1 macro prueba', 'f1_macro_prueba', PALETA['secondary']),
    (.22, 'Exactitud prueba', 'exactitud_prueba', PALETA['accent']),
]:
    es_cv = campo == 'f1_macro_cv'
    fig_comp.add_trace(go.Scatter(
        name=etiqueta,
        mode='markers',
        y=filas_modelos + desplazamiento,
        x=tabla_comp[campo],
        error_x=dict(array=tabla_comp['desviacion_cv'], color=color, thickness=2, width=5) if es_cv else None,
        text=tabla_comp['Algoritmo'],
        customdata=tabla_comp['desviacion_cv'] if es_cv else None,
        marker=dict(color=color, size=10, line=dict(color=PALETA['text-primary'], width=1)),
        hovertemplate='<b>%{text}</b><br>' + etiqueta + ': %{x:.3f}'
        + (' · DE %{customdata:.3f}' if es_cv else '') + '<extra></extra>',
    ))
fig_comp.update_xaxes(title_text='Puntaje (0–1)', range=[0, 1])
fig_comp.update_yaxes(
    tickmode='array', tickvals=filas_modelos,
    ticktext=[etiquetas_modelos.get(modelo, modelo) for modelo in tabla_comp['modelo']],
    range=[len(filas_modelos) - .5, -.5], fixedrange=True, ticklabelstandoff=8,
)
mostrar_grafica(fig_comp, 'Desempeño en validación cruzada y prueba', alto=465)
st.caption('Cada punto muestra el puntaje. El segmento azul indica ±1 desviación estándar del F1 macro entre los pliegues.')

st.caption(
    'La MLP se evalúa con los mismos pliegues y la misma prueba reservada que los otros clasificadores. '
    'Se ajusta una capa oculta y su regularización con F1 macro de validación cruzada.'
)

fila_prueba = tabla_comp.loc[tabla_comp['f1_macro_prueba'].idxmax()]
if fila_prueba['modelo'] != metricas['modelo']:
    st.caption(
        f"Modelo activo por validación cruzada: {nombres_legibles[metricas['modelo']]}. "
        f"Mayor F1 macro en prueba: {fila_prueba['Algoritmo']} "
        f"({fila_prueba['f1_macro_prueba']:.4f})."
    )

# ---------------------------------------------------------------------------
# 3. MATRIZ DE CONFUSIÓN Y VARIABLES MÁS INFLUYENTES (ANCHO COMPLETO)
# ---------------------------------------------------------------------------
# El ancho completo mantiene legibles títulos, intervalos y etiquetas.
col_cm, col_pi = st.container(), st.container()

with col_cm:
    section_banner('Matriz de Confusión (Holdout n = 222)', 'Mapa de Calor en Azul y Violeta')
    clases = metricas['clases']  # ['bajo', 'medio', 'alto']
    matriz = np.asarray(resumen_m['matriz_confusion'], dtype=int)

    texto_celdas = [[f'{val}' for val in fila] for fila in matriz]
    fig_cm = go.Figure(
        data=go.Heatmap(
            z=matriz,
            x=[c.upper() for c in clases],
            y=[c.upper() for c in clases],
            text=texto_celdas,
            texttemplate='',
            textfont=dict(size=18, color=PALETA['text-primary'], family='ComicProyecto, sans-serif'),
            colorscale=[
                [0.0, PALETA['bg-chart-deep']],
                [0.35, PALETA['purple-deep']],
                [0.7, PALETA['secondary']],
                [1.0, PALETA['text-primary']],
            ],
            colorbar=dict(title='Juegos', thickness=10),
            hovertemplate='Clase Real: <b>%{y}</b><br>Clase Predicha: <b>%{x}</b><br>Juegos: <b>%{z}</b><extra></extra>',
        )
    )
    for fila, clase_real in enumerate(clases):
        for columna, clase_predicha in enumerate(clases):
            valor = int(matriz[fila, columna])
            fig_cm.add_annotation(x=clase_predicha.upper(), y=clase_real.upper(),
                                  text=str(valor), showarrow=False,
                                  font=dict(size=18, color=PALETA['bg-primary'] if valor >= .65 * matriz.max() else PALETA['text-primary']))
    fig_cm.update_xaxes(title_text='Clase predicha')
    fig_cm.update_yaxes(title_text='Clase real', autorange='reversed')
    mostrar_grafica(fig_cm, 'Clases reales frente a predicciones', alto=390)

with col_pi:
    section_banner('Importancia de variables en Random Forest', 'Reducción de impureza de Gini')
    df_gini = read_report('modelo_importancia_gini.csv').sort_values('importancia')
    etiquetas = {'Rating': 'Usuarios', 'Metacritic Rating': 'Metacritic',
                 'generos': 'Géneros', 'estudio': 'Organización', 'decada': 'Década'}
    figura_gini = go.Figure(go.Bar(
        x=df_gini['importancia'] * 100, y=df_gini['variable'].map(etiquetas),
        orientation='h', marker_color=PALETA['primary'],
        hovertemplate='%{y}: %{x:.2f} %<extra></extra>',
    ))
    figura_gini.update_xaxes(title_text='Importancia relativa (%)', rangemode='tozero')
    figura_gini.update_yaxes(ticklabelstandoff=8)
    mostrar_grafica(figura_gini, 'Contribución a la reducción de impureza', alto=360)
    st.caption('Se suman las contribuciones de las columnas codificadas de cada variable original. '
               f'Esta gráfica explica Random Forest. Modelo activo: {nombres_legibles[metricas["modelo"]]}. ')

# ---------------------------------------------------------------------------
# 4. REPORTE DETALLADO POR CLASE Y AUDITORÍA DE IMPUTACIÓN
# ---------------------------------------------------------------------------
section_banner('Desempeño Desglosado por Clase y Diagnóstico de Ausencia', 'Auditoría Metodológica Fase 4B')

col_d1, col_d2 = st.columns(2)
with col_d1:
    st.markdown('**Precisión, Recall y F1-Score por Tercil en Prueba:**')
    filas_clases = []
    for c in metricas['clases']:
        info_c = resumen_m['reporte_clases'][c]
        filas_clases.append(
            {
                'Clase': c.upper(),
                'Soporte (n)': int(info_c['support']),
                'Precisión': info_c['precision'],
                'Recall (Sensibilidad)': info_c['recall'],
                'F1-Score': info_c['f1-score'],
            }
        )
    st.dataframe(
        pd.DataFrame(filas_clases),
        hide_index=True,
        width='stretch',
        column_config={
            'Precisión': st.column_config.NumberColumn(format='%.3f'),
            'Recall (Sensibilidad)': st.column_config.NumberColumn(format='%.3f'),
            'F1-Score': st.column_config.NumberColumn(format='%.3f'),
        },
    )

with col_d2:
    st.markdown('**Recall Comparativo por Clase entre los 4 Modelos:**')
    err_df = read_report('modelo_error_por_clase.csv')
    st.dataframe(
        err_df,
        hide_index=True,
        width='stretch',
        column_config={
            'modelo': 'Modelo',
            'clase': 'Clase',
            'n': st.column_config.NumberColumn('Total Clase', format='%d'),
            'aciertos': st.column_config.NumberColumn('Aciertos', format='%d'),
            'recall': st.column_config.NumberColumn('Recall', format='%.3f'),
        },
    )

with st.expander('Diagnóstico de Imputación de Metacritic y Prevención de Fuga (Metadata JSON)'):
    diag = metricas.get('diagnostico_ausencia', {})
    st.markdown(
        f"""
        - **Definición del objetivo sin fuga:** `{metricas['definicion_objetivo']['formula']}` calculado exclusivamente sobre los `n = {metricas['n_entrenamiento']}` juegos de entrenamiento (`{metricas['definicion_objetivo']['version']}`).
        - **Partición por grupos de título (`GroupShuffleSplit`):** Garantiza 0 títulos compartidos entre entrenamiento y prueba (evita contaminar ediciones multiplataforma).
        - **Sensibilidad al ocultar crítica (`n = {diag.get('n_criticas_ocultadas', 180)}` casos en prueba):** Cambio mediano en probabilidad de clase baja = `{diag.get('delta_probabilidad_bajo_mediana', 0.0):.4f}` · F1 macro en ablación sin Metacritic = `{diag.get('f1_macro_ablacion_sin_critica', 0.0):.4f}`.
        """
    )

manual_checks()


````

