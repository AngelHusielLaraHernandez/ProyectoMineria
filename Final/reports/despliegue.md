# Estado y procedimiento de publicación

La publicación pública está pendiente de acceso a una cuenta de Streamlit Community Cloud y de sincronizar el código con GitHub.
Repositorio remoto detectado: `AngelHusielLaraHernandez/ProyectoMineria`; entrada prevista: `Final/app.py`.
No se ha hecho push, alterado la rama main ni creado un servicio remoto desde este trabajo.

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
