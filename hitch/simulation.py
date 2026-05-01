from __future__ import annotations

from collections import Counter
from typing import Any

from .paths import SIMULATION_DIR
from .storage import append_jsonl, now_iso, read_json
from .wiki import SUMMARY_PATH, record_interaction_delta


SIMULATION_RUNS_PATH = SIMULATION_DIR / "runs.jsonl"


def _dominant_language(summary: dict[str, Any]) -> str:
    counts = Counter(summary.get("love_language_signal_counts", {}))
    if not counts:
        return "shared time and attentive follow-through"
    labels = {
        "words": "words of affirmation",
        "time": "quality time",
        "acts": "acts of service",
        "gifts": "gifts or concrete tokens",
        "touch": "physical closeness",
    }
    return labels.get(counts.most_common(1)[0][0], counts.most_common(1)[0][0])


def run_simulation(prompt: str, source: str = "cli", persist: bool = True) -> dict[str, Any]:
    summary = read_json(SUMMARY_PATH, {})
    dominant = _dominant_language(summary)
    signal_count = summary.get("signal_count", 0)
    message_count = summary.get("message_count", 0)
    if signal_count:
        partner_estimate = (
            f"Given the grounded local history, the partner side may notice {dominant} most. "
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
            "dominant_signal": dominant,
        },
        "partner_perspective_estimate": partner_estimate,
        "gap_or_alignment_note": (
            "The useful next check is whether the user's intended expression of care matches "
            f"the partner-side signal around {dominant}."
        ),
        "uncertainty": uncertainty,
        "signal_delta": {"simulated_loop_turns": 1, "dominant_signal_used": dominant},
        "interpretation_delta": f"Latest loop connected the user prompt to partner-side {dominant} signals.",
        "follow_up_question": "What specific moment from this week should Hitch compare against that pattern?",
        "created_at": now_iso(),
    }
    if persist:
        append_jsonl(SIMULATION_RUNS_PATH, result)
        record_interaction_delta(prompt, result)
    return result
