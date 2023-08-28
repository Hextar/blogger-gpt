import re
from utils.elevenlabs import text_to_speech
from utils.openai import chatgpt, record_and_transcribe
from utils.print import print_colored
from utils.config import get_name, get_elevenl_labs_name
from utils.clear import clear_temp_files_on_exit

while True:
    user_message = record_and_transcribe()
    response = chatgpt(user_message)
    print_colored(get_name(), f"{user_message}\n\n")
    print_colored(get_elevenl_labs_name(), f"{response}\n\n")
    # user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
    text_to_speech(response.strip())

clear_temp_files_on_exit()

