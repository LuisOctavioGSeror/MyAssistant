"""
Configurations tab: API keys and language saved to the project root .env file.
"""
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
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

import localization
from main import config as app_config
from ui.styles import CONFIG_SAVE_BUTTON_STYLE, CONFIGURATIONS_PANEL_STYLE

# Keys written to .env (order). APP_LANGUAGE first.
API_KEYS_ORDER = [
    "ELEVENLABS_API_KEY",
    "GROQ_API_KEY",
    "COINMARKETCAP_API",
    "SPOTIFY_CLIENT_ID",
    "SPOTIFY_CLIENT_SECRET",
]

WRITE_ORDER = ["APP_LANGUAGE"] + API_KEYS_ORDER

FIELD_TR_KEYS = {
    "ELEVENLABS_API_KEY": ("field_elevenlabs", "hint_elevenlabs"),
    "GROQ_API_KEY": ("field_groq", "hint_groq"),
    "COINMARKETCAP_API": ("field_coinmarketcap", "hint_coinmarketcap"),
    "SPOTIFY_CLIENT_ID": ("field_spotify_id", "hint_spotify_id"),
    "SPOTIFY_CLIENT_SECRET": ("field_spotify_secret", "hint_spotify_secret"),
}

# Combo display names (same in every UI locale)
LANG_COMBO_ITEMS = [
    ("Português (Brasil)", "pt_BR"),
    ("English", "en_US"),
    ("Deutsch", "de_DE"),
    ("Español", "es_ES"),
]


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
    for k, v in updates.items():
        merged[k] = (v or "").strip() if isinstance(v, str) else v
    lines = []
    for k in WRITE_ORDER:
        lines.append(f"{k}={merged.get(k, '')}")
    for k in sorted(merged.keys()):
        if k not in WRITE_ORDER:
            lines.append(f"{k}={merged[k]}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


class ConfigurationsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(CONFIGURATIONS_PANEL_STYLE)

        self._fields: dict[str, QLineEdit] = {}
        self._api_label_titles: dict[str, QLabel] = {}
        self._api_label_hints: dict[str, QLabel] = {}

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        inner = QWidget()
        inner_layout = QVBoxLayout(inner)
        inner_layout.setSpacing(16)

        self._title_label = QLabel()
        self._title_label.setObjectName("configTitle")
        self._title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        inner_layout.addWidget(self._title_label)

        self._subtitle_label = QLabel()
        self._subtitle_label.setObjectName("configSubtitle")
        self._subtitle_label.setWordWrap(True)
        inner_layout.addWidget(self._subtitle_label)

        lang_group = QGroupBox()
        lang_group.setObjectName("configGroup")
        lang_layout = QVBoxLayout(lang_group)
        lang_form = QFormLayout()
        lang_form.setSpacing(10)
        self._lang_group = lang_group
        self._lang_form_label = QLabel()
        self._lang_form_label.setObjectName("configFieldLabel")
        self._lang_combo = QComboBox()
        self._lang_combo.setMinimumHeight(36)
        for display, code in LANG_COMBO_ITEMS:
            self._lang_combo.addItem(display, code)
        lang_form.addRow(self._lang_form_label, self._lang_combo)
        lang_layout.addLayout(lang_form)
        inner_layout.addWidget(lang_group)

        api_group = QGroupBox()
        api_group.setObjectName("configGroup")
        form = QFormLayout(api_group)
        form.setSpacing(12)
        form.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._api_group = api_group

        for key in API_KEYS_ORDER:
            tr_title, tr_hint = FIELD_TR_KEYS[key]
            label_container = QVBoxLayout()
            lab = QLabel()
            lab.setObjectName("configFieldLabel")
            self._api_label_titles[key] = lab
            label_container.addWidget(lab)
            sub = QLabel()
            sub.setObjectName("configFieldHint")
            self._api_label_hints[key] = sub
            label_container.addWidget(sub)
            wrap = QWidget()
            wrap.setLayout(label_container)

            edit = QLineEdit()
            edit.setEchoMode(QLineEdit.Password)
            edit.setMinimumHeight(36)
            self._fields[key] = edit
            form.addRow(wrap, edit)

        inner_layout.addWidget(api_group)

        self._show_secrets = QCheckBox()
        self._show_secrets.setObjectName("configShowSecrets")
        self._show_secrets.toggled.connect(self._toggle_secrets)
        inner_layout.addWidget(self._show_secrets)

        btn_row = QHBoxLayout()
        btn_row.addStretch(1)
        self._save_btn = QPushButton()
        self._save_btn.setStyleSheet(CONFIG_SAVE_BUTTON_STYLE)
        self._save_btn.setMinimumHeight(44)
        self._save_btn.setMinimumWidth(200)
        self._save_btn.clicked.connect(self._on_save)
        btn_row.addWidget(self._save_btn)
        btn_row.addStretch(1)
        inner_layout.addLayout(btn_row)

        inner_layout.addStretch(1)

        scroll.setWidget(inner)
        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.addWidget(scroll)

        self.apply_translations()
        self._load_from_env()

    def apply_translations(self):
        loc = localization
        self._title_label.setText(loc.tr("settings_title"))
        self._subtitle_label.setText(loc.tr("settings_subtitle"))
        self._lang_group.setTitle(loc.tr("language_group"))
        self._lang_form_label.setText(loc.tr("language_label"))
        self._api_group.setTitle(loc.tr("api_keys_group"))
        for key in API_KEYS_ORDER:
            tt, th = FIELD_TR_KEYS[key]
            self._api_label_titles[key].setText(loc.tr(tt))
            self._api_label_hints[key].setText(loc.tr(th))
            self._fields[key].setPlaceholderText(loc.tr("paste_key_placeholder"))
        self._show_secrets.setText(loc.tr("show_keys"))
        self._save_btn.setText(loc.tr("save_env"))

    def _toggle_secrets(self, checked: bool):
        mode = QLineEdit.Normal if checked else QLineEdit.Password
        for edit in self._fields.values():
            edit.setEchoMode(mode)

    def _load_from_env(self):
        path = _env_path()
        data = _load_env_dict(path)
        lang = _normalize_lang_value(data.get("APP_LANGUAGE") or app_config.app_language)
        idx = self._lang_combo.findData(lang)
        if idx >= 0:
            self._lang_combo.setCurrentIndex(idx)

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
            lang = self._lang_combo.currentData()
            if not lang:
                lang = "en_US"
            updates = {k: self._fields[k].text() for k in API_KEYS_ORDER}
            updates["APP_LANGUAGE"] = lang
            _save_env(updates)
            app_config.reload_from_disk()
            win = self.window()
            if hasattr(win, "refresh_language_ui"):
                win.refresh_language_ui()
            QMessageBox.information(
                self,
                localization.tr("saved_dialog_title"),
                localization.tr("saved_dialog_body"),
            )
        except OSError as e:
            QMessageBox.critical(
                self,
                localization.tr("error_dialog_title"),
                f"{localization.tr('error_dialog_save')}: {e}",
            )


def _normalize_lang_value(raw: str) -> str:
    if not raw:
        return "en_US"
    v = raw.strip()
    return v if v in localization.VALID_LOCALES else "en_US"
