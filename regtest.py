import winreg

# 値を読む
# path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders'
# key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path)
# data, regtype = winreg.QueryValueEx(key, 'AppData')
# print('種類:', regtype)
# print('データ:', data)
# winreg.CloseKey(key)  # key.Close() と書いても同じ

# 値を書く 動作分らん
# path = r'Software\\7-Zip\\FM'
# key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
# winreg.SetValueEx(key, '値の名前', 0, winreg.REG_SZ, 'データ(PATHとか)')
# winreg.CloseKey(key)

# 値の削除
# path = r'Software\\__test2__'
# with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_SET_VALUE) as key:
#     winreg.DeleteValue(key, '値の名前')

# キー作成
# newkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r'Software\\__test__')
# winreg.CloseKey(newkey)

# キー削除
# winreg.DeleteKeyEx(winreg.HKEY_CURRENT_USER, r'Software\\__test__')

#######################
# 7-zipにtestキーを追加して値「hello world」を追加する
path = r'Software\\7-Zip\\test'
head = winreg.HKEY_CURRENT_USER

newkey = winreg.CreateKeyEx(head, path)
# newkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path)
winreg.CloseKey
#
# key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
# winreg.SetValueEx(key, 'PanelPath0', 0, winreg.REG_SZ, 'hello world')
# winreg.CloseKey(key)

## 7-zip/test内の値を削除して、そのあとキーを削除する
# with winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_SET_VALUE) as key:
#     winreg.DeleteValue(key, 'PanelPath0')
#
# winreg.DeleteKeyEx(winreg.HKEY_CURRENT_USER, path)