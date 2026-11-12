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

