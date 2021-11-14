:: This script converts all *.ui files to python code
for %%i in (.\ui\*.ui) do (
venv\Scripts\pyuic5.exe %%i > .\src\ui\%%~ni_ui.py
)