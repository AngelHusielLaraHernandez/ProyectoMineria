"""Correlaciones, perfiles y gráficos descriptivos, sin inferencia causal."""
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.cluster import DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from .config import CLEAN, REPORTS, MODELS, SIGNALS, SEED


def correlation_row(group, name):
    pairs = group[['Rating', 'critica_verificada_csv']].dropna()
    n = len(pairs)
    result = {'grupo': name, 'n': n, 'r': np.nan, 'p': np.nan,
              'ic95_inferior': np.nan, 'ic95_superior': np.nan,
              'media_rating': pairs['Rating'].mean(),
              'media_critica': pairs['critica_verificada_csv'].mean()}
    if n >= 10 and pairs.nunique().min() > 1:
        estimate = pearsonr(pairs['Rating'], pairs['critica_verificada_csv'])
        ci = estimate.confidence_interval(confidence_level=.95)
        result.update(r=float(estimate.statistic), p=float(estimate.pvalue),
                      ic95_inferior=float(ci.low), ic95_superior=float(ci.high))
    return result


def grouped_correlations(df, column):
    exploded = df.explode(column).dropna(subset=[column])
    out = pd.DataFrame([correlation_row(g, name) for name, g in exploded.groupby(column)])
    out['q_bh'] = np.nan
    valid = out['p'].dropna().sort_values()
    if len(valid):
        adjusted = np.minimum.accumulate((valid.to_numpy() * len(valid) / np.arange(1, len(valid)+1))[::-1])[::-1]
        out.loc[valid.index, 'q_bh'] = np.minimum(adjusted, 1)
    return out.sort_values(['n', 'grupo'], ascending=[False, True])


def analyze(df):
    global_r = correlation_row(df, 'Todos')
    pd.DataFrame([global_r]).to_csv(REPORTS / 'pearson_global.csv', index=False)
    for column in ['generos', 'organizaciones']:
        grouped_correlations(df, column).to_csv(REPORTS / f'pearson_{column}.csv', index=False)
    # La brecha no se calcula sin confirmar la escala; Pearson no requiere igualarla.
    fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
    ax.scatter(df['critica_verificada_csv'], df['Rating'], alpha=.3, s=20, color='#17645b')
    ax.set(xlabel='Metacritic según procedencia del CSV', ylabel='Rating de usuarios (escala original)',
           title=f'Usuarios y prensa · n={global_r["n"]} · r={global_r["r"]:.3f}')
    fig.savefig(REPORTS / 'figures' / 'usuarios_critica.png', dpi=160)
    plt.close(fig)
    eligible = df.dropna(subset=SIGNALS).copy()
    scaler = StandardScaler()
    values = scaler.fit_transform(np.log1p(eligible[SIGNALS]))
    km_trials, km_models = [], {}
    for k in range(2, 9):
        model = KMeans(n_clusters=k, random_state=SEED, n_init=20).fit(values)
        score = silhouette_score(values, model.labels_)
        km_trials.append({'k': k, 'silhouette': score, 'inercia': model.inertia_})
        km_models[k] = model
    table = pd.DataFrame(km_trials)
    best_k = int(table.loc[table['silhouette'].idxmax(), 'k'])
    eligible['kmeans'] = km_models[best_k].labels_
    table.to_csv(REPORTS / 'seleccion_kmeans.csv', index=False)
    db_trials, db_models = [], {}
    for eps in [.2, .35, .5, .7, 1.0]:
        for min_samples in [5, 10, 20]:
            model = DBSCAN(eps=eps, min_samples=min_samples).fit(values)
            mask = model.labels_ != -1
            clusters = len(set(model.labels_[mask]))
            coverage = float(mask.mean())
            sil = float(silhouette_score(values[mask], model.labels_[mask])) if 1 < clusters < mask.sum() else np.nan
            # Penaliza ruido y exige que al menos 70 % de la muestra esté agrupada.
            score = sil * coverage if coverage >= .7 and np.isfinite(sil) else np.nan
            db_trials.append({'eps': eps, 'min_samples': min_samples, 'clusters': clusters,
                              'cobertura': coverage, 'silhouette_sin_ruido': sil, 'criterio': score})
            db_models[(eps, min_samples)] = model
    db_table = pd.DataFrame(db_trials)
    candidates = db_table.dropna(subset=['criterio'])
    if len(candidates):
        chosen = candidates.loc[candidates['criterio'].idxmax()]
    else:
        # No se presenta este resultado como una partición de calidad validada.
        chosen = db_table.loc[(db_table['eps'].eq(.5)) & db_table['min_samples'].eq(10)].iloc[0]
    db_model = db_models[(float(chosen['eps']), int(chosen['min_samples']))]
    eligible['dbscan'] = db_model.labels_
    db_table.to_csv(REPORTS / 'seleccion_dbscan.csv', index=False)
    pca = PCA(n_components=2, random_state=SEED).fit(values)
    projection = pca.transform(values)
    eligible[['componente_1', 'componente_2']] = projection
    cols = ['ID Original', 'Title', *SIGNALS, 'popularidad_indice', 'kmeans', 'dbscan', 'componente_1', 'componente_2']
    eligible[cols].to_csv(CLEAN / 'perfiles.csv', index=False)
    for method in ['kmeans', 'dbscan']:
        summary = eligible.groupby(method)[SIGNALS + ['popularidad_indice']].median()
        summary.insert(0, 'n', eligible.groupby(method).size())
        summary.to_csv(REPORTS / f'perfiles_{method}.csv')
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout='constrained')
    for ax, method in zip(axes, ['kmeans', 'dbscan']):
        ax.scatter(projection[:, 0], projection[:, 1], c=eligible[method], cmap='viridis', s=12, alpha=.65)
        ax.set(title=method.upper(), xlabel='Componente 1', ylabel='Componente 2')
    fig.savefig(REPORTS / 'figures' / 'perfiles.png', dpi=160)
    plt.close(fig)
    MODELS.mkdir(exist_ok=True)
    import joblib
    joblib.dump({'scaler': scaler, 'kmeans': km_models[best_k], 'dbscan': db_model,
                 'pca': pca, 'senales': SIGNALS}, MODELS / 'clusters.joblib')
    result = {'pearson_global': global_r, 'kmeans_k': best_k,
              'dbscan': {k: float(v) for k, v in chosen.to_dict().items()},
              'dbscan_criterio_valido': bool(len(candidates)),
              'pca_varianza_explicada': pca.explained_variance_ratio_.tolist(),
              'filas_agrupadas': len(eligible)}
    (REPORTS / 'analisis.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result
