"""Evaluación separada del ajuste: títulos agrupados y terciles de entrenamiento."""
import json
import platform
import hashlib

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, classification_report,
                             confusion_matrix, f1_score)
from sklearn.model_selection import GroupKFold, GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler

from .config import CLEAN, FEATURES, LEVELS, MODELS, REPORTS, SEED, RAW
from .features import ListEncoder


def thresholds(scores):
    cuts = np.quantile(scores, [1/3, 2/3])
    if cuts[0] >= cuts[1]:
        raise ValueError('No hay variación suficiente para definir tres niveles.')
    return cuts


def levels(scores, cuts):
    # Los empates reciben la misma clase, aunque los tamaños no sean idénticos.
    return np.asarray(LEVELS)[np.searchsorted(cuts, np.asarray(scores), side='left')]


def make_pipeline(estimator):
    numeric = Pipeline([('imputar', SimpleImputer(strategy='median', add_indicator=True)),
                        ('escalar', StandardScaler())])
    decade = Pipeline([('tipo_float', FunctionTransformer(np.asarray, kw_args={'dtype': float}, feature_names_out='one-to-one')),
                       ('imputar', SimpleImputer(strategy='constant', fill_value=-1)),
                       ('codificar', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])
    prep = ColumnTransformer([
        ('generos', ListEncoder(), ['generos']),
        ('organizaciones', ListEncoder(), ['organizaciones']),
        ('decada', decade, ['decada']),
        ('notas', numeric, ['Rating', 'critica_verificada_csv']),
    ])
    return Pipeline([('preparar', prep), ('clasificar', estimator)])


def train(df):
    eligible = df.dropna(subset=['popularidad_indice']).copy().reset_index(drop=True)
    splitter = GroupShuffleSplit(n_splits=1, test_size=.2, random_state=SEED)
    tr, te = next(splitter.split(eligible, groups=eligible['grupo_titulo']))
    training, testing = eligible.iloc[tr], eligible.iloc[te]
    assert set(training['grupo_titulo']).isdisjoint(set(testing['grupo_titulo']))
    cuts = thresholds(training['popularidad_indice'])
    y_train = levels(training['popularidad_indice'], cuts)
    y_test = levels(testing['popularidad_indice'], cuts)
    candidates = {
        'base_mayoritaria': DummyClassifier(strategy='most_frequent', random_state=SEED),
        'regresion_logistica': LogisticRegression(max_iter=3000, C=1, random_state=SEED),
        'bosque_aleatorio': RandomForestClassifier(n_estimators=250, min_samples_leaf=3,
                                                   class_weight='balanced', random_state=SEED, n_jobs=1),
    }
    trials = []
    cv = GroupKFold(n_splits=5, shuffle=True, random_state=SEED)
    # Cada fold vuelve a obtener sus propios cortes: la validación no define su clase.
    for name, estimator in candidates.items():
        for fold, (it, iv) in enumerate(cv.split(training, groups=training['grupo_titulo']), 1):
            a, b = training.iloc[it], training.iloc[iv]
            local_cuts = thresholds(a['popularidad_indice'])
            ya, yb = levels(a['popularidad_indice'], local_cuts), levels(b['popularidad_indice'], local_cuts)
            model = make_pipeline(clone(estimator)).fit(a[FEATURES], ya)
            pred = model.predict(b[FEATURES])
            trials.append({'modelo': name, 'fold': fold,
                           'f1_macro': f1_score(yb, pred, labels=LEVELS, average='macro', zero_division=0),
                           'balanced_accuracy': balanced_accuracy_score(yb, pred)})
    cv_table = pd.DataFrame(trials)
    cv_table.to_csv(REPORTS / 'validacion_cruzada.csv', index=False)
    averages = cv_table.groupby('modelo')['f1_macro'].agg(['mean', 'std'])
    averages.to_csv(REPORTS / 'comparacion_modelos.csv')
    best = averages['mean'].idxmax()
    model = make_pipeline(clone(candidates[best])).fit(training[FEATURES], y_train)
    pred = model.predict(testing[FEATURES])
    baseline = make_pipeline(clone(candidates['base_mayoritaria'])).fit(training[FEATURES], y_train)
    metrics = {
        'modelo': best, 'n_entrenamiento': len(tr), 'n_prueba': len(te),
        'fuente': RAW.name, 'sha256_fuente': hashlib.sha256(RAW.read_bytes()).hexdigest(),
        'cortes_entrenamiento': cuts.tolist(), 'semilla': SEED,
        'accuracy': accuracy_score(y_test, pred),
        'balanced_accuracy': balanced_accuracy_score(y_test, pred),
        'f1_macro': f1_score(y_test, pred, labels=LEVELS, average='macro', zero_division=0),
        'f1_macro_base': f1_score(y_test, baseline.predict(testing[FEATURES]), labels=LEVELS, average='macro', zero_division=0),
        'reporte': classification_report(y_test, pred, labels=LEVELS, output_dict=True, zero_division=0),
        'distribucion_entrenamiento': pd.Series(y_train).value_counts().to_dict(),
        'distribucion_prueba': pd.Series(y_test).value_counts().to_dict(),
        'python': platform.python_version(), 'sklearn': sklearn.__version__,
        'nota': 'Modelo conservado tal como se evaluó; no reajustado con prueba. Probabilidades sin calibrar.',
    }
    (REPORTS / 'metricas.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding='utf-8')
    pd.DataFrame(confusion_matrix(y_test, pred, labels=LEVELS), index=LEVELS, columns=LEVELS).rename_axis('real / predicha').to_csv(REPORTS / 'matriz_confusion.csv')
    joblib.dump({'pipeline': model, 'cortes': cuts, 'features': FEATURES, 'metricas': metrics}, MODELS / 'popularidad.joblib')
    all_levels = levels(eligible['popularidad_indice'], cuts)
    partition = np.full(len(eligible), 'entrenamiento', dtype=object)
    partition[te] = 'prueba'
    export = eligible.copy()
    export['nivel_popularidad'] = all_levels
    export['particion'] = partition
    for c in ['generos', 'organizaciones']:
        export[c] = export[c].map(lambda x: json.dumps(x, ensure_ascii=False))
    export.to_csv(CLEAN / 'juegos_modelo.csv', index=False)
    # Exportación numérica con el mismo preprocesamiento, nunca reajustado en prueba.
    prep = model.named_steps['preparar']
    names = prep.get_feature_names_out()
    for indexes, label in [(tr, 'entrenamiento'), (te, 'prueba')]:
        data = pd.DataFrame(prep.transform(eligible.iloc[indexes][FEATURES]), columns=names)
        data['nivel_popularidad'] = all_levels[indexes]
        data.to_csv(CLEAN / f'{label}_orange.csv', index=False)
        lines = ['% Variables transformadas con entrenamiento; no contiene conteos ni índice.', '@RELATION popularidad']
        lines += [f'@ATTRIBUTE variable_{i} NUMERIC' for i in range(len(names))]
        lines += ['@ATTRIBUTE nivel_popularidad {bajo,medio,alto}', '@DATA']
        lines += [','.join([*(format(float(v), '.12g') for v in row[:-1]), row[-1]]) for row in data.itertuples(index=False, name=None)]
        (CLEAN / f'{label}_weka.arff').write_text('\n'.join(lines), encoding='utf-8')
    pd.DataFrame({'atributo_arff': [f'variable_{i}' for i in range(len(names))], 'variable': names}).to_csv(CLEAN / 'diccionario_weka.csv', index=False)
    return metrics
