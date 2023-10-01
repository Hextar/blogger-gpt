import threading
import time
import sys

class Spinner:
    def __init__(self, leading_text):
        self.leading_text = leading_text
        # self.spinner_chars = ["|", "/", "-", "\\"]
        # self.spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.spinner_chars = [
            "🖊️  ", "🖊️  ", "🖊️  ",
            "_🖊️ ", "_🖊️ ", "_🖊️ ",
            "__🖊️", "__🖊️", "__🖊️",
          ]
        self.stop_signal = False

    def start(self):
        index = 0
        while not self.stop_signal:
            char = self.spinner_chars[index]
            sys.stdout.write(f"\r{self.leading_text} {char}")
            sys.stdout.flush()
            index = (index + 1) % len(self.spinner_chars)
            time.sleep(0.1)

    def stop(self):
        self.stop_signal = True
        sys.stdout.write(f"\r{self.leading_text} Done!")
        sys.stdout.flush()

def print_animated_loader(leading_text):
    """
    Display a given leading text followed by an animated loading icon.

    Args:
        leading_text (str): The leading text to display.
    """
    spinner = Spinner(leading_text)
    spinner_thread = threading.Thread(target=spinner.start)
    spinner_thread.start()
    return spinner
