import numpy as np
from gdelt import GDelt
from itertools import permutations

from .data_handler import load_hofstede_scores, load_wals_features


def calculate_cds(country1_code: str, country2_code: str) -> float:
    """Calculate Cultural Distance Score (CDS)."""
    df = load_hofstede_scores()
    c1 = df[df['code'] == country1_code.upper()].iloc[0]
    c2 = df[df['code'] == country2_code.upper()].iloc[0]
    dimensions = [
        'power_distance',
        'individualism',
        'masculinity',
        'uncertainty_avoidance',
        'long_term_orientation',
        'indulgence',
    ]
    diffs = [(c1[d] - c2[d]) ** 2 for d in dimensions]
    # simple variance placeholder
    variances = [1 for _ in dimensions]
    cds = np.sqrt(sum(d / v for d, v in zip(diffs, variances)))
    return float(cds)


def calculate_gis(country1_code: str, country2_code: str) -> float:
    """Calculate Geopolitical Interaction Score using GDELT events."""
    gd = GDelt()
    query = {
        'query': f"{country1_code} {country2_code}",
        'mode': 'ArtList',
        'format': 'json',
    }
    events = gd.Search(query)
    conflict = len([e for e in events if 'CONFLICT' in e.get('themes', '')])
    coop = len([e for e in events if 'COOPERATION' in e.get('themes', '')])
    epsilon = 1e-9
    return conflict / (conflict + coop + epsilon)


def calculate_lds(lang1_code: str, lang2_code: str) -> float:
    """Calculate Linguistic Distance Score using simple Hamming distance."""
    df = load_wals_features()
    l1 = df[df['code'] == lang1_code].iloc[0]
    l2 = df[df['code'] == lang2_code].iloc[0]
    features = ['feature1', 'feature2', 'feature3']
    diff_count = sum(l1[f] != l2[f] for f in features)
    defined_count = len(features)
    return diff_count / defined_count


def select_diverse_languages(source_language: str, num_pivots: int = 3):
    """Select a path of languages maximizing diversity via greedy approach."""
    df = load_wals_features()
    candidate_langs = list(df['code'].unique())
    candidate_langs = [c for c in candidate_langs if c != source_language]

    best_path = []
    current = source_language
    for _ in range(num_pivots):
        scores = []
        for lang in candidate_langs:
            cds = calculate_cds(current.upper(), lang.upper())
            lds = calculate_lds(current, lang)
            score = cds + lds
            scores.append((score, lang))
        if not scores:
            break
        scores.sort(reverse=True)
        best_lang = scores[0][1]
        best_path.append((current, best_lang))
        candidate_langs.remove(best_lang)
        current = best_lang
    return best_path
