from colorama import Fore, Style, init
import re
import shutil

from utils.template import get_user_name, get_chatgpt_name

init()


def print_full_line(character="-"):
    """
    Print a full line in the terminal with the specified character.

    Args:
        character (str, optional): The character to use for the line. Default is "-".
    """
    terminal_width, _ = shutil.get_terminal_size()
    line = character * terminal_width
    print(line)
    print()


def print_colored(agent, text):
    """
    Print some colored message with an agent followed by the given text

    Args:
        agent (str): Specify who's talking
        text (str): What the agent is saying
    """
    agent_colors = {
        "LolCat": Fore.MAGENTA,
        get_user_name(): Fore.BLUE,
        get_chatgpt_name(): Fore.GREEN,
    }

    color = agent_colors.get(agent, "")

    # Make sure not to include prepended text that Chat GPT
    # sometime automatically adds
    cleared_text = re.sub(
        r'(Response:|Narration:|Image: generate_image:.*|get_user_name():|get_chatgpt_name():)',
        '',
        text
    ).strip()

    print(color + f"{agent}: {cleared_text}" + Style.RESET_ALL, end="")


def flush_print():
    """
    Fix for potential buffering issue: force flushing of printed characters
    """
    print("", end='', flush=True)
