"""Página 3 — Acerca del Modelo: Métricas, Comparación de Algoritmos, Matriz de Confusión e Importancia."""
import html
import importlib
import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import src.data as _data

if getattr(_data, '_MOD_VERSION', None) != 'p5-v14-menu':
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
    menu_idx=2,
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
    'DummyClassifier': 'Referencia mayoritaria',
    'CategoricalNB': 'Naive Bayes',
    'DecisionTreeClassifier': 'Árbol de decisión',
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

explicaciones = {
    'RandomForestClassifier': 'Combina las predicciones de muchos árboles para elegir un nivel de popularidad.',
    'MLPClassifier': 'Aprende combinaciones entre los datos del juego para estimar su nivel de popularidad.',
    'CategoricalNB': 'Agrupa las notas en rangos y estima qué nivel es más probable según los géneros, la organización y los demás datos del juego.',
    'DecisionTreeClassifier': 'Sigue una serie de preguntas sobre el juego hasta asignarle un nivel.',
    'DummyClassifier': 'Siempre elige el nivel más frecuente del entrenamiento. Sirve como punto de partida para comparar los demás modelos.',
}
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
    origen_html = html.escape(str(row_m['origen_prueba']), quote=True)
    params_html = html.escape(str(row_m['mejores_parametros']), quote=True)
    explicacion = explicaciones.get(row_m['modelo'], 'Clasifica los juegos en niveles de popularidad.')
    total_prueba = metricas['n_prueba']
    exactitud = row_m['exactitud_prueba']
    aciertos = round(exactitud * total_prueba)
    arte = arte_algoritmos.get(row_m['modelo'], 'zelda')
    arte_b64 = asset_b64(f'img/juegos/{arte}.webp')
    sp_left_html += f"""
    <div class="sp-item {act_cls}" data-sp-target="alg-{idx_m}">
        <img class="sp-item-art" src="data:image/webp;base64,{arte_b64}" alt=""/>
        <div>
            <div class="sp-item-title">{nombre_corto}</div>
            <div class="sp-item-stack">{exactitud:.1%} de exactitud en prueba</div>
        </div>
    </div>
    """
    sp_right_html += f"""
    <div class="sp-right" data-sp-id="alg-{idx_m}" style="display:{disp_style};">
        <div class="sp-tag">{tag_txt}</div>
        <div class="sp-right-title">{nombre_corto}</div>
        <div class="sp-right-summary">
            <p>{explicacion}</p>
            <p><strong>{exactitud:.1%} de exactitud en prueba.</strong> Acertó el nivel de {aciertos} de {total_prueba} juegos.</p>
            <p><strong>F1 macro en prueba {row_m['f1_macro_prueba']:.3f}.</strong> Da el mismo peso a los niveles bajo, medio y alto.</p>
        </div>
        <details class="sp-link">
            <summary>Detalles técnicos</summary>
            <div>F1 macro en validación cruzada (10 × 5) de {row_m['f1_macro_cv']:.4f} (±{row_m['desviacion_cv']:.4f}).</div>
            <div>Origen de la prueba: {origen_html}</div>
            <div>Parámetros: {params_html}</div>
        </details>
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
        'exactitud_prueba': st.column_config.NumberColumn('Exactitud en prueba', format='percent'),
        'f1_macro_prueba': st.column_config.NumberColumn('F1 Macro (Prueba)', format='%.4f'),
        'balanced_accuracy_prueba': st.column_config.NumberColumn('Exactitud Balanceada (Prueba)', format='%.4f'),
        'origen_prueba': 'Origen de la prueba',
    },
)
mejor_exactitud = tabla_comp.loc[tabla_comp['exactitud_prueba'].idxmax()]
referencia = tabla_comp.loc[tabla_comp['modelo'].eq('DummyClassifier')].iloc[0]
st.caption(
    f"{mejor_exactitud['Algoritmo']} tiene la mayor exactitud de las pruebas mostradas "
    f"({mejor_exactitud['exactitud_prueba']:.1%}, frente al {referencia['exactitud_prueba']:.1%} de la referencia). "
    "La tabla reúne la prueba actual del bosque y las pruebas históricas de los demás modelos."
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
lider_cv = tabla_comp.loc[tabla_comp['f1_macro_cv'].idxmax()]
lider_prueba = tabla_comp.loc[tabla_comp['f1_macro_prueba'].idxmax()]
st.caption(
    f"En validación cruzada, {lider_cv['Algoritmo']} logró el mayor F1 macro "
    f"({lider_cv['f1_macro_cv']:.3f}). De los resultados de prueba mostrados, el mayor fue el de "
    f"{lider_prueba['Algoritmo']} ({lider_prueba['f1_macro_prueba']:.3f})."
)

cv = read_report('tables/comparativo_modelos.csv').set_index('modelo')
contrastes = read_report('tables/comparacion_estadistica.csv')
rf, mlp = cv.loc['RandomForestClassifier'], cv.loc['MLPClassifier']
rf_mlp = contrastes.loc[contrastes.modelo_a.eq('RandomForestClassifier') & contrastes.modelo_b.eq('MLPClassifier')]
p_t = rf_mlp.loc[rf_mlp.prueba.str.startswith('t corregida'), 'p_valor'].iloc[0]
with st.expander('Métricas de validación externa y contrastes'):
    st.dataframe(cv.reset_index(), hide_index=True, width='stretch')
    st.caption(
        f"El bosque y la red neuronal promediaron una exactitud parecida en validación "
        f"({rf.exactitud_pct_media:.1f}% y {mlp.exactitud_pct_media:.1f}%). "
        f"El F1 macro varió menos en el bosque ({rf.f1_macro_de:.3f} frente a {mlp.f1_macro_de:.3f})."
    )
    st.dataframe(contrastes, hide_index=True, width='stretch')
    st.caption(
        f"La prueba t corregida dio un valor p de {p_t:.3f} para el bosque y la red neuronal. "
        "Con estos datos, la prueba no muestra una diferencia clara en F1 macro entre ambos."
    )

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
    errores = matriz.copy()
    np.fill_diagonal(errores, 0)
    fila_error, columna_error = np.unravel_index(errores.argmax(), errores.shape)
    if errores[fila_error, columna_error]:
        st.caption(
            f"El modelo acertó el nivel de {matriz.trace()} de {matriz.sum()} juegos. El error más común "
            f"fue clasificar {errores[fila_error, columna_error]} juegos de nivel "
            f"{clases[fila_error]} como {clases[columna_error]}."
        )
    else:
        st.caption(f"El modelo acertó el nivel de los {matriz.sum()} juegos de prueba.")

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
    mayor_gini = df_gini.iloc[-1]
    st.caption(
        f"La entrada «{etiquetas[mayor_gini['variable']]}» aportó más a la separación de los niveles "
        f"al construir el bosque ({mayor_gini['importancia']:.1%} de la importancia según Gini)."
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
    menor_recall = min(filas_clases, key=lambda fila: fila['Recall (Sensibilidad)'])
    mayor_recall = max(filas_clases, key=lambda fila: fila['Recall (Sensibilidad)'])
    st.caption(
        f"El modelo reconoció el {mayor_recall['Recall (Sensibilidad)']:.1%} de los juegos de nivel "
        f"{mayor_recall['Clase'].lower()} y el {menor_recall['Recall (Sensibilidad)']:.1%} de los de nivel "
        f"{menor_recall['Clase'].lower()}. Ahí están su mejor y su peor resultado por nivel."
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
    nivel_dificil = menor_recall['Clase']
    filas_nivel = err_df.loc[err_df['clase'].eq(nivel_dificil)]
    mejor_nivel = filas_nivel.loc[filas_nivel['recall'].idxmax()]
    nombre_nivel = nombres_legibles.get(mejor_nivel['modelo'], mejor_nivel['modelo'])
    st.caption(
        f"De los resultados mostrados para el nivel {nivel_dificil.lower()}, {nombre_nivel} reconoció "
        f"la mayor proporción de juegos ({mejor_nivel['aciertos']} de {mejor_nivel['n']})."
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
    if archivo == 'calibracion_ajustada.csv':
        grupo_mayor = filas.loc[filas['n'].idxmax()]
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
st.caption(
    f"En el grupo más numeroso tras calibrar ({int(grupo_mayor['n'])} juegos), el bosque estimó "
    f"en promedio un {grupo_mayor['probabilidad_media']:.1%} para el nivel {nivel}. "
    f"El {grupo_mayor['fraccion_observada']:.1%} de ese grupo quedó realmente en ese nivel."
)
st.markdown(
    '| Métrica en prueba | Sin calibrar | Calibrada |\n'
    '| --- | ---: | ---: |\n'
    f'| Brier multiclase | {resumen_m["brier_multiclase"]:.4f} | {ajustada["brier_multiclase"]:.4f} |\n'
    f'| Log-loss | {resumen_m["log_loss"]:.4f} | {ajustada["log_loss"]:.4f} |'
)
mejoras_calibracion = sum(ajustada[campo] < resumen_m[campo] for campo in ('brier_multiclase', 'log_loss'))
if mejoras_calibracion == 2:
    st.caption("Con la calibración bajaron los dos errores. En esta prueba, las probabilidades ajustadas se acercaron más a los resultados reales.")
elif mejoras_calibracion == 1:
    st.caption("Con la calibración bajó uno de los dos errores. La mejora en esta prueba dependió de la medida.")
else:
    st.caption("En esta prueba, los dos errores fueron menores o iguales con las probabilidades originales.")
