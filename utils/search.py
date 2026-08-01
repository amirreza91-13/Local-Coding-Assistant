def search_messages(messages, keyword):

    keyword = keyword.lower()

    results = []

    for message in messages:

        if keyword in message["content"].lower():

            results.append(message)

    return results