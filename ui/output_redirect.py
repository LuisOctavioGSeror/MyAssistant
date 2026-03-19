class OutputRedirect:
    def __init__(self, terminal_widget):
        self.terminal_widget = terminal_widget

    def write(self, text):
        self.terminal_widget.appendPlainText(text)

    def flush(self):
        pass
