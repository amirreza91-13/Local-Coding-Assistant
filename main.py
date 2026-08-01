from ollama import Client
import time

# ==========================================
# Mirhaj AI Studio
# Version : 2.0
# ==========================================

HOST = "http://localhost:11434"
MODEL = "qwen2.5-coder:3b"

client = Client(host=HOST)

SYSTEM_PROMPT = """
You are Mirhaj AI.

Your personality:
- Friendly
- Professional
- Helpful
- Honest
- Fast

Rules:
- Detect user's language automatically.
- Reply in same language.
- Persian -> Persian
- English -> English

Programming:
- Always use Markdown code blocks.
- Write modern optimized code.
- Never write broken code.
- Explain only if requested.

General:
- Format answers nicely.
- Use bullet points.
- Never invent facts.
"""

MAX_HISTORY = 10

chat_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def trim_history():
    """
    Keep only the latest conversation.
    """

    if len(chat_history) > MAX_HISTORY * 2 + 1:
        del chat_history[1:3]


def ask(prompt: str):

    chat_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    trim_history()

    start = time.time()

    response = client.chat(
        model=MODEL,
        messages=chat_history
    )

    elapsed = time.time() - start

    answer = response["message"]["content"]

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer, elapsed


def banner():

    print("\n")

    print("=" * 60)
    print("             MIRHAJ AI STUDIO")
    print("=" * 60)

    print(f"Model : {MODEL}")
    print(f"Host  : {HOST}")

    print("=" * 60)


if __name__ == "__main__":

    banner()

    while True:

        user = input("\nYou ➜ ")

        if user.lower() in [
            "exit",
            "quit",
            "/bye"
        ]:
            print("\n👋 Goodbye.")
            break

        try:

            answer, elapsed = ask(user)

            print("\nAI\n")
            print(answer)

            print(f"\n⚡ Response Time : {elapsed:.2f} sec")

        except KeyboardInterrupt:

            print("\nStopped.")
            break

        except Exception as e:

            print("\nError")
            print(e)