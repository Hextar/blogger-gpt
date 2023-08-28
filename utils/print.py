import time
from colorama import Fore, Style, init

from utils.config import get_template
from utils.template import get_user_name, get_chatgpt_name

init()


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
        get_chatgpt_name(): Fore.YELLOW,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")


def flush_print():
    """
    Fix for potential buffering issue: force flushing of printed characters
    """
    print("", end='', flush=True)
