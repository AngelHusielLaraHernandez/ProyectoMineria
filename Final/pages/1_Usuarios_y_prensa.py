"""Comparación con casos completos y procedencia explícita."""
import streamlit as st
from src.ui import setup, resources, read_report, manual_checks

setup('Usuarios y prensa')
df, bundle, analysis = resources()
r = analysis['pearson_global']
st.write(f'En {r["n"]} pares, Pearson r = {r["r"]:.3f}; '
         f'IC del 95 %: {r["ic95_inferior"]:.3f} a {r["ic95_superior"]:.3f}.')
st.write('Pearson mide asociación lineal. No mide la distancia entre notas y no demuestra que una valoración cause la otra. '
         'Se excluyeron las notas etiquetadas como estimaciones propias.')
st.scatter_chart(df, x='critica_verificada_csv', y='Rating', color='#17645b', x_label='Prensa según CSV', y_label='Rating original')
group = st.radio('Comparar por', ['Género', 'Organización de Team'], horizontal=True)
file = 'pearson_generos.csv' if group == 'Género' else 'pearson_organizaciones.csv'
if group != 'Género':
    st.warning('Team no distingue desarrollador de editor. Estos resultados no se pueden atribuir todavía a estudios desarrolladores.')
st.caption('Cada juego participa en todos sus géneros y organizaciones. Se informa r a partir de 10 pares con variación; '
           'q_bh corrige comparaciones dentro de cada familia. Los grupos se superponen y sus tamaños no se suman.')
st.dataframe(read_report(file), hide_index=True, width='stretch')
st.download_button('Descargar correlaciones', read_report(file).to_csv(index=False), file, 'text/csv')
manual_checks()
