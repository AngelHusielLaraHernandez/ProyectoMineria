"""Actualiza los estados de la auditoría preservando los identificadores originales."""
from collections import Counter
import csv
from datetime import datetime
import json
from pathlib import Path
from zoneinfo import ZoneInfo

REPORTES = Path(__file__).resolve().parent
CSV = REPORTES / 'tables/estado_ci.csv'
ACTUALIZADOS = {
    'OBJ-04': ('cumplido', 'Final/reports/tables/popularidad_genero.csv; Final/reports/tables/popularidad_estudio.csv',
               'Ninguno en el alcance descriptivo.', 'Popularidad de interacciones del catálogo. Team agrupa organizaciones mencionadas.'),
    'OBJ-05': ('parcial', 'Final/reports/tables/metricas_clusters.csv; Final/reports/tables/perfiles_clusters.csv; Final/reports/tables/bic_gmm.csv; Final/reports/riesgo_comercial.md',
               'Falta una cohorte comparable con ingresos y costos por juego para evaluar pérdidas por género.',
               'Se documentan los tres métodos de agrupamiento y casos publicados sobre desempeño comercial.'),
    'OBJ-06': ('parcial', 'Final/reports/tables/comparativo_modelos.csv; Final/reports/tables/comparativo_herramientas.csv; Final/models/metadata.json',
               'Orange carece de corridas verificadas.', 'La MLP se evaluó en Python. Random Forest queda activo. La clase media conserva la menor recuperación.'),
    'OBJ-07': ('parcial', 'Final/app.py; Final/reports/despliegue.md',
               'Publicación sin autorización y redistribución del maestro sin confirmar.', 'La app opera localmente.'),
    'ACT-11': ('parcial', 'Final/reports/clustering.md; Final/reports/BITACORA_UNIFICADA.md; Final/reports/verificacion_weka_orange.md',
               'Faltan corridas de Orange.', 'Weka conserva sus salidas. Python y la web incluyen los tres algoritmos.'),
    'ACT-12': ('HECHO', 'Final/reports/tables/metricas_clusters.csv; Final/reports/tables/bic_gmm.csv; Final/reports/tables/perfiles_clusters.csv',
               '', 'Se verifican la pertenencia, los índices disponibles y el alcance de DBSCAN.'),
    'ACT-13': ('PARCIAL', 'Final/reports/tables/comparativo_herramientas.csv; Final/reports/tables/comparativo_modelos.csv',
               'Orange carece de corridas verificadas.', 'Se comparan cinco modelos de Python, cuatro salidas de Weka y se documenta la desviación de Orange.'),
    'ACT-15': ('HECHO', 'Final/app.py; Final/pages/1_Exploracion.py; Final/pages/2_Prediccion.py; Final/pages/3_Acerca_del_modelo.py',
               '', 'Se comprobaron filtros, métricas, formulario local y los cuatro casos del selector comercial.'),
    'ACT-16': ('PARCIAL', 'Final/reports/despliegue.md; Final/reports/verificacion_independiente.json',
               'Instalación en Linux y despliegue remoto sin comprobar.', 'Publicación descartada para la entrega privada.'),
    'ACT-17': ('HECHO', 'DocumentoFinal/main.tex; DocumentoFinal/main.pdf; Final/reports/tables/plan_baseline_git.csv',
               'Motivos de las desviaciones de calendario requieren confirmación del equipo.', 'El informe compila e incorpora los casos comerciales, sus fuentes y el diseño de comparación por género.'),
    'ACT-18': ('HECHO', 'README.md; Final/reports/evaluacion.md; Final/reports/revision_predicciones/auditoria.json',
               '', 'Cifras, artefacto de inferencia, documentación y comparativo sincronizados.'),
    'ACT-20': ('HECHO', 'Final/reports/evaluacion.md; Final/reports/verificacion_independiente.json; Final/reports/tables/evidencia_comercial.csv',
               '', 'Se verificaron resultados analíticos y los casos comerciales con sus fuentes.'),
    'DATA-RAW-1.0': ('HECHO', 'Final/data/raw/games_curated.csv; Final/data/historical/games_actualizado_metacritic.csv; Final/reports/tables/procedencia_datos.csv',
                     'El archivo exacto de 15 columnas del anteproyecto no se encontró.', 'El maestro se conserva inmutable. El antecedente local de 20 columnas permite reconstruirlo.'),
    'CONFIG-ENV-1.0': ('HECHO', 'Final/.python-version; Final/requirements.txt; Final/requirements-lock.txt; Final/models/metadata.json',
                       '', 'El venv y los modelos se regeneraron en Python 3.14.6. Se reutilizaron paquetes locales ante la falta de acceso al índice.'),
    'CONFIGTEC-1.0': ('PARCIAL', 'Final/reports/BITACORA_UNIFICADA.md; Final/reports/verificacion_weka_orange.md; Final/reports/tables/verificacion_weka_entradas.csv',
                      'Orange sin resultados.', 'La alternativa sin interfaz abortó con requisito NEON de Qt.'),
    'CLUSTER-REPORT-1.0': ('HECHO', 'Final/reports/clustering.md; Final/reports/tables/perfiles_clusters.csv; Final/reports/tables/metricas_clusters.csv',
                           '', 'Se completa el informe de agrupamiento. La ausencia de Orange se registra en CONFIGTEC-1.0.'),
    'MODEL-SUP-1.0': ('PARCIAL', 'Final/src/04_modelo.py; Final/reports/modelo.md; Final/reports/tables/comparativo_herramientas.csv',
                      'Sin resultados de Orange ni una validación prospectiva independiente.', 'Se completaron las corridas previstas de Python y las cuatro comparaciones de Weka.'),
    'MODEL-FILE-1.0': ('HECHO', 'Final/models/metadata.json; Final/reports/revision_predicciones/auditoria.json',
                       '', 'Se verificaron las probabilidades, las etiquetas y el espacio de vecinos del bosque.'),
    'EVAL-REPORT-1.0': ('HECHO', 'Final/reports/evaluacion.md; Final/reports/tables/comparacion_estadistica.csv',
                        '', 'Las referencias apuntan a las tablas y bitácoras vigentes.'),
    'APP-WEB-1.0': ('HECHO', 'Final/app.py; Final/pages/1_Exploracion.py; Final/pages/2_Prediccion.py; Final/pages/3_Acerca_del_modelo.py',
                     '', 'Se muestran cinco candidatos, importancia de Gini, fiabilidad y advertencia ética.'),
    'DEPLOY-1.0': ('DESCARTADO', 'Final/reports/despliegue.md; .streamlit/config.toml; Final/requirements.txt',
                    'Autorización de publicación, licencias y validación del entorno remoto.', 'La decisión vigente es conservar el proyecto localmente.'),
    'SEG-1.0': ('HECHO', 'Final/reports/weka/RESPALDO_UNIFICADO.zip; DocumentoFinal/ProyectoMineriaDatos_LaTeX.zip',
                '', 'Respaldo inicial y bloques registrados localmente en Git.'),
    'HW-PC-1.0': ('HECHO', 'Final/models/metadata.json; Final/reports/BITACORA_UNIFICADA.md',
                   '', 'Entorno local macOS verificado con Python 3.14.6. Se conservaron las evidencias de Weka.'),
    'DEMO-1.0': ('PARCIAL', 'Final/app.py; DocumentoFinal/main.pdf; Final/reports/verificacion_independiente.json',
                 'Demostración académica pendiente de acreditación.', 'La demostración técnica local se comprobó con Random Forest.'),
    'DOC-PLAN-1.0': ('HECHO', 'README.md; DocumentoFinal/main.tex; Final/reports/tables/plan_baseline_git.csv',
                     'La fecha de terminación y los motivos de calendario requieren respaldo del equipo.', 'El plan muestra la línea base y fechas de la primera evidencia en Git.'),
}


