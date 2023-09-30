# blogger-gpt

Use Chat GPT to write blog posts.

# Requirements

Python 3 was used to develop this project.

# Install

1. Run `pip install -r requirements.txt`
4. Duplicate the `.env-example` file and rename it `.env`
5. Fill in your api keys within `.env`
6. Run `python main.py`

# Settings

Before running this implementation you need to add some configs creating a `.env` file.\

Tip: duplicate the `.env-example` file and rename it.

#### AGENT

Choose the desired agent, discover more [here](/agents/AGENTS.md).

#### DEBUG

Use basic python text to speech step to spare eleven labs quotas.


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

# TODO

- chain gpt responses to improve the blog post quality