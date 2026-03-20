from abc import ABC, abstractmethod

class VoiceRecognizerInterface(ABC):
    @abstractmethod
    def recognize(self, language: str = "en-US") -> str:
        pass