import asyncio
import re

from ai.elevenlabs import text_to_speech
from ai.openai import chatgpt
from utils.config import get_silent, get_template
from utils.record import record_and_transcribe
from utils.print import print_colored, print_full_line
from utils.reading import calculate_reading_time
from utils.template import get_user_name, get_chatgpt_name
from utils.terminate import check_termination_condition


async def main():
    print_full_line()
    print(f"💬 Starting template chat: \033[1m{get_template()}\033[0m" + (" [🔇 Silent mode]" if get_silent() else "") + ".\n")
    print(f"👄 You're now talking with: \033[1m{get_chatgpt_name()}\033[0m.\n")

    count = 1

    while True:
        print_full_line()
        print(f"Message: {count}\n")

        # Record user's voice and transcript it to text
        user_message = await record_and_transcribe()

        # Not blocking the UX if the user message is empty
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

        # Print the user transcript
        print_colored(get_user_name(), f"{user_message}\n\n")

        # Send user's transcript to Chat GPT to get a response
        response = chatgpt(user_message)

        # Print ChatGPT transcript
        print_colored(get_chatgpt_name(), f"{response}\n\n")

        # Make sure no to include prepended text that Chat GPT
        # sometime automatically adds
        user_message_cleared = re.sub(
            r'(Response:|Narration:|Image: generate_image:.*|)',
            '',
            response
        ).strip()

        if (not get_silent()):

            # Sends to the eleven labs model Chat GPT response and play it
            text_to_speech(user_message_cleared)

        await asyncio.sleep(calculate_reading_time(user_message_cleared))  # wait for N seconds before next iteration

        count = count + 1

if __name__ == "__main__":
    asyncio.run(main())
