' ショートカットリンクの作成

' 参考(の範疇でおさまってるか？)
' https://www.projectgroup.info/tips/Windows/vbs_0001.html

' *.vbs TergetPATH SetPATH SetNAME Description Shortcut

' 引数をとれるようにする
args_number = Wscript.Arguments.Count

Set shortcut = WScript.CreateObject("WScript.Shell").CreateShortcut(Wscript.Arguments(1) & "\" & Wscript.Arguments(2) & ".lnk")
shortcut.TargetPath = Wscript.Arguments(0)
shortcut.Description = Wscript.Arguments(3) & " (&" & Wscript.Arguments(4) & ")"
shortcut.Save

' 出力確認
Wscript.Echo "setPATH = " & Wscript.Arguments(1) & "\" & Wscript.Arguments(2) & ".lnk"
Wscript.Echo "tergetPATH = " & Wscript.Arguments(0)
Wscript.Echo "Description = " & Wscript.Arguments(3) & " (&" & Wscript.Arguments(4) & ")"

' Set shell = WScript.CreateObject("WScript.Shell")
'
' desktopPath = shell.SpecialFolders("Desktop")
' fil = desktopPath + "\電卓.lnk"
'
' Set shortCut = shell.CreateShortcut(fil)
' shortCut.TargetPath = "%SystemRoot%\System32\calc.exe"
' shortCut.Save
