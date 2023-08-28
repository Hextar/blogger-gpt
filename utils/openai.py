import asyncio
import openai
import os
import sounddevice as sd
import soundfile as sf
import keyboard
from utils.print import print_wave_spinner
from utils.config import (
  get_prompt,
  get_open_ai_api_key,
  get_open_ai_model,
  get_filename,
)

template = get_prompt('templates/therapist.txt')
conversation = []  

# Call the record function to record the user voice, waits for the
# recording to complete and then perform the recording transcript
# which will be then returned
# async def record_and_transcribe():
#     recording_done = asyncio.Event()  # Create an event for signaling recording done
#     recording_result = await asyncio.gather(record_voice(recording_done))
#     print(recording_result[0])

#     with open(get_filename(), "rb") as file:
#         openai.api_key = get_open_ai_api_key()
#         result = openai.Audio.transcribe("whisper-1", file)

#     transcription = result['text']

#     print('[DEBUG] Transcription complete.', transcription)

#     return transcription

# Send a text message to chatgpt and await for a text answer
def chatgpt(user_input, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    openai.api_key = get_open_ai_api_key()
    conversation.append({"role": "user","content": user_input})
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": template}]
    messages_input.insert(0, prompt[0])
    completion = openai.ChatCompletion.create(
        model=get_open_ai_model(),
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messages_input)
    chat_response = completion['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": chat_response})
    return chat_response

