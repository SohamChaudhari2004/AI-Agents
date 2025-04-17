from pydantic_ai import Agent
from utils.groq_model import model, groq_provider
import logfire
from config import logfire_token




logfire_config = logfire.configure(
    token= logfire_token
)

agent = Agent(
    model=model,
    instrument=True
)

import asyncio 

async def main():
  result = await agent.run("hello")
  while True:
    print(f"\n{result.data}")
    
    user_input = input(" \n > ")
    
    result = await agent.run(user_input,
                              message_history=result.new_messages(),
                              )
      

asyncio.run(main())