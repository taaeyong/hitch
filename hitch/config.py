from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping

from .paths import ENV_FILE


TOKEN_NAME = "HITCH_TELEGRAM_TOKEN"


def load_dotenv(path: Path = ENV_FILE) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def merged_env() -> Mapping[str, str]:
    values = dict(load_dotenv())
    values.update(os.environ)
    return values


def telegram_token(required: bool = False) -> str | None:
    token = merged_env().get(TOKEN_NAME)
    if required and not token:
        raise RuntimeError(f"{TOKEN_NAME} is required in .env or the process environment")
    return token
