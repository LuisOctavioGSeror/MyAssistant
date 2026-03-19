from textwrap import dedent

from agents.agent_controller import create_agent
from agents.tools import *
from agents.llms import llm_groq

tools = [text_to_speech_tool, discover_current_date_and_time_tool,get_list_of_emails_tool,
         send_email_tool, note_something_tool, delete_a_note_tool,
         access_a_note_tool, discover_notes_names_tool, play_a_song_from_spotify_tool, get_crypto_values_tool]

general_agent = create_agent(llm=llm_groq, tools=tools, context=dedent(\
    """This Agent role is to perform only the instructions asked, that means that it should only do what is 
    asked nothing more nothing less"""), max_iterations=20)
