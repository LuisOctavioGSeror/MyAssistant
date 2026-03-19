TAB_STYLE = """
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
"""

TERMINAL_STYLE = "background-color: #2b2b2b; color: white; border: 2px black"

RUN_BUTTON_STYLE = """
    QPushButton {
        border-radius: 100px;
        border: 2px solid black;
        background-color: #FFD700;
    }
    QPushButton:hover {
        background-color: #d0d0d0;
    }
    QPushButton:pressed {
        background-color: #a0a0a0;
    }
"""
