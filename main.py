import asyncio

from ai.openai import chatgpt
from pyperclip import copy
from utils.config import get_debug, get_agent
from utils.io import save_string_to_txt
from utils.print import (
  print_colored,
  print_empty_line,
  print_full_line,
  print_word_count
)
from utils.agent import get_chatgpt_name
from halo import Halo

async def chatgpt_query(blog_post_title = ""):
    print('\n')

    # Start the animated loader
    spinner = Halo(text='🧠 Thinking', spinner='dots')
    spinner.start()

    # Send the blog post request to Chat GPT to get a response
    response = chatgpt(blog_post_title)

    # Print ChatGPT output
    print_empty_line()
    print_colored(get_chatgpt_name(), f"{response}\n\n")
    print_empty_line()

    print_word_count(response)

    # Stop the animated loader
    spinner.stop_and_persist(symbol='✔', text='Loading Complete!')

    save_string_to_txt(response, blog_post_title)

    # Copy ChatGPT output to clipboard
    copy(response)
    print("📋 GhatGPT output automatically copied to clipboard")


async def main():
    print_full_line()
    if get_debug():
        print(f"🔧 Debug mode is enabled.\n")
    print(f"💬 Starting chat with agent: \033[1m{get_agent()}\033[0m.\n")

    while True:
        print_full_line()
        user_message = input(f"Blog post title: ")

        # Not blocking the UX if the user message is empty
        if not (user_message):
            print(f"🔧 Please enter a valid title.\n")
            continue # skip to the next loop

        await chatgpt_query(user_message)

        print_full_line()


if __name__ == "__main__":
    asyncio.run(main())
