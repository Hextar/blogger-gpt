import yaml

def load_template(file_name):
    """
    Load a template from a given file path.

    Arg: the template file name
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

def get_lang(file_name):
    """
    Get the lang that ChatGPT should use.

    Arg: the template file name
    """
    data = load_template(file_name)
    return data.get('lang', 'en')

def get_chatgpt_name(file_name):
    """
    Get the name that ChatGPT should use.

    Arg: the template file name
    """
    data = load_template(file_name)
    return data.get('chatgpt_name', 'Chatgpt')

def get_eleven_labs_voice(file_name):
    """
    Get the voice tha Eleven Labs should use.

    Arg: the template file name
    """
    data = load_template(file_name)
    return data.get('eleven_labs_voice', 'Dorothy')

def get_user_name(file_name):
    """
    Get the name that should be used to refer to the user.

    Arg: the template file name
    """
    data = load_template(file_name)
    return data.get('user_name', 'User')

def get_prompt(file_name):
    """
    Get the prompt to set ChatGPT's behavior.

    Arg: the template file name
    """
    data = load_template(file_name)
    return data.get('prompt', '')

