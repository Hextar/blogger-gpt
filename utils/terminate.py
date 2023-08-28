# Do not use punctuation here
TERMINAL_CONDITIONS = [
    "Computer and program",
    "Computer end program",
    "Computer arch",
    "Goodbye",
    "Exit simulation",
    "Interrupt simulation"
]

def check_termination_condition(user_message):
    """
    Check if the current user message contains a termination condition
    """
    try:
        return any(terminal_condition.lower() in user_message.lower() for terminal_condition in TERMINAL_CONDITIONS)
    except AttributeError:
        return False