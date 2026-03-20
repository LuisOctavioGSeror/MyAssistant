import speech_recognition as sr

import localization
from recognition_of_speech.interface import VoiceRecognizerInterface


class GoogleSpeechRecognizer(VoiceRecognizerInterface):
    def recognize(self, language: str = "en-US", device_index: int | None = None) -> str:
        recognizer = sr.Recognizer()
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 0.8

        try:
            with sr.Microphone(device_index=device_index) as microphone:
                recognizer.adjust_for_ambient_noise(microphone, duration=0.4)
                print(localization.tr("speak_now"))
                audio = recognizer.listen(microphone, timeout=10, phrase_time_limit=18)
                text = recognizer.recognize_google(audio, language=language)
                return text
        except sr.WaitTimeoutError as exc:
            raise RuntimeError(localization.tr("err_no_speech")) from exc
        except sr.UnknownValueError as exc:
            raise RuntimeError(localization.tr("err_unknown_speech")) from exc
        except sr.RequestError as exc:
            raise RuntimeError(localization.tr("err_service", error=str(exc))) from exc
