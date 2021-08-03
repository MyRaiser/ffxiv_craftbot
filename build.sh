rm -rf dist
pyinstaller -F -w -i ffxiv_craftbot.ico ffxiv_craftbot.pyw --onefile
cp ffxiv_craftbot.json dist
cp ffxiv_craftbot.ico dist