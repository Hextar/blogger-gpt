import os
from dotenv import load_dotenv

load_dotenv()

def get_name():
  return os.getenv('MY_NAME')

def get_lang():
  return os.getenv('LANG')

def get_prompt(filepath):
  with open(filepath, 'r', encoding='utf-8') as infile:
      return infile.read()

def get_open_ai_api_key():
  return os.getenv('OPEN_AI_API_KEY')

def get_open_ai_model():
  return os.getenv('OPEN_AI_MODEL')

def get_elevenl_labs_api_key():
  return os.getenv('ELEVEN_LABS_API_KEY')

def get_elevenl_labs_name():
  return os.getenv('ELEVEN_LABS_NAME')

def get_elevenl_labs_model():
  return os.getenv('ELEVEN_LABS_MODEL')
