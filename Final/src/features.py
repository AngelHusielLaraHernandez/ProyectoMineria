"""Codificadores ajustados exclusivamente con la partición de entrenamiento."""
import numpy as np
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
