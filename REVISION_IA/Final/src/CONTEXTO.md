# Carpeta: Final/src

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## 01_inspeccion.py

Ruta: `Final/src/01_inspeccion.py` · Bytes: 6482 · SHA-256: `fb93e2c5c2466254ff2138631df23ae49749901c8b5cbb29fccff29adec24506`

````text
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

````

## 02_limpieza.py

Ruta: `Final/src/02_limpieza.py` · Bytes: 19606 · SHA-256: `8f1aaf78713d94560fe89d2e52379a013bafe54992d4ffcf5953003d2e7c560d`

````text
"""Limpieza auditable. Desde Final: python src/02_limpieza.py.

No modifica el maestro ni imputa notas. Las escalas y decisiones están
documentadas previamente en reports/inspeccion.md. No requiere conexión.
"""
import argparse
import ast
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd
if __package__:
    from .procedencia import auditar_historia
else:
    from procedencia import auditar_historia

RAIZ = Path(__file__).resolve().parents[1]
CONTEOS = ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Times Listed', 'Number of Reviews']
REQUERIDAS = ['ID Original', 'Title', 'Release Date', 'Genres', 'Rating',
              'Metacritic Rating', 'critic_score_final', 'critic_source',
              'Origen_calificacion', *CONTEOS]
FUENTE_USUARIOS = 'https://backloggd.com/games/elden-ring/'
FUENTE_PRENSA = 'https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore'


def es_nulo(valor):
    return valor is None or (not isinstance(valor, (list, tuple)) and pd.isna(valor))


def convertir_conteo(valor):
    """Convierte K/M, nulos y espacios; un texto inválido produce un error explícito."""
    if es_nulo(valor) or (isinstance(valor, str) and not valor.strip()):
        return np.nan
    if isinstance(valor, (int, float, np.number)) and not isinstance(valor, (bool, np.bool_)):
        numero = float(valor)
    else:
        coincidencia = re.fullmatch(r'(\d+(?:\.\d+)?|\d{1,3}(?:,\d{3})+(?:\.\d+)?)\s*([KM]?)', str(valor).strip().upper())
        if not coincidencia:
            raise ValueError(f'Conteo inválido: {valor!r}; se esperaba número o sufijo K/M.')
        numero = float(coincidencia[1].replace(',', '')) * {'': 1, 'K': 1000, 'M': 1000000}[coincidencia[2]]
    if not np.isfinite(numero) or numero < 0:
        raise ValueError(f'Conteo inválido: {valor!r}; debe ser finito y no negativo.')
    return numero


def interpretar_fecha(valor):
    """Acepta ISO, día/mes/año y mes inglés, sin inferir formatos por la primera fila."""
    if es_nulo(valor) or not str(valor).strip():
        return pd.NaT
    if isinstance(valor, (datetime, date, pd.Timestamp)):
        return pd.Timestamp(valor).normalize()
    texto = str(valor).strip()
    for formato in ['%Y-%m-%d', '%Y/%m/%d', '%d/%m/%Y', '%d-%m-%Y']:
        try:
            return pd.Timestamp(datetime.strptime(texto, formato))
        except ValueError:
            pass
    # El mapa explícito evita depender del idioma del sistema operativo.
    meses = {}
    for i, nombre in enumerate(['january', 'february', 'march', 'april', 'may', 'june',
                              'july', 'august', 'september', 'october', 'november', 'december'], 1):
        meses[nombre] = meses[nombre[:3]] = i
    coincidencia = re.fullmatch(r'([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})', texto)
    if coincidencia and coincidencia[1].lower() in meses:
        try:
            return pd.Timestamp(datetime(int(coincidencia[3]), meses[coincidencia[1].lower()], int(coincidencia[2])))
        except ValueError:
            pass
    return pd.NaT


def interpretar_generos(valor):
    """Conserva el orden original y elimina solo repeticiones internas de género."""
    if es_nulo(valor) or (isinstance(valor, str) and not valor.strip()):
        return []
    lista = valor if isinstance(valor, list) else ast.literal_eval(str(valor))
    if not isinstance(lista, list) or not all(isinstance(g, str) for g in lista):
        raise ValueError(f'Lista de géneros inválida: {valor!r}')
    return list(dict.fromkeys(g.strip() for g in lista if g.strip()))


class Bitacora:
    """Impide exportar si cambia el número de juegos sin una razón conciliable."""
    def __init__(self, filas):
        self.inicial = filas
        self.actual = filas
        self.pasos = []

    def registrar(self, paso, antes, despues, detalle, eliminadas=0, razon=''):
        if antes != self.actual:
            raise ValueError('Cambio de filas fuera del registro de limpieza.')
        if despues > antes or antes - despues != eliminadas:
            raise ValueError('El cambio de filas no coincide con las eliminaciones registradas.')
        if eliminadas and not razon.strip():
            raise ValueError('Toda eliminación requiere una razón registrada en el log.')
        self.pasos.append({'paso': paso, 'antes': antes, 'despues': despues,
                           'eliminadas': eliminadas, 'razon': razon, 'detalle': detalle})
        self.actual = despues

    def verificar(self, filas_finales):
        if self.actual != filas_finales or self.inicial - sum(p['eliminadas'] for p in self.pasos) != filas_finales:
            raise ValueError('No se conserva el balance de filas documentado en el log.')


def deduplicar(datos):
    """Solo elimina repeticiones equivalentes; los conflictos analíticos son un error."""
    df = datos.copy()
    if df['Title'].isna().any() or df['Title'].astype(str).str.strip().eq('').any():
        raise ValueError('No se puede identificar un juego con título vacío.')
    titulos = df['Title'].astype(str).map(lambda s: ' '.join(s.split()).casefold())
    fechas = df['Release Date'].map(interpretar_fecha)
    texto_fecha = df['Release Date'].map(lambda x: '' if es_nulo(x) else ' '.join(str(x).split()).casefold())
    claves = pd.DataFrame({'titulo': titulos, 'fecha': fechas.map(lambda x: x.isoformat() if pd.notna(x) else None).fillna('texto:' + texto_fecha)}, index=df.index)
    campos = [c for c in [*CONTEOS, 'Rating', 'Metacritic Rating', 'metacritic_rating_original', 'critic_score_final',
                         'critic_source', 'Origen_calificacion', 'Genres', 'Team'] if c in df]
    for _, indices in claves.groupby(['titulo', 'fecha'], sort=False).groups.items():
        grupo = df.loc[indices]
        conflictos = []
        for campo in campos:
            valores = grupo[campo].map(lambda v: tuple(sorted(interpretar_generos(v))) if campo in ['Genres', 'Team'] else v)
            if valores.nunique(dropna=False) > 1:
                conflictos.append(campo)
        if conflictos:
            raise ValueError(f'Duplicados en conflicto para {grupo.iloc[0]["Title"]!r}: {conflictos}. Revisar antes de eliminar.')
    repetidos = claves.duplicated(keep='first')
    return df.loc[~repetidos].copy(), df.loc[repetidos].copy()


