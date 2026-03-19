from elevenlabs.play import play
from elevenlabs.client import ElevenLabs

from main.config import elevenlabs_api_key


def convert_text_to_speech(text: str) -> str:
    api_key = elevenlabs_api_key
    client = ElevenLabs(api_key=api_key)
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    play(audio)
    return "text spoken"
