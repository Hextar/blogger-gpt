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
    return "[name] Your name is " + data.get('chatgpt_name', 'Chatgpt')


def get_chatgpt_role():
    """
    Get the role that ChatGPT should cover.
    """
    data = load_template()
    return "[role] " + data.get('chatgpt_role', 'Chatgpt')


def get_chatgpt_emotional_tone():
    """
    Get the emotional tone that ChatGPT should user.
    """
    data = load_template()
    return "[emotional_tone] " + data.get('chatgpt_emotional_tone', 'Chatgpt')


def get_chatgpt_competency():
    """
    Get the competency that ChatGPT should cover.
    """
    data = load_template()
    return "[competency] " + data.get('chatgpt_competency', 'Chatgpt')


def get_chatgpt_workflow():
    """
    Get the workflow that ChatGPT should follow.
    """
    data = load_template()
    return "[workflow] " + data.get('chatgpt_workflow', 'Chatgpt')


def get_chatgpt_goal(title = ""):
    """
    Get the goal that ChatGPT should follow.
    """
    data = load_template()
    return "[goal] " + data.get('chatgpt_goal', 'Chatgpt').replace('{title}', title)


def get_chatgpt_prompt(title = ""):
    """
    Load the prompt that ChatGPT should use.
    """
    return (
        get_chatgpt_name() +  "\n\n" +
        get_chatgpt_role() + "\n\n" +
        get_chatgpt_emotional_tone() + "\n\n" +
        get_chatgpt_competency() + "\n\n" +
        get_chatgpt_workflow() + "\n\n" +
        get_chatgpt_goal(title) + "\n\n"
    )
