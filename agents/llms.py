from llama_index.llms.groq import Groq
from llama_index.llms.ollama import Ollama

from main.config import groq_api_key

llm_ollama = Ollama(model="llama3", request_timeout=300.0)
llm_groq = Groq(model="llama-3.3-70b-versatile", api_key=groq_api_key)