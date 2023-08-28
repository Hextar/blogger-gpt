# Do not use punctuation here
TERMINAL_CONDITIONS = [
    "Computer end program",
    "Computer arch",
    "Goodbye",
    "Exit simulation",
    "Interrupt simulation"
]

"""
Check if the current user message contains a termination condition
"""
def check_termination_condition(user_message):
    return any(terminal_condition.lower() in user_message.lower() for terminal_condition in TERMINAL_CONDITIONS)
