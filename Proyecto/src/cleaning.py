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
