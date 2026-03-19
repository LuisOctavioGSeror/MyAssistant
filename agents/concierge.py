from agents.agent_controller import create_agent
from agents.tools import *
from agents.llms import llm_groq

tools = [text_to_speech_tool, discover_current_date_and_time_tool]

host_agent = create_agent(llm=llm_groq, tools=tools, context="This Agent function is to greet the person and be a nice host")