from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
coinmarketcap_api = os.getenv("COINMARKETCAP_API")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")


def reload_from_disk():
    """Reload variables from .env (e.g. after saving from the UI)."""
    load_dotenv(override=True)
    global elevenlabs_api_key, groq_api_key, coinmarketcap_api
    global spotify_client_secret, spotify_client_id
    elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    coinmarketcap_api = os.getenv("COINMARKETCAP_API")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")

