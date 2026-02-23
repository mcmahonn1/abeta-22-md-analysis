from pathlib import Path

# Repo root = parent of /src
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_PROCESSED = DATA_DIR / "processed"

RESULTS_DIR = BASE_DIR / "results"
RESULTS_FIGURES = RESULTS_DIR / "figures"
RESULTS_TABLES = RESULTS_DIR / "tables"

def ensure_dirs():
    RESULTS_FIGURES.mkdir(parents=True, exist_ok=True)
    RESULTS_TABLES.mkdir(parents=True, exist_ok=True)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

