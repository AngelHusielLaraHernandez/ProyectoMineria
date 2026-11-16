"""Reconstrucción auditable del antecedente; nunca sustituye el maestro designado."""
import ast
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

CONTEOS = ['Times Listed', 'Number of Reviews', 'Plays', 'Playing', 'Backlogs', 'Wishlist']


def numero(valor):
    if pd.isna(valor):
        return np.nan
    s = str(valor).strip().replace(',', '').upper()
    return float(s[:-1]) * {'K': 1000, 'M': 1000000}[s[-1]] if s.endswith(('K', 'M')) else float(s)


def reconstruir_historico(raw):
    """Reproduce la regla histórica first para documentarla, no para aprobarla."""
    d = raw.sort_values('ID Original').drop_duplicates(['Title', 'Release Date'], keep='first').copy()
    for c in CONTEOS:
        d[c] = d[c].map(numero)
    d['release_date'] = pd.to_datetime(d['Release Date'], format='%b %d, %Y', errors='coerce').dt.strftime('%Y-%m-%d')
    fechas = pd.to_datetime(d['release_date'])
    d['year'] = fechas.dt.year
    d['decade'] = d.year // 10 * 10
    gs = d.Genres.map(lambda v: ast.literal_eval(v) if pd.notna(v) else [])
    ts = d.Team.map(lambda v: ast.literal_eval(v) if pd.notna(v) else [])
    d['genres_list'], d['team_list'] = gs.map(str), ts.map(str)
    d['n_genres'] = gs.str.len()
    d['studio_main'] = ts.map(lambda v: v[-1] if v else None)
    d['publisher_main'] = ts.map(lambda v: v[0] if v else None)
    frecuencias = gs.explode().value_counts()
    def principal(v):
        if not v:
            return 'Unknown'
        g = min(v, key=lambda x: frecuencias.get(x, 0) if x != 'Indie' else 10**9)
        return g if frecuencias.get(g, 0) >= 30 else 'Other'
    d['genre_main'] = gs.map(principal)
    d['rating_100'] = d.Rating * 20
    d['gap'] = d.rating_100 - d['Metacritic Rating']
    d['metacritic_real'] = d.Origen_calificacion.eq('Metacritic')
    d['critic_score_final'] = d['Metacritic Rating'].where(d.metacritic_real)
    d['critic_source'] = np.where(d.metacritic_real, 'metacritic_csv', 'none')
    d['gap_real'] = d.rating_100 - d.critic_score_final
    for c in ['Plays', 'Wishlist', 'Backlogs', 'Playing']:
        d[f'log_{c.lower()}'] = np.log1p(d[c])
    financieras = [c for c in raw if 'estimad' in c.lower()]
    d['estimates_zero'] = d[financieras].eq(0).any(axis=1)
    d['has_rating'] = d.Rating.notna()
    d['population'] = 'original'
    return d.reset_index(drop=True)


