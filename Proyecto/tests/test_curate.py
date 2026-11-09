"""Pruebas del CSV único curado (src/curate.py)."""
import pandas as pd
import pytest
from src import config as C
from src.curate import CURATED, REVIEW


@pytest.fixture(scope="module")
def cur():
    return pd.read_csv(CURATED)


def test_single_csv_has_all_columns(cur):
    assert "Reviews" in cur.columns
    assert "Summary" in cur.columns
    assert set(C.ESTIMATED_COLS) <= set(cur.columns)


def test_critic_only_from_real_metacritic(cur):
    assert cur.loc[cur.critic_source == "none", "critic_score_final"].isna().all()
    assert cur.loc[cur.critic_source == "metacritic_csv", "critic_score_final"].notna().all()


def test_review_queue_covers_estimated(cur):
    rv = pd.read_csv(REVIEW)
    est = set(cur.loc[~cur.metacritic_real, "ID Original"])
    assert est <= set(rv["ID Original"])


def test_seeds_are_unverified():
    s = pd.read_csv(C.ROOT / "data" / "curated" / "complement_seeds.csv")
    assert (s["verified"].astype(str) == "False").all()
