# chat-gpt-voice-to-voice
Talk To ChatGPT using a voice-to-voice approach 

# Requirements
Python 3 is used for this project

# Install
1. Install ffmpeg. On mac use 'brew install ffmpeg'. On linux/windows check https://ffmpeg.org/
2. Run `sudo apt install python3-pyaudio`
3. Run `pip install -r requirements.txt`
4. Duplicate the `.env-example` file and rename it `.env`
5. Fill in your api keys within `.env`
6. Run `python main.py`

# Customize
You're going to chat with chat-gpt using the pre-made template found within
the directory `templates`.

Change it as the eleven labs voice (within `.env`) at your pleasure and re run the
`main.py` file.

# TODO
- improve the record algorithm to ask the user to pess Enter when the recording concluded
- improve the record algorithm to automatically detect when the record has finished
- improve the template+voice logic to allow defining an eleven labs voice and the user name
  directly from the template file
- implemente chat with memory, storing locally the chat transcript to send it to future chats`