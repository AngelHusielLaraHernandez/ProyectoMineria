"""Evaluación externa repetida y contrastes pareados sobre F1 macro."""
import json

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold
from threadpoolctl import threadpool_limits

from .config import SEED
from .objetivo import CLASES, ClasificadorObjetivoLocal, aplicar_referencia, puntuar_objetivo_local

ACTIVO = 'RandomForestClassifier'
METRICAS = ['exactitud_pct', 'f1_macro', 'f1_ponderado', 'kappa', 'roc_auc_ovr']
REPETICIONES = 5
PLIEGUES = 10
PLIEGUES_INTERNOS = 3


def puntuar(real, predicho, proba, clases):
    return {
        'exactitud_pct': 100 * accuracy_score(real, predicho),
        'f1_macro': f1_score(real, predicho, labels=CLASES, average='macro', zero_division=0),
        'f1_ponderado': f1_score(real, predicho, labels=CLASES, average='weighted', zero_division=0),
        'kappa': cohen_kappa_score(real, predicho, labels=CLASES),
        'roc_auc_ovr': roc_auc_score(real, proba, labels=clases, average='macro', multi_class='ovr'),
    }


def evaluar(contexto, etiquetas, grupos, candidatos, construir_pipeline, tablas):
    filas = []
    with threadpool_limits(limits=1, user_api='blas'):
        for repeticion in range(REPETICIONES):
            semilla = SEED + repeticion
            externo = StratifiedGroupKFold(n_splits=PLIEGUES, shuffle=True, random_state=semilla)
            for fold, (a, b) in enumerate(externo.split(contexto, etiquetas, grupos), 1):
                ajuste, validacion = contexto.iloc[a], contexto.iloc[b]
                # Los estratos internos se construyen solo con el subentrenamiento externo.
                from .objetivo import ajustar_referencia
                estratos = aplicar_referencia(ajuste, ajustar_referencia(ajuste)).nivel_popularidad
                interno = StratifiedGroupKFold(n_splits=PLIEGUES_INTERNOS, shuffle=True, random_state=semilla)
                particiones = list(interno.split(ajuste, estratos, grupos[a]))
                for nombre, (estimador, grid) in candidatos.items():
                    busqueda = GridSearchCV(
                        ClasificadorObjetivoLocal(construir_pipeline(estimador)),
                        {f'pipeline__{k}': v for k, v in grid.items()}, cv=particiones,
                        scoring=puntuar_objetivo_local, error_score='raise', n_jobs=1,
                    ).fit(ajuste, estratos)
                    modelo = busqueda.best_estimator_
                    real = aplicar_referencia(validacion, modelo.referencia_).nivel_popularidad
                    metricas = puntuar(real, modelo.predict(validacion), modelo.predict_proba(validacion), modelo.classes_)
                    filas.append(dict(modelo=nombre, repeticion=repeticion + 1, fold=fold,
                                      semilla=semilla, n_ajuste=len(a), n_validacion=len(b),
                                      parametros=json.dumps(busqueda.best_params_, sort_keys=True), **metricas))
            print(f'CV externa: repetición {repeticion + 1}/{REPETICIONES}', flush=True)
    detalle = pd.DataFrame(filas)
    resumen = detalle.groupby('modelo', sort=False)[METRICAS].agg(['mean', 'std'])
    resumen.columns = [f'{metrica}_{"media" if estadistico == "mean" else "de"}'
                       for metrica, estadistico in resumen.columns]
    resumen['n_pliegues'] = PLIEGUES * REPETICIONES
    resumen = resumen.reset_index()
    contrastes = contrastar(detalle)
    detalle.to_csv(tablas / 'cv_externa_folds.csv', index=False)
    resumen.to_csv(tablas / 'comparativo_modelos.csv', index=False)
    contrastes.to_csv(tablas / 'comparacion_estadistica.csv', index=False)
    return resumen.set_index('modelo'), contrastes


def contrastar(detalle):
    f1 = detalle.pivot(index=['repeticion', 'fold'], columns='modelo', values='f1_macro')
    tamanos = detalle.drop_duplicates(['repeticion', 'fold'])
    razon = (tamanos.n_validacion / tamanos.n_ajuste).mean()
    n = len(f1)
    filas = []
    for candidato in f1.columns.drop(ACTIVO):
        delta = f1[ACTIVO] - f1[candidato]
        media = delta.mean()
        error = np.sqrt((1 / n + razon) * delta.var(ddof=1))
        t = media / error if error else (np.sign(media) * np.inf if media else 0)
        wilcoxon = stats.wilcoxon(delta, method='approx') if delta.any() else (0., 1.)
        filas.extend([
            ('t corregida Nadeau–Bengio', ACTIVO, candidato, n, media, t, 2 * stats.t.sf(abs(t), n - 1)),
            ('Wilcoxon', ACTIVO, candidato, n, media, *wilcoxon),
        ])
    nombres = f1.columns.to_list()
    friedman = stats.friedmanchisquare(*(f1[col] for col in nombres))
    filas.append(('Friedman', 'Todos', '', n, np.nan, *friedman))
    rangos = f1.rank(axis=1, ascending=False, method='average').mean()
    k = len(nombres)
    error_rangos = np.sqrt(k * (k + 1) / (6 * n))
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            q = abs(rangos[a] - rangos[b]) / error_rangos
            p = stats.studentized_range.sf(q * np.sqrt(2), k, np.inf)
            filas.append(('Nemenyi', a, b, n, (f1[a] - f1[b]).mean(), q, p))
    return pd.DataFrame(filas, columns=['prueba', 'modelo_a', 'modelo_b', 'n_pares',
                                        'delta_f1_macro_a_menos_b', 'estadistico', 'p_valor'])


def guardar_calibracion(tablas, real, proba, clases, nombre='calibracion.csv'):
    """Brier multiclase sin reescalar y fiabilidad OvR por intervalos fijos."""
    from sklearn.metrics import log_loss
    observada = np.asarray(real)[:, None] == np.asarray(clases)[None, :]
    filas = []
    limites = np.linspace(0, 1, 11)
    for i, clase in enumerate(clases):
        cubetas = np.searchsorted(limites[1:-1], proba[:, i], side='right')
        for b in range(10):
            mascara = cubetas == b
            if mascara.any():
                filas.append({'clase': clase, 'limite_inferior': limites[b],
                              'limite_superior': limites[b+1], 'n': int(mascara.sum()),
                              'probabilidad_media': proba[mascara, i].mean(),
                              'fraccion_observada': observada[mascara, i].mean()})
    pd.DataFrame(filas).to_csv(tablas / nombre, index=False)
    return {'brier_multiclase': float(np.mean(np.sum((proba - observada) ** 2, axis=1))),
            'log_loss': float(log_loss(real, proba, labels=clases))}
