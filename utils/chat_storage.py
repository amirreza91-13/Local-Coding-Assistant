import json
from pathlib import Path

CHAT_FILE = Path("chat_history.json")


def save_chat(messages):

    with open(CHAT_FILE, "w", encoding="utf-8") as f:

        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=4
        )


def load_chat():

    if CHAT_FILE.exists():

        with open(CHAT_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    return []