def contar(filas):
    return Counter('Completado' if f['estado'].upper() in {'HECHO', 'CUMPLIDO'}
                   else f['estado'].capitalize() for f in filas)


def ejecutar():
    with CSV.open(encoding='utf-8', newline='') as entrada:
        filas = list(csv.DictReader(entrada))
    ruta = REPORTES / 'tables/estado_ci_resumen.json'
    previo = json.loads(ruta.read_text())['antes'] if ruta.exists() else dict(contar(filas))
    fecha = datetime.now(ZoneInfo('America/Mexico_City')).strftime('%Y-%m-%d')
    for fila in filas:
        cambio = ACTUALIZADOS.get(fila['id'])
        if cambio:
            fila['estado'], fila['evidencia'], fila['falta'], fila['desviacion_motivo'] = cambio
            fila['fecha_archivo'] = fecha
    with CSV.open('w', encoding='utf-8', newline='') as destino:
        salida = csv.DictWriter(destino, fieldnames=list(filas[0]), lineterminator='\n')
        salida.writeheader()
        salida.writerows(filas)
    actual = contar(filas)
    ruta.write_text(json.dumps({'total': len(filas), 'antes': previo, 'despues': dict(actual)}, ensure_ascii=False, indent=2) + '\n')
    lineas = ['# Estado del proyecto al cierre de la auditoría', '',
              'La comparación conserva los 52 identificadores del inventario anterior. Se agrupan HECHO y cumplido como completado. '
              'El corte anterior puede recuperarse del commit local de respaldo d390d27.', '',
              '| Estado | Antes | Después |', '|---|---:|---:|']
    for estado in ['Completado', 'Parcial', 'Descartado']:
        lineas.append(f'| {estado} | {previo.get(estado, 0)} | {actual[estado]} |')
    lineas += ['', 'El [inventario actualizado](tables/estado_ci.csv) incluye evidencia y desviación por elemento. '
               'El [plan de fechas](tables/plan_baseline_git.csv) registra cuándo aparece la evidencia en Git.', '',
               '## Resultados verificados', '',
               '- Linaje de datos y maestro intacto. [Dimensiones y origen](tables/procedencia_datos.csv).',
               '- Comparación supervisada y Random Forest activo. [Validación externa](tables/comparativo_modelos.csv), '
               '[contrastes](tables/comparacion_estadistica.csv), [prueba y probabilidades](tables/metricas_prueba.csv).',
               '- Perfiles de K-Means, Ward y DBSCAN y agregados de popularidad. [Clustering](clustering.md).',
               '- Casos comerciales y fuentes cotejados en Streamlit y LaTeX. [Reporte](riesgo_comercial.md).',
               '- Weka conserva salidas y capturas verificadas. Orange queda sin resultados. [Verificación actual](verificacion_weka_orange.md) · [Bitácora histórica](BITACORA_UNIFICADA.md).',
               '- Predicción comprobada con el Pipeline y revisión de integridad. [Auditoría de inferencia](revision_predicciones/auditoria.json) '
               'y [verificación independiente](verificacion_independiente.json).',
               '- Documento final y plan actualizados en DocumentoFinal. [Procedimiento de despliegue](despliegue.md).',
               '', '## Alcance pendiente', '']
    lineas += [f"- **{f['id']}** · {f['falta']}" for f in filas if f['estado'].upper() in {'PARCIAL', 'DESCARTADO'}]
    (REPORTES / 'estado_proyecto.md').write_text('\n'.join(lineas) + '\n', encoding='utf-8')
    print(ruta.read_text())


if __name__ == '__main__':
    ejecutar()
