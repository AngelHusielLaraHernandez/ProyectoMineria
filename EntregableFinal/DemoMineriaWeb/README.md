# Ejecutar la web en localhost

Instala **Python 3.14 de 64 bits** desde https://www.python.org/downloads/ y abre una terminal dentro de la carpeta `EntregableFinal`. La primera instalación requiere internet para descargar las dependencias. El modelo guardado se carga con scikit-learn 1.9.1, que ya está fijado en `requirements.txt`.

## Windows · PowerShell

```powershell
cd DemoMineriaWeb
py -3.14 --version
py -3.14 -m venv entorno
.\entorno\Scripts\python.exe -m pip install --upgrade pip
.\entorno\Scripts\python.exe -m pip install -r requirements.txt
.\entorno\Scripts\python.exe -m pip check
.\entorno\Scripts\python.exe iniciar_demo.py
```

Si tu instalación no trae el lanzador `py`, puedes usar `python` en los dos primeros comandos de Python después de confirmar que apunta a la versión 3.14.

## macOS o Linux · Terminal

```bash
cd DemoMineriaWeb
python3.14 --version
python3.14 -m venv entorno
entorno/bin/python -m pip install --upgrade pip
entorno/bin/python -m pip install -r requirements.txt
entorno/bin/python -m pip check
entorno/bin/python iniciar_demo.py
```

Si el sistema instaló Python 3.14 con otro nombre, usa ese ejecutable para crear el entorno. En algunas distribuciones Linux, `venv` se instala como un paquete separado para la misma versión de Python.

## Abrir y probar

- Abre **http://localhost:8501**. Mantén abierta la terminal y usa **Ctrl+C** para cerrar el servidor.
- En **Predicción**, una prueba rápida es seleccionar **RPG** y **Turn Based Strategy**, elegir **Otro**, década **2020**, prensa **92** y usuarios **4.8**. Al analizar el lanzamiento, se muestra **46.9% de popularidad alta** y cinco juegos parecidos.
- Si el puerto 8501 está ocupado, añade `--server.port 8502` al último comando y abre http://localhost:8502.
- El arranque, los filtros y la predicción usan los archivos incluidos. Algunas tarjetas pueden consultar Steam para buscar portadas. Cuando la consulta no está disponible, se sigue mostrando la información del catálogo.

El lanzador lee `config-streamlit.toml` y aplica el tema y la navegación de la app. La versión de Python está en `python-version.txt`.

Los comandos llaman a Python directamente dentro de `entorno`, así que funcionan sin activar el entorno. Si cambias de computadora, vuelve a crearlo con los comandos de arriba. Los archivos de `data/`, `models/` y `reports/` son parte de la misma versión. Mantén sus rutas y contenido para que el manifiesto los pueda validar.
