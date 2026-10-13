import json
import shutil
from datetime import datetime
from pathlib import Path

# Store chat history beside the project, independent of the launch directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHAT_FILE = PROJECT_ROOT / "chat_history.json"


def save_chat(messages):
    """Persist chat history atomically so interrupted writes do not corrupt it."""
    temporary_file = CHAT_FILE.with_suffix(".json.tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=2)
        file.flush()

    temporary_file.replace(CHAT_FILE)


def load_chat():
    """Load valid chat messages and preserve malformed history for recovery."""
    if not CHAT_FILE.exists():
        return []

    try:
        with CHAT_FILE.open("r", encoding="utf-8") as file:
            messages = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_file = CHAT_FILE.with_name(
            f"chat_history.corrupt-{timestamp}.json"
        )
        try:
            shutil.copy2(CHAT_FILE, backup_file)
        except OSError:
            # Keep the original file untouched if a recovery copy cannot be made.
            pass
        raise RuntimeError(
            f"Could not read chat history. The original file is preserved at "
            f"{CHAT_FILE}; check its format or recover from "
            f"{backup_file.name} if that copy was created."
        ) from exc

    if not isinstance(messages, list):
        raise RuntimeError("Chat history must be a JSON list of messages.")

    valid_messages = []
    for message in messages:
        if (
            isinstance(message, dict)
            and message.get("role") in {"user", "assistant"}
            and isinstance(message.get("content"), str)
        ):
            valid_messages.append(
                {"role": message["role"], "content": message["content"]}
            )

    return valid_messages
