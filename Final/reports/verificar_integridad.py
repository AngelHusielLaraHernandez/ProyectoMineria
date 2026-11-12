"""Comprobación independiente; desde Final: python reports/verificar_integridad.py."""
from pathlib import Path
import hashlib
import json
import sys

import joblib
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, log_loss, cohen_kappa_score, roc_auc_score
from sklearn.preprocessing import StandardScaler

raiz = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(raiz))
from src.evaluacion_anidada import METRICAS, contrastar
from src.pipeline import huella_pipeline
from src.objetivo import ajustar_referencia

limpio = pd.read_csv(raiz / 'data/clean/dataset_depurado.csv')
clusters = pd.read_csv(raiz / 'data/clean/dataset_con_clusters.csv')
juegos = pd.read_csv(raiz / 'data/clean/juegos_modelo.csv')
meta = json.loads((raiz / 'models/metadata.json').read_text())
manifest = json.loads((raiz / 'reports/manifest.json').read_text())
salida = {}

original = raiz.parent / 'Proyecto/data/processed/games_curated.csv'
maestro = raiz / 'data/raw/games_curated.csv'
assert hashlib.sha256(maestro.read_bytes()).hexdigest() == 'b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd'
if original.exists():
    assert original.read_bytes() == maestro.read_bytes()
salida['original_intacto'] = True

archivos = {'modelo_popularidad': 'models/modelo_popularidad.joblib',
            'metadata_modelo': 'models/metadata.json', 'vecinos': 'models/vecinos_popularidad.joblib',
            'dataset_depurado': 'data/clean/dataset_depurado.csv',
            'dataset_con_clusters': 'data/clean/dataset_con_clusters.csv'}
for clave, ruta in archivos.items():
    assert hashlib.sha256((raiz / ruta).read_bytes()).hexdigest() == manifest['sha256_' + clave], ruta
for nombre, huella in manifest['sha256_reportes_app'].items():
    assert hashlib.sha256((raiz / 'reports' / nombre).read_bytes()).hexdigest() == huella, nombre
assert manifest['huella_pipeline'] == huella_pipeline()
salida['artefactos_y_reportes_concuerdan'] = True

assert len(limpio) == len(clusters) == 1117
assert limpio.id_juego.is_unique and clusters.id_juego.is_unique
campos = ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Rating', 'Metacritic Rating']
mascara = limpio.elegible_analisis & limpio[campos].notna().all(axis=1)
assert set(clusters.loc[clusters.incluido_clustering, 'id_juego']) == set(limpio.loc[mascara, 'id_juego'])
assert clusters.loc[~clusters.incluido_clustering, ['cluster_kmeans', 'cluster_dbscan']].isna().all().all()
assert set(limpio.loc[~limpio.elegible_analisis, 'id_juego']) == {117, 140, 296}
assert not set(juegos.id_juego) & {117, 140, 296}
# Rating / 5 * 100 y Rating * 20 pueden diferir por redondeo de coma flotante.
np.testing.assert_allclose(limpio.brecha, limpio.Rating * 20 - limpio['Metacritic Rating'], equal_nan=True, atol=1e-10)
salida['filas_y_brecha'] = {'conservadas': len(limpio), 'agrupadas': int(mascara.sum()), 'no_agrupadas': int((~mascara).sum())}

pares = limpio.loc[limpio.elegible_analisis, ['Rating', 'Metacritic Rating']].dropna()
r, p = pearsonr(pares.Rating, pares['Metacritic Rating'])
rho, ps = spearmanr(pares.Rating, pares['Metacritic Rating'])
guardado = pd.read_csv(raiz / 'reports/clustering_03_correlaciones_catalogo.csv').iloc[0]
assert int(guardado['n']) == len(pares)
np.testing.assert_allclose([r, p, rho, ps], guardado[['pearson_r', 'pearson_p', 'spearman_rho', 'spearman_p']].astype(float), rtol=1e-10, atol=0)
salida['correlacion_recalculada'] = {'n': len(pares), 'pearson_r': float(r), 'pearson_p': float(p), 'spearman_rho': float(rho), 'spearman_p': float(ps)}

bundle = joblib.load(raiz / 'models/clustering_03.joblib')
x = clusters.loc[clusters.incluido_clustering, campos].copy()
conteos = campos[:4]
x[conteos] = np.log1p(x[conteos])
z = StandardScaler().fit_transform(x)
np.testing.assert_allclose(z, pd.read_csv(raiz / 'data/clean/clustering_espacio.csv'), atol=1e-12)
np.testing.assert_array_equal(bundle['kmeans'].predict(z), clusters.loc[clusters.incluido_clustering, 'cluster_kmeans'].astype(int))
np.testing.assert_array_equal(bundle['dbscan'].labels_, clusters.loc[clusters.incluido_clustering, 'cluster_dbscan'].astype(int))
salida['clusters_y_espacio_concordantes'] = True

