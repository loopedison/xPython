@echo off
echo "--------------------------------------------------"
pyinstaller -F -w -i image\vLauncher.ico --hidden-import=PyQt5.sip vLauncherClient.py
copy dist\vLauncherClient.exe .\
echo "--------------------------------------------------"
pyinstaller -F -w -i image\vLauncher.ico --hidden-import=PyQt5.sip vLauncherServer.py
copy dist\vLauncherServer.exe .\
echo "--------------------------------------------------"
pause
exit