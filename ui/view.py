import sys
import threading
import traceback
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from ui.assistant_service import AssistantService
from ui.audio_processor import AudioProcessor
from ui.components import AssistantTab
from ui.output_redirect import OutputRedirect
from ui.styles import TAB_STYLE

class MainWindow(QMainWindow):
    recognition_finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.assistant_service = AssistantService()
        self._recognition_running = False
        self.recognition_finished.connect(self._on_recognition_finished)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(TAB_STYLE)
        main_layout.addWidget(self.tabs)

        self.assistant_tab = AssistantTab(self)
        self.tabs.addTab(self.assistant_tab, "Assistant")
        self.tabs.addTab(QWidget(), "Configurations")

        self.original_stdout = sys.stdout
        self.stdout_redirect = OutputRedirect(self.assistant_tab.terminal)
        sys.stdout = self.stdout_redirect

        self.assistant_tab.run_button.clicked.connect(self.run_recognition_thread)

        self.audio_processor = AudioProcessor(self.assistant_tab.canvas)
        self.audio_processor.start_stream()

    def run_recognition_thread(self):
        if self._recognition_running:
            print("Voice recognition is already running.")
            return
        self._recognition_running = True
        self.assistant_tab.run_button.setEnabled(False)
        print("Starting voice recognition...")
        threading.Thread(target=self.run_recognition, daemon=True).start()

    def run_recognition(self):
        try:
            recognized_text, result = self.assistant_service.run_voice_command()
            print(f"Recognized text: {recognized_text}")
            print(f"Agent's response: {result}")
        except Exception as e:
            print(f"An error occurred: {type(e).__name__}: {e}")
            print(traceback.format_exc(limit=3))
        finally:
            self._recognition_running = False
            self.recognition_finished.emit()

    def _on_recognition_finished(self):
        self.assistant_tab.run_button.setEnabled(True)

    def closeEvent(self, event):
        self.audio_processor.stop_stream()
        sys.stdout = self.original_stdout
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
