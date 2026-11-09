"""Página 1 — Exploración (EDA, Brecha Usuarios-Crítica y Perfiles de Clustering)."""
import importlib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v7-delegated':
    importlib.reload(_ui)

from src.config import CLEAN
from src.ui import (
    asset_b64,
    manual_checks,
    p5_plotly_layout,
    read_report,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

setup(
    'Exploración y Brecha Usuarios–Crítica',
    'Análisis Exploratorio (EDA) · Interacción en Escala Logarítmica · Discrepancia Prensa vs. Comunidad',
    transition='about',
    menu_idx=1,
    compact_menu=True,
)

render_lb_rb_nav('EXPLORACION // EDA & BRECHA')

df, bundle, analysis = resources()
elegibles = df.loc[df['elegible_analisis']].copy()
elegibles['rating_100_vista'] = elegibles['Rating'] * 20.0
elegibles['brecha_vista'] = elegibles['rating_100_vista'] - elegibles['critica_verificada_csv']

# ---------------------------------------------------------------------------
# 1. FILTROS INTERACTIVOS EN BARRA LATERAL ESTILIZADA
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="p5-font" style="font-size:1.25rem;color:#ffe600;margin-top:0.5rem;">'
        'FILTROS TACTICOS // EDA</div>',
        unsafe_allow_html=True,
    )
    todos_generos = sorted({g for row in elegibles['generos'] for g in row})
    generos_sel = st.multiselect(
        'Filtrar por género',
        options=todos_generos,
        default=[],
        placeholder='Todos los géneros',
    )
    decadas_disp = sorted(int(d) for d in elegibles['decada'].dropna().unique() if int(d) > 0)
    decadas_sel = st.multiselect(
        'Filtrar por década',
        options=decadas_disp,
        default=[],
        format_func=lambda d: f'{d}s',
        placeholder='Todas las décadas',
    )
    rango_rating = st.slider(
        'Rango de Rating de Usuarios (0–5)',
        min_value=0.0,
        max_value=5.0,
        value=(0.0, 5.0),
        step=0.1,
    )
    rango_meta = st.slider(
        'Rango de Metacritic (0–100)',
        min_value=0,
        max_value=100,
        value=(0, 100),
        step=1,
    )

filtrado = elegibles.copy()
if generos_sel:
    filtrado = filtrado[filtrado['generos'].map(lambda gs: any(g in gs for g in generos_sel))]
if decadas_sel:
    filtrado = filtrado[filtrado['decada'].isin(decadas_sel)]
filtrado = filtrado[
    filtrado['Rating'].isna()
    | filtrado['Rating'].between(rango_rating[0], rango_rating[1])
]
filtrado = filtrado[
    filtrado['critica_verificada_csv'].isna()
    | filtrado['critica_verificada_csv'].between(rango_meta[0], rango_meta[1])
]

cat_corr = read_report('clustering_03_correlaciones_catalogo.csv').iloc[0]
brecha_media_global = float(elegibles['brecha_vista'].dropna().mean())
brecha_abs_global = float(elegibles['brecha_vista'].dropna().abs().mean())

newsign_b64 = asset_b64('img/newsign.png')
icon1_b64 = asset_b64('img/icon1.png')
icon2_b64 = asset_b64('img/icon2.png')
icon3_b64 = asset_b64('img/icon3.png')

