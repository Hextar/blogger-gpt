import yaml
from simple_term_menu import TerminalMenu
import os


def load_agents(directory="agents"):
    """
    Load menu options with filenames from YAML files in the specified directory.

    Returns:
        list: List of menu options, each containing a dictionary with "label" and "filename" keys, sorted by "label".
    """
    menu_options = []

    # Check if the directory exists
    if os.path.exists(directory) and os.path.isdir(directory):
        # Loop through files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                # Create a dictionary for each menu option
                option_dict = {
                    "label": os.path.splitext(filename)[0].capitalize(),
                    "filename": filename,
                }
                menu_options.append(option_dict)

    # Sort the list of dictionaries by the "label" key
    sorted_menu_options = sorted(menu_options, key=lambda x: x["label"])

    return sorted_menu_options


def show_menu():
    """
    Display a menu with selectable options using inquirer.

    Returns:
        str: The selected menu option.
    """
    menu_entries = load_agents()
    terminal_menu = TerminalMenu(
        menu_entries=[agent["label"] for agent in menu_entries],
        title="🕵️  Please select an Agent:",
        menu_cursor="👉 ",
        cycle_cursor=True,
    )
    menu_entry_index = terminal_menu.show()
    return menu_entries[menu_entry_index]["filename"]


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


def get_initial_prompt(agent_name):
    """
    Retrieve the initial prompt that ChatGPT will use.

    Args:
        :param agent_name: The agent name.
        :return: A string representation of the dictionary.
    """
    initial_prompt_dict = extract_data_from_yaml(agent_name)
    output_str = ""

    for key, value in initial_prompt_dict.items():
        output_str += f"[{key}]\n{value}\n\n"
    
    return output_str
