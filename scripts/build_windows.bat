@echo off
REM Build a Windows folder bundle (onedir). Run from repo root on Windows:
REM   scripts\build_windows.bat
setlocal
cd /d "%~dp0\.."

if not exist .venv\Scripts\activate.bat (
  echo Create venv first: python -m venv .venv
  echo Then: .venv\Scripts\activate && pip install -r requirements.txt
  exit /b 1
)

call .venv\Scripts\activate.bat
python -m pip install -q --upgrade pip
python -m pip install -q pyinstaller

REM --onedir is more reliable than --onefile for PyQt5 + matplotlib
REM --windowed = no console (use --console for debug builds)
pyinstaller --noconfirm --clean ^
  --onedir ^
  --windowed ^
  --name MyAssistant ^
  --collect-all PyQt5 ^
  --collect-all matplotlib ^
  --hidden-import=ui ^
  --hidden-import=ui.view ^
  --hidden-import=ui.components ^
  --hidden-import=ui.configurations_tab ^
  --hidden-import=ui.styles ^
  --hidden-import=ui.output_redirect ^
  --hidden-import=ui.assistant_service ^
  --hidden-import=ui.audio_processor ^
  --hidden-import=ui.canvas_plot ^
  --hidden-import=main.config ^
  --hidden-import=recognition_of_speech ^
  --hidden-import=agents ^
  --hidden-import=features ^
  --hidden-import=speak ^
  main\app.py

if errorlevel 1 (
  echo PyInstaller failed.
  exit /b 1
)

echo.
echo Output: dist\MyAssistant\MyAssistant.exe
echo Put your .env next to MyAssistant.exe or in the same folder as you run from.
echo Copy your data\notes folder next to the exe if you use notes/email files.
pause
