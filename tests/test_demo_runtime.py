from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from hitch.ingest import parse_csv
from hitch.simulation import run_simulation


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


if __name__ == "__main__":
    unittest.main()
