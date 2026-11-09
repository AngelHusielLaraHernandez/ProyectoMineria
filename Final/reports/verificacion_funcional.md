# Verificación funcional local

Registro de la primera comprobación del 08/11/2026. La revisión posterior y el formulario actualizado (ambas notas vacías por defecto) se documentan en `revision_integral.md`; los casos siguientes conservan la evidencia histórica, no describen los valores iniciales actuales.

Fecha: 2026-11-08. Se verificó la aplicación servida en `http://127.0.0.1:8501/Consultar_modelo` mediante Chrome y se ejecutó de nuevo la suite desde `Final`.

## Resultados observados

| Comprobación | Resultado |
|---|---|
| Estado inicial de la nota crítica | Campo habilitado, vacío y ausencia desmarcada; no se propone una nota inventada. |
| Envío con nota vacía | Se bloquea y solicita escribir una nota o marcar explícitamente su ausencia. |
| Nota crítica 85, Rating 3.7, década 1980, sin géneros ni organizaciones seleccionados | Predicción medio; probabilidades sin calibrar: bajo 0.404308, medio 0.406572, alto 0.189120. Caso sintético de verificación del formulario, no un videojuego real. |
| Mismo formulario, marcando ausencia de nota crítica | Predicción bajo; probabilidades sin calibrar: bajo 0.513058, medio 0.378036, alto 0.108906. El campo 85 queda deshabilitado y se ignora para la predicción. Se muestra el aviso de imputación y posible sesgo residual. |
| Cinco vecinos de la consulta con ausencia explícita | Se muestran Peggle Deluxe (1475), Ms. Pac-Man (1454), Tetris (1203), Super Mario Bros. 3 (126) y Pac-Man (591), con distancias. Las etiquetas de cluster disponibles se adjuntan por ID; las vacías se explican en pantalla. |
| Pruebas automatizadas | `.venv314/bin/pytest -q`: 82 aprobadas en 3.71 s; una advertencia de joblib sobre detección de núcleos físicos, con uso de núcleos lógicos como alternativa. |
| Integridad de artefactos | SHA-256 de los dos datasets, Pipeline, metadata y vecinos coincide con `reports/manifest.json`. |
| Original | SHA-256 de `../Proyecto/data/processed/games_curated.csv` conserva el valor `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`. |

## Interpretación y decisiones

Se mantuvieron los artefactos y el modelo sin reentrenar: las verificaciones no identificaron un fallo funcional que lo justificara. Los casos del navegador complementan las pruebas automatizadas porque comprueban la interacción real del formulario y sus mensajes.

La ausencia de crítica sigue pudiendo cambiar la predicción. Este ejemplo cruza una frontera de decisión estrecha y no demuestra por sí solo una causa ni un efecto general; el diagnóstico agregado de cobertura y la limitación de la clase media permanecen en `modelo.md` y `correcciones_auditoria2.md`.

La verificación se hizo localmente, sin publicar archivos. Una etiqueta de cluster vacía en los vecinos significa que faltó información para agrupar ese juego; no se fabrica una pertenencia para completar la tabla.

## Que debo verificar manualmente

- Resolver identidad/plataforma de los conflictos históricos 117, 140 y 296 con evidencia externa.
- Confirmar el papel de las organizaciones de Team antes de llamarlas estudios desarrolladores.
- Revisar la representatividad y cobertura de las notas de prensa; quitar indicadores de ausencia no elimina automáticamente su influencia.
- Considerar que el recall de la clase medio es 27/80 (33.75 %) y que las probabilidades no están calibradas.
