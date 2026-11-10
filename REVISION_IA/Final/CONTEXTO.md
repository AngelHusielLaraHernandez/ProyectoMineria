# Carpeta: Final

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## .gitignore

Ruta: `Final/.gitignore` · Bytes: 90 · SHA-256: `658d308e80f75dd757ed5f3db735c1d93221874cb4f847a155258e80c8b1693f`

````text
.venv/
.venv314/
__pycache__/
.pytest_cache/
.cache/
.impeccable/
.streamlit/secrets.toml

````

## DESIGN.md

Ruta: `Final/DESIGN.md` · Bytes: 889 · SHA-256: `5e3013c1ee6b3b5e3c028db957f28371cb5dafb7d12381af4634283a3e273a18`

````text
# Interfaz de consulta académica

Modo: operar. Navegación lateral de Streamlit, encabezados breves y una tarea principal por página.
Tablas y formularios nativos: conservan teclado, foco y adaptación de Streamlit. Los gráficos muestran unidades y alcance.

## Tokens

Fuente: sans serif nativa, escala tipográfica de Streamlit.
Fondo `#fafaf7`, superficie secundaria `#eeeee8`, texto `#202d2b`, acción `#17645b`.
Sin animaciones decorativas ni métricas presentadas como garantía de éxito.

## Estados y evidencia

Filtros con estado vacío; errores de preparación con recuperación explícita; predicción solicitada mediante formulario.
Se probaron las cuatro páginas, la búsqueda vacía y la predicción con valores ausentes mediante AppTest.
La consulta principal se revisó visualmente en Chrome. El alcance visual no equivale a una auditoría completa de accesibilidad.

````

## PRODUCT.md

Ruta: `Final/PRODUCT.md` · Bytes: 1056 · SHA-256: `27fca0e0604363e4f2db64f2796d050370a00a6beec98bfb02b6ec2ebcffa2e4`

````text
# Observatorio de videojuegos

## Platform
web

## Stack
Python y Streamlit, indicados por el usuario. Datos y modelos locales, sin APIs necesarias para reproducir.

## Propósito y evidencia
Consultar valoración, actividad, interés, perfiles de mercado y clasificación relativa de popularidad.
Fuente indicada: Backloggd vía Kaggle, Arnab Chaki, con agregados locales. La atribución no sustituye la verificación de licencia.
El maestro designado games_curated.csv contiene 42 columnas y 1,117 registros; sus estimaciones se distinguen de la crítica marcada como Metacritic.

## Restricciones confirmadas
No inventar datos, usar semilla 42, rutas portables, comentarios y mensajes en español.
Conservar el trabajo anterior en Proyecto y desarrollar aquí. No inferir escala ni funciones de Team.

## Supuestos declarados
Uso académico para explorar y presentar hallazgos. Interfaz de consulta con tablas y controles nativos de Streamlit.
No hay referencias visuales vinculantes. Se priorizan legibilidad y acceso a metodología sobre decoración.

````

## README.md

Ruta: `Final/README.md` · Bytes: 5012 · SHA-256: `1ab587da492fcad734d3e8235b3cf3545c87e41416a19bbf8b40dc21b9e77353`

````text
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
- Orange no tiene corridas verificadas. Weka sí (ver `reports/weka/BITACORA_UNIFICADA.md`).
- No editar `src/*.py` ni `requirements.txt` sin regenerar el pipeline, porque su hash se registra en el manifiesto.

````

## app.py

Ruta: `Final/app.py` · Bytes: 25837 · SHA-256: `3767e5a232bedb83904964014893c25f05875066cd521e8a949fa5445923d2fe`

````text
"""Página de Inicio: Observatorio de Videojuegos — Edición Phantom Thieves (Persona 5 UI)."""
import importlib
import streamlit as st

import src.ui as _ui

if not hasattr(_ui, 'asset_b64') or getattr(_ui, '_UI_VERSION', None) != 'p5-v8-neon':
    importlib.reload(_ui)

from src.config import SIGNALS
from src.ui import (
    asset_b64,
    manual_checks,
    render_html,
    render_lb_rb_nav,
    resources,
    section_banner,
    setup,
)

setup(
    'Observatorio de Videojuegos',
    'Phantom Thieves Edition · Menú Interactivo Persona 5 · Backloggd & Metacritic',
    transition='default',
    menu_idx=0,
    compact_menu=False,
)

