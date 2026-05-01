from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from hitch import simulation
from hitch import graph
from hitch import telegram, wiki
from hitch.ingest import parse_csv
from hitch.simulation import run_simulation
from hitch.storage import append_jsonl, read_json, read_jsonl, write_json, write_jsonl


class FakeTelegramClient:
    def __init__(self) -> None:
        self.messages: list[tuple[int, str]] = []

    def send_message(self, chat_id: int, text: str) -> None:
        self.messages.append((chat_id, text))


class IngestTests(unittest.TestCase):
    def test_parse_utf16_kakao_like_csv(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            path.write_text("날짜,작성자,내용\n2026-01-01,A,같이 산책하자\n", encoding="utf-16")
            records, meta = parse_csv(path)
        self.assertEqual(meta["encoding"], "utf-16")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].sender, "A")
        self.assertIn("산책", records[0].text)

    def test_simulation_has_uncertainty_and_delta(self) -> None:
        result = run_simulation("오늘 관계 점검", persist=False)
        self.assertIn("partner_perspective_estimate", result)
        self.assertIn("uncertainty", result)
        self.assertEqual(result["signal_delta"]["simulated_loop_turns"], 1)

    def test_simulation_persists_effect_and_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original_simulation_paths = (
                simulation.SUMMARY_PATH,
                simulation.SIMULATION_RUNS_PATH,
                simulation.SIMULATION_EFFECTS_PATH,
                simulation.SIMULATION_SNAPSHOT_PATH,
                simulation.FEEDBACK_STATE_PATH,
            )
            original_wiki_paths = (
                wiki.SUMMARY_PATH,
                wiki.INTERACTIONS_PATH,
                wiki.FEEDBACK_STATE_PATH,
            )
            try:
                summary_path = root / "summary.json"
                simulation.SUMMARY_PATH = summary_path
                wiki.SUMMARY_PATH = summary_path
                wiki.INTERACTIONS_PATH = root / "interaction_deltas.jsonl"
                wiki.FEEDBACK_STATE_PATH = root / "feedback_state.json"
                simulation.SIMULATION_RUNS_PATH = root / "runs.jsonl"
                simulation.SIMULATION_EFFECTS_PATH = root / "effects.jsonl"
                simulation.SIMULATION_SNAPSHOT_PATH = root / "latest_snapshot.json"
                simulation.FEEDBACK_STATE_PATH = root / "feedback_state.json"

                result = simulation.run_simulation("이번 주 신호 점검", source="test")
                effects = read_jsonl(root / "effects.jsonl")
                snapshot = read_json(root / "latest_snapshot.json", {})
                feedback_state = read_json(root / "feedback_state.json", {})
            finally:
                (
                    simulation.SUMMARY_PATH,
                    simulation.SIMULATION_RUNS_PATH,
                    simulation.SIMULATION_EFFECTS_PATH,
                    simulation.SIMULATION_SNAPSHOT_PATH,
                    simulation.FEEDBACK_STATE_PATH,
                ) = original_simulation_paths
                (
                    wiki.SUMMARY_PATH,
                    wiki.INTERACTIONS_PATH,
                    wiki.FEEDBACK_STATE_PATH,
                ) = original_wiki_paths

        self.assertEqual(len(effects), 1)
        self.assertEqual(effects[0]["simulation_run_id"], result["id"])
        self.assertEqual(effects[0]["changed"]["feedback_loop_count"], 1)
        self.assertEqual(snapshot["latest_simulation_run_id"], result["id"])
        self.assertEqual(snapshot["effect_count"], 1)
        self.assertEqual(snapshot["feedback_state"]["loop_count"], 1)
        self.assertEqual(feedback_state["loop_count"], 1)

    def test_wiki_refresh_preserves_simulation_delta_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original_paths = (
                wiki.MESSAGE_PATH,
                wiki.SIGNALS_PATH,
                wiki.SUMMARY_PATH,
                wiki.INTERACTIONS_PATH,
                wiki.FEEDBACK_STATE_PATH,
            )
            try:
                wiki.MESSAGE_PATH = root / "messages.jsonl"
                wiki.SIGNALS_PATH = root / "signals.jsonl"
                wiki.SUMMARY_PATH = root / "summary.json"
                wiki.INTERACTIONS_PATH = root / "interaction_deltas.jsonl"
                wiki.FEEDBACK_STATE_PATH = root / "feedback_state.json"
                write_jsonl(
                    wiki.MESSAGE_PATH,
                    [
                        {
                            "message_id": "m1",
                            "timestamp": "2026-01-01",
                            "sender": "A",
                            "text": "같이 시간 보내자",
                        }
                    ],
                )
                append_jsonl(
                    wiki.INTERACTIONS_PATH,
                    {
                        "id": "delta-1",
                        "signal_delta": {"dominant_signal_used": "quality time"},
                        "interpretation_delta": "Latest loop connected the prompt to time signals.",
                        "follow_up_question": "Which moment should be compared next?",
                        "created_at": "2026-01-02T00:00:00+00:00",
                    },
                )

                summary = wiki.build_wiki_state()
                feedback_state = read_json(root / "feedback_state.json", {})
            finally:
                (
                    wiki.MESSAGE_PATH,
                    wiki.SIGNALS_PATH,
                    wiki.SUMMARY_PATH,
                    wiki.INTERACTIONS_PATH,
                    wiki.FEEDBACK_STATE_PATH,
                ) = original_paths

        self.assertEqual(summary["simulation_delta_count"], 1)
        self.assertEqual(summary["feedback_loop_count"], 1)
        self.assertEqual(feedback_state["pattern_counts"]["time"], 1)
        self.assertIn("latest_interpretation_delta", summary)
        self.assertIn("Which moment should be compared next?", summary["open_questions"])

    def test_graph_includes_feedback_state_and_questions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original_paths = (
                graph.SPACE_STATE_PATH,
                graph.SUMMARY_PATH,
                graph.SIGNALS_PATH,
                graph.INTERACTIONS_PATH,
                graph.FEEDBACK_STATE_PATH,
                graph.SIMULATION_RUNS_PATH,
                graph.SIMULATION_EFFECTS_PATH,
                graph.SIMULATION_SNAPSHOT_PATH,
                graph.GRAPH_PATH,
            )
            try:
                graph.SPACE_STATE_PATH = root / "space.json"
                graph.SUMMARY_PATH = root / "summary.json"
                graph.SIGNALS_PATH = root / "signals.jsonl"
                graph.INTERACTIONS_PATH = root / "interaction_deltas.jsonl"
                graph.FEEDBACK_STATE_PATH = root / "feedback_state.json"
                graph.SIMULATION_RUNS_PATH = root / "runs.jsonl"
                graph.SIMULATION_EFFECTS_PATH = root / "effects.jsonl"
                graph.SIMULATION_SNAPSHOT_PATH = root / "snapshot.json"
                graph.GRAPH_PATH = root / "relationship_graph.json"
                append_jsonl(
                    graph.INTERACTIONS_PATH,
                    {
                        "id": "delta-1",
                        "signal_delta": {"dominant_signal_used": "time"},
                        "follow_up_question": "Which moment should be compared next?",
                    },
                )
                write_jsonl(graph.SIGNALS_PATH, [])

                write_json(graph.SUMMARY_PATH, {"love_language_signal_counts": {"time": 1}})
                write_json(
                    graph.FEEDBACK_STATE_PATH,
                    {
                        "loop_count": 1,
                        "pattern_counts": {"time": 1},
                        "open_questions": ["Which moment should be compared next?"],
                    },
                )

                payload = graph.export_graph()
            finally:
                (
                    graph.SPACE_STATE_PATH,
                    graph.SUMMARY_PATH,
                    graph.SIGNALS_PATH,
                    graph.INTERACTIONS_PATH,
                    graph.FEEDBACK_STATE_PATH,
                    graph.SIMULATION_RUNS_PATH,
                    graph.SIMULATION_EFFECTS_PATH,
                    graph.SIMULATION_SNAPSHOT_PATH,
                    graph.GRAPH_PATH,
                ) = original_paths

        node_ids = {node["id"] for node in payload["nodes"]}
        edge_types = {edge["type"] for edge in payload["edges"]}
        self.assertIn("artifact:feedback-state", node_ids)
        self.assertIn("question:feedback-1", node_ids)
        self.assertIn("raises", edge_types)

    def test_telegram_help_exposes_demo_commands(self) -> None:
        client = FakeTelegramClient()
        telegram.handle_text("/help", 42, client)  # type: ignore[arg-type]

        self.assertEqual(len(client.messages), 1)
        self.assertEqual(client.messages[0][0], 42)
        self.assertIn("/daily", client.messages[0][1])
        self.assertIn("/loop", client.messages[0][1])
        self.assertIn("/weekly", client.messages[0][1])
        self.assertIn("/graph", client.messages[0][1])


if __name__ == "__main__":
    unittest.main()