prueba = juegos[juegos.particion.eq('prueba')].copy()
entrenamiento = juegos[juegos.particion.eq('entrenamiento')]
assert set(prueba.grupo_titulo).isdisjoint(entrenamiento.grupo_titulo)
for campo in ['generos', 'estudio']:
    prueba[campo] = prueba[campo].map(json.loads)
modelo = joblib.load(raiz / 'models/modelo_popularidad.joblib')
pred = modelo.predict(prueba[meta['variables']])
f1 = f1_score(prueba.nivel_popularidad, pred, average='macro')
acc = accuracy_score(prueba.nivel_popularidad, pred)
np.testing.assert_allclose([f1, acc], [meta['metricas']['f1_macro'], meta['metricas']['exactitud']])
np.testing.assert_array_equal(confusion_matrix(prueba.nivel_popularidad, pred, labels=meta['clases']), meta['metricas']['matriz_confusion'])
salida['metricas_recalculadas'] = {'n_prueba': len(prueba), 'f1_macro': f1, 'exactitud': acc}
tablas = raiz / 'reports/tables'
proba = modelo.predict_proba(prueba[meta['variables']])
np.testing.assert_allclose(proba.sum(axis=1), 1)
uno_hot = np.asarray(prueba.nivel_popularidad)[:, None] == modelo.classes_[None, :]
metricas = {
    'exactitud_pct': 100 * acc, 'f1_macro': f1,
    'f1_ponderado': f1_score(prueba.nivel_popularidad, pred, average='weighted'),
    'kappa': cohen_kappa_score(prueba.nivel_popularidad, pred),
    'roc_auc_ovr': roc_auc_score(prueba.nivel_popularidad, proba, multi_class='ovr'),
    'brier_multiclase': np.mean(np.sum((proba - uno_hot) ** 2, axis=1)),
    'log_loss': log_loss(prueba.nivel_popularidad, proba),
}
publicadas = pd.read_csv(tablas / 'metricas_prueba.csv').iloc[0]
for clave, valor in metricas.items():
    np.testing.assert_allclose(valor, [publicadas[clave], meta['metricas'][clave]])
np.testing.assert_array_equal(pd.read_csv(tablas / 'matriz_confusion.csv').set_index('real'),
                              meta['metricas']['matriz_confusion'])
calibracion = pd.read_csv(tablas / 'calibracion.csv')
for i, clase in enumerate(modelo.classes_):
    total = 0
    for intervalo in calibracion.loc[calibracion.clase.eq(clase)].itertuples():
        superior = proba[:, i] <= 1 if intervalo.limite_superior == 1 else proba[:, i] < intervalo.limite_superior
        grupo = (proba[:, i] >= intervalo.limite_inferior) & superior
        assert int(grupo.sum()) == intervalo.n
        np.testing.assert_allclose([proba[grupo, i].mean(), uno_hot[grupo, i].mean()],
                                   [intervalo.probabilidad_media, intervalo.fraccion_observada])
        total += intervalo.n
    assert total == len(prueba)
cv = pd.read_csv(tablas / 'cv_externa_folds.csv')
resumen = pd.read_csv(tablas / 'comparativo_modelos.csv').set_index('modelo')
assert len(cv) == 250 and cv.groupby(['repeticion', 'fold']).modelo.nunique().eq(5).all()
for metrica in METRICAS:
    por_modelo = cv.groupby('modelo')[metrica]
    np.testing.assert_allclose(por_modelo.mean().reindex(resumen.index), resumen[metrica + '_media'])
    np.testing.assert_allclose(por_modelo.std().reindex(resumen.index), resumen[metrica + '_de'])
np.testing.assert_allclose(contrastar(cv).p_valor, pd.read_csv(tablas / 'comparacion_estadistica.csv').p_valor, atol=1e-13)
np.testing.assert_allclose(ajustar_referencia(juegos)['cortes'], meta['terciles_descriptivos_catalogo']['cortes'])
for clave in ['genero', 'estudio']:
    grupos = pd.read_csv(tablas / f'popularidad_{clave}.csv')
    assert grupos.n_juegos.ge(20).all()
    assert grupos.loc[grupos.n.lt(20), ['pearson_r', 'spearman_rho']].isna().all().all()
pca = pd.read_csv(tablas / 'pca_clusters.csv')
assert len(pca) == int(mascara.sum()) and pca.id_juego.is_unique
perfiles = pd.read_csv(tablas / 'perfiles_clusters.csv')
assert perfiles.groupby('metodo').n.sum().eq(len(pca)).all()
salida['auditoria_integral'] = {'modelo': meta['modelo'], 'python': meta['python'], 'filas_cv': len(cv),
                               'metricas_prueba': metricas, 'matriz_y_calibracion_reproducidas': True,
                               'resumen_cv_y_p_valores_recalculados': True, 'perfiles_y_terciles_revisados': True}
(raiz / 'reports/verificacion_independiente.json').write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(salida, ensure_ascii=False, indent=2))
