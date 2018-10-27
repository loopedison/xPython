@echo off
echo "--------------------------------------------------"
pyinstaller -F -w --hidden-import=PyQt5.sip QtTetris.py
echo "--------------------------------------------------"
pause
exit