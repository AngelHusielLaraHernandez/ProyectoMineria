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
