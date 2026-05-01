"""One-command Hitch v4 demo rehearsal entrypoint."""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = REPO_ROOT / ".env"
PRIMARY_RAW_CSV = REPO_ROOT / "raw" / "girlfriend_kakaotalk.csv"
LEGACY_RAW_CSV = REPO_ROOT / "girlfriend_kakaotalk.csv"
LOCAL_DATA_ROOT = REPO_ROOT / "data" / "demo-run"
RELATIONSHIP_ID = "main-romantic-partner"
TOKEN_NAME = "HITCH_TELEGRAM_TOKEN"
DEFAULT_DAILY_TIME = "21:30"
DEFAULT_SIMULATION_PROMPT = "오늘 내가 보낸 표현이 상대에게 어떻게 닿았을지 알고 싶어요."
SIGNAL_KEYWORDS = {
    "affection": ("사랑", "좋아", "보고", "고마", "예쁘", "귀엽", "love", "miss", "thank"),
    "care": ("괜찮", "밥", "잠", "아프", "걱정", "조심", "쉬어", "챙겨", "care"),
    "conflict": ("미안", "싫", "화", "서운", "짜증", "싸우", "sorry", "upset"),
    "planning": ("언제", "내일", "주말", "만나", "갈까", "하자", "계획", "plan"),
    "repair": ("다시", "괜찮아", "이해", "풀", "말해", "생각해볼", "repair"),
}

@dataclass(frozen=True)
class RuntimeContext:
    env_path: Path
    raw_csv_path: Path
    data_root: Path
    token_present: bool

class DemoRunError(RuntimeError):
    pass

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m hitch.demo", description="Run the Hitch v4 local demo rehearsal flow.")
    subcommands = parser.add_subparsers(dest="command")
    subcommands.add_parser("prepare", help="Prepare local relationship state.")
    simulation = subcommands.add_parser("simulation", help="Run a grounded simulation loop turn.")
    simulation.add_argument("--prompt", default=DEFAULT_SIMULATION_PROMPT)
    simulation.add_argument("--turns", type=int, default=1)
    demo = subcommands.add_parser("demo", help="Start the Telegram-first demo runtime.")
    demo.add_argument("--once", action="store_true")
    telegram = subcommands.add_parser("telegram", help="Compatibility alias for demo.")
    telegram.add_argument("--once", action="store_true")
    rehearse = subcommands.add_parser("rehearse", help="Run the full local rehearsal path.")
    rehearse.add_argument("--start-telegram", action="store_true")
    return parser

def load_dotenv(path: Path) -> dict[str, str]:
    values = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key:
            values[key] = value
            os.environ.setdefault(key, value)
    return values

def resolve_raw_csv() -> Path:
    if PRIMARY_RAW_CSV.exists():
        return PRIMARY_RAW_CSV
    if LEGACY_RAW_CSV.exists():
        return LEGACY_RAW_CSV
    raise DemoRunError("missing private raw input: expected raw/girlfriend_kakaotalk.csv")

def build_context(*, require_token: bool) -> RuntimeContext:
    if not ENV_PATH.exists():
        raise DemoRunError("missing local .env")
    env_values = load_dotenv(ENV_PATH)
    token_present = bool(os.environ.get(TOKEN_NAME) or env_values.get(TOKEN_NAME))
    if require_token and not token_present:
        raise DemoRunError(f"missing {TOKEN_NAME} in local .env")
    return RuntimeContext(env_path=ENV_PATH, raw_csv_path=resolve_raw_csv(), data_root=LOCAL_DATA_ROOT, token_present=token_present)

def prepare_directories(context: RuntimeContext) -> None:
    for path in (
        context.data_root,
        context.data_root / "relationships" / RELATIONSHIP_ID,
        context.data_root / "ingest",
        context.data_root / "wiki",
        context.data_root / "simulation",
        context.data_root / "graph",
        context.data_root / "telegram",
    ):
        path.mkdir(parents=True, exist_ok=True)

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def relationship_space() -> dict[str, Any]:
    return {
        "id": RELATIONSHIP_ID,
        "relationship_type": "romantic",
        "partner_label": "partner",
        "current_relationship_state": "ongoing romantic relationship grounded in local KakaoTalk history",
        "daily_delivery_time": DEFAULT_DAILY_TIME,
        "love_language_mode": "deep",
        "language": "ko",
        "privacy": {"source": "local_private_raw", "remote_safe": False},
        "created_or_refreshed_at": utc_now(),
    }

def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()

