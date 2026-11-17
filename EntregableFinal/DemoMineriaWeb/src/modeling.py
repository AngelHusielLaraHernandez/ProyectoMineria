"""Adaptador: la única implementación supervisada es src/04_modelo.py."""
import importlib
import numpy as np


def thresholds(scores):
    cortes = np.quantile(scores, [1/3, 2/3])
    if cortes[0] >= cortes[1]:
        raise ValueError('No se pueden definir tres niveles distintos.')
    return cortes


def levels(scores, cuts):
    return np.asarray(['bajo', 'medio', 'alto'])[np.searchsorted(cuts, scores, side='left')]


def train(df):
    return importlib.import_module('src.04_modelo').entrenar_datos(df)
