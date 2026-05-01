from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from hitch.ingest import parse_csv
from hitch.simulation import run_simulation
from hitch.storage import append_jsonl, write_jsonl
from hitch import wiki


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

    def test_wiki_refresh_preserves_simulation_delta_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original_paths = (
                wiki.MESSAGE_PATH,
                wiki.SIGNALS_PATH,
                wiki.SUMMARY_PATH,
                wiki.INTERACTIONS_PATH,
            )
            try:
                wiki.MESSAGE_PATH = root / "messages.jsonl"
                wiki.SIGNALS_PATH = root / "signals.jsonl"
                wiki.SUMMARY_PATH = root / "summary.json"
                wiki.INTERACTIONS_PATH = root / "interaction_deltas.jsonl"
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
                        "signal_delta": {"dominant_signal_used": "time"},
                        "interpretation_delta": "Latest loop connected the prompt to time signals.",
                        "follow_up_question": "Which moment should be compared next?",
                        "created_at": "2026-01-02T00:00:00+00:00",
                    },
                )

                summary = wiki.build_wiki_state()
            finally:
                (
                    wiki.MESSAGE_PATH,
                    wiki.SIGNALS_PATH,
                    wiki.SUMMARY_PATH,
                    wiki.INTERACTIONS_PATH,
                ) = original_paths

        self.assertEqual(summary["simulation_delta_count"], 1)
        self.assertIn("latest_interpretation_delta", summary)
        self.assertIn("Which moment should be compared next?", summary["open_questions"])


if __name__ == "__main__":
    unittest.main()