render_html(
    f"""
    <div class="sc-info-bar-list">
        <div class="sc-info-bar-wrap selected">
            <img class="sc-info-bar-new" src="data:image/png;base64,{newsign_b64}" alt=""/>
            <div class="sc-info-bar">
                <div class="sc-info-bar-icon-wrap"><img class="sc-info-bar-icon" src="data:image/png;base64,{icon1_b64}" alt=""/></div>
                <span class="sc-info-bar-text">TITULOS FILTRADOS EN VISTA ACTUAL</span>
                <span class="sc-info-bar-box">COHORTE</span>
                <span class="sc-info-bar-count">{len(filtrado):,} / {len(elegibles):,}</span>
            </div>
        </div>
        <div class="sc-info-bar-wrap">
            <div class="sc-info-bar">
                <div class="sc-info-bar-icon-wrap"><img class="sc-info-bar-icon" src="data:image/png;base64,{icon2_b64}" alt=""/></div>
                <span class="sc-info-bar-text">CORRELACION CATALOGO (N = {int(cat_corr['n'])} PARES VERIFICADOS)</span>
                <span class="sc-info-bar-box">PEARSON / SPEARMAN</span>
                <span class="sc-info-bar-count">r = {cat_corr['pearson_r']:.3f} · ρ = {cat_corr['spearman_rho']:.3f}</span>
            </div>
        </div>
        <div class="sc-info-bar-wrap">
            <div class="sc-info-bar">
                <div class="sc-info-bar-icon-wrap"><img class="sc-info-bar-icon" src="data:image/png;base64,{icon3_b64}" alt=""/></div>
                <span class="sc-info-bar-text">BRECHA TIPICA GLOBAL (RATING × 20 − METACRITIC)</span>
                <span class="sc-info-bar-box">|Δ| MEDIA</span>
                <span class="sc-info-bar-count">{brecha_abs_global:.2f} PTS ({brecha_media_global:+.2f})</span>
            </div>
        </div>
    </div>
    """
)

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
        x='Genero',
        y=senal_sel,
        category_orders={'Genero': orden_gen},
        color_discrete_sequence=['#d92323'],
        points='outliers',
        hover_data=['Title'],
    )
    fig_box.update_traces(
        marker=dict(color='#ffe600', size=5, opacity=0.75),
        line=dict(color='#ffffff', width=1.5),
        fillcolor='rgba(217, 35, 35, 0.65)',
    )
    fig_box.update_yaxes(type='log', title_text=f'{senal_sel} (Escala Log10)')
    fig_box.update_xaxes(title_text='Género')
    p5_plotly_layout(
        fig_box,
        title=f'Distribución Logarítmica de {senal_sel} por Género',
        height=440,
    )
    st.plotly_chart(fig_box, use_container_width=True)

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
        colores_bar = {'Plays': '#d92323', 'Backlogs': '#ffffff', 'Wishlist': '#7b7b7b'}
        for senal in ['Plays', 'Backlogs', 'Wishlist']:
            fig_bar_log.add_trace(
                go.Bar(
                    name=senal,
                    x=df_med['Genero'],
                    y=df_med[senal],
                    marker_color=colores_bar[senal],
                    marker_line_color='#000000',
                    marker_line_width=1.5,
                )
            )
        fig_bar_log.update_layout(barmode='group')
        fig_bar_log.update_yaxes(type='log', title_text='Mediana de Conteos (Escala Log10)')
        fig_bar_log.update_xaxes(title_text='Género')
        p5_plotly_layout(
            fig_bar_log,
            title='Comparativa de Medianas por Género: Plays vs. Backlogs vs. Wishlist',
            height=410,
        )
        st.plotly_chart(fig_bar_log, use_container_width=True)
else:
    st.info('No hay registros con los filtros actuales para construir la distribución por género.')

# ---------------------------------------------------------------------------
# 3. DISPERSIÓN / DENSIDAD ENTRE RATING (USUARIOS) Y METACRITIC (PRENSA)
# ---------------------------------------------------------------------------
section_banner(
    'Recepción: Comunidad (Rating) vs. Prensa (Metacritic)',
    'Diagrama de Dispersión y Densidad Conjunta en Pares Elegibles',
)

pares_filtrados = filtrado.dropna(subset=['Rating', 'critica_verificada_csv']).copy()
modo_scatter = st.radio(
    'Modo de visualización conjunta',
    options=['Dispersión + Contornos de Densidad', 'Mapa de Calor 2D (Densidad)', 'Solo Dispersión'],
    horizontal=True,
)

if len(pares_filtrados):
    if modo_scatter == 'Mapa de Calor 2D (Densidad)':
        fig_sc = px.density_heatmap(
            pares_filtrados,
            x='critica_verificada_csv',
            y='Rating',
            nbinsx=22,
            nbinsy=22,
            color_continuous_scale=['#0d0d0d', '#3d0a0a', '#732424', '#d92323', '#ffe600', '#ffffff'],
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
                    colorscale=[[0, 'rgba(13,13,13,0)'], [0.5, 'rgba(115,36,36,0.35)'], [1, 'rgba(217,35,35,0.65)']],
                    showscale=False,
                    line=dict(color='#732424', width=1),
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
                    ],
                    axis=-1,
                ),
                hovertemplate=(
                    '<b>%{text}</b> (%{customdata[0]})<br>'
                    'Metacritic: %{x:.0f} / 100<br>'
                    'Rating Usuarios: %{y:.2f} / 5.0<br>'
                    'Brecha (Rating×20 − Meta): %{customdata[1]:+.1f} pts<extra></extra>'
                ),
                marker=dict(
                    color='#d92323',
                    size=7,
                    opacity=0.82,
                    line=dict(color='#ffffff', width=0.8),
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
                name='Paridad exacta (Rating×20 = Metacritic)',
                line=dict(color='#ffe600', width=2, dash='dash'),
            )
        )
        fig_sc.update_xaxes(title_text='Metacritic Rating (Escala 0–100)')
        fig_sc.update_yaxes(title_text='Rating de Usuarios (Escala 0–5)')

    p5_plotly_layout(
        fig_sc,
        title='Relación entre Calificación de Prensa (Metacritic) y Comunidad (Rating)',
        height=460,
    )
    st.plotly_chart(fig_sc, use_container_width=True)
