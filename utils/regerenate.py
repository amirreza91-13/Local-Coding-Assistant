def last_user_message(messages):

    for message in reversed(messages):

        if message["role"] == "user":

            return message["content"]

    return ""