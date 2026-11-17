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
