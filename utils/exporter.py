import json


def export_txt(messages):

    text = ""

    for msg in messages:

        text += f"{msg['role'].upper()}\n"

        text += msg["content"]

        text += "\n\n"

    return text


def export_json(messages):

    return json.dumps(
        messages,
        ensure_ascii=False,
        indent=4
    )