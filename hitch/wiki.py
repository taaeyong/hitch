from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .ingest import MESSAGE_PATH
from .paths import SPACE_DIR, WIKI_DIR
from .storage import now_iso, read_json, write_json, write_jsonl


SPACE_STATE_PATH = SPACE_DIR / "state.json"
SIGNALS_PATH = WIKI_DIR / "signals.jsonl"
SUMMARY_PATH = WIKI_DIR / "summary.json"
INTERACTIONS_PATH = WIKI_DIR / "interaction_deltas.jsonl"

LOVE_LANGUAGE_KEYWORDS = {
    "words": ("고마워", "사랑", "좋아", "미안", "보고", "말", "칭찬", "thank", "love"),
    "time": ("같이", "함께", "만나", "시간", "데이트", "보자", "전화"),
    "acts": ("해줄", "도와", "챙겨", "준비", "데려", "사줘", "해줘"),
    "gifts": ("선물", "샀", "사왔", "꽃", "기념"),
    "touch": ("안아", "손", "뽀뽀", "키스", "스킨십"),
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
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            import json

            rows.append(json.loads(line))
    return rows


def _keyword_hits(text: str) -> list[str]:
    hits: list[str] = []
    lowered = text.lower()
    for category, keywords in LOVE_LANGUAGE_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            hits.append(category)
    return hits


def build_wiki_state() -> dict[str, Any]:
    messages = _load_messages()
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
    summary = {
        "relationship_space_id": "main",
        "message_count": len(messages),
        "sender_count": len(sender_counts),
        "top_senders": sender_counts.most_common(6),
        "signal_count": len(signals),
        "love_language_signal_counts": dict(category_counts),
        "sender_signal_counts": {sender: dict(counts) for sender, counts in sender_category_counts.items()},
        "open_questions": [
            "Which signals are stable patterns versus one-off context?",
            "Where does expressed love fail to land as received love?",
        ],
        "updated_at": now_iso(),
    }
    write_json(SUMMARY_PATH, summary)
    return summary


def record_interaction_delta(prompt: str, result: dict[str, Any]) -> dict[str, Any]:
    delta = {
        "id": f"delta-{now_iso()}",
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
    summary["updated_at"] = now_iso()
    write_json(SUMMARY_PATH, summary)
    return delta
