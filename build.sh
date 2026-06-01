#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Build the portable, single-file executable for the SPL-290X app.
#
# Run this ON WINDOWS (Git Bash / WSL with a Windows Python) to get a .exe.
# PyInstaller does not cross-compile: a Linux/macOS build yields a native
# binary for that platform, not a Windows .exe.
# ---------------------------------------------------------------------------
set -euo pipefail

# 1) Sanity-check the math before building.
python spl290x.py --selftest

# 2) Install the build-time-only dependency (not bundled at runtime).
python -m pip install --upgrade pyinstaller

# 3) Produce dist/SPL-290X.exe : onefile, windowed (no console).
pyinstaller --onefile --windowed --name SPL-290X spl290x.py

echo
echo "Done. Portable exe: dist/SPL-290X.exe"
