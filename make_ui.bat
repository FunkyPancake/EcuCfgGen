:: This script converts all *.ui files to python code 
for %%i in (.\ui\*.ui) do (
pyuic5 %%i > .\src\ui\%%~ni_ui.py
)