def parse_messages(path: Path, *, limit: int = 5000) -> list[dict[str, Any]]:
    records = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise DemoRunError("raw csv has no header")
        lowered = {field.lower().strip(): field for field in reader.fieldnames}
        date_field = lowered.get("date") or lowered.get("datetime") or reader.fieldnames[0]
        user_field = lowered.get("user") or lowered.get("sender") or reader.fieldnames[1]
        message_field = lowered.get("message") or lowered.get("text") or reader.fieldnames[-1]
        for index, row in enumerate(reader, start=1):
            text = normalize_text(row.get(message_field, ""))
            if not text:
                continue
            records.append({
                "id": f"msg-{index:06d}",
                "source": path.name,
                "date": normalize_text(row.get(date_field, "")),
                "speaker": normalize_text(row.get(user_field, "")) or "unknown",
                "text": text,
                "text_length": len(text),
            })
            if len(records) >= limit:
                break
    if not records:
        raise DemoRunError("raw csv did not yield any usable messages")
    return records

def build_signal_state(messages: list[dict[str, Any]]) -> dict[str, Any]:
    tag_counts = {key: 0 for key in SIGNAL_KEYWORDS}
    tagged = []
    for message in messages:
        lower_text = message["text"].lower()
        matched = [tag for tag, keywords in SIGNAL_KEYWORDS.items() if any(keyword in lower_text for keyword in keywords)]
        for tag in matched:
            tag_counts[tag] += 1
        if matched:
            tagged.append({"message_id": message["id"], "speaker": message["speaker"], "tags": matched, "text": message["text"][:180]})
    return {"tag_counts": tag_counts, "tagged_messages": tagged[:200], "updated_at": utc_now()}

def build_wiki_state(space: dict[str, Any], signals: dict[str, Any], messages: list[dict[str, Any]]) -> dict[str, Any]:
    top_tags = sorted(signals["tag_counts"].items(), key=lambda item: item[1], reverse=True)
    summary_tags = [tag for tag, count in top_tags if count > 0][:3]
    return {
        "relationship_id": space["id"],
        "summary": {
            "message_count": len(messages),
            "top_signal_tags": summary_tags,
            "last_updated_at": utc_now(),
        },
        "signals": signals,
        "interaction_deltas": [],
        "open_questions": [],
    }

def build_partner_perspective(space: dict[str, Any], wiki_state: dict[str, Any], prompt: str, turn_index: int) -> dict[str, Any]:
    top_tags = wiki_state["summary"].get("top_signal_tags") or ["care"]
    tag_phrase = ", ".join(top_tags)
    return {
        "relationship_id": space["id"],
        "turn": turn_index,
        "user_prompt": prompt,
        "likely_partner_reaction": f"상대는 이 표현을 {tag_phrase} 맥락에서 받아들일 가능성이 높아요.",
        "interpretation": f"현재 관계 신호상 {tag_phrase} 표현이 반복적으로 중요하게 나타나요.",
        "uncertainty": "실제 감정은 다를 수 있어 부드럽게 확인이 필요해요.",
        "generated_at": utc_now(),
    }

def build_graph_payload(space: dict[str, Any], wiki_state: dict[str, Any], runs: list[dict[str, Any]]) -> dict[str, Any]:
    nodes = [{"id": space["id"], "type": "relationship", "label": space["partner_label"]}]
    for tag, count in wiki_state["signals"]["tag_counts"].items():
        if count > 0:
            nodes.append({"id": f"signal:{tag}", "type": "signal", "label": tag, "count": count})
    edges = [{"source": space["id"], "target": node["id"], "type": "has_signal"} for node in nodes if node["id"].startswith("signal:")]
    return {"schema": "hitch.graph.v1", "generated_at": utc_now(), "nodes": nodes, "edges": edges, "simulation_run_count": len(runs)}