else:
    st.info('No hay pares completos de Rating y Metacritic bajo los filtros seleccionados.')

# ---------------------------------------------------------------------------
# 4. ANÁLISIS DE LA BRECHA USUARIOS-CRÍTICA POR GÉNERO Y ESTUDIO
# ---------------------------------------------------------------------------
section_banner(
    'Análisis de la Brecha Usuarios–Crítica',
    'Rating Escalado a 100 (Rating × 20) vs. Metacritic por Género y Organización',
)

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
        'Brecha absoluta media |Rating×20 − Metacritic| (Magnitud del desacuerdo)'
        if m == 'brecha_absoluta_media'
        else 'Brecha media con signo (Rating×20 − Metacritic)'
    ),
)

df_plot_b = df_brecha.sort_values(metrica_orden, ascending=True)
colores_brecha = [
    '#ffe600' if i >= len(df_plot_b) - 3 else '#d92323'
    for i in range(len(df_plot_b))
]

fig_gap = go.Figure(
    go.Bar(
        x=df_plot_b[metrica_orden],
        y=df_plot_b['grupo'],
        orientation='h',
        marker=dict(color=colores_brecha, line=dict(color='#ffffff', width=1)),
        text=df_plot_b[metrica_orden].map(lambda v: f'{v:.2f} pts'),
        textposition='outside',
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
fig_gap.update_xaxes(title_text='Puntos sobre escala 0–100')
fig_gap.update_yaxes(title_text=dim_brecha)
p5_plotly_layout(
    fig_gap,
    title=f'Desacuerdo Usuarios–Crítica por {dim_brecha} (Amarillo = Mayor Desacuerdo)',
    height=max(420, len(df_plot_b) * 26),
)
st.plotly_chart(fig_gap, use_container_width=True)

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

with st.expander('Ver tabla completa de correlaciones y brechas con corrección Benjamini–Hochberg (FDR)'):
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
    'Proyección PCA 2D y Diagnóstico K-Means / DBSCAN sobre 6 Variables',
)

profiles = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
resumen_perfiles = read_report('clustering_03_perfiles.csv')
method = st.radio('Algoritmo de agrupamiento a inspeccionar', ['kmeans', 'dbscan'], horizontal=True)

if method == 'dbscan' and analysis['dbscan_clusters'] < 2:
    st.warning(
        'DBSCAN identifica un núcleo denso principal (cluster 0) y 21 casos atípicos de densidad (-1); '
        'no separa múltiples segmentos comerciales.'
    )

column = f'cluster_{method}'
st.dataframe(
    resumen_perfiles[resumen_perfiles.metodo.eq(method)],
    hide_index=True,
    width='stretch',
)

agrupados = profiles[profiles.incluido_clustering].copy()
agrupados['perfil'] = agrupados[column].astype(int).astype(str)

fig_pca = px.scatter(
    agrupados,
    x='componente_1',
    y='componente_2',
    color='perfil',
    hover_name='Title',
    hover_data=['Release Date', 'Rating', 'Metacritic Rating', 'Plays'],
    color_discrete_sequence=['#d92323', '#ffe600', '#ffffff', '#7b7b7b'],
    labels={
        'componente_1': 'Componente Principal 1 (Tracción / Popularidad)',
        'componente_2': 'Componente Principal 2 (Recepción Crítica / Usuarios)',
        'perfil': 'Cluster',
    },
)
fig_pca.update_traces(marker=dict(size=7, opacity=0.85, line=dict(width=0.7, color='#000000')))
p5_plotly_layout(
    fig_pca,
    title=f'Mapa PCA 2D ({sum(analysis["pca_varianza"]):.1%} Varianza Explicada) — {method.upper()}',
    height=430,
)
st.plotly_chart(fig_pca, use_container_width=True)

with st.expander('Comparar k=2, k=3 y k=4, selección de hiperparámetros y validación cruzada con Weka'):
    st.markdown('**Comparación de alternativas k=2, k=3 y k=4:**')
    st.dataframe(read_report('clustering_03_alternativas_k.csv'), hide_index=True, width='stretch')
    st.markdown('**Búsqueda de parámetros:**')
    st.dataframe(
        read_report('clustering_03_seleccion_kmeans.csv' if method == 'kmeans' else 'clustering_03_sensibilidad_dbscan.csv'),
        hide_index=True,
        width='stretch',
    )
    try:
        st.markdown('**Comparación reproducible contra Weka 3.8.6:**')
        st.dataframe(read_report('weka/comparacion.csv'), hide_index=True, width='stretch')
    except FileNotFoundError:
        st.info('Reporte de Weka no encontrado en este entorno.')

manual_checks()
