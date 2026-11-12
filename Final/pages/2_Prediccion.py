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
st.info('Estimación orientativa basada en interacciones de Backloggd. No se estiman ventas. El modelo puede favorecer géneros populares y desfavorecer géneros de nicho.')

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

