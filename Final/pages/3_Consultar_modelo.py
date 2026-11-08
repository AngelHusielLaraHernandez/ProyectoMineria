"""Estimación descriptiva con los mismos atributos utilizados al entrenar."""
import numpy as np
import pandas as pd
import streamlit as st
from src.config import FEATURES
from src.ui import setup, resources, manual_checks

setup('Estimar nivel de popularidad')
df, bundle, analysis = resources()
model = bundle['pipeline']
metrics = bundle['metricas']
st.write('Estima un nivel relativo a esta muestra: bajo, medio o alto. '
         'Las notas ya publicadas hacen que sea una estimación contemporánea, no una predicción anterior al lanzamiento.')
st.caption(f'Modelo: {metrics["modelo"]}. Prueba reservada: {metrics["n_prueba"]} juegos; '
           f'F1 macro: {metrics["f1_macro"]:.3f}; base mayoritaria: {metrics["f1_macro_base"]:.3f}.')
genre_encoder = model.named_steps['preparar'].named_transformers_['generos'].encoder_
org_encoder = model.named_steps['preparar'].named_transformers_['organizaciones'].encoder_
with st.form('consulta'):
    genres = st.multiselect('Géneros', genre_encoder.classes_.tolist())
    orgs = st.multiselect('Organizaciones (función sin verificar)', org_encoder.classes_.tolist())
    decade = st.selectbox('Década de lanzamiento', sorted(df['decada'].dropna().astype(int).unique().tolist()))
    a, b = st.columns(2)
    rating_missing = a.checkbox('Sin Rating de usuarios')
    rating = a.number_input('Rating de usuarios · escala original', min_value=float(df['Rating'].min()),
                            max_value=float(df['Rating'].max()), value=float(df['Rating'].median()), step=.1,
                            disabled=rating_missing)
    critic_missing = b.checkbox('Sin nota de prensa comprobable', value=True)
    critic = b.number_input('Metacritic Rating', min_value=0., max_value=100., value=80., step=1., disabled=critic_missing)
    submitted = st.form_submit_button('Estimar popularidad', type='primary')
if submitted:
    row = pd.DataFrame([{'generos': genres, 'organizaciones': orgs, 'decada': decade,
                         'Rating': np.nan if rating_missing else rating,
                         'critica_verificada_csv': np.nan if critic_missing else critic}], columns=FEATURES)
    label = model.predict(row)[0]
    st.subheader(f'Nivel estimado: {label}')
    st.write('Es una categoría del índice de actividad e interés; no representa ventas ni una garantía de éxito.')
    probabilities = model.predict_proba(row)[0]
    st.dataframe(pd.DataFrame({'Nivel': model.classes_, 'Probabilidad sin calibrar': probabilities}), hide_index=True)
    st.caption('Las probabilidades no son porcentajes de éxito comercial ni intervalos de confianza. '
               'Los géneros u organizaciones ausentes en entrenamiento se representan sin indicadores activos.')
with st.expander('Evaluación y límites'):
    st.json(metrics)
manual_checks()
