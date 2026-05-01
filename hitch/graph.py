from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .paths import GRAPH_DIR
from .storage import now_iso, read_json, write_json
from .wiki import SIGNALS_PATH, SPACE_STATE_PATH, SUMMARY_PATH


GRAPH_PATH = GRAPH_DIR / "relationship_graph.json"


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def export_graph() -> dict[str, Any]:
    space = read_json(SPACE_STATE_PATH, {})
    summary = read_json(SUMMARY_PATH, {})
    signals = _read_jsonl(SIGNALS_PATH)
    nodes: list[dict[str, Any]] = [
        {"id": "relationship:main", "type": "relationship", "label": space.get("relationship_type", "romantic")},
        {"id": "person:user", "type": "person", "label": "user"},
        {"id": "person:partner", "type": "person", "label": space.get("partner_label", "partner")},
    ]
    edges: list[dict[str, Any]] = [
        {"source": "person:user", "target": "relationship:main", "type": "participates_in"},
        {"source": "person:partner", "target": "relationship:main", "type": "participates_in"},
    ]
    for category, count in summary.get("love_language_signal_counts", {}).items():
        node_id = f"pattern:{category}"
        nodes.append({"id": node_id, "type": "pattern", "label": category, "count": count})
        edges.append({"source": node_id, "target": "relationship:main", "type": "observed_in", "weight": count})
    for signal in signals[:250]:
        node_id = signal["id"]
        nodes.append({"id": node_id, "type": "signal", "label": ",".join(signal.get("categories", []))})
        edges.append({"source": node_id, "target": "relationship:main", "type": "evidence_for"})
    payload = {"generated_at": now_iso(), "nodes": nodes, "edges": edges}
    write_json(GRAPH_PATH, payload)
    return payload
