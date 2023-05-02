from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """
    Custom tool to inject into 
    langchain Tool class. Informs the langchain
    agent as to what to search for.
    """
    print('TEXXXXXXXXXXXXXXT', text)
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
