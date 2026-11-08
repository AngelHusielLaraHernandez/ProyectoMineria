"""Entrada: streamlit run app.py, desde Final o usando Final/app.py desde la raíz."""
import streamlit as st

from src.config import SIGNALS
from src.ui import setup, resources, manual_checks

setup('Observatorio de videojuegos')
st.write('Explora cómo conviven la valoración, la actividad y el interés. '
         'Usa el menú lateral para contrastar usuarios y prensa, revisar perfiles o consultar el modelo.')
try:
    df, bundle, analysis = resources()
except (ValueError, FileNotFoundError, ImportError) as error:
    st.error(f'No fue posible preparar los datos: {error}. Revisa el CSV y ejecuta python -m src.pipeline desde Final.')
    st.stop()
st.subheader('Explorar la muestra')
a, b = st.columns([2, 1])
query = a.text_input('Buscar título', placeholder='Escribe parte del nombre')
genres = sorted({g for row in df['generos'] for g in row})
genre = b.selectbox('Género', ['Todos', *genres])
view = df[df['Title'].str.contains(query, case=False, regex=False, na=False)]
if genre != 'Todos':
    view = view[view['generos'].map(lambda row: genre in row)]
labels = {'popularidad_indice': 'Índice de popularidad', 'critica_verificada_csv': 'Prensa según CSV',
          'Rating': 'Valoración de usuarios', 'Plays': 'Plays · alcance acumulado',
          'Playing': 'Playing · actividad', 'Backlogs': 'Backlogs · pendientes', 'Wishlist': 'Wishlist · deseos'}
order = st.selectbox('Ordenar por', ['popularidad_indice', *SIGNALS, 'Rating', 'critica_verificada_csv'], format_func=labels.get)
st.caption(f'{len(view):,} juegos visibles de {len(df):,} registros únicos por título y fecha. Conteos de una captura; no son ventas.')
shown = view.sort_values(order, ascending=False)[['Title', 'anio', 'Rating', 'critica_verificada_csv', *SIGNALS, 'popularidad_indice']]
if len(shown):
    st.dataframe(shown, hide_index=True, width='stretch', column_config={
        'Title': 'Videojuego', 'anio': st.column_config.NumberColumn('Año', format='%d'),
        'critica_verificada_csv': 'Prensa según CSV',
        'popularidad_indice': st.column_config.NumberColumn('Índice de popularidad', format='%.3f')})
    st.download_button('Descargar esta consulta', shown.to_csv(index=False).encode('utf-8'), 'consulta.csv', 'text/csv')
else:
    st.info('No hay coincidencias. Cambia el título o selecciona Todos en género.')
with st.expander('Cómo se define la popularidad'):
    st.latex(r'I=\frac{1}{4}\sum_{j=1}^{4}\log(1+x_j)')
    st.write('Cada señal pesa lo mismo en escala logarítmica. Plays describe alcance acumulado; Playing, '
             'actividad declarada; Backlogs y Wishlist, intención. No son usuarios únicos sumables ni una medida de rentabilidad.')
manual_checks()
