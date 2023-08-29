import asyncio

from ai.debug import debug_text_to_speech
from ai.elevenlabs import text_to_speech
from ai.openai import chatgpt
from utils.config import get_debug, get_template
from utils.record import record_and_transcribe
from utils.print import print_colored, print_full_line
from utils.reading import calculate_reading_time
from utils.template import (
    get_user_name,
    get_chatgpt_name,
    get_chat_gpt_goes_first,
    get_chatgpt_pronoun
)
from utils.terminate import check_termination_condition


async def user_turn():
    # Record user's voice and transcript it to text
    user_message = await record_and_transcribe()

    # Not blocking the UX if the user message is empty
    if (user_message is None):
        print_colored(
            get_user_name(),
            "I didn't got your last phrase, can you please repeat?\n\n"
        )
        return -1
        
    if check_termination_condition(user_message):
        print_colored("LolCat", "KTHXBYE\n\n")
        return -2

    # Print the user transcript
    print_colored(get_user_name(), f"{user_message}\n\n")

    return user_message


async def chatgpt_turn(user_message = ""):
    # Send user's transcript to Chat GPT to get a response
    response = chatgpt(user_message)

    # Print ChatGPT transcript
    print_colored(get_chatgpt_name(), f"{response}\n\n")

    if (get_debug()):
        # Uses pyttsx3 basic tts to play it
        debug_text_to_speech(response)
    else:
        # Sends to the eleven labs model Chat GPT response and play it
        text_to_speech(response)

    # Wait for N seconds to give the user time to read
    await asyncio.sleep(calculate_reading_time(response))

    return response


async def main():
    print_full_line()
    if get_debug():
        print(f"🔧 Debug mode is enabled.\n")
    print(f"💬 Starting template chat: \033[1m{get_template()}\033[0m.\n")
    print(f"👄 You're now talking with: \033[1m{get_chatgpt_name()}\033[0m.\n")
    if get_chat_gpt_goes_first():
        print(f"   {get_chatgpt_pronoun()} will speak first.\n")
    else:
        print("   You're starting the conversation.\n")

    count = 1

    while True:
        print_full_line()
        print(f"Message: {count}\n")

        if (get_chat_gpt_goes_first()):
            await chatgpt_turn()

        # Record user's voice and transcript it to text
        user_message = await user_turn()

        # Not blocking the UX if the user message is empty
        if (user_message == -1):
            continue # skip to the next loop
        elif (user_message == -1):
            break  # This will exit the loop immediately

        if (not get_chat_gpt_goes_first()):
            await chatgpt_turn(user_message)

        count = count + 1

if __name__ == "__main__":
    asyncio.run(main())
