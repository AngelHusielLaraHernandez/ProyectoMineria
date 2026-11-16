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
