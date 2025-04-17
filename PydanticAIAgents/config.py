from dotenv import load_dotenv
import os
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

logfire_token = os.getenv('LOGFIRE_TOKEN')

print(groq_api_key ,"\n",logfire_token )