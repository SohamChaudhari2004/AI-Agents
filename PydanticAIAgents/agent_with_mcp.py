import asyncio 
from pydantic_ai import Agent
from utils.groq_model import model
import logfire
from config import logfire_token
# from utils.mcp_server import fetch_server
from pydantic_ai.mcp import MCPServerStdio




fetch_server = MCPServerStdio(
    'python',  ["-m", "mcp_server_fetch"]
)


logfire_config = logfire.configure(
    token= logfire_token
)

agent = Agent(
    model=model,
    instrument=True,
    mcp_servers=[fetch_server],
)


async def main():
    # Ensure MCP servers are running
    async with agent.run_mcp_servers():
        result = await agent.run("hello")
        while True:
            print(f"\n{result.data}")
            user_input = input("\n> ")
            result = await agent.run(
                user_input,
                message_history=result.new_messages(),
            )

      

asyncio.run(main())