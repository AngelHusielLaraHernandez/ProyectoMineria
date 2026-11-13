"""Página 3 — Acerca del Modelo: Métricas, Comparación de Algoritmos, Matriz de Confusión e Importancia."""
import html
import importlib
import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import src.data as _data

if getattr(_data, '_MOD_VERSION', None) != 'p5-v12-portadas':
    if 'src.config' in sys.modules:
        importlib.reload(sys.modules['src.config'])
    _data = importlib.reload(_data)
    _data.asegurar_modulos_vigentes(config_recargado=True)
else:
    _data.asegurar_modulos_vigentes()

from src.visualizacion import PALETA

from vista_graficas import mostrar_grafica
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
    'Cómo salió el modelo',
    'Compara los modelos y revisa en qué niveles se equivocaron.',
    transition='default',
    menu_idx=3,
    compact_menu=True,
)

df, bundle, analysis = resources()
render_lb_rb_nav('RESULTADOS DEL MODELO')
metricas = bundle['metricas']
resumen_m = metricas['metricas']

# ---------------------------------------------------------------------------
# 1. KPIs DINÁMICOS DESDE models/metadata.json
# ---------------------------------------------------------------------------
section_banner('Ficha del modelo activo', metricas['modelo'])

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
            <div class="p5-kpi-note">CV externa 10 × 5: {resumen_m['f1_macro_cv']:.4f} (Base Dummy: {resumen_m['f1_macro_referencia']:.4f})</div>
        </div>
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">Exactitud / Bal. Acc</div>
            <div class="p5-kpi-value">{resumen_m['exactitud']:.1%} / {resumen_m['balanced_accuracy']:.1%}</div>
            <div class="p5-kpi-note">Juegos de entrenamiento: {metricas['n_entrenamiento']} · Juegos de prueba: {metricas['n_prueba']}</div>
        </div>
        <div class="p5-kpi-card">
            <div class="p5-kpi-label">Niveles de popularidad</div>
            <div class="p5-kpi-value" style="font-size:1.45rem;">Bajo, medio y alto</div>
            <div class="p5-kpi-note">Cortes terciles: {metricas['definicion_objetivo']['cortes'][0]:.3f} y {metricas['definicion_objetivo']['cortes'][1]:.3f}</div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. COMPARACIÓN DE ALGORITMOS (reports/modelo_comparacion.csv)
# ---------------------------------------------------------------------------
section_banner(
    f'Comparación de {len(metricas["evaluacion_anidada"])} modelos supervisados',
    'Naive Bayes · CART · Random Forest · Red neuronal MLP · Referencia mayoritaria',
)

tabla_comp = read_report('tables/comparacion_prueba_actual_e_historica.csv').copy()
nombres_legibles = {
    'DummyClassifier': 'DummyClassifier (Base Mayoritaria)',
    'CategoricalNB': 'Naive Bayes (CategoricalNB Discretizado)',
    'DecisionTreeClassifier': 'Árbol de Decisión (CART)',
    'RandomForestClassifier': 'Random Forest',
    'MLPClassifier': 'Red neuronal MLP',
}
nombres_cortos = {
    'DummyClassifier': 'REFERENCIA MAYORITARIA',
    'CategoricalNB': 'NAIVE BAYES',
    'DecisionTreeClassifier': 'ÁRBOL DE DECISIÓN',
    'RandomForestClassifier': 'RANDOM FOREST',
    'MLPClassifier': 'RED NEURONAL MLP',
}
tabla_comp['Algoritmo'] = tabla_comp['modelo'].map(lambda m: nombres_legibles.get(m, m))

