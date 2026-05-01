from __future__ import annotations

from typing import Any

from .paths import GRAPH_DIR
from .simulation import SIMULATION_RUNS_PATH
from .storage import now_iso, read_json, read_jsonl, write_json
from .wiki import INTERACTIONS_PATH, SIGNALS_PATH, SPACE_STATE_PATH, SUMMARY_PATH


GRAPH_PATH = GRAPH_DIR / "relationship_graph.json"


def export_graph() -> dict[str, Any]:
    space = read_json(SPACE_STATE_PATH, {})
    summary = read_json(SUMMARY_PATH, {})
    signals = read_jsonl(SIGNALS_PATH)
    interaction_deltas = read_jsonl(INTERACTIONS_PATH)
    simulation_runs = read_jsonl(SIMULATION_RUNS_PATH)
    nodes: list[dict[str, Any]] = [
        {"id": "relationship:main", "type": "relationship", "label": space.get("relationship_type", "romantic")},
        {"id": "person:user", "type": "person", "label": "user"},
        {"id": "person:partner", "type": "person", "label": space.get("partner_label", "partner")},
        {
            "id": "artifact:wiki-summary",
            "type": "artifact",
            "label": "wiki summary",
            "message_count": summary.get("message_count", 0),
            "signal_count": summary.get("signal_count", 0),
            "simulation_delta_count": summary.get("simulation_delta_count", 0),
        },
    ]
    edges: list[dict[str, Any]] = [
        {"source": "person:user", "target": "relationship:main", "type": "participates_in"},
        {"source": "person:partner", "target": "relationship:main", "type": "participates_in"},
        {"source": "artifact:wiki-summary", "target": "relationship:main", "type": "summarizes"},
    ]
    for category, count in summary.get("love_language_signal_counts", {}).items():
        node_id = f"pattern:{category}"
        nodes.append({"id": node_id, "type": "pattern", "label": category, "count": count})
        edges.append({"source": node_id, "target": "relationship:main", "type": "observed_in", "weight": count})
    for signal in signals[:250]:
        node_id = signal["id"]
        nodes.append({"id": node_id, "type": "signal", "label": ",".join(signal.get("categories", []))})
        edges.append({"source": node_id, "target": "relationship:main", "type": "evidence_for"})
    for index, delta in enumerate(interaction_deltas[-50:], start=1):
        node_id = f"interaction-delta:{delta.get('id', index)}"
        nodes.append(
            {
                "id": node_id,
                "type": "interaction_delta",
                "label": "simulation feedback delta",
                "created_at": delta.get("created_at"),
                "interpretation_delta": delta.get("interpretation_delta", ""),
                "follow_up_question": delta.get("follow_up_question", ""),
            }
        )
        edges.append({"source": node_id, "target": "artifact:wiki-summary", "type": "updates"})
        dominant = delta.get("signal_delta", {}).get("dominant_signal_used")
        if dominant:
            edges.append({"source": node_id, "target": f"pattern:{dominant}", "type": "uses_pattern"})
    for index, run in enumerate(simulation_runs[-50:], start=1):
        node_id = f"simulation-run:{run.get('id', index)}"
        nodes.append(
            {
                "id": node_id,
                "type": "simulation_run",
                "label": run.get("source", "simulation"),
                "created_at": run.get("created_at"),
                "uncertainty": run.get("uncertainty"),
            }
        )
        edges.append({"source": node_id, "target": "relationship:main", "type": "estimates_perspective_for"})
        edges.append({"source": node_id, "target": "artifact:wiki-summary", "type": "feeds"})
    payload = {"generated_at": now_iso(), "nodes": nodes, "edges": edges}
    write_json(GRAPH_PATH, payload)
    return payload
