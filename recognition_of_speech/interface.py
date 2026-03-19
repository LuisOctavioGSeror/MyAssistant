from abc import ABC, abstractmethod

class VoiceRecognizerInterface(ABC):
    @abstractmethod
    def recognize(self, language: str = "pt-BR") -> str:
        pass