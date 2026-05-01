from __future__ import annotations

import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import hitch.demo as demo


class DemoRuntimeTest(unittest.TestCase):
    def runtime(self, *, token: str = "secret-token") -> contextlib.AbstractContextManager[Path]:
        @contextlib.contextmanager
        def _runtime() -> Path:
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                raw_dir = root / "raw"
                raw_dir.mkdir()
                (root / ".env").write_text(f"{demo.TOKEN_NAME}={token}\n", encoding="utf-8")
                (raw_dir / "girlfriend_kakaotalk.csv").write_text(
                    "Date,User,Message\n"
                    "2026-04-01,user,오늘 고마웠고 내일 만나자\n"
                    "2026-04-01,partner,괜찮아 밥 잘 챙겨\n"
                    "2026-04-02,user,미안해 다시 말해보고 싶어\n",
                    encoding="utf-8",
                )
                data_root = root / "data" / "demo-run"
                with mock.patch.object(demo, "REPO_ROOT", root), mock.patch.object(
                    demo, "ENV_PATH", root / ".env"
                ), mock.patch.object(
                    demo, "PRIMARY_RAW_CSV", raw_dir / "girlfriend_kakaotalk.csv"
                ), mock.patch.object(
                    demo, "LEGACY_RAW_CSV", root / "girlfriend_kakaotalk.csv"
                ), mock.patch.object(
                    demo, "LOCAL_DATA_ROOT", data_root
                ), mock.patch.dict(
                    os.environ, {}, clear=True
                ):
                    yield root

        return _runtime()

    def test_prepare_writes_rehearsal_artifacts(self) -> None:
        with self.runtime() as root:
            self.assertEqual(demo.main(["prepare"]), 0)
            data_root = root / "data" / "demo-run"
            expected = [
                data_root / "relationships" / demo.RELATIONSHIP_ID / "space.json",
                data_root / "ingest" / "messages.json",
                data_root / "wiki" / "signals.json",
                data_root / "wiki" / "state.json",
                data_root / "simulation" / "partner_perspective.json",
                data_root / "simulation" / "runs.json",
                data_root / "simulation" / "effects.json",
                data_root / "graph" / "relationship_graph.json",
                data_root / "telegram" / "state.json",
            ]
            for path in expected:
                self.assertTrue(path.exists(), path)

            graph = json.loads((data_root / "graph" / "relationship_graph.json").read_text(encoding="utf-8"))
            self.assertEqual(graph["schema"], "hitch.graph.v1")
            self.assertTrue(graph["nodes"])

    def test_simulation_appends_wiki_deltas(self) -> None:
        with self.runtime() as root:
            self.assertEqual(demo.main(["prepare"]), 0)
            self.assertEqual(demo.main(["simulation", "--prompt", "오늘 고맙다고 더 말하고 싶어", "--turns", "2"]), 0)
            data_root = root / "data" / "demo-run"
            runs = json.loads((data_root / "simulation" / "runs.json").read_text(encoding="utf-8"))
            effects = json.loads((data_root / "simulation" / "effects.json").read_text(encoding="utf-8"))
            wiki = json.loads((data_root / "wiki" / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(len(runs), 3)
            self.assertEqual(len(effects), 3)
            self.assertEqual(len(wiki["interaction_deltas"]), 2)
            self.assertIn("care", wiki["signals"]["tag_counts"])

    def test_demo_once_does_not_print_token(self) -> None:
        token = "super-secret-token"
        with self.runtime(token=token):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(demo.main(["demo", "--once"]), 0)
            output = stream.getvalue()
            self.assertIn("demo: /start", output)
            self.assertNotIn(token, output)

if __name__ == "__main__":
    unittest.main()
