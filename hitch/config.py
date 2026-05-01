"""Runtime configuration for the local Hitch v4 demo."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = PROJECT_ROOT / "data"


@dataclass(frozen=True)
class HitchConfig:
    data_dir: Path
    telegram_token: str | None
    active_space_id: str


def _read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def load_config() -> HitchConfig:
    env_file_values = _read_env_file(PROJECT_ROOT / ".env")
    data_dir = Path(
        os.environ.get("HITCH_DATA_DIR")
        or env_file_values.get("HITCH_DATA_DIR")
        or DEFAULT_DATA_DIR
    ).expanduser()
    token = os.environ.get("HITCH_TELEGRAM_TOKEN") or env_file_values.get(
        "HITCH_TELEGRAM_TOKEN"
    )
    active_space_id = (
        os.environ.get("HITCH_ACTIVE_SPACE_ID")
        or env_file_values.get("HITCH_ACTIVE_SPACE_ID")
        or "demo-relationship"
    )
    return HitchConfig(
        data_dir=data_dir,
        telegram_token=token,
        active_space_id=active_space_id,
    )
