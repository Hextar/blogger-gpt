import os
from dotenv import load_dotenv

load_dotenv()


def get_template():
    """
    Get the template to be used.
    """
    return os.getenv('TEMPLATE')


def get_debug():
    """
    Get the debug option.
    """
    debug = os.getenv('DEBUG')
    return debug == '1' or debug == 1

def get_reading_speed():
    """
    Get the reading speed option.
    """
    return os.getenv('READING_SPEED')


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
