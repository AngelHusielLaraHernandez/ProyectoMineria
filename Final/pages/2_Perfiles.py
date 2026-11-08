"""Perfiles descriptivos de actividad e interés."""
import pandas as pd
import streamlit as st
from src.config import CLEAN
from src.ui import setup, resources, read_report, manual_checks

setup('Perfiles de popularidad')
df, bundle, analysis = resources()
method = st.radio('Método', ['kmeans', 'dbscan'], horizontal=True)
st.write('Los grupos se ajustan con las cuatro señales transformadas mediante log(1 + conteo) y estandarizadas. '
         'No usan Rating ni Metacritic. Sus números son identificadores, no categorías de éxito.')
st.caption(f'K-Means: k={analysis["kmeans_k"]}, elegido entre 2 y 8. DBSCAN: '
           f'eps={analysis["dbscan"]["eps"]}, min_samples={analysis["dbscan"]["min_samples"]:.0f}. '
           'En DBSCAN, −1 significa ruido y no un perfil de mercado.')
if method == 'dbscan' and not analysis['dbscan_criterio_valido']:
    st.warning('Ninguna configuración cumplió el criterio de selección. Se muestra la configuración de referencia, sin validarla como partición útil.')
profiles = pd.read_csv(CLEAN / 'perfiles.csv')
st.subheader('Medianas de las cuatro señales')
st.dataframe(read_report(f'perfiles_{method}.csv'), hide_index=True, width='stretch')
st.subheader('Proyección de los juegos')
st.caption(f'Las dos componentes PCA conservan {sum(analysis["pca_varianza_explicada"]):.1%} de la varianza. La proyección no define los clusters.')
profiles['perfil'] = profiles[method].astype(str)
st.scatter_chart(profiles, x='componente_1', y='componente_2', color='perfil', x_label='Componente 1', y_label='Componente 2')
profile = st.selectbox('Consultar perfil', sorted(profiles[method].unique().tolist()))
st.dataframe(profiles[profiles[method].eq(profile)].drop(columns=['perfil']), hide_index=True, width='stretch')
with st.expander('Ver selección de parámetros'):
    st.dataframe(read_report(f'seleccion_{method}.csv'), hide_index=True)
manual_checks()
