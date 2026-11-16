# Log de limpieza

SHA-256 del insumo inmutable: `b23cc1c4c23e65171bbe8a3436c358773cee15b8e11b446261cd575daa625acd`.

Fuente: `data/raw/games_curated.csv`. Decisiones previas: `reports/inspeccion.md`.

| Paso | Filas antes | Filas después | Eliminadas | Razón del cambio | Detalle |
|---|---:|---:|---:|---|---|
| 1. Validación y conversión de conteos | 1117 | 1117 | 0 | Sin cambio de filas | En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución. |
| 2. Fechas | 1117 | 1117 | 0 | Sin cambio de filas | 0 fechas ausentes y 3 no interpretables; no se eliminan juegos. |
| 3. Géneros | 1117 | 1117 | 0 | Sin cambio de filas | Primer género no vacío como convención de presentación; tabla larga tras deduplicar. |
| 4. Faltantes y procedencia | 1117 | 1117 | 0 | Sin cambio de filas | Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa. |
| 5. Duplicados | 1117 | 1117 | 0 | Sin cambio de filas | Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución. |
| 6. Escalas y brecha | 1117 | 1117 | 0 | Sin cambio de filas | Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra. |
| 7. Preparación de exportación | 1117 | 1117 | 0 | Sin cambio de filas | Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one. |

## Decisiones y justificación

**Conteos y fechas.** Se convierten solo formatos numéricos reconocidos; los inválidos causan un error con columna y fila. Las fechas desconocidas o imposibles se conservan como NaT con indicador: inventar un año alteraría el análisis por década.

**Faltantes.** No se imputan notas ni se eliminan juegos por ausencia. La imputación estadística pertenece al entrenamiento dentro de cada fold; en análisis descriptivo se usan pares completos e indicadores para mostrar la cobertura.

**Procedencia.** Se conserva Metacritic original en metacritic_rating_original y se usa critic_score_final con su etiqueta de fuente para la columna analítica. Una nota derivada de Rating no aporta evidencia independiente de prensa; la etiqueta del CSV no demuestra verificación externa.

**Géneros.** El primer elemento no vacío es una convención de presentación, no un género dominante acreditado. La tabla larga conserva cada género distinto y el ID; sus filas no se suman para contar juegos únicos.

**Duplicados.** Solo se descartan equivalencias analíticas bajo la clave documentada y se guardan las filas eliminadas. Un conflicto impide exportar para evitar seleccionar una cifra sin fundamento.

## Verificación de escalas previa a la brecha

Fuentes primarias consultadas el 08/11/2026: [Backloggd, extremo superior de cinco estrellas](https://backloggd.com/games/elden-ring/) y [Metacritic, escala 0–100](https://metacritichelp.zendesk.com/hc/en-us/articles/15456550496023-How-do-I-interpret-a-Metascore). No se descargan ni sustituyen puntuaciones actuales.

Conversión por máximo documentado: `rating_normalizado = Rating × 100 / 5`; `brecha = rating_normalizado − Metacritic Rating`. Positiva: usuarios por encima de prensa; negativa: por debajo. No se trasladan los extremos observados de la muestra a 0 y 100, ni se afirma equivalencia psicométrica.

Rango observado Rating: 0.7–4.8; Metacritic original: 45–99; crítica analítica: 45–99.

## Conciliación comprobable

El bloque JSON permite contrastar el log con la tabla exportada. Toda disminución requiere una razón; ningún otro paso puede añadir o eliminar juegos.

```json
{
  "filas_entrada": 1117,
  "filas_salida": 1117,
  "filas_generos_largo": 2682,
  "pasos": [
    {
      "paso": "1. Validación y conversión de conteos",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "En seis columnas: 6702 celdas ya numéricas, 0 textos K/M convertidos, 0 textos numéricos convertidos y 0 nulos conservados. Los formatos inválidos detienen la ejecución."
    },
    {
      "paso": "2. Fechas",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "0 fechas ausentes y 3 no interpretables; no se eliminan juegos."
    },
    {
      "paso": "3. Géneros",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Primer género no vacío como convención de presentación; tabla larga tras deduplicar."
    },
    {
      "paso": "4. Faltantes y procedencia",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Sin imputación: Rating=13 ausentes; Metacritic original=0; notas estimadas=218; Metacritic analítico=218 ausentes. La columna original se conserva en metacritic_rating_original; las notas estimadas no se presentan como prensa."
    },
    {
      "paso": "5. Duplicados",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Clave: título sin diferencias de mayúsculas/espacios y fecha normalizada. Primera fila equivalente conservada; conflicto analítico detiene la ejecución."
    },
    {
      "paso": "6. Escalas y brecha",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Escalas comprobadas: máximo de usuarios 5 estrellas; prensa 0–100. Rating × 100 / 5; brecha = rating_normalizado − Metacritic Rating. 890 brechas calculables; 227 ausentes. No es min–max de la muestra."
    },
    {
      "paso": "7. Preparación de exportación",
      "antes": 1117,
      "despues": 1117,
      "eliminadas": 0,
      "razon": "",
      "detalle": "Tabla principal: 1117 juegos. Tabla larga: 2682 pertenencias, relación uno a muchos, no nuevos juegos. 3 casos históricos señalados como no elegibles; 35 registros comparten título. Unir solo por id_juego, validando many_to_one."
    }
  ]
}
```

## Que debo verificar manualmente

- Representación de cinco estrellas en la extracción histórica, media absoluta/ponderada y origen de cada nota de prensa.
- Fechas numéricas ambiguas: se usa día/mes/año; consultar las marcadas no interpretables.
- Orden de la lista de géneros y posibles plataformas o versiones distintas con igual título/fecha.
- Las ausencias de crítica utilizable incluyen estimaciones excluidas; no significan que el juego no tenga nota fuera del CSV.

## Antecedente de la deduplicación

Estado: verificado. Esta corrida no elimina las 395 filas históricas: ya no están en el maestro de entrada. Ver trazabilidad_historica.md, deduplicacion_historica.csv y conflictos_historicos.csv para decisiones por ID. No confundir 0 descartes actuales con ausencia de decisiones anteriores.

## Que debo verificar manualmente

- Resolver los conflictos heredados y usar id_juego para relacionar tablas.

## Dimensiones y linaje del insumo

| Etapa | Filas | Columnas | Evidencia |
|---|---:|---:|---|
| Anteproyecto | 1512 | 15 | Proyecto/main.tex. Dimensiones declaradas, sin el CSV exacto para cotejo. |
| Antecedente enriquecido | 1512 | 20 | CSV local. Incluye procedencia de crítica y cuatro estimaciones financieras o comerciales. |
| Reconstrucción del maestro | 1117 | 42 | 395 descartes heredados por título y fecha. Columnas derivadas de calendario, listas, notas, logaritmos y banderas. |
| Maestro curado | 1117 | 42 | CSV designado como original para el pipeline actual. |
| Depurado actual | 1117 | 38 | Salida de la fase de limpieza. |

El maestro curado es un archivo distinto del insumo de 15 columnas descrito en el anteproyecto. El origen exacto de las adiciones entre esa versión y el antecedente de 20 columnas no está documentado. La conciliación verificable comienza en el antecedente local. Los campos económicos estimados se excluyen de las conclusiones y del modelo.
