from elevenlabs import generate, play

from utils.template import get_eleven_labs_voice
from utils.config import get_eleven_labs_api_key, get_eleven_labs_model


def text_to_speech(text):
    audio = generate(
        api_key=get_eleven_labs_api_key(),
        text=text,
        voice=get_eleven_labs_voice(),
        model=get_eleven_labs_model()
    )

    play(audio)
