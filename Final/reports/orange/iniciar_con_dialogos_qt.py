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
