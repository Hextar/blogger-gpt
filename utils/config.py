import os
from dotenv import load_dotenv

load_dotenv()

def get_template():
  return os.getenv('TEMPLATE')

def get_open_ai_api_key():
  return os.getenv('OPEN_AI_API_KEY')

def get_open_ai_model():
  return os.getenv('OPEN_AI_MODEL')

def get_eleven_labs_api_key():
  return os.getenv('ELEVEN_LABS_API_KEY')

def get_eleven_labs_model():
  return os.getenv('ELEVEN_LABS_MODEL')
