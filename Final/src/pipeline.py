"""Ejecutar desde Final: python -m src.pipeline."""
import os
os.environ.setdefault('MPLCONFIGDIR', '.cache/matplotlib')
os.environ.setdefault('XDG_CACHE_HOME', '.cache')

from .data import prepare
from .analysis import analyze
from .modeling import train
from .config import REPORTS


def main():
    df, inspection = prepare()
    analysis = analyze(df)
    metrics = train(df)
    r = analysis['pearson_global']
    text = f'''# Hallazgos calculados

Fuente original designada: `Proyecto/data/processed/games_curated.csv`.
Copia inmutable: `data/raw/games_curated.csv`. SHA-256: `{inspection['sha256']}`.
Se observaron {inspection['filas']} filas, {inspection['columnas']} columnas y {inspection['duplicados_descartados']} repeticiones de título y fecha.
Títulos con conflictos analíticos en esta fuente: {len(inspection['conflictos_analiticos'])}; filas en conflicto: {inspection['filas_en_conflicto']}.
Quedan {len(df)} videojuegos por título y fecha; años {inspection['rango_anios']}.

Pearson usuarios–prensa: n={r['n']}, r={r['r']:.4f}, IC95 % [{r['ic95_inferior']:.4f}, {r['ic95_superior']:.4f}].
Es asociación lineal, no diferencia de medias ni causalidad. La procedencia Metacritic es una etiqueta del CSV, no una auditoría externa.
Los grupos con menos de 10 pares o sin variación quedan sin estimación; los CSV por grupo incluyen n, IC y q de Benjamini–Hochberg.

K-Means eligió k={analysis['kmeans_k']} por silhouette entre 2 y 8. DBSCAN usa eps={analysis['dbscan']['eps']} y min_samples={analysis['dbscan']['min_samples']:.0f}.
Su selección cumplió el criterio de cobertura y silhouette: {analysis['dbscan_criterio_valido']}. Ver tablas completas y medianas antes de nombrar perfiles.

Clasificador elegido en validación interna: {metrics['modelo']}.
Prueba reservada: {metrics['n_prueba']} juegos; accuracy={metrics['accuracy']:.4f}, balanced accuracy={metrics['balanced_accuracy']:.4f}, F1 macro={metrics['f1_macro']:.4f}.
F1 macro de la base mayoritaria: {metrics['f1_macro_base']:.4f}. Los cortes del índice son {metrics['cortes_entrenamiento']}.

La popularidad es relativa a esta muestra de Backloggd. No mide ventas, ingresos, rentabilidad ni fracaso de juegos como servicio.
Las notas son posteriores al lanzamiento; el clasificador describe popularidad contemporánea y no constituye un pronóstico previo al estreno.

## Que debo verificar manualmente

- Escala teórica de Rating y enlaces de procedencia de Metacritic, incluyendo plataforma y fecha de cada nota.
- Roles reales de Team: no se puede atribuir un resultado a desarrolladores con esta columna sin curarla.
- Fecha del scrape, redondeo de conteos, títulos con versiones distintas y fechas TBD.
- Sesgo de selección de juegos populares y dependencia entre juegos de una misma franquicia o estudio.
- Sensibilidad del índice a sus pesos iguales y estabilidad de clusters en otras muestras.
'''
    (REPORTS / 'hallazgos.md').write_text(text, encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
