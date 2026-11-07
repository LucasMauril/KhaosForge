@echo off
REM ==============================================================================
REM Khaos Forge - Windows Test Suite Runner
REM Author: Lucas Mauril
REM ==============================================================================

echo ========================================================
echo   KHAOS FORGE: RUNNING WINDOWS TEST SUITE
echo ========================================================

cd /d "%~dp0.."

echo [*] 1. Executing Python Core Tests...
python -m unittest discover -s tests -v
if %ERRORLEVEL% NEQ 0 (
    echo [-] Python unit tests failed!
    exit /b %ERRORLEVEL%
)

echo [*] 2. Verifying Windows CLI Executable...
call "%~dp0..\bin\khaos.cmd" --help > nul
if %ERRORLEVEL% NEQ 0 (
    echo [-] CLI executable failed!
    exit /b %ERRORLEVEL%
)

echo ========================================================
echo   ALL TESTS PASSED SUCCESSFULLY (100%% GREEN)
echo ========================================================
