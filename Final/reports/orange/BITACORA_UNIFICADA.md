# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: Final/reports/orange/diagnostico_cierres.md

SHA-256: `649d3bd5a831967209db2f73d329f0fd88bba5beefc76ff955565fa5f8fcab6f`

````text
# Diagnóstico de cierres de Orange

## Evidencia confirmada

Se leyeron cuatro reportes del sistema, sin modificar sus fuentes. Todos corresponden al ejecutable PythonApp de Orange y registran EXC_BAD_ACCESS / SIGSEGV (Segmentation fault: 11) en el hilo principal.

El reporte más reciente, Python-2026-11-08-171716.ips, corresponde a /Applications/Orange.app; los tres anteriores corresponden a la copia del volumen externo. Sus capturas son del 08/11/2026, entre 16:56 y 17:17, hora de México. Los símbolos iniciales incluyen objc_release u objc_msgSend, liberación de NSArray y libqcocoa.dylib. El resumen técnico reducido está en diagnostico_cierres.json; no se copiaron reportes completos, identificadores de máquina ni volcados de memoria.

## Interpretación y límites

Hay un cierre real del proceso, no solo pérdida de una ventana en el controlador. La repetición de la pila Qt/Cocoa y su aparición al confirmar selectores apuntan a la interacción gráfica nativa de macOS como hipótesis de trabajo; los reportes no demuestran el disparador preciso ni permiten atribuirlo al CSV, al TAB o al disco externo.

La carga manual de 892 instancias fue reportada exitosa por el usuario, pero no se ha verificado una evaluación gráfica. No se obtuvieron métricas de modelos ni matrices de confusión. No se realizaron nuevas importaciones durante este diagnóstico.

## Prueba propuesta, sin instalación

Se preparó iniciar_con_dialogos_qt.py para establecer AA_DontUseNativeDialogs antes de crear la aplicación gráfica. El enumerado existe en QtCore.pyi de la copia local PyQt6; el punto de entrada Orange.canvas.__main__.main se confirmó en el código de esa aplicación. El lanzador abre Orange y deja las corridas en la interfaz; no entrena modelos por código ni modifica la aplicación.

Esta es una prueba de la hipótesis, no una solución validada. Su ejecución y la reanudación de la GUI quedan pendientes de autorización por la regla 5. El cambio sería temporal, solo en ese proceso; al iniciar Orange normalmente se mantendría su comportamiento original.

## Que debo verificar manualmente

- Que el selector mostrado por la prueba sea el de Qt y no el panel nativo de macOS.
- Que se carguen 892 instancias y nivel_popularidad sea una clase categórica de tres valores antes de evaluar.
- Si persiste el cierre, conservar el reporte nuevo y detener el ensayo sin repetir formatos ni inventar resultados.

````

## Origen: Final/reports/orange/inicio_dialogos_qt.log

SHA-256: `fe9cadde4d98b95a2457f94a38d07e2e94c712b5b8c7d7755bcfe3ec6c02a801`

````text
Incompatible processor. This Qt build requires the following features:
    neon

````

## Origen: Final/reports/orange/inicio_dialogos_qt_arm64.log

SHA-256: `fe9cadde4d98b95a2457f94a38d07e2e94c712b5b8c7d7755bcfe3ec6c02a801`

````text
Incompatible processor. This Qt build requires the following features:
    neon

````
