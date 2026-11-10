# Carpeta: Final/reports/orange

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `Final/reports/orange/BITACORA_UNIFICADA.md` · Bytes: 3404 · SHA-256: `24f4d96a7e3afdf47d7dbb88012b8a33b78ba28b7f64320a66aec4b993b01853`

`````text
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

`````

## aviso_inicial.png

Ruta: `Final/reports/orange/aviso_inicial.png` · Bytes: 220084 · SHA-256: `c844c333eb36b0861607bfe5d75a69362d6754f6307bd7419774b61aabe9607f`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## diagnostico_cierres.json

Ruta: `Final/reports/orange/diagnostico_cierres.json` · Bytes: 5427 · SHA-256: `773b6625956d23aaaed860ec884881a84bb281172c6cda3dadfc771b56a00010`

````text
[
  {
    "reporte": "Python-2026-11-08-171716.ips",
    "captura": "2026-11-08 17:17:14.1490 -0600",
    "proceso": "/Applications/Orange.app/Contents/MacOS/PythonApp",
    "excepcion": "EXC_BAD_ACCESS",
    "senal": "SIGSEGV",
    "terminacion": "Segmentation fault: 11",
    "hilo": 0,
    "pila_inicial": [
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_release"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libqcocoa.dylib",
        "simbolo": null
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "AutoreleasePoolPage::releaseUntil(objc_object**)"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_autoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "_CFAutoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__CFRunLoopPerCalloutARPEnd"
      }
    ]
  },
  {
    "reporte": "Python-2026-11-08-170816.ips",
    "captura": "2026-11-08 17:08:15.0191 -0600",
    "proceso": "/Volumes/VOLUME/*/Orange.app/Contents/MacOS/PythonApp",
    "excepcion": "EXC_BAD_ACCESS",
    "senal": "SIGSEGV",
    "terminacion": "Segmentation fault: 11",
    "hilo": 0,
    "pila_inicial": [
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_release"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libqcocoa.dylib",
        "simbolo": null
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "AutoreleasePoolPage::releaseUntil(objc_object**)"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_autoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "_CFAutoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__CFRunLoopPerCalloutARPEnd"
      }
    ]
  },
  {
    "reporte": "Python-2026-11-08-170148.ips",
    "captura": "2026-11-08 17:01:45.7171 -0600",
    "proceso": "/Volumes/VOLUME/*/Orange.app/Contents/MacOS/PythonApp",
    "excepcion": "EXC_BAD_ACCESS",
    "senal": "SIGSEGV",
    "terminacion": "Segmentation fault: 11",
    "hilo": 0,
    "pila_inicial": [
      {
        "biblioteca": "libobjcMsgSend.dylib",
        "simbolo": "objc_msgSend"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libqcocoa.dylib",
        "simbolo": null
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "AutoreleasePoolPage::releaseUntil(objc_object**)"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_autoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "_CFAutoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__CFRunLoopPerCalloutARPEnd"
      }
    ]
  },
  {
    "reporte": "Python-2026-11-08-165714.ips",
    "captura": "2026-11-08 16:56:58.7058 -0600",
    "proceso": "/Volumes/VOLUME/*/Orange.app/Contents/MacOS/PythonApp",
    "excepcion": "EXC_BAD_ACCESS",
    "senal": "SIGSEGV",
    "terminacion": "Segmentation fault: 11",
    "hilo": 0,
    "pila_inicial": [
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_release"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libqcocoa.dylib",
        "simbolo": null
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__RELEASE_OBJECTS_IN_THE_ARRAY__"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "-[__NSArrayM dealloc]"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "AutoreleasePoolPage::releaseUntil(objc_object**)"
      },
      {
        "biblioteca": "libobjc.A.dylib",
        "simbolo": "objc_autoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "_CFAutoreleasePoolPop"
      },
      {
        "biblioteca": "CoreFoundation",
        "simbolo": "__CFRunLoopPerCalloutARPEnd"
      }
    ]
  }
]
````

## dialogo_recuperacion.png

Ruta: `Final/reports/orange/dialogo_recuperacion.png` · Bytes: 40472 · SHA-256: `4e83ac945e4ec63e233141916b3395f55a7c58ad9b112a29e7e0874a6ae2991c`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## iniciar_con_dialogos_qt.py

Ruta: `Final/reports/orange/iniciar_con_dialogos_qt.py` · Bytes: 667 · SHA-256: `f01d8e873f71b1bdda7b06e363a817aeff3a34b63341345ace51f56d457a0a54`

````text
"""Inicio gráfico alternativo de Orange, pendiente de autorización para ejecutar.

Ejecutar con el intérprete incluido en Orange, desde la carpeta Final.
El cambio solo afecta este proceso; no instala ni altera la aplicación.
No carga datos ni ejecuta algoritmos por código: las corridas siguen en la GUI.
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    # Debe fijarse antes de que Orange cree QApplication y los selectores.
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeDialogs, True)
    from Orange.canvas.__main__ import main

    raise SystemExit(main(sys.argv))

````

## inicio_tras_fallo_tab.png

Ruta: `Final/reports/orange/inicio_tras_fallo_tab.png` · Bytes: 86002 · SHA-256: `76185c90171abdb2dde36a00b92c71f32d235332b9c635705fd2a5dc132a1176`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

