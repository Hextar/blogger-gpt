import asyncio
import re

from ai.elevenlabs import text_to_speech
from ai.openai import chatgpt
from utils.config import get_template
from utils.record import record_and_transcribe
from utils.print import print_colored
from utils.template import get_user_name, get_chatgpt_name
from utils.terminate import check_termination_condition


async def main():
    print(f"Starting template {get_template()}\n\n")

    while True:
        # Record user's voice and transcript it to text
        user_message = await record_and_transcribe()

        # Not blocking the UX if the user message being empty
        if (user_message is None):
            print_colored(
                get_user_name(),
                "I didn't got your last phrase, can you please repeat?\n\n"
            )
            continue

        # If a terminal condition is encountered exit immediately
        if check_termination_condition(user_message):
            print_colored("LolCat", "KTHXBYE\n\n")
            break  # This will exit the loop immediately

        # Send user's transcript to Chat GPT to receive a response
        response = chatgpt(user_message)

        # Print the current transcript
        print_colored(get_user_name(), f"{user_message}\n\n")
        print_colored(get_chatgpt_name(), f"{response}\n\n")

        # Make sure no to include prepended text that Chat GPT
        # sometime automatically adds
        user_message_without_generate_image = re.sub(
            r'(Response:|Narration:|Image: generate_image:.*|)',
            '',
            response
        ).strip()

        # Sends to the eleven labs model Chat GPT response and play it
        text_to_speech(user_message_without_generate_image)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Pretty print reacting to a SIGINT
        print_colored("LolCat", "KTHXBYE\n\n")
