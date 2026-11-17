"""Inicia la demo local con la configuración visible de esta entrega."""

from pathlib import Path
import subprocess
import sys
import tomllib


def main():
    carpeta = Path(__file__).resolve().parent
    with (carpeta / 'config-streamlit.toml').open('rb') as archivo:
        configuracion = tomllib.load(archivo)

    opciones = [
        f'--{seccion}.{clave}={str(valor).lower() if isinstance(valor, bool) else valor}'
        for seccion, valores in configuracion.items()
        for clave, valor in valores.items()
    ]
    comando = [
        sys.executable, '-m', 'streamlit', 'run', 'app.py',
        '--server.address=127.0.0.1', *opciones, *sys.argv[1:],
    ]
    try:
        return subprocess.call(comando, cwd=carpeta)
    except KeyboardInterrupt:
        return 130


if __name__ == '__main__':
    raise SystemExit(main())
