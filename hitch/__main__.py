from __future__ import annotations

import argparse

from .demo import check_environment, print_result
from .telegram import check_token, run_bot


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m hitch")
    parser.add_argument("--check", action="store_true", help="check local Telegram token/API availability")
    args = parser.parse_args()
    if args.check:
        env = check_environment(require_token=True)
        bot = check_token()
        print_result(
            "Checked Hitch Telegram runtime",
            {**env, "telegram_api_ok": bot.get("ok", False), "bot_username": bot.get("result", {}).get("username")},
        )
        return 0
    run_bot()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
