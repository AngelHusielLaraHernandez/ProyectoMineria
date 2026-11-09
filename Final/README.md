# Observatorio de Videojuegos — Edición Phantom Thieves (Persona 5 UI)

Proyecto de minería de datos sobre un catálogo curado de videojuegos de Backloggd y Metacritic (1,117 registros, 1,114 elegibles). Contiene un pipeline reproducible (inspección, limpieza, clustering, clasificación) y una app Streamlit con estética Persona 5.

> Alcance: popularidad **relativa** (interacciones en Backloggd) y brecha usuarios–prensa. No mide ventas ni éxito comercial. Resultados y límites: [`reports/evaluacion.md`](reports/evaluacion.md).

## 1. Ejecución rápida

```bash
cd Final
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py          # http://localhost:8501
pytest -q                     # pruebas
```
> [!NOTE]
> En caso de regenerar datos, clústeres y modelos es necesario ejecutar el script `python -m src.pipeline`.

`requirements.txt` fija las versiones (`scikit-learn==1.9.1`, igual que `models/metadata.json`). `requirements-lock.txt` guarda el entorno completo. Se validó con Python 3.14. Los entornos `.venv`, `.venv314` y `.cache` no se versionan.

## 2. Código fuente (`src/`)

| Archivo | Función |
|---|---|
| `pipeline.py` | Orquesta 01 → 02 → 03 → 04, escribe `reports/manifest.json` con hashes y `huella_pipeline()` (hash de `src/*.py` + `requirements.txt`). |
| `01_inspeccion.py` | Esquema, procedencia de notas, seis figuras EDA → `reports/inspeccion.md/json`, `figures/`. |
| `02_limpieza.py` | Valida el maestro, genera `dataset_depurado.csv`, `generos_largo.csv` y `limpieza_log.md`. |
| `procedencia.py` | Reconstruye 1,512 → 1,117 filas, descartes y conflictos históricos (117, 140, 296). |
| `03_clustering.py` | Correlaciones (Pearson/Spearman, mín. 20 pares, corrección BH), K-Means k = 2…10, DBSCAN, PCA, sensibilidad por título → `reports/clustering*.csv/md`, `dataset_con_clusters.csv`. |
| `comparar_weka.py` | K-Means de Weka 3.8.6 por CLI sobre el mismo espacio (`--descargar` baja los JAR) → `reports/weka/`. |
| `objetivo.py` | Define el índice de popularidad (promedio de rangos percentiles de Plays, Wishlist, Backlogs) y los terciles, ajustados solo con entrenamiento. |
| `features.py` | Preprocesamiento: géneros multi-hot, estudio, década, notas con mediana. |
| `04_modelo.py` | Compara Dummy, CategoricalNB, DecisionTree y RandomForest con `StratifiedGroupKFold` de 10 pliegues. Guarda `models/`. |
| `similitud.py` | `NearestNeighbors` en el espacio predictivo, solo con entrenamiento. |
| `config.py`, `data.py`, `analysis.py`, `modeling.py` | Rutas, carga con caché y adaptadores para la app. |
| `ui.py` | Tema Persona 5: CSS, fuente en Base64, menú lateral, audio, tema Plotly. |

## 3. Datos, modelos y reportes

- `data/raw/games_curated.csv`: maestro inmutable (42 columnas).
- `data/historical/`: antecedente de 1,512 filas, solo para auditoría.
- `data/clean/`: `dataset_depurado.csv`, `dataset_con_clusters.csv`, `generos_largo.csv`, `juegos_modelo.csv` y exportaciones para Weka/Orange.
- `data/export/`: `clustering.*` y `clasificacion.*` (CSV, ARFF, TAB) usados en Weka.
- `models/`: `modelo_popularidad.joblib` (Pipeline portátil con cloudpickle), `vecinos_popularidad.joblib`, `clustering_03.joblib`, `metadata.json`, `referencias_folds.json`.
- `reports/`: `evaluacion.md` (evaluación final), `inspeccion.md`, `limpieza_log.md`, `clustering.md`, `modelo.md`, `hallazgos.md`, `comparacion_weka.md`, `weka/` (corridas gráficas de Weka 3.8.7), `orange/` (diagnóstico de cierres), `tables/comparativo_herramientas.csv`, `manifest.json`. Las carpetas `archivo_*` guardan resultados anteriores a las auditorías.
- `tests/`: pruebas de limpieza, clustering, modelo, auditorías y pipeline.

## 4. Aplicación web

| Página | Archivo | Contenido |
|---|---|---|
| Inicio | `app.py` | Hero, propósito, KPIs, aviso de limitaciones. |
| Exploración | `pages/1_Exploracion.py` | Filtros, distribuciones logarítmicas, Rating frente a Metacritic, brecha por género y estudio, clusters. |
| Predicción | `pages/2_Prediccion.py` | Formulario, probabilidades (bajo/medio/alto, sin calibrar) y 5 vecinos similares. |
| Acerca del modelo | `pages/3_Acerca_del_modelo.py` | Comparación de modelos, matriz de confusión, importancia por permutación. |

Recursos: `assets/css/persona5.css`, `assets/js/interacciones.js`, `assets/fonts/Persona5main.ttf`, `assets/audio/` (BGM y efecto de selección), `assets/img/`. El tema oscuro está en `.streamlit/config.toml`. Los modelos y datos se cachean con `@st.cache_resource` y `@st.cache_data`. Todas las rutas usan `pathlib.Path` relativo a `Final/`. Si falta un artefacto, la app indica ejecutar `python -m src.pipeline`.

## 5. Notas importantes

- No hay despliegue público (ver `reports/despliegue.md`).
- Orange no tiene corridas verificadas. Weka sí (ver `reports/weka/resumen_gui.md`).
- No editar `src/*.py` ni `requirements.txt` sin regenerar el pipeline, porque su hash se registra en el manifiesto.