df, bundle, analysis = resources()
metricas_modelo = bundle['metricas']

# ---------------------------------------------------------------------------
# 1. CABECERA HERO ("TAKE YOUR HEART" CON ASSETS/IMG/)
# ---------------------------------------------------------------------------
hero_b64 = asset_b64('img/hero.png')
joker_b64 = asset_b64('img/jokerface2.png')
hero_img_html = (
    f'<img class="p5-hero-img" src="data:image/png;base64,{joker_b64}" alt="Phantom Thieves"/>'
    if joker_b64 else ''
)
logo_img_html = (
    f'<img src="data:image/png;base64,{hero_b64}" width="175" '
    f'style="filter:drop-shadow(4px 4px 0 #000);margin-bottom:0.4rem;" alt="Take Your Heart"/>'
    if hero_b64 else ''
)

render_html(
    f"""
    <div class="p5-hero">
        <div>
            {logo_img_html}
            <div class="p5-hero-badge">PHANTOM THIEVES DATA OBSERVATORY // SHUJIN ACADEMY</div>
            <div class="p5-hero-title">TAKE YOUR HEART: BRECHA CRITICA Y POPULARIDAD</div>
            <p class="p5-hero-sub">
                Investigación empírica sobre la industria del videojuego: contrastamos la recepción de la
                comunidad de jugadores (Backloggd) frente a la prensa especializada (Metacritic), evaluamos
                la actividad y el interés registrados, y describimos perfiles de recepción y popularidad.
                El catálogo no permite medir pérdidas ni riesgo comercial de <em>Games as a Service (GaaS)</em>.
            </p>
        </div>
        {hero_img_html}
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. PROPÓSITO DEL PROYECTO — BARRAS DESLIZANTES DE PERSONAJES (Socials.jsx / AboutMe.jsx)
# ---------------------------------------------------------------------------
render_lb_rb_nav('MISSION BRIEFING // PARTY')

char1_b64 = asset_b64('img/char1.png')
char2_b64 = asset_b64('img/char2.png')
char3_b64 = asset_b64('img/char3.png')

render_html(
    f"""
    <div class="sc-root" role="region" aria-label="Propósito Ejecutivo del Proyecto">
        <!-- BAR 1: LEADER // INDUSTRIA -->
        <div class="sc-bar-outer active">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char1_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">LEADER</div>
                    <div class="sc-main">
                        <div class="sc-label">01 // INDUSTRIA &amp; TRACCION</div>
                        <div class="sc-subdesc">
                            Separamos alcance acumulado (Plays) de interés pendiente (Wishlist / Backlogs) sobre los 1,117 registros del maestro games_curated.csv; el antecedente histórico contiene 1,512 registros.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">HIST</span>
                                <span class="sc-stat-num">1,512</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">MAESTRO</span>
                                <span class="sc-stat-num">1,117</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--secondary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- BAR 2: PARTY // BRECHA USUARIOS VS CRITICA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char2_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">PARTY</div>
                    <div class="sc-main">
                        <div class="sc-label">02 // BRECHA COMUNIDAD-PRENSA</div>
                        <div class="sc-subdesc">
                            Correlación moderada (r = 0.544 en 887 pares elegibles según CSV). La brecha y la asociación por género y organización se consultan en Exploración; Team no acredita funciones de desarrollador.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">PAIRS</span>
                                <span class="sc-stat-num">887</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--accent);border-color:var(--accent);">PEARSON</span>
                                <span class="sc-stat-num">0.544</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--accent);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- BAR 3: PARTY // RIESGOS GAAS & INFERENCIA -->
        <div class="sc-bar-outer">
            <div class="sc-bar-red"></div>
            <div class="sc-bar">
                <img class="sc-char" src="data:image/png;base64,{char3_b64}" alt=""/>
                <div class="sc-bar-fill"></div>
                <div class="sc-bar-shade"></div>
                <div class="sc-bar-content">
                    <div class="sc-role">PARTY</div>
                    <div class="sc-main">
                        <div class="sc-label">03 // RIESGO GAAS &amp; MODELADO</div>
                        <div class="sc-subdesc">
                            Estimamos popularidad relativa y consultamos cinco vecinos del entrenamiento. No hay una variable de juegos como servicio ni datos de rentabilidad para cuantificar su riesgo.
                        </div>
                    </div>
                    <div class="sc-stats">
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--primary);border-color:var(--primary);">F1 TEST</span>
                                <span class="sc-stat-num">{metricas_modelo['metricas']['f1_macro']:.3f}</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--primary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                        <div class="sc-stat">
                            <div class="sc-stat-top">
                                <span class="sc-stat-tag" style="color:var(--secondary);border-color:var(--secondary);">KNN</span>
                                <span class="sc-stat-num">TOP 5</span>
                            </div>
                            <div class="sc-stat-bars">
                                <div class="sc-stat-bar-color" style="background:var(--secondary);"></div>
                                <div class="sc-stat-bar-black"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 2. MÉTRICAS GENERALES (KPIs) — CONFIDANT RANK CARDS & DETAIL PANEL (ResumePage.jsx)