# Menú de candidatos (configuración e historial de validación). La tabla inferior concentra métricas comparadas.
arte_algoritmos = {
    'RandomForestClassifier': 'halo',
    'MLPClassifier': 'spider-man',
    'CategoricalNB': 'god-of-war',
    'DecisionTreeClassifier': 'link',
    'DummyClassifier': 'mario',
}
sp_left_html = '<div class="sp-title">BITÁCORA DE ALGORITMOS</div>'
sp_right_html = ''
orden_sp = tabla_comp.assign(activo=tabla_comp.modelo.eq(metricas['modelo'])).sort_values(['activo', 'f1_macro_cv'], ascending=False).reset_index(drop=True)
for idx_m, row_m in orden_sp.iterrows():
    es_activo = bool(row_m['activo'])
    act_cls = 'active' if es_activo else ''
    disp_style = 'block' if es_activo else 'none'
    tag_txt = 'MODELO ACTIVO' if es_activo else 'CANDIDATO COMPARADO'
    nombre_corto = html.escape(nombres_cortos.get(row_m['modelo'], str(row_m['modelo'])), quote=True)
    algoritmo_html = html.escape(str(row_m['Algoritmo']), quote=True)
    origen_html = html.escape(str(row_m['origen_prueba']), quote=True)
    params_html = html.escape(str(row_m['mejores_parametros']), quote=True)
    arte = arte_algoritmos.get(row_m['modelo'], 'zelda')
    arte_b64 = asset_b64(f'img/juegos/{arte}.webp')
    sp_left_html += f"""
    <div class="sp-item {act_cls}" data-sp-target="alg-{idx_m}">
        <img class="sp-item-art" src="data:image/webp;base64,{arte_b64}" alt=""/>
        <div>
            <div class="sp-item-title">{nombre_corto}</div>
            <div class="sp-item-stack">F1 CV: {row_m['f1_macro_cv']:.4f} · F1 PRUEBA: {row_m['f1_macro_prueba']:.4f}</div>
        </div>
    </div>
    """
    sp_right_html += f"""
    <div class="sp-right" data-sp-id="alg-{idx_m}" style="display:{disp_style};">
        <div class="sp-tag">{tag_txt}</div>
        <div class="sp-right-title">{nombre_corto}</div>
        <div class="sp-right-summary">
            <strong>{algoritmo_html}</strong><br/>
            F1 macro en CV externa (10 × 5): {row_m['f1_macro_cv']:.4f} (±{row_m['desviacion_cv']:.4f})<br/>
            Alcance de prueba (n={metricas["n_prueba"]}): {origen_html}<br/>
            Nota: consulta todas las métricas numéricas comparadas en la tabla inferior.
        </div>
        <div class="sp-link">PARÁMETROS: {params_html}</div>
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
            'origen_prueba',
        ]
    ],
    hide_index=True,
    width='stretch',
    column_config={
        'Algoritmo': 'Algoritmo',
        'f1_macro_cv': st.column_config.NumberColumn('F1 macro CV externa', format='%.4f'),
        'desviacion_cv': st.column_config.NumberColumn('Desv. Est. CV', format='%.4f'),
        'exactitud_prueba': st.column_config.NumberColumn('Exactitud (Prueba)', format='%.4f'),
        'f1_macro_prueba': st.column_config.NumberColumn('F1 Macro (Prueba)', format='%.4f'),
        'balanced_accuracy_prueba': st.column_config.NumberColumn('Exactitud Balanceada (Prueba)', format='%.4f'),
        'origen_prueba': 'Origen de la prueba',
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
for desplazamiento, etiqueta, campo, color, simbolo in [
    (-.22, 'F1 macro CV', 'f1_macro_cv', PALETA['primary'], 'circle'),
    (0, 'F1 macro prueba', 'f1_macro_prueba', PALETA['secondary'], 'diamond'),
    (.22, 'Exactitud prueba', 'exactitud_prueba', PALETA['accent'], 'square'),
]:
    es_cv = campo == 'f1_macro_cv'
    fig_comp.add_trace(go.Scatter(
        name=etiqueta,
        mode='markers',
        y=filas_modelos + desplazamiento,
        x=tabla_comp[campo],
        error_x=dict(array=tabla_comp['desviacion_cv'], color=color, thickness=2, width=5) if es_cv else None,
        text=tabla_comp['Algoritmo'],
        customdata=tabla_comp['desviacion_cv'] if es_cv else tabla_comp['origen_prueba'],
        marker=dict(color=color, symbol=simbolo, size=10, line=dict(color=PALETA['text-primary'], width=1)),
        hovertemplate='<b>%{text}</b><br>' + etiqueta + ': %{x:.3f}'
        + (' · DE %{customdata:.3f}' if es_cv else '<br>%{customdata}') + '<extra></extra>',
    ))
fig_comp.update_xaxes(title_text='Puntaje (0–1)', range=[0, 1])
fig_comp.update_yaxes(
    tickmode='array', tickvals=filas_modelos,
    ticktext=[etiquetas_modelos.get(modelo, modelo) for modelo in tabla_comp['modelo']],
    range=[len(filas_modelos) - .5, -.5], fixedrange=True, ticklabelstandoff=8, title_text='Modelo',
)
mostrar_grafica(fig_comp, 'Desempeño en validación cruzada y prueba', alto=465)
st.caption('Cada punto muestra un resultado. El tramo azul indica cuánto cambió el F1 macro entre las pruebas.')

cv = read_report('tables/comparativo_modelos.csv').set_index('modelo')
contrastes = read_report('tables/comparacion_estadistica.csv')
rf, mlp = cv.loc['RandomForestClassifier'], cv.loc['MLPClassifier']
rf_mlp = contrastes.loc[contrastes.modelo_a.eq('RandomForestClassifier') & contrastes.modelo_b.eq('MLPClassifier')]
p_t = rf_mlp.loc[rf_mlp.prueba.str.startswith('t corregida'), 'p_valor'].iloc[0]
st.caption(f'El F1 macro varió menos entre pruebas para Random Forest ({rf.f1_macro_de:.4f}) que la MLP ({mlp.f1_macro_de:.4f}). '
           f'La t corregida para su diferencia da p={p_t:.4f}. La prueba de los demás candidatos es histórica.')
with st.expander('Métricas de validación externa y contrastes'):
    st.dataframe(cv.reset_index(), hide_index=True, width='stretch')
    st.dataframe(contrastes, hide_index=True, width='stretch')

# ---------------------------------------------------------------------------
# 3. MATRIZ DE CONFUSIÓN Y VARIABLES MÁS INFLUYENTES (ANCHO COMPLETO)
# ---------------------------------------------------------------------------
# El ancho completo mantiene legibles títulos, intervalos y etiquetas.
col_cm, col_pi = st.container(), st.container()

with col_cm:
    section_banner('Matriz de confusión', f'Prueba con {metricas["n_prueba"]} juegos')
    clases = metricas['clases']  # ['bajo', 'medio', 'alto']
    matriz = np.asarray(resumen_m['matriz_confusion'], dtype=int)

    fig_cm = go.Figure(
        data=go.Heatmap(
            z=matriz,
            x=[c.capitalize() for c in clases],
            y=[c.capitalize() for c in clases],
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
            fig_cm.add_annotation(
                x=clase_predicha.capitalize(),
                y=clase_real.capitalize(),
                text=str(valor),
                showarrow=False,
                font=dict(size=18, color=PALETA['bg-primary'] if valor >= .45 * matriz.max() else PALETA['text-primary']),
            )
    fig_cm.update_xaxes(title_text='Clase predicha')
    fig_cm.update_yaxes(title_text='Clase real', autorange='reversed')
    mostrar_grafica(fig_cm, 'Clases reales frente a predicciones', alto=390)
    st.caption('En la diagonal se ven los aciertos. Si sigues una fila, puedes ver en qué otros niveles quedaron los juegos.')

with col_pi:
    section_banner('Importancia de variables en Random Forest', 'Reducción de impureza de Gini')
    df_gini = read_report('tables/modelo_importancia_gini.csv').sort_values('importancia')
    etiquetas = {'Rating': 'Usuarios', 'Metacritic Rating': 'Metacritic',
                 'generos': 'Géneros', 'estudio': 'Organización', 'decada': 'Década'}
    figura_gini = go.Figure(go.Bar(
        x=df_gini['importancia'] * 100, y=df_gini['variable'].map(etiquetas),
        orientation='h', marker_color=PALETA['primary'],
        hovertemplate='%{y}: %{x:.2f} %<extra></extra>',
    ))
    figura_gini.update_xaxes(title_text='Importancia relativa (%)', rangemode='tozero')
    figura_gini.update_yaxes(ticklabelstandoff=8, title_text='Entrada del modelo')
    mostrar_grafica(figura_gini, 'Contribución a la reducción de impureza', alto=360)
    st.caption(
        'Una barra más larga indica que el bosque usó más ese dato para separar los niveles.'
    )

# ---------------------------------------------------------------------------
# 4. REPORTE DETALLADO POR CLASE Y AUDITORÍA DE IMPUTACIÓN
# ---------------------------------------------------------------------------
section_banner('Resultados por nivel', 'Bajo, medio y alto')

col_d1, col_d2 = st.columns(2)
with col_d1:
    st.markdown('**Precisión, Recall y F1-Score por Tercil en Prueba:**')
    filas_clases = []
    for c in metricas['clases']:
        info_c = resumen_m['reporte_clases'][c]
        filas_clases.append(
            {
                'Clase': c.capitalize(),
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
            'Clase': 'Clase',
            'Soporte (n)': st.column_config.NumberColumn('Soporte (n)', format='%d'),
            'Precisión': st.column_config.NumberColumn(format='%.3f'),
            'Recall (Sensibilidad)': st.column_config.NumberColumn(format='%.3f'),
            'F1-Score': st.column_config.NumberColumn(format='%.3f'),
        },
    )

with col_d2:
    st.markdown(f'**Recall por clase para {len(tabla_comp)} modelos**')
    st.caption('Prueba actual del bosque y resultados históricos para los demás candidatos.')
    err_df = read_report('tables/modelo_error_por_clase.csv').copy()
    err_df['clase'] = err_df['clase'].astype(str).str.capitalize()
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

section_banner('Calibración de probabilidades', 'Compara los porcentajes del bosque con lo que pasó en la prueba')
calibracion = metricas['calibracion_web']
ajustada = calibracion['metricas_prueba']
st.markdown(
    f'El ajuste se aprendió con predicciones fuera de pliegue de **{calibracion["n_ajuste"]} juegos** '
    f'de entrenamiento. La comparación usa los mismos **{calibracion["n_prueba"]} juegos** de prueba.'
)
nivel = st.radio('Nivel de popularidad', ['alto', 'medio', 'bajo'], format_func=str.capitalize, horizontal=True)
curva = go.Figure()
curva.add_scatter(x=[0, 1], y=[0, 1], mode='lines', name='Referencia ideal',
                  line=dict(color=PALETA['text-primary'], dash='dot'))
for archivo, serie, color, simbolo in [
    ('calibracion.csv', 'Sin calibrar', PALETA['secondary'], 'diamond'),
    ('calibracion_ajustada.csv', 'Calibrada', PALETA['primary'], 'circle'),
]:
    fiabilidad = read_report(f'tables/{archivo}')
    filas = fiabilidad.loc[fiabilidad.clase.eq(nivel)]
    curva.add_scatter(
        x=filas.probabilidad_media,
        y=filas.fraccion_observada,
        customdata=filas.n,
        mode='lines+markers',
        name=serie,
        line=dict(color=color),
        marker=dict(symbol=simbolo, size=7),
        hovertemplate='Probabilidad media %{x:.1%}<br>Fracción observada %{y:.1%}<br>Juegos %{customdata}<extra></extra>',
    )
curva.update_xaxes(title_text='Probabilidad estimada media (%)', tickformat='.0%', range=[0, 1])
curva.update_yaxes(title_text='Fracción observada de la clase (%)', tickformat='.0%', range=[0, 1])
mostrar_grafica(curva, f'Fiabilidad del nivel {nivel}', alto=400)
st.caption('Cada punto agrupa juegos con probabilidades parecidas. Cuanto más cerca esté de la diagonal, '
           'más se parece la probabilidad estimada a la frecuencia observada en ese grupo.')
st.markdown(
    '| Métrica en prueba | Sin calibrar | Calibrada |\n'
    '| --- | ---: | ---: |\n'
    f'| Brier multiclase | {resumen_m["brier_multiclase"]:.4f} | {ajustada["brier_multiclase"]:.4f} |\n'
    f'| Log-loss | {resumen_m["log_loss"]:.4f} | {ajustada["log_loss"]:.4f} |'
)
st.caption('En ambas métricas, un valor más bajo indica mejores probabilidades en esta prueba.')
