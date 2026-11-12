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
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler, KBinsDiscretizer
from sklearn.tree import DecisionTreeClassifier

from src.config import FEATURES, SEED
from src.evaluacion_anidada import ACTIVO, PLIEGUES_INTERNOS, REPETICIONES, evaluar, guardar_calibracion, puntuar
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
        'MLPClassifier': (MLPClassifier(activation='tanh', solver='lbfgs', max_iter=2000, tol=1e-3, random_state=SEED),
                          {'clasificar__hidden_layer_sizes': [(16,), (32,)],
                           'clasificar__alpha': [1., 5.]}),
    }
    informes, modelos, limpio = raiz / 'reports', raiz / 'models', raiz / 'data/clean'
    for p in [informes, modelos, limpio]:
        p.mkdir(parents=True, exist_ok=True)
    tablas = informes / 'tables'
    tablas.mkdir(exist_ok=True)
    referencia_catalogo = ajustar_referencia(df)
    pd.DataFrame([{'n': len(df), 'tercil_1': referencia_catalogo['cortes'][0],
                   'tercil_2': referencia_catalogo['cortes'][1]}]).to_csv(tablas / 'terciles_catalogo.csv', index=False)
    resumen_externo, contrastes = evaluar(contexto.iloc[tr], y_train, grupos, candidatos, construir_pipeline, tablas)
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
    # La decisión de producción queda fijada antes de la evaluación de esta corrida.
    mejor_nombre = ACTIVO
    mejor = busquedas[mejor_nombre].best_estimator_.pipeline_
    matrices, predicciones = {}, pd.DataFrame({'id_juego': df.id_juego.iloc[te].to_numpy(), 'real': y_test})
    pred_activo = mejor.predict(X_test)
    proba_activo = mejor.predict_proba(X_test)
    metricas_prueba = puntuar(y_test, pred_activo, proba_activo, mejor.classes_)
    metricas_prueba.update(guardar_calibracion(tablas, y_test, proba_activo, mejor.classes_))
    historico = tablas / 'prueba_historica_predicciones.csv'
    if not historico.exists():
        historico = RAIZ / 'reports/tables/prueba_historica_predicciones.csv'
    if historico.exists():
        previas = pd.read_csv(historico)
        if not previas[['id_juego', 'real']].equals(predicciones):
            previas = pd.DataFrame()
    else:
        previas = pd.DataFrame()
    for nombre, busqueda in busquedas.items():
        if nombre == mejor_nombre:
            pred, origen = pred_activo, 'Prueba actual'
        elif nombre in previas:
            pred, origen = previas[nombre], 'Prueba histórica congelada'
        elif nombre == 'DummyClassifier':
            pred, origen = np.repeat(pd.Series(y_train).mode().iloc[0], len(y_test)), 'Referencia mayoritaria analítica'
        else:
            pred, origen = None, 'Sin prueba comparable'
        fila = {'modelo': nombre, 'f1_macro_cv': resumen_externo.loc[nombre, 'f1_macro_media'],
                'desviacion_cv': resumen_externo.loc[nombre, 'f1_macro_de'], 'origen_prueba': origen,
                'mejores_parametros': json.dumps(busqueda.best_params_, sort_keys=True)}
        if pred is not None:
            predicciones[nombre] = pred
            matriz = confusion_matrix(y_test, pred, labels=CLASES)
            matrices[nombre] = matriz.tolist()
            pd.DataFrame(matriz, index=CLASES, columns=CLASES).rename_axis('real / predicha').to_csv(informes / f'modelo_confusion_{nombre}.csv')
            fila.update(exactitud_prueba=accuracy_score(y_test, pred),
                        f1_macro_prueba=f1_score(y_test, pred, labels=CLASES, average='macro', zero_division=0),
                        balanced_accuracy_prueba=balanced_accuracy_score(y_test, pred))
        resultados.append(fila)
    pd.DataFrame(matrices[mejor_nombre], index=CLASES, columns=CLASES).rename_axis('real').to_csv(tablas / 'matriz_confusion.csv')
    pd.DataFrame([{'modelo': mejor_nombre, 'n': len(te), **metricas_prueba}]).to_csv(tablas / 'metricas_prueba.csv', index=False)
    tabla = pd.DataFrame(resultados)
    tabla.to_csv(tablas / 'comparacion_prueba_actual_e_historica.csv', index=False)
    tabla.to_csv(informes / 'modelo_comparacion.csv', index=False)
    pd.DataFrame(filas_cv).to_csv(informes / 'modelo_grid_cv.csv', index=False)
    predicciones.to_csv(informes / 'modelo_predicciones_prueba.csv', index=False)
    bosque = busquedas['RandomForestClassifier'].best_estimator_.pipeline_
    columnas = bosque.named_steps['preparar'].get_feature_names_out()
    valores = bosque.named_steps['clasificar'].feature_importances_
    variables = [nombre.split('__', 1)[1] if nombre.startswith('notas__')
                 else nombre.split('__', 1)[0] for nombre in columnas]
    gini = pd.DataFrame({'variable': variables, 'importancia': valores})
    gini = gini.groupby('variable', as_index=False)['importancia'].sum()
    gini.to_csv(informes / 'modelo_importancia_gini.csv', index=False)
    gini.to_csv(tablas / 'modelo_importancia_gini.csv', index=False)
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
                'definicion_objetivo': definicion,
                'terciles_descriptivos_catalogo': {'n': len(df), 'cortes': referencia_catalogo['cortes']}, 'alternativa_solo_plays': {'cortes': definicion_plays['cortes'],
                    'fraccion_etiquetas_coincidentes': float((y == alternativa.nivel_popularidad).mean())},
                'n_cohorte': len(df), 'n_entrenamiento': len(tr), 'n_prueba': len(te),
                'particion': {'test_size': .2, 'estratificada': False, 'sin_titulos_compartidos': True,
                              'regla': 'GroupShuffleSplit, una partición independiente de los conteos/etiquetas; aproximadamente 80/20 por grupos.',
                              'intentos': 1},
                'validacion': {'pliegues': 10, 'estratificada': True, 'agrupacion': 'grupo_titulo',
                               'metodo': 'StratifiedGroupKFold anidado', 'repeticiones': REPETICIONES, 'pliegues_internos': PLIEGUES_INTERNOS,
                               'seleccion': 'Random Forest fijado para producción. Búsqueda interna por F1 macro y evaluación externa independiente.',
                               'etiquetas_para_organizar_estratos': 'Referencia externa de entrenamiento; no se usa para fit/score de los folds.'},
                'distribuciones': {nombre: pd.Series(valores).value_counts().to_dict() for nombre, valores in [('catalogo', y), ('entrenamiento', y_train), ('prueba', y_test)]},
                'mejores_parametros': busquedas[mejor_nombre].best_params_,
                'metricas': {'exactitud': float(final.exactitud_prueba), 'f1_macro': float(final.f1_macro_prueba),
                             'balanced_accuracy': float(final.balanced_accuracy_prueba), 'f1_macro_referencia': float(base.f1_macro_prueba),
                             'diferencia_f1_referencia': diferencia, 'f1_macro_cv': float(final.f1_macro_cv),
                             'matriz_confusion': matrices[mejor_nombre],
                             **metricas_prueba,
                             'reporte_clases': classification_report(y_test, pred_activo, labels=CLASES, output_dict=True, zero_division=0)},
                'comparacion_modelos': json.loads(tabla.to_json(orient='records')), 'evaluacion_referencia': juicio,
                'evaluacion_anidada': resumen_externo.reset_index().to_dict(orient='records'),
                'comparacion_estadistica': json.loads(contrastes.to_json(orient='records')),
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
        'Notas: mediana ajustada solo con entrenamiento, sin MissingIndicator. StandardScaler se aplica exclusivamente a las dos notas continuas para árboles, bosque, referencia y MLP; los otros indicadores se mantienen en 0/1. La curación de Metacritic sigue siendo una fuente posible de sesgo no aleatorio, aun sin bandera explícita.', '',
        'Se reemplaza GaussianNB por CategoricalNB: la mayoría de atributos son indicadores categóricos y las dos notas se discretizan en cinco intervalos de ancho uniforme entre los extremos de entrenamiento de cada fold. min_categories=5 permite códigos nuevos dentro del rango; alpha se ajusta en tres valores. Se reconoce pérdida de resolución por discretización e independencia condicional aproximada; no se ajustan gaussianas a decenas de dummies raras.', '',
        '## Comparación y selección', '',
        'La MLP usa una capa oculta con activación tanh de 16 o 32 neuronas y optimización L-BFGS. Se comparan dos valores de regularización L2 dentro de los mismos pliegues que los demás candidatos.', '',
        tabla_md(tabla), '',
        f'Modelo activo por decisión de proyecto: **{m["modelo"]}**. {m["evaluacion_referencia"]} Diferencia en prueba frente a referencia: {m["metricas"]["diferencia_f1_referencia"]:.4f}.',
        'La evaluación externa repite diez pliegues estratificados por grupos cinco veces, con semillas 42 a 46 compartidas por los cinco modelos. Una búsqueda de tres pliegues internos escoge parámetros para cada evaluación externa. La búsqueda final en diez pliegues solo sirve para ajustar el artefacto sobre entrenamiento.',
        f'El catálogo elegible completo tiene {m["terciles_descriptivos_catalogo"]["n"]} juegos y cortes descriptivos {m["terciles_descriptivos_catalogo"]["cortes"]}. La evaluación y la inferencia usan la referencia de entrenamiento para impedir que los conteos reservados intervengan en los cortes.',
        'La evaluación previa produjo resultados de prueba de los candidatos, incluida la MLP. El código archivado seleccionaba por CV antes de calcular la prueba, pero la decisión actual se toma con esos resultados ya conocidos. Esta prueba reutiliza la misma partición histórica y no constituye una confirmación independiente de la decisión de producción. Solo se recalcula la prueba del Random Forest.',
        f'Brier multiclase (suma sobre clases) = {m["metricas"]["brier_multiclase"]:.4f}. Log-loss = {m["metricas"]["log_loss"]:.4f}. La fiabilidad por clase usa diez intervalos fijos y registra el número de observaciones en tables/calibracion.csv.',
        'Los contrastes sobre F1 macro están en tables/comparacion_estadistica.csv. La t de Nadeau–Bengio corrige por la razón entre tamaños de validación y ajuste. Wilcoxon, Friedman y Nemenyi son complementarios: el solapamiento de los pliegues limita sus supuestos de independencia. Una diferencia no significativa no demuestra equivalencia.', '',
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
    errores.to_csv(informes / 'tables/modelo_error_por_clase.csv', index=False)
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
