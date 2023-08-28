import openai
from utils.template import get_prompt
from utils.config import get_template, get_open_ai_api_key, get_open_ai_model

template = get_prompt(get_template())
conversation = []


def chatgpt(user_input, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    """
    Send a text message to chatgpt and await for a text answer
    """
    openai.api_key = get_open_ai_api_key()
    conversation.append({"role": "user", "content": user_input})
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": template}]
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
