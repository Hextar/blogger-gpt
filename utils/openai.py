# OUTDATED, converting everything to use utils/langchain.py now

import openai

from .config import get_open_ai_api_key, get_open_ai_model
from .print import print_animated_loader, print_empty_line


conversation = []


def chat_with_gpt(
        current_prompt,
        temperature=0.9,
        frequency_penalty=0.2,
        presence_penalty=0
    ):
    """
    Send a text message to ChatGPT and await a text answer.
    """
    conversation.append({"role": "user", "content": current_prompt})
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": current_prompt}]
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


def query_gpt_for_blog(initial_prompt):
    animated_loader = print_animated_loader("📜 Writing")

    try:
        # Setup OpenAI API key
        openai.api_key = get_open_ai_api_key()

        response = chat_with_gpt(initial_prompt)

        animated_loader.stop()
        print_empty_line()

        return response
    except Exception as e:
        print(f"❌ An error occurred: {e}")
