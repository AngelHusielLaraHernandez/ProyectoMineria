# Estado y procedimiento de publicación

Por decisión explícita del usuario, el proyecto y sus datos se conservan **solo localmente**. La publicación no está autorizada.
Repositorio remoto detectado: `AngelHusielLaraHernandez/ProyectoMineria`; entrada prevista: `Final/app.py`.
No se hizo push ni se creó un servicio remoto. La rama local de trabajo es `codex/final-videojuegos-curated`; los cambios previos del usuario quedaron fuera del commit de Final.

La revisión automática rechazó el intento de push porque faltaba autorización explícita para transmitir el CSV y sus derivados a GitHub. Se solicitó esa autorización y el usuario eligió conservar todo localmente.
La sesión de Streamlit Cloud sí estaba activa; no hay un bloqueo de cuenta que deba resolverse para usar la app local.

## Ejecución local

Desde Final: `python3.14 -m streamlit run app.py` si las dependencias están instaladas en ese entorno; o `.venv314/bin/python -m streamlit run app.py` con el entorno creado aquí.
Se validaron 17 pruebas en Python 3.14 y en Python 3.15, y se comprobó una predicción en Chrome.

## Referencia para una eventual publicación autorizada

1. Validar `python -m src.pipeline` y `python -m pytest -q` desde Final.
2. Revisar y subir el directorio Final, excluyendo lo indicado por su `.gitignore`.
3. En Streamlit Community Cloud elegir el repositorio, la rama publicada y `Final/app.py`.
4. Seleccionar una versión de Python compatible con `Final/requirements.txt`. Este entorno se validó con Python 3.14; si no está disponible, crear y validar un entorno compatible antes de cambiar versiones fijadas.
5. Confirmar la reconstrucción de artefactos cuando cambie sklearn, consultar las cuatro páginas y probar una predicción.
6. Registrar aquí URL pública, revisión Git desplegada y versión de Python una vez comprobadas.

La documentación oficial describe la selección de repositorio y entrada:
[Desplegar una aplicación](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
Las dependencias pueden colocarse junto a la entrada:
[Organización de archivos](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization).

## Que debo verificar manualmente

- Cuenta, acceso al repositorio, rama y revisión efectivamente desplegada.
- Licencia del CSV, compatibilidad de Python y ausencia de secretos en el commit.
- URL accesible desde una sesión sin autenticar y predicción funcional con datos faltantes.
