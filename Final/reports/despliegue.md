# DEPLOY-1.0 · Preparación para Streamlit Community Cloud

**Estado: descartado en la entrega actual.** Se acordó conservar el catálogo, los modelos y sus derivados localmente. La aplicación se comprobó en localhost. Para una publicación futura hacen falta autorización, derechos de redistribución y una prueba en el entorno de alojamiento.

## Licencia y alcance de publicación

La [ficha original de Kaggle](https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023) identifica el recurso atribuido a Arnab Chaki, pero su licencia no fue visible en la consulta pública disponible. Los [términos de Backloggd](https://backloggd.com/about/terms-of-service/) consultados no acreditan un permiso general de redistribución del material. No se confirmó que pueda publicarse el maestro curado. Además de las columnas de Kaggle, el maestro contiene notas agregadas de Metacritic, textos y valores derivados. La app usa imágenes, música, efectos y tipografía que requieren su propia revisión de derechos.

El repositorio local contiene datos y binarios ya rastreados en el historial. `.gitignore` protege secretos y archivos futuros, pero no elimina material previamente versionado. Antes de publicar, la fuente de despliegue debe ser una exportación saneada con archivos autorizados y sin el historial local privado. Para publicar una demo con datos y recursos distintos, regenerar los artefactos compatibles con esa demo y probar las cuatro páginas.

## Checklist para cuando se autorice la publicación

- [ ] Confirmar la licencia en la ficha de Kaggle y su versión. Confirmar por separado permisos sobre datos agregados, textos y recursos visuales y sonoros, o sustituir el material que carezca de autorización.
- [ ] Revisar el inventario de los archivos del repositorio de despliegue y su historial. Incluir exclusivamente recursos autorizados y los artefactos que la app necesita. Comprobar que no haya secretos, historial privado ni evidencia gráfica con datos que no se autorizaron.
- [ ] Confirmar que **Python 3.14** figure en Advanced settings. La documentación vigente admite versiones publicadas que reciben actualizaciones de seguridad. Se verificó localmente con 3.14.6. El valor por defecto documentado es 3.12. [Versiones de Python](https://devguide.python.org/versions/) y [despliegue de Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
- [ ] Usar `Final/app.py` como entrada si se conserva la estructura. `Final/requirements.txt` va junto a la entrada y `.streamlit/config.toml` en la raíz del repositorio. Confirmar las reglas de precedencia de dependencias y ejecutar desde la raíz, igual que Community Cloud. [Organización de archivos](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization) y [dependencias](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies).
- [ ] Comprobar en Linux que se instalen las versiones fijadas y carguen los modelos, y ejecutar las pruebas con la misma versión menor de Python. La prueba local en macOS no acredita esa instalación.
- [ ] Verificar en la revisión desplegada el inicio, filtros y descargas, los tres agrupamientos, la predicción con y sin nota de prensa y el panel Modelo. Registrar revisión, versión de Python y URL.

Para verificar desde la raíz en local: `Final/.venv/bin/python -m streamlit run Final/app.py`.
