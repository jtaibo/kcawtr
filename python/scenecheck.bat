@echo off

set MAYA_VERSION=%1
set MAYA_PROJECT=%2
set MAYA_SCENE=%3

set MAYA_BIN_DIR="C:\Archivos de programa\autodesk\Maya%MAYA_VERSION%\bin"

%MAYA_BIN_DIR%\mayapy.exe scenecheck.py "%MAYA_PROJECT%" "%MAYA_SCENE%"
