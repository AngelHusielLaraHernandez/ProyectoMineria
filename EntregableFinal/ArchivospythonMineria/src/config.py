"""Esquema comprobado en el archivo original; no inferido de Kaggle."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
RAW = ROOT / 'data' / 'raw' / 'games_curated.csv'
CLEAN = ROOT / 'data' / 'clean'
REPORTS = ROOT / 'reports'
MODELS = ROOT / 'models'
SIGNALS = ['Plays', 'Playing', 'Backlogs', 'Wishlist']
REQUIRED = ['ID Original', 'Title', 'Release Date', 'Team', 'Rating',
            'Times Listed', 'Number of Reviews', 'Genres', 'Summary', 'Reviews',
            *SIGNALS, 'Metacritic Rating', 'Origen_calificacion',
            'critic_score_final', 'critic_source']
FEATURES = ['generos', 'estudio', 'decada', 'Metacritic Rating', 'Rating']
LEVELS = ['bajo', 'medio', 'alto']
