"""Codificadores ajustados exclusivamente con la partición de entrenamiento."""
import numpy as np
import ast
from collections import Counter
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer


class ListEncoder(TransformerMixin, BaseEstimator):
    """Codifica cada miembro de una lista sin imponer un género o estudio principal."""
    def fit(self, X, y=None):
        self.encoder_ = MultiLabelBinarizer()
        self.encoder_.fit(X.iloc[:, 0])
        return self

    def transform(self, X):
        known = set(self.encoder_.classes_)
        return self.encoder_.transform([[v for v in row if v in known] for row in X.iloc[:, 0]])

    def get_feature_names_out(self, input_features=None):
        return np.asarray(self.encoder_.classes_, dtype=object)


def lista_cruda(valor):
    if isinstance(valor, (list, tuple)):
        lista = list(valor)
    elif pd.isna(valor) or not str(valor).strip():
        return []
    elif str(valor).strip().startswith('['):
        lista = ast.literal_eval(str(valor))
    else:
        lista = [str(valor)]
    if not isinstance(lista, list) or not all(isinstance(v, str) for v in lista):
        raise ValueError('Se esperaba una lista de categorías de texto.')
    return list(dict.fromkeys(v.strip() for v in lista if v.strip()))


class CategoriasFrecuentes(TransformerMixin, BaseEstimator):
    """Multi-hot con vocabulario entrenado dentro de cada fold; raros/nuevos a Otro."""
    def __init__(self, min_frecuencia=10, max_categorias=None, otro_solo_si_ninguna=False):
        self.min_frecuencia = min_frecuencia
        self.max_categorias = max_categorias
        self.otro_solo_si_ninguna = otro_solo_si_ninguna

    def fit(self, X, y=None):
        filas = X.iloc[:, 0] if hasattr(X, 'iloc') else np.asarray(X, dtype=object)[:, 0]
        frecuencias = Counter(v for fila in filas for v in lista_cruda(fila))
        orden = sorted(frecuencias, key=lambda c: (-frecuencias[c], c))
        self.vocabulario_ = [c for c in orden if frecuencias[c] >= self.min_frecuencia and c not in ['Otro', 'Sin dato']]
        if self.max_categorias is not None:
            self.vocabulario_ = self.vocabulario_[:self.max_categorias]
        self.frecuencias_ = dict(frecuencias)
        self.columnas_ = [*self.vocabulario_, 'Otro', 'Sin dato']
        return self

    def transform(self, X):
        filas = X.iloc[:, 0] if hasattr(X, 'iloc') else np.asarray(X, dtype=object)[:, 0]
        posiciones = {c: i for i, c in enumerate(self.vocabulario_)}
        salida = np.zeros((len(filas), len(self.columnas_)), dtype=float)
        for i, fila in enumerate(filas):
            categorias = lista_cruda(fila)
            if not categorias:
                salida[i, -1] = 1
            conocidas = [c for c in categorias if c in posiciones]
            for c in categorias:
                if c in posiciones:
                    salida[i, posiciones[c]] = 1
                elif not self.otro_solo_si_ninguna or not conocidas:
                    salida[i, len(self.vocabulario_)] = 1
        return salida

    def get_feature_names_out(self, input_features=None):
        return np.asarray(self.columnas_, dtype=object)
