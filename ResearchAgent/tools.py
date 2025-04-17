from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data:str , filename : str = "research_results.txt"):
    timestamp  = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_text = f'------Research Results------\nTimeStamp : {timestamp}\n\n Data : {data}\n\n'
    
    with open(filename, "a" , encoding= 'utf-8') as file:
        file.write(formatted_text)
    
    return f"Data saved to {filename}."


save_tool  = Tool(
    name="Save_text_to_file",
    func=save_to_txt,
    description="Saves structured research results to a text file." "\n"
    "use this tool when it is specifically specified",
)

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web using DuckDuckGo. only when you need to search the web for information. "
                  "Use this tool when you need to search the web for information. ",
)

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=100,
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper,
    name="Wikipedia",
    description="Get information from Wikipedia. for the given query.",
)