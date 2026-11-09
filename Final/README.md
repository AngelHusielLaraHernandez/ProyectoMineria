# Observatorio de Videojuegos — Edición Phantom Thieves (Persona 5 UI)

Aplicación web interactiva de minería de datos construida con **Python**, **Streamlit**, **Plotly** y **scikit-learn**, diseñada bajo la identidad visual y sonora de **Persona 5 (Phantom Thieves / UI Shujin)**.

Analiza la relación entre la recepción comunitaria (`Rating` en Backloggd), la crítica especializada (`Metacritic Rating`) y las señales de tracción de jugadores (`Plays`, `Playing`, `Backlogs`, `Wishlist`) sobre un catálogo curado de **1,117 títulos únicos** (depurados a partir de **1,512 registros históricos**).

---

## 1. Arquitectura y Estructura del Repositorio

Todas las rutas se resuelven de forma estrictamente relativa a la raíz de `Final/` mediante `pathlib.Path`, garantizando portabilidad total entre entornos locales (macOS, Linux, Windows) y **Streamlit Community Cloud**:

```text
Final/
├── app.py                      # Página 1: Inicio (Hero P5, propósito, KPIs y callout de sesgos)
├── pages/
│   ├── 1_Exploracion.py        # Página 2: EDA logarítmico, brecha usuarios-crítica y clustering
│   ├── 2_Prediccion.py         # Página 3: Menú de Batalla P5 (inferencia + 5 NearestNeighbors)
│   └── 3_Acerca_del_modelo.py  # Página 4: Comparativa de modelos, matriz de confusión e importancia
├── assets/
│   ├── fonts/                  # Persona5main.ttf (inyectada vía Base64)
│   ├── audio/                  # select.mp3, background.mp3 (Velvet Audio Console)
│   ├── img/                    # hero.png, card.png, jokerface2.png, char1-3.png, icons
│   └── css/                    # persona5.css (polígonos irregulares, Calling Cards, hover invertido)
├── .streamlit/
│   └── config.toml             # Tema oscuro P5 (primary #d92323, bg #0d0d0d)
├── data/
│   ├── raw/                    # games_curated.csv (fuente maestra inmutable)
│   ├── historical/             # games_actualizado_metacritic.csv (trazabilidad 1,512 filas)
│   └── clean/                  # games_curated.csv, dataset_depurado.csv, dataset_con_clusters.csv
├── models/                     # modelo_popularidad.joblib, vecinos_popularidad.joblib, metadata.json
├── reports/                    # Métricas, correlaciones BH-FDR, perfiles y manifest.json
├── src/                        # Pipeline canónico (01_inspeccion a 04_modelo), ui.py y similitud.py
├── tests/                      # Suite automatizada pytest + Streamlit AppTest
└── requirements.txt            # Dependencias con versiones fijas (scikit-learn==1.9.1)
```

---

## 2. Requisitos e Instalación

1. **Crear y activar un entorno virtual** (Python 3.11+ / 3.14):
   ```bash
   cd Final
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

2. **Instalar dependencias con versiones fijas** (la versión de `scikit-learn==1.9.1` coincide con `models/metadata.json`):
   ```bash
   pip install -r requirements.txt
   ```

3. **(Opcional) Regenerar todos los artefactos de datos, clustering y modelos desde cero:**
   Si falta algún archivo en `data/clean/`, `models/` o `reports/`, la interfaz mostrará una pantalla temática **`CRITICAL ALERT // MISSION FAILED`** indicando ejecutar:
   ```bash
   python -m src.pipeline
   ```

---

## 3. Ejecución de la Aplicación Web

Desde el directorio `Final/`, ejecuta:

```bash
streamlit run app.py
```

La aplicación abrirá automáticamente en tu navegador (por defecto en `http://localhost:8501`).

### Navegación de Páginas
- **Inicio (`app.py`):** Cabecera Hero *"Take Your Heart"*, contexto ejecutivo sobre la brecha crítica y riesgos en modelos *GaaS*, tarjetas KPI angulares (1,117 títulos únicos, rango 1980–2025, géneros y organizaciones), advertencia de sesgo de supervivencia y explorador rápido del catálogo.
- **Exploración (`pages/1_Exploracion.py`):** Filtros tácticos en barra lateral (género, década, rangos de calificación), distribuciones logarítmicas (`Plays`, `Wishlist`, `Backlogs`), diagrama de dispersión/densidad `Rating` vs. `Metacritic`, ranking de brecha usuarios-crítica (`Rating × 20 − Metacritic`) por género y estudio, y proyección PCA 2D de clustering (`K-Means` y `DBSCAN`).
- **Predicción (`pages/2_Prediccion.py`):** Formulario estilo *Menú de Batalla P5* con validación de entrada, probabilidades del clasificador supervisado (`RandomForestClassifier`), perfil de mercado por cluster, los **5 videojuegos más similares** (`NearestNeighbors` ajustado exclusivamente en entrenamiento), brecha típica contextual del género y leyenda legal obligatoria.
- **Acerca del Modelo (`pages/3_Acerca_del_modelo.py`):** Lectura dinámica de `models/metadata.json` y `reports/`, tabla y gráfico comparativo (`DummyClassifier`, `CategoricalNB`, `DecisionTreeClassifier`, `RandomForestClassifier`), mapa de calor de la matriz de confusión (`n = 222` en prueba) e importancia por permutación (`Permutation Importance`).

---

## 4. Pruebas Automatizadas

Para verificar la integridad científica, ausencia de fuga de información y renderizado de las 4 páginas con `AppTest`:

```bash
pytest -q
```
