from agents import general_agent
from recognition_of_speech import GoogleSpeechRecognizer


class AssistantService:
    def __init__(self, recognizer_factory=GoogleSpeechRecognizer, agent=general_agent):
        self.recognizer_factory = recognizer_factory
        self.agent = agent

    def run_voice_command(self, language="pt-BR"):
        recognizer = self.recognizer_factory()
        recognized_text = recognizer.recognize(language=language)
        agent_response = self.agent.query(recognized_text)
        return recognized_text, str(agent_response)
