"""Casos de prueba de limpieza (CP-1.0)."""
import pandas as pd
import pytest
from src.cleaning import parse_suffix, parse_list, clean
from src import config as C


@pytest.mark.parametrize(
    "v,e", [("3.9K", 3900), ("17K", 17000), ("1.2M", 1.2e6), ("850", 850), ("0", 0)]
)
def test_suffix(v, e):
    assert parse_suffix(v) == pytest.approx(e)


def test_suffix_nan():
    assert pd.isna(parse_suffix(float("nan")))


def test_parse_list():
    assert parse_list("['RPG', 'Indie']") == ["RPG", "Indie"]
    assert parse_list(None) == []


@pytest.fixture(scope="module")
def df():
    return clean(pd.read_csv(C.RAW_CSV, encoding="utf-8-sig"))


def test_no_duplicates(df):
    assert not df.duplicated(["Title", "Release Date"]).any()


def test_numeric_types(df):
    for c in C.SUFFIX_COLS:
        assert pd.api.types.is_numeric_dtype(df[c]) and df[c].notna().all()


def test_dates(df):
    assert df["year"].min() >= 1980 and df["year"].max() <= 2025
    assert df["release_date"].isna().sum() <= 3


def test_gap_and_flags(df):
    r = df.dropna(subset=["Rating"]).iloc[0]
    assert r["gap"] == pytest.approx(r["Rating"] * 20 - r["Metacritic Rating"])
    assert df["metacritic_real"].sum() > 0


def test_keeps_reviews_summary_and_estimates(df):
    assert "Reviews" in df.columns
    assert "Summary" in df.columns
    assert set(C.ESTIMATED_COLS) <= set(df.columns)
