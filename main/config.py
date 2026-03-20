from dotenv import load_dotenv
import os

_APP_LANGS = frozenset({"pt_BR", "en_US", "de_DE", "es_ES"})


def _normalize_app_language(raw: str | None) -> str:
    if not raw:
        return "en_US"
    v = raw.strip()
    return v if v in _APP_LANGS else "en_US"


load_dotenv()  # Load environment variables from .env
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
coinmarketcap_api = os.getenv("COINMARKETCAP_API")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
app_language = _normalize_app_language(os.getenv("APP_LANGUAGE"))


def reload_from_disk():
    """Reload variables from .env (e.g. after saving from the UI)."""
    load_dotenv(override=True)
    global elevenlabs_api_key, groq_api_key, coinmarketcap_api
    global spotify_client_secret, spotify_client_id, app_language
    elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    coinmarketcap_api = os.getenv("COINMARKETCAP_API")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
    app_language = _normalize_app_language(os.getenv("APP_LANGUAGE"))
    import localization

    localization.set_language(app_language)

