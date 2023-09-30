import os
from dotenv import load_dotenv

load_dotenv()


def get_agent():
    """
    Get the agent to be used.
    """
    return os.getenv('AGENT')


def get_debug():
    """
    Get the debug option.
    """
    debug = os.getenv('DEBUG')
    return debug == '1' or debug == 1


def get_open_ai_api_key():
    """
    Get Open AI API Key.
    """
    return os.getenv('OPEN_AI_API_KEY')


def get_open_ai_model():
    """
    Get Open AI Model.
    """
    return os.getenv('OPEN_AI_MODEL')