# ============================================
# run.bat (Windows)
# ============================================
@echo off
echo ========================================
echo Systeme Expert - Droit du Numerique
echo ========================================
echo.
echo Demarrage de l'application...
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERREUR : Impossible de demarrer l'application
    echo Verifiez que Python est installe
    pause
    exit /b 1
)