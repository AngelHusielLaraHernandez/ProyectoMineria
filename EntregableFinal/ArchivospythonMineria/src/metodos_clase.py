"""Comparación reproducible de Ward y K-Means en el espacio de agrupamiento."""

import json
from pathlib import Path

import pandas as pd
from scipy.cluster.hierarchy import cut_tree, dendrogram, linkage
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score, silhouette_score

from .config import ROOT


def evaluar_ward(raiz=ROOT):
    raiz = Path(raiz)
    limpio, informes = raiz / 'data/clean', raiz / 'reports'
    espacio = pd.read_csv(limpio / 'clustering_espacio.csv')
    orden = pd.read_csv(limpio / 'clustering_orden.csv')
    perfiles = pd.read_csv(limpio / 'dataset_con_clusters.csv').set_index('id_juego')
    assert len(orden) == len(espacio) and orden.id_juego.is_unique
    arbol = linkage(espacio, method='ward', metric='euclidean')

    def metricas(metodo, etiquetas):
        return dict(metodo=metodo, k=len(set(etiquetas)),
                    silhouette=silhouette_score(espacio, etiquetas),
                    davies_bouldin=davies_bouldin_score(espacio, etiquetas),
                    calinski_harabasz=calinski_harabasz_score(espacio, etiquetas))

    cortes = {k: cut_tree(arbol, n_clusters=k).ravel() for k in range(2, 11)}
    candidatos = pd.DataFrame(metricas('Ward', etiquetas) for etiquetas in cortes.values())
    k = int(candidatos.sort_values(['silhouette', 'k'], ascending=[False, True]).iloc[0].k)
    elegidos = cortes[k]
    etiquetas_kmeans = perfiles.loc[orden.id_juego, 'cluster_kmeans'].astype(int)
    comparacion = pd.DataFrame([metricas('K-Means', etiquetas_kmeans), metricas('Ward', elegidos)])
    comparacion.to_csv(informes / 'clase_comparacion_clustering.csv', index=False)
    candidatos.to_csv(informes / 'clase_ward_cortes.csv', index=False)
    asignaciones = orden[['id_juego']].assign(cluster_ward=elegidos)
    asignaciones.to_csv(informes / 'clase_ward_asignaciones.csv', index=False)
    grupos = perfiles.loc[orden.id_juego, espacio.columns].assign(cluster=elegidos).groupby('cluster')
    grupos.mean().assign(n=grupos.size()).reset_index().to_csv(informes / 'clase_ward_perfiles.csv', index=False)

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Se muestran las últimas fusiones. Las hojas indican cuántos juegos representan.
    figura, eje = plt.subplots(figsize=(9, 3.6), layout='constrained')
    ramas = dendrogram(arbol, truncate_mode='lastp', p=12, show_leaf_counts=True,
                       color_threshold=0, above_threshold_color='#17645b', ax=eje)
    eje.set(xlabel='Ramas (entre paréntesis, número de juegos)', ylabel='Distancia de Ward')
    (informes / 'figures').mkdir(exist_ok=True)
    figura.savefig(informes / 'figures/clase_ward_dendrograma.png', dpi=160)
    plt.close(figura)
    (informes / 'clase_ward_dendrograma.json').write_text(json.dumps({
        'k': k, 'n': len(orden), 'x': ramas['icoord'], 'y': ramas['dcoord'],
        'hojas': ramas['ivl'],
    }))
    return comparacion
