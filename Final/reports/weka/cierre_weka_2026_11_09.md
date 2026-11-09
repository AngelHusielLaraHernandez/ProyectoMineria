# Cierre de pendientes de Weka — 9 de noviembre de 2026

Se revisaron los entregables pedidos para Weka 3.8.7. No se encontraron corridas ni archivos pendientes dentro de ese alcance. Las seis corridas ya realizadas conservan sus salidas completas, capturas y valores; no se volvieron a entrenar durante esta revisión.

| Entregable | Comprobación | Estado |
| --- | --- | --- |
| Entradas de clustering | 887 filas, seis variables; CSV y ARFF idénticos valor por valor | Completo |
| SimpleKMeans | k=2, semilla 42, seis centroides por variable, tamaños 477/410 y captura | Completo |
| DBSCAN | eps=1.666296, minPoints=12, 887 asignaciones verificadas y captura | Completo |
| Clasificación | 892 filas, 53 atributos; último atributo nivel_popularidad nominal; CSV y ARFF idénticos | Completo |
| ZeroR, NaiveBayes, J48, RandomForest | Diez pliegues estratificados, salidas completas y matrices que suman 892 | Completo |
| Comparativo | Exactitud y F-Measure ponderada transcritas sin diferencias frente a las salidas | Completo |
| Capturas y respaldo | Imágenes válidas, hashes e integridad del ZIP verificados | Completo |

Se volvió a abrir Explorer y se cargó clasificacion.arff. La interfaz confirmó 892 instancias, 53 atributos y Class: nivel_popularidad (Nom). Evidencia nueva: [captura actual de Explorer](revision_explorer_2026_11_09.jpg). Las clases del archivo contienen alto=297, medio=297 y bajo=298.

Auditoría detallada: [auditoria_cierre_2026_11_09.json](auditoria_cierre_2026_11_09.json). Los resultados de rendimiento siguen en [resumen_gui.md](resumen_gui.md).

## Que debo verificar manualmente

- Estas comprobaciones corresponden a Weka; Orange se descartó como desviación técnica documentada en reports/codex_log.md.
- Weka muestra F1 ponderado y exactitud en porcentaje; no confundirlos con F1 macro y el conjunto de prueba de Python.
- Las diferencias de clustering frente a Python se conservan registradas; no se ajustaron parámetros para igualarlas.
