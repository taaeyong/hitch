"""Wiki-style structured memory for Hitch relationship spaces."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .relationship_space import RelationshipSpace, space_dir
from .storage import read_json, utc_now_iso, write_json


WIKI_COLLECTIONS = (
    "people",
    "relationships",
    "episodes",
    "signals",
    "patterns",
    "summaries",
    "reports",
    "open_questions",
)


@dataclass(frozen=True)
class Signal:
    signal_id: str
    relationship_space_id: str
    source: str
    category: str
    content: str
    confidence: str
    created_at: str
    references: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class WikiEvent:
    event_id: str
    relationship_space_id: str
    event_type: str
    payload: dict[str, Any]
    created_at: str


def wiki_dir(data_dir: Path, space_id: str) -> Path:
    return space_dir(data_dir, space_id) / "wiki"


def collection_path(data_dir: Path, space_id: str, collection: str) -> Path:
    if collection not in WIKI_COLLECTIONS:
        raise ValueError(f"Unknown wiki collection: {collection}")
    return wiki_dir(data_dir, space_id) / f"{collection}.json"


def initialize_wiki(data_dir: Path, space: RelationshipSpace) -> None:
    now = utc_now_iso()
    defaults: dict[str, Any] = {
        "people": {
            "items": [
                {
                    "person_id": "local-user",
                    "label": "나",
                    "role": "self",
                    "created_at": now,
                },
                {
                    "person_id": "partner",
                    "label": space.partner_label,
                    "role": "partner",
                    "created_at": now,
                },
            ]
        },
        "relationships": {
            "items": [
                {
                    "relationship_space_id": space.space_id,
                    "relationship_type": space.relationship_type,
                    "current_state": space.current_state,
                    "created_at": now,
                }
            ]
        },
        "episodes": {"items": []},
        "signals": {"items": []},
        "patterns": {"items": []},
        "summaries": {
            "items": [
                {
                    "summary_id": "current",
                    "relationship_space_id": space.space_id,
                    "summary": space.current_state,
                    "confidence": "early",
                    "updated_at": now,
                }
            ]
        },
        "reports": {"items": []},
        "open_questions": {"items": []},
    }
    for collection, payload in defaults.items():
        path = collection_path(data_dir, space.space_id, collection)
        if not path.exists():
            write_json(path, payload)


def _stable_id(*parts: str) -> str:
    return hashlib.sha256(":".join(parts).encode("utf-8")).hexdigest()[:16]


def add_signal(
    data_dir: Path,
    space: RelationshipSpace,
    *,
    source: str,
    category: str,
    content: str,
    confidence: str = "low",
    references: list[str] | None = None,
) -> Signal:
    initialize_wiki(data_dir, space)
    now = utc_now_iso()
    signal = Signal(
        signal_id=_stable_id(space.space_id, source, category, content, now),
        relationship_space_id=space.space_id,
        source=source,
        category=category,
        content=content,
        confidence=confidence,
        created_at=now,
        references=references or [],
    )
    path = collection_path(data_dir, space.space_id, "signals")
    payload = read_json(path, default={"items": []})
    payload["items"].append(signal.__dict__)
    write_json(path, payload)
    return signal


def add_weekly_report(data_dir: Path, space: RelationshipSpace, report: dict[str, Any]) -> dict[str, Any]:
    initialize_wiki(data_dir, space)
    now = utc_now_iso()
    stored = {
        "report_id": report.get("report_id") or _stable_id(space.space_id, "weekly", now),
        "relationship_space_id": space.space_id,
        "created_at": now,
        **report,
    }
    path = collection_path(data_dir, space.space_id, "reports")
    payload = read_json(path, default={"items": []})
    payload["items"].append(stored)
    write_json(path, payload)
    return stored


def load_wiki_snapshot(data_dir: Path, space: RelationshipSpace) -> dict[str, Any]:
    initialize_wiki(data_dir, space)
    return {
        collection: read_json(collection_path(data_dir, space.space_id, collection), default={"items": []})
        for collection in WIKI_COLLECTIONS
    }


def wiki_counts(snapshot: dict[str, Any]) -> dict[str, int]:
    return {
        collection: len(payload.get("items", []))
        for collection, payload in snapshot.items()
    }
