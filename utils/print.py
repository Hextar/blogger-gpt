import time
from colorama import Fore, Style, init

from utils.template import get_user_name, get_chatgpt_name

init()


def print_wave_spinner(text):
    """
    Print a wave-like spinner animation followed by the given text.

    Args:
        text (str): Text to display before the spinner animation.
    """
    for frame in [".·˙·.", "..·˙·", "·..·˙", "˙·..·", "·˙·..", ".·˙·."]:
        print(f"\r{text} {frame}", end='', flush=True)
        time.sleep(0.1)  # Add a small delay between frames
    print("\r" + " " * len(text), end='', flush=True)  # Clear the spinner animation
    print(f"\r{text}", end='', flush=True)  # Print the text without animation


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
