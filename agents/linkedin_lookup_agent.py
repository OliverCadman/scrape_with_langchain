from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url

import os
if os.path.exists('env.py'):
    import env


def lookup(name: str) -> str:
    """
    A langchain Chain method
    
    Initializes a langchain Agent, which will
    interact with the SerpAPI in order to get information
    following a given prompt. Ultimately, the agent will return
    a LinkedIn URL.
    """
    print("NAAAAAAAAAAME", name)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=os.environ.get('OPENAI_API_KEY'))
    template = """
        Given the full name {name_of_person}, I want you to get
        me a link to their LinkedIn profile page. Your answer
        should only contain a URL.
    """

    tools_for_agent = [
        Tool(name="Crawl google for LinkedIn profile page.",
             func=get_profile_url,
             description="Useful when you need to get the LinkedIn profile URL.")
             ]
    
    agent = initialize_agent(tools=tools_for_agent,
                             llm=llm, verbose=True,
                             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    
    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person'])
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url

