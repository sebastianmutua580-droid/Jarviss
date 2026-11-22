# JARVIS Personal AI Desktop Assistant

JARVIS is a local-first personal assistant for Windows 10/11. This repository is being built in phases.

## Current status: Phase 1

The PySide6 interface foundation is implemented:
- Futuristic responsive dashboard
- Working navigation across ten pages
- Live date and time
- Keyboard chat interface
- Settings saved locally
- Graceful unavailable-service status indicators

AI, voice, Windows automation, search, news, weather, memory, Gmail, and Calendar integrations are added in later phases.

## Requirements

- Windows 10 or 11
- Python 3.12
- Visual Studio C++ Build Tools may be required by optional future dependencies

## Setup

```powershell
cd Jarviss
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

If the PowerShell execution policy blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Test

```powershell
python -m compileall .
python tests/smoke_test.py
python main.py
```
