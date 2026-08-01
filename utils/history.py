def build_prompt(history):

    prompt = ""

    for message in history:

        prompt += (
            f"{message['role']} : "
            f"{message['content']}\n"
        )

    return prompt