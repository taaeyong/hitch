from __future__ import annotations

import argparse
from typing import Any

from .config import telegram_token
from .graph import GRAPH_PATH, export_graph
from .ingest import DEFAULT_RAW_CSV, ingest_girlfriend_csv
from .paths import DATA_DIR, ENV_FILE, ensure_data_dirs
from .simulation import SIMULATION_EFFECTS_PATH, SIMULATION_SNAPSHOT_PATH, run_simulation
from .storage import write_json
from .wiki import SUMMARY_PATH, create_or_refresh_space, build_wiki_state


def prepare() -> dict[str, Any]:
    ensure_data_dirs()
    state = create_or_refresh_space()
    ingest_meta = ingest_girlfriend_csv(DEFAULT_RAW_CSV)
    summary = build_wiki_state()
    graph = export_graph()
    return {
        "relationship_space": state,
        "ingest": ingest_meta,
        "summary_path": str(SUMMARY_PATH),
        "graph_path": str(GRAPH_PATH),
        "simulation_effects_path": str(SIMULATION_EFFECTS_PATH),
        "simulation_snapshot_path": str(SIMULATION_SNAPSHOT_PATH),
        "graph_nodes": len(graph["nodes"]),
        "graph_edges": len(graph["edges"]),
    }


def rehearse(prompt: str) -> dict[str, Any]:
    prepared = prepare()
    simulation = run_simulation(prompt, source="rehearse")
    graph = export_graph()
    report_path = DATA_DIR / "demo-run" / "latest_rehearsal.json"
    write_json(
        report_path,
        {
            "prepared": prepared,
            "simulation": simulation,
            "graph_path": str(GRAPH_PATH),
            "telegram_ready": bool(telegram_token(required=False)),
        },
    )
    return {
        "report_path": str(report_path),
        "simulation": simulation,
        "simulation_effects_path": str(SIMULATION_EFFECTS_PATH),
        "simulation_snapshot_path": str(SIMULATION_SNAPSHOT_PATH),
        "graph_nodes": len(graph["nodes"]),
    }


def check_environment(require_token: bool = False) -> dict[str, Any]:
    token_available = bool(telegram_token(required=require_token))
    return {
        "env_file": str(ENV_FILE),
        "env_file_exists": ENV_FILE.exists(),
        "raw_girlfriend_csv": str(DEFAULT_RAW_CSV),
        "raw_girlfriend_csv_exists": DEFAULT_RAW_CSV.exists(),
        "telegram_token_available": token_available,
        "data_dir": str(DATA_DIR),
    }


def print_result(title: str, payload: dict[str, Any]) -> None:
    print(title)
    for key, value in payload.items():
        if key == "relationship_space":
            print(f"- {key}: {value.get('id')} ({value.get('relationship_type')})")
        elif key == "simulation":
            print(f"- partner_perspective_estimate: {value.get('partner_perspective_estimate')}")
            print(f"- gap_or_alignment_note: {value.get('gap_or_alignment_note')}")
            print(f"- uncertainty: {value.get('uncertainty')}")
        elif key == "simulation_effects_path":
            print(f"- {key}: {value}")
        elif key == "simulation_snapshot_path":
            print(f"- {key}: {value}")
        else:
            print(f"- {key}: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m hitch.demo")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("prepare")
    subparsers.add_parser("telegram")
    simulation_parser = subparsers.add_parser("simulation")
    simulation_parser.add_argument("prompt", nargs="?", default="이번 주 관계에서 내가 놓친 신호가 있을까?")
    rehearse_parser = subparsers.add_parser("rehearse")
    rehearse_parser.add_argument("prompt", nargs="?", default="오늘 관계 점검에서 어떤 부분을 먼저 보면 좋을까?")
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--require-token", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "rehearse"
    if command == "prepare":
        print_result("Prepared Hitch local rehearsal state", prepare())
        return 0
    if command == "simulation":
        result = run_simulation(args.prompt, source="cli")
        export_graph()
        print_result("Ran Hitch simulation loop", {"simulation": result, "graph_path": str(GRAPH_PATH)})
        return 0
    if command == "rehearse":
        print_result("Ran Hitch rehearsal", rehearse(args.prompt))
        return 0
    if command == "check":
        print_result("Checked Hitch environment", check_environment(require_token=args.require_token))
        return 0
    if command == "telegram":
        from .telegram import run_bot

        run_bot()
        return 0
    parser.error(f"unknown command: {command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