def limpiar(entrada, ids_pendientes=()):
    faltan = sorted(set(REQUERIDAS) - set(entrada.columns))
    if faltan:
        raise ValueError(f'El esquema cambió; faltan columnas comprobadas: {faltan}')
    # No heredar brechas, roles ni estimaciones financieras del maestro.
    columnas = list(dict.fromkeys([*REQUERIDAS, *[c for c in ['Team', 'population'] if c in entrada]]))
    df = entrada[columnas].copy().reset_index(drop=True)
    bitacora = Bitacora(len(df))
    formatos = {'numericos': 0, 'texto_k_m': 0, 'texto_sin_sufijo': 0, 'nulos': 0}
    for campo in CONTEOS:
        valores = []
        for fila, valor in df[campo].items():
            clase = ('nulos' if es_nulo(valor) or (isinstance(valor, str) and not valor.strip())
                     else 'numericos' if isinstance(valor, (int, float, np.number))
                     else 'texto_k_m' if str(valor).strip().upper().endswith(('K', 'M')) else 'texto_sin_sufijo')
            formatos[clase] += 1
            try:
                valores.append(convertir_conteo(valor))
            except ValueError as error:
                raise ValueError(f'Columna {campo}, fila de datos {fila + 1}: {error}') from error
        df[campo] = valores
    bitacora.registrar('1. Validación y conversión de conteos', len(df), len(df),
                       f'En seis columnas: {formatos["numericos"]} celdas ya numéricas, {formatos["texto_k_m"]} textos K/M convertidos, '
                       f'{formatos["texto_sin_sufijo"]} textos numéricos convertidos y {formatos["nulos"]} nulos conservados. Los formatos inválidos detienen la ejecución.')

    df['fecha_lanzamiento'] = df['Release Date'].map(interpretar_fecha)
    df['anio'] = df['fecha_lanzamiento'].dt.year.astype('Int64')
    df['decada'] = (df['anio'] // 10 * 10).astype('Int64')
    df['fecha_faltante'] = df['Release Date'].map(lambda v: es_nulo(v) or not str(v).strip())
    df['fecha_no_interpretable'] = df['fecha_lanzamiento'].isna() & ~df['fecha_faltante']
    bitacora.registrar('2. Fechas', len(df), len(df), f'{int(df.fecha_faltante.sum())} fechas ausentes y {int(df.fecha_no_interpretable.sum())} no interpretables; no se eliminan juegos.')

    df['generos'] = df['Genres'].map(interpretar_generos)
    df['genero_principal'] = df['generos'].map(lambda gs: gs[0] if gs else pd.NA)
    df['generos_faltantes'] = df['generos'].map(len).eq(0)
    bitacora.registrar('3. Géneros', len(df), len(df), 'Primer género no vacío como convención de presentación; tabla larga tras deduplicar.')

    for campo in ['Rating', 'Metacritic Rating', 'critic_score_final']:
        df[campo] = pd.to_numeric(df[campo].map(lambda v: np.nan if isinstance(v, str) and not v.strip() else v), errors='raise')
        if not np.isfinite(df[campo].dropna()).all():
            raise ValueError(f'Notas no finitas en {campo}.')
    df['metacritic_rating_original'] = df['Metacritic Rating']
    df['metacritic_rating_faltante_original'] = df['Metacritic Rating'].isna()
    verificada = df['critic_source'].eq('metacritic_csv') & df['Origen_calificacion'].eq('Metacritic')
    if (df['critic_score_final'].notna() & ~verificada).any():
        raise ValueError('Hay critic_score_final sin procedencia coherente; revisar el maestro.')
    completos = verificada & df['critic_score_final'].notna() & df['Metacritic Rating'].notna()
    if not df.loc[completos, 'critic_score_final'].eq(df.loc[completos, 'Metacritic Rating']).all():
        raise ValueError('La nota curada y la nota original difieren en filas marcadas Metacritic.')
    df['metacritic_estimado'] = df['Origen_calificacion'].eq('Estimacion propia')
    df['Metacritic Rating'] = df['critic_score_final'].where(verificada)
    df['rating_faltante'] = df['Rating'].isna()
    df['metacritic_rating_faltante'] = df['Metacritic Rating'].isna()
    bitacora.registrar('4. Faltantes y procedencia', len(df), len(df),
                       f'Sin imputación: Rating={int(df.rating_faltante.sum())} ausentes; Metacritic original={int(df.metacritic_rating_faltante_original.sum())}; '
                       f'notas estimadas={int(df.metacritic_estimado.sum())}; Metacritic analítico={int(df.metacritic_rating_faltante.sum())} ausentes. '
                       'La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa.')

    antes = len(df)
    df, descartados = deduplicar(df)
    bitacora.registrar('5. Duplicados', antes, len(df), 'Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución.',
                       eliminadas=len(descartados), razon='Repeticiones analíticamente equivalentes de título y fecha.' if len(descartados) else '')
    if df['ID Original'].isna().any() or df['ID Original'].duplicated().any():
        raise ValueError('ID Original ausente o repetido entre juegos diferentes; no se puede relacionar la tabla larga.')
    df['id_juego'] = df['ID Original']
    df['conflicto_historico_pendiente'] = df.id_juego.isin(ids_pendientes)
    df['elegible_analisis'] = ~df.conflicto_historico_pendiente
    df['grupo_titulo'] = df.Title.map(lambda v: ' '.join(v.split()).casefold())
    df['titulo_compartido'] = df.grupo_titulo.duplicated(keep=False)

    # Se comprueban escalas documentadas, nunca se infieren de máximos muestrales.
    for campo, maximo in [('Rating', 5), ('metacritic_rating_original', 100), ('Metacritic Rating', 100)]:
        if not df[campo].dropna().between(0, maximo).all():
            raise ValueError(f'{campo} está fuera de la escala documentada con máximo {maximo}; no se calculará la brecha.')
    df['rating_normalizado'] = df['Rating'] / 5 * 100
    df['brecha'] = df['rating_normalizado'] - df['Metacritic Rating']
    df['brecha_faltante'] = df['brecha'].isna()
    bitacora.registrar('6. Escalas y brecha', len(df), len(df),
                       f'Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. '
                       f'{int(df.brecha.notna().sum())} brechas calculables; {int(df.brecha_faltante.sum())} ausentes. No es min–max de la muestra.')
    largo = df[['id_juego', 'Title', 'generos']].explode('generos').dropna(subset=['generos']).rename(columns={'Title': 'juego', 'generos': 'genero'}).reset_index(drop=True)
    df['generos'] = df['generos'].map(lambda gs: json.dumps(gs, ensure_ascii=False))
    df = df.reset_index(drop=True)
    bitacora.registrar('7. Preparación de exportación', len(df), len(df),
                       f'Tabla principal: {len(df)} juegos. Tabla larga: {len(largo)} pertenencias, relación uno a muchos, no nuevos juegos. '
                       f'{int(df.conflicto_historico_pendiente.sum())} casos históricos señalados como no elegibles; {int(df.titulo_compartido.sum())} registros comparten título. Unir solo por id_juego, validando many_to_one.')
    bitacora.verificar(len(df))
    return df, largo, descartados, bitacora


def escribir_log(bitacora, datos, largo, ruta, huella):
    bitacora.verificar(len(datos))
    lineas = ['# Log de limpieza', '', f'SHA-256 del insumo inmutable: `{huella}`.', '',
              'Fuente: `data/raw/games_curated.csv`. Decisiones previas: `reports/inspeccion.md`.', '',
              '| Paso | Filas antes | Filas después | Eliminadas | Razón del cambio | Detalle |',
              '|---|---:|---:|---:|---|---|']
    for paso in bitacora.pasos:
        lineas.append(f'| {paso["paso"]} | {paso["antes"]} | {paso["despues"]} | {paso["eliminadas"]} | {paso["razon"] or "Sin cambio de filas"} | {paso["detalle"]} |')
    lineas += ['', '## Decisiones y justificación', '',
               '**Conteos y fechas.** Se convierten solo formatos numéricos reconocidos; los inválidos causan un error con columna y fila. Las fechas desconocidas o imposibles se conservan como NaT con indicador: inventar un año alteraría el análisis por década.', '',
               '**Faltantes.** No se imputan notas ni se eliminan juegos por ausencia. La imputación estadística pertenece al entrenamiento dentro de cada fold; en análisis descriptivo se usan pares completos e indicadores para mostrar la cobertura.', '',
               '**Procedencia.** Se conserva Metacritic original en metacritic_rating_original y se usa critic_score_final con su etiqueta de fuente para la columna analítica. Una nota derivada de Rating no aporta evidencia independiente de prensa; la etiqueta del CSV no demuestra verificación externa.', '',
               '**Géneros.** El primer elemento no vacío es una convención de presentación, no un género dominante acreditado. La tabla larga conserva cada género distinto y el ID; sus filas no se suman para contar juegos únicos.', '',
               '**Duplicados.** Solo se descartan equivalencias analíticas bajo la clave documentada y se guardan las filas eliminadas. Un conflicto impide exportar para evitar seleccionar una cifra sin fundamento.', '',
               '## Verificación de escalas previa a la brecha', '',
               f'Fuentes primarias consultadas el 08/11/2026: [Backloggd, extremo superior de cinco estrellas]({FUENTE_USUARIOS}) y [Metacritic, escala 0–100]({FUENTE_PRENSA}). No se descargan ni sustituyen puntuaciones actuales.', '',
               'Conversión por máximo documentado: `rating_normalizado = Rating × 100 / 5`; `brecha = rating_normalizado − Metacritic Rating`. Positiva: usuarios por encima de prensa; negativa: por debajo. No se trasladan los extremos observados de la muestra a 0 y 100, ni se afirma equivalencia psicométrica.', '',
               f'Rango observado Rating: {datos.Rating.min():g}–{datos.Rating.max():g}; Metacritic original: {datos.metacritic_rating_original.min():g}–{datos.metacritic_rating_original.max():g}; crítica analítica: {datos["Metacritic Rating"].min():g}–{datos["Metacritic Rating"].max():g}.', '',
               '## Conciliación comprobable', '',
               'El bloque JSON permite contrastar el log con la tabla exportada. Toda disminución requiere una razón; ningún otro paso puede añadir o eliminar juegos.', '', '```json',
               json.dumps({'filas_entrada': bitacora.inicial, 'filas_salida': len(datos),
                           'filas_generos_largo': len(largo), 'pasos': bitacora.pasos}, ensure_ascii=False, indent=2), '```', '',
               '## Que debo verificar manualmente', '',
               '- Representación de cinco estrellas en la extracción histórica, media absoluta/ponderada y origen de cada nota de prensa.',
               '- Fechas numéricas ambiguas: se usa día/mes/año; consultar las marcadas no interpretables.',
               '- Orden de la lista de géneros y posibles plataformas o versiones distintas con igual título/fecha.',
               '- Las ausencias de crítica utilizable incluyen estimaciones excluidas; no significan que el juego no tenga nota fuera del CSV.', '']
    ruta.write_text('\n'.join(lineas), encoding='utf-8')


def ejecutar(raiz=RAIZ):
    raiz = Path(raiz)
    entrada = raiz / 'data' / 'raw' / 'games_curated.csv'
    contenido = entrada.read_bytes()
    huella = hashlib.sha256(contenido).hexdigest()
    historia, ids_pendientes = auditar_historia(raiz)
    datos, largo, descartados, bitacora = limpiar(pd.read_csv(entrada, encoding='utf-8-sig'), ids_pendientes)
    salida, informes = raiz / 'data' / 'clean', raiz / 'reports'
    salida.mkdir(parents=True, exist_ok=True)
    informes.mkdir(parents=True, exist_ok=True)
    datos.to_csv(salida / 'dataset_depurado.csv', index=False, encoding='utf-8')
    largo.to_csv(salida / 'generos_largo.csv', index=False, encoding='utf-8')
    descartados.to_csv(salida / 'duplicados_limpieza.csv', index=False, encoding='utf-8')
    escribir_log(bitacora, datos, largo, informes / 'limpieza_log.md', huella)
    with (informes / 'limpieza_log.md').open('a', encoding='utf-8') as archivo:
        archivo.write('\n## Antecedente de la deduplicación\n\n')
        archivo.write(f'Estado: {historia["estado"]}. Esta corrida no elimina las 395 filas históricas: ya no están en el maestro de entrada. ')
        archivo.write('Ver trazabilidad_historica.md, deduplicacion_historica.csv y conflictos_historicos.csv para decisiones por ID. ' if ids_pendientes else '')
        archivo.write('No confundir 0 descartes actuales con ausencia de decisiones anteriores.\n\n## Que debo verificar manualmente\n\n- Resolver los conflictos heredados y usar id_juego para relacionar tablas.\n')
    if entrada.read_bytes() != contenido:
        raise RuntimeError('La fuente cambió durante la ejecución; revisar antes de usar las salidas.')
    print(f'Limpieza completada: {bitacora.inicial} → {len(datos)} juegos; {len(largo)} pertenencias de género. Ver reports/limpieza_log.md.')
    return datos, largo, bitacora


if __name__ == '__main__':
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument('--raiz', type=Path, default=RAIZ, help='Raíz del proyecto; por defecto se deriva de este archivo.')
    ejecutar(analizador.parse_args().raiz)

````

## 03_clustering.py

Ruta: `Final/src/03_clustering.py` · Bytes: 33309 · SHA-256: `9451a90f1db4994b813fc697ef05e5f16759d16ee63e878535c4a4810034bc38`

````text
"""Correlaciones y clustering de seis variables. Desde Final: python src/03_clustering.py."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(RAIZ / '.cache' / 'matplotlib'))
os.environ.setdefault('XDG_CACHE_HOME', str(RAIZ / '.cache'))

import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.cluster import DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

SEMILLA = 42
MINIMO_PARES = 20
CONTEOS = ['Plays', 'Playing', 'Backlogs', 'Wishlist']
VARIABLES = [*CONTEOS, 'Rating', 'Metacritic Rating']


def lista(valor):
    if isinstance(valor, list):
        salida = valor
    elif pd.isna(valor) or not str(valor).strip():
        return []
    else:
        salida = ast.literal_eval(str(valor))
    if not isinstance(salida, list) or not all(isinstance(v, str) for v in salida):
        raise ValueError(f'Lista inválida: {valor!r}')
    return list(dict.fromkeys(v.strip() for v in salida if v.strip()))


def asociacion(df, a='Rating', b='Metacritic Rating', grupo='Catálogo'):
    pares = df[[a, b]].dropna()
    resultado = {'grupo': grupo, 'variable_a': a, 'variable_b': b, 'n_juegos': len(df),
                 'n': len(pares), 'estado': 'incluido', 'pearson_r': np.nan, 'pearson_p': np.nan,
                 'spearman_rho': np.nan, 'spearman_p': np.nan}
    if len(pares) < MINIMO_PARES:
        resultado['estado'] = 'excluido: menos de 20 pares completos'
    elif pares.nunique().min() < 2:
        resultado['estado'] = 'excluido: variable constante'
    else:
        r, p = pearsonr(pares[a], pares[b])
        rho, ps = spearmanr(pares[a], pares[b])
        resultado.update(pearson_r=float(r), pearson_p=float(p), spearman_rho=float(rho), spearman_p=float(ps))
    return resultado


def ajustar_bh(tabla):
    """Ajusta cada familia de pruebas, conservando los p-valores sin ajustar."""
    for campo in ['pearson_p', 'spearman_p']:
        orden = tabla[campo].dropna().sort_values()
        tabla[campo.replace('_p', '_q_bh')] = np.nan
        if len(orden):
            q = orden.to_numpy() * len(orden) / np.arange(1, len(orden) + 1)
            q = np.minimum.accumulate(q[::-1])[::-1].clip(max=1)
            tabla.loc[orden.index, campo.replace('_p', '_q_bh')] = q
    return tabla


def correlaciones_por_grupo(df, columna):
    expandido = df.explode(columna).dropna(subset=[columna])
    resultados = []
    for nombre, grupo in expandido.groupby(columna):
        fila = asociacion(grupo, grupo=nombre)
        pares = grupo.dropna(subset=['Rating', 'Metacritic Rating'])
        fila['brecha_media'] = pares['brecha'].mean()
        fila['brecha_absoluta_media'] = pares['brecha'].abs().mean()
        resultados.append(fila)
    columnas = list(asociacion(df).keys()) + ['brecha_media', 'brecha_absoluta_media']
    return ajustar_bh(pd.DataFrame(resultados, columns=columnas)).sort_values(['n_juegos', 'grupo'], ascending=[False, True])


def preparar_espacio(df):
    """Solo casos completos: ni notas sintéticas ni imputaciones para el clustering."""
    for campo in VARIABLES:
        valores = df[campo].dropna()
        if not np.isfinite(valores).all() or (valores < 0).any():
            raise ValueError(f'Valores negativos o no finitos en {campo}.')
    if not df['Rating'].dropna().between(0, 5).all() or not df['Metacritic Rating'].dropna().between(0, 100).all():
        raise ValueError('Notas fuera de las escalas documentadas en la limpieza.')
    mascara = df[VARIABLES].notna().all(axis=1)
    if 'elegible_analisis' in df:
        mascara &= df.elegible_analisis
    if mascara.sum() < 21:
        raise ValueError('Se necesitan al menos 21 casos completos para este protocolo.')
    transformados = df.loc[mascara, VARIABLES].copy().astype(float)
    transformados[CONTEOS] = np.log1p(transformados[CONTEOS])
    escalador = StandardScaler().fit(transformados)
    return mascara, escalador.transform(transformados), escalador


def elegir_eps(espacio, min_samples):
    """Codo determinista: máxima distancia a la cuerda de la curva normalizada."""
    vecinos = NearestNeighbors(n_neighbors=min_samples).fit(espacio)
    # Consultar X explícitamente incluye el propio punto, igual que min_samples de DBSCAN.
    distancias = np.sort(vecinos.kneighbors(espacio)[0][:, -1])
    positivos = distancias[distancias > 0]
    if not len(positivos):
        raise ValueError('Todos los puntos coinciden; no hay eps positivo identificable.')
    if np.isclose(distancias[-1], distancias[0]):
        indice = len(distancias) // 2
        motivo = 'Curva sin codo distinguible; referencia de distancia constante, requiere revisión.'
    else:
        x = np.linspace(0, 1, len(distancias))
        y = (distancias - distancias[0]) / (distancias[-1] - distancias[0])
        indice = int(np.argmax(x - y))
        motivo = 'Máxima separación x−y respecto de la cuerda, tras normalizar ambos ejes a [0,1].'
    eps = float(distancias[indice])
    if eps <= 0:
        eps = float(positivos[0])
        motivo += ' Se usó la menor distancia positiva porque el codo era cero.'
    return eps, indice, distancias, motivo


def silueta_sin_ruido(espacio, etiquetas):
    mascara = etiquetas != -1
    n_grupos = len(set(etiquetas[mascara]))
    return float(silhouette_score(espacio[mascara], etiquetas[mascara])) if 1 < n_grupos < mascara.sum() else None


def nombre_perfil(grupo, completo, ruido=False):
    if ruido:
        return 'Atípicos de densidad (ruido; no es un cluster)'
    referencia = np.log1p(completo[CONTEOS])
    nivel = ((np.log1p(grupo[CONTEOS]).mean() - referencia.mean()) / referencia.std(ddof=0).replace(0, np.nan)).mean()
    notas = completo[['Rating', 'Metacritic Rating']]
    recepcion = ((grupo[['Rating', 'Metacritic Rating']].mean() - notas.mean()) / notas.std(ddof=0).replace(0, np.nan)).mean()
    actividad = 'Actividad e interés superiores al promedio' if nivel > 0 else 'Actividad e interés inferiores al promedio' if nivel < 0 else 'Actividad en el promedio'
    calidad = 'recepción superior al promedio' if recepcion > 0 else 'recepción inferior al promedio' if recepcion < 0 else 'recepción en el promedio'
    return f'{actividad}; {calidad}'


def describir_perfiles(completo, espacio, etiquetas, metodo):
    filas, ejemplos = [], []
    for etiqueta in sorted(set(etiquetas)):
        posiciones = np.flatnonzero(etiquetas == etiqueta)
        grupo = completo.iloc[posiciones]
        frecuencias = grupo['_generos'].explode().dropna().value_counts().rename_axis('genero').reset_index(name='n')
        frecuencias = frecuencias.sort_values(['n', 'genero'], ascending=[False, True]).head(3)
        dominantes = '; '.join(f'{r.genero}: {r.n} ({r.n/len(grupo):.1%})' for r in frecuencias.itertuples()) or 'Sin género registrado'
        fila = {'metodo': metodo, 'cluster': int(etiqueta), 'n': len(grupo),
                'perfil_propuesto': nombre_perfil(grupo, completo, etiqueta == -1), 'generos_dominantes': dominantes}
        fila.update({f'media_{c}': float(grupo[c].mean()) for c in VARIABLES})
        filas.append(fila)
        if etiqueta == -1:
            seleccion = grupo.sort_values('id_juego', kind='stable').head(5)
        else:
            centro = espacio[posiciones].mean(axis=0)
            orden = np.argsort(np.linalg.norm(espacio[posiciones] - centro, axis=1), kind='stable')[:5]
            seleccion = grupo.iloc[orden]
        ejemplos.extend({'metodo': metodo, 'cluster': int(etiqueta), 'id_juego': int(r.id_juego), 'juego': r.Title} for r in seleccion.itertuples())
    return pd.DataFrame(filas), pd.DataFrame(ejemplos)


def tabla_md(df):
    """Tabla portable sin dependencia opcional de tabulate."""
    def celda(valor, columna):
        if pd.isna(valor):
            return '—'
        if isinstance(valor, (float, np.floating)):
            if valor == 0 and str(columna).endswith(('_p', '_q_bh')):
                return '≈0 (límite numérico)'
            return f'{valor:.4g}'
        return str(valor).replace('|', '/').replace('\n', ' ')
    if df.empty:
        return '_Sin grupos que cumplan el criterio._'
    return '\n'.join(['| ' + ' | '.join(map(str, df.columns)) + ' |',
                      '| ' + ' | '.join(['---'] * len(df.columns)) + ' |',
                      *['| ' + ' | '.join(celda(v, c) for c, v in zip(df.columns, fila)) + ' |' for fila in df.itertuples(index=False, name=None)]])


def ejecutar(raiz=RAIZ):
    raiz = Path(raiz)
    entrada = raiz / 'data' / 'clean' / 'dataset_depurado.csv'
    contenido = entrada.read_bytes()
    df = pd.read_csv(entrada)
    necesarias = set(VARIABLES + ['id_juego', 'Title', 'Team', 'generos', 'brecha', 'critic_source', 'metacritic_estimado'])
    if necesarias - set(df):
        raise ValueError(f'Faltan campos de la fase 02: {sorted(necesarias - set(df))}')
    if df.id_juego.isna().any() or df.id_juego.duplicated().any():
        raise ValueError('id_juego debe ser único y estar presente.')
    if (df['Metacritic Rating'].notna() & (df['critic_source'].ne('metacritic_csv') | df['metacritic_estimado'])).any():
        raise ValueError('La entrada contiene notas críticas sin procedencia válida según la fase 02.')
    esperada = df.Rating * 20 - df['Metacritic Rating']
    if not np.allclose(df['brecha'], esperada, equal_nan=True):
        raise ValueError('La brecha no coincide con las escalas de la fase 02.')
    df['_generos'] = df.generos.map(lista)
    df['_organizaciones'] = df.Team.map(lista)
    informes = raiz / 'reports'
    figuras = informes / 'figures'
    modelos = raiz / 'models'
    for ruta in [figuras, modelos]:
        ruta.mkdir(parents=True, exist_ok=True)

    cohorte = df.loc[df.elegible_analisis] if 'elegible_analisis' in df else df
    globales = ajustar_bh(pd.DataFrame([asociacion(cohorte)]))
    generos = correlaciones_por_grupo(cohorte, '_generos')
    organizaciones = correlaciones_por_grupo(cohorte, '_organizaciones')
    # Los 15 grupos con más títulos se eligen sin mirar correlaciones ni p-valores.
    top_organizaciones = organizaciones.head(15)
    pares_senales = ajustar_bh(pd.DataFrame([asociacion(cohorte, a, b) for i, a in enumerate(VARIABLES) for b in VARIABLES[i+1:]]))
    sensibilidad_titulo = []
    for columna in [None, '_generos', '_organizaciones']:
        grupos = [('Catálogo', cohorte)] if columna is None else cohorte.explode(columna).dropna(subset=[columna]).groupby(columna)
        for nombre, grupo in grupos:
            pares = grupo.dropna(subset=['Rating', 'Metacritic Rating'])
            titulo = pares.Title.map(lambda s: ' '.join(s.split()).casefold())
            unicos = pares.assign(_titulo=titulo).groupby('_titulo')[['Rating', 'Metacritic Rating']].mean()
            fila = asociacion(unicos, grupo=nombre)
            fila['familia'] = columna or 'catalogo'
            fila['n_registros_pareados'] = len(pares)
            sensibilidad_titulo.append(fila)
    pd.DataFrame(sensibilidad_titulo).to_csv(informes / 'clustering_03_sensibilidad_titulos.csv', index=False)
    ranking = generos.loc[generos.estado.eq('incluido')].sort_values(['brecha_absoluta_media', 'grupo'])
    for nombre, tabla in [('catalogo', globales), ('generos', generos), ('organizaciones', organizaciones),
                          ('senales', pares_senales), ('ranking_generos', ranking)]:
        tabla.to_csv(informes / f'clustering_03_correlaciones_{nombre}.csv', index=False)

    mascara, espacio, escalador = preparar_espacio(df)
    completo = df.loc[mascara].copy()
    ensayos, ajustados = [], {}
    for k in range(2, 11):
        modelo = KMeans(n_clusters=k, n_init=30, random_state=SEMILLA).fit(espacio)
        ensayos.append({'k': k, 'inercia': float(modelo.inertia_), 'silhouette': float(silhouette_score(espacio, modelo.labels_))})
        ajustados[k] = modelo
    seleccion = pd.DataFrame(ensayos)
    mejor_k = int(seleccion.sort_values(['silhouette', 'k'], ascending=[False, True]).iloc[0]['k'])
    kmeans = ajustados[mejor_k]
    seleccion.to_csv(informes / 'clustering_03_seleccion_kmeans.csv', index=False)
    fig, ejes = plt.subplots(1, 2, figsize=(10, 4), layout='constrained')
    for eje, variable in zip(ejes, ['inercia', 'silhouette']):
        eje.plot(seleccion.k, seleccion[variable], marker='o', color='#17645b')
        eje.axvline(mejor_k, linestyle='--', color='#a34b35', label=f'k elegido = {mejor_k}')
        eje.set(xlabel='Número de clusters (k)', ylabel=variable.capitalize(), xticks=list(range(2, 11)))
        eje.legend()
    fig.savefig(figuras / 'clustering_03_kmeans.png', dpi=160)
    plt.close(fig)

    min_samples = 2 * len(VARIABLES)
    eps, codo, distancias, regla_eps = elegir_eps(espacio, min_samples)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(espacio)
    fig, eje = plt.subplots(figsize=(8, 4), layout='constrained')
    eje.plot(np.arange(1, len(distancias)+1), distancias, color='#17645b')
    eje.axhline(eps, color='#a34b35', linestyle='--', label=f'eps={eps:.4f}')
    eje.scatter([codo+1], [distancias[codo]], color='#a34b35', zorder=3)
    eje.set(xlabel='Juegos ordenados por distancia', ylabel=f'Distancia al vecino {min_samples} (incluye el propio punto)', title='Selección de eps mediante k-distancia')
    eje.legend()
    fig.savefig(figuras / 'clustering_03_dbscan_kdistancia.png', dpi=160)
    plt.close(fig)
    pd.DataFrame({'orden': np.arange(1, len(distancias)+1), 'k_distancia': distancias}).to_csv(informes / 'clustering_03_kdistancia.csv', index=False)
    sensibilidad = []
    for factor in [.8, 1., 1.2]:
        etiquetas = DBSCAN(eps=eps * factor, min_samples=min_samples).fit_predict(espacio)
        tamanos = pd.Series(etiquetas[etiquetas != -1]).value_counts()
        sensibilidad.append({'factor_eps': factor, 'eps': eps * factor, 'clusters': len(tamanos),
                             'ruido': int((etiquetas == -1).sum()), 'grupo_mayor': int(tamanos.max()) if len(tamanos) else 0})
    sensibilidad = pd.DataFrame(sensibilidad)
    sensibilidad.to_csv(informes / 'clustering_03_sensibilidad_dbscan.csv', index=False)

    resumenes, muestras = [], []
    for metodo, etiquetas in [('kmeans', kmeans.labels_), ('dbscan', dbscan.labels_)]:
        resumen, ejemplos = describir_perfiles(completo, espacio, etiquetas, metodo)
        resumenes.append(resumen)
        muestras.append(ejemplos)
        columna = f'cluster_{metodo}'
        df[columna] = pd.Series(pd.NA, index=df.index, dtype='Int64')
        df.loc[mascara, columna] = etiquetas
        nombres = resumen.set_index('cluster')['perfil_propuesto']
        df[f'perfil_{metodo}'] = df[columna].map(nombres)
    perfiles = pd.concat(resumenes, ignore_index=True)
    ejemplos = pd.concat(muestras, ignore_index=True)
    perfiles.to_csv(informes / 'clustering_03_perfiles.csv', index=False)
    ejemplos.to_csv(informes / 'clustering_03_ejemplos.csv', index=False)
    df['incluido_clustering'] = mascara
    df['motivo_no_agrupado'] = df.apply(lambda fila: '; '.join(
        [f'Falta {c}' for c in VARIABLES if pd.isna(fila[c])] +
        (['Conflicto numérico histórico pendiente'] if not fila.get('elegible_analisis', True) else [])), axis=1)
    salida = df.drop(columns=['_generos', '_organizaciones'])
    salida.to_csv(raiz / 'data' / 'clean' / 'dataset_con_clusters.csv', index=False)
    pca = PCA(n_components=2, random_state=SEMILLA).fit(espacio)
    proyeccion = pca.transform(espacio)
    salida['componente_1'] = np.nan
    salida['componente_2'] = np.nan
    salida.loc[mascara, ['componente_1', 'componente_2']] = proyeccion
    salida.to_csv(raiz / 'data/clean/dataset_con_clusters.csv', index=False)
    alternativas, ejemplos_alt = [], []
    for k in [2, 3, 4]:
        resumen, ej = describir_perfiles(completo, espacio, ajustados[k].labels_, f'kmeans_k{k}')
        alternativas.append(resumen)
        ejemplos_alt.append(ej)
    alternativas = pd.concat(alternativas, ignore_index=True)
    alternativas.to_csv(informes / 'clustering_03_alternativas_k.csv', index=False)
    pd.concat(ejemplos_alt, ignore_index=True).to_csv(informes / 'clustering_03_ejemplos_alternativas.csv', index=False)
    pd.DataFrame(espacio, columns=VARIABLES).to_csv(raiz / 'data/clean/clustering_espacio.csv', index=False)
    completo[['id_juego', 'Title']].to_csv(raiz / 'data/clean/clustering_orden.csv', index=False)
    fig, ejes = plt.subplots(1, 2, figsize=(10, 4), layout='constrained')
    for eje, etiquetas, titulo in zip(ejes, [kmeans.labels_, dbscan.labels_], ['K-Means', 'DBSCAN (−1 = ruido)']):
        eje.scatter(proyeccion[:, 0], proyeccion[:, 1], c=etiquetas, cmap='viridis', s=12, alpha=.6)
        eje.set(title=titulo, xlabel='Componente 1', ylabel='Componente 2')
    fig.savefig(figuras / 'clustering_03_proyeccion.png', dpi=160)
    plt.close(fig)
    parametros = {'sha256_entrada': hashlib.sha256(contenido).hexdigest(), 'semilla': SEMILLA,
                  'variables': VARIABLES, 'log1p': CONTEOS, 'n_entrada': len(df), 'n_completos': int(mascara.sum()),
                  'n_excluidos_clustering': int((~mascara).sum()), 'n_cohorte_analitica': len(cohorte),
                  'n_conflictos_historicos': len(df) - len(cohorte), 'minimo_pares_correlacion': MINIMO_PARES,
                  'kmeans_k': mejor_k, 'dbscan_eps': eps, 'dbscan_min_samples': min_samples,
                  'dbscan_ruido': int((dbscan.labels_ == -1).sum()),
                  'dbscan_clusters': len(set(dbscan.labels_) - {-1}),
                  'dbscan_silhouette_sin_ruido': silueta_sin_ruido(espacio, dbscan.labels_),
                  'pca_varianza': pca.explained_variance_ratio_.tolist(), 'regla_eps': regla_eps}
    (informes / 'clustering_03_parametros.json').write_text(json.dumps(parametros, ensure_ascii=False, indent=2), encoding='utf-8')
    joblib.dump({'scaler': escalador, 'kmeans': kmeans, 'dbscan': dbscan, 'pca': pca, 'parametros': parametros}, modelos / 'clustering_03.joblib')
    escribir_reporte(informes, df, globales, generos, top_organizaciones, ranking, pares_senales, seleccion, perfiles, ejemplos, sensibilidad, parametros)
    reporte = informes / 'clustering.md'
    texto = reporte.read_text(encoding='utf-8')
    texto += '\n## Comparación interpretativa de k=2, k=3 y k=4\n\n'
    texto += 'k=2 maximiza silhouette, pero resume sobre todo magnitud conjunta. Se presentan también k=3 y k=4 para evaluar perfiles cruzados sin cambiar k por conveniencia narrativa. Sus medias se calculan en las unidades originales; ver clustering_03_ejemplos_alternativas.csv para ejemplos de cada alternativa.\n\n'
    texto += tabla_md(alternativas) + '\n\n'
    texto += '## Sensibilidad a títulos compartidos\n\n'
    texto += 'Las relaciones entre tablas usan id_juego, nunca Title. Como análisis de sensibilidad, se promedian las dos notas dentro de cada título sobre sus pares completos y se recalculan Pearson/Spearman por título único. Esto reduce el peso de nombres repetidos, pero puede juntar obras distintas: no sustituye la unidad juego ni resuelve remakes. El archivo clustering_03_sensibilidad_titulos.csv incluye géneros y organizaciones.\n\n'
    texto += tabla_md(pd.DataFrame(sensibilidad_titulo).query('familia == "catalogo"'))
    texto += '\n\n## Diagnóstico de la auditoría\n\n'
    texto += f'Se excluyen {len(df)-len(cohorte)} conflictos numéricos históricos señalados; no se cambia el maestro. El grupo Visual Novel puede tener menor brecha absoluta sin concordancia de orden: revisar r, rho y sus p-valores. La cercanía de puntuaciones no prueba que usuarios y críticos ordenen igual los juegos. Tampoco se atribuye una varianza mínima sin comprobarla.\n\n'
    texto += 'Si DBSCAN devuelve un solo grupo, no se inventa una silhouette ni se fuerza eps para obtener perfiles. Con este protocolo es un detector de núcleo y atípicos; su utilidad como segmentación de mercado queda rechazada. La curva geométrica y la sensibilidad local son diagnósticos, no pruebas de separación natural.\n\n'
    texto += '## Que debo verificar manualmente\n\n- Resolver plataformas de conflictos heredados y validar títulos compartidos.\n- Elegir entre parsimonia de k=2 y utilidad descriptiva de k=3/4 antes de convertir perfiles en decisiones.\n- No usar etiquetas ni scaler descriptivo como entrada de la clasificación supervisada.\n'
    reporte.write_text(texto, encoding='utf-8')
    if entrada.read_bytes() != contenido or len(salida) != len(df):
        raise RuntimeError('La fuente cambió o no se conserva el número de juegos.')
    print(f'Análisis completado: {len(df)} juegos conservados; {int(mascara.sum())} agrupados; k={mejor_k}; eps={eps:.4f}; ruido={parametros["dbscan_ruido"]}. Ver reports/clustering.md.')
    return parametros


def escribir_reporte(informes, df, globales, generos, organizaciones, ranking, senales, seleccion, perfiles, ejemplos, sensibilidad, p):
    columnas = ['grupo', 'n_juegos', 'n', 'pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']
    elegibles = generos.loc[generos.estado.eq('incluido')]
    descartados = generos.loc[~generos.estado.eq('incluido'), ['grupo', 'n_juegos', 'n', 'estado']]
    org_validas = organizaciones.loc[organizaciones.estado.eq('incluido')]
    org_excluidas = organizaciones.loc[~organizaciones.estado.eq('incluido'), ['grupo', 'n_juegos', 'n', 'estado']]
    bloques = ['# Correlaciones y clustering de videojuegos', '',
        f'Entrada: `data/clean/dataset_depurado.csv`, SHA-256 `{p["sha256_entrada"]}`. Semilla: 42. La fuente permanece intacta.', '',
        f'Universo: {p["n_entrada"]} juegos. Cohorte histórica elegible: {p["n_cohorte_analitica"]}; conflictos pendientes excluidos: {p["n_conflictos_historicos"]}. Casos completos elegibles: {p["n_completos"]}; no agrupados por ausencias o conflictos: {p["n_excluidos_clustering"]}. La salida conserva todos los juegos.', '',
        '## 1. Correlaciones', '',
        '**Poblaciones y cobertura.** Las correlaciones usan pares completos para cada comparación. Se excluyen grupos con menos de 20 pares válidos, criterio más conservador que contar 20 juegos aunque falten notas; los n y las exclusiones se muestran explícitamente.', '',
        '**Procedencia.** Metacritic Rating es la columna analítica producida por la fase 02: excluye estimaciones propias. Se valida la coherencia con critic_source y la brecha antes de calcular; las etiquetas del CSV no son una comprobación externa de cada nota.', '',
        '### Catálogo: usuarios frente a prensa', '', tabla_md(globales[columnas]), '',
        'Pearson estima asociación lineal y Spearman asociación monótona basada en rangos; ninguno mide acuerdo ni causalidad. No se interpretan las diferencias entre coeficientes de grupos superpuestos como diferencias estadísticamente probadas.', '',
        '### Géneros incluidos', '', tabla_md(elegibles[columnas]), '',
        'Cada juego participa una vez en cada género declarado, no solo en genero_principal. Los grupos se superponen y sus n no se suman para contar juegos.', '',
        '### Géneros excluidos', '', tabla_md(descartados), '',
        '### Organizaciones con más juegos', '',
        'Se seleccionan las 15 organizaciones con más títulos antes de observar los coeficientes y luego se aplica el mínimo de 20 pares. Team mezcla desarrolladores y editores: esta tabla no acredita que todas estas organizaciones sean estudios desarrolladores.', '',
        tabla_md(org_validas[columnas]), '', 'Excluidas dentro de las 15 más frecuentes:', '', tabla_md(org_excluidas), '',
        'El CSV clustering_03_correlaciones_organizaciones.csv conserva el inventario completo, incluidos los grupos pequeños y la razón de exclusión.', '',
        '### Comprobación por sesgo de las señales', '',
        tabla_md(pd.DataFrame({'variable': CONTEOS, 'asimetria_original': [df[c].skew() for c in CONTEOS], 'asimetria_log1p': [np.log1p(df[c]).skew() for c in CONTEOS]})), '',
        'Spearman se calcula también para todos los pares de las seis variables, sobre sus valores originales. Es una comprobación útil ante asimetría y relaciones monótonas no lineales; log1p no cambia el orden de los conteos, y por tanto no cambia sus rangos.', '',
        tabla_md(senales[['variable_a', 'variable_b', 'n', 'pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']]), '',
        'Los CSV conservan p-valores y q de Benjamini–Hochberg por familia y método. Los p-valores de Spearman usan la aproximación asintótica de SciPy, no permutaciones exactas; con grupos pequeños o muchos empates deben interpretarse con cautela. Cuando SciPy devuelve cero por límite numérico, se muestra ≈0 y no se afirma una probabilidad exactamente nula.', '',
        'El p-valor es bilateral y contrasta asociación nula, no igualdad de notas; la dependencia entre juegos/franquicias y los grupos superpuestos limita la inferencia.', '',
        '### Coincidencia y discrepancia por género', '',
        '**Criterio.** Se ordena por media de la brecha absoluta, en puntos sobre 100: menor valor significa mayor cercanía de puntuaciones. La brecha firmada Rating × 20 − Metacritic informa dirección; una media cercana a cero puede ocultar diferencias opuestas, por eso no se usa para ordenar.', '',
        tabla_md(ranking[['grupo', 'n', 'brecha_absoluta_media', 'brecha_media', 'pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']]), '',
        f'Menor distancia de puntuaciones (sin implicar concordancia de orden): {", ".join(ranking.grupo.head(5))}. Mayores brechas absolutas: {", ".join(ranking.sort_values(["brecha_absoluta_media", "grupo"], ascending=[False, True]).grupo.head(5))}.', '',
        'La conversión de la fase 02 usa el máximo de cinco estrellas documentado de Backloggd y la escala 0–100 de prensa; no implica equivalencia psicométrica entre sus sistemas. La incertidumbre y las diferencias de composición impiden interpretar este orden como un ranking poblacional definitivo.', '',
        '## 2. Preparación del clustering', '',
        '**Variables.** Se usan Plays, Playing, Backlogs, Wishlist, Rating y Metacritic Rating. Los cuatro conteos reciben log1p para reducir escala y asimetría, conservando ceros; después StandardScaler se ajusta a las seis variables entre los casos completos.', '',
        '**Faltantes.** No se imputan notas: excluir casos incompletos evita fabricar la recepción de los juegos. Se conservan en el CSV con incluido_clustering=False, motivo_no_agrupado y etiquetas vacías; la cobertura parcial puede sesgar los perfiles hacia títulos con crítica disponible.', '',
        '**Género.** No entra a las distancias: se usa únicamente para describir la composición posterior. Así no se impone una distancia arbitraria entre categorías ni se pondera adicionalmente a juegos con múltiples géneros.', '',
        '**Alcance.** Es segmentación descriptiva de todos los casos completos, por eso no hay partición de entrenamiento/prueba. Estos clusters sí usan calificaciones: no se debe evaluar después un clasificador de sus etiquetas usando las mismas notas como si fuera una validación independiente.', '',
        '## 3. K-Means: elección de k', '', tabla_md(seleccion), '',
        '![Inercia y silhouette](figures/clustering_03_kmeans.png)', '',
        f'**Elección.** k={p["kmeans_k"]} maximiza silhouette entre 2 y 10; ante empate se prefiere el menor k. Se usan 30 inicializaciones y random_state=42; la inercia se muestra como diagnóstico complementario, no como criterio que siempre escogería el k más grande.', '',
        'La preferencia de silhouette no acredita que existan segmentos comerciales naturales ni estabilidad frente a otra muestra. El género no se utilizó para seleccionar k.', '',
        '## 4. DBSCAN: k-distancia y ruido', '',
        f'**Parámetros.** Se fija min_samples={p["dbscan_min_samples"]} como convención operativa de dos veces las seis dimensiones. La curva usa ese vecino contando el propio punto, coherente con la definición de densidad de DBSCAN; no se mezclan distancias de la escala original y la estandarizada.', '',
        f'**Selección reproducible.** {p["regla_eps"]} Se obtiene eps={p["dbscan_eps"]:.6f}; no se selecciona el valor para forzar un número de clusters ni maximizar silhouette.', '',
        '![Curva de k-distancia](figures/clustering_03_dbscan_kdistancia.png)', '',
        f'Resultado: {p["dbscan_clusters"]} clusters y **{p["dbscan_ruido"]} puntos de ruido** ({p["dbscan_ruido"]/p["n_completos"]:.2%} de los agrupables). La etiqueta −1 es ruido, no un perfil. Silhouette excluyendo ruido: {p["dbscan_silhouette_sin_ruido"] if p["dbscan_silhouette_sin_ruido"] is not None else "no definida: no hay al menos dos clusters válidos"}.', '',
        'Sensibilidad local a eps (min_samples fijo):', '', tabla_md(sensibilidad), '',
        'Esta comparación local no demuestra estabilidad general frente a remuestreo u otros min_samples. Un grupo dominante o muchos puntos de ruido limitan la utilidad de la segmentación, aunque una métrica aislada resulte favorable.', '',
        '## 5. Interpretación de cada perfil', '',
        '**Nombres propuestos.** Se describe la posición superior o inferior al promedio de los casos completos mediante la media de z-scores, sin umbral arbitrario de 0.5 ni categorías absolutas de calidad. Los valores medios acompañan los nombres; no se infieren ventas, rentabilidad ni condición de culto.', '',
        '**Géneros y ejemplos.** Se muestran los tres géneros más frecuentes, con número y porcentaje de juegos del grupo; sus porcentajes pueden sumar más de 100 %. Los cinco ejemplos son los más cercanos al centro descriptivo del grupo en las seis dimensiones transformadas; para ruido se eligen los primeros cinco IDs. Si hay menos de cinco juegos se muestran todos.', '']
    for fila in perfiles.itertuples(index=False):
        bloques += [f'### {fila.metodo}: etiqueta {fila.cluster} · {fila.perfil_propuesto}', '',
                    f'Tamaño: **{fila.n}** juegos. Géneros dominantes: {fila.generos_dominantes}.', '',
                    tabla_md(pd.DataFrame({'variable': VARIABLES, 'media_en_escala_original': perfiles.loc[(perfiles.metodo == fila.metodo) & (perfiles.cluster == fila.cluster), [f'media_{c}' for c in VARIABLES]].iloc[0].to_numpy()})), '',
                    'Juegos de ejemplo:', '', tabla_md(ejemplos.loc[(ejemplos.metodo == fila.metodo) & (ejemplos.cluster == fila.cluster), ['id_juego', 'juego']]), '']
    bloques += ['### Proyección complementaria', '',
                '![Proyección PCA](figures/clustering_03_proyeccion.png)', '',
                f'PCA se usa solo para visualizar: las dos componentes conservan {sum(p["pca_varianza"]):.1%} de la varianza. Las etiquetas se ajustaron en seis dimensiones y no sobre esta proyección.', '',
                '## 6. Artefactos y límites', '',
                f'`data/clean/dataset_con_clusters.csv` conserva los {p["n_entrada"]:,} registros de la fuente y agrega cluster_kmeans, cluster_dbscan, perfiles, incluido_clustering y motivo_no_agrupado. Las etiquetas vacías no significan ruido; −1 solo aparece para los casos completos considerados atípicos por DBSCAN.', '',
                'Las tablas completas, búsqueda de k, curva de distancias, sensibilidad, medias y ejemplos se guardan con prefijo clustering_03_ en reports. El pipeline descriptivo se conserva en models/clustering_03.joblib junto con variables y parámetros; DBSCAN no aporta una regla predict de asignación para juegos nuevos.', '',
                'Este es el único protocolo de clustering activo: la app y el orquestador leen estos mismos artefactos de seis variables. Los resultados antiguos de cuatro conteos quedan archivados fuera del flujo; las etiquetas descriptivas no se entregan al clasificador supervisado.', '',
                '## Que debo verificar manualmente', '',
                '- Procedencia/plataforma de Metacritic y escala histórica de Rating; las estimaciones siguen excluidas.',
                '- Función de las organizaciones de Team: los nombres no acreditan que sean desarrolladores.',
                '- Grupos con n<20 y sesgo por ausencias: los resultados representan los pares/casos disponibles.',
                '- Codo de k-distancia, grupo dominante, ruido y estabilidad frente a otras muestras y parámetros.',
                '- Interpretaciones de nombres y ejemplos: no son etiquetas de éxito comercial ni pruebas de causalidad.',
                '- No usar notas para predecir estas etiquetas sin reconocer la circularidad de su construcción.', '']
    (informes / 'clustering.md').write_text('\n'.join(bloques), encoding='utf-8')


if __name__ == '__main__':
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument('--raiz', type=Path, default=RAIZ, help='Raíz del proyecto; por defecto se deriva del archivo.')
    ejecutar(analizador.parse_args().raiz)

````

## 04_modelo.py

Ruta: `Final/src/04_modelo.py` · Bytes: 27386 · SHA-256: `c68c4ea59027dd3fcfa04600c39dd1a0eefcece63e684f4288fec172b23b9023`

````text
"""Modelo de popularidad. Desde Final: python src/04_modelo.py."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import platform
import sys
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parents[1]
if not __package__:
    sys.path.insert(0, str(RAIZ))

import cloudpickle
import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report,
                             confusion_matrix, f1_score)
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold, GroupShuffleSplit
from sklearn.naive_bayes import CategoricalNB
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler, KBinsDiscretizer
from sklearn.tree import DecisionTreeClassifier

