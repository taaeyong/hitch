"""Minimal private-safe raw source registration.

This layer records metadata about local txt/csv drops without copying raw content
into pushable artifacts. Parser and segmenter depth is intentionally deferred.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .relationship_space import RelationshipSpace, space_dir
from .storage import read_json, utc_now_iso, write_json


SUPPORTED_SOURCE_TYPES = {"txt", "csv"}


class IngestError(ValueError):
    pass


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    relationship_space_id: str
    source_type: str
    original_path: str
    display_name: str
    byte_size: int
    sha256: str
    registered_at: str
    parser_status: str = "registered_parse_pending"
    notes: dict[str, Any] = field(default_factory=dict)


def infer_source_type(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    if suffix not in SUPPORTED_SOURCE_TYPES:
        raise IngestError("Only txt and csv raw source registration is supported in v4 demo")
    return suffix


def source_registry_path(data_dir: Path, space_id: str) -> Path:
    return space_dir(data_dir, space_id) / "ingest" / "sources.json"


def _file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _source_id(space_id: str, path: Path, digest: str) -> str:
    seed = f"{space_id}:{path.name}:{digest[:16]}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]


def register_source(
    data_dir: Path,
    space: RelationshipSpace,
    raw_path: Path,
    *,
    display_name: str | None = None,
    notes: dict[str, Any] | None = None,
) -> SourceRecord:
    if not raw_path.exists() or not raw_path.is_file():
        raise IngestError(f"Raw source file does not exist: {raw_path}")

    source_type = infer_source_type(raw_path)
    digest = _file_hash(raw_path)
    stat = raw_path.stat()
    record = SourceRecord(
        source_id=_source_id(space.space_id, raw_path, digest),
        relationship_space_id=space.space_id,
        source_type=source_type,
        original_path=str(raw_path),
        display_name=display_name or raw_path.name,
        byte_size=stat.st_size,
        sha256=digest,
        registered_at=utc_now_iso(),
        notes=notes or {},
    )

    registry_path = source_registry_path(data_dir, space.space_id)
    registry = read_json(registry_path, default={"sources": []})
    existing = [item for item in registry["sources"] if item["source_id"] != record.source_id]
    existing.append(record.__dict__)
    write_json(registry_path, {"sources": existing})
    return record


def list_sources(data_dir: Path, space_id: str) -> list[SourceRecord]:
    registry = read_json(source_registry_path(data_dir, space_id), default={"sources": []})
    return [SourceRecord(**item) for item in registry["sources"]]
