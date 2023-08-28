import os
from dotenv import load_dotenv

load_dotenv()


def get_template():
    """
    Get the template to be used.
    """
    return os.getenv('TEMPLATE')


def get_silent():
    """
    Get the silent option.
    """
    return os.getenv('SILENT')


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


def get_eleven_labs_api_key():
    """
    Get Eleven labs API Key.
    """
    return os.getenv('ELEVEN_LABS_API_KEY')


def get_eleven_labs_model():
    """
    Get Eleven labs model.
    """
    return os.getenv('ELEVEN_LABS_MODEL')
