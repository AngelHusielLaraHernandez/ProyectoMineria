# Observatorio de videojuegos

Proyecto independiente desarrollado en `Final`. El contenido anterior de `Proyecto` se conserva.
Fuente original designada por el usuario: `Proyecto/data/processed/games_curated.csv`.
Se conserva una copia exacta e inmutable en `data/raw/games_curated.csv`; el pipeline solo escribe derivados en Final.

## Inspección real de la fuente original

- **1,117 filas y 42 columnas**. No hay duplicados de título y fecha en este maestro ya curado.
- `Rating`: 0.7–4.8 observados, 13 faltantes. `rating_100` refleja una conversión previa por 20, pero no acredita por sí misma la escala teórica.
- `Metacritic Rating`: 45–99, incluyendo estimaciones. Para análisis se usa **`critic_score_final`**, con 899 notas y 218 ausencias; `critic_source` distingue `metacritic_csv` y `none`.
- Las 218 filas de crítica estimada se conservan como juegos, sin usar su nota sintética. Hay 890 pares completos para Pearson.
- `Plays`, `Playing`, `Backlogs`, `Wishlist` ya son numéricas; el parser admite además sufijos K/M si aparecen en una futura versión.
- `Genres` y `Team` son listas serializadas. `studio_main` y `publisher_main` existen, pero la lógica local anterior los asignó por posición de Team, no por funciones documentadas.
- Se conserva el maestro con todas sus columnas. La vista analítica reconstruye listas y fechas y no usa `rating_100`, `gap`, `gap_real`, `studio_main`, `publisher_main` ni cifras financieras estimadas.
- Años 1980–2025 y tres fechas `releases on TBD`. La fecha del scrape no está documentada en el CSV.
- `Times Listed` y `Number of Reviews` son idénticas; no se usan como dos señales independientes.
- El hash y el inventario completo están en `reports/inspeccion.json`. Los resultados previos calculados con otro CSV quedan sustituidos.

## Reproducir

Ejecutar desde la carpeta `Final`, con Python 3.14 (entorno validado):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m src.pipeline
python -m pytest -q
python -m streamlit run app.py
```

`requirements.txt` fija dependencias directas; `requirements-lock.txt` registra también las transitivas usadas en esta ejecución.
Las rutas se resuelven con `pathlib` desde el proyecto. Las operaciones aleatorias usan semilla 42 y los artefactos registran versiones.
No se necesita consultar APIs, Kaggle ni Metacritic para repetir esta ejecución. No se actualizan automáticamente las cifras originales.

## Decisiones de diseño

**Conservar evidencia.** Se copia el CSV sin modificar y se registra su SHA-256; los descartes y conflictos se exportan.
Los duplicados sin conflicto conservan la primera fila; los títulos con cifras distintas se excluyen completos hasta revisión.

**Comparación de valoraciones.** Pearson se calcula con las escalas originales y únicamente con pares completos marcados Metacritic.
Mide asociación, no diferencia de notas; calcular una brecha exige confirmar primero la escala de usuarios y la comparabilidad de plataformas.

**Géneros y organizaciones múltiples.** Cada juego pertenece a todos los géneros y miembros de Team, sin elegir un principal arbitrario.
Se reportan n, IC95 % y corrección BH por familia; con menos de diez pares o sin variación no se estima r. Los grupos no son independientes ni aditivos.

**Popularidad observable.** El índice es el promedio de log(1 + conteo) de las cuatro señales con pesos iguales.
Reduce la dominancia de Plays y conserva ceros, pero expresa una decisión de ponderación; los conteos permanecen visibles para distinguir actividad e intención.

**Agrupación.** K-Means y DBSCAN usan exclusivamente las cuatro señales con log1p y StandardScaler; es análisis descriptivo de la muestra completa.
K-Means maximiza silhouette entre k=2…8; DBSCAN explora eps y min_samples, exige cobertura ≥70 % y maximiza silhouette sin ruido por cobertura. Se conserva toda la búsqueda.

**Evaluación supervisada.** Se reserva aproximadamente 20 % por grupos de título antes de calcular terciles; se mantienen empates en la misma clase.
Cinco folds agrupados recalculan cortes, codificadores e imputación en cada entrenamiento. Se comparan base mayoritaria, regresión logística y bosque, eligiendo por F1 macro interno.

**Atributos y límites.** Géneros y Team se codifican como indicadores múltiples; década como categoría, notas con mediana e indicador de ausencia.
Los conteos y el índice no entran al clasificador. No se usan notas estimadas como prensa; las probabilidades se muestran sin atribuirles calibración.

**Modelo publicado.** Se conserva el modelo ajustado solo con entrenamiento, exactamente el que produjo las métricas de prueba.
La app lo carga junto con su preprocesamiento; si sklearn cambia o faltan artefactos, reconstruye el pipeline, sin usar prueba para seleccionar el modelo.

**Interfaz.** Tablas, filtros y navegación nativos de Streamlit para una consulta académica legible.
Los avisos de escala, procedencia y alcance acompañan los resultados, con estados vacíos y descarga de consultas.

## Resultados y archivos

Consultar `reports/hallazgos.md`, `reports/metricas.json`, matrices de confusión y tablas completas por grupo.
Los CSV limpios y perfiles están en `data/clean`; los pipelines serializados, en `models`; los gráficos, en `reports/figures`.
Los nombres de clusters son identificadores sin orden, no perfiles comerciales validados.

DBSCAN concentra la mayoría de juegos en un grupo; una silhouette alta no demuestra segmentación comercial útil.
K-Means principalmente separa niveles de las señales. Se necesita comprobar estabilidad y sensibilidad de los pesos antes de atribuir significado de mercado.

## Orange, Weka y Power BI

- Orange: importar `data/clean/entrenamiento_orange.csv`, elegir `nivel_popularidad` como objetivo y conectar el archivo `prueba_orange.csv` como prueba separada. No volver a hacer una partición aleatoria si se comparan métricas con Python.
- Weka: cargar `entrenamiento_weka.arff`, fijar el último atributo como clase y usar `prueba_weka.arff` en Supplied test set. `diccionario_weka.csv` traduce los nombres de atributos.
- Los dos formatos contienen atributos ya transformados con entrenamiento, sin título, índice ni conteos. Los algoritmos y sus parámetros pueden diferir de sklearn; no se promete igualdad de resultados.
- Power BI: importar `games.csv`, `perfiles.csv` y tablas de `reports`; relacionar juegos y perfiles por `ID Original`, no por título. Las correlaciones por grupo ya están calculadas y no deben sumarse.
- No se generaron ni validaron flujos `.ows`, `.model` de Weka ni `.pbix`: se proporcionan datos interoperables e instrucciones, sin simular ejecuciones de esas herramientas.

## Publicación

La app funciona localmente. **No hay un despliegue público verificado.** Consultar `reports/despliegue.md` para el procedimiento y los requisitos de cuenta.
No subir `.venv`, cachés ni secretos. El CSV contiene contenido de terceros; confirmar su licencia y la de los agregados antes de redistribuirlo públicamente.

## Que debo verificar manualmente

- Escala teórica de usuarios, enlaces y plataforma de cada nota crítica, y origen de las estimaciones propias.
- Roles de Team, la deduplicación previa del maestro, las tres fechas TBD y la fecha real de captura.
- Licencia y atribución del dataset y de las notas agregadas para una publicación pública.
- Robustez de los pesos del índice y de los clusters; representatividad frente a otros juegos y franquicias.
- Uso correcto de particiones en Orange/Weka y relaciones sin duplicación en Power BI.
- Versión de Python disponible en el alojamiento y comprobación de la URL pública después del despliegue.
