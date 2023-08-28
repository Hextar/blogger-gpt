import asyncio
import re
from utils.elevenlabs import text_to_speech
from utils.openai import chatgpt
from utils.record import record_and_transcribe
from utils.print import print_colored
from utils.config import get_name, get_elevenl_labs_name
from utils.clear import clear_temp_files_on_exit
from utils.terminate import check_termination_condition


async def main():
    while True:
        # Record user's voice and transcript it to text
        user_message = await record_and_transcribe()

        if check_termination_condition(user_message):
            print_colored("LolCat", "KTHXBYE\n\n")
            break  # This will exit the loop immediately

        # Send user's transcript to Chat GPT to receive a response
        response = chatgpt(user_message)

        # Print the current transcript
        print_colored(get_name(), f"{user_message}\n\n")
        print_colored(get_elevenl_labs_name(), f"{response}\n\n")

        # Make sure no to include prepended text that Chat GPT sometime automatically adds
        user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
        
        # Sends to the eleven labs model Chat GPT response and play it
        text_to_speech(user_message_without_generate_image)

clear_temp_files_on_exit()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print_colored("LolCat", "KTHXBYE\n\n")