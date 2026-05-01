from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "raw"
DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_RAW_CSV = RAW_DIR / "girlfriend_kakaotalk.csv"
ENV_FILE = PROJECT_ROOT / ".env"

SPACE_DIR = DATA_DIR / "relationship_spaces" / "main"
INGEST_DIR = DATA_DIR / "ingest"
WIKI_DIR = DATA_DIR / "wiki"
SIMULATION_DIR = DATA_DIR / "simulation"
GRAPH_DIR = DATA_DIR / "graph"
REPORT_DIR = DATA_DIR / "reports"


def ensure_data_dirs() -> None:
    for path in (SPACE_DIR, INGEST_DIR, WIKI_DIR, SIMULATION_DIR, GRAPH_DIR, REPORT_DIR):
        path.mkdir(parents=True, exist_ok=True)
