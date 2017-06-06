@echo off
cls
echo Preparing tests
echo.
C:/msys64/usr/bin/python3.exe convert_tests.py
echo %ERRORLEVEL% tests served
echo.
echo Starting tests
echo.

for /L %%i in (0,1,%ERRORLEVEL%) do call test.bat %%i

echo.
echo End of tests
echo.