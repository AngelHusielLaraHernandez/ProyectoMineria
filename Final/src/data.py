"""Inspección, validación y limpieza conservadora del CSV local."""
import ast
import hashlib
import json
import re

import numpy as np
import pandas as pd

from .config import RAW, CLEAN, REPORTS, REQUIRED, SIGNALS


def parse_count(value):
    """Acepta números y sufijos K/M/B; rechaza negativos o texto desconocido."""
    if pd.isna(value) or str(value).strip() == '':
        return np.nan
    text = str(value).strip().upper().replace(',', '')
    match = re.fullmatch(r'(\d+(?:\.\d+)?)\s*([KMB]?)', text)
    if not match:
        raise ValueError(f'Conteo no reconocido: {value!r}')
    return float(match[1]) * {'': 1, 'K': 1e3, 'M': 1e6, 'B': 1e9}[match[2]]


def parse_list(value):
    if isinstance(value, list):
        return value
    if pd.isna(value) or value == '':
        return []
    result = ast.literal_eval(value)
    if not isinstance(result, list) or not all(isinstance(x, str) for x in result):
        raise ValueError(f'Lista no válida: {value!r}')
    return sorted(set(x.strip() for x in result if x.strip()))


def load_clean():
    df = pd.read_csv(CLEAN / 'games.csv')
    for column in ['generos', 'organizaciones']:
        df[column] = df[column].map(json.loads)
    return df


def prepare():
    raw = pd.read_csv(RAW, encoding='utf-8-sig')
    missing = sorted(set(REQUIRED) - set(raw.columns))
    if missing:
        raise ValueError(f'Cambió el esquema; faltan columnas: {missing}')
    for path in [CLEAN, REPORTS, REPORTS / 'figures']:
        path.mkdir(parents=True, exist_ok=True)
    inspection = {
        'archivo_original': 'Proyecto/data/processed/games_curated.csv',
        'copia_inmutable': 'data/raw/games_curated.csv',
        'filas': len(raw), 'columnas': len(raw.columns),
        'sha256': hashlib.sha256(RAW.read_bytes()).hexdigest(),
        'esquema': {c: {'tipo': str(raw[c].dtype), 'faltantes': int(raw[c].isna().sum())}
                    for c in raw},
        'rangos_observados': {c: {'min': float(raw[c].min()), 'max': float(raw[c].max())}
                              for c in ['Rating', 'Metacritic Rating']},
        'procedencia_critica': raw['Origen_calificacion'].value_counts().to_dict(),
        'critic_source': raw['critic_source'].value_counts(dropna=False).to_dict(),
        'escala_rating': 'Límites teóricos no documentados; rango observado compatible con 0–5.',
        'reviews_igual_times_listed': bool(raw['Times Listed'].equals(raw['Number of Reviews'])),
    }
    # Los conflictos se aíslan completos para no escoger una cifra arbitraria.
    keys = ['Title', 'Release Date']
    analytical = [c for c in REQUIRED if c not in keys + ['ID Original', 'Reviews', 'Summary']]
    conflicts = []
    conflict_indices = []
    for key, group in raw.groupby(keys, dropna=False):
        differing = [c for c in analytical if group[c].nunique(dropna=False) > 1]
        if differing:
            conflicts.append({'clave': str(key), 'columnas': differing})
            conflict_indices.extend(group.index.tolist())
    raw.loc[conflict_indices].to_csv(CLEAN / 'conflictos_duplicados.csv', index=False)
    inspection['conflictos_analiticos'] = conflicts
    inspection['filas_en_conflicto'] = len(conflict_indices)
    discarded = raw.duplicated(keys, keep='first')
    raw.loc[discarded].to_csv(CLEAN / 'duplicados_descartados.csv', index=False)
    inspection['duplicados_descartados'] = int(discarded.sum())
    df = raw.loc[~discarded & ~raw.index.isin(conflict_indices)].copy().reset_index(drop=True)
    for c in SIGNALS + ['Times Listed', 'Number of Reviews']:
        df[c] = df[c].map(parse_count)
    for c in ['Rating', 'Metacritic Rating']:
        df[c] = pd.to_numeric(df[c], errors='raise')
    df['generos'] = df['Genres'].map(parse_list)
    df['organizaciones'] = df['Team'].map(parse_list)
    df['fecha'] = pd.to_datetime(df['Release Date'], format='%b %d, %Y', errors='coerce')
    df['anio'] = df['fecha'].dt.year
    df['decada'] = df['anio'].floordiv(10).mul(10)
    real = df['critic_source'].eq('metacritic_csv') & df['Origen_calificacion'].eq('Metacritic')
    invalid = (df['critic_score_final'].notna() & ~real) | (real & df['critic_score_final'].isna())
    if invalid.any():
        raise ValueError('critic_score_final y su procedencia no concuerdan; revisar el archivo original.')
    if not df.loc[real, 'critic_score_final'].eq(df.loc[real, 'Metacritic Rating']).all():
        raise ValueError('critic_score_final difiere de Metacritic Rating en filas marcadas metacritic_csv.')
    df['critica_verificada_csv'] = df['critic_score_final'].where(real)
    # Se preserva la etiqueta de procedencia, sin afirmar verificación externa.
    df['grupo_titulo'] = df['Title'].str.strip().str.casefold()
    df['popularidad_indice'] = np.log1p(df[SIGNALS]).mean(axis=1, skipna=False)
    inspection['filas_limpias'] = len(df)
    inspection['rango_anios'] = [int(df['anio'].min()), int(df['anio'].max())]
    inspection['fechas_no_interpretables'] = df.loc[df['fecha'].isna(), ['Title', 'Release Date']].to_dict('records')
    inspection['pares_critica_real'] = int(df[['Rating', 'critica_verificada_csv']].dropna().shape[0])
    inspection['organizaciones_sin_roles'] = True
    (REPORTS / 'inspeccion.json').write_text(json.dumps(inspection, ensure_ascii=False, indent=2), encoding='utf-8')
    # El maestro se conserva completo en raw. La vista analítica admite solo campos
    # comprobados y derivados propios; no hereda brechas, roles ni escala asumidos.
    derived = ['generos', 'organizaciones', 'fecha', 'anio', 'decada',
               'critica_verificada_csv', 'grupo_titulo', 'popularidad_indice']
    df = df[[c for c in REQUIRED if c not in ['Summary', 'Reviews']] + derived]
    saved = df.copy()
    for c in ['generos', 'organizaciones']:
        saved[c] = saved[c].map(lambda x: json.dumps(x, ensure_ascii=False))
    saved.to_csv(CLEAN / 'games.csv', index=False)
    return df, inspection
