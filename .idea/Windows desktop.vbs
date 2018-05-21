Set wshShell =wscript.CreateObject("WScript.Shell") 

wscript.sleep 3600

do

wshshell.sendkeys "{CAPSLOCK}" 

wscript.sleep 900 

wshshell.sendkeys "k" 

wscript.sleep 100 

wshshell.sendkeys "~(enter)"

wscript.sleep 100 

loop