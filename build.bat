@echo off
REM ---------------------------------------------------------------------------
REM Build the portable, single-file Windows executable for the SPL-290X app.
REM Requires: Windows + Python 3.8+ (Tkinter ships with the standard installer).
REM ---------------------------------------------------------------------------

REM 1) Sanity-check the math before building.
python spl290x.py --selftest
if errorlevel 1 (
    echo.
    echo Self-test FAILED - aborting build.
    exit /b 1
)

REM 2) Install the build-time-only dependency (not bundled at runtime).
python -m pip install --upgrade pyinstaller

REM 3) Produce dist\SPL-290X.exe : onefile, windowed (no console).
pyinstaller --onefile --windowed --name SPL-290X spl290x.py

echo.
echo Done. Portable exe: dist\SPL-290X.exe
