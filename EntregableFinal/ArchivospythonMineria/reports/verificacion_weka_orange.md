# Verificación de Weka y desviación de Orange

## Weka

Se verificaron por SHA-256 las salidas y capturas del manifiesto gráfico de Explorer 3.8.7. Las matrices se contrastaron con aciertos y exactitud. Los CSV exportados coinciden con los datos de origen y los ARFF contienen los mismos atributos y valores fila por fila. La declaración nominal del ARFF nuevo explicita el orden bajo, medio, alto. La evidencia histórica se obtuvo desde CSV y Weka mostró alto, bajo, medio. El orden nominal puede afectar desempates en corridas nuevas. No se repitió la sesión gráfica porque las filas de entrada se conservaron.

Archivos producidos: `tables/verificacion_weka_entradas.csv`, `tables/comparativo_herramientas.csv` y ARFF nominal verificado en `data/export`.

## Orange

Orange 3.40.0 sufrió cierres nativos SIGSEGV de Qt/Cocoa en macOS al automatizar selectores de archivos. La bitácora de Orange documenta intentos con File, CSV File Import, TAB, recuperación y arranque limpio, instalación local por el usuario y lanzador con selectores Qt. Ninguno produjo una evaluación guardada.

Se hizo un único reintento sin interfaz con el Python de la aplicación instalada y `import Orange`, preparado para cargar la copia local `clasificacion.tab`. Abortó con código 134 y el mensaje «Incompatible processor. This Qt build requires the following features: neon». El aborto ocurrió antes de leer el TAB. No se instaló software, no se intentó otro método y no se reportan métricas de Orange.
