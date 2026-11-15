"""Predicción de popularidad y juegos parecidos."""
import html
import importlib
import sys
import numpy as np
import pandas as pd
import streamlit as st

import src.data as _data

if getattr(_data, '_MOD_VERSION', None) != 'p5-v14-menu':
    if 'src.config' in sys.modules:
        importlib.reload(sys.modules['src.config'])
    _data = importlib.reload(_data)
    _data.asegurar_modulos_vigentes(config_recargado=True)
else:
    _data.asegurar_modulos_vigentes()

from src.similitud import cinco_vecinos
from src.inferencia import predecir_formulario
from src.lectura_prediccion import comparar_probabilidad_alta, concluir_prediccion
from src.portadas import PORTADAS_LOCALES, PORTADAS_ORIGINALES, buscar_portadas
from src.ui import (
    _p5_ascii,
    asset_b64,
    read_report,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

portadas_en_cache = st.cache_data(ttl=3600, max_entries=128, show_spinner=False)(buscar_portadas)

setup(
    'Predicción de popularidad',
    'Prueba cómo cambia el nivel al modificar los datos de un juego.',
    transition='resume',
    menu_idx=3,
    compact_menu=True,
)

df, bundle, analysis = resources()
render_lb_rb_nav('MENÚ DE BATALLA // PREDICCIÓN')
pipeline = bundle['pipeline']
metricas = bundle['metricas']

# Taxonomía aprendida por el preprocesador en entrenamiento
prep = pipeline.named_steps['preparar']
taxonomia_generos = sorted(prep.named_transformers_['generos'].vocabulario_)
estudios_frecuentes = sorted(prep.named_transformers_['estudio'].vocabulario_)
opciones_estudio = ['Otro / Organización no frecuente', *estudios_frecuentes]
decadas_modelo = [int(x) for x in prep.named_transformers_['decada'].named_steps['codificar'].categories_[0]]
opciones_decada = [*sorted(d for d in decadas_modelo if d >= 0), *([-1] if -1 in decadas_modelo else [])]
indice_decada_defecto = opciones_decada.index(2020) if 2020 in opciones_decada else 0

section_banner('Datos del lanzamiento', 'Elige los géneros, la organización, la década y las notas')

with st.form('p5_battle_inference_form'):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        generos_seleccionados = st.multiselect(
            'Géneros del videojuego',
            options=taxonomia_generos,
            default=['Adventure', 'RPG'] if 'Adventure' in taxonomia_generos and 'RPG' in taxonomia_generos else taxonomia_generos[:1],
            help='Puedes elegir más de un género.',
        )
        estudio_seleccionado = st.selectbox(
            'Estudio o editora',
            options=opciones_estudio,
            index=0,
            help='Si la organización que buscas no aparece, elige «Otro».',
        )
        decada_seleccionada = st.selectbox(
            'Década de lanzamiento',
            options=opciones_decada,
            index=indice_decada_defecto,
            format_func=lambda d: 'Sin fecha interpretable (Década -1)' if d == -1 else f'Década de {d}s',
        )

    with col_f2:
        metacritic_esperado = st.slider(
            'Nota de prensa esperada (0 a 100)',
            min_value=0,
            max_value=100,
            value=82,
            step=1,
        )
        rating_esperado = st.slider(
            'Nota de usuarios esperada (0 a 5)',
            min_value=0.0,
            max_value=5.0,
            value=3.9,
            step=0.1,
        )
        sin_metacritic = st.checkbox(
            'Probar sin nota de prensa',
            value=False,
        )

    submitted = st.form_submit_button('⚔️ ANALIZAR LANZAMIENTO')

# Validación de al menos un género seleccionado
if not generos_seleccionados:
    st.warning(
        'Elige al menos un género para calcular el nivel de popularidad.'
    )
else:
    estudio_valor = (
        ['Otro']
        if estudio_seleccionado == 'Otro / Organización no frecuente'
        else [estudio_seleccionado]
    )
    meta_valor = np.nan if sin_metacritic else float(metacritic_esperado)

    fila, prediccion, mapa_probs = predecir_formulario(
        pipeline, generos_seleccionados, estudio_valor, decada_seleccionada,
        meta_valor, rating_esperado,
        temperatura=metricas['calibracion_web']['temperatura'],
    )

    # Vecinos más cercanos en el espacio predictivo de entrenamiento
    vecinos = cinco_vecinos(fila, pipeline, vecinos=bundle['vecinos'])
    meta_df = df[['id_juego', 'anio', 'generos', 'organizaciones', 'popularidad_indice']].copy()
    meta_df['generos_texto'] = meta_df['generos'].map(lambda gs: ', '.join(gs))
    vecinos = vecinos.merge(
        meta_df[['id_juego', 'anio', 'generos_texto', 'organizaciones', 'popularidad_indice']],
        on='id_juego',
        how='left',
    )

    # -----------------------------------------------------------------------
    # 2. RESULTADOS DE LA INFERENCIA
    # -----------------------------------------------------------------------
    section_banner('Resultado de la predicción', f'Modelo Activo: {metricas["modelo"]}')

    st.subheader(f'Nivel estimado de popularidad: {prediccion.upper()}')
    if sin_metacritic:
        st.warning(
            'Para este ejemplo usamos la nota de prensa que queda en medio al ordenar las del entrenamiento. '
            'Si luego ingresas la nota real, el resultado puede cambiar.'
        )

    col_r1, col_r2 = st.columns([1.25, 1])

    with col_r1:
        render_html(
            '<div class="p5-font" style="font-size:1.25rem;color:var(--accent);margin-bottom:0.6rem;">'
            'PROBABILIDAD CALIBRADA POR NIVEL</div>'
        )
        barras_html = ''
        for nivel_key, etiqueta in [('alto', 'ALTO'), ('medio', 'MEDIO'), ('bajo', 'BAJO')]:
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
            'La barra más larga indica el nivel que estima el modelo. Los porcentajes '
            'se ajustaron con predicciones de juegos de entrenamiento que quedaron fuera de cada pliegue.'
        )
        with st.expander('¿Qué significan alto, medio y bajo?'):
            corte_bajo, corte_alto = metricas['definicion_objetivo']['cortes']
            st.markdown(
                'Los niveles se definen con un índice de 0 a 1. Para calcularlo se compara '
                'cada juego con los del entrenamiento en partidas registradas, pendientes y '
                'listas de deseos. Después se promedian las tres posiciones relativas.'
            )
            st.markdown(
                f'- **Alto.** Índice por encima de {corte_alto:.4f}.\n'
                f'- **Medio.** Índice mayor que {corte_bajo:.4f} y hasta {corte_alto:.4f}.\n'
                f'- **Bajo.** Índice hasta {corte_bajo:.4f}.'
            )
            st.caption('Los cortes se muestran redondeados. Las barras estiman la probabilidad de caer en cada nivel.')

    with col_r2:
        # 2. Perfil de mercado (Cluster asignado por contexto de vecinos K-Means)
        clusters_validos = vecinos['cluster_kmeans'].dropna().astype(int)
        perfiles_tabla = read_report('tables/perfiles_clusters.csv').query('metodo == "K-Means"')
        if len(clusters_validos):
            cluster_modal = int(clusters_validos.mode().iloc[0])
            fila_perfil = perfiles_tabla[perfiles_tabla['cluster'].astype(int) == cluster_modal]
            desc_perfil = (
                fila_perfil.iloc[0]['perfil_propuesto']
                if len(fila_perfil)
                else 'Perfil intermedio del catálogo'
            )
            etiqueta_perfil = f'Grupo K-Means {cluster_modal}'
        else:
            cluster_modal = -1
            desc_perfil = 'Sin cluster K-Means asignado en vecinos con crítica completa'
            etiqueta_perfil = 'Perfil en evaluación'

        # 3. Brecha típica contextual del género principal seleccionado
        genero_principal = generos_seleccionados[0]
        genero_html = html.escape(str(genero_principal), quote=True)
        desc_perfil_html = html.escape(str(desc_perfil), quote=True)
        etiqueta_perfil_html = html.escape(str(etiqueta_perfil), quote=True)
        tabla_gen_corr = read_report('tables/correlacion_generos.csv')
        fila_gen = tabla_gen_corr[tabla_gen_corr['grupo'] == genero_principal]
        if (
            len(fila_gen)
            and fila_gen.iloc[0].get('estado') == 'incluido'
            and pd.notna(fila_gen.iloc[0]['brecha_absoluta_media'])
        ):
            brecha_abs_gen = float(fila_gen.iloc[0]['brecha_absoluta_media'])
            brecha_med_gen = float(fila_gen.iloc[0]['brecha_media'])
            n_gen = int(fila_gen.iloc[0]['n'])
            texto_brecha = (
                f'En <strong>{genero_html}</strong> ({n_gen} juegos con las dos notas), '
                f'la brecha absoluta media es <strong>{brecha_abs_gen:.2f} pts</strong> sobre 100 '
                f'(brecha media con signo: <strong>{brecha_med_gen:+.2f} pts</strong>).'
            )
        else:
            n_info = f' (n = {int(fila_gen.iloc[0]["n"])} pares)' if len(fila_gen) else ''
            texto_brecha = (
                f'Para <strong>{genero_html}</strong>{n_info} hacen falta al menos 20 juegos con ambas notas '
                'para calcular la diferencia media.'
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
                    GRUPO DE JUEGOS PARECIDOS
                </div>
                <div style="font-family:'ComicProyecto',sans-serif;font-size:1.5rem;color:var(--text-primary);">
                    {etiqueta_perfil_html}
                </div>
                <p style="font-size:0.9rem;color:#dddddd;margin:0.25rem 0 0.9rem 0;">
                    {desc_perfil_html}. Este grupo es el más común entre los juegos parecidos que aparecen abajo.
                </p>
                <hr style="border-color:var(--primary);margin:0.65rem 0;"/>
                <div class="p5-font" style="font-size:1.2rem;color:var(--accent);margin-bottom:0.4rem;">
                    DIFERENCIA ENTRE NOTAS ({html.escape(_p5_ascii(genero_principal).upper(), quote=True)})
                </div>
                <p style="font-size:0.92rem;color:#f0f0f0;margin:0;">
                    {texto_brecha}<br/>
                    <span style="color:var(--accent);">Diferencia con las notas que elegiste: <strong>{brecha_usuario_input}</strong></span>
                </p>
            </div>
            """
        )

    st.subheader('Conclusión de esta consulta')
    imputador = prep.named_transformers_['notas'].named_steps['imputar']
    medianas = dict(zip(imputador.feature_names_in_, imputador.statistics_))
    prob_alta = mapa_probs['alto']
    with st.container(border=True):
        st.markdown(f'**Probabilidad de éxito: {prob_alta:.1%}**')
        st.caption('Éxito entendido como alcanzar popularidad alta en Backloggd.')
    lectura, contexto = concluir_prediccion(fila.iloc[0], prediccion, mapa_probs, medianas['Metacritic Rating'])
    st.markdown(lectura)
    st.markdown(html.escape(contexto))
    st.caption('Popularidad alta significa quedar en el rango superior del índice de partidas registradas, pendientes y listas de deseos en Backloggd. Para evaluar éxito comercial hacen falta datos de ventas y costos.')
    comparaciones = comparar_probabilidad_alta(
        pipeline, fila, prob_alta, metricas['calibracion_web']['temperatura'], medianas,
    )
    if comparaciones:
        st.markdown('**Cómo cambia la probabilidad de popularidad alta**')
        st.caption('En cada escenario cambiamos un dato del formulario y dejamos los demás como están. Son estimaciones del modelo para esos escenarios.')
        for descripcion, alternativa, cambio in comparaciones:
            diferencia = f'{cambio:+.1f} puntos porcentuales' if abs(cambio) >= 0.05 else 'sin cambio al redondear'
            st.markdown(f'- {html.escape(descripcion)} → **{alternativa:.1%}** ({diferencia}).')

    section_banner(
        'Cinco juegos parecidos',
        'Son juegos del catálogo con datos parecidos a los que elegiste.',
    )

    tabla_vecinos = vecinos[
        ['id_juego', 'Title', 'anio', 'generos_texto', 'organizaciones', 'cluster_kmeans', 'distancia']
    ].copy()
    tabla_vecinos['anio'] = tabla_vecinos['anio'].fillna(0).astype(int)
    tabla_vecinos['cluster_kmeans'] = tabla_vecinos['cluster_kmeans'].map(
        lambda v: 'Sin cluster (sin crítica CSV)' if pd.isna(v) else f'Cluster {int(v)}'
    )

    pendientes = tuple(sorted({
        (r.Title, int(r.anio)) for r in tabla_vecinos.itertuples(index=False)
        if r.Title not in PORTADAS_LOCALES and r.anio
    }))
    portadas = portadas_en_cache(pendientes) if pendientes else {}
    vecinos_bars_html = ''
    for idx_v, row_v in tabla_vecinos.reset_index(drop=True).iterrows():
        act_cls = 'active' if idx_v == 0 else ''
        titulo = row_v['Title']
        archivo = PORTADAS_LOCALES.get(titulo)
        arte_local = asset_b64(f'img/juegos/{archivo}.webp') if archivo else ''
        arte_steam = portadas.get((titulo, int(row_v['anio'])))
        if arte_local or arte_steam:
            formato = 'webp' if arte_local else 'jpeg'
            clase_arte = ' sc-portada-original' if archivo in PORTADAS_ORIGINALES else ''
            imagen = (
                f'<figure class="sc-vecino-arte{clase_arte}">'
                f'<img src="data:image/{formato};base64,{arte_local or arte_steam}" alt=""/></figure>'
            )
        else:
            organizaciones = row_v['organizaciones']
            nombre = ' · '.join(organizaciones) if isinstance(organizaciones, list) and organizaciones else ''
            if nombre == 'Pionner LDC':
                nombre = 'Pioneer LDC'
            siglas = ''.join(p[0] for p in (nombre or titulo).split() if p[0].isalnum())[:3].upper()
            imagen = (
                '<div class="sc-vecino-arte sc-vecino-organizacion">'
                f'<span aria-hidden="true">{html.escape(siglas)}</span>'
                f'<small>{html.escape(nombre or "Portada no disponible")}</small></div>'
            )
        titulo_v = html.escape(_p5_ascii(row_v['Title']), quote=True)
        generos_v = html.escape(str(row_v['generos_texto']), quote=True)
        cluster_v = html.escape(str(row_v['cluster_kmeans']), quote=True)
        anio_v = 'N/D' if int(row_v['anio']) == 0 else str(int(row_v['anio']))
        vecinos_bars_html += f"""
        <div class="sc-bar-outer {act_cls}">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    {imagen}
                    <div class="sc-main">
                        <div class="sc-label">{titulo_v}</div>
                        <div class="sc-subdesc">
                            Géneros: {generos_v} · {cluster_v}
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">AÑO</span>
                                <span class="sc-stat-num">{anio_v}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">DIST.</span>
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
        column_order=['Title', 'anio', 'generos_texto', 'cluster_kmeans', 'distancia'],
        column_config={
            'Title': 'Videojuego',
            'anio': st.column_config.NumberColumn('Año', format='%d'),
            'generos_texto': 'Géneros',
            'cluster_kmeans': 'Perfil K-Means (Descriptivo)',
            'distancia': st.column_config.NumberColumn('Distancia Euclídea', format='%.3f'),
        },
    )

    render_html(
        """
        <div class="p5-legal-footer">
            La estimación se basa en la actividad registrada en Backloggd.
        </div>
        """
    )
