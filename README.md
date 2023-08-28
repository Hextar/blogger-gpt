# chat-gpt-voice-to-voice
Talk To ChatGPT using a voice-to-voice approach .

# Requirements
Python 3 was used to develop this project.

# Install
1. Install ffmpeg. On mac use 'brew install ffmpeg'. On linux/windows check https://ffmpeg.org/
2. Run `sudo apt install python3-pyaudio`
3. Run `pip install -r requirements.txt`
4. Duplicate the `.env-example` file and rename it `.env`
5. Fill in your api keys within `.env`
6. Run `python main.py`

# Settings
Before running this implementation you need to add some configs creating a `.env` file.\

Tip: duplicate the `.env-example` file and rename it.

#### LANG
Can be used to specify ELEVEN_LABS_ACCENTS (Currently not being used).

#### TEMPLATE
Choose the STS template, discover more [here](/templates/TEMPLATES.md).

#### OPEN_AI_API_KEY
Your Open AI API key (mandatory).

#### OPEN_AI_MODEL
The Open AI model currently in use.
No need to change anything unless you want to experiment with different models.

Examples:
- gpt-3.5-turbo-0613
- gpt-3.5-turbo-16k
- gpt-4
- text-davinci-003

#### ELEVEN_LABS_API_KEY
Your Eleven labs API key (mandatory).

#### ELEVEN_LABS_MODEL
The Eleven labs model currently in use;

You can choose between:
- eleven_monolingual_v1
- eleven_monolingual_v2

# TODO
- improve the record algorithm to ask the user to press Enter when the recording concluded
- implement chat with memory, storing locally the chat transcript to send it to future chats`