from langchain_ollama import OllamaLLM

_models = {}


def get_model(model_name: str):

    if model_name not in _models:

        _models[model_name] = OllamaLLM(
            model=model_name
        )

    return _models[model_name]