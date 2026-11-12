"""Tablas de popularidad y validación interna de perfiles."""
from importlib import import_module
import json

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score, silhouette_score
from sklearn.mixture import GaussianMixture
from threadpoolctl import threadpool_limits

from .config import ROOT, SEED

fase = import_module('src.03_clustering')


def resumir_popularidad(cohorte, columna):
    grupos = cohorte.explode(columna).dropna(subset=[columna]).drop_duplicates(['id_juego', columna])
    filas = []
    for nombre, grupo in grupos.groupby(columna):
        if len(grupo) < 20:
            continue
        fila = {'grupo': nombre, 'n_juegos': len(grupo)}
        for variable in fase.VARIABLES:
            x = grupo[variable]
            fila.update({f'n_{variable}': x.count(), f'media_{variable}': x.mean(), f'mediana_{variable}': x.median()})
        pares = fase.asociacion(grupo, grupo=nombre)
        fila.update({k: v for k, v in pares.items() if k in
                     ['n', 'pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']})
        if pares['n'] < 20:
            for clave in ['pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']:
                fila[clave] = np.nan
        filas.append(fila)
    return pd.DataFrame(filas).sort_values(['n_juegos', 'grupo'], ascending=[False, True])


def metricas(espacio, etiquetas, metodo, **datos):
    etiquetas = np.asarray(etiquetas)
    validos = etiquetas != -1
    k = len(set(etiquetas[validos]))
    fila = dict(metodo=metodo, k=k, n_evaluado=int(validos.sum()), ruido=int((~validos).sum()), **datos)
    if 2 <= k < validos.sum():
        x, y = espacio[validos], etiquetas[validos]
        fila.update(silhouette=silhouette_score(x, y), calinski_harabasz=calinski_harabasz_score(x, y),
                    davies_bouldin=davies_bouldin_score(x, y))
    return fila


