# Carpeta: Proyecto/src

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## __init__.py

Ruta: `Proyecto/src/__init__.py` · Bytes: 0 · SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

````text

````

## cleaning.py

Ruta: `Proyecto/src/cleaning.py` · Bytes: 3560 · SHA-256: `ed82d7c08ef30362d9496359472aeb6e212fe458c6ebba2d2ff566573ecb30c7`

````text
"""Limpieza, curación y variables derivadas en un único CSV (CLEAN-SCRIPT-1.0).

Uso:  python -m src.cleaning
"""
import ast
import numpy as np
import pandas as pd
from . import config as C


def parse_suffix(value) -> float:
    """Convierte '3.9K' -> 3900.0, '1.2M' -> 1200000.0, '850' -> 850.0."""
    if pd.isna(value):
        return float("nan")
    s = str(value).strip().replace(",", "").upper()
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}
    if s and s[-1] in mult:
        return float(s[:-1]) * mult[s[-1]]
    return float(s)


def parse_list(value) -> list:
    if pd.isna(value):
        return []
    try:
        out = ast.literal_eval(value)
        return list(out) if isinstance(out, (list, tuple)) else []
    except (ValueError, SyntaxError):
        return []


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Fechas ("releases on TBD" -> NaT)
    df["release_date"] = pd.to_datetime(
        df["Release Date"], format="%b %d, %Y", errors="coerce"
    )
    df["year"] = df["release_date"].dt.year.astype("Int64")
    df["decade"] = (df["year"] // 10 * 10).astype("Int64")

    # 2. Duplicados: mismas filas salvo ID (Title + Release Date)
    df = df.sort_values("ID Original")
    df = df.drop_duplicates(subset=["Title", "Release Date"], keep="first")

    # 3. Sufijos K/M en todas las columnas de interacción (conservando todas las originales)
    for c in C.SUFFIX_COLS:
        if c in df.columns:
            df[c] = df[c].map(parse_suffix)

    # 4. Listas (conservando también Summary y Reviews íntegros)
    df["genres_list"] = df["Genres"].map(parse_list)
    df["team_list"] = df["Team"].map(parse_list)
    df["n_genres"] = df["genres_list"].str.len()
    df["studio_main"] = df["team_list"].map(lambda t: t[-1] if t else None)
    df["publisher_main"] = df["team_list"].map(lambda t: t[0] if t else None)

    # 5. Género principal (el menos frecuente del juego, para evitar que 'Adventure' domine)
    freq = df["genres_list"].explode().value_counts()

    def main_genre(gs):
        if not gs:
            return "Unknown"
        g = min(gs, key=lambda x: freq.get(x, 0) if x != "Indie" else 10**9)
        return g if freq.get(g, 0) >= C.MIN_GENRE_COUNT else "Other"

    df["genre_main"] = df["genres_list"].map(main_genre)

    # 6. Rating vs Metacritic (escala 0-100) y procedencia verificada
    df["rating_100"] = df["Rating"] * 20
    df["gap"] = df["rating_100"] - df["Metacritic Rating"]
    df["metacritic_real"] = df["Origen_calificacion"].eq("Metacritic")
    df["critic_score_final"] = df["Metacritic Rating"].where(df["metacritic_real"])
    df["critic_source"] = df["metacritic_real"].map(
        {True: "metacritic_csv", False: "none"}
    )
    df["gap_real"] = df["rating_100"] - df["critic_score_final"]

    # 7. Popularidad (log por asimetría fuerte)
    for c in ["Plays", "Wishlist", "Backlogs", "Playing"]:
        df[f"log_{c.lower()}"] = np.log1p(df[c])

    # 8. Banderas de columnas estimadas y población
    df["estimates_zero"] = (df[C.ESTIMATED_COLS] == 0).any(axis=1)
    df["has_rating"] = df["Rating"].notna()
    df["population"] = "original"

    return df.reset_index(drop=True)


def main() -> pd.DataFrame:
    raw = pd.read_csv(C.RAW_CSV, encoding="utf-8-sig")
    out = clean(raw)
    C.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(C.CURATED_CSV, index=False, encoding="utf-8")
    print(f"raw={len(raw)} curated={len(out)} cols={len(out.columns)} -> {C.CURATED_CSV}")
    return out


if __name__ == "__main__":
    main()

````

## config.py

Ruta: `Proyecto/src/config.py` · Bytes: 864 · SHA-256: `89c4688efca334427b3659fd99c4e7675541eb099be07283c310818ee4031807`

````text
"""Configuración central: rutas, columnas y semilla aleatoria."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "docs" / "games_actualizado_metacritic.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
CURATED_CSV = PROCESSED_DIR / "games_curated.csv"
CLEAN_CSV = CURATED_CSV  # Alias para mantener un único CSV procesado
SEED = 42

# Columnas con sufijo K/M que se convierten a numérico
SUFFIX_COLS = [
    "Times Listed",
    "Number of Reviews",
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist",
]

# Columnas financieras estimadas del CSV original (incluidas en el CSV único)
ESTIMATED_COLS = [
    "ingresos_empresa_estimados_USD",
    "gastos_estimados_USD",
    "unidades_vendidas_estimadas",
    "ventas_brutas_estimadas_USD",
]

# Géneros con muy pocos casos se agrupan en "Other"
MIN_GENRE_COUNT = 30

````

## curate.py

Ruta: `Proyecto/src/curate.py` · Bytes: 4368 · SHA-256: `4eaa78d005510e5e9b5353c794293f928e30a2e076560c3e6138f5ca923dc022`

````text
"""Genera el CSV único curado, el informe de Pearson y la cola de revisión manual.

Uso:  python -m src.curate
"""
import numpy as np
import pandas as pd
from . import config as C
from .cleaning import clean

REPORT = C.ROOT / "reports" / "pearson_before_after.md"
CURATED = C.CURATED_CSV
REVIEW = C.ROOT / "data" / "curated" / "manual_review.csv"


def pearson(df, a="Rating", b="Metacritic Rating"):
    d = df[[a, b]].dropna()
    return len(d), (d[a].corr(d[b]) if len(d) > 2 else float("nan"))


def main():
    raw = pd.read_csv(C.RAW_CSV, encoding="utf-8-sig")
    cur = clean(raw)

    # 1. Guardar un único CSV con todas las columnas (incluyendo Reviews, Summary y estimados)
    C.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    cur.to_csv(CURATED, index=False, encoding="utf-8")

    # 2. Informe Pearson
    raw["rating_100"] = raw["Rating"] * 20
    real_raw = raw[raw["Origen_calificacion"] == "Metacritic"]
    est_raw = raw[raw["Origen_calificacion"] != "Metacritic"]
    est_clean = cur[~cur["metacritic_real"]]
    rows = [
        ("1. Crudo (1,512, con duplicados y estimados)", raw),
        ("2. Limpio (1,117, con estimados)", cur),
        ("3. Solo estimados en crudo", est_raw),
        ("4. Solo estimados en limpio", est_clean),
        ("5. Crudo, solo Metacritic real", real_raw),
        ("6. Limpio, solo Metacritic real (línea base)", cur[cur["metacritic_real"]]),
    ]
    L = [
        "# Pearson usuarios vs. crítica: antes y después de depurar\n",
        "Generado por `src/curate.py` con los datos del repositorio.\n",
        "| Escenario | N pares | Pearson r | Media de la brecha (rating×20 − Metacritic) |",
        "|---|---|---|---|",
    ]
    for name, d in rows:
        d = d.copy()
        d["_gap"] = d["Rating"] * 20 - d["Metacritic Rating"]
        n, r = pearson(d)
        L.append(f"| {name} | {n} | {r:.4f} | {d['_gap'].mean():.2f} |")
    est = est_raw.dropna(subset=["Rating"])
    b, a = np.polyfit(est["Rating"], est["Metacritic Rating"], 1)
    resid = (est["Metacritic Rating"] - (b * est["Rating"] + a).round()).abs().max()
    L += [
        "",
        "## Hallazgo sobre los estimados",
        f"En las {len(est)} filas estimadas con Rating, Metacritic ≈ {b:.4f}·Rating + {a:.4f} "
        f"(residuo máximo tras redondear con estos coeficientes: {resid:.1f}). "
        "No es una calificación de crítica independiente: es una función del Rating y se marca con "
        "`metacritic_real = False` y `critic_score_final = NaN` para excluirla de la comparación usuarios–crítica.\n",
    ]
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(L), encoding="utf-8")

    # 3. Cola de revisión manual
    out = []

    def add(df, reason, note=""):
        for _, r in df.iterrows():
            out.append(
                {
                    "ID Original": r["ID Original"],
                    "Title": r["Title"],
                    "Release Date": r["Release Date"],
                    "reason": reason,
                    "note": note,
                    "resolved": "",
                }
            )

    add(
        cur[cur["Release Date"].str.contains("TBD", na=False)],
        "fecha_TBD",
        "Buscar fecha real de lanzamiento en IGDB/RAWG",
    )
    add(
        cur[(cur["year"] >= 2023) & cur["Rating"].isna()],
        "sin_rating_reciente",
        "Salió tras el scrape de Backloggd; sin Rating de usuarios",
    )
    add(
        cur[cur["year"] >= 2024],
        "fecha_futura_o_cancelado",
        "Verificar si se lanzó o se canceló",
    )
    dup = cur[cur.duplicated(["Title", "year"], keep=False)]
    add(
        dup,
        "colision_titulo_anio",
        "Distintas versiones/plataformas: desambiguar con igdb_id",
    )
    add(
        cur[~cur["metacritic_real"]],
        "critica_estimada",
        "Buscar puntaje real en RAWG/OpenCritic; si no existe, dejar NaN",
    )
    rv = pd.DataFrame(out)
    rv = rv.groupby(["ID Original", "Title", "Release Date"], as_index=False).agg(
        reason=("reason", "; ".join),
        note=("note", " | ".join),
        resolved=("resolved", "first"),
    )
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    rv.to_csv(REVIEW, index=False)

    print(f"curated={len(cur)} cols={len(cur.columns)} review={len(rv)}")


if __name__ == "__main__":
    main()

````

