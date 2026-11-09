"""Fase 2: inspección reproducible y seis figuras EDA. No altera las fuentes."""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(RAIZ / '.cache/matplotlib'))
os.environ.setdefault('XDG_CACHE_HOME', str(RAIZ / '.cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ejecutar(raiz=RAIZ):
    raiz = Path(raiz)
    fuente = raiz / 'data/raw/games_curated.csv'
    raw = pd.read_csv(fuente)
    limpieza = importlib.import_module('.02_limpieza', __package__) if __package__ else importlib.import_module('02_limpieza')
    historia, pendientes = limpieza.auditar_historia(raiz)
    d, _, _, _ = limpieza.limpiar(raw, pendientes)
    informes = raiz / 'reports'
    figuras = informes / 'figures'
    figuras.mkdir(parents=True, exist_ok=True)
    generos = raw.Genres.map(limpieza.interpretar_generos).explode().dropna().value_counts()
    estado = {'archivo_original': 'Proyecto/data/processed/games_curated.csv',
              'copia_inmutable': 'data/raw/games_curated.csv', 'filas': len(raw), 'columnas': len(raw.columns),
              'sha256': hashlib.sha256(fuente.read_bytes()).hexdigest(),
              'esquema': {c: {'tipo': str(raw[c].dtype), 'faltantes': int(raw[c].isna().sum())} for c in raw},
              'rangos_observados': {c: {'min': float(raw[c].min()), 'max': float(raw[c].max())} for c in ['Rating', 'Metacritic Rating']},
              'procedencia_critica': raw.Origen_calificacion.value_counts().to_dict(),
              'filas_limpias': len(d), 'duplicados_descartados': 0,
              'historia': historia, 'rango_anios': [int(d.anio.min()), int(d.anio.max())],
              'pares_critica_real': int(d[['Rating', 'Metacritic Rating']].dropna().shape[0]),
              'conflictos_historicos_pendientes': len(pendientes),
              'registros_titulo_compartido': int(d.titulo_compartido.sum()),
              'titulos_compartidos': int(d.loc[d.titulo_compartido, 'grupo_titulo'].nunique()),
              'organizaciones_sin_roles': True}
    (informes / 'inspeccion.json').write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding='utf-8')
    for c, nombre, titulo in [('Rating', 'eda_rating', 'Rating de usuarios · escala de cinco estrellas'),
                              ('Metacritic Rating', 'eda_metacritic', 'Nota de prensa utilizable · escala 0–100'),
                              ('Plays', 'eda_plays_log', 'Plays · transformación log1p')]:
        fig, ax = plt.subplots(figsize=(7, 4), layout='constrained')
        valores = np.log1p(d[c]) if c == 'Plays' else d[c].dropna()
        ax.hist(valores, bins=25, color='#17645b')
        ax.set(title=titulo, xlabel='log(1 + Plays)' if c == 'Plays' else c, ylabel='Juegos')
        fig.savefig(figuras / f'{nombre}.png', dpi=150)
        plt.close(fig)
    for serie, nombre, titulo in [(d.decada.value_counts().sort_index(), 'eda_decadas', 'Juegos por década'),
                                  (generos.head(15).sort_values(), 'eda_generos_top15', 'Quince géneros más frecuentes · pertenencias múltiples')]:
        fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
        if nombre == 'eda_decadas':
            ax.bar(serie.index.astype(str), serie, color='#17645b')
            ax.set(xlabel='Década', ylabel='Juegos')
        else:
            ax.barh(serie.index, serie, color='#17645b')
            ax.set(xlabel='Juegos con el género')
        ax.set_title(titulo)
        fig.savefig(figuras / f'{nombre}.png', dpi=150)
        plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4), layout='constrained')
    ax.scatter(d['Metacritic Rating'], d.Rating, alpha=.3, s=15, color='#17645b')
    ax.set(xlabel='Prensa · 0–100', ylabel='Rating · cinco estrellas', title='Usuarios frente a prensa · pares disponibles')
    fig.savefig(figuras / 'eda_rating_vs_metacritic.png', dpi=150)
    plt.close(fig)
    nombres = ['rating', 'metacritic', 'plays_log', 'decadas', 'generos_top15', 'rating_vs_metacritic']
    texto = f'''# Inspección reproducible del maestro

Generado por src/01_inspeccion.py. Fuente: data/raw/games_curated.csv; {len(raw)} filas y {len(raw.columns)} columnas. SHA-256: {estado['sha256']}.
El maestro es el original designado, ya curado. El antecedente de 1,512 filas se conserva separado en data/historical y se audita en trazabilidad_historica.md; no se reemplaza el maestro.

Rating observado: {raw.Rating.min()}–{raw.Rating.max()}, {int(raw.Rating.isna().sum())} ausencias. Metacritic original: {raw['Metacritic Rating'].min()}–{raw['Metacritic Rating'].max()}; crítica utilizable: {int(d['Metacritic Rating'].notna().sum())}; estimaciones excluidas: {int(d.metacritic_estimado.sum())}.

Los seis conteos ya son numéricos en el maestro: esta fase no afirma haber convertido textos K/M. Su formato y la cuenta real de conversiones quedan en limpieza_log.md. El esquema completo está en inspeccion.json.

Hay {estado['registros_titulo_compartido']} registros de {estado['titulos_compartidos']} títulos compartidos en fechas distintas. No se presume que sean el mismo juego: relaciones por id_juego, nunca por Title. Los {len(pendientes)} casos numéricos heredados sin resolver se mantienen señalados y no participan del análisis principal.

## Seis figuras del EDA

'''
    texto += '\n\n'.join(f'![{n}](figures/eda_{n}.png)' for n in nombres)
    texto += '\n\nLas distribuciones describen el maestro completo disponible; la inferencia y el clustering aplican además la elegibilidad histórica. Los géneros se cuentan como pertenencias múltiples; faltan tres fechas, sin inventar década. Team no acredita roles de desarrollo.\n\n'
    escalas = raiz / 'reports/escalas.md'
    texto += escalas.read_text(encoding='utf-8') if escalas.exists() else 'Consultar documentación de escala antes de interpretar brechas.\n'
    texto += '\n## Que debo verificar manualmente\n\n- Procedencia de notas, escala histórica y decisiones de deduplicación.\n- Roles de Team, fechas TBD y títulos iguales en versiones distintas.\n'
    (informes / 'inspeccion.md').write_text(texto, encoding='utf-8')
    return estado


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raiz', type=Path, default=RAIZ)
    ejecutar(parser.parse_args().raiz)
