These directory contains the templates you can choose from to try this
speech-to-speech implementation.

# Choose a different template
You can choose a different template by changing the TEMPLATE value
in your `.env` file.

Be sure to match the name of an existing file within this directory.

# Create a new template
To create a new template you should use the following
yaml keys.

#### chatgpt_name
Name that will be used for the bot

#### user_name
Name that the bot will refer the user to

#### eleven_labs_voice
Voice name used by 11-labs speech synthesis
(check it here: elevenlabs.io/speech-synthesis)

#### prompt
Chat GPT prompt

Tip: remember that prepending the prompt with the `|` symbol allow you to
specify a multiline description which will be easier to read.