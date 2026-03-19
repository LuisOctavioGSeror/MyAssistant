"""
Configurations tab: API keys are saved to the project root .env file.
"""
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QCheckBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from main import config as app_config
from ui.styles import CONFIG_SAVE_BUTTON_STYLE, CONFIGURATIONS_PANEL_STYLE


# Fixed order in file; other keys in .env are preserved when saving
ENV_KEY_ORDER = [
    "ELEVENLABS_API_KEY",
    "GROQ_API_KEY",
    "COINMARKETCAP_API",
    "SPOTIFY_CLIENT_ID",
    "SPOTIFY_CLIENT_SECRET",
]

FIELD_LABELS = {
    "ELEVENLABS_API_KEY": "ElevenLabs",
    "GROQ_API_KEY": "Groq (LLM)",
    "COINMARKETCAP_API": "CoinMarketCap",
    "SPOTIFY_CLIENT_ID": "Spotify — Client ID",
    "SPOTIFY_CLIENT_SECRET": "Spotify — Client Secret",
}

FIELD_HINTS = {
    "ELEVENLABS_API_KEY": "Text-to-speech",
    "GROQ_API_KEY": "Assistant LLM backend",
    "COINMARKETCAP_API": "Crypto quotes",
    "SPOTIFY_CLIENT_ID": "Spotify integration",
    "SPOTIFY_CLIENT_SECRET": "Spotify integration",
}


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _env_path() -> Path:
    return _project_root() / ".env"


def _load_env_dict(path: Path) -> dict:
    data = {}
    if not path.is_file():
        return data
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        data[key.strip()] = value.strip()
    return data


def _save_env(updates: dict) -> None:
    path = _env_path()
    merged = _load_env_dict(path)
    for k in ENV_KEY_ORDER:
        merged[k] = (updates.get(k) or "").strip()
    lines = []
    for k in ENV_KEY_ORDER:
        lines.append(f"{k}={merged.get(k, '')}")
    for k in sorted(merged.keys()):
        if k not in ENV_KEY_ORDER:
            lines.append(f"{k}={merged[k]}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


class ConfigurationsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(CONFIGURATIONS_PANEL_STYLE)

        self._fields: dict[str, QLineEdit] = {}

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        inner = QWidget()
        inner_layout = QVBoxLayout(inner)
        inner_layout.setSpacing(16)

        title = QLabel("Settings")
        title.setObjectName("configTitle")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        inner_layout.addWidget(title)

        subtitle = QLabel(
            "Your keys are stored only in this project’s <b>.env</b> file "
            "(do not commit it). Optionally show or hide values below."
        )
        subtitle.setObjectName("configSubtitle")
        subtitle.setWordWrap(True)
        inner_layout.addWidget(subtitle)

        group = QGroupBox("API keys")
        group.setObjectName("configGroup")
        form = QFormLayout(group)
        form.setSpacing(12)
        form.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)

        for key in ENV_KEY_ORDER:
            label_text = FIELD_LABELS[key]
            hint = FIELD_HINTS.get(key, "")
            label_container = QVBoxLayout()
            lab = QLabel(label_text)
            lab.setObjectName("configFieldLabel")
            label_container.addWidget(lab)
            if hint:
                sub = QLabel(hint)
                sub.setObjectName("configFieldHint")
                label_container.addWidget(sub)
            wrap = QWidget()
            wrap.setLayout(label_container)

            edit = QLineEdit()
            edit.setPlaceholderText("Paste your key here")
            edit.setEchoMode(QLineEdit.Password)
            edit.setMinimumHeight(36)
            self._fields[key] = edit
            form.addRow(wrap, edit)

        inner_layout.addWidget(group)

        show_secrets = QCheckBox("Show keys")
        show_secrets.setObjectName("configShowSecrets")
        show_secrets.toggled.connect(self._toggle_secrets)
        inner_layout.addWidget(show_secrets)

        btn_row = QHBoxLayout()
        btn_row.addStretch(1)
        save_btn = QPushButton("Save to .env")
        save_btn.setStyleSheet(CONFIG_SAVE_BUTTON_STYLE)
        save_btn.setMinimumHeight(44)
        save_btn.setMinimumWidth(200)
        save_btn.clicked.connect(self._on_save)
        btn_row.addWidget(save_btn)
        btn_row.addStretch(1)
        inner_layout.addLayout(btn_row)

        inner_layout.addStretch(1)

        scroll.setWidget(inner)
        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.addWidget(scroll)

        self._load_from_env()

    def _toggle_secrets(self, checked: bool):
        mode = QLineEdit.Normal if checked else QLineEdit.Password
        for edit in self._fields.values():
            edit.setEchoMode(mode)

    def _load_from_env(self):
        path = _env_path()
        data = _load_env_dict(path)
        fallbacks = {
            "ELEVENLABS_API_KEY": app_config.elevenlabs_api_key or "",
            "GROQ_API_KEY": app_config.groq_api_key or "",
            "COINMARKETCAP_API": app_config.coinmarketcap_api or "",
            "SPOTIFY_CLIENT_ID": app_config.spotify_client_id or "",
            "SPOTIFY_CLIENT_SECRET": app_config.spotify_client_secret or "",
        }
        for key, edit in self._fields.items():
            val = (data.get(key) or "").strip() or fallbacks.get(key, "")
            edit.setText(val)

    def _on_save(self):
        try:
            updates = {k: self._fields[k].text() for k in ENV_KEY_ORDER}
            _save_env(updates)
            app_config.reload_from_disk()
            QMessageBox.information(
                self,
                "Saved",
                "Keys written to <b>.env</b>. "
                "To use a new Groq key, please <b>quit and restart</b> the app.",
            )
        except OSError as e:
            QMessageBox.critical(self, "Error", f"Could not save: {e}")
