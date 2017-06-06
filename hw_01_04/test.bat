@echo off
echo in_%1.txt> command
echo out.txt>> command

C:/msys64/usr/bin/python3.exe binary_to_hex.py < command > nul
fc out.txt out_%1.txt > nul

if %ERRORLEVEL% EQU 0 echo Test %1 complete

if %ERRORLEVEL% EQU 1 echo Test %1 FAILED

if %ERRORLEVEL% EQU 2 echo Some issue when try Test %1

del in_%1.txt
del out.txt
del out_%1.txt
del command