"""Contrato único del formulario con el Pipeline entrenado."""
import numpy as np
import pandas as pd
from .config import FEATURES
from .features import lista_cruda


def predecir_formulario(pipeline, generos, estudio, decada, metacritic, rating):
    """Valida escalas y devuelve entrada cruda, clase y probabilidades por nombre."""
    generos = lista_cruda(generos)
    if not generos:
        raise ValueError('Selecciona al menos un género.')
    notas = {}
    for campo, valor, limite in [('Rating', rating, 5), ('Metacritic Rating', metacritic, 100)]:
        numero = np.nan if valor is None or pd.isna(valor) else float(valor)
        if not np.isnan(numero) and (not np.isfinite(numero) or numero < 0 or numero > limite):
            raise ValueError(f'{campo} debe estar entre 0 y {limite}, o ausente.')
        notas[campo] = numero
    d = float(decada)
    if not np.isfinite(d) or d != int(d) or int(d) % 10:
        raise ValueError('La década debe ser un entero múltiplo de diez.')
    fila = pd.DataFrame([{'generos': generos, 'estudio': lista_cruda(estudio),
                          'decada': int(d), **notas}], columns=FEATURES)
    prediccion = str(pipeline.predict(fila)[0])
    valores = pipeline.predict_proba(fila)[0]
    if not np.isfinite(valores).all() or not np.isclose(valores.sum(), 1) or (valores < 0).any():
        raise ValueError('El modelo devolvió probabilidades inválidas.')
    probabilidades = {str(c):float(p) for c,p in zip(pipeline.classes_, valores)}
    if prediccion != str(pipeline.classes_[np.argmax(valores)]):
        raise ValueError('La clase estimada no coincide con la mayor probabilidad.')
    return fila, prediccion, probabilidades
