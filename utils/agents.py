import yaml
from simple_term_menu import TerminalMenu
import os


def load_agents(directory = "agents"):
    """
    Load menu options with filenames from YAML files in the specified directory.

    Returns:
        list: List of menu options containing filenames.
    """
    menu_options = []

    # Check if the directory exists
    if os.path.exists(directory) and os.path.isdir(directory):
        # Loop through files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                menu_options.append(filename)

    return menu_options


def show_menu():
    """
    Display a menu with selectable options using inquirer.

    Returns:
        str: The selected menu option.
    """
    menu_entries = load_agents()
    terminal_menu = TerminalMenu(
        menu_entries=menu_entries,
        title="🕵️  Please select an Agent:",
        menu_cursor="👉 ",
        cycle_cursor=True,
    )
    menu_entry_index = terminal_menu.show()
    return menu_entries[menu_entry_index]


def extract_data_from_yaml(file_path):
    """
    Extract data from a YAML file.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The extracted data as a dictionary.
    """
    try:
        with open("agents/" + file_path, 'r') as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            return data
    except FileNotFoundError:
        print(f"❌ The file '{file_path}' does not exist.")
    except yaml.YAMLError as e:
        print(f"❌ Error loading data from YAML file: {e}")


def get_initial_prompt(agent_name, blog_post_title, blog_post_keywords):
    """
    Retrieve the initial prompt that ChatGPT will use.

    Args:
        :param agent_name: The agent name.
        :param blog_post_title: The string to replace {title} in the "goal" key.
        :param blog_post_keywords: The string to replace {comma_separated_list_of_keywords} in the "goal" key.
        :return: A string representation of the dictionary.
    """
    initial_prompt_dict = extract_data_from_yaml(agent_name)
    output_str = ""

    for key, value in initial_prompt_dict.items():
        # Replace {title} in the "goal" key if provided
        if key == "goal" and blog_post_title:
            value = value.replace("{title}", blog_post_title)

        # Replace {comma_separated_list_of_keywords} in the "keywords" key if provided
        if key == "goal" and blog_post_keywords:
            value = value.replace("{comma_separated_list_of_keywords}", blog_post_keywords)
        
        output_str += f"[{key}]\n{value}\n\n"
    
    return output_str
