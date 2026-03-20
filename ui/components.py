import localization
from PyQt5.QtWidgets import QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

from ui.canvas_plot import MplCanvas
from ui.styles import RUN_BUTTON_STYLE, TERMINAL_STYLE


class AssistantTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.canvas = MplCanvas(self, width=9, height=4, dpi=100)
        layout.addWidget(self.canvas, stretch=1)

        self.terminal = QPlainTextEdit(self)
        self.terminal.setReadOnly(True)
        self.terminal.setStyleSheet(TERMINAL_STYLE)
        layout.addWidget(self.terminal, stretch=1)

        self.run_button = QPushButton(self)
        self.run_button.setFixedSize(200, 200)
        self.run_button.setStyleSheet(RUN_BUTTON_STYLE)
        self.apply_translations()

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.run_button)
        button_layout.addStretch(1)
        layout.addLayout(button_layout)

    def apply_translations(self):
        self.run_button.setText(localization.tr("run_voice_recognition"))
