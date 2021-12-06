import os
import winreg

#参考
# https://itasuke.hatenablog.com/entry/2018/01/08/133510

import tkinter
from tkinter import ttk
from tkinter import filedialog


# 宣言
str_rootkey = "" # 使用するルートキー
str_type = "" # 適応するレジストリの位置
str_registry = "" # レジストリの型(?)の種類
str_extension = "" # 対象拡張指名
str_exe = "" # 実行ファイル名



# ウィンドウを作る
class MakeWindow():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry() # サイズ設定
        self.window.title("hello world")
        self.window.resizable(width= False, height= False)
        self.window.configure(background= "#add8e6")

    # フレーム作成
    def makeFrame(self):
        self.winf = tkinter.Frame(self.window)
        self.winf.grid(column= 0, row= 0, sticky= tkinter.NSEW, padx= 5, pady= 5) # NSEW:位置揃え, padx,y:上下、左右の余白
        # self.winf.grid(column= 0, row= 0, padx= 10, pady= 10) # NSEW:位置揃え, padx,y:上下、左右の余白
        self.winf.configure(background="#4682b4")

    # ウィジェット作成
    def makeWidget(self):
        # ラベル
        self.material_title = tkinter.Label(self.winf, text= "右クリックしたときに出る項目追加するやーつ")
        # self.material_title = tkinter.Label(self.winf,width= 50, height= 100, text= "右クリックしたときに出る項目追加するやーつ")
        self.material_rootkey_label = tkinter.Label(self.winf, text= "ルートキー設定")
        self.material_registry_label = tkinter.Label(self.winf, text= "レジストリの種類")
        self.material_type_label = tkinter.Label(self.winf, text = "対象項目")
        self.material_exe_label = tkinter.Label(self.winf, text = "適応実行ファイル")
        self.material_extension_label = tkinter.Label(self.winf, text = "対象拡張指名")
        self.material_space_label = tkinter.Label(self.winf, text= " ")
        self.material_space_label.configure(background= '#4682b4')

        # コンボボックス
        self.material_rootkey_combobox = tkinter.ttk.Combobox(self.winf, values=["HKCR", "HKCU", "HKLM", "HKU", "HKCC"])
        self.material_rootkey_combobox.configure(state= "readonly")
        self.material_rootkey_combobox.current(1)
        self.material_registry_combobox = tkinter.ttk.Combobox(self.winf, values=["文字列値", "バイナリ値", "DWORD(32bit)値", "QWORD(64bit)値", "複数行文字列値", "展開可能な文字列値", "キー",])
        self.material_registry_combobox.configure(state= "readonly")
        self.material_registry_combobox.current(0)
        self.material_type_combobox = tkinter.ttk.Combobox(self.winf, values=["デスクトップ","背景", "フォルダ", "ファイル", "ライブラリ", "特定拡張子"])
        self.material_type_combobox.bind('<<ComboboxSelected>>', self.selectType) # コンボボックスが変更されたときに発生するイベント
        self.material_type_combobox.configure(state= "readonly")
        self.material_type_combobox.current(0)

        # テキストボックス
        self.material_extension_textbox = tkinter.ttk.Entry(self.winf)
        self.material_extension_textbox.configure(state= "readonly")

        # ボタン
        self.material_exe_button = tkinter.ttk.Button(self.winf, text= "参照", command= self.choiceExeFile)
        self.material_exe_button.bind('<Return>', lambda event: self.choiceExeFile())
        self.material_add_button = tkinter.ttk.Button(self.winf, text= "レジストリ追加", command= self.showSetting)
        self.material_add_button.bind('<Return>', lambda event: self.showSetting())




    # widget設定
    def setWidget(self):
        self.material_title.grid(column= 0, row= 0, columnspan= 3, padx= 10, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_space_label.grid(column= 1, row=1, rowspan= 3, padx=1)

        self.material_rootkey_label.grid(column= 0, row= 1, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )
        self.material_rootkey_combobox.grid(column= 2, row= 1, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_registry_label.grid(column= 0, row= 2, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_registry_combobox.grid(column= 2, row= 2, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_type_label.grid(column= 0, row= 3, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_type_combobox.grid(column= 2, row= 3, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_extension_label.grid(column=0, row=4, padx=2, pady=5, sticky= tkinter.W + tkinter.E)
        self.material_extension_textbox.grid(column=2, row=4, padx=2, pady=5, sticky= tkinter.W + tkinter.E)

        self.material_exe_label.grid(column= 0, row= 5, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_exe_button.grid(column= 2, row= 5, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)

        self.material_add_button.grid(column= 0, row= 6, columnspan= 3, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)





    # ファイル選択ダイアログ
    def choiceExeFile(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        ft = [("実行ファイル", "*.exe"), ("すべてのファイル", "*")]
        fp = "C:\\Program files"
        self.path_exe_file = self.material_exe_filechoice = tkinter.filedialog.askopenfilename(filetypes= ft, initialdir= fp)

        print(self.path_exe_file)
        return self.path_exe_file

    # 表示
    def showWindow(self):
        self.window.mainloop()


    # タイプコンボボックスの項目が変わったときに動作する
    def selectType(self, event):
        if(self.material_type_combobox.get() == "特定拡張子"):
            self.material_extension_textbox.configure(state= "normal")
        else:
            self.material_extension_textbox.configure(state= "readonly")


    # 設定項目の確認
    def showSetting(self):

        # str_rootkey = self.material_rootkey_combobox.get()
        str_rootkey = self.convRootkey(self.material_rootkey_combobox.get())
        # str_registry = self.material_registry_combobox.get()
        str_registry = self.convRegistry(self.material_registry_combobox.get())
        # str_type = self.material_type_combobox.get()
        str_type = self.convType(self.material_type_combobox.get(), self.material_extension_textbox.get())
        # ここに例外処理がほしい
        str_extension = self.material_extension_textbox.get()
        str_exe = self.path_exe_file


        print(f'rootkey is {str_rootkey}')
        print(f' type is {str_type}')
        print(f'registry is {str_registry}')
        print(f'extension is {str_extension}')
        print(f' exefile is {str_exe}\n\n')

        self.addReg()


    def convRootkey(self, temp_key):
        if(temp_key == "HKCR"):
            temp_key = winreg.HKEY_CLASSES_ROOT
        elif(temp_key == "HKCU"):
            temp_key = winreg.HKEY_CURRENT_USER
        elif(temp_key == "HKLM"):
            temp_key = winreg.HKEY_LOCAL_MACHINE
        elif(temp_key == "HKU"):
            temp_key = winreg.HKEY_USERS
        elif(temp_key == "HKCC"):
            temp_key = winreg.HKEY_CURRENT_CONFIG
        return temp_key

    def convRegistry(self, temp_reg):
        if(temp_reg == "文字列値"):
            temp_reg = winreg.REG_SZ
        elif(temp_reg == "バイナリ値"):
            temp_reg = winreg.REG_BINARY
        elif(temp_reg == "DWORD(32bit)値"):
            temp_reg = winreg.REG_DWORD
        elif(temp_reg == "QWORD(64bit)値"):
            temp_reg = winreg.REG_QWORD
        elif(temp_reg == "複数行文字列値"):
            temp_reg = winreg.REG_MULTI_SZ
        elif(temp_reg == "展開可能な文字列値"):
            temp_reg = winreg.REG_EXPAND_SZ
        elif(temp_reg == "キー"):
            # ここ何を入れたらいいか分らない
            temp_reg = "キーを選択したけどよくわからん"
        return temp_reg


    def convType(self, temp_type, temp_extension):
        if(temp_type == "デスクトップ"):
            temp_type = "Software\\Classes\\DesktopBackground\\"
        elif(temp_type == "拝啓"):
            temp_type = "Software\\Classes\\Directory\\Background\\shell\\"
        elif(temp_type == "フォルダ"):
            temp_type = "Software\\Classes\\Directory\\shell\\"
        elif(temp_type == "ファイル"):
            temp_type = "Software\\Classes\\*\\shell\\"
        elif(temp_type == "ライブラリ"):
            temp_type = "Software\\Classes\\Folder\\shell\\"
        elif(temp_type == "特定拡張子"):
            temp_type = f"Software\\Classes\\SystemFileAssociations\\.{temp_extension}\\shell\\"
        return temp_type


    def addReg(self):
        RegistryAdd().addKey()


# レジストリの登録
class RegistryAdd():
    def addKey(self):
        # 7-zipにtestキーを追加して値「hello world」を追加する
        path = r'Software\\7-Zip\\test'

        newkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path)
        winreg.CloseKey

        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'PanelPath0', 0, winreg.REG_SZ, 'hello world')
        winreg.CloseKey(key)


# レジストリの解除(削除)
class RegistryDel():
    def delKey(self):
        # いつかやる
        pass


# メイン部
def Main():
    window = MakeWindow()
    window.makeFrame()
    window.makeWidget()
    window.setWidget()


    window.showWindow()



if __name__ == "__main__":
    Main()

    # class: HelloWorld
    # 関数: helloWorld
    # 変数: hello_world
