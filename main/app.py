import sys

from main import config  # noqa: F401 — loads .env before locale
import localization

localization.set_language(config.app_language)

from PyQt5.QtWidgets import QApplication
from ui import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

