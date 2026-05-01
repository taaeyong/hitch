from __future__ import annotations

from collections import Counter
from typing import Any

from .paths import SIMULATION_DIR
from .storage import append_jsonl, now_iso, read_json, read_jsonl, write_json
from .wiki import SUMMARY_PATH, record_interaction_delta


SIMULATION_RUNS_PATH = SIMULATION_DIR / "runs.jsonl"
SIMULATION_EFFECTS_PATH = SIMULATION_DIR / "effects.jsonl"
SIMULATION_SNAPSHOT_PATH = SIMULATION_DIR / "latest_snapshot.json"


def _dominant_signal(summary: dict[str, Any]) -> tuple[str | None, str]:
    counts = Counter(summary.get("love_language_signal_counts", {}))
    if not counts:
        return None, "shared time and attentive follow-through"
    labels = {
        "words": "words of affirmation",
        "time": "quality time",
        "acts": "acts of service",
        "gifts": "gifts or concrete tokens",
        "touch": "physical closeness",
    }
    key = counts.most_common(1)[0][0]
    return key, labels.get(key, key)


def run_simulation(prompt: str, source: str = "cli", persist: bool = True) -> dict[str, Any]:
    summary = read_json(SUMMARY_PATH, {})
    dominant_key, dominant_label = _dominant_signal(summary)
    signal_count = summary.get("signal_count", 0)
    message_count = summary.get("message_count", 0)
    if signal_count:
        partner_estimate = (
            f"Given the grounded local history, the partner side may notice {dominant_label} most. "
            "Treat this as a soft perspective estimate, not a real partner answer."
        )
        uncertainty = "grounded but still approximate"
    else:
        partner_estimate = (
            "The prepared state is thin, so the safest estimate is general: the partner may need "
            "specific context and a clear sign that the user's intent connects to their felt need."
        )
        uncertainty = "low signal"

    result = {
        "id": f"simulation-{now_iso()}",
        "relationship_space_id": "main",
        "source": source,
        "prompt": prompt,
        "basis": {
            "message_count": message_count,
            "signal_count": signal_count,
            "dominant_signal": dominant_key,
            "dominant_signal_label": dominant_label,
        },
        "partner_perspective_estimate": partner_estimate,
        "gap_or_alignment_note": (
            "The useful next check is whether the user's intended expression of care matches "
            f"the partner-side signal around {dominant_label}."
        ),
        "uncertainty": uncertainty,
        "signal_delta": {
            "simulated_loop_turns": 1,
            "dominant_signal_used": dominant_key,
            "dominant_signal_label": dominant_label,
        },
        "interpretation_delta": f"Latest loop connected the user prompt to partner-side {dominant_label} signals.",
        "follow_up_question": "What specific moment from this week should Hitch compare against that pattern?",
        "created_at": now_iso(),
    }
    if persist:
        append_jsonl(SIMULATION_RUNS_PATH, result)
        delta = record_interaction_delta(prompt, result)
        refreshed_summary = read_json(SUMMARY_PATH, {})
        effect = {
            "id": f"effect-{now_iso()}",
            "relationship_space_id": result["relationship_space_id"],
            "simulation_run_id": result["id"],
            "interaction_delta_id": delta["id"],
            "source": source,
            "changed": {
                "simulation_delta_count": refreshed_summary.get("simulation_delta_count", 0),
                "latest_interpretation_delta": refreshed_summary.get("latest_interpretation_delta", ""),
                "open_question": delta.get("follow_up_question", ""),
            },
            "graph_implication": {
                "adds_interaction_delta_node": True,
                "links_to_pattern": dominant_key,
            },
            "created_at": now_iso(),
        }
        append_jsonl(SIMULATION_EFFECTS_PATH, effect)
        snapshot = {
            "relationship_space_id": result["relationship_space_id"],
            "latest_simulation_run_id": result["id"],
            "latest_effect_id": effect["id"],
            "source": source,
            "summary": {
                "message_count": refreshed_summary.get("message_count", 0),
                "signal_count": refreshed_summary.get("signal_count", 0),
                "simulation_delta_count": refreshed_summary.get("simulation_delta_count", 0),
                "dominant_signal": dominant_key,
                "dominant_signal_label": dominant_label,
                "latest_interpretation_delta": refreshed_summary.get("latest_interpretation_delta", ""),
                "open_questions": refreshed_summary.get("open_questions", [])[-5:],
            },
            "run_count": len(read_jsonl(SIMULATION_RUNS_PATH)),
            "effect_count": len(read_jsonl(SIMULATION_EFFECTS_PATH)),
            "updated_at": now_iso(),
        }
        write_json(SIMULATION_SNAPSHOT_PATH, snapshot)
    return result
