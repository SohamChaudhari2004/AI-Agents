from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
import os
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers  import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain.memory import ConversationBufferMemory
from tools import search_tool , wiki_tool,save_tool


tools = [   
    search_tool, wiki_tool, save_tool
]

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str] = Field(default_factory=list)
    tools_used: list[str] = Field(default_factory=list)


groq_api  = os.getenv("GROQ_API")
mistral_api = os.getenv("MISTRAL_API_KEY")



llm = ChatGroq(
    api_key= groq_api,
    model =  'llama-3.2-90b-vision-preview'
)


parser = PydanticOutputParser(pydantic_object=ResearchResponse)


prompt = ChatPromptTemplate.from_messages(
     [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            provide brief summary of the topic and provide sources and a little explanation.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions() )

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

query = input("what can i help you research ? ")
# agent_memory = ConversationBufferMemory(
#     memory_key="chat_history",
#     return_messages=True,
#     input_key= query,
# )


agent_exec = AgentExecutor(
    agent = agent,
    tools = tools,
    verbose = True,
    # memory=agent_memory,
)


raw_res = agent_exec.invoke(
    {
        "query": query,
       
    }
)

structured_res = parser.parse(raw_res["output"])
try :
    print(structured_res)   
except Exception as e:
    print(f"Error parsing response: {e} , raw response: {raw_res['output']}")

