from langchain.prompts import load_prompt, PromptTemplate 
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.memory.chat_message_histories import ChatMessageHistory
from langchain.schema import AIMessage

from .config import get_open_ai_api_key, get_open_ai_model
from .print import print_animated_loader, print_empty_line


def query_gpt_for_blog(filename, blog_post_title, blog_post_keywords, word_count=1000):
  animated_loader = print_animated_loader("📜 Writing")

  try:
    # Init ---------------------------------

    ##### Create the LLM model
    llm = ChatOpenAI(
      model_name=get_open_ai_model(),
      openai_api_key=get_open_ai_api_key(),
      temperature=0.9,
    )

    ##### Web Search Tool
    search = DuckDuckGoSearchRun()
    search_tool = Tool(
        name="Web Search",
        func=search.run,
        description="A useful tool for searching the Internet to find information on world events, issues, etc. Worth using for general topics. Use precise questions.",
    )

    ##### Wikipedia Tool
    wikipedia = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="A useful tool for searching the Internet to find information on world events, issues, etc. Worth using for general topics. Use precise questions.",
    )

    # STEP 1: Plan ---------------------------------

    #### Initialize prompt templates
    plan_prompt = load_prompt(filename).format(
      comma_separated_list_of_keywords=blog_post_keywords,
      title=blog_post_title,
      word_count=word_count,
    )

    writing_prompt = PromptTemplate(
        input_variables=[],
        template="""

        Start writing the blog post, using the following tools to enrich the
        content, remember to cite your best findings as sources:
        - Wikipedia
        - Web Search

        REMEMBER: You don't have access to information beyond September 2021.
        Use the tools to find current information.
        """,
    )

    #### Prepare Conversational chain
    conversational = ConversationChain(llm=llm)

    #### Instruct about the plan 
    plan_result = conversational.run(plan_prompt)

    # Step 2: Write blog post ---------------------------------

    #### Chat history
    chat_history = ChatMessageHistory([
        AIMessage(content=plan_result),
    ])

    #### Initialize Agent
    agent = initialize_agent(
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        tools=[search_tool, wikipedia_tool],
        verbose=True,
        max_iterations=12
    )

    print('================================')

    #### Agent execution
    response = agent({
      "input": writing_prompt,
      "chat_history": chat_history,
    })

    print('================================')
    print(response["output"])
  
    animated_loader.stop()
    print_empty_line()
    
    return response
  except Exception as e:
    print(f"❌ An error occurred while writing: {e}")
    exit()
