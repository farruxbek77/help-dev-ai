Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Hozirgi papkani olish
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Python scriptni yashirin rejimda ishga tushirish
WshShell.Run "python " & chr(34) & currentDir & "\bot_service.py" & chr(34), 0, False

Set WshShell = Nothing
Set fso = Nothing
