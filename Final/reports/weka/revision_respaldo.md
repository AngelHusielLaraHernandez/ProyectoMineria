# Revisión del respaldo y las capturas de Weka

Fecha: 2026-11-08T19:35:13.159127-06:00.

Primero se guardó una captura nueva de la ventana actual y un respaldo local; después se verificaron sus contenidos y se actualizó el respaldo final.

## Comprobaciones realizadas

- Se abrieron y revisaron visualmente las seis capturas de resultados: K-Means, DBSCAN, ZeroR, NaiveBayes, J48 y RandomForest. Son legibles y los números visibles corresponden a sus salidas completas.
- Se detectó que las 12 capturas principales tenían contenido JPEG bajo extensión .png. Se corrigió únicamente la codificación a PNG real, conservando sus originales JPEG en capturas_originales_jpeg. Se comprobó igualdad exacta de dimensiones, modo y todos los píxeles antes y después; perfiles de color y EXIF existentes se conservaron. Registro: conversion_capturas.json.
- Las cuatro matrices tienen tres clases, suman 892 y sus diagonales coinciden con los aciertos mostrados. Exactitud y F-Measure ponderada coinciden literalmente con el comparativo, incluido el signo ? de ZeroR.
- K-Means conserva k=2, semilla=42 y tamaños 477/410, que suman 887.
- DBSCAN conserva epsilon=1.666296 y minPoints=12. Sus 887 asignaciones tienen etiqueta 0, con identificadores 0–886 y sin omisiones.
- Se verificaron la integridad CRC del ZIP final, la ausencia de entradas duplicadas y los tamaños y hashes SHA-256 de sus contenidos. No se volvieron a entrenar modelos ni se alteraron sus resultados durante esta revisión.

## Que debo verificar manualmente

- Las capturas muestran la parte visible de cada panel; los TXT conservan las salidas completas.
- El comparativo de Weka usa exactitud en porcentaje y F1 ponderado, no F1 macro.
- Este respaldo acredita las corridas de Weka; Orange se descartó como desviación técnica documentada en reports/codex_log.md.