from src.config import FEATURES, SEED
from src.features import CategoriasFrecuentes, lista_cruda
from src.objetivo import (CAMPOS_OBJETIVO, CLASES, ajustar_referencia, aplicar_referencia,
                          ClasificadorObjetivoLocal, puntuar_objetivo_local)


def particion_agrupada(grupos):
    """Partición independiente del target; aproximadamente 80/20, sin rechazo."""
    return next(GroupShuffleSplit(n_splits=1, test_size=.2, random_state=SEED).split(np.zeros(len(grupos)), groups=grupos))


def construir_pipeline(clasificador, sin_critica=False):
    # Ninguna bandera binaria de ausencia se concatena al bloque de notas.
    if isinstance(clasificador, CategoricalNB):
        transformar_notas = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform', subsample=None)
    else:
        transformar_notas = StandardScaler()
    notas = Pipeline([('imputar', SimpleImputer(strategy='median', add_indicator=False)),
                      ('escalar', transformar_notas)])
    decada = Pipeline([('tipo', FunctionTransformer(np.asarray, kw_args={'dtype': float}, feature_names_out='one-to-one')),
                       ('imputar', SimpleImputer(strategy='constant', fill_value=-1)),
                       ('codificar', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])
    preparar = ColumnTransformer([
        ('generos', CategoriasFrecuentes(min_frecuencia=20, max_categorias=15), ['generos']),
        ('estudio', CategoriasFrecuentes(min_frecuencia=10, otro_solo_si_ninguna=True), ['estudio']),
        ('decada', decada, ['decada']),
        ('notas', notas, ['Rating'] if sin_critica else ['Metacritic Rating', 'Rating']),
    ], remainder='drop', sparse_threshold=0)
    return Pipeline([('preparar', preparar), ('clasificar', clasificador)])


def tabla_md(df):
    def valor(v):
        if isinstance(v, (float, np.floating)):
            return f'{v:.4f}'
        return str(v).replace('|', '/').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(df.columns) + ' |', '| ' + ' | '.join(['---']*len(df.columns)) + ' |',
                      *['| ' + ' | '.join(valor(v) for v in row) + ' |' for row in df.itertuples(index=False, name=None)]])


