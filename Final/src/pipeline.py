"""Cadena canónica: inspección → limpieza → clustering → clasificación independiente."""
import hashlib
import importlib
import json
import shutil
from .config import ROOT, RAW, REPORTS
from .data import load_clean
from .modeling import train
from .metodos_clase import evaluar_ward
from .analisis_integral import ejecutar as analizar
from .comparativo_integral import ejecutar as comparar

REPORTES_APP = (
    'clustering_03_parametros.json', 'clustering_03_correlaciones_catalogo.csv',
    'clustering_03_correlaciones_generos.csv', 'clustering_03_correlaciones_organizaciones.csv',
    'clustering_03_correlaciones_ranking_generos.csv', 'clustering_03_perfiles.csv',
    'clustering_03_alternativas_k.csv', 'clustering_03_seleccion_kmeans.csv',
    'clustering_03_sensibilidad_dbscan.csv',
    'clase_comparacion_clustering.csv', 'clase_ward_cortes.csv',
    'clase_ward_asignaciones.csv', 'clase_ward_perfiles.csv', 'clase_ward_dendrograma.json',
    'tables/modelo_importancia_gini.csv', 'tables/calibracion.csv', 'tables/comparativo_modelos.csv',
    'tables/comparacion_estadistica.csv', 'tables/comparacion_prueba_actual_e_historica.csv',
    'tables/perfiles_clusters.csv', 'tables/metricas_clusters.csv', 'tables/bic_gmm.csv',
    'tables/popularidad_genero.csv', 'tables/popularidad_estudio.csv',
    'tables/correlacion_catalogo.csv', 'tables/procedencia_datos.csv', 'tables/parametros_clustering.csv',
)


def huella_pipeline():
    rutas = [RAW, ROOT / 'data/historical/games_actualizado_metacritic.csv', ROOT / 'requirements.txt', *sorted((ROOT / 'src').glob('*.py'))]
    h = hashlib.sha256()
    for ruta in rutas:
        if ruta.exists():
            h.update(str(ruta.relative_to(ROOT)).encode())
            h.update(ruta.read_bytes())
    return h.hexdigest()


def main():
    importlib.import_module('src.01_inspeccion').ejecutar()
    importlib.import_module('src.02_limpieza').ejecutar()
    parametros = importlib.import_module('src.03_clustering').ejecutar()
    if (ROOT / '.cache/weka/weka-stable-3.8.6.jar').exists() and shutil.which('java'):
        from .comparar_weka import ejecutar
        ejecutar()
    # Fase supervisada: solo datos depurados; nunca etiquetas ni scaler de clusters.
    evaluar_ward()
    analizar()
    metricas = train(load_clean())
    comparar()
    (REPORTS / 'analisis.json').write_text(json.dumps(parametros, ensure_ascii=False, indent=2))
    texto = f"""# Hallazgos de la cadena canónica

Fuente maestra: data/raw/games_curated.csv, sin modificar. Historia de 1,512 registros y decisiones heredadas: trazabilidad_historica.md.
La inspección, limpieza, clustering y app comparten dataset_depurado.csv y dataset_con_clusters.csv. El análisis completo de asociación está en clustering.md, con mínimo de 20 pares por grupo.

Fase 4A: {parametros['n_completos']} casos completos elegibles de {parametros['n_entrada']} registros conservados; {parametros['n_conflictos_historicos']} conflictos históricos pendientes excluidos del análisis principal.
K-Means usa seis variables y k={parametros['kmeans_k']} entre 2 y 10. DBSCAN usa eps={parametros['dbscan_eps']:.6f}, min_samples={parametros['dbscan_min_samples']}; clusters={parametros['dbscan_clusters']}, ruido={parametros['dbscan_ruido']}.
Un solo grupo de DBSCAN no acredita segmentación comercial útil. Ver comparación de k=2/3/4 y sensibilidad a títulos compartidos en clustering.md.

Clasificador independiente por terciles del promedio de rangos percentiles de Plays, Wishlist y Backlogs: {metricas['modelo']}; n prueba={metricas['n_prueba']}, F1 macro={metricas['metricas']['f1_macro']:.4f}, base={metricas['metricas']['f1_macro_referencia']:.4f}. Los clusters descriptivos no se utilizan como objetivo ni predictores.

## Que debo verificar manualmente

- Resolver plataformas de discrepancias históricas y roles de Team.
- Interpretar distancias de puntuaciones separadas de asociación de orden.
- Confirmar estabilidad de perfiles; popularidad no equivale a éxito comercial.
"""
    (REPORTS / 'hallazgos.md').write_text(texto, encoding='utf-8')
    actualizar_manifiesto()
    print(texto)


def actualizar_manifiesto():
    manifest = {'huella_pipeline': huella_pipeline(), 'fuente_clustering': 'data/clean/dataset_depurado.csv',
                'artefacto_clustering': 'data/clean/dataset_con_clusters.csv',
                'modelo_popularidad': 'models/modelo_popularidad.joblib',
                'metadata_modelo': 'models/metadata.json',
                'sha256_modelo_popularidad': hashlib.sha256((ROOT / 'models/modelo_popularidad.joblib').read_bytes()).hexdigest(),
                'sha256_metadata_modelo': hashlib.sha256((ROOT / 'models/metadata.json').read_bytes()).hexdigest(),
                'sha256_vecinos': hashlib.sha256((ROOT / 'models/vecinos_popularidad.joblib').read_bytes()).hexdigest(),
                'sha256_dataset_depurado': hashlib.sha256((ROOT / 'data/clean/dataset_depurado.csv').read_bytes()).hexdigest(),
                'sha256_dataset_con_clusters': hashlib.sha256((ROOT / 'data/clean/dataset_con_clusters.csv').read_bytes()).hexdigest(),
                'sha256_reportes_app': {nombre: hashlib.sha256((REPORTS / nombre).read_bytes()).hexdigest()
                                       for nombre in REPORTES_APP}}
    (REPORTS / 'manifest.json').write_text(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
