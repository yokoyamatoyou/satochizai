import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

HOFSTEDE_FILE = os.path.join(DATA_DIR, 'hofstede_scores.csv')
WALS_FILE = os.path.join(DATA_DIR, 'wals_features.csv')


def load_hofstede_scores():
    """Load Hofstede cultural dimension scores from CSV."""
    if not os.path.exists(HOFSTEDE_FILE):
        raise FileNotFoundError(f"Hofstede data not found: {HOFSTEDE_FILE}")
    df = pd.read_csv(HOFSTEDE_FILE)
    df = df.fillna(method='ffill')
    return df


def load_wals_features():
    """Load WALS language features from CSV."""
    if not os.path.exists(WALS_FILE):
        raise FileNotFoundError(f"WALS data not found: {WALS_FILE}")
    df = pd.read_csv(WALS_FILE)
    df = df.fillna(0)
    return df
