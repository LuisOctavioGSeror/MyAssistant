from agents.agent_controller import create_agent
from agents.tools import *
from agents.llms import llm_groq

tools = [send_email_tool, text_to_speech_tool]

email_sender_agent = create_agent(llm=llm_groq, context="This Agent function is to send emails", tools=tools)