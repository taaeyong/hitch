from __future__ import annotations

import argparse

from .config import telegram_token
from .telegram import TelegramClient


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a single Hitch Telegram message without polling")
    parser.add_argument("chat_id", type=int, help="Telegram chat id")
    parser.add_argument("text", help="Message text to send")
    args = parser.parse_args()

    token = telegram_token(required=True)
    client = TelegramClient(token)
    client.send_message(args.chat_id, args.text)
    print(f"Sent Hitch message to chat_id={args.chat_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