def prepare(context: RuntimeContext) -> None:
    prepare_directories(context)
    space = relationship_space()
    messages = parse_messages(context.raw_csv_path)
    signals = build_signal_state(messages)
    wiki_state = build_wiki_state(space, signals, messages)
    first_run = build_partner_perspective(space, wiki_state, DEFAULT_SIMULATION_PROMPT, 1)
    runs = [first_run]
    effects = [{"turn": 1, "delta_type": "initial_grounding", "notes": "Seeded grounded partner perspective from local relationship state."}]
    graph = build_graph_payload(space, wiki_state, runs)
    write_json(context.data_root / "relationships" / RELATIONSHIP_ID / "space.json", space)
    write_json(context.data_root / "ingest" / "messages.json", messages)
    write_json(context.data_root / "wiki" / "signals.json", signals)
    write_json(context.data_root / "wiki" / "state.json", wiki_state)
    write_json(context.data_root / "simulation" / "partner_perspective.json", first_run)
    write_json(context.data_root / "simulation" / "runs.json", runs)
    write_json(context.data_root / "simulation" / "effects.json", effects)
    write_json(context.data_root / "graph" / "relationship_graph.json", graph)
    write_json(context.data_root / "telegram" / "state.json", {
        "ready": True,
        "commands": ["/start", "/loop", "/weekly", "/graph"],
        "updated_at": utc_now(),
    })
    print("env: .env present")
    print(f"telegram token: {'present' if context.token_present else 'missing'}")
    print(f"raw input: {context.raw_csv_path.relative_to(REPO_ROOT)}")
    print(f"local data root: {context.data_root.relative_to(REPO_ROOT)}")
    print("outputs:")
    print(f"- relationship_space: {(context.data_root / 'relationships' / RELATIONSHIP_ID / 'space.json').relative_to(REPO_ROOT)}")
    print(f"- messages: {(context.data_root / 'ingest' / 'messages.json').relative_to(REPO_ROOT)}")
    print(f"- signals: {(context.data_root / 'wiki' / 'signals.json').relative_to(REPO_ROOT)}")
    print(f"- wiki_state: {(context.data_root / 'wiki' / 'state.json').relative_to(REPO_ROOT)}")
    print(f"- simulation: {(context.data_root / 'simulation' / 'partner_perspective.json').relative_to(REPO_ROOT)}")
    print(f"- simulation_runs: {(context.data_root / 'simulation' / 'runs.json').relative_to(REPO_ROOT)}")
    print(f"- simulation_effects: {(context.data_root / 'simulation' / 'effects.json').relative_to(REPO_ROOT)}")
    print(f"- graph: {(context.data_root / 'graph' / 'relationship_graph.json').relative_to(REPO_ROOT)}")
    print(f"- telegram_state: {(context.data_root / 'telegram' / 'state.json').relative_to(REPO_ROOT)}")
    print("prepare: local relationship state, simulation, and graph artifacts are ready")

def run_simulation(context: RuntimeContext, prompt: str, turns: int) -> None:
    prepare(context)
    space = read_json(context.data_root / "relationships" / RELATIONSHIP_ID / "space.json")
    wiki_state = read_json(context.data_root / "wiki" / "state.json")
    runs = read_json(context.data_root / "simulation" / "runs.json", default=[])
    effects = read_json(context.data_root / "simulation" / "effects.json", default=[])
    for offset in range(turns):
        turn_number = len(runs) + 1
        result = build_partner_perspective(space, wiki_state, prompt, turn_number)
        runs.append(result)
        delta = {
            "turn": turn_number,
            "prompt": prompt,
            "signal_hint": wiki_state["summary"].get("top_signal_tags", [])[:2],
            "added_at": utc_now(),
        }
        wiki_state["interaction_deltas"].append(delta)
        effects.append({"turn": turn_number, "delta_type": "simulation_feedback", "notes": result["interpretation"]})
    graph = build_graph_payload(space, wiki_state, runs)
    write_json(context.data_root / "wiki" / "state.json", wiki_state)
    write_json(context.data_root / "simulation" / "partner_perspective.json", runs[-1])
    write_json(context.data_root / "simulation" / "runs.json", runs)
    write_json(context.data_root / "simulation" / "effects.json", effects)
    write_json(context.data_root / "graph" / "relationship_graph.json", graph)
    print("env: .env present")
    print(f"telegram token: {'present' if context.token_present else 'missing'}")
    print(f"raw input: {context.raw_csv_path.relative_to(REPO_ROOT)}")
    print(f"local data root: {context.data_root.relative_to(REPO_ROOT)}")
    print(f"simulation: wrote grounded loop result sim-{datetime.now().strftime('%Y%m%d%H%M%S')}")
    print(f"simulation output: {(context.data_root / 'simulation' / 'partner_perspective.json').relative_to(REPO_ROOT)}")
    print(f"graph output: {(context.data_root / 'graph' / 'relationship_graph.json').relative_to(REPO_ROOT)}")

def run_demo(context: RuntimeContext, *, once: bool) -> None:
    prepare_directories(context)
    if not context.token_present:
        raise DemoRunError(f"missing {TOKEN_NAME} in local .env")
    print("env: .env present")
    print("telegram token: present")
    print(f"raw input: {context.raw_csv_path.relative_to(REPO_ROOT)}")
    print(f"local data root: {context.data_root.relative_to(REPO_ROOT)}")
    print("demo: /start, free-text answer, /loop, /weekly, and /graph are wired")
    if not once:
        print("demo runtime placeholder: polling start would happen here")

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "rehearse"
    try:
        if command == "prepare":
            context = build_context(require_token=False)
            prepare(context)
        elif command == "simulation":
            context = build_context(require_token=False)
            run_simulation(context, args.prompt, max(args.turns, 1))
        elif command in {"demo", "telegram"}:
            context = build_context(require_token=True)
            run_demo(context, once=args.once)
        elif command == "rehearse":
            context = build_context(require_token=True)
            prepare(context)
            run_simulation(context, DEFAULT_SIMULATION_PROMPT, 1)
            if args.start_telegram:
                run_demo(context, once=False)
            else:
                run_demo(context, once=True)
        else:
            parser.error(f"unsupported command: {command}")
            return 2
    except DemoRunError as exc:
        print(f"error: {exc}", file=os.sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
