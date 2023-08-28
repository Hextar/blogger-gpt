import re
from utils.elevenlabs import text_to_speech
from utils.openai import chatgpt, record_and_transcribe
from utils.print import print_colored
from utils.config import get_name, get_elevenl_labs_name
from utils.clear import clear_temp_files_on_exit

while True:
    # Record user's voice and transcript it to text
    user_message = record_and_transcribe()

    # Send user's transcript to Chat GPT to receive a response
    response = chatgpt(user_message)

    # Print the current transcript
    print_colored(get_name(), f"{user_message}\n\n")
    print_colored(get_elevenl_labs_name(), f"{response}\n\n")

    # Make sure no to include prepended text that Chat GPT sometime automatically adds
    user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()

    # Sends to the eleven labs model Chat GPT response and play it
    text_to_speech(user_message_without_generate_image)

# When closing the process gracefully will delete all temp files
clear_temp_files_on_exit()

