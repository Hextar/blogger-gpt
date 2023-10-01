from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from .config import get_open_ai_api_key, get_open_ai_model
from .print import print_animated_loader, print_empty_line


def query_gpt_for_blog(initial_prompt, blog_post_title, blog_post_keywords, word_count=1000):
  animated_loader = print_animated_loader("📜 Writing")

  try:
    prompt = PromptTemplate(
        input_variables=[
          "comma_separated_list_of_keywords",
          "title",
          "word_count"
        ],
        template=initial_prompt,
    )

    llm = ChatOpenAI(
      model_name=get_open_ai_model(),
      openai_api_key=get_open_ai_api_key(),
      temperature=0.9,
    )
    llmchain = LLMChain(llm=llm, prompt=prompt)
    response =  llmchain.run({
      "comma_separated_list_of_keywords": blog_post_keywords,
      "title": blog_post_title,
      "word_count": word_count
    })
  
    animated_loader.stop()
    print_empty_line()
    
    return response
  except Exception as e:
    print(f"❌ An error occurred while writing: {e}")
