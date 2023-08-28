from elevenlabs import generate, play
import os
from utils.config import get_elevenl_labs_api_key

from utils.config import (
  get_prompt,
  get_elevenl_labs_api_key,
  get_elevenl_labs_name,
  get_elevenl_labs_model
)
 
def text_to_speech(text):
  audio = generate(
    api_key=get_elevenl_labs_api_key(),
    text=text,
    voice=get_elevenl_labs_name(),
    model=get_elevenl_labs_model()
  )

  play(audio)