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
