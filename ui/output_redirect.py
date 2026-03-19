from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QTextCursor


class OutputRedirect(QObject):
    text_written = pyqtSignal(str)

    def __init__(self, terminal_widget):
        super().__init__()
        self.terminal_widget = terminal_widget
        self.text_written.connect(self._append_text)

    def write(self, text):
        if text:
            self.text_written.emit(str(text))

    @pyqtSlot(str)
    def _append_text(self, text):
        self.terminal_widget.moveCursor(QTextCursor.End)
        self.terminal_widget.insertPlainText(text)
        self.terminal_widget.moveCursor(QTextCursor.End)

    def flush(self):
        pass
