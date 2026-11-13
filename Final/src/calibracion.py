"""Ajusta y comprueba la calibración multiclase del modelo de popularidad."""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import softmax
from sklearn.base import clone
from sklearn.metrics import log_loss

from .config import FEATURES
from .evaluacion_anidada import guardar_calibracion
from .objetivo import ajustar_referencia, aplicar_referencia


def aplicar_temperatura(probabilidades, temperatura):
    """Escala log(p) con una temperatura positiva y conserva el orden de clases."""
    log_probabilidades = np.log(np.clip(probabilidades, np.finfo(float).eps, 1))
    return softmax(log_probabilidades / temperatura, axis=-1)


def calibrar_modelo(modelo, entrenamiento, prueba, tablas):
    """Aprende con predicciones fuera de pliegue y mide el efecto en prueba."""
    clases = modelo.classes_
    if set(entrenamiento.grupo_titulo) & set(prueba.grupo_titulo):
        raise ValueError('La calibración necesita separar los títulos de entrenamiento y prueba.')
    probabilidades = np.empty((len(entrenamiento), len(clases)))
    etiquetas = np.empty(len(entrenamiento), dtype=clases.dtype)
    pliegues = entrenamiento.fold_validacion
    if pliegues.isna().any() or pliegues.nunique() < 2:
        raise ValueError('La calibración necesita un pliegue válido por juego de entrenamiento.')

    for numero in sorted(pliegues.unique()):
        validacion = pliegues.eq(numero).to_numpy()
        ajuste, fuera = entrenamiento.loc[~validacion], entrenamiento.loc[validacion]
        if set(ajuste.grupo_titulo) & set(fuera.grupo_titulo):
            raise ValueError('La calibración necesita separar los títulos por pliegue.')
        referencia = ajustar_referencia(ajuste)
        clases_ajuste = aplicar_referencia(ajuste, referencia).nivel_popularidad
        bosque = clone(modelo).fit(ajuste[FEATURES], clases_ajuste)
        if not np.array_equal(bosque.classes_, clases):
            raise ValueError('Cada ajuste necesita las tres clases de popularidad.')
        probabilidades[validacion] = bosque.predict_proba(fuera[FEATURES])
        etiquetas[validacion] = aplicar_referencia(fuera, referencia).nivel_popularidad

    # Se ajusta solo el parámetro de escala, con los hiperparámetros del bosque activo.
    resultado = minimize_scalar(
        lambda log_t: log_loss(etiquetas, aplicar_temperatura(probabilidades, np.exp(log_t)), labels=clases),
        bounds=(-3, 3), method='bounded',
    )
    if not resultado.success:
        raise ValueError('No se pudo ajustar la temperatura.')
    temperatura = float(np.exp(resultado.x))
    probabilidades_prueba = modelo.predict_proba(prueba[FEATURES])
    ajustadas = aplicar_temperatura(probabilidades_prueba, temperatura)
    metricas = guardar_calibracion(
        tablas, prueba.nivel_popularidad, ajustadas, clases, nombre='calibracion_ajustada.csv',
    )
    return {'metodo': 'Escalado de temperatura', 'temperatura': temperatura,
            'n_ajuste': len(entrenamiento), 'pliegues': int(pliegues.nunique()),
            'n_prueba': len(prueba), 'metricas_prueba': metricas}
