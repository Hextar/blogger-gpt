import yaml

from utils.config import get_template


def load_template(file_name=get_template()):
    """
    Load a template from a given file path.

    Args:
        file_name, the template file name
    """
    # Add "templates/" prefix if not already present
    if not file_name.startswith("templates/"):
        file_name = "templates/" + file_name

    # Add ".yaml" extension if not already present
    if not file_name.endswith(".yaml"):
        file_name = file_name + ".yaml"

    with open(file_name, 'r') as f:
        data = yaml.safe_load(f)

    return data

def get_chatgpt_name():
    """
    Get the name that ChatGPT should use.
    """
    data = load_template()
    return data.get('chatgpt_name', 'Chatgpt')


def get_chatgpt_pronoun():
    """
    Get the pronoun that ChatGPT should use.
    """
    data = load_template()
    return data.get('chatgpt_pronoun', 'They')


def get_eleven_labs_voice():
    """
    Get the voice tha Eleven Labs should use.
    """
    data = load_template()
    return data.get('eleven_labs_voice', 'Dorothy')


def get_user_name():
    """
    Get the name that should be used to refer to the user.
    """
    data = load_template()
    return data.get('user_name', 'User')

def get_chat_gpt_goes_first():
    """
    Get if ChatGPT will start the conversation.
    """
    data = load_template()
    chat_goes_first = data.get('chat_got_goes_first', 0)
    return chat_goes_first == '1' or chat_goes_first == 1

def get_prompt():
    """
    Get the prompt to set ChatGPT's behavior.
    """
    data = load_template()
    return data.get('prompt', '')
