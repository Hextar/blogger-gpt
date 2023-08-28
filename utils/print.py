import time
from colorama import Fore, Style, init
from utils.config import get_name, get_elevenl_labs_name

init()

# Define a rotating spinner animation
SPINNER_FRAMES = [".·˙·.", "..·˙·", "·..·˙", "˙·..·", "·˙·..", ".·˙·."]

"""
Print a wave-like spinner animation followed by the given text.

Args:
    text (str): Text to display before the spinner animation.
"""
def print_wave_spinner(text):
    for frame in SPINNER_FRAMES:
        print(f"\r{text} {frame}", end='', flush=True)
        time.sleep(0.1)  # Add a small delay between frames
    print("\r" + " " * len(text), end='', flush=True)  # Clear the spinner animation
    print(f"\r{text}", end='', flush=True)  # Print the text without animation

"""
Print some colored message with an agent followed by the given text

Args:
    agent (str): Specify who's talking
    text (str): What the agent is saying
"""
def print_colored(agent, text):
    agent_colors = {
        "LolCat": Fore.MAGENTA,
        get_name(): Fore.BLUE,
        get_elevenl_labs_name(): Fore.YELLOW,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

# Fix for potential buffering issue: force flushing of printed characters
def flush_print():
    print("", end='', flush=True)