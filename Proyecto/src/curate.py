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