def entrenar_datos(entrada, raiz=RAIZ):
    raiz = Path(raiz)
    if any(c.startswith(('cluster_', 'componente_')) for c in entrada):
        raise ValueError('La clasificación no acepta etiquetas ni proyecciones de clustering.')
    if set(FEATURES) & set(CAMPOS_OBJETIVO):
        raise ValueError('Hay señales del objetivo dentro de los predictores.')
    df = entrada.copy()
    if 'elegible_analisis' in df:
        df = df.loc[df.elegible_analisis].copy()
    df = df.dropna(subset=CAMPOS_OBJETIVO).reset_index(drop=True)
    if 'critic_source' in df and (df['Metacritic Rating'].notna() & df.critic_source.ne('metacritic_csv')).any():
        raise ValueError('Se detectaron notas sin procedencia de prensa en las entradas.')
    if 'generos' not in df:
        df['generos'] = df.Genres.map(lista_cruda)
    else:
        df['generos'] = df.generos.map(lista_cruda)
    df['estudio'] = df['Team'].map(lista_cruda) if 'Team' in df else df['estudio'].map(lista_cruda)
    df['grupo_titulo'] = df.Title.map(lambda t: ' '.join(t.split()).casefold())
    tr, te = particion_agrupada(df.grupo_titulo.to_numpy())
    definicion = ajustar_referencia(df.iloc[tr])
    objetivo = aplicar_referencia(df, definicion)
    definicion_plays = ajustar_referencia(df.iloc[tr], 'solo_plays')
    alternativa = aplicar_referencia(df, definicion_plays)
    y = objetivo.nivel_popularidad.to_numpy()
    X = df[FEATURES].copy()
    X_train, X_test = X.iloc[tr], X.iloc[te]
    y_train, y_test = y[tr], y[te]
    grupos = df.grupo_titulo.iloc[tr].to_numpy()
    contexto = df[[*FEATURES, *CAMPOS_OBJETIVO, 'id_juego']].copy()
    if pd.Series(y_train).value_counts().min() < 10:
        raise ValueError('Cada clase de entrenamiento necesita al menos diez ejemplos para los diez pliegues.')
    cv = StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=SEED)
    # y_train solo organiza estratos; fit y score recalculan el target local del fold.
    folds = list(cv.split(X_train, y_train, groups=grupos))
    evidencia_folds = []
    asignaciones_cv = []
    for numero, (a, b) in enumerate(folds, 1):
        if not set(grupos[a]).isdisjoint(grupos[b]):
            raise ValueError('Los títulos no están separados dentro de un fold.')
        ref = ajustar_referencia(df.iloc[tr[a]])
        local_train = aplicar_referencia(df.iloc[tr[a]], ref).nivel_popularidad
        local_val = aplicar_referencia(df.iloc[tr[b]], ref).nivel_popularidad
        if set(local_val) != set(CLASES):
            raise ValueError('Un fold local no conserva las tres clases; revisar la distribución.')
        evidencia_folds.append({'fold': numero, 'ids_ajuste': df.id_juego.iloc[tr[a]].tolist(),
                                'ids_validacion': df.id_juego.iloc[tr[b]].tolist(), 'referencia': ref,
                                'distribucion_ajuste': local_train.value_counts().to_dict(),
                                'distribucion_validacion': local_val.value_counts().to_dict()})
        asignaciones_cv.extend({'id_juego': int(i), 'fold': numero, 'nivel_popularidad_local': c}
                               for i, c in zip(df.id_juego.iloc[tr[b]], local_val))
    candidatos = {
        'DummyClassifier': (DummyClassifier(strategy='most_frequent', random_state=SEED), {}),
        'CategoricalNB': (CategoricalNB(min_categories=5), {'clasificar__alpha': [.1, 1., 5.]}),
        'DecisionTreeClassifier': (DecisionTreeClassifier(random_state=SEED),
                                   {'clasificar__max_depth': [4, 8, None], 'clasificar__min_samples_leaf': [3, 10]}),
        'RandomForestClassifier': (RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=1),
                                  {'clasificar__max_depth': [8, None], 'clasificar__min_samples_leaf': [2, 5]}),
    }
    informes, modelos, limpio = raiz / 'reports', raiz / 'models', raiz / 'data/clean'
    for p in [informes, modelos, limpio]:
        p.mkdir(parents=True, exist_ok=True)
    busquedas, filas_cv, resultados = {}, [], []
    for nombre, (estimador, grid) in candidatos.items():
        grid_local = {f'pipeline__{k}': v for k, v in grid.items()}
        busqueda = GridSearchCV(ClasificadorObjetivoLocal(construir_pipeline(estimador)), grid_local, scoring=puntuar_objetivo_local, cv=folds,
                                refit=True, n_jobs=1, error_score='raise', return_train_score=False)
        busqueda.fit(contexto.iloc[tr], y_train)
        busquedas[nombre] = busqueda
        for i, parametros in enumerate(busqueda.cv_results_['params']):
            for fold in range(10):
                filas_cv.append({'modelo': nombre, 'candidato': i, 'fold': fold+1,
                                 'parametros': json.dumps(parametros, sort_keys=True),
                                 'f1_macro': float(busqueda.cv_results_[f'split{fold}_test_score'][i])})
    # La selección se cierra antes de consultar la prueba.
    mejor_nombre = max(candidatos, key=lambda n: busquedas[n].best_score_)
    mejor = busquedas[mejor_nombre].best_estimator_.pipeline_
    matrices, predicciones = {}, pd.DataFrame({'id_juego': df.id_juego.iloc[te].to_numpy(), 'real': y_test})
    for nombre, busqueda in busquedas.items():
        pred = busqueda.best_estimator_.pipeline_.predict(X_test)
        predicciones[nombre] = pred
        matriz = confusion_matrix(y_test, pred, labels=CLASES)
        matrices[nombre] = matriz.tolist()
        pd.DataFrame(matriz, index=CLASES, columns=CLASES).rename_axis('real / predicha').to_csv(informes / f'modelo_confusion_{nombre}.csv')
        resultados.append({'modelo': nombre, 'f1_macro_cv': float(busqueda.best_score_),
                           'desviacion_cv': float(busqueda.cv_results_['std_test_score'][busqueda.best_index_]),
                           'exactitud_prueba': accuracy_score(y_test, pred),
                           'f1_macro_prueba': f1_score(y_test, pred, labels=CLASES, average='macro', zero_division=0),
                           'balanced_accuracy_prueba': balanced_accuracy_score(y_test, pred),
                           'mejores_parametros': json.dumps(busqueda.best_params_, sort_keys=True)})
    tabla = pd.DataFrame(resultados)
    tabla.to_csv(informes / 'modelo_comparacion.csv', index=False)
    pd.DataFrame(filas_cv).to_csv(informes / 'modelo_grid_cv.csv', index=False)
    predicciones.to_csv(informes / 'modelo_predicciones_prueba.csv', index=False)
    importancia = permutation_importance(mejor, X_test, y_test, scoring='f1_macro', n_repeats=30, random_state=SEED, n_jobs=1)
    perm = pd.DataFrame({'variable_cruda': FEATURES, 'caida_f1_macro_media': importancia.importances_mean,
                         'desviacion': importancia.importances_std}).sort_values('caida_f1_macro_media', ascending=False)
    perm.to_csv(informes / 'modelo_permutation_importance.csv', index=False)
    pd.DataFrame(importancia.importances.T, columns=FEATURES).to_csv(informes / 'modelo_permutaciones_repeticiones.csv', index=False)
    final = tabla.set_index('modelo').loc[mejor_nombre]
    base = tabla.set_index('modelo').loc['DummyClassifier']
    diferencia = float(final.f1_macro_prueba - base.f1_macro_prueba)
    juicio = ('No supera al modelo de referencia en F1 macro de prueba.' if diferencia <= 0 else
              'Apenas supera al modelo de referencia: la mejora es de dos puntos de F1 macro o menos.' if diferencia <= .02 else
              'Supera al modelo de referencia en esta partición; no se ha probado significancia estadística de la diferencia.')
    fecha = datetime.now(ZoneInfo('America/Mexico_City')).isoformat(timespec='seconds')
    metadata = {'version_sklearn': sklearn.__version__, 'python': platform.python_version(), 'fecha': fecha,
                'zona_horaria': 'America/Mexico_City', 'semilla': SEED, 'modelo': mejor_nombre,
                'variables': FEATURES, 'clases': CLASES, 'orden_probabilidades': mejor.classes_.tolist(),
                'definicion_objetivo': definicion, 'alternativa_solo_plays': {'cortes': definicion_plays['cortes'],
                    'fraccion_etiquetas_coincidentes': float((y == alternativa.nivel_popularidad).mean())},
                'n_cohorte': len(df), 'n_entrenamiento': len(tr), 'n_prueba': len(te),
                'particion': {'test_size': .2, 'estratificada': False, 'sin_titulos_compartidos': True,
                              'regla': 'GroupShuffleSplit, una partición independiente de los conteos/etiquetas; aproximadamente 80/20 por grupos.',
                              'intentos': 1},
                'validacion': {'pliegues': 10, 'estratificada': True, 'agrupacion': 'grupo_titulo',
                               'metodo': 'StratifiedGroupKFold', 'seleccion': 'Mayor F1 macro media en CV; referencia del target y preprocesador ajustados por fold.',
                               'etiquetas_para_organizar_estratos': 'Referencia externa de entrenamiento; no se usa para fit/score de los folds.'},
                'distribuciones': {nombre: pd.Series(valores).value_counts().to_dict() for nombre, valores in [('catalogo', y), ('entrenamiento', y_train), ('prueba', y_test)]},
                'mejores_parametros': busquedas[mejor_nombre].best_params_,
                'metricas': {'exactitud': float(final.exactitud_prueba), 'f1_macro': float(final.f1_macro_prueba),
                             'balanced_accuracy': float(final.balanced_accuracy_prueba), 'f1_macro_referencia': float(base.f1_macro_prueba),
                             'diferencia_f1_referencia': diferencia, 'f1_macro_cv': float(final.f1_macro_cv),
                             'matriz_confusion': matrices[mejor_nombre],
                             'reporte_clases': classification_report(y_test, mejor.predict(X_test), labels=CLASES, output_dict=True, zero_division=0)},
                'comparacion_modelos': resultados, 'evaluacion_referencia': juicio,
                'preprocesamiento': {'generos': 'Multi-hot: hasta 15 con frecuencia >=20 en cada entrenamiento; resto/nuevos a Otro.',
                                     'estudio': 'Miembros de Team con frecuencia >=10; Otro solo si no hay miembro frecuente; no se acredita rol desarrollador.',
                                     'notas': 'Mediana ajustada en entrenamiento, sin indicadores de ausencia; scaler solo de notas, o bins para CategoricalNB.',
                                     'decada': 'Ausencia -1 y one-hot; categorías nuevas sin indicadores activos.'},
                'sha256_dataset_depurado': hashlib.sha256((limpio / 'dataset_depurado.csv').read_bytes()).hexdigest(),
                'probabilidades_calibradas': False}
    (modelos / 'metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    # Serializa las clases propias por valor: joblib.load funciona sin importar src.
    import src.features as modulo_features
    cloudpickle.register_pickle_by_value(modulo_features)
    try:
        with (modelos / 'modelo_popularidad.joblib').open('wb') as archivo:
            cloudpickle.dump(mejor, archivo)
    finally:
        cloudpickle.unregister_pickle_by_value(modulo_features)
    espacio_vecinos = mejor.named_steps['preparar'].transform(X_train)
    joblib.dump({'vecinos': NearestNeighbors(n_neighbors=5).fit(espacio_vecinos),
                 'ids': df.id_juego.iloc[tr].to_numpy()}, modelos / 'vecinos_popularidad.joblib')
    export = df.copy()
    for c in objetivo:
        export[c] = objetivo[c]
    export['particion'] = 'entrenamiento'
    export.loc[te, 'particion'] = 'prueba'
    export['fold_validacion'] = pd.Series(pd.NA, index=export.index, dtype='Int64')
    for fold, (_, validacion) in enumerate(folds, 1):
        export.loc[tr[validacion], 'fold_validacion'] = fold
    for c in ['generos', 'estudio', 'organizaciones']:
        if c in export:
            export[c] = export[c].map(lambda v: json.dumps(lista_cruda(v), ensure_ascii=False))
    export.to_csv(limpio / 'juegos_modelo.csv', index=False)
    # Entradas para otras herramientas: mismas particiones y preprocesador final.
    preparador = mejor.named_steps['preparar']
    nombres = preparador.get_feature_names_out()
    for indices, etiqueta in [(tr, 'entrenamiento'), (te, 'prueba')]:
        tabla_datos = pd.DataFrame(preparador.transform(X.iloc[indices]), columns=nombres)
        tabla_datos['nivel_popularidad'] = y[indices]
        tabla_datos.to_csv(limpio / f'{etiqueta}_orange.csv', index=False)
        lineas = ['@RELATION popularidad'] + [f'@ATTRIBUTE variable_{i} NUMERIC' for i in range(len(nombres))] + ['@ATTRIBUTE nivel_popularidad {bajo,medio,alto}', '@DATA']
        lineas += [','.join([*(format(float(v), '.12g') for v in row[:-1]), row[-1]]) for row in tabla_datos.itertuples(index=False, name=None)]
        (limpio / f'{etiqueta}_weka.arff').write_text('\n'.join(lineas), encoding='utf-8')
    pd.DataFrame({'atributo_arff': [f'variable_{i}' for i in range(len(nombres))], 'variable': nombres}).to_csv(limpio / 'diccionario_weka.csv', index=False)
    pd.DataFrame(asignaciones_cv).to_csv(informes / 'modelo_etiquetas_validacion_locales.csv', index=False)
    (modelos / 'referencias_folds.json').write_text(json.dumps(evidencia_folds, ensure_ascii=False, indent=2))
    diagnostico = diagnosticar_ausencia(mejor, X_train, y_train, X_test, y_test, informes)
    metadata['diagnostico_ausencia'] = diagnostico
    metadata['formato_artefacto'] = 'Pipeline serializado por valor con cloudpickle; compatible con joblib.load sin src en PYTHONPATH.'
    metadata['cloudpickle'] = cloudpickle.__version__
    (modelos / 'metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    escribir_reporte(informes, metadata, tabla, perm, matrices)
    print(f'Modelo guardado: {mejor_nombre}; entrenamiento={len(tr)}, prueba={len(te)}, F1 macro={final.f1_macro_prueba:.4f}; referencia={base.f1_macro_prueba:.4f}.')
    return metadata


def diagnosticar_ausencia(modelo, X_train, y_train, X_test, y_test, informes):
    c = 'Metacritic Rating'
    partes = []
    for nombre, Xp, yp in [('entrenamiento', X_train, y_train), ('prueba', X_test, y_test)]:
        t = pd.crosstab(Xp[c].isna().to_numpy(), yp, normalize='index').reindex(columns=CLASES, fill_value=0)
        t.index.name = 'critica_ausente'
        t.reset_index().assign(particion=nombre).to_csv(informes / f'modelo_ausencia_{nombre}.csv', index=False)
        z = modelo.named_steps['preparar'].transform(Xp)
        nombres = modelo.named_steps['preparar'].get_feature_names_out().tolist()
        partes.append({'particion': nombre, 'fraccion_estudio_otro': float(z[:, nombres.index('estudio__Otro')].mean())})
    conocidas = X_test[c].notna()
    original = X_test.loc[conocidas].copy()
    sin_nota = original.copy()
    sin_nota[c] = np.nan
    posicion = list(modelo.classes_).index('bajo')
    delta = modelo.predict_proba(sin_nota)[:, posicion] - modelo.predict_proba(original)[:, posicion]
    pd.DataFrame({'fila_prueba': original.index, 'cambio_probabilidad_bajo_al_ocultar_critica': delta}).to_csv(informes / 'modelo_sensibilidad_critica.csv', index=False)
    # Ablación diagnóstica, sin nueva selección ni cambio del ganador.
    from sklearn.base import clone
    ablado = construir_pipeline(clone(modelo.named_steps['clasificar']), sin_critica=True).fit(X_train, y_train)
    abla_f1 = f1_score(y_test, ablado.predict(X_test), labels=CLASES, average='macro', zero_division=0)
    return {'prevalencia_otro': partes, 'n_criticas_ocultadas': int(conocidas.sum()),
            'delta_probabilidad_bajo_media': float(delta.mean()), 'delta_probabilidad_bajo_mediana': float(np.median(delta)),
            'f1_macro_ablacion_sin_critica': float(abla_f1),
            'limitacion': 'La imputación puede seguir codificando cobertura; eliminar el indicador no garantiza ausencia de sesgo MNAR. Ablación de prueba solo diagnóstica, no reselección.'}


def escribir_reporte(informes, m, tabla, perm, matrices):
    d = m['definicion_objetivo']
    bloques = ['# Modelo supervisado corregido tras la segunda auditoría', '',
        '## Objetivo y separación de datos', '',
        'Se mantiene el índice de rangos percentiles de Plays, Wishlist y Backlogs con pesos iguales. Solo Plays es más simple, pero omite interés pendiente; el índice elegido da dos tercios del peso a dos señales de interés correlacionadas. Playing se usa en EDA/clustering, pero no en el target ni como predictor del clasificador.', '',
        f'Antes de calcular etiquetas se divide por grupos de título mediante GroupShuffleSplit con semilla 42: {m["n_entrenamiento"]} entrenamiento y {m["n_prueba"]} prueba. La proporción 80/20 es aproximada por grupos; no se fuerza estratificación en clases aún no definidas ni se buscan repartos por rechazo.', '',
        f'En entrenamiento se ajustan los rangos medios/N y sus terciles: {d["cortes"]}. La prueba se interpola contra esos mismos valores, con percentil 0 por debajo del mínimo y 1 sobre el máximo de entrenamiento. Los empates comparten etiqueta. La referencia tiene N={d["poblacion_referencia_n"]}; nunca usa los conteos de prueba.', '',
        'La CV de diez pliegues agrupa títulos y organiza estratos con las etiquetas externas de entrenamiento. Dentro de cada fit se recalculan referencia, cortes, etiquetas, categorías e imputación usando solo el subentrenamiento; score construye las etiquetas de validación con esa referencia local. GridSearchCV recibe un estimador de contexto que separa las tres señales del objetivo de las cinco entradas predictivas. Las referencias e IDs se guardan en models/referencias_folds.json.', '',
        '## Entradas y Naive Bayes', '',
        f'Predictores: {m["variables"]}. Ningún conteo, índice, cluster, componente PCA, indicador de procedencia o bandera de ausencia entra al Pipeline final.', '',
        'Géneros frecuentes: multi-hot de hasta 15 con frecuencia mínima 20 en cada ajuste. Estudio representa organizaciones de Team con mínimo 10; Otro se activa solo cuando no existe ninguna organización frecuente en la lista. Las listas vacías usan Sin dato; no se atribuye rol desarrollador por posición.', '',
        'Notas: mediana ajustada solo con entrenamiento, sin MissingIndicator. StandardScaler se aplica exclusivamente a las dos notas continuas para árboles/bosque/referencia; los otros indicadores se mantienen en 0/1. La curación de Metacritic sigue siendo una fuente posible de sesgo no aleatorio, aun sin bandera explícita.', '',
        'Se reemplaza GaussianNB por CategoricalNB: la mayoría de atributos son indicadores categóricos y las dos notas se discretizan en cinco intervalos de ancho uniforme entre los extremos de entrenamiento de cada fold. min_categories=5 permite códigos nuevos dentro del rango; alpha se ajusta en tres valores. Se reconoce pérdida de resolución por discretización e independencia condicional aproximada; no se ajustan gaussianas a decenas de dummies raras.', '',
        '## Comparación y selección', '', tabla_md(tabla), '',
        f'Ganador por F1 macro media de CV: **{m["modelo"]}**. {m["evaluacion_referencia"]} Diferencia en prueba frente a referencia: {m["metricas"]["diferencia_f1_referencia"]:.4f}. No se usa la prueba para ajustar parámetros o cambiar ganador.', '',
        f'**Limitación visible del ganador:** recall de la clase medio = {m["metricas"]["reporte_clases"]["medio"]["recall"]:.1%}. Una exactitud global razonable no permite afirmar que identifique bien esa clase; no se hizo una nueva búsqueda usando estos errores de prueba.', '',
        'Dummy usa la clase realmente más frecuente en cada ajuste, con etiquetas locales; si hay empate, sklearn desempata por orden de clases. Los terciles tienden a equilibrar por construcción incluso sin fuga, por lo que una referencia mayoritaria cercana a F1 macro 1/6 es esperable y no un modelo comercial inteligente.', '',
        '## Matrices y análisis de error por clase', '', 'Filas reales y columnas predichas: bajo, medio, alto.', '']
    errores = []
    for nombre, matriz in matrices.items():
        t = pd.DataFrame(matriz, columns=CLASES)
        t.insert(0, 'real', CLASES)
        bloques += [f'### {nombre}', '', tabla_md(t), '']
        mat = np.asarray(matriz)
        for i, c in enumerate(CLASES):
            errores.append({'modelo': nombre, 'clase': c, 'n': int(mat[i].sum()),
                            'aciertos': int(mat[i, i]), 'recall': float(mat[i, i]/mat[i].sum()) if mat[i].sum() else 0})
    errores = pd.DataFrame(errores)
    errores.to_csv(informes / 'modelo_error_por_clase.csv', index=False)
    bloques += [tabla_md(errores), '',
        'La clase media se evalúa explícitamente: sus notas y géneros pueden solaparse con ambos extremos y sus fronteras son cortes artificiales de un continuo. Es una hipótesis interpretativa, no una causa demostrada; el recall observado no se oculta bajo la exactitud global. El rendimiento de CategoricalNB se informa por clase y no se presenta la antigua matriz de GaussianNB como resultado vigente.', '',
        '## Permutation importance', '', tabla_md(perm), '',
        'Caída de F1 macro sobre la prueba al permutar cada entrada cruda (listas completas para género/estudio), con 30 repeticiones y semilla 42. No es efecto causal ni intervalo de confianza; las variables correlacionadas comparten información. No se reoptimiza después de verla.', '',
        '## Diagnóstico de cobertura de prensa y categoría Otro', '',
        json.dumps(m['diagnostico_ausencia'], ensure_ascii=False, indent=2), '',
        'Las tablas modelo_ausencia_entrenamiento/prueba.csv muestran distribución de clases con y sin crítica. modelo_sensibilidad_critica.csv cuantifica el cambio de probabilidad baja al ocultar notas conocidas manteniendo los otros datos. La ablación sin crítica reutiliza parámetros elegidos y es diagnóstica: no selecciona otro modelo ni demuestra equidad. No se concluye que un Otro frecuente causara una importancia baja solo por observar ambos.', '',
        '## Uso y reproducibilidad', '',
        'models/modelo_popularidad.joblib contiene directamente el Pipeline y acepta un DataFrame con las cinco columnas crudas, listas o textos para categorías y nulos para notas. Las clases propias se serializan por valor con cloudpickle, compatible con joblib.load desde un proceso limpio sin src en PYTHONPATH; se conserva la dependencia de versiones de sklearn/pandas/numpy/cloudpickle.', '',
        'models/metadata.json conserva referencia de entrenamiento, cortes, versiones, clases, fecha y métricas. models/vecinos_popularidad.joblib guarda NearestNeighbors ajustado únicamente al espacio predictivo de entrenamiento: las etiquetas de clusters solo se adjuntan por ID después de buscar, no intervienen en las distancias ni en la clasificación.', '',
        f'Fecha: {m["fecha"]}; sklearn {m["version_sklearn"]}; Python {m["python"]}. Las métricas previas de objetivo global están archivadas y no son directamente comparables con las nuevas.', '',
        '## Que debo verificar manualmente', '',
        '- Pesos y redundancia del índice, antigüedad y representatividad de Backloggd.',
        '- Procedencia de notas y sesgo de cobertura; la mediana puede conservar señales indirectas de ausencia.',
        '- Identidad de juegos homónimos y roles de Team; los tres conflictos históricos siguen excluidos.',
        '- Vecinos como similitud de atributos declarados, no recomendaciones de éxito ni causalidad.',
        '- Probabilidades no calibradas y límites de la clase media.', '']
    (informes / 'modelo.md').write_text('\n'.join(bloques), encoding='utf-8')


def ejecutar(raiz=RAIZ):
    raiz = Path(raiz)
    return entrenar_datos(pd.read_csv(raiz / 'data/clean/dataset_depurado.csv'), raiz)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raiz', type=Path, default=RAIZ)
    ejecutar(parser.parse_args().raiz)

````

## 05_revision_predicciones.py

Ruta: `Final/src/05_revision_predicciones.py` · Bytes: 6852 · SHA-256: `e791c3a31abef6505f13f6226d49ca03764e7c4cb5e8a9a018d3f051053f3cca`

````text
"""Audita el modelo vigente y busca mejoras solo en los pliegues de entrenamiento.

Ejecutar desde Final: python src/05_revision_predicciones.py
No sustituye el modelo de producción ni selecciona parámetros con la prueba.
"""
from pathlib import Path
import sys
RAIZ = Path(__file__).resolve().parents[1]
if not __package__:
    sys.path.insert(0, str(RAIZ))
import importlib
import json
import hashlib
import joblib
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix
from src.config import FEATURES, SEED
from src.features import lista_cruda
from src.objetivo import aplicar_referencia, ajustar_referencia, CLASES, ClasificadorObjetivoLocal


def ejecutar():
    salida = RAIZ / 'reports/revision_predicciones'
    salida.mkdir(exist_ok=True, parents=True)
    datos = pd.read_csv(RAIZ / 'data/clean/juegos_modelo.csv')
    for c in ['generos', 'estudio']:
        datos[c] = datos[c].map(lista_cruda)
    modelo = joblib.load(RAIZ / 'models/modelo_popularidad.joblib')
    meta = json.loads((RAIZ / 'models/metadata.json').read_text())
    tr = datos.loc[datos.particion.eq('entrenamiento')].copy()
    te = datos.loc[datos.particion.eq('prueba')].copy()
    assert set(tr.grupo_titulo).isdisjoint(te.grupo_titulo)
    esperado = aplicar_referencia(datos, meta['definicion_objetivo']).nivel_popularidad
    assert np.array_equal(esperado, datos.nivel_popularidad)
    pred = modelo.predict(te[FEATURES])
    prob = modelo.predict_proba(te[FEATURES])
    assert np.all(np.isfinite(prob)) and np.allclose(prob.sum(axis=1), 1)
    assert np.array_equal(pred, modelo.classes_[prob.argmax(axis=1)])
    archivo_pred = pd.read_csv(RAIZ / 'reports/modelo_predicciones_prueba.csv').set_index('id_juego')
    assert np.array_equal(pred, archivo_pred.loc[te.id_juego, meta['modelo']])
    f1 = f1_score(te.nivel_popularidad, pred, labels=CLASES, average='macro')
    assert np.isclose(f1, meta['metricas']['f1_macro'])
    nn = joblib.load(RAIZ / 'models/vecinos_popularidad.joblib')
    assert set(nn['ids']) == set(tr.id_juego)
    z = modelo.named_steps['preparar'].transform(tr[FEATURES])
    por_id = pd.DataFrame(z, index=tr.id_juego).loc[nn['ids']].to_numpy()
    assert np.allclose(por_id, nn['vecinos']._fit_X)
    ref = ajustar_referencia(tr)
    assert ref['cortes'] == meta['definicion_objetivo']['cortes']
    filas_auditoria = {'n_entrenamiento':len(tr), 'n_prueba':len(te),
        'exactitud_prueba':accuracy_score(te.nivel_popularidad,pred), 'f1_macro_prueba':f1,
        'f1_ponderado_prueba':f1_score(te.nivel_popularidad,pred,average='weighted'),
        'recall_por_clase':dict(zip(CLASES,recall_score(te.nivel_popularidad,pred,labels=CLASES,average=None))),
        'matriz_confusion':confusion_matrix(te.nivel_popularidad,pred,labels=CLASES).tolist(),
        'paridad_predicciones_guardadas':True, 'probabilidades_validas':True,
        'vecinos_solo_entrenamiento_y_mismo_espacio':True, 'objetivo_reproducido':True,
        'sha256_modelo':hashlib.sha256((RAIZ/'models/modelo_popularidad.joblib').read_bytes()).hexdigest()}
    (salida/'auditoria.json').write_text(json.dumps(filas_auditoria,ensure_ascii=False,indent=2))
    print('Auditoría de integridad completada.',flush=True)
    modulo = importlib.import_module('src.04_modelo')
    contexto = tr[[*FEATURES, 'Plays','Wishlist','Backlogs','id_juego']].reset_index(drop=True)
    folds = [(np.flatnonzero(tr.fold_validacion.to_numpy()!=n),np.flatnonzero(tr.fold_validacion.to_numpy()==n)) for n in range(1,11)]
    candidatos = {'Vigente':clone(modelo)}
    configuraciones = [
        {'min_samples_leaf':1, 'class_weight':None, 'max_features':'sqrt'},
        {'min_samples_leaf':2, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':5, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':10, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':2, 'class_weight':None, 'max_features':.5},
        {'min_samples_leaf':5, 'class_weight':'balanced_subsample', 'max_features':.5},
        {'min_samples_leaf':10, 'class_weight':None, 'max_features':.5},
    ]
    for n,c in enumerate(configuraciones,1):
        candidatos[f'RF_revision_{n}'] = modulo.construir_pipeline(RandomForestClassifier(n_estimators=200,random_state=SEED,n_jobs=1,**c))
    filas=[]
    for nombre,pipeline in candidatos.items():
        for n,(a,b) in enumerate(folds,1):
            assert set(tr.grupo_titulo.iloc[a]).isdisjoint(tr.grupo_titulo.iloc[b])
            estimador=ClasificadorObjetivoLocal(clone(pipeline)).fit(contexto.iloc[a])
            verdad=aplicar_referencia(contexto.iloc[b],estimador.referencia_).nivel_popularidad
            p=estimador.predict(contexto.iloc[b])
            filas.append({'candidato':nombre,'fold':n,'n_validacion':len(b),
                'f1_macro':f1_score(verdad,p,labels=CLASES,average='macro',zero_division=0),
                'exactitud':accuracy_score(verdad,p),
                'recall_medio':recall_score(verdad,p,labels=['medio'],average=None,zero_division=0)[0]})
        pd.DataFrame(filas).to_csv(salida/'busqueda_folds.csv',index=False)
        print(f'{nombre}: F1 CV={np.mean([f["f1_macro"] for f in filas if f["candidato"]==nombre]):.4f}',flush=True)
    tabla=pd.DataFrame(filas)
    resumen=tabla.groupby('candidato').agg(f1_macro_cv=('f1_macro','mean'),desviacion_cv=('f1_macro','std'),recall_medio_cv=('recall_medio','mean')).sort_values('f1_macro_cv',ascending=False)
    resumen.to_csv(salida/'busqueda_resumen.csv')
    ganador=resumen.index[0]
    base=tabla.loc[tabla.candidato.eq('Vigente')].sort_values('fold').f1_macro.to_numpy()
    nuevo=tabla.loc[tabla.candidato.eq(ganador)].sort_values('fold').f1_macro.to_numpy()
    mejora=float(nuevo.mean()-base.mean())
    promover=bool(ganador!='Vigente' and mejora>=.01 and (nuevo>base).sum()>=6)
    decision={'ganador_cv':ganador,'mejora_f1_cv':mejora,'pliegues_superiores':int((nuevo>base).sum()),
        'criterio_predefinido':'Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.',
        'recomienda_promocion':promover,'parametros':candidatos[ganador].named_steps['clasificar'].get_params(),
        'limitacion':'Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva.'}
    (salida/'decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2))
    print(json.dumps(decision,ensure_ascii=False),flush=True)
    return decision


if __name__=='__main__':
    ejecutar()

````

## __init__.py

Ruta: `Final/src/__init__.py` · Bytes: 45 · SHA-256: `9d9fcc3e68f3573f40a262363aae95848921cde9865bee99147f560667cfa536`

````text
"""Análisis reproducible de videojuegos."""

````

## analysis.py

Ruta: `Final/src/analysis.py` · Bytes: 698 · SHA-256: `c3c7ad613676c085eeb37ae0ebc36b984d04740f673a468533b5ed82702809d5`

````text
"""Adaptador de compatibilidad; el único clustering vive en 03_clustering.py."""
import importlib
import json
from .config import REPORTS


def grouped_correlations(df, column):
    modulo = importlib.import_module('src.03_clustering')
    d = df.rename(columns={'critica_verificada_csv': 'Metacritic Rating'}).copy()
    d['brecha'] = d['Rating'] * 20 - d['Metacritic Rating']
    return modulo.correlaciones_por_grupo(d, column).rename(columns={'pearson_r': 'r', 'pearson_p': 'p'})


def analyze(df=None):
    resultado = importlib.import_module('src.03_clustering').ejecutar()
    (REPORTS / 'analisis.json').write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
    return resultado

````

## comparar_weka.py

Ruta: `Final/src/comparar_weka.py` · Bytes: 7552 · SHA-256: `b16d4904d9da77ecfe1a3bd1dda59a7bd7bd55e28bde3342493967f46468d2a1`

````text
"""Comparación real de K-Means en Weka y sklearn sobre el mismo espacio canónico."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.request

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

RAIZ = Path(__file__).resolve().parents[1]
URLS = {
    'weka-stable-3.8.6.jar': 'https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/weka-stable/3.8.6/weka-stable-3.8.6.jar',
    'bounce-0.18.jar': 'https://repo.maven.apache.org/maven2/nz/ac/waikato/cms/weka/thirdparty/bounce/0.18/bounce-0.18.jar',
}
HUELLAS_JAR = {'weka-stable-3.8.6.jar': '932ea2f342b58fe45736389e9c426d5b5955e610d1f5f6485117f532068915e9',
               'bounce-0.18.jar': 'bffff1505335c02256b7ab2ccffbe4aa4d3ac9fe14c17557809b7c9d99d666ca'}


def ejecutar(raiz=RAIZ, descargar=False):
    raiz = Path(raiz)
    cache = raiz / '.cache/weka'
    cache.mkdir(parents=True, exist_ok=True)
    for nombre, url in URLS.items():
        destino = cache / nombre
        if not destino.exists():
            if not descargar:
                raise FileNotFoundError('Falta Weka/Bounce en .cache/weka; ejecutar este script con --descargar para obtenerlos de Maven Central.')
            urllib.request.urlretrieve(url, destino)
        if hashlib.sha256(destino.read_bytes()).hexdigest() != HUELLAS_JAR[nombre]:
            raise ValueError(f'El JAR {nombre} no coincide con la versión validada; revisar la descarga.')
    df = pd.read_csv(raiz / 'data/clean/clustering_espacio.csv')
    orden = pd.read_csv(raiz / 'data/clean/clustering_orden.csv')
    datos = df.to_numpy()
    if len(df) != len(orden) or df.shape[1] != 6 or not np.isfinite(datos).all():
        raise ValueError('Espacio de comparación inválido o IDs no alineados.')
    arff = raiz / 'data/clean/clustering_weka.arff'
    lineas = ['@RELATION clustering_canonico'] + [f'@ATTRIBUTE variable_{i} NUMERIC' for i in range(6)] + ['@DATA']
    lineas += [','.join(format(float(v), '.17g') for v in row) for row in datos]
    arff.write_text('\n'.join(lineas), encoding='utf-8')
    destino = raiz / 'reports/weka'
    destino.mkdir(parents=True, exist_ok=True)
    resultados, comandos = [], []
    for k in [2, 3, 4]:
        comando = ['java', '-Dweka.packageManager.offline=true', '-DWEKA_HOME=.cache/weka/home',
                   '-cp', '.cache/weka/*', 'weka.clusterers.SimpleKMeans', '-t', 'data/clean/clustering_weka.arff',
                   '-N', str(k), '-S', '42', '-I', '300', '-init', '1',
                   '-A', 'weka.core.EuclideanDistance -D', '-p', '0']
        ejecucion = subprocess.run(comando, cwd=raiz, text=True, capture_output=True, timeout=120)
        (destino / f'k{k}_stdout.txt').write_text(ejecucion.stdout)
        (destino / f'k{k}_stderr.txt').write_text(ejecucion.stderr)
        if ejecucion.returncode != 0:
            raise RuntimeError(f'Weka terminó con error; revisar reports/weka/k{k}_stderr.txt.')
        filas = [tuple(map(int, m.groups())) for linea in ejecucion.stdout.splitlines()
                 if (m := re.fullmatch(r'\s*(\d+)\s+(\d+)\s*', linea))]
        if [f[0] for f in filas] != list(range(len(df))):
            raise ValueError('Weka no devolvió una asignación por fila, en el orden esperado.')
        weka = np.array([f[1] for f in filas])
        python = KMeans(n_clusters=k, n_init=30, max_iter=300, random_state=42).fit_predict(datos)
        predicciones = orden.copy()
        predicciones['cluster_weka'] = weka
        predicciones['cluster_python'] = python
        predicciones.to_csv(destino / f'k{k}_asignaciones.csv', index=False)
        for herramienta, etiquetas in [('Weka 3.8.6', weka), ('sklearn', python)]:
            inercia = sum(float(np.square(datos[etiquetas == c] - datos[etiquetas == c].mean(axis=0)).sum()) for c in np.unique(etiquetas))
            resultados.append({'k': k, 'herramienta': herramienta, 'n': len(df),
                               'silhouette': silhouette_score(datos, etiquetas), 'inercia_comun': inercia,
                               'ARI_weka_python': adjusted_rand_score(weka, python),
                               'tamanos': json.dumps(pd.Series(etiquetas).value_counts().sort_index().to_dict())})
        comandos.append(comando)
    comparacion = pd.DataFrame(resultados)
    comparacion.to_csv(destino / 'comparacion.csv', index=False)
    manifest = {'java': subprocess.run(['java', '-version'], capture_output=True, text=True).stderr.strip(),
                'sha256_dataset_depurado': hashlib.sha256((raiz / 'data/clean/dataset_depurado.csv').read_bytes()).hexdigest(),
                'comandos': comandos, 'sha256_arff': hashlib.sha256(arff.read_bytes()).hexdigest(),
                'jars': {n: {'url': u, 'sha256': hashlib.sha256((cache / n).read_bytes()).hexdigest()} for n, u in URLS.items()}}
    (destino / 'ejecucion.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    columnas = comparacion.columns
    tabla = '| ' + ' | '.join(columnas) + ' |\n| ' + ' | '.join(['---']*len(columnas)) + ' |\n'
    tabla += '\n'.join('| ' + ' | '.join(str(v) for v in row) + ' |' for row in comparacion.itertuples(index=False, name=None))
    (raiz / 'reports/comparacion_weka.md').write_text(f'''# Comparación ejecutada con Weka

Ejecución local real por CLI: Weka 3.8.6 y Java, sin enviar datos a servicios externos. Las salidas originales, comandos, versiones, hashes y asignaciones por id_juego están en reports/weka. No se simula una ejecución de Orange ni una captura de su interfaz.

Ambas herramientas reciben los mismos {len(df)} casos y seis columnas ya transformadas. Weka usa EuclideanDistance -D para desactivar su normalización adicional; no recibe Title ni etiquetas ni género. Python usa 30 inicializaciones, Weka una, con k-means++ y semilla 42; los generadores y criterios de parada pueden diferir.

Silhouette e inercia se recalculan para ambas asignaciones con la misma implementación sobre el mismo espacio. ARI compara particiones sin depender del número asignado a cada cluster; no se presentan números de cluster como correspondencias automáticas.

{tabla}

Para reproducir con Java instalado: python src/comparar_weka.py --descargar. La descarga obtiene JAR de Maven Central; luego la ejecución es local. Sin --descargar requiere los JAR ya presentes en .cache/weka, excluido de Git.

Fuentes: [artefacto de Weka en Maven Central](https://central.sonatype.com/artifact/nz.ac.waikato.cms.weka/weka-stable/3.8.6) y ayuda de SimpleKMeans conservada junto a la ejecución. La comparación de Fase 4A no sustituye una comparación supervisada futura.

## Que debo verificar manualmente

- Diferencias de inicialización y convergencia antes de atribuir una mejora a la herramienta.
- Que la rúbrica admita evidencia por CLI; no se realizó una demo gráfica de Weka/Orange.
''', encoding='utf-8')
    ayuda = subprocess.run(['java', '-cp', '.cache/weka/*', 'weka.clusterers.SimpleKMeans', '-h'], cwd=raiz, capture_output=True, text=True)
    (destino / 'ayuda_simplekmeans.txt').write_text(ayuda.stdout + ayuda.stderr)
    return comparacion


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raiz', type=Path, default=RAIZ)
    parser.add_argument('--descargar', action='store_true', help='Descargar JAR faltantes de Maven Central, sin subir datos.')
    args = parser.parse_args()
    ejecutar(args.raiz, args.descargar)

````

## config.py

Ruta: `Final/src/config.py` · Bytes: 718 · SHA-256: `09d1460f1fa12ac7fff9811a4fe874c0f5de4527d8b168a250227d6655961042`

````text
"""Esquema comprobado en el archivo original; no inferido de Kaggle."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
RAW = ROOT / 'data' / 'raw' / 'games_curated.csv'
CLEAN = ROOT / 'data' / 'clean'
REPORTS = ROOT / 'reports'
MODELS = ROOT / 'models'
SIGNALS = ['Plays', 'Playing', 'Backlogs', 'Wishlist']
REQUIRED = ['ID Original', 'Title', 'Release Date', 'Team', 'Rating',
            'Times Listed', 'Number of Reviews', 'Genres', 'Summary', 'Reviews',
            *SIGNALS, 'Metacritic Rating', 'Origen_calificacion',
            'critic_score_final', 'critic_source']
FEATURES = ['generos', 'estudio', 'decada', 'Metacritic Rating', 'Rating']
LEVELS = ['bajo', 'medio', 'alto']

````

## data.py

Ruta: `Final/src/data.py` · Bytes: 1415 · SHA-256: `4f8b7a139c47ad8c54dd0c3ac578c211c897764538bd7a32855f002fcf6c182b`

````text
"""Adaptadores de la fuente canónica producida por la fase 02."""
import importlib
import json
import numpy as np
import pandas as pd
from .config import CLEAN, REPORTS, SIGNALS
from .objetivo import aplicar_referencia
from .config import MODELS


def parse_count(value):
    return importlib.import_module('src.02_limpieza').convertir_conteo(value)


def parse_list(value):
    return sorted(importlib.import_module('src.02_limpieza').interpretar_generos(value))


def load_clean():
    df = pd.read_csv(CLEAN / 'dataset_depurado.csv')
    df['generos'] = df['generos'].map(json.loads)
    df['organizaciones'] = df['Team'].map(parse_list)
    df['estudio'] = df['organizaciones']
    df['critica_verificada_csv'] = df['Metacritic Rating']
    df['popularidad_indice'] = np.nan
    elegibles = df.elegible_analisis & df[['Plays', 'Wishlist', 'Backlogs']].notna().all(axis=1)
    metadata = MODELS / 'metadata.json'
    if metadata.exists():
        referencia = json.loads(metadata.read_text())['definicion_objetivo']
        if referencia.get('version') == 'INDICE-PERCENTILES-TRAIN-2.0':
            objetivo = aplicar_referencia(df.loc[elegibles], referencia)
            df.loc[elegibles, 'popularidad_indice'] = objetivo.popularidad_indice
    return df


def prepare():
    importlib.import_module('src.02_limpieza').ejecutar()
    return load_clean(), json.loads((REPORTS / 'inspeccion.json').read_text())

````

## features.py

Ruta: `Final/src/features.py` · Bytes: 3257 · SHA-256: `3faa9dfb1cf0c771b2ccba37a6af476f1532f33cfa7983bd0e8fb408a5bf454a`

````text
"""Codificadores ajustados exclusivamente con la partición de entrenamiento."""
import numpy as np
import ast
from collections import Counter
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer


class ListEncoder(TransformerMixin, BaseEstimator):
    """Codifica cada miembro de una lista sin imponer un género o estudio principal."""
    def fit(self, X, y=None):
        self.encoder_ = MultiLabelBinarizer()
        self.encoder_.fit(X.iloc[:, 0])
        return self

    def transform(self, X):
        known = set(self.encoder_.classes_)
        return self.encoder_.transform([[v for v in row if v in known] for row in X.iloc[:, 0]])

    def get_feature_names_out(self, input_features=None):
        return np.asarray(self.encoder_.classes_, dtype=object)


def lista_cruda(valor):
    if isinstance(valor, (list, tuple)):
        lista = list(valor)
    elif pd.isna(valor) or not str(valor).strip():
        return []
    elif str(valor).strip().startswith('['):
        lista = ast.literal_eval(str(valor))
    else:
        lista = [str(valor)]
    if not isinstance(lista, list) or not all(isinstance(v, str) for v in lista):
        raise ValueError('Se esperaba una lista de categorías de texto.')
    return list(dict.fromkeys(v.strip() for v in lista if v.strip()))


class CategoriasFrecuentes(TransformerMixin, BaseEstimator):
    """Multi-hot con vocabulario entrenado dentro de cada fold; raros/nuevos a Otro."""
    def __init__(self, min_frecuencia=10, max_categorias=None, otro_solo_si_ninguna=False):
        self.min_frecuencia = min_frecuencia
        self.max_categorias = max_categorias
        self.otro_solo_si_ninguna = otro_solo_si_ninguna

    def fit(self, X, y=None):
        filas = X.iloc[:, 0] if hasattr(X, 'iloc') else np.asarray(X, dtype=object)[:, 0]
        frecuencias = Counter(v for fila in filas for v in lista_cruda(fila))
        orden = sorted(frecuencias, key=lambda c: (-frecuencias[c], c))
        self.vocabulario_ = [c for c in orden if frecuencias[c] >= self.min_frecuencia and c not in ['Otro', 'Sin dato']]
        if self.max_categorias is not None:
            self.vocabulario_ = self.vocabulario_[:self.max_categorias]
        self.frecuencias_ = dict(frecuencias)
        self.columnas_ = [*self.vocabulario_, 'Otro', 'Sin dato']
        return self

    def transform(self, X):
        filas = X.iloc[:, 0] if hasattr(X, 'iloc') else np.asarray(X, dtype=object)[:, 0]
        posiciones = {c: i for i, c in enumerate(self.vocabulario_)}
        salida = np.zeros((len(filas), len(self.columnas_)), dtype=float)
        for i, fila in enumerate(filas):
            categorias = lista_cruda(fila)
            if not categorias:
                salida[i, -1] = 1
            conocidas = [c for c in categorias if c in posiciones]
            for c in categorias:
                if c in posiciones:
                    salida[i, posiciones[c]] = 1
                elif not self.otro_solo_si_ninguna or not conocidas:
                    salida[i, len(self.vocabulario_)] = 1
        return salida

    def get_feature_names_out(self, input_features=None):
        return np.asarray(self.columnas_, dtype=object)

````

## inferencia.py

Ruta: `Final/src/inferencia.py` · Bytes: 1699 · SHA-256: `3df0a6f805057fbdfe3645671ea94907a1b2482c80fc8cff47fb10b92576fc7c`

````text
"""Contrato único del formulario con el Pipeline entrenado."""
import numpy as np
import pandas as pd
from .config import FEATURES
from .features import lista_cruda


def predecir_formulario(pipeline, generos, estudio, decada, metacritic, rating):
    """Valida escalas y devuelve entrada cruda, clase y probabilidades por nombre."""
    generos = lista_cruda(generos)
    if not generos:
        raise ValueError('Selecciona al menos un género.')
    notas = {}
    for campo, valor, limite in [('Rating', rating, 5), ('Metacritic Rating', metacritic, 100)]:
        numero = np.nan if valor is None or pd.isna(valor) else float(valor)
        if not np.isnan(numero) and (not np.isfinite(numero) or numero < 0 or numero > limite):
            raise ValueError(f'{campo} debe estar entre 0 y {limite}, o ausente.')
        notas[campo] = numero
    d = float(decada)
    if not np.isfinite(d) or d != int(d) or int(d) % 10:
        raise ValueError('La década debe ser un entero múltiplo de diez.')
    fila = pd.DataFrame([{'generos': generos, 'estudio': lista_cruda(estudio),
                          'decada': int(d), **notas}], columns=FEATURES)
    prediccion = str(pipeline.predict(fila)[0])
    valores = pipeline.predict_proba(fila)[0]
    if not np.isfinite(valores).all() or not np.isclose(valores.sum(), 1) or (valores < 0).any():
        raise ValueError('El modelo devolvió probabilidades inválidas.')
    probabilidades = {str(c):float(p) for c,p in zip(pipeline.classes_, valores)}
    if prediccion != str(pipeline.classes_[np.argmax(valores)]):
        raise ValueError('La clase estimada no coincide con la mayor probabilidad.')
    return fila, prediccion, probabilidades

````

## modeling.py

Ruta: `Final/src/modeling.py` · Bytes: 514 · SHA-256: `8a6339965efb35991a06e494a49487978b46f9559e8b476c46bf7ec57a8b78f6`

````text
"""Adaptador: la única implementación supervisada es src/04_modelo.py."""
import importlib
import numpy as np


def thresholds(scores):
    cortes = np.quantile(scores, [1/3, 2/3])
    if cortes[0] >= cortes[1]:
        raise ValueError('No se pueden definir tres niveles distintos.')
    return cortes


def levels(scores, cuts):
    return np.asarray(['bajo', 'medio', 'alto'])[np.searchsorted(cuts, scores, side='left')]


def train(df):
    return importlib.import_module('src.04_modelo').entrenar_datos(df)

````

## objetivo.py

Ruta: `Final/src/objetivo.py` · Bytes: 4390 · SHA-256: `bf07800118e1c2bd8310bbb6600b82fdaa6d037db4551531ec65cb22a5394072`

````text
"""Referencias del objetivo ajustadas únicamente con entrenamiento."""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.metrics import f1_score
from .config import FEATURES

CAMPOS_OBJETIVO = ['Plays', 'Wishlist', 'Backlogs']
CLASES = ['bajo', 'medio', 'alto']


def valores_objetivo(df):
    valores = df[CAMPOS_OBJETIVO].apply(pd.to_numeric, errors='raise')
    if valores.isna().any().any() or not np.isfinite(valores).all().all() or valores.lt(0).any().any():
        raise ValueError('Las señales del objetivo deben ser completas, finitas y no negativas.')
    return valores


def ajustar_referencia(entrenamiento, opcion='indice_percentiles'):
    valores = valores_objetivo(entrenamiento)
    if opcion not in ['indice_percentiles', 'solo_plays']:
        raise ValueError('Definición del objetivo desconocida.')
    referencias = {}
    for c in CAMPOS_OBJETIVO:
        rangos = valores[c].rank(method='average', pct=True)
        tabla = pd.DataFrame({'valor': valores[c], 'percentil': rangos}).drop_duplicates().sort_values('valor')
        referencias[c] = {'valores': tabla.valor.tolist(), 'percentiles': tabla.percentil.tolist()}
    referencia = {'version': 'INDICE-PERCENTILES-TRAIN-2.0', 'opcion': opcion,
                  'campos': CAMPOS_OBJETIVO if opcion == 'indice_percentiles' else ['Plays'],
                  'formula': '(P_train(Plays) + P_train(Wishlist) + P_train(Backlogs)) / 3' if opcion == 'indice_percentiles' else 'Plays',
                  'referencias': referencias, 'poblacion_referencia_n': len(entrenamiento),
                  'percentil': 'Rango medio/N en entrenamiento; interpolación lineal entre valores distintos, 0 bajo mínimo y 1 sobre máximo.',
                  'momento_definicion': 'Referencia y terciles ajustados solo en entrenamiento; cada fold repite el ajuste sin su validación.',
                  'clases_ordenadas': CLASES,
                  'regla': 'bajo: índice <= corte1; medio: corte1 < índice <= corte2; alto: índice > corte2'}
    indices = aplicar_referencia(entrenamiento, referencia, solo_indice=True).popularidad_indice
    cortes = np.quantile(indices, [1/3, 2/3])
    if cortes[0] >= cortes[1]:
        raise ValueError('Los empates no permiten definir tres niveles distintos.')
    referencia['cortes'] = cortes.tolist()
    return referencia


def aplicar_referencia(df, referencia, solo_indice=False):
    valores = valores_objetivo(df)
    resultado = pd.DataFrame(index=df.index)
    for c in CAMPOS_OBJETIVO:
        ref = referencia['referencias'][c]
        resultado[f'percentil_{c.lower()}'] = np.interp(valores[c], ref['valores'], ref['percentiles'], left=0, right=1)
    resultado['popularidad_indice'] = resultado.mean(axis=1) if referencia['opcion'] == 'indice_percentiles' else valores.Plays
    if not solo_indice:
        resultado['nivel_popularidad'] = np.asarray(CLASES)[np.searchsorted(referencia['cortes'], resultado.popularidad_indice, side='left')]
    return resultado


def definir_objetivo(cohorte, opcion='indice_percentiles'):
    """Conveniencia para ajustar sobre una referencia explícita, no para dividir luego."""
    referencia = ajustar_referencia(cohorte, opcion)
    return aplicar_referencia(cohorte, referencia), referencia


class ClasificadorObjetivoLocal(ClassifierMixin, BaseEstimator):
    """Contexto para GridSearchCV: las señales del target no entran al Pipeline."""
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def fit(self, X, y=None):
        self.referencia_ = ajustar_referencia(X)
        etiquetas = aplicar_referencia(X, self.referencia_).nivel_popularidad.to_numpy()
        self.pipeline_ = clone(self.pipeline).fit(X[FEATURES], etiquetas)
        self.classes_ = self.pipeline_.classes_
        self.ids_ajuste_ = X.id_juego.tolist() if 'id_juego' in X else X.index.tolist()
        return self

    def predict(self, X):
        return self.pipeline_.predict(X[FEATURES])

    def predict_proba(self, X):
        return self.pipeline_.predict_proba(X[FEATURES])

    def score(self, X, y=None):
        verdaderas = aplicar_referencia(X, self.referencia_).nivel_popularidad
        return f1_score(verdaderas, self.predict(X), labels=CLASES, average='macro', zero_division=0)


def puntuar_objetivo_local(estimador, X, y):
    return estimador.score(X)

````

## pipeline.py

Ruta: `Final/src/pipeline.py` · Bytes: 4535 · SHA-256: `aca23ce69dc620612f2bc8078b4cdc4beec4e98ddd2b8360e0f1488d2e3e9150`

````text
"""Cadena canónica: inspección → limpieza → clustering → clasificación independiente."""
import hashlib
import importlib
import json
import shutil
from .config import ROOT, RAW, REPORTS
from .data import load_clean
from .modeling import train

REPORTES_APP = (
    'clustering_03_parametros.json', 'clustering_03_correlaciones_catalogo.csv',
    'clustering_03_correlaciones_generos.csv', 'clustering_03_correlaciones_organizaciones.csv',
    'clustering_03_correlaciones_ranking_generos.csv', 'clustering_03_perfiles.csv',
    'clustering_03_alternativas_k.csv', 'clustering_03_seleccion_kmeans.csv',
    'clustering_03_sensibilidad_dbscan.csv',
)


def huella_pipeline():
    rutas = [RAW, ROOT / 'data/historical/games_actualizado_metacritic.csv', ROOT / 'requirements.txt', *sorted((ROOT / 'src').glob('*.py'))]
    h = hashlib.sha256()
    for ruta in rutas:
        if ruta.exists():
            h.update(str(ruta.relative_to(ROOT)).encode())
            h.update(ruta.read_bytes())
    return h.hexdigest()


def main():
    importlib.import_module('src.01_inspeccion').ejecutar()
    importlib.import_module('src.02_limpieza').ejecutar()
    parametros = importlib.import_module('src.03_clustering').ejecutar()
    if (ROOT / '.cache/weka/weka-stable-3.8.6.jar').exists() and shutil.which('java'):
        from .comparar_weka import ejecutar
        ejecutar()
    # Fase supervisada: solo datos depurados; nunca etiquetas ni scaler de clusters.
    metricas = train(load_clean())
    (REPORTS / 'analisis.json').write_text(json.dumps(parametros, ensure_ascii=False, indent=2))
    texto = f"""# Hallazgos de la cadena canónica

Fuente maestra: data/raw/games_curated.csv, sin modificar. Historia de 1,512 registros y decisiones heredadas: trazabilidad_historica.md.
La inspección, limpieza, clustering y app comparten dataset_depurado.csv y dataset_con_clusters.csv. El análisis completo de asociación está en clustering.md, con mínimo de 20 pares por grupo.

Fase 4A: {parametros['n_completos']} casos completos elegibles de {parametros['n_entrada']} registros conservados; {parametros['n_conflictos_historicos']} conflictos históricos pendientes excluidos del análisis principal.
K-Means usa seis variables y k={parametros['kmeans_k']} entre 2 y 10. DBSCAN usa eps={parametros['dbscan_eps']:.6f}, min_samples={parametros['dbscan_min_samples']}; clusters={parametros['dbscan_clusters']}, ruido={parametros['dbscan_ruido']}.
Un solo grupo de DBSCAN no acredita segmentación comercial útil. Ver comparación de k=2/3/4 y sensibilidad a títulos compartidos en clustering.md.

Clasificador independiente por terciles del promedio de rangos percentiles de Plays, Wishlist y Backlogs: {metricas['modelo']}; n prueba={metricas['n_prueba']}, F1 macro={metricas['metricas']['f1_macro']:.4f}, base={metricas['metricas']['f1_macro_referencia']:.4f}. Los clusters descriptivos no se utilizan como objetivo ni predictores.

## Que debo verificar manualmente

- Resolver plataformas de discrepancias históricas y roles de Team.
- Interpretar distancias de puntuaciones separadas de asociación de orden.
- Confirmar estabilidad de perfiles; popularidad no equivale a éxito comercial.
"""
    (REPORTS / 'hallazgos.md').write_text(texto, encoding='utf-8')
    manifest = {'huella_pipeline': huella_pipeline(), 'fuente_clustering': 'data/clean/dataset_depurado.csv',
                'artefacto_clustering': 'data/clean/dataset_con_clusters.csv',
                'modelo_popularidad': 'models/modelo_popularidad.joblib',
                'metadata_modelo': 'models/metadata.json',
                'sha256_modelo_popularidad': hashlib.sha256((ROOT / 'models/modelo_popularidad.joblib').read_bytes()).hexdigest(),
                'sha256_metadata_modelo': hashlib.sha256((ROOT / 'models/metadata.json').read_bytes()).hexdigest(),
                'sha256_vecinos': hashlib.sha256((ROOT / 'models/vecinos_popularidad.joblib').read_bytes()).hexdigest(),
                'sha256_dataset_depurado': hashlib.sha256((ROOT / 'data/clean/dataset_depurado.csv').read_bytes()).hexdigest(),
                'sha256_dataset_con_clusters': hashlib.sha256((ROOT / 'data/clean/dataset_con_clusters.csv').read_bytes()).hexdigest(),
                'sha256_reportes_app': {nombre: hashlib.sha256((REPORTS / nombre).read_bytes()).hexdigest()
                                       for nombre in REPORTES_APP}}
    (REPORTS / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    print(texto)


if __name__ == '__main__':
    main()

````

## procedencia.py

Ruta: `Final/src/procedencia.py` · Bytes: 8666 · SHA-256: `99a7f75372627638bffec4d16070f66cea0e6a584e9c716788107a6ae48fc9e1`

````text
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

````

## similitud.py

Ruta: `Final/src/similitud.py` · Bytes: 783 · SHA-256: `251232ca02ef085037050c37c5a68ce0257a772b1ff1bf83cc8b9fd46602d73c`

````text
"""Vecinos descriptivos exclusivamente en el espacio predictivo de entrenamiento."""
import joblib
import numpy as np
import pandas as pd
from .config import CLEAN, MODELS


def cinco_vecinos(fila, pipeline):
    bundle = joblib.load(MODELS / 'vecinos_popularidad.joblib')
    espacio = pipeline.named_steps['preparar'].transform(fila)
    distancias, posiciones = bundle['vecinos'].kneighbors(espacio, n_neighbors=5)
    resultado = pd.DataFrame({'id_juego': np.asarray(bundle['ids'])[posiciones[0]], 'distancia': distancias[0]})
    catalogo = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
    return resultado.merge(catalogo[['id_juego', 'Title', 'Release Date', 'cluster_kmeans', 'cluster_dbscan']],
                           on='id_juego', how='left', validate='one_to_one')

````

## ui.py

Ruta: `Final/src/ui.py` · Bytes: 26081 · SHA-256: `c9da4cb356e5f43fda63e58e2d4eeacd8d74891032254ebdd76efd50a41f3d59`

````text
"""Módulo UI/UX Persona 5 (Port fiel de PruebasMenu/persona5-website-theme) y caché de artefactos."""
import base64
import hashlib
import json
import unicodedata
import textwrap
from pathlib import Path

import joblib
import pandas as pd
import plotly.graph_objects as go
import sklearn
import streamlit as st
import streamlit.components.v1 as components

from .config import CLEAN, MODELS, RAW, REPORTS, ROOT
from .data import load_clean
from .visualizacion import PALETA, COLORWAY

ASSETS = ROOT / 'assets'
FONTS_DIR = ASSETS / 'fonts'
AUDIO_DIR = ASSETS / 'audio'
IMG_DIR = ASSETS / 'img'
CSS_DIR = ASSETS / 'css'

P5_COLORS = {
    'black': PALETA['bg-primary'], 'surface': PALETA['bg-panel'],
    'red': PALETA['primary'], 'dark_red': PALETA['bg-chart'],
    'white': PALETA['text-primary'], 'gray': PALETA['text-secondary'],
    'yellow': PALETA['accent'], 'cyan': PALETA['primary'],
}
P5_COLORWAY = COLORWAY
_UI_VERSION = 'p5-v8-neon'


def _p5_ascii(text: str) -> str:
    """Conserva tildes y signos admitidos por la fuente cómic local."""
    return unicodedata.normalize('NFC', str(text))


def clean_html(raw_html: str) -> str:
    """Compacta HTML multilínea eliminando sangrías y líneas vacías para evitar bloques <pre><code> en Markdown."""
    return '\n'.join(line.strip() for line in str(raw_html).splitlines() if line.strip())


def render_html(raw_html: str) -> None:
    """Renderiza HTML en Streamlit de forma segura sin que CommonMark interprete sangrías como código."""
    st.markdown(clean_html(raw_html), unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def asset_b64(rel_path: str) -> str:
    """Codifica un archivo de assets/ en Base64 usando pathlib.Path relativo a ROOT."""
    ruta = ASSETS / Path(rel_path)
    if not ruta.exists():
        return ''
    return base64.b64encode(ruta.read_bytes()).decode('ascii')


@st.cache_data(show_spinner=False)
def _build_global_css(css_hash: str, font_hash: str) -> str:
    """Construye el tema con la fuente cómic local y caché ligada a sus bytes."""
    font_b64 = base64.b64encode((FONTS_DIR / 'Persona5main.ttf').read_bytes()).decode('ascii')
    font_face = ''
    if font_b64:
        font_face = (
            "@font-face { font-family: 'ComicProyecto'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; } "
            "@font-face { font-family: 'Persona5Main'; "
            f"src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype'); "
            "font-weight: normal; font-style: normal; font-display: swap; }"
        )
    css_file = CSS_DIR / 'persona5.css'
    base_css = css_file.read_text(encoding='utf-8') if css_file.exists() else ''
    tokens = ':root {' + ''.join(f'--{k}: {v};' for k, v in PALETA.items()) + '}'
    return f'<style>{font_face}\n{tokens}\n{base_css}</style>'


def inject_p5_css() -> None:
    """Inyecta el tema visual Persona 5 y la tipografía Base64 en la vista actual."""
    css_file = CSS_DIR / 'persona5.css'
    css_hash = hashlib.sha256(css_file.read_bytes()).hexdigest() if css_file.exists() else 'v0'
    font_hash = hashlib.sha256((FONTS_DIR / 'Persona5main.ttf').read_bytes()).hexdigest()
    st.markdown(_build_global_css(css_hash, font_hash), unsafe_allow_html=True)


def render_page_transition(variant: str = 'default') -> None:
    """Renderiza las cortinas de transición animadas exactas de PageTransition.jsx."""
    if variant == 'about':
        panels = [
            (PALETA['bg-primary'], '-12vh', '-18vw', '86vw', '0s', 999),
            (PALETA['text-primary'], '24vh', '-10vw', '72vw', '0.05s', 998),
            (PALETA['text-primary'], '58vh', '-14vw', '82vw', '0.10s', 997),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-panel" style="background:{c};top:{t};left:{l};width:{w};animation-delay:{d};z-index:{z};"></div>'
            for c, t, l, w, d, z in panels
        )
    elif variant == 'resume':
        cards = [
            ('14vh', PALETA['bg-chart'], '0s', 'none', 999),
            ('31vh', PALETA['text-primary'], '0.05s', '10px 0 0 #00CFFF', 998),
            ('48vh', PALETA['text-primary'], '0.10s', '10px 0 0 #00CFFF', 997),
            ('65vh', PALETA['bg-chart'], '0.15s', 'none', 996),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-card" style="top:{t};background:{c};animation-delay:{d};box-shadow:{sh};z-index:{z};"></div>'
            for t, c, d, sh, z in cards
        )
    else:
        stripes = [
            (PALETA['bg-primary'], '72vw', '24vw', '0s', 999),
            (PALETA['primary'], '80vw', '14vw', '0.06s', 998),
            (PALETA['text-primary'], '88vw', '8vw', '0.12s', 997),
        ]
        items_html = ''.join(
            f'<div class="p5-trans-stripe" style="background:{c};left:{l};width:{w};animation-delay:{d};z-index:{z};"></div>'
            for c, l, w, d, z in stripes
        )

    render_html(
        f"""
        <div class="p5-stripe" aria-hidden="true"></div>
        <div class="p5-stripe2" aria-hidden="true"></div>
        <div class="p5-transition-layer" aria-hidden="true">{items_html}</div>
        """
    )


def render_p5_main_menu(active_idx: int = 0, compact: bool = False) -> None:
    """Renderiza el único menú principal estilo P5Menu.jsx exclusivamente dentro de la barra lateral izquierda."""
    items = [
        {'idx': 0, 'label': 'INICIO',      'font': 38, 'ox': 6,  'oy': 0, 'sx': -6, 'sy': 6},
        {'idx': 1, 'label': 'EXPLORACION', 'font': 24, 'ox': 4, 'oy': 6, 'sx': -9, 'sy': -5},
        {'idx': 2, 'label': 'PREDICCION',  'font': 26, 'ox': 4, 'oy': 6, 'sx': -3, 'sy': -3},
        {'idx': 3, 'label': 'MODELO',      'font': 38, 'ox': 12, 'oy': 6, 'sx': -5, 'sy': 5},
    ]

    joker_b64 = asset_b64('img/P5_Joker_Chain_Chronicle_1.png')
    art_html = (
        f'<img class="p5-stage-art" src="data:image/png;base64,{joker_b64}" alt=""/>'
        if joker_b64 else ''
    )

    rutas = ['/', '/Exploracion', '/Prediccion', '/Acerca_del_modelo']
    rows_html = ''
    for i, item in enumerate(items):
        is_act = 'active' if i == active_idx else ''
        fs = item['font']
        ox = item['ox']
        oy = item['oy']
        delay = i * 80
        rows_html += (
            f'<a href="{rutas[i]}" target="_self" class="p5-row {is_act}" aria-label="{item["label"]}" data-nav-index="{item["idx"]}" '
            f'style="margin-left:{ox}px;margin-top:{oy}px;animation-delay:{delay}ms;">'
            f'<div class="p5-glow"></div>'
            f'<div class="p5-skew-wrap" style="transform:skewX({item["sx"]}deg) skewY({item["sy"]}deg);">'
            f'<div class="p5-shadow-tri"></div>'
            f'<div class="p5-highlight"></div>'
            f'<div class="p5-label-wrap">'
            f'<span class="p5-label-base p5-label-dark" style="font-size:{fs}px;">{item["label"]}</span>'
            f'<span class="p5-label-base p5-label-bright" aria-hidden="true" style="font-size:{fs}px;">{item["label"]}</span>'
            f'</div>'
            f'</div>'
            f'</a>'
        )

    html_block = (
        f'<div class="p5-menu-stage">'
        f'{art_html}'
        f'<div class="p5-name-tag">'
        f'<span>Phantom\'s</span>'
        f'<span>persona</span>'
        f'</div>'
        f'<nav class="p5-menu" aria-label="Persona 5 Sidebar Menu">'
        f'{rows_html}'
        f'</nav>'
        f'<div class="p5-hint">'
        f'<span class="p5-hint-key">HOVER</span><span>SELECT</span>'
        f'<span class="p5-hint-key">CLICK</span><span>GO</span>'
        f'</div>'
        f'</div>'
    )
    with st.sidebar:
        render_html(html_block)


def render_lb_rb_nav(label: str) -> None:
    """Renderiza el cabezal animado ◄ LB [LABEL] RB ► de Socials.jsx / AboutMe.jsx."""
    clean_label = _p5_ascii(label)
    render_html(
        f"""
        <div class="sc-right-nav-bar">
            <span class="sc-nav-arrow left">◄</span>
            <span class="sc-nav-btn">LB</span>
            <span class="sc-nav-label">{clean_label}</span>
            <span class="sc-nav-btn">RB</span>
            <span class="sc-nav-arrow right">►</span>
        </div>
        """
    )


def _inject_parent_interactive_engine() -> None:
    """Inyecta en window.parent el motor de audio (BGM fade 450ms + select.mp3) y eventos de menús P5."""
    select_b64 = asset_b64('audio/select.mp3')
    bgm_b64 = ''
    # Para BGM pesado (7.7 MB), solo lo inyectamos una vez en window.parent para no repetir transferencia
    bgm_path = AUDIO_DIR / 'background.mp3'
    if bgm_path.exists() and not st.session_state.get('_p5_bgm_injected', False):
        bgm_b64 = base64.b64encode(bgm_path.read_bytes()).decode('ascii')
        st.session_state['_p5_bgm_injected'] = True

    motor_interactivo = (ASSETS / "js/interacciones.js").read_text(encoding="utf-8")
    sfx_desactivado = json.dumps(not st.session_state.get('p5_sfx_toggle', True))
    js_code = f"""
    <script>
    (function() {{
      const doc = window.parent.document;
      const win = window.parent;
      win.__p5SfxDisabled = {sfx_desactivado};

      // 1. Registrar select.mp3 y playSelectSound() idéntico a src/utils/audio.js
      if ("{select_b64}" && !win.__p5SelectSrc) {{
        win.__p5SelectSrc = "data:audio/mp3;base64,{select_b64}";
      }}
      if ("{bgm_b64}" && !win.__p5BgmSrc) {{
        win.__p5BgmSrc = "data:audio/mp3;base64,{bgm_b64}";
      }}

      win.playSelectSound = function() {{
        if (win.__p5SfxDisabled) return;
        if (!win.__p5SelectSrc) return;
        try {{
          const a = new win.Audio(win.__p5SelectSrc);
          a.volume = 0.5;
          a.play().catch(function(){{}});
        }} catch (e) {{}}
      }};

      // 2. Montar el panel flotante .bgm-panel de App.jsx en window.parent.document.body
      if (!doc.getElementById('p5-floating-bgm-panel') && win.__p5BgmSrc) {{
        const BGM_STATE_KEY = 'p5-bgm-enabled';
        const BGM_VOLUME_KEY = 'p5-bgm-volume';
        const FADE_MS = 450;
        let savedVol = parseFloat(win.localStorage.getItem(BGM_VOLUME_KEY));
        if (!Number.isFinite(savedVol)) savedVol = 0.45;
        savedVol = Math.min(1, Math.max(0, savedVol));

        const panel = doc.createElement('div');
        panel.id = 'p5-floating-bgm-panel';
        panel.className = 'bgm-panel';
        panel.innerHTML = `
          <audio id="p5-bgm-audio" loop preload="none" src="${{win.__p5BgmSrc}}"></audio>
          <button id="p5-bgm-toggle-btn" class="bgm-toggle" type="button">BGM OFF</button>
          <div class="bgm-slider-wrap" aria-label="Background music volume">
            <span class="bgm-slider-label">VOL</span>
            <input id="p5-bgm-vol-slider" class="bgm-slider" type="range" min="0" max="1" step="0.01" value="${{savedVol}}" />
            <span id="p5-bgm-vol-val" class="bgm-slider-value">${{Math.round(savedVol * 100)}}</span>
          </div>
        `;
        doc.body.appendChild(panel);

        const audio = panel.querySelector('#p5-bgm-audio');
        const btn = panel.querySelector('#p5-bgm-toggle-btn');
        const slider = panel.querySelector('#p5-bgm-vol-slider');
        const valSpan = panel.querySelector('#p5-bgm-vol-val');
        let isPlaying = false;
        let fadeRaf = null;

        function stopFade() {{
          if (fadeRaf) {{
            win.cancelAnimationFrame(fadeRaf);
            fadeRaf = null;
          }}
        }}

        function fadeTo(target, done) {{
          stopFade();
          const start = audio.volume;
          const diff = target - start;
          const begin = win.performance.now();
          function tick(now) {{
            const p = Math.min(1, (now - begin) / FADE_MS);
            audio.volume = Math.min(1, Math.max(0, start + diff * p));
            if (p < 1) {{
              fadeRaf = win.requestAnimationFrame(tick);
              return;
            }}
            fadeRaf = null;
            if (done) done();
          }}
          fadeRaf = win.requestAnimationFrame(tick);
        }}

        btn.addEventListener('click', function() {{
          win.playSelectSound();
          if (isPlaying) {{
            fadeTo(0, function() {{
              audio.pause();
              audio.currentTime = 0;
              isPlaying = false;
              btn.classList.remove('on');
              btn.textContent = 'BGM OFF';
              win.localStorage.setItem(BGM_STATE_KEY, '0');
            }});
          }} else {{
            stopFade();
            audio.volume = 0;
            audio.play().then(function() {{
              fadeTo(parseFloat(slider.value));
              isPlaying = true;
              btn.classList.add('on');
              btn.textContent = 'BGM ON';
              win.localStorage.setItem(BGM_STATE_KEY, '1');
            }}).catch(function(){{}});
          }}
          btn.blur();
        }});

        slider.addEventListener('input', function(e) {{
          const v = parseFloat(e.target.value);
          valSpan.textContent = String(Math.round(v * 100));
          if (isPlaying) audio.volume = v;
          win.localStorage.setItem(BGM_VOLUME_KEY, String(v));
        }});
      }}

      {motor_interactivo}
    }})();
    </script>
    """
    components.html(js_code, height=0, width=0)


def render_sidebar_audio() -> None:
    """Controles de audio compactos en barra lateral sincronizados con el panel flotante BGM."""
    with st.sidebar:
        icon_b64 = asset_b64('img/icon1.png')
        icon_html = (
            f'<img src="data:image/png;base64,{icon_b64}" width="22" '
            f'style="vertical-align:middle;margin-right:6px;" alt="P5"/>'
            if icon_b64 else ''
        )
        render_html(
            f"""
            <div style="border-top:2px solid #00CFFF;padding-top:0.65rem;margin-top:0.2rem;margin-bottom:0.4rem;">
                <div class="p5-font" style="font-size:1.05rem;color:var(--accent);letter-spacing:0.06em;">
                    {icon_html}PHANTOM SOUND
                </div>
            </div>
            """
        )
        sfx_on = st.toggle('SFX de menú (select.mp3)', value=True, key='p5_sfx_toggle')
        bgm_on = st.toggle('Reproductor BGM alternativo', value=False, key='p5_bgm_toggle')
        if bgm_on:
            bgm_path = AUDIO_DIR / 'background.mp3'
            if bgm_path.exists():
                st.audio(bgm_path.read_bytes(), format='audio/mp3', loop=True, autoplay=True)
        if sfx_on and st.session_state.pop('_trigger_select_sfx', False):
            sfx_b64 = asset_b64('audio/select.mp3')
            if sfx_b64:
                render_html(
                    f'<audio autoplay style="display:none">'
                    f'<source src="data:audio/mp3;base64,{sfx_b64}" type="audio/mp3">'
                    f'</audio>'
                )


def trigger_select_sfx() -> None:
    """Marca la reproducción del efecto select.mp3 tras presionar un botón principal."""
    st.session_state['_trigger_select_sfx'] = True


def render_critical_alert(detalle: str) -> None:
    """Pantalla de error temática ('CRITICAL ALERT / MISSION FAILED') cuando faltan artefactos."""
    inject_p5_css()
    char_b64 = asset_b64('img/jokerface2.png')
    img_html = (
        f'<img src="data:image/png;base64,{char_b64}" width="110" '
        f'style="float:right;margin-left:1rem;filter:drop-shadow(4px 4px 0 #000);" alt="Alert"/>'
        if char_b64 else ''
    )
    render_html(
        f"""
        <div class="p5-critical-alert">
            {img_html}
            <div class="p5-critical-title">CRITICAL ALERT // MISSION FAILED</div>
            <p style="font-size:1.05rem;color:var(--text-primary);margin-bottom:0.6rem;">
                No se encontraron o no pudieron validarse los artefactos de datos o modelos requeridos para iniciar el Observatorio Phantom Thieves.
            </p>
            <p style="font-family:monospace;background:var(--bg-primary);padding:0.6rem 0.9rem;border:1px solid #00CFFF;color:var(--accent);">
                Detalle técnico: {detalle}
            </p>
            <p style="font-size:0.98rem;color:var(--text-primary);margin-top:0.8rem;margin-bottom:0.3rem;">
                <strong>Instrucciones de recuperación:</strong> Ejecuta el pipeline de entrenamiento desde la carpeta <code>Final/</code>:
            </p>
            <pre style="background:#000000;color:var(--accent);padding:0.75rem;border:2px solid #F5F7FF;">cd Final · python -m src.pipeline · streamlit run app.py</pre>
        </div>
        """
    )
    st.error(
        f'CRITICAL ALERT / MISSION FAILED — {detalle}. '
        'Ejecuta `python -m src.pipeline` desde la carpeta `Final/` y recarga la página.'
    )


@st.cache_data(show_spinner=False)
def load_curated_datasets(depurado_hash: str, clusters_hash: str, metadata_hash: str):
    """Carga datasets (games_curated.csv, dataset_depurado.csv y dataset_con_clusters.csv) en caché de datos."""
    df_clean = load_clean()
    df_clusters = pd.read_csv(CLEAN / 'dataset_con_clusters.csv')
    curated_path = CLEAN / 'games_curated.csv'
    if not curated_path.exists():
        curated_path = RAW
    df_raw = pd.read_csv(curated_path)
    analysis = json.loads((REPORTS / 'clustering_03_parametros.json').read_text(encoding='utf-8'))
    return df_clean, df_clusters, df_raw, analysis


@st.cache_data(show_spinner=False)
def load_metadata(metadata_hash: str) -> dict:
    """Carga models/metadata.json con @st.cache_data."""
    return json.loads((MODELS / 'metadata.json').read_text(encoding='utf-8'))


@st.cache_resource(show_spinner=False)
def load_model_artifacts(model_hash: str, vecinos_hash: str, metadata_hash: str) -> dict:
    """Carga modelos pesados (scikit-learn, joblib y estimador NearestNeighbors) con @st.cache_resource."""
    pipeline = joblib.load(MODELS / 'modelo_popularidad.joblib')
    vecinos = joblib.load(MODELS / 'vecinos_popularidad.joblib')
    metricas = load_metadata(metadata_hash)
    return {'pipeline': pipeline, 'vecinos': vecinos, 'metricas': metricas}


def _file_sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resources():
    """Valida y retorna (df_depurado, bundle_modelo, parametros_clustering) usando cachés separadas."""
    from .pipeline import REPORTES_APP, huella_pipeline
    rutas = [
        REPORTS / 'manifest.json',
        CLEAN / 'dataset_depurado.csv',
        CLEAN / 'dataset_con_clusters.csv',
        MODELS / 'modelo_popularidad.joblib',
        MODELS / 'metadata.json',
        MODELS / 'vecinos_popularidad.joblib',
        *[REPORTS / nombre for nombre in REPORTES_APP],
    ]
    estado = tuple(
        (ruta.name, hashlib.sha256(ruta.read_bytes()).hexdigest() if ruta.exists() else None)
        for ruta in rutas
    )
    try:
        return _resources(huella_pipeline(), estado)
    except (ValueError, FileNotFoundError, ImportError, OSError, KeyError) as error:
        render_critical_alert(str(error))
        st.stop()


@st.cache_resource(show_spinner=False)
def _resources(huella, estado):
    """Valida integridad o delega a cachés de datos (@st.cache_data) y modelos (@st.cache_resource)."""
    from .pipeline import REPORTES_APP, main
    requeridos = [
        RAW,
        CLEAN / 'dataset_depurado.csv',
        CLEAN / 'dataset_con_clusters.csv',
        MODELS / 'modelo_popularidad.joblib',
        MODELS / 'metadata.json',
        MODELS / 'vecinos_popularidad.joblib',
        *[REPORTS / nombre for nombre in REPORTES_APP],
    ]
    faltantes = [str(r.relative_to(ROOT)) for r in requeridos if not r.exists()]
    if faltantes:
        raise FileNotFoundError(f"Archivos requeridos faltantes: {', '.join(faltantes)}")

    # Comprobar el manifiesto antes de deserializar: las claves de caché detectan
    # cambios, pero por sí solas no acreditan que los archivos concuerden.
    manifest = json.loads((REPORTS / 'manifest.json').read_text(encoding='utf-8'))
    artefactos = {'modelo_popularidad': MODELS / 'modelo_popularidad.joblib',
                 'metadata_modelo': MODELS / 'metadata.json',
                 'vecinos': MODELS / 'vecinos_popularidad.joblib',
                 'dataset_depurado': CLEAN / 'dataset_depurado.csv',
                 'dataset_con_clusters': CLEAN / 'dataset_con_clusters.csv'}
    for nombre, ruta in artefactos.items():
        if manifest.get(f'sha256_{nombre}') != _file_sha256(ruta):
            raise ValueError(f'Integridad incorrecta en {ruta.relative_to(ROOT)}; no se cargarán artefactos discordantes.')
    for nombre in REPORTES_APP:
        if manifest.get('sha256_reportes_app', {}).get(nombre) != _file_sha256(REPORTS / nombre):
            raise ValueError(f'El reporte {nombre} no coincide con el manifiesto.')

    dep_hash = _file_sha256(CLEAN / 'dataset_depurado.csv') or ''
    clu_hash = _file_sha256(CLEAN / 'dataset_con_clusters.csv') or ''
    mod_hash = _file_sha256(MODELS / 'modelo_popularidad.joblib') or ''
    vec_hash = _file_sha256(MODELS / 'vecinos_popularidad.joblib') or ''
    meta_hash = _file_sha256(MODELS / 'metadata.json') or ''

    metricas = load_metadata(meta_hash)
    if metricas.get('version_sklearn') != sklearn.__version__:
        main()
        mod_hash = _file_sha256(MODELS / 'modelo_popularidad.joblib') or ''
        vec_hash = _file_sha256(MODELS / 'vecinos_popularidad.joblib') or ''
        meta_hash = _file_sha256(MODELS / 'metadata.json') or ''

    df_clean, _, _, analysis = load_curated_datasets(dep_hash, clu_hash, meta_hash)
    bundle = load_model_artifacts(mod_hash, vec_hash, meta_hash)
    return df_clean, bundle, analysis


def setup(
    title: str,
    subtitle: str = 'Backloggd · muestra curada de videojuegos · análisis minería de datos',
    transition: str = 'default',
    menu_idx: int = 0,
    compact_menu: bool = True,
) -> None:
    """Configura la página con transiciones PageTransition.jsx, menú único en barra lateral P5Menu.jsx y motor de audio."""
    st.set_page_config(
        page_title=f'{title} · P5 Data Observatory',
        page_icon='🎭',
        layout='wide',
        initial_sidebar_state='expanded',
    )
    inject_p5_css()
    render_page_transition(transition)
    render_p5_main_menu(active_idx=menu_idx, compact=compact_menu)
    render_sidebar_audio()
    st.title(_p5_ascii(title))
    st.caption(subtitle)
    _inject_parent_interactive_engine()


def section_banner(title: str, subtitle: str = '') -> None:
    """Renderiza un banner inclinado estilo cómic Persona 5."""
    clean_title = _p5_ascii(title)
    sub_html = f'<div class="p5-banner-sub">{subtitle}</div>' if subtitle else ''
    render_html(
        f"""
        <div class="p5-banner">
            <div class="p5-banner-title">{clean_title}</div>
            {sub_html}
        </div>
        """
    )


def p5_plotly_layout(fig: go.Figure, title: str = '', height: int = 430) -> go.Figure:
    """Aplica el tema personalizado Persona 5 a cualquier figura de Plotly."""
    lineas_titulo = textwrap.wrap(_p5_ascii(title).upper(), width=56) if title else []
    fig.update_layout(
        title=dict(
            text='<br>'.join(lineas_titulo),
            font=dict(family='ComicProyecto, sans-serif', size=18, color=PALETA['text-primary']),
            x=0.01,
        ),
        paper_bgcolor=PALETA['bg-chart-deep'],
        plot_bgcolor=PALETA['bg-chart'],
        font=dict(family='ComicProyecto, sans-serif', size=13, color=PALETA['text-primary']),
        colorway=P5_COLORWAY,
        height=height,
        margin=dict(l=64, r=32, t=35 + 26 * len(lineas_titulo) if title else 28, b=64),
        legend=dict(
            bgcolor=PALETA['bg-panel'],
            bordercolor=PALETA['primary'],
            borderwidth=1,
            font=dict(color=PALETA['text-primary'], size=12),
        ),
        hoverlabel=dict(
            bgcolor=PALETA['bg-primary'],
            bordercolor=PALETA['primary'],
            font=dict(family='ComicProyecto, sans-serif', size=13, color=PALETA['text-primary']),
        ),
    )
    fig.update_xaxes(
        gridcolor=PALETA['grid-color'],
        zerolinecolor=PALETA['purple-deep'],
        linecolor=PALETA['primary'],
        tickfont=dict(color=PALETA['text-secondary']),
        automargin=True,
        title_font=dict(family='ComicProyecto, sans-serif', size=16, color=PALETA['accent']),
    )
    fig.update_yaxes(
        gridcolor=PALETA['grid-color'],
        zerolinecolor=PALETA['purple-deep'],
        linecolor=PALETA['primary'],
        tickfont=dict(color=PALETA['text-secondary']),
        automargin=True,
        title_font=dict(family='ComicProyecto, sans-serif', size=16, color=PALETA['accent']),
    )
    # Solo etiquetas de potencias de diez: evita dígitos menores amontonados.
    for eje in list(fig.select_xaxes()) + list(fig.select_yaxes()):
        if eje.type == 'log':
            eje.update(dtick=1, tickformat='~s', minor=dict(showgrid=False, ticks=''))
    return fig


def manual_checks() -> None:
    """Expander de verificación metodológica manual."""
    with st.expander('Qué debo verificar manualmente (Protocolo de Auditoría)'):
        st.write(
            'Confirma escala de Rating (0–5 vs 0–100), procedencia y plataforma de Metacritic, '
            'roles de Team (desarrollador vs publisher), fecha de captura de Backloggd, '
            'versiones multiplataforma y licencia antes de interpretar o redistribuir.'
        )


@st.cache_data(show_spinner=False)
def _cached_report(name: str, file_hash: str) -> pd.DataFrame:
    return pd.read_csv(REPORTS / name)


def read_report(name: str) -> pd.DataFrame:
    """Lee un CSV de reports/ con @st.cache_data invalidado por hash de contenido."""
    ruta = REPORTS / name
    if not ruta.exists():
        raise FileNotFoundError(f'No existe el reporte {ruta.relative_to(ROOT)}')
    return _cached_report(name, _file_sha256(ruta) or '')

````

## visualizacion.py

Ruta: `Final/src/visualizacion.py` · Bytes: 2184 · SHA-256: `7008c52adbb14e66db73df60ed0207f28a3a57ed9e1860abd29e902d9f212344`

````text
"""Tokens y etiquetas compartidos; no transforma datos ni escalas estadísticas."""

PALETA = {
    'bg-primary': '#050D22', 'bg-panel': '#15254A',
    'bg-chart': '#170D37', 'bg-chart-deep': '#100B29',
    'primary': '#00CFFF', 'secondary': '#8B9CFF',
    'purple-neon': '#A56BFF', 'purple-deep': '#6D42D8',
    'accent': '#FFD166', 'text-primary': '#F5F7FF',
    'text-secondary': '#C8CDEB', 'border-primary': '#00CFFF',
    'border-purple': '#A56BFF', 'grid-color': 'rgba(165, 107, 255, 0.18)',
}
COLOR_SENALES = { 'Plays': PALETA['primary'], 'Backlogs': PALETA['secondary'], 'Wishlist': PALETA['accent'] }
COLORWAY = [PALETA[k] for k in ('primary', 'secondary', 'accent', 'purple-neon', 'purple-deep')]


def etiquetas_fuera_del_error(fig, indice_traza=0, desplazamiento_categoria=0.0, sufijo=''):
    """Ubica cada cifra más allá del extremo positivo de su barra de error.

    El desplazamiento categórico reproduce la posición del grupo de barras;
    los 10 píxeles adicionales separan texto e intervalo a cualquier escala.
    """
    traza = fig.data[indice_traza]
    horizontal = traza.orientation == 'h'
    valores = traza.x if horizontal else traza.y
    categorias = traza.y if horizontal else traza.x
    error = traza.error_x if horizontal else traza.error_y
    errores = error.array if error.array is not None else [0.0] * len(valores)
    traza.text = None
    for i, (valor, categoria, desviacion) in enumerate(zip(valores, categorias, errores)):
        extremo = float(valor) + float(desviacion)
        etiqueta = f'{float(valor):.4f}{sufijo}' if horizontal else f'{float(valor):.3f}{sufijo}'
        fig.add_annotation(
            x=extremo if horizontal else i + desplazamiento_categoria,
            y=categoria if horizontal else extremo,
            text=etiqueta, showarrow=False,
            xanchor='left' if horizontal else 'center',
            yanchor='middle' if horizontal else 'bottom',
            xshift=10 if horizontal else 0, yshift=0 if horizontal else 10,
            font=dict(family='ComicProyecto, sans-serif', size=13, color=PALETA['text-primary']),
            bgcolor=PALETA['bg-chart'], borderpad=2,
        )
    return fig

````

