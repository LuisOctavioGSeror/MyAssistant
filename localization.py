"""
UI and message translations. Locale codes: pt_BR, en_US, de_DE, es_ES.
"""
from __future__ import annotations

import os

VALID_LOCALES = frozenset({"pt_BR", "en_US", "de_DE", "es_ES"})
DEFAULT_LOCALE = "en_US"

# Google Speech Recognition language codes
SPEECH_LANGUAGE_CODE: dict[str, str] = {
    "pt_BR": "pt-BR",
    "en_US": "en-US",
    "de_DE": "de-DE",
    "es_ES": "es-ES",
}

_current: str = DEFAULT_LOCALE

STRINGS: dict[str, dict[str, str]] = {
    "en_US": {
        "tab_assistant": "Assistant",
        "tab_configurations": "Configurations",
        "run_voice_recognition": "Run voice recognition",
        "voice_already_running": "Voice recognition is already running.",
        "starting_voice_recognition": "Starting voice recognition…",
        "recognized_text": "Recognized text",
        "agent_response": "Agent response",
        "error_occurred": "An error occurred",
        "settings_title": "Settings",
        "settings_subtitle": "Your keys are stored only in this project's <b>.env</b> file "
        "(do not commit it). Optionally show or hide values below.",
        "language_group": "Language",
        "language_label": "Interface and speech",
        "api_keys_group": "API keys",
        "paste_key_placeholder": "Paste your key here",
        "show_keys": "Show keys",
        "save_env": "Save to .env",
        "saved_dialog_title": "Saved",
        "saved_dialog_body": "Settings written to <b>.env</b>. "
        "To use a new Groq key, please <b>quit and restart</b> the app.",
        "error_dialog_title": "Error",
        "error_dialog_save": "Could not save",
        "field_elevenlabs": "ElevenLabs",
        "hint_elevenlabs": "Text-to-speech",
        "field_groq": "Groq (LLM)",
        "hint_groq": "Assistant LLM backend",
        "field_coinmarketcap": "CoinMarketCap",
        "hint_coinmarketcap": "Crypto quotes",
        "field_spotify_id": "Spotify — Client ID",
        "hint_spotify_id": "Spotify integration",
        "field_spotify_secret": "Spotify — Client secret",
        "hint_spotify_secret": "Spotify integration",
        "speak_now": "Speak now",
        "err_no_speech": "No speech detected within the time limit.",
        "err_unknown_speech": "Could not understand the speech.",
        "err_service": "Speech recognition service error: {error}",
        "audio_viz_disabled": "Audio visualization disabled",
    },
    "pt_BR": {
        "tab_assistant": "Assistente",
        "tab_configurations": "Configurações",
        "run_voice_recognition": "Reconhecimento de voz",
        "voice_already_running": "O reconhecimento de voz já está em execução.",
        "starting_voice_recognition": "Iniciando reconhecimento de voz…",
        "recognized_text": "Texto reconhecido",
        "agent_response": "Resposta do agente",
        "error_occurred": "Ocorreu um erro",
        "settings_title": "Configurações",
        "settings_subtitle": "Suas chaves ficam apenas no arquivo <b>.env</b> deste projeto "
        "(não faça commit). Opcional: mostrar ou ocultar os valores abaixo.",
        "language_group": "Idioma",
        "language_label": "Interface e fala",
        "api_keys_group": "Chaves de API",
        "paste_key_placeholder": "Cole sua chave aqui",
        "show_keys": "Mostrar chaves",
        "save_env": "Salvar no .env",
        "saved_dialog_title": "Salvo",
        "saved_dialog_body": "Configurações gravadas em <b>.env</b>. "
        "Para usar uma nova chave Groq, <b>feche e abra</b> o aplicativo.",
        "error_dialog_title": "Erro",
        "error_dialog_save": "Não foi possível salvar",
        "field_elevenlabs": "ElevenLabs",
        "hint_elevenlabs": "Texto para voz",
        "field_groq": "Groq (LLM)",
        "hint_groq": "Motor do assistente (LLM)",
        "field_coinmarketcap": "CoinMarketCap",
        "hint_coinmarketcap": "Cotações de cripto",
        "field_spotify_id": "Spotify — ID do cliente",
        "hint_spotify_id": "Integração Spotify",
        "field_spotify_secret": "Spotify — Segredo do cliente",
        "hint_spotify_secret": "Integração Spotify",
        "speak_now": "Fale agora",
        "err_no_speech": "Nenhuma fala detectada no tempo limite.",
        "err_unknown_speech": "Não foi possível entender a fala.",
        "err_service": "Erro no serviço de reconhecimento de voz: {error}",
        "audio_viz_disabled": "Visualização de áudio desativada",
    },
    "de_DE": {
        "tab_assistant": "Assistent",
        "tab_configurations": "Einstellungen",
        "run_voice_recognition": "Spracherkennung starten",
        "voice_already_running": "Spracherkennung läuft bereits.",
        "starting_voice_recognition": "Spracherkennung wird gestartet…",
        "recognized_text": "Erkannter Text",
        "agent_response": "Antwort des Assistenten",
        "error_occurred": "Ein Fehler ist aufgetreten",
        "settings_title": "Einstellungen",
        "settings_subtitle": "Ihre Schlüssel werden nur in der <b>.env</b>-Datei dieses Projekts gespeichert "
        "(nicht committen). Optional: Werte unten ein- oder ausblenden.",
        "language_group": "Sprache",
        "language_label": "Oberfläche und Spracheingabe",
        "api_keys_group": "API-Schlüssel",
        "paste_key_placeholder": "Schlüssel hier einfügen",
        "show_keys": "Schlüssel anzeigen",
        "save_env": "In .env speichern",
        "saved_dialog_title": "Gespeichert",
        "saved_dialog_body": "Einstellungen in <b>.env</b> geschrieben. "
        "Für einen neuen Groq-Schlüssel bitte die App <b>beenden und neu starten</b>.",
        "error_dialog_title": "Fehler",
        "error_dialog_save": "Speichern fehlgeschlagen",
        "field_elevenlabs": "ElevenLabs",
        "hint_elevenlabs": "Text-zu-Sprache",
        "field_groq": "Groq (LLM)",
        "hint_groq": "LLM-Backend des Assistenten",
        "field_coinmarketcap": "CoinMarketCap",
        "hint_coinmarketcap": "Krypto-Kurse",
        "field_spotify_id": "Spotify — Client-ID",
        "hint_spotify_id": "Spotify-Integration",
        "field_spotify_secret": "Spotify — Client-Geheimnis",
        "hint_spotify_secret": "Spotify-Integration",
        "speak_now": "Bitte sprechen",
        "err_no_speech": "Keine Sprache innerhalb der Zeitgrenze erkannt.",
        "err_unknown_speech": "Sprache konnte nicht verstanden werden.",
        "err_service": "Fehler beim Spracherkennungsdienst: {error}",
        "audio_viz_disabled": "Audio-Visualisierung deaktiviert",
    },
    "es_ES": {
        "tab_assistant": "Asistente",
        "tab_configurations": "Configuración",
        "run_voice_recognition": "Reconocimiento de voz",
        "voice_already_running": "El reconocimiento de voz ya está en curso.",
        "starting_voice_recognition": "Iniciando reconocimiento de voz…",
        "recognized_text": "Texto reconocido",
        "agent_response": "Respuesta del agente",
        "error_occurred": "Se produjo un error",
        "settings_title": "Ajustes",
        "settings_subtitle": "Tus claves solo se guardan en el archivo <b>.env</b> de este proyecto "
        "(no lo subas al repositorio). Opcional: mostrar u ocultar los valores abajo.",
        "language_group": "Idioma",
        "language_label": "Interfaz y voz",
        "api_keys_group": "Claves API",
        "paste_key_placeholder": "Pega tu clave aquí",
        "show_keys": "Mostrar claves",
        "save_env": "Guardar en .env",
        "saved_dialog_title": "Guardado",
        "saved_dialog_body": "Ajustes escritos en <b>.env</b>. "
        "Para usar una nueva clave de Groq, <b>cierra y vuelve a abrir</b> la aplicación.",
        "error_dialog_title": "Error",
        "error_dialog_save": "No se pudo guardar",
        "field_elevenlabs": "ElevenLabs",
        "hint_elevenlabs": "Texto a voz",
        "field_groq": "Groq (LLM)",
        "hint_groq": "Motor LLM del asistente",
        "field_coinmarketcap": "CoinMarketCap",
        "hint_coinmarketcap": "Cotizaciones de cripto",
        "field_spotify_id": "Spotify — ID de cliente",
        "hint_spotify_id": "Integración Spotify",
        "field_spotify_secret": "Spotify — Secreto de cliente",
        "hint_spotify_secret": "Integración Spotify",
        "speak_now": "Habla ahora",
        "err_no_speech": "No se detectó voz dentro del límite de tiempo.",
        "err_unknown_speech": "No se pudo entender lo dicho.",
        "err_service": "Error del servicio de reconocimiento de voz: {error}",
        "audio_viz_disabled": "Visualización de audio desactivada",
    },
}


def set_language(locale: str) -> None:
    global _current
    _current = locale if locale in VALID_LOCALES else DEFAULT_LOCALE


def set_language_from_config() -> None:
    """Read APP_LANGUAGE from environment (after load_dotenv)."""
    try:
        from main import config

        raw = (getattr(config, "app_language", None) or os.getenv("APP_LANGUAGE") or DEFAULT_LOCALE).strip()
    except Exception:
        raw = (os.getenv("APP_LANGUAGE") or DEFAULT_LOCALE).strip()
    set_language(raw if raw in VALID_LOCALES else DEFAULT_LOCALE)


def current_locale() -> str:
    return _current


def tr(key: str, **kwargs) -> str:
    table = STRINGS.get(_current, STRINGS[DEFAULT_LOCALE])
    text = table.get(key) or STRINGS[DEFAULT_LOCALE].get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text


def speech_google_code() -> str:
    return SPEECH_LANGUAGE_CODE.get(_current, "en-US")
