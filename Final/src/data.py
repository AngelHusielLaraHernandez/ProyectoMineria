"""Adaptadores de la fuente canónica producida por la fase 02."""
import importlib
import inspect
import json
import sys
import numpy as np
import pandas as pd
from .config import CLEAN, MODELS, REPORTS
from .objetivo import aplicar_referencia

_MOD_VERSION = 'p5-v12-portadas'
_MODULOS_ORDENADOS = (
    ('src.visualizacion', ()),
    ('src.data', ('src.config',)),
    ('src.inferencia', ('src.config',)),
    ('src.portadas', ()),
    ('src.similitud', ('src.config',)),
    ('src.ui', ('src.config', 'src.data', 'src.visualizacion')),
    ('vista_graficas', ('src.ui',)),
)


def _modulo_version_distinta(nombre: str, mod) -> bool:
    """Indica si un módulo cargado tiene una versión distinta a la vigente."""
    attr = '_UI_VERSION' if nombre == 'src.ui' else '_MOD_VERSION'
    return getattr(mod, attr, None) != _MOD_VERSION


def _modulo_obsoleto(nombre: str, mod) -> bool:
    """Detecta versiones obsoletas y comprueba las firmas que usan las páginas."""
    if _modulo_version_distinta(nombre, mod):
        return True
    if nombre == 'src.ui':
        return not hasattr(mod, 'asset_b64')
    if nombre == 'src.inferencia':
        fn = getattr(mod, 'predecir_formulario', None)
        return fn is None or 'temperatura' not in inspect.signature(fn).parameters
    if nombre == 'src.similitud':
        fn = getattr(mod, 'cinco_vecinos', None)
        return fn is None or 'vecinos' not in inspect.signature(fn).parameters
    return False


def asegurar_modulos_vigentes(config_recargado: bool = False) -> list[str]:
    """Recarga en orden de dependencias los módulos obsoletos presentes en sys.modules."""
    recargados = {'src.config'} if config_recargado else set()
    orden_recarga = []
    hay_desfase_version = config_recargado or any(
        (mod := sys.modules.get(nombre)) is not None and _modulo_version_distinta(nombre, mod)
        for nombre, _ in _MODULOS_ORDENADOS
    )
    if hay_desfase_version and not config_recargado and (cfg := sys.modules.get('src.config')) is not None:
        importlib.reload(cfg)
        recargados.add('src.config')
        orden_recarga.append('src.config')
    for nombre, deps in _MODULOS_ORDENADOS:
        mod = sys.modules.get(nombre)
        if mod is None:
            continue
        if nombre == 'src.data' and config_recargado:
            recargados.add('src.data')
            continue
        if any(dep in recargados for dep in deps) or _modulo_obsoleto(nombre, mod):
            importlib.reload(mod)
            recargados.add(nombre)
            orden_recarga.append(nombre)
    return orden_recarga


def parse_count(value):
    return importlib.import_module('src.02_limpieza').convertir_conteo(value)


def parse_list(value):
    return sorted(importlib.import_module('src.02_limpieza').interpretar_generos(value))


def load_clean():
    df = pd.read_csv(CLEAN / 'dataset_depurado.csv')
    df['generos'] = df['generos'].map(json.loads)
    df['organizaciones'] = df['Team'].map(parse_list)
    df['estudio'] = df['organizaciones']
    df['critica_verificada_csv'] = df['Metacritic Rating']
    df['popularidad_indice'] = np.nan
    elegibles = df.elegible_analisis & df[['Plays', 'Wishlist', 'Backlogs']].notna().all(axis=1)
    metadata = MODELS / 'metadata.json'
    if metadata.exists():
        referencia = json.loads(metadata.read_text(encoding='utf-8'))['definicion_objetivo']
        if referencia.get('version') == 'INDICE-PERCENTILES-TRAIN-2.0':
            objetivo = aplicar_referencia(df.loc[elegibles], referencia)
            df.loc[elegibles, 'popularidad_indice'] = objetivo.popularidad_indice
    return df


def prepare():
    importlib.import_module('src.02_limpieza').ejecutar()
    return load_clean(), json.loads((REPORTS / 'inspeccion.json').read_text(encoding='utf-8'))
