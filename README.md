# MyAssistant

Voice assistant with a desktop UI (PyQt5) that:

- captures speech from the microphone;
- sends text to an LLM agent (LlamaIndex + Groq/Ollama);
- runs tools such as text-to-speech, notes, email, Spotify, date/time, and crypto quotes.

## Features

- Desktop UI with a button to start voice recognition;
- real-time audio visualizer;
- agent with tools for lightweight automation;
- environment variables via `.env` and an in-app **Configurations** tab.

## Project layout

- `main/`: app entry point and config;
- `ui/`: main window and visual components;
- `recognition_of_speech/`: speech recognition;
- `agents/`: LLM agents and tools;
- `features/`: integrations and feature logic;
- `speak/`: text-to-speech.

## Requirements

- Python 3.10+ (3.11 recommended)
- `pip`
- Internet access for external services (Groq, ElevenLabs, Spotify, CoinMarketCap)

## Environment variables

1. Copy the example file:

```bash
cp .env.example .env
```

2. Fill in `.env`:

```env
ELEVENLABS_API_KEY=
GROQ_API_KEY=
COINMARKETCAP_API=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

## Local data

The project expects a `data/notes/` folder.

- Example email list: `data/notes/e-mails.example.txt`
- Create the real file:

```bash
cp data/notes/e-mails.example.txt data/notes/e-mails.txt
```

## Run locally

### Ubuntu / Zorin / Debian-based distros

1. Install system packages:

```bash
sudo apt update
sudo apt install -y python3-venv python3-dev portaudio19-dev
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Python dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run:

```bash
python -m main.app
```

### Windows (PowerShell)

1. Create a virtual environment:

```powershell
py -m venv .venv
```

2. Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run:

```powershell
python -m main.app
```

> If `PyAudio` fails to install, install **Visual Studio Build Tools** (C++ workload) and try again.

### macOS

1. Install Python 3 and PortAudio if needed:

```bash
brew install python portaudio
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run:

```bash
python -m main.app
```

## Troubleshooting

- **Microphone / no speech detected**
  - Check OS microphone permission and default input device.
  - On Linux, use system settings or `pavucontrol` to pick the correct input.

- **PyAudio issues**
  - Linux: ensure `portaudio19-dev` is installed.
  - macOS: ensure `portaudio` is installed (Homebrew).
  - Windows: may require Visual C++ Build Tools.

- **External API failures**
  - Verify keys in `.env` or save them in **Configurations**.
  - Check network connectivity.

## MVP checklist (keep it small)

- [ ] `.env` with at least `GROQ_API_KEY` (and any other keys you actually use).
- [ ] `data/notes/e-mails.txt` if you test email-related features.
- [ ] Smoke test: open app → voice button → one agent command.
- [ ] Tell users: keys belong in `.env`; never commit `.env` to git.
- [ ] Optional: disable or skip heavy tools you won’t demo (smaller/fewer failure modes).

## Windows executable (PyInstaller)

Build **on a Windows machine** (same Python version you use to develop).

1. Create a venv and install deps (see [Windows (PowerShell)](#windows-powershell)).
2. Install PyInstaller: `pip install pyinstaller`
3. From the **repo root**, run:

```bat
scripts\build_windows.bat
```

Output: `dist\MyAssistant\MyAssistant.exe`

**Distribute the entire `dist\MyAssistant\` folder** (not only the `.exe`). Place next to `MyAssistant.exe`:

- Your `.env` (or configure keys in the app once on that PC).
- `data\notes\` if you use notes or the email list file.

**Debug build** (show console errors): edit `scripts\build_windows.bat` and replace `--windowed` with `--console`.

**Notes**

- The first build might need extra `--hidden-import=...` if PyInstaller misses a lazy-imported module (the error usually names it).
- Antivirus may briefly flag a new `.exe` (false positive); code signing is a later step.
- The bundle can be **large** (ML + UI). `--onedir` is the default and is usually more reliable than `--onefile` for Qt.

## Notes

- This project is an early prototype.
- Do **not** commit your `.env` file to the repository.
