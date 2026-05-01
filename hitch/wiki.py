from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .ingest import MESSAGE_PATH
from .paths import SPACE_DIR, WIKI_DIR
from .storage import new_id, now_iso, read_json, read_jsonl, write_json, write_jsonl


SPACE_STATE_PATH = SPACE_DIR / "state.json"
SIGNALS_PATH = WIKI_DIR / "signals.jsonl"
SUMMARY_PATH = WIKI_DIR / "summary.json"
INTERACTIONS_PATH = WIKI_DIR / "interaction_deltas.jsonl"
FEEDBACK_STATE_PATH = WIKI_DIR / "feedback_state.json"

LOVE_LANGUAGE_KEYWORDS = {
    "words": ("고마워", "사랑", "좋아", "미안", "보고", "말", "칭찬", "thank", "love"),
    "time": ("같이", "함께", "만나", "시간", "데이트", "보자", "전화"),
    "acts": ("해줄", "도와", "챙겨", "준비", "데려", "사줘", "해줘"),
    "gifts": ("선물", "샀", "사왔", "꽃", "기념"),
    "touch": ("안아", "손", "뽀뽀", "키스", "스킨십"),
}
SIGNAL_ALIASES = {
    "words of affirmation": "words",
    "quality time": "time",
    "shared time and attentive follow-through": "time",
    "acts of service": "acts",
    "gifts or concrete tokens": "gifts",
    "physical closeness": "touch",
}


def create_or_refresh_space() -> dict[str, Any]:
    existing = read_json(SPACE_STATE_PATH, {})
    state = {
        "id": "main",
        "relationship_type": "romantic",
        "partner_label": existing.get("partner_label", "partner"),
        "current_state": existing.get("current_state", "grounded local rehearsal relationship space"),
        "daily_delivery_time": existing.get("daily_delivery_time", "21:30"),
        "love_language_mode": existing.get("love_language_mode", "delta-based"),
        "updated_at": now_iso(),
    }
    write_json(SPACE_STATE_PATH, state)
    return state


def _load_messages(path: Path = MESSAGE_PATH) -> list[dict[str, Any]]:
    return read_jsonl(path)


def _keyword_hits(text: str) -> list[str]:
    hits: list[str] = []
    lowered = text.lower()
    for category, keywords in LOVE_LANGUAGE_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            hits.append(category)
    return hits


def _canonical_signal(signal: str | None) -> str:
    if not signal:
        return "unclassified"
    return SIGNAL_ALIASES.get(signal, signal)


def build_wiki_state() -> dict[str, Any]:
    messages = _load_messages()
    existing_summary = read_json(SUMMARY_PATH, {})
    existing_deltas = read_jsonl(INTERACTIONS_PATH)
    sender_counts = Counter(row.get("sender") or "unknown" for row in messages)
    category_counts: Counter[str] = Counter()
    signals: list[dict[str, Any]] = []
    sender_category_counts: dict[str, Counter[str]] = defaultdict(Counter)

    for row in messages:
        text = row.get("text", "")
        hits = _keyword_hits(text)
        if not hits:
            continue
        sender = row.get("sender") or "unknown"
        for category in hits:
            category_counts[category] += 1
            sender_category_counts[sender][category] += 1
        signals.append(
            {
                "id": f"signal-{row.get('message_id')}",
                "source_message_id": row.get("message_id"),
                "sender": sender,
                "timestamp": row.get("timestamp"),
                "categories": hits,
                "evidence_excerpt": text[:180],
                "created_at": now_iso(),
            }
        )

    write_jsonl(SIGNALS_PATH, signals)
    open_questions = [
        "Which signals are stable patterns versus one-off context?",
        "Where does expressed love fail to land as received love?",
    ]
    for delta in existing_deltas[-3:]:
        question = delta.get("follow_up_question")
        if question and question not in open_questions:
            open_questions.append(question)

    feedback_state = refresh_feedback_state()
    summary = {
        "relationship_space_id": "main",
        "message_count": len(messages),
        "sender_count": len(sender_counts),
        "top_senders": sender_counts.most_common(6),
        "signal_count": len(signals),
        "love_language_signal_counts": dict(category_counts),
        "sender_signal_counts": {sender: dict(counts) for sender, counts in sender_category_counts.items()},
        "open_questions": open_questions,
        "simulation_delta_count": len(existing_deltas),
        "feedback_loop_count": feedback_state.get("loop_count", 0),
        "feedback_pattern_counts": feedback_state.get("pattern_counts", {}),
        "updated_at": now_iso(),
    }
    latest_delta = existing_deltas[-1] if existing_deltas else None
    if latest_delta:
        summary["latest_interpretation_delta"] = latest_delta.get("interpretation_delta", "")
    elif existing_summary.get("latest_interpretation_delta"):
        summary["latest_interpretation_delta"] = existing_summary["latest_interpretation_delta"]
    write_json(SUMMARY_PATH, summary)
    return summary


def refresh_feedback_state() -> dict[str, Any]:
    deltas = read_jsonl(INTERACTIONS_PATH)
    pattern_counts: Counter[str] = Counter()
    recent_deltas: list[dict[str, Any]] = []
    open_questions: list[str] = []
    for delta in deltas:
        signal_delta = delta.get("signal_delta", {})
        pattern = _canonical_signal(signal_delta.get("dominant_signal_used") or signal_delta.get("dominant_signal_label"))
        pattern_counts[pattern] += signal_delta.get("simulated_loop_turns", 1)
        question = delta.get("follow_up_question")
        if question and question not in open_questions:
            open_questions.append(question)
        recent_deltas.append(
            {
                "id": delta.get("id"),
                "created_at": delta.get("created_at"),
                "pattern": pattern,
                "pattern_label": signal_delta.get("dominant_signal_label"),
                "interpretation_delta": delta.get("interpretation_delta", ""),
                "follow_up_question": question,
            }
        )
    state = {
        "relationship_space_id": "main",
        "loop_count": len(deltas),
        "pattern_counts": dict(pattern_counts),
        "recent_deltas": recent_deltas[-8:],
        "open_questions": open_questions[-8:],
        "updated_at": now_iso(),
    }
    write_json(FEEDBACK_STATE_PATH, state)
    return state


def record_interaction_delta(prompt: str, result: dict[str, Any]) -> dict[str, Any]:
    delta = {
        "id": new_id("delta"),
        "relationship_space_id": "main",
        "prompt": prompt,
        "signal_delta": result.get("signal_delta", {}),
        "interpretation_delta": result.get("interpretation_delta", ""),
        "follow_up_question": result.get("follow_up_question", ""),
        "created_at": now_iso(),
    }
    from .storage import append_jsonl

    append_jsonl(INTERACTIONS_PATH, delta)
    summary = read_json(SUMMARY_PATH, {})
    summary.setdefault("simulation_delta_count", 0)
    summary["simulation_delta_count"] += 1
    summary["latest_interpretation_delta"] = delta["interpretation_delta"]
    feedback_state = refresh_feedback_state()
    summary["feedback_loop_count"] = feedback_state["loop_count"]
    summary["feedback_pattern_counts"] = feedback_state["pattern_counts"]
    summary["updated_at"] = now_iso()
    write_json(SUMMARY_PATH, summary)
    return delta
