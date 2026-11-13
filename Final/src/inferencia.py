"""Contrato único del formulario con el Pipeline entrenado."""
import numpy as np
import pandas as pd
from .calibracion import aplicar_temperatura
from .config import FEATURES
from .features import lista_cruda

_MOD_VERSION = 'p5-v12-portadas'


def predecir_formulario(pipeline, generos, estudio, decada, metacritic, rating, *, temperatura=None):
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
    if isinstance(decada, (bool, np.bool_)):
        raise ValueError('La década debe ser un entero válido, no booleano.')
    d = float(decada)
    if not np.isfinite(d) or d != int(d):
        raise ValueError('La década debe ser un entero válido (-1 o múltiplo de diez).')
    decada_int = int(d)
    if decada_int != -1 and (decada_int < 0 or decada_int % 10):
        raise ValueError('La década debe ser -1 o un entero no negativo múltiplo de diez.')
    fila = pd.DataFrame([{'generos': generos, 'estudio': lista_cruda(estudio),
                          'decada': decada_int, **notas}], columns=FEATURES)
    valores = pipeline.predict_proba(fila)[0]
    if not np.isfinite(valores).all() or not np.isclose(valores.sum(), 1) or (valores < 0).any():
        raise ValueError('El modelo devolvió probabilidades inválidas.')
    prediccion = str(pipeline.classes_[int(np.argmax(valores))])
    if temperatura is not None:
        valores = aplicar_temperatura(valores, temperatura)
    probabilidades = {str(c): float(p) for c, p in zip(pipeline.classes_, valores)}
    return fila, prediccion, probabilidades
