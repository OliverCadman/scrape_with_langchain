from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

import os

if os.path.exists("env.py"):
    import env


if __name__ == '__main__':
    print('Hello Langchain!')

    summary_template = """
        Given the information {information} about a person, I want you to create:

        1. A short summary.
        2. Two interesting things about them.
    """

    summary_template_prompt = PromptTemplate(input_variables=['information'], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=os.environ.get('OPENAI_API_KEY'))

    chain = LLMChain(llm=llm, prompt=summary_template_prompt)

    linkedin_url = linkedin_lookup_agent(name="Oliver Cadman Xander Talent")
    linkedin_profile = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    print(chain.run(information=linkedin_profile))
    