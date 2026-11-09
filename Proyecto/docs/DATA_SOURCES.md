# Documentación de Fuentes de Datos, Licencias y Reglas de Curación

## 1. Registro de fuentes externas y condiciones de uso

> **Nota importante:** Cada fuente debe verificarse en su documentación oficial al momento de ejecutar las consultas. Registrar la fecha exacta de consulta en `data/external/manifest.jsonl`.

| Fuente | URL oficial | Campos objetivo para `games_enriched.csv` | Límites de tasa y condiciones de uso | Ruta de almacenamiento crudo |
|---|---|---|---|---|
| **IGDB API v4** | https://api-docs.igdb.com/ | `igdb_id`, `platforms_list`, `n_platforms`, `game_modes`, `genre_igdb_main`, `first_release_date`, `involved_companies`, `external_games` (Steam AppID) | Autenticación Twitch OAuth2 (`client_credentials`). Límite de 4 req/s (configurar cliente a ≤ 3.5 req/s). Uso gratuito no comercial; no redistribuir volcados crudos completos. | `data/external/igdb/<igdb_id>.json` |
| **RAWG API** | https://rawg.io/apidocs | `rawg_id`, `critic_score_rawg` (`metacritic`), `platforms`, `stores`, `released` | Plan gratuito hasta 20,000 req/mes. Exige atribución visible y enlace activo a RAWG en la aplicación Streamlit y en los reportes. | `data/external/rawg/<id>.json` |
| **OpenCritic API** (vía RapidAPI) | https://opencritic.com/api | `opencritic_id`, `critic_score_opencritic` (`topCriticScore`), `medianScore`, `percentRecommended` | Cuota gratuita limitada según nivel RapidAPI. Priorizar para las 218 filas con crítica estimada no cubiertas por RAWG y para la población complementaria. | `data/external/opencritic/<id>.json` |
| **Steam Storefront API** (`appdetails`) | `https://store.steampowered.com/api/appdetails?appids=<ID>&cc=us` | `steam_appid`, `is_free`, `price_usd_initial` (`price_overview.initial / 100`), categorías multijugador | Endpoint semi-público; usar pausa mínima de 1.6 s entre llamadas y `User-Agent` identificable. | `data/external/steam/<appid>.json` |
| **SteamSpy API** | `https://steamspy.com/api.php?request=appdetails&appid=<ID>` | `owners_low`, `owners_high` (de `owners`), `median_playtime_min` (`median_forever`) | Límite de 1 req/s en `appdetails`. Propietarios expresados en rangos de estimación estadística, nunca como ventas exactas. | `data/external/steamspy/<appid>.json` |
| **Wikipedia: Best-selling video games** | https://en.wikipedia.org/wiki/List_of_best-selling_video_games | `sales_units_public`, `sales_source_url` | Licencia CC BY-SA 4.0. Solo registrar si cuenta con nota al pie verificable en el artículo. | `data/external/wikipedia/best_selling.html` |
| **Wikipedia: Commercial failures y prensa** | https://en.wikipedia.org/wiki/List_of_commercial_failures_in_video_games | `outcome_label`, `outcome_source_url`, `is_live_service` | Licencia CC BY-SA 4.0. Cada etiqueta (`failure` / `underperformer`) requiere URL verificada de artículo de prensa o comunicado oficial. | `data/curated/complement_seeds.csv` |

---

## 2. Manejo de columnas financieras en el CSV único (`games_curated.csv`)

La auditoría sobre `docs/games_actualizado_metacritic.csv` demostró que las columnas `ingresos_empresa_estimados_USD`, `gastos_estimados_USD`, `unidades_vendidas_estimadas` y `ventas_brutas_estimadas_USD` siguen relaciones deterministas sintéticas (`ingresos = 0.70 * ventas_brutas` en el 98.2% de los registros y precios unitarios escalonados en \$12, \$18, \$20 y \$30).

Para mantener **un único CSV maestro** (`data/processed/games_curated.csv`):
1. Dichas columnas se conservan dentro de `data/processed/games_curated.csv` junto con la bandera `estimates_zero` y con las columnas de texto `Reviews` (comentarios) y `Summary`.
2. Solo deben usarse como referencia exploratoria y no como variable objetivo o predictora en modelos supervisados, clustering o pruebas de hipótesis sin antes sustituirlas por datos verificados (`sales_units_public` / `owners_low` y `owners_high`).

---

## 3. Exclusión de calificaciones de crítica sintéticas (`Origen_calificacion == "Estimacion propia"`)

En las 261 filas con `Rating` válido y `Origen_calificacion == "Estimacion propia"`, la columna `Metacritic Rating` fue generada mediante la fórmula lineal:
$$\text{Metacritic Rating} = \text{round}(8.5851 \times \text{Rating} + 50.9504)$$
con correlación interna $r = 0.9985$.

En `data/processed/games_curated.csv`:
- `critic_score_final` conserva únicamente los 899 registros con `Origen_calificacion == "Metacritic"` (`critic_source = "metacritic_csv"`).
- Los 218 registros únicos con `"Estimacion propia"` tienen `critic_score_final = NaN` y `critic_source = "none"` hasta que sean consultados en RAWG u OpenCritic.

---

## 4. Criterio operativo para `is_live_service` y `business_model`

Un título recibe `is_live_service = True` si cumple al menos **dos** de las siguientes condiciones documentadas con fuente:
1. **Monetización recurrente post-lanzamiento:** pases de batalla, gacha/cajas de botín, suscripción recurrente o tienda rotativa con moneda premium.
2. **Contenido vivo por temporadas:** actualizaciones estructurales periódicas (Seasons/Capítulos) orientadas a retención continua.
3. **Dependencia de servidores en línea:** requiere conexión permanente o servidores centrales cuyo apagado vuelve inaccesible el juego principal.

Regla para `business_model`:
- `is_live_service == True` $\rightarrow$ `live_service` (conservando `is_free` para distinguir GaaS gratuitos de GaaS de pago).
- `is_live_service == False` e `is_free == True` $\rightarrow$ `free_to_play`.
- `is_live_service == False` e `is_free == False` $\rightarrow$ `premium`.
- Sin datos verificables $\rightarrow$ `unknown`.