def ejecutar(raiz=ROOT):
    informes, limpio = raiz / 'reports', raiz / 'data/clean'
    tablas = informes / 'tables'
    tablas.mkdir(exist_ok=True)
    for nombre in ('catalogo', 'generos', 'organizaciones', 'senales'):
        fuente = informes / f'clustering_03_correlaciones_{nombre}.csv'
        pd.read_csv(fuente).to_csv(tablas / f'correlacion_{nombre}.csv', index=False)
    for nombre in ['clustering_03_alternativas_k.csv', 'clase_ward_asignaciones.csv',
                   'clase_comparacion_clustering.csv', 'clase_ward_cortes.csv',
                   'clustering_03_perfiles.csv', 'clustering_03_correlaciones_ranking_generos.csv']:
        (tablas / nombre).write_bytes((informes / nombre).read_bytes())
    weka = informes / 'weka/comparacion.csv'
    if weka.exists():
        (tablas / 'weka_clustering_cli.csv').write_bytes(weka.read_bytes())
    depurado = pd.read_csv(limpio / 'dataset_depurado.csv')
    catalogo = {'n': len(depurado), 'anio_min': int(depurado.anio.min()), 'anio_max': int(depurado.anio.max())}
    for origen, clave in [('generos', 'generos'), ('Team', 'organizaciones')]:
        frecuencias = depurado[origen].map(fase.lista).explode().dropna().value_counts()
        catalogo[f'n_{clave}'] = len(frecuencias)
        catalogo[f'top_{clave}'] = [{'grupo': k, 'n': int(v)} for k, v in frecuencias.head(3).items()]
    (tablas / 'catalogo_resumen.json').write_text(json.dumps(catalogo, ensure_ascii=False, indent=2) + '\n')
    cohorte = depurado.loc[depurado.elegible_analisis].copy()
    cohorte['_generos'] = cohorte.generos.map(fase.lista)
    cohorte['_organizaciones'] = cohorte.Team.map(fase.lista)
    for columna, archivo in [('_generos', 'genero'), ('_organizaciones', 'estudio')]:
        resumir_popularidad(cohorte, columna).to_csv(tablas / f'popularidad_{archivo}.csv', index=False)

    orden = pd.read_csv(limpio / 'clustering_orden.csv')
    espacio = pd.read_csv(limpio / 'clustering_espacio.csv').to_numpy()
    salida = pd.read_csv(limpio / 'dataset_con_clusters.csv').set_index('id_juego').loc[orden.id_juego].reset_index()
    salida['cluster_ward'] = pd.read_csv(informes / 'clase_ward_asignaciones.csv').set_index('id_juego').loc[orden.id_juego, 'cluster_ward'].to_numpy()
    salida['_generos'] = salida.generos.map(fase.lista)
    parametros = json.loads((informes / 'clustering_03_parametros.json').read_text())
    pd.DataFrame([dict(parametros, pca_varianza_total=sum(parametros['pca_varianza']))]).to_csv(tablas / 'parametros_clustering.csv', index=False)
    elegidos = {'K-Means': 'cluster_kmeans', 'Ward': 'cluster_ward', 'DBSCAN': 'cluster_dbscan'}
    cuadros = []
    for metodo, columna in elegidos.items():
        perfiles, muestras = fase.describir_perfiles(salida, espacio, salida[columna].to_numpy(), metodo)
        ejemplos = muestras.groupby('cluster').juego.agg(' | '.join).rename('juegos_ejemplo')
        cuadros.append(perfiles.join(ejemplos, on='cluster'))
    pd.concat(cuadros).to_csv(tablas / 'perfiles_clusters.csv', index=False)
    salida[['id_juego', 'Title', 'componente_1', 'componente_2', *elegidos.values()]].to_csv(
        tablas / 'pca_clusters.csv', index=False)

    filas = pd.read_csv(informes / 'clase_ward_cortes.csv').assign(n_evaluado=len(espacio), ruido=0).to_dict('records')
    bic = []
    with threadpool_limits(limits=1):
        for k in range(1, 11):
            gmm = GaussianMixture(n_components=k, n_init=5, random_state=SEED).fit(espacio)
            bic.append({'k': k, 'bic': gmm.bic(espacio), 'convergio': gmm.converged_})
            if k >= 2:
                km = KMeans(n_clusters=k, n_init=30, random_state=SEED).fit(espacio)
                filas.append(metricas(espacio, km.labels_, 'K-Means', inercia=km.inertia_))
        for factor in [.8, 1., 1.2]:
            eps = parametros['dbscan_eps'] * factor
            min_samples = parametros['dbscan_min_samples']
            labels = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(espacio)
            filas.append(metricas(espacio, labels, 'DBSCAN', factor_eps=factor, eps=eps, min_samples=min_samples))
    pd.DataFrame(filas).to_csv(tablas / 'metricas_clusters.csv', index=False)
    pd.DataFrame(bic).to_csv(tablas / 'bic_gmm.csv', index=False)

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ejes = plt.subplots(1, 3, figsize=(12, 4), sharex=True, sharey=True, layout='constrained')
    for ax, (metodo, columna) in zip(ejes, elegidos.items()):
        for cluster, puntos in salida.groupby(columna):
            ax.scatter(puntos.componente_1, puntos.componente_2, s=8, alpha=.55,
                       label='Ruido' if cluster == -1 else f'Grupo {int(cluster)}')
        ax.set(title=metodo, xlabel='Componente principal 1')
        ax.legend()
    ejes[0].set_ylabel('Componente principal 2')
    fig.savefig(informes / 'figures/pca_tres_metodos.png', dpi=160)
    plt.close(fig)
    texto = (informes / 'clustering.md').read_text()
    encabezado = '## Validación de los tres métodos y popularidad por grupo'
    texto = texto.split(encabezado)[0].rstrip()
    (informes / 'clustering.md').write_text(f"""{texto}

{encabezado}

- `tables/metricas_clusters.csv` contiene silueta, Calinski–Harabasz y Davies–Bouldin para K-Means y Ward entre 2 y 10 grupos. DBSCAN se explora variando eps con min_samples fijo. Su k es el número observado de grupos. Se excluye ruido de las métricas internas y quedan vacías si hay menos de dos grupos.
- `tables/bic_gmm.csv` evalúa mezclas gaussianas de 1 a 10 componentes. El BIC mide ajuste penalizado de la mezcla y sirve como diagnóstico complementario. El k operativo de K-Means y Ward sigue la silueta.
- `tables/perfiles_clusters.csv` muestra tamaño, medias, géneros dominantes y ejemplos en los tres métodos. `tables/pca_clusters.csv` y `figures/pca_tres_metodos.png` muestran sus etiquetas sobre la misma proyección exploratoria.
- `tables/popularidad_genero.csv` y `tables/popularidad_estudio.csv` excluyen grupos de menos de 20 juegos elegibles. Cada variable tiene su propio n observado, media y mediana. Pearson y Spearman comparan las dos notas cuando hay al menos 20 pares válidos. Team identifica organizaciones mencionadas y un juego puede pertenecer a varios grupos.
""", encoding='utf-8')


if __name__ == '__main__':
    ejecutar()
