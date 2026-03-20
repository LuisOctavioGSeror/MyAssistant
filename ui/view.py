import sys
import threading
import traceback

import localization
from main import config as app_config
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from ui.assistant_service import AssistantService
from ui.audio_processor import AudioProcessor
from ui.components import AssistantTab
from ui.configurations_tab import ConfigurationsTab
from ui.output_redirect import OutputRedirect
from ui.styles import TAB_STYLE

class MainWindow(QMainWindow):
    recognition_finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("MyAssistant")
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
        self.config_tab = ConfigurationsTab(self)
        self.tabs.addTab(self.assistant_tab, localization.tr("tab_assistant"))
        self.tabs.addTab(self.config_tab, localization.tr("tab_configurations"))

        self.original_stdout = sys.stdout
        self.stdout_redirect = OutputRedirect(self.assistant_tab.terminal)
        sys.stdout = self.stdout_redirect

        self.assistant_tab.run_button.clicked.connect(self.run_recognition_thread)

        self.audio_processor = AudioProcessor(self.assistant_tab.canvas)
        self.audio_processor.start_stream()

    def refresh_language_ui(self):
        localization.set_language(app_config.app_language)
        self.tabs.setTabText(0, localization.tr("tab_assistant"))
        self.tabs.setTabText(1, localization.tr("tab_configurations"))
        self.assistant_tab.apply_translations()
        self.config_tab.apply_translations()

    def run_recognition_thread(self):
        if self._recognition_running:
            print(localization.tr("voice_already_running"))
            return
        self._recognition_running = True
        self.assistant_tab.run_button.setEnabled(False)
        print(localization.tr("starting_voice_recognition"))
        threading.Thread(target=self.run_recognition, daemon=True).start()

    def run_recognition(self):
        try:
            recognized_text, result = self.assistant_service.run_voice_command()
            print(f"{localization.tr('recognized_text')}: {recognized_text}")
            print(f"{localization.tr('agent_response')}: {result}")
        except Exception as e:
            print(f"{localization.tr('error_occurred')}: {type(e).__name__}: {e}")
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