# ---------------------------------------------------------------------------
anios_validos = df['anio'].dropna().astype(int)
rango_temporal = f'{int(anios_validos.min())}–{int(anios_validos.max())}' if len(anios_validos) else '1980–2023'
generos_unicos = sorted({g for row in df['generos'] for g in row})
estudios_unicos = sorted({org for row in df['organizaciones'] for org in row})
frecuencias_generos = df['generos'].explode().dropna().value_counts()
top_generos = frecuencias_generos.head(3)

render_html(
    f"""
    <div class="resume-grid">
        <div class="resume-stack">
            <div class="resume-list-tag">LIST // KPIS</div>

            <div class="resume-card-wrap active" data-detail-target="kpi-1">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">I</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">CATALOGO</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TOTAL</div>
                            <div class="resume-rank-number">{len(df):,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">1,117 REGISTROS EN EL MAESTRO CURADO; ANTECEDENTE HISTORICO DE 1,512</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-2">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">II</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">HORIZONTE</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">SPAN</div>
                            <div class="resume-rank-number">1980-25</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">COBERTURA HISTORICA {rango_temporal} (ANALISIS HASTA 2025)</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-3">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">III</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">GENEROS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TAXON</div>
                            <div class="resume-rank-number">{len(generos_unicos)}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">MULTI-ETIQUETA CON 15 GENEROS FRECUENTES EN EL MODELO</div>
                    </div>
                </div>
            </div>

            <div class="resume-card-wrap" data-detail-target="kpi-4">
                <div class="resume-card">
                    <div class="resume-badge"><div class="resume-badge-text">IV</div></div>
                    <div class="resume-card-inner">
                        <div class="resume-title">ESTUDIOS</div>
                        <div class="resume-rank">
                            <div class="resume-rank-label">TEAMS</div>
                            <div class="resume-rank-number">{len(estudios_unicos):,}</div>
                        </div>
                    </div>
                    <div class="resume-subtitle-bar">
                        <div class="resume-subtitle">ORGANIZACIONES ANALIZADAS EN EL CAMPO TEAM DE BACKLOGGD</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PANELES DE DETALLE DINÁMICOS (ResumePage.jsx .resume-detail-panel) -->
        <div>
            <div class="resume-detail-panel" data-detail-id="kpi-1" style="display:block;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">01</div>
                    <div class="resume-detail-top-title">CATALOGO LOG</div>
                    <div class="resume-detail-top-progress">1,117</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Registros Históricos Originales</div>
                        <div class="resume-detail-status">1,512 FILAS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Títulos Únicos por Nombre y Fecha</div>
                        <div class="resume-detail-status">1,117 JUEGOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Cohorte Elegible Sin Conflicto</div>
                        <div class="resume-detail-status">{metricas_modelo['n_cohorte']:,} CASOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Pares Elegibles con Ambas Notas</div>
                        <div class="resume-detail-status">{analysis['n_completos']:,} PARES</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-2" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">02</div>
                    <div class="resume-detail-top-title">TEMPORAL LOG</div>
                    <div class="resume-detail-top-progress">1980-25</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Rango Observado en Dataset</div>
                        <div class="resume-detail-status">{rango_temporal}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Horizonte Analítico del Proyecto</div>
                        <div class="resume-detail-status">1980–2025</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Décadas Codificadas One-Hot</div>
                        <div class="resume-detail-status">1980s A 2020s</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Títulos sin Fecha Conocida</div>
                        <div class="resume-detail-status">DECADA -1</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-3" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">03</div>
                    <div class="resume-detail-top-title">GENRE TAXONOMY</div>
                    <div class="resume-detail-top-progress">{len(generos_unicos)} GEN</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Género Dominante en Catálogo</div>
                        <div class="resume-detail-status">{top_generos.index[0]} ({top_generos.iloc[0]})</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Segundo y Tercer Género</div>
                        <div class="resume-detail-status">{' / '.join(f'{g} ({n})' for g, n in top_generos.iloc[1:].items())}</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Umbral de Correlación por Grupo</div>
                        <div class="resume-detail-status">MINIMO 20 PARES</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Codificación en Clasificador</div>
                        <div class="resume-detail-status">MULTI-HOT + OTRO</div>
                    </div>
                </div>
            </div>

            <div class="resume-detail-panel" data-detail-id="kpi-4" style="display:none;">
                <div class="resume-detail-top">
                    <div class="resume-detail-top-index">04</div>
                    <div class="resume-detail-top-title">STUDIOS &amp; TEAMS</div>
                    <div class="resume-detail-top-progress">{len(estudios_unicos)} ORG</div>
                </div>
                <div class="resume-detail-list">
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">01</div>
                        <div class="resume-detail-row-title">Organización con Mayor Presencia</div>
                        <div class="resume-detail-status">NINTENDO (170)</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">02</div>
                        <div class="resume-detail-row-title">Siguientes por Volumen</div>
                        <div class="resume-detail-status">CAPCOM / SQUARE ENIX</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">03</div>
                        <div class="resume-detail-row-title">Frecuencia Mínima en Modelo</div>
                        <div class="resume-detail-status">&gt;= 10 TITULOS</div>
                    </div>
                    <div class="resume-detail-row">
                        <div class="resume-detail-row-index">04</div>
                        <div class="resume-detail-row-title">Respaldo para Estudios Independientes</div>
                        <div class="resume-detail-status">CLASE OTRO</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 3. AVISO DE LIMITACIONES METODOLÓGICAS (CALLOUT ROJO / OSCURO)
# ---------------------------------------------------------------------------
render_html(
    """
    <div class="p5-callout-warning">
        <div class="p5-callout-title">⚠️ AVISO METODOLOGICO Y LIMITACIONES DEL ESTUDIO (CALLING CARD)</div>
        <ul style="margin:0;padding-left:1.25rem;color:#f2f2f2;line-height:1.55;font-size:0.95rem;">
            <li><strong>Sesgo de supervivencia hacia juegos populares:</strong> La muestra original procede de listados curados de Backloggd con alta visibilidad comunitaria; no representa una muestra aleatoria de todos los lanzamientos comerciales de la industria.</li>
            <li><strong>Ausencia de fracasos comerciales puros:</strong> Los niveles de popularidad (<em>bajo</em>, <em>medio</em>, <em>alto</em>) son <strong>relativos a los terciles del conjunto de entrenamiento</strong> dentro de este catálogo popular, no absolutos respecto al mercado global.</li>
            <li><strong>Advertencia sobre datos de ventas:</strong> Las señales <code>Plays</code>, <code>Playing</code>, <code>Backlogs</code> y <code>Wishlist</code> reflejan registros de actividad en plataforma social en un corte temporal; <strong>no equivalen a unidades vendidas ni a ingresos en USD</strong>.</li>
        </ul>
    </div>
    """
)

# ---------------------------------------------------------------------------
# 4. EXPLORADOR RÁPIDO DEL CATÁLOGO MAESTRO
# ---------------------------------------------------------------------------
section_banner('Explorador Rápido del Catálogo', 'Consulta Directa de Títulos y Señales de Popularidad')

a, b = st.columns([2, 1])
query = a.text_input('Buscar título', placeholder='Escribe parte del nombre (ej. Persona, Zelda, Elden Ring)')
genre = b.selectbox('Género', ['Todos', *generos_unicos])

view = df[df['Title'].str.contains(query, case=False, regex=False, na=False)]
if genre != 'Todos':
    view = view[view['generos'].map(lambda row: genre in row)]

labels = {
    'popularidad_indice': 'Índice de popularidad',
    'critica_verificada_csv': 'Prensa según CSV (Metacritic)',
    'Rating': 'Valoración de usuarios (0–5)',
    'Plays': 'Plays · alcance acumulado',
    'Playing': 'Playing · actividad',
    'Backlogs': 'Backlogs · pendientes',
    'Wishlist': 'Wishlist · deseos',
}
order = st.selectbox(
    'Ordenar por',
    ['popularidad_indice', *SIGNALS, 'Rating', 'critica_verificada_csv'],
    format_func=labels.get,
)

st.caption(
    f'Juegos visibles: {len(view):,} de {len(df):,} registros únicos por título y fecha. '
    'Conteos de una captura; no son ventas.'
)
st.caption(
    'El índice usa solo percentiles de Plays, Wishlist y Backlogs contra la referencia de entrenamiento. '
    'Playing se muestra como contexto y solo interviene en el EDA/clustering.'
)

shown = view.sort_values(order, ascending=False)[
    [
        'id_juego',
        'Title',
        'conflicto_historico_pendiente',
        'anio',
        'Rating',
        'critica_verificada_csv',
        *SIGNALS,
        'popularidad_indice',
    ]
]

if len(shown):
    st.dataframe(
        shown,
        hide_index=True,
        width='stretch',
        column_config={
            'Title': 'Videojuego',
            'anio': st.column_config.NumberColumn('Año', format='%d'),
            'critica_verificada_csv': 'Prensa según CSV',
            'popularidad_indice': st.column_config.NumberColumn('Índice de popularidad', format='%.3f'),
        },
    )
    st.download_button(
        'Descargar esta consulta (CSV)',
        shown.to_csv(index=False).encode('utf-8'),
        'consulta_phantom_thieves.csv',
        'text/csv',
    )
else:
    st.info('No hay coincidencias. Cambia el título o selecciona Todos en género.')

with st.expander('Cómo se define el Índice de Popularidad (Sin Fuga de Información)'):
    st.latex(r'I=\frac{P_{\text{train}}(\text{Plays})+P_{\text{train}}(\text{Wishlist})+P_{\text{train}}(\text{Backlogs})}{3}')
    st.write(
        'P se ajusta con rangos medios/N solo en la partición de entrenamiento (n = 892). '
        'Para los demás juegos se interpola contra esa referencia congelada: 0 por debajo del mínimo '
        'y 1 por encima del máximo de entrenamiento. Las tres señales pesan lo mismo; Wishlist y Backlogs '
        'representan interés pendiente y están correlacionadas. Playing se muestra como contexto, pero no '
        'construye el objetivo ni entra al clasificador. No es una medida de ventas o rentabilidad.'
    )

manual_checks()

````

## pytest.ini

Ruta: `Final/pytest.ini` · Bytes: 42 · SHA-256: `b160d82f7811555051f8966d8e02750a985227c1d022208c784e606946f2eada`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## requirements-lock.txt

Ruta: `Final/requirements-lock.txt` · Bytes: 849 · SHA-256: `11d78966be859ebd62255cf07c4c36fcaaf8660cfa3ee4182b0b18e54a93a0f6`

````text
altair==6.3.0
anyio==4.16.0
attrs==26.1.0
certifi==2026.10.23
charset-normalizer==3.5.2
click==8.5.1
cloudpickle==3.1.2
contourpy==1.4.0
cycler==0.12.1
fonttools==4.68.0
h11==0.16.0
idna==3.20
iniconfig==2.3.1
itsdangerous==2.2.0
Jinja2==3.1.6
joblib==1.6.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
kiwisolver==1.5.1
MarkupSafe==3.0.4
matplotlib==3.11.2
narwhals==2.28.0
numpy==2.5.4
packaging==26.3
pandas==3.1.1
pillow==13.0.0
plotly==7.1.0
pluggy==1.7.0
protobuf==7.36.2
pyarrow==26.0.1
pydeck==0.9.3
Pygments==2.21.0
pyparsing==3.3.3
pytest==9.2.0
python-dateutil==4.0.0
python-multipart==0.0.33
referencing==0.37.0
requests==2.34.2
rpds-py==2026.9.1
scikit-learn==1.9.1
scipy==1.18.1
starlette==1.10.0
streamlit==1.67.0
threadpoolctl==3.8.0
typing_extensions==4.16.0
tzdata==2026.6
urllib3==2.8.0
uvicorn==0.54.0
websockets==17.4

````

## requirements.txt

Ruta: `Final/requirements.txt` · Bytes: 159 · SHA-256: `7452f835f1a463ef3f4a6a9e624750e9fea9c404f02d7438b7a060a98a02a249`

````text
cloudpickle==3.1.2
joblib==1.6.0
matplotlib==3.11.2
numpy==2.5.4
pandas==3.1.1
plotly==7.1.0
pytest==9.2.0
scikit-learn==1.9.1
scipy==1.18.1
streamlit==1.67.0

````

