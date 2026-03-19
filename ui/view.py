import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPlainTextEdit, QPushButton, QTabWidget, QApplication

from ui.canvas_plot import MplCanvas
from ui.audio_processor import AudioProcessor
from ui.output_redirect import OutputRedirect
from recognition_of_speech import GoogleSpeechRecognizer
from agents import general_agent

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Criar o widget central e configurar o layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Criar o QTabWidget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { 
                border-top: 2px solid #C2C2C2;
                background: #2b2b2b;
            }

            QTabBar::tab {
                background: #444444;
                color: white;
                font-size: 20px;
                border: 1px solid #2b2b2b;
                border-radius: 5px;
                padding: 10px;
                min-width: 300px;
                min-height: 40px;
            }

            QTabBar::tab:selected, QTabBar::tab:hover {
                background: #555555;
                border-color: #888888;
            }

            QTabBar::tab:selected {
                color: #FFD700;
                background: #666666;
            }
        """)

        self.main_layout.addWidget(self.tabs)  # Adiciona o QTabWidget ao layout principal

        # Adicionar a primeira aba
        home_tab = QWidget()
        self.tabs.addTab(home_tab, "Assistant")

        # Adicionar a segunda aba
        second_tab = QWidget()
        self.tabs.addTab(second_tab, "Configurations")

        # Layout da aba inicial (Home)
        home_layout = QVBoxLayout(home_tab)

        # Configuração do canvas do Matplotlib
        self.canvas = MplCanvas(self, width=9, height=4, dpi=100)
        home_layout.addWidget(self.canvas, stretch=1)

        # Criar o terminal na metade inferior da tela
        self.terminal = QPlainTextEdit(self)
        self.terminal.setReadOnly(True)  # Terminal somente para leitura
        self.terminal.setStyleSheet("background-color: #2b2b2b; color: white; border: 2px black")
        home_layout.addWidget(self.terminal, stretch=1)

        # Redirecionar stdout para o terminal embutido
        self.original_stdout = sys.stdout
        self.stdout_redirect = OutputRedirect(self.terminal)
        sys.stdout = self.stdout_redirect

        # Criar o botão na parte inferior centralizada
        self.button = QPushButton("Run Voice Recognition", self)
        self.button.setFixedSize(200, 200)  # Definir um tamanho fixo para o botão
        self.button.setStyleSheet("""
            QPushButton {
                border-radius: 100px;
                border: 2px solid black;
                background-color: #FFD700;;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #a0a0a0;
            }
        """)
        self.button.clicked.connect(self.run_recognition_thread)  # Conectar o clique do botão a uma função

        # Layout horizontal para centralizar o botão
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.button)
        button_layout.addStretch(1)
        home_layout.addLayout(button_layout)  # Adicionar o layout do botão ao layout da aba

        # Inicializa o processador de áudio
        self.audio_processor = AudioProcessor(self.canvas)
        self.audio_processor.start_stream()

    def run_recognition_thread(self):
        # Iniciar o reconhecimento de voz em uma nova thread para não bloquear a GUI
        threading.Thread(target=self.run_recognition, daemon=True).start()

    def run_recognition(self):
        # Executa o reconhecimento de voz e processa o resultado
        try:
            voice_recognizer = GoogleSpeechRecognizer()
            recognized_text = voice_recognizer.recognize()

            print(f"Recognized text: {recognized_text}")
            result = general_agent.query(recognized_text)
            print(f"Agent's response: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def closeEvent(self, event):
        self.audio_processor.stop_stream()
        sys.stdout = self.original_stdout
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
