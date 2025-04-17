from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from config import groq_api_key 



groq_provider = GroqProvider(
    api_key= groq_api_key
)

model = GroqModel(
    model_name= 'llama-3.3-70b-versatile',
    provider=groq_provider,

)