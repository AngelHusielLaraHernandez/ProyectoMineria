# Fase 1: alcance y contratos de implementación

## Objetivo verificable

Describir recepción, actividad e interés en el maestro de Backloggd; comparar usuarios y prensa con procedencia explícita, explorar perfiles descriptivos y estimar popularidad relativa por terciles. No demostrar ventas, causalidad de fracasos GaaS ni rentabilidad.

## Fuente y unidad de análisis

games_curated.csv es el maestro designado por el usuario: 1,117 filas, 42 columnas, copia inmutable en data/raw. El antecedente de 1,512 filas vive en data/historical y se usa exclusivamente para auditar y reconstruir decisiones históricas.
Cada id_juego identifica una observación por título y fecha. Los títulos compartidos se señalizan; no se fusionan porque Doom o God of War pueden representar obras distintas. Las relaciones se validan por ID.

## Contratos por fase

| Fase | Implementación | Salida y condición verificable |
|---|---|---|
| 1. Alcance | Este documento | Diferenciar popularidad de éxito comercial; registrar maestro y unidad. |
| 2. Inspección | src/01_inspeccion.py | Esquema, procedencia y seis figuras EDA, sin cambiar fuentes. |
| 3. Limpieza | src/02_limpieza.py + src/procedencia.py | dataset_depurado.csv, géneros por ID, balance de filas e historia de cada descarte; conflictos heredados no elegibles hasta revisión. |
| 4A. Asociación y clustering | src/03_clustering.py | Correlación con mínimo de 20 pares; seis variables transformadas; k=2…10, DBSCAN y diagnóstico, alternativas k=3/4 y sensibilidad a títulos. |
| 4A. Comparación de herramienta | src/comparar_weka.py | Ejecución real de K-Means en Weka sobre el mismo espacio, con comandos, hashes, asignaciones y comparación de métricas. |
| 4B. Clasificación independiente | src/04_modelo.py | Objetivo por terciles del promedio de percentiles de Plays, Wishlist y Backlogs, ajustado solo con entrenamiento y de nuevo dentro de cada fold; holdout aproximadamente 80/20 por grupos sin target global y diez folds estratificados por título con objetivos locales. |
| Consulta local | app.py y pages | Lee los mismos artefactos de 4A, comprobados mediante reports/manifest.json. No hay publicación autorizada. |

## Decisiones y límites

**Conflictos históricos.** No se altera la selección del maestro ni se elige una cifra más reciente sin evidencia. Se conservan los tres registros con indicador y se excluyen provisionalmente de inferencia, clustering y clasificación: se informa cobertura y motivo.

**Evidencia histórica.** Reproducir las 42 columnas comprueba trazabilidad, no legitima la regla first ni valida la prensa. Las estimaciones propias se identifican por procedencia y se corrobora su dependencia de Rating sin tratarlas como crítica independiente.

**Perfiles.** K-Means seleccionado por silhouette se contrasta interpretativamente con k=3/4. DBSCAN puede devolver un núcleo y atípicos: se acepta ese resultado como falta de segmentación útil, sin forzar una respuesta favorable.

**Entorno.** Las versiones fijadas son las realmente instaladas y probadas; Python 3.14 está validado localmente. No se inventa compatibilidad de nube ni se cambian versiones solo por parecer poco comunes; los entornos y JAR están excluidos de Git.

## Que debo verificar manualmente

- Plataformas y capturas de las tres discrepancias numéricas; roles de Team.
- Identidad de los juegos con títulos iguales y la representatividad de la muestra.
- Aceptación de evidencia CLI de Weka y de una demo local por el profesor.
