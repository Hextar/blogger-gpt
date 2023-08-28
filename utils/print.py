from colorama import Fore, Style, init
from utils.config import get_name, get_elevenl_labs_name

init()

def print_colored(agent, text):
    agent_colors = {
        get_name(): Fore.BLUE,
        get_elevenl_labs_name(): Fore.YELLOW,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

