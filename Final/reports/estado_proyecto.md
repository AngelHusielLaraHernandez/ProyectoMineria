# Estado del proyecto al cierre de la auditoría

La comparación conserva los 52 identificadores del inventario anterior. Se agrupan HECHO y cumplido como completado. El corte anterior puede recuperarse del commit local de respaldo d390d27.

| Estado | Antes | Después |
|---|---:|---:|
| Completado | 37 | 41 |
| Parcial | 14 | 10 |
| Descartado | 1 | 1 |

El [inventario actualizado](tables/estado_ci.csv) incluye evidencia y desviación por elemento. El [plan de fechas](tables/plan_baseline_git.csv) registra cuándo aparece la evidencia en Git.

## Resultados verificados

- Linaje de datos y maestro intacto. [Dimensiones y origen](tables/procedencia_datos.csv).
- Comparación supervisada y Random Forest activo. [Validación externa](tables/comparativo_modelos.csv), [contrastes](tables/comparacion_estadistica.csv), [prueba y probabilidades](tables/metricas_prueba.csv).
- Perfiles de K-Means, Ward y DBSCAN y agregados de popularidad. [Clustering](clustering.md).
- Casos comerciales y fuentes cotejados en Streamlit y LaTeX. [Reporte](riesgo_comercial.md).
- Weka conserva salidas y capturas verificadas. Orange queda sin resultados. [Verificación actual](verificacion_weka_orange.md) · [Bitácora histórica](BITACORA_UNIFICADA.md).
- Predicción comprobada con el Pipeline y revisión de integridad. [Auditoría de inferencia](revision_predicciones/auditoria.json) y [verificación independiente](verificacion_independiente.json).
- Documento final y plan actualizados en DocumentoFinal. [Procedimiento de despliegue](despliegue.md).

## Alcance pendiente

- **OBJ-05** · Falta una cohorte comparable con ingresos y costos por juego para evaluar pérdidas por género.
- **OBJ-06** · Orange carece de corridas verificadas.
- **OBJ-07** · Publicación sin autorización y redistribución del maestro sin confirmar.
- **ACT-11** · Faltan corridas de Orange.
- **ACT-13** · Orange carece de corridas verificadas.
- **ACT-16** · Instalación en Linux y despliegue remoto sin comprobar.
- **ACT-19** · Falta la presentación/exposición académica final programada para el 25 de noviembre de 2026 y confirmar los pendientes manuales con el profesor
- **CONFIGTEC-1.0** · Orange sin resultados.
- **MODEL-SUP-1.0** · Sin resultados de Orange ni una validación prospectiva independiente.
- **DEPLOY-1.0** · Autorización de publicación, licencias y validación del entorno remoto.
- **DEMO-1.0** · Demostración académica pendiente de acreditación.
