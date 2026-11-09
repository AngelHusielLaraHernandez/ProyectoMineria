"""Página 3 — Acerca del Modelo: Métricas, Comparación de Algoritmos, Matriz de Confusión e Importancia."""
import importlib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v7-delegated':
    importlib.reload(_ui)

from src.ui import (
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
    'Acerca del Modelo Supervisado',
    'Evaluación Fase 4B · StratifiedGroupKFold (10 Pliegues) · Matriz de Confusión · Permutation Importance',
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
    'Naive Bayes (CategoricalNB) vs. Árbol de Decisión vs. Random Forest vs. Referencia Dummy',
)

tabla_comp = read_report('modelo_comparacion.csv').copy()
nombres_legibles = {
    'DummyClassifier': 'DummyClassifier (Base Mayoritaria)',
    'CategoricalNB': 'Naive Bayes (CategoricalNB Discretizado)',
    'DecisionTreeClassifier': 'Árbol de Decisión (CART)',
    'RandomForestClassifier': 'Random Forest (Ensamble Ganador)',
}
nombres_cortos = {'DummyClassifier': 'REFERENCIA MAYORITARIA', 'CategoricalNB': 'NAIVE BAYES',
                 'DecisionTreeClassifier': 'ARBOL DE DECISION', 'RandomForestClassifier': 'RANDOM FOREST'}
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
fig_comp.add_trace(
    go.Bar(
        name='F1 Macro Validación Cruzada (10-fold)',
        x=tabla_comp['Algoritmo'],
        y=tabla_comp['f1_macro_cv'],
        error_y=dict(type='data', array=tabla_comp['desviacion_cv'], color='#ffe600'),
        marker_color='#d92323',
        marker_line_color='#ffffff',
        marker_line_width=1.5,
        text=tabla_comp['f1_macro_cv'].map(lambda v: f'{v:.3f}'),
        textposition='outside',
    )
)
fig_comp.add_trace(
    go.Bar(
        name='F1 Macro Conjunto de Prueba (Holdout)',
        x=tabla_comp['Algoritmo'],
        y=tabla_comp['f1_macro_prueba'],
        marker_color='#ffffff',
        marker_line_color='#000000',
        marker_line_width=1.5,
        text=tabla_comp['f1_macro_prueba'].map(lambda v: f'{v:.3f}'),
        textposition='outside',
    )
)
fig_comp.add_trace(
    go.Bar(
        name='Exactitud en Prueba (Accuracy)',
        x=tabla_comp['Algoritmo'],
        y=tabla_comp['exactitud_prueba'],
        marker_color='#7b7b7b',
        marker_line_color='#000000',
        marker_line_width=1.5,
        text=tabla_comp['exactitud_prueba'].map(lambda v: f'{v:.3f}'),
        textposition='outside',
    )
)
fig_comp.update_layout(barmode='group', yaxis_range=[0, 0.72])
fig_comp.update_xaxes(title_text='Familia Algorítmica')
fig_comp.update_yaxes(title_text='Puntaje (0.0 – 1.0)')
p5_plotly_layout(fig_comp, title='Desempeño Comparativo: Validación Cruzada vs. Prueba', height=430)
st.plotly_chart(fig_comp, use_container_width=True)

st.caption(
    'Nota sobre arquitecturas neuronales (MLP) y Weka: Con n = 892 registros de entrenamiento y representación '
    'dispersa multi-hot, los ensambles de árboles (`RandomForestClassifier`) y el modelo probabilístico '
    'discretizado (`CategoricalNB`) ofrecen mejor estabilidad y menor varianza que perceptrones multicapa (MLP) '
    'sobre datos tabulares pequeños. Los archivos `.arff` y `.csv` de partición idéntica están disponibles en '
    '`data/clean/entrenamiento_weka.arff` y `data/clean/prueba_weka.arff` para contraste externo.'
)

# ---------------------------------------------------------------------------
# 3. MATRIZ DE CONFUSIÓN Y VARIABLES MÁS INFLUYENTES (LADO A LADO)
# ---------------------------------------------------------------------------
col_cm, col_pi = st.columns(2)

with col_cm:
    section_banner('Matriz de Confusión (Holdout n = 222)', 'Mapa de Calor en Tonos Oscuros y Carmesí')
    clases = metricas['clases']  # ['bajo', 'medio', 'alto']
    etiquetas_clases = [f'Real/Pred: {c.upper()}' for c in clases]
    matriz = np.asarray(resumen_m['matriz_confusion'], dtype=int)

    texto_celdas = [[f'{val}' for val in fila] for fila in matriz]
    fig_cm = go.Figure(
        data=go.Heatmap(
            z=matriz,
            x=[c.upper() for c in clases],
            y=[c.upper() for c in clases],
            text=texto_celdas,
            texttemplate='<b>%{text}</b>',
            textfont=dict(size=18, color='#ffffff', family='Bebas Neue, sans-serif'),
            colorscale=[
                [0.0, '#0d0d0d'],
                [0.35, '#3a0a0a'],
                [0.7, '#732424'],
                [1.0, '#d92323'],
            ],
            showscale=True,
            hovertemplate='Clase Real: <b>%{y}</b><br>Clase Predicha: <b>%{x}</b><br>Juegos: <b>%{z}</b><extra></extra>',
        )
    )
    fig_cm.update_xaxes(title_text='Nivel Predicho por el Modelo')
    fig_cm.update_yaxes(title_text='Nivel Real en Prueba', autorange='reversed')
    p5_plotly_layout(fig_cm, title='Matriz de Confusión (RandomForestClassifier)', height=420)
    st.plotly_chart(fig_cm, use_container_width=True)

with col_pi:
    section_banner('Variables Más Influyentes', 'Permutation Importance sobre Variables Crudas')
    df_perm = read_report('modelo_permutation_importance.csv').sort_values(
        'caida_f1_macro_media', ascending=True
    )
    etiquetas_vars = {
        'Rating': 'Rating de Usuarios (0–5)',
        'Metacritic Rating': 'Metacritic Rating (0–100)',
        'generos': 'Géneros (Multi-hot)',
        'estudio': 'Estudio / Organización (Team)',
        'decada': 'Década de Lanzamiento',
    }
    df_perm['Variable'] = df_perm['variable_cruda'].map(lambda v: etiquetas_vars.get(v, v))

    fig_perm = go.Figure(
        go.Bar(
            x=df_perm['caida_f1_macro_media'],
            y=df_perm['Variable'],
            orientation='h',
            error_x=dict(type='data', array=df_perm['desviacion'], color='#ffe600'),
            marker=dict(
                color=['#732424', '#7b7b7b', '#d92323', '#d92323', '#ffe600'][-len(df_perm) :],
                line=dict(color='#ffffff', width=1.5),
            ),
            text=df_perm['caida_f1_macro_media'].map(lambda v: f'−{v:.4f} F1'),
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Caída media en F1 macro: %{x:.4f}<extra></extra>',
        )
    )
    fig_perm.update_xaxes(title_text='Caída Media en F1 Macro al Permutar (30 repeticiones)', range=[0, 0.115])
    fig_perm.update_yaxes(title_text='Atributo de Entrada')
    p5_plotly_layout(fig_perm, title='Importancia por Permutación en Prueba', height=420)
    st.plotly_chart(fig_perm, use_container_width=True)

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

