These directory contains the agents you can choose from to let Chat GPT behave as different agents.

# Choose a different agent

You can choose a different agent by changing the AGENT value
in your `.env` file.

Be sure to match the name of an existing file within this directory.

# Create a new agent

To create a new agent you should use the following
yaml keys.

### chatgpt_name

Name that will be used for the bot

### user_name

Name that the bot will refer the user to

### eleven_labs_voice

Voice name used by 11-labs speech synthesis
(check it here: elevenlabs.io/speech-synthesis)

### prompt

ChatGPT prompt

Tip: remember that prepending the prompt with the `|` symbol allow you to
specify a multiline description which will be easier to read.
