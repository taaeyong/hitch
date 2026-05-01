from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from typing import Any

from .config import telegram_token
from .demo import prepare
from .graph import GRAPH_PATH, export_graph
from .simulation import run_simulation
from .storage import read_json, write_json
from .wiki import SUMMARY_PATH


DAILY_QUESTION = "오늘 관계에서 사랑을 표현하거나 받고 싶었던 순간이 있었나요?"
HELP_TEXT = (
    "Hitch rehearsal commands\n"
    "/daily - 오늘의 관계 질문\n"
    "/loop [상황] - 시뮬레이션 기반 관계 점검\n"
    "/weekly - 누적 신호 리포트\n"
    "/space - 현재 relationship space 요약\n"
    "/graph - graph artifact 상태"
)
START_MESSAGES = (
    "Hitch는 사랑이 어떻게 표현되고, 어떻게 도착하는지 같이 보는 relationship coach예요.",
    "이번 리허설은 하나의 romantic relationship space를 만들고, 로컬에 있는 관계 기록으로 wiki 신호를 쌓아요.",
    "파트너 초대는 지금은 건너뛰고 solo rehearsal로 진행할게요. 나중에 invite code나 bot link를 붙일 수 있어요.",
    "지금 바로 시작해볼까요? /daily 로 첫 질문을 열거나 /loop 뒤에 상황을 적어 관계 신호를 점검할 수 있어요.",
    HELP_TEXT,
)


class TelegramClient:
    def __init__(self, token: str):
        self.base_url = f"https://api.telegram.org/bot{token}"

    def call(self, method: str, payload: dict[str, Any] | None = None, timeout: int = 30) -> dict[str, Any]:
        data = urllib.parse.urlencode(payload or {}).encode("utf-8")
        request = urllib.request.Request(f"{self.base_url}/{method}", data=data)
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    def send_message(self, chat_id: int, text: str) -> None:
        self.call("sendMessage", {"chat_id": chat_id, "text": text})


def check_token() -> dict[str, Any]:
    token = telegram_token(required=True)
    return TelegramClient(token).call("getMe", timeout=10)


def _weekly_report() -> str:
    summary = read_json(SUMMARY_PATH, {})
    counts = summary.get("love_language_signal_counts", {})
    if counts:
        strongest = max(counts.items(), key=lambda item: item[1])[0]
    else:
        strongest = "아직 뚜렷하지 않은 신호"
    return (
        "이번 주 관계 신호\n"
        f"- 누적 메시지: {summary.get('message_count', 0)}\n"
        f"- 누적 신호: {summary.get('signal_count', 0)}\n"
        f"- 가장 선명한 축: {strongest}\n"
        "- 다음 초점: 표현한 사랑이 상대에게 어떻게 도착했는지 한 장면으로 확인하기"
    )


def handle_text(text: str, chat_id: int, client: TelegramClient) -> None:
    normalized = text.strip()
    if normalized.startswith("/start"):
        prepare()
        for message in START_MESSAGES:
            client.send_message(chat_id, message)
    elif normalized.startswith("/help"):
        client.send_message(chat_id, HELP_TEXT)
    elif normalized.startswith("/daily"):
        client.send_message(chat_id, DAILY_QUESTION)
    elif normalized.startswith("/loop"):
        prompt = normalized.removeprefix("/loop").strip() or DAILY_QUESTION
        result = run_simulation(prompt, source="telegram")
        export_graph()
        client.send_message(
            chat_id,
            f"{result['partner_perspective_estimate']}\n\n{result['gap_or_alignment_note']}\n\n다음 질문: {result['follow_up_question']}",
        )
    elif normalized.startswith("/weekly"):
        report = _weekly_report()
        write_json(SUMMARY_PATH.parent.parent / "reports" / "latest_weekly.json", {"text": report})
        export_graph()
        client.send_message(chat_id, report)
    elif normalized.startswith("/space"):
        summary = read_json(SUMMARY_PATH, {})
        client.send_message(
            chat_id,
            f"main relationship space\nmessages={summary.get('message_count', 0)} signals={summary.get('signal_count', 0)}",
        )
    elif normalized.startswith("/graph"):
        graph = export_graph()
        client.send_message(chat_id, f"Graph ready: {GRAPH_PATH} nodes={len(graph['nodes'])} edges={len(graph['edges'])}")
    else:
        result = run_simulation(normalized, source="telegram")
        export_graph()
        client.send_message(chat_id, f"{result['partner_perspective_estimate']}\n\n{result['gap_or_alignment_note']}")


def run_bot() -> None:
    token = telegram_token(required=True)
    client = TelegramClient(token)
    me = client.call("getMe", timeout=10)
    username = me.get("result", {}).get("username", "unknown")
    print(f"Starting Hitch Telegram runtime as @{username}")
    offset = 0
    while True:
        updates = client.call("getUpdates", {"timeout": 25, "offset": offset}, timeout=35).get("result", [])
        for update in updates:
            offset = max(offset, update["update_id"] + 1)
            message = update.get("message") or update.get("edited_message") or {}
            text = message.get("text")
            chat = message.get("chat") or {}
            chat_id = chat.get("id")
            if text and chat_id:
                try:
                    handle_text(text, chat_id, client)
                except Exception as exc:  # noqa: BLE001 - keep bot responsive during rehearsal.
                    client.send_message(chat_id, f"Local rehearsal error: {exc}")
        time.sleep(0.2)
