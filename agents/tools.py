from llama_index.core.tools import FunctionTool
from features.email_handler import send_email, get_list_of_emails
from features.discover_current_date_and_time import discover_current_time
from features.note import take_a_note, delete_note, access_note, discover_notes_names
from features.spotify import play_a_song
from features.discover_cryptocoins_quotes import get_crypto_values
from speak import convert_text_to_speech

get_list_of_emails_tool = FunctionTool.from_defaults(
    get_list_of_emails,
    description="this function returns a list of emails, each item of the list is an email of a person"
)

get_crypto_values_tool = FunctionTool.from_defaults(
    get_crypto_values,
    description="This function discovers information about cryptocurrencies like BTC (Bitcoin) and ETH (Ethereum)"
)

play_a_song_from_spotify_tool = FunctionTool.from_defaults(
    play_a_song,
    description="this function plays a specific song from Spotify"
)

note_something_tool = FunctionTool.from_defaults(
    take_a_note,
    description="this function creates a new .txt file with a user-chosen name and note, or appends to the file if it already exists"
)

delete_a_note_tool = FunctionTool.from_defaults(
    delete_note,
    description="this function deletes the note chosen by the user"
)

discover_notes_names_tool = FunctionTool.from_defaults(
    discover_notes_names,
    description="This function returns the names saved in notes"
)

access_a_note_tool = FunctionTool.from_defaults(
    access_note,
    description="this function accesses a specific note and returns its content"
)

send_email_tool = FunctionTool.from_defaults(
    send_email,
    description="this function sends emails using the email list in the path data/e-mails.txt"
)

text_to_speech_tool = FunctionTool.from_defaults(
    convert_text_to_speech,
    description="this function converts text to audio"
)

discover_current_date_and_time_tool = FunctionTool.from_defaults(
    discover_current_time,
    description="this function discovers the current date and time and returns a datetime object"
)
