# Comparación ejecutada con Weka

Ejecución local real por CLI: Weka 3.8.6 y Java, sin enviar datos a servicios externos. Las salidas originales, comandos, versiones, hashes y asignaciones por id_juego están en reports/weka. No se simula una ejecución de Orange ni una captura de su interfaz.

Ambas herramientas reciben los mismos 887 casos y seis columnas ya transformadas. Weka usa EuclideanDistance -D para desactivar su normalización adicional; no recibe Title ni etiquetas ni género. Python usa 30 inicializaciones, Weka una, con k-means++ y semilla 42; los generadores y criterios de parada pueden diferir.

Silhouette e inercia se recalculan para ambas asignaciones con la misma implementación sobre el mismo espacio. ARI compara particiones sin depender del número asignado a cada cluster; no se presentan números de cluster como correspondencias automáticas.

| k | herramienta | n | silhouette | inercia_comun | ARI_weka_python | tamanos |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | Weka 3.8.6 | 887 | 0.318771290568622 | 3298.5136907203664 | 1.0 | {"0": 422, "1": 465} |
| 2 | sklearn | 887 | 0.318771290568622 | 3298.5136907203664 | 1.0 | {"0": 465, "1": 422} |
| 3 | Weka 3.8.6 | 887 | 0.23584911911092818 | 2748.816578572579 | 0.9702040990038893 | {"0": 399, "1": 304, "2": 184} |
| 3 | sklearn | 887 | 0.23770761869366513 | 2748.3649194969653 | 0.9702040990038893 | {"0": 306, "1": 177, "2": 404} |
| 4 | Weka 3.8.6 | 887 | 0.21890593755013293 | 2461.530540316411 | 0.7820944557579367 | {"0": 225, "1": 267, "2": 219, "3": 176} |
| 4 | sklearn | 887 | 0.22684617714843563 | 2455.4536828792275 | 0.7820944557579367 | {"0": 238, "1": 298, "2": 159, "3": 192} |

Para reproducir con Java instalado: python src/comparar_weka.py --descargar. La descarga obtiene JAR de Maven Central; luego la ejecución es local. Sin --descargar requiere los JAR ya presentes en .cache/weka, excluido de Git.

Fuentes: [artefacto de Weka en Maven Central](https://central.sonatype.com/artifact/nz.ac.waikato.cms.weka/weka-stable/3.8.6) y ayuda de SimpleKMeans conservada junto a la ejecución. La comparación de Fase 4A no sustituye una comparación supervisada futura.

## Que debo verificar manualmente

- Diferencias de inicialización y convergencia antes de atribuir una mejora a la herramienta.
- Que la rúbrica admita evidencia por CLI; no se realizó una demo gráfica de Weka/Orange.
