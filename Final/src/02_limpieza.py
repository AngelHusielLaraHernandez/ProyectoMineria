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
    tablas = informes / 'tables'
    tablas.mkdir(exist_ok=True)
    dimensiones = [{'etapa': 'Anteproyecto', 'filas': 1512, 'columnas': 15,
                    'evidencia': 'Proyecto/main.tex. Dimensiones declaradas, sin el CSV exacto para cotejo.'}]
    if historia['estado'] != 'sin antecedente':
        antecedente = pd.read_csv(raiz / 'data/historical/games_actualizado_metacritic.csv')
        dimensiones.append({'etapa': 'Antecedente enriquecido', 'filas': len(antecedente), 'columnas': len(antecedente.columns),
                            'evidencia': 'CSV local. Incluye procedencia de crítica y cuatro estimaciones financieras o comerciales.'})
        dimensiones.append({'etapa': 'Reconstrucción del maestro', 'filas': historia['filas_maestro'],
                            'columnas': historia['columnas_reconstruidas'],
                            'evidencia': f"{historia['descartes_heredados']} descartes heredados por título y fecha. Columnas derivadas de calendario, listas, notas, logaritmos y banderas."})
    dimensiones.extend([
        {'etapa': 'Maestro curado', 'filas': len(datos) + len(descartados),
         'columnas': len(pd.read_csv(entrada, nrows=0).columns), 'evidencia': 'CSV designado como original para el pipeline actual.'},
        {'etapa': 'Depurado actual', 'filas': len(datos), 'columnas': len(datos.columns), 'evidencia': 'Salida de la fase de limpieza.'},
    ])
    pd.DataFrame(dimensiones).to_csv(tablas / 'procedencia_datos.csv', index=False)
    with (informes / 'limpieza_log.md').open('a', encoding='utf-8') as archivo:
        archivo.write('\n## Dimensiones y linaje del insumo\n\n')
        archivo.write('| Etapa | Filas | Columnas | Evidencia |\n|---|---:|---:|---|\n')
        for fila in dimensiones:
            archivo.write(f"| {fila['etapa']} | {fila['filas']} | {fila['columnas']} | {fila['evidencia']} |\n")
        archivo.write('\nEl maestro curado es un archivo distinto del insumo de 15 columnas descrito en el anteproyecto. El origen exacto de las adiciones entre esa versión y el antecedente de 20 columnas no está documentado. La conciliación verificable comienza en el antecedente local. Los campos económicos estimados se excluyen de las conclusiones y del modelo.\n')
    if entrada.read_bytes() != contenido:
        raise RuntimeError('La fuente cambió durante la ejecución; revisar antes de usar las salidas.')
    print(f'Limpieza completada: {bitacora.inicial} → {len(datos)} juegos; {len(largo)} pertenencias de género. Ver reports/limpieza_log.md.')
    return datos, largo, bitacora


if __name__ == '__main__':
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument('--raiz', type=Path, default=RAIZ, help='Raíz del proyecto; por defecto se deriva de este archivo.')
    ejecutar(analizador.parse_args().raiz)
