import speech_recognition as sr
from recognition_of_speech.interface import VoiceRecognizerInterface


class GoogleSpeechRecognizer(VoiceRecognizerInterface):
    def recognize(self, language: str = "pt-BR", device_index: int | None = None) -> str:
        recognizer = sr.Recognizer()

        with sr.Microphone(device_index=device_index) as microphone:
            recognizer.adjust_for_ambient_noise(microphone)
            print("Fale agora")
            audio = recognizer.listen(microphone)
            text = recognizer.recognize_google(audio, language=language)
            return text
