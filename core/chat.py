from core.models import get_model
from core.prompt import SYSTEM_PROMPT

from utils.history import build_prompt


def ask(
    model_name,
    history,
    user_message
):

    model = get_model(model_name)

    prompt = SYSTEM_PROMPT

    prompt += "\n"

    prompt += build_prompt(history)

    prompt += f"\nuser : {user_message}"

    return model.invoke(prompt)