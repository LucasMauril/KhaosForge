@echo off
REM ==============================================================================
REM Khaos Forge - Windows Environment Provisioner
REM Author: Lucas Mauril
REM ==============================================================================

echo [*] Provisioning Khaos Forge on Windows...

python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [-] Python not found in PATH. Please install Python 3.10+
    exit /b 1
)

echo [+] Python environment verified.
echo [*] Checking dependencies...
pip install -r requirements.txt 2> nul || echo [*] Core runs with standard library (Zero external deps required).

echo [+] Setup complete. You can run .\bin\khaos.cmd --help
