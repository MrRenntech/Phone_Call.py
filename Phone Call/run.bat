@echo off
TITLE Phone Call Launcher
ECHO Starting Phone Call Script...
ECHO.
REM This will launch the GUI version by default if no arguments are passed.
python phone_call.py
ECHO.
REM Pause only if the script exits immediately (e.g. error), 
REM though with GUI the script waits for mainloop.
PAUSE