def auditar_historia(raiz):
    raiz = Path(raiz)
    historico = raiz / 'data/historical/games_actualizado_metacritic.csv'
    maestro = raiz / 'data/raw/games_curated.csv'
    if not historico.exists():
        return {'estado': 'sin antecedente', 'advertencia': 'No se validó la deduplicación previa.'}, set()
    raw, cur = pd.read_csv(historico), pd.read_csv(maestro)
    reconstruido = reconstruir_historico(raw)
    errores = []
    if list(reconstruido['ID Original']) != list(cur['ID Original']):
        errores.append('Selección u orden de IDs distintos')
    elif set(reconstruido) != set(cur):
        errores.append('Esquemas reconstruido y maestro distintos')
    else:
        for c in cur:
            if pd.api.types.is_numeric_dtype(cur[c]) or pd.api.types.is_numeric_dtype(reconstruido[c]):
                iguales = np.isclose(pd.to_numeric(cur[c]), pd.to_numeric(reconstruido[c]), equal_nan=True)
            else:
                iguales = cur[c].fillna('').astype(str).eq(reconstruido[c].fillna('').astype(str))
            if not np.all(iguales):
                errores.append(c)
    decisiones, grupos, ambiguos = [], [], set()
    analiticas = ['Rating', 'Metacritic Rating', *CONTEOS, 'Genres', 'Team', 'Origen_calificacion']
    for (titulo, fecha), grupo in raw.groupby(['Title', 'Release Date'], sort=False):
        grupo = grupo.sort_values('ID Original')
        if len(grupo) < 2:
            continue
        campos = [c for c in raw if c != 'ID Original' and grupo[c].nunique(dropna=False) > 1]
        conflictos = [c for c in campos if c in analiticas]
        elegido = int(grupo.iloc[0]['ID Original'])
        if conflictos:
            ambiguos.add(elegido)
        if campos:
            grupos.append({'juego': titulo, 'fecha': fecha, 'id_conservado_historicamente': elegido,
                           'ids_del_grupo': json.dumps(grupo['ID Original'].tolist()),
                           'campos_distintos': '; '.join(campos), 'conflicto_analitico': bool(conflictos)})
        for _, fila in grupo.iloc[1:].iterrows():
            decisiones.append({'juego': titulo, 'fecha': fecha, 'id_conservado': elegido,
                               'id_descartado': int(fila['ID Original']),
                               'regla_historica': 'Primer ID por título y fecha; decisión heredada, no resolución verificada',
                               'conflicto_analitico': bool(conflictos)})
    informes = raiz / 'reports'
    informes.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(decisiones).to_csv(informes / 'deduplicacion_historica.csv', index=False)
    pd.DataFrame(grupos).to_csv(informes / 'conflictos_historicos.csv', index=False)
    raw.loc[raw['ID Original'].isin([i for g in grupos for i in json.loads(g['ids_del_grupo'])])].to_csv(informes / 'variantes_historicas.csv', index=False)
    reconstruido.to_csv(informes / 'maestro_reconstruido_solo_auditoria.csv', index=False)
    pares = cur.loc[cur.Origen_calificacion.ne('Metacritic')].dropna(subset=['Rating'])
    coef = np.polyfit(pares.Rating, pares['Metacritic Rating'], 1)
    residuo = float((pares['Metacritic Rating'] - np.round(np.polyval(coef, pares.Rating))).abs().max())
    estado = {'estado': 'verificado' if not errores else 'diferencias detectadas',
              'sha256_historico': hashlib.sha256(historico.read_bytes()).hexdigest(),
              'sha256_maestro': hashlib.sha256(maestro.read_bytes()).hexdigest(),
              'filas_historicas': len(raw), 'filas_maestro': len(cur), 'descartes_heredados': len(decisiones),
              'grupos_con_diferencias': len(grupos), 'grupos_con_conflicto_analitico': len(ambiguos),
              'ids_analiticos_pendientes': sorted(ambiguos), 'columnas_reconstruidas': len(reconstruido.columns),
              'diferencias_reconstruccion': errores, 'critica_estimada_maestro': int(cur.Origen_calificacion.ne('Metacritic').sum()),
              'estimaciones_con_rating': len(pares), 'coeficientes_ajuste_sintetico': coef.tolist(),
              'residuo_maximo_tras_redondear': residuo}
    (informes / 'trazabilidad_historica.json').write_text(json.dumps(estado, ensure_ascii=False, indent=2))
    (informes / 'trazabilidad_historica.md').write_text(f'''# Trazabilidad histórica

El maestro designado sigue siendo games_curated.csv y no se modifica. El antecedente de data/historical permite reproducir sus decisiones heredadas, no aprobarlas como correctas.

Se reconstruyen {len(raw)} → {len(cur)} registros, con {len(decisiones)} descartes documentados individualmente en deduplicacion_historica.csv. Estado de comparación de las {len(reconstruido.columns)} columnas: **{estado['estado']}**; diferencias: {errores}.

Hay {len(grupos)} grupos con alguna diferencia, pero solo {len(ambiguos)} con conflicto analítico. Los IDs conservados por la regla histórica y pendientes de resolución son {sorted(ambiguos)}. Se preservan en el dataset con indicador y se excluyen del análisis principal y del entrenamiento hasta revisión, sin elegir el máximo ni promediar versiones desconocidas.

conflictos_historicos.csv identifica campos e IDs; variantes_historicas.csv conserva todas las alternativas de esos grupos. maestro_reconstruido_solo_auditoria.csv permite comparar sin escribir sobre raw.

La procedencia crítica se reconstruye a partir de Origen_calificacion: {estado['critica_estimada_maestro']} notas propias se dejan sin critic_score_final. En {len(pares)} estimaciones con Rating, el ajuste es {coef[0]:.6f} × Rating + {coef[1]:.6f}; residuo máximo tras redondear: {residuo}. Esta relación corrobora dependencia sintética; no demuestra por sí sola el algoritmo histórico exacto ni verifica las notas marcadas Metacritic.

Los conteos se obtienen con un lector CSV: wc -l no cuenta registros cuando Reviews o Summary contienen saltos de línea.

## Que debo verificar manualmente

- Plataformas, versiones y fecha de captura de las tres discrepancias numéricas.
- Procedencia de las notas críticas y decisiones heredadas de la deduplicación.
- No interpretar una reconstrucción exacta como aprobación del criterio first.
''', encoding='utf-8')
    if errores:
        raise ValueError(f'El antecedente no reconstruye el maestro: {errores}')
    return estado, ambiguos
