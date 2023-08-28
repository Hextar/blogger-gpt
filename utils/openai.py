import openai
import os
import sounddevice as sd
import soundfile as sf
import keyboard
from utils.config import (
  get_prompt,
  get_open_ai_api_key,
  get_open_ai_model
)

template = get_prompt('templates/therapist.txt')
conversation = []  

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

def record_and_transcribe(duration=12, fs=44100):
    print('Recording...')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print('Recording complete.')
    filename = 'temp/myrecording.wav'
    sf.write(filename, myrecording, fs)
    with open(filename, "rb") as file:
        openai.api_key = get_open_ai_api_key()
        result = openai.Audio.transcribe("whisper-1", file)
    transcription = result['text']
    return transcription