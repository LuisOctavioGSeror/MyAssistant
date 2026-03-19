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

CONFIGURATIONS_PANEL_STYLE = """
    QWidget {
        background-color: #2b2b2b;
        color: #e8e8e8;
    }
    QLabel#configTitle {
        font-size: 26px;
        font-weight: 600;
        color: #FFD700;
        padding-bottom: 4px;
    }
    QLabel#configSubtitle {
        font-size: 13px;
        color: #b0b0b0;
        padding-bottom: 8px;
    }
    QGroupBox#configGroup {
        font-size: 15px;
        font-weight: 600;
        color: #e0e0e0;
        border: 1px solid #555555;
        border-radius: 8px;
        margin-top: 12px;
        padding: 18px 14px 14px 14px;
        background-color: #353535;
    }
    QGroupBox#configGroup::title {
        subcontrol-origin: margin;
        left: 12px;
        padding: 0 8px;
        color: #FFD700;
    }
    QLabel#configFieldLabel {
        font-size: 14px;
        font-weight: 500;
        color: #f0f0f0;
    }
    QLabel#configFieldHint {
        font-size: 11px;
        color: #888888;
    }
    QLineEdit {
        background-color: #1e1e1e;
        color: #f5f5f5;
        border: 1px solid #555555;
        border-radius: 6px;
        padding: 8px 12px;
        selection-background-color: #555555;
    }
    QLineEdit:focus {
        border: 1px solid #FFD700;
    }
    QCheckBox#configShowSecrets {
        font-size: 13px;
        color: #c0c0c0;
        spacing: 8px;
    }
    QCheckBox#configShowSecrets::indicator {
        width: 18px;
        height: 18px;
    }
    QScrollArea {
        background: transparent;
    }
"""

CONFIG_SAVE_BUTTON_STYLE = """
    QPushButton {
        background-color: #FFD700;
        color: #1a1a1a;
        font-weight: 600;
        font-size: 14px;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #e6c200;
    }
    QPushButton:pressed {
        background-color: #ccad00;
    }
    QPushButton:disabled {
        background-color: #666666;
        color: #999999;
    }
"""
