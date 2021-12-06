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
str_exe = "" # 実行ファイルpath
str_name = ""

reg_rootkey = winreg.HKEY_CLASSES_ROOT # 使用するルートキー
reg_type = "" # 適応するレジストリの位置
reg_registry = "" # レジストリの型(?)の種類
reg_extension = "" # 対象拡張指名
reg_exe = "" # 実行ファイルpath
reg_name = ""


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
        self.material_name_label = tkinter.Label(self.winf, text= "キーの名称")

         #選択によって表示されるレジストリキーのパスを出力するラベル
        self.material_overview_label = tkinter.Label(self.winf, text= "　　　作成されるキー　　　")
        self.material_rootkey_overview_label = tkinter.Label(self.winf, text= "")
        self.material_registry_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_type_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_exe_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_overview2_label = tkinter.Label(self.winf, text= "　　　生成されるレジストリ　　　")
        self.material_name_overview_label = tkinter.Label(self.winf, text= " ")

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
        self.material_extension_textbox.insert(0, "*")
        self.material_extension_textbox.configure(state= "readonly")
        self.material_name_textbox = tkinter.ttk.Entry(self.winf)

        # ボタン
        self.material_exe_button = tkinter.ttk.Button(self.winf, text= "参照", command= self.choiceExeFile)
        self.material_exe_button.bind('<Return>', lambda event: self.choiceExeFile())
        self.material_add_button = tkinter.ttk.Button(self.winf, text= "レジストリ追加", command= self.addReg)
        self.material_add_button.bind('<Return>', lambda event: self.addReg())

         # 概要表示ボタン
        self.material_overview_button = tkinter.ttk.Button(self.winf, text= "レジストリキーを確認", command= self.showOverview)
        self.material_overview_button.bind('<Return>', lambda event: self.showOverview())




    # widget設定
    def setWidget(self):
        self.material_title.grid(column= 0, row= 0, columnspan= 5, padx= 10, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_space_label.grid(column= 1, row=1, rowspan= 3, padx=1)
        self.material_space_label.grid(column= 3, row=1, rowspan= 3, padx=1)

        self.material_overview_label.grid(column= 4, row= 1, padx= 1, sticky= tkinter.W + tkinter.E )

        self.material_rootkey_label.grid(column= 0, row= 2, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )
        self.material_rootkey_combobox.grid(column= 2, row= 2, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_rootkey_overview_label.grid(column= 4, row= 2, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )

        self.material_type_label.grid(column= 0, row= 3, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_type_combobox.grid(column= 2, row= 3, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_type_overview_label.grid(column= 4, row= 3, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)


        self.material_name_label.grid(column= 0, row= 4, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )
        self.material_name_textbox.grid(column= 2, row= 4, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )
        self.material_name_overview_label.grid(column= 4, row= 4, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E )

        self.material_extension_label.grid(column=0, row=5, padx=2, pady=5, sticky= tkinter.W + tkinter.E)
        self.material_extension_textbox.grid(column=2, row=5, padx=2, pady=5, sticky= tkinter.W + tkinter.E)
        self.material_overview2_label.grid(column=4, row=5, padx=2, pady=5, sticky= tkinter.W + tkinter.E)

        self.material_registry_label.grid(column= 0, row= 6, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_registry_combobox.grid(column= 2, row= 6, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_registry_overview_label.grid(column= 4, row= 6, padx= 2, pady= 10, sticky= tkinter.W + tkinter.E)

        self.material_exe_label.grid(column= 0, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_exe_button.grid(column= 2, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_exe_overview_label.grid(column= 4, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)

        self.material_add_button.grid(column= 0, row= 8, columnspan= 3, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_overview_button.grid(column= 4, row= 8, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)





    # ファイル選択ダイアログ
    def choiceExeFile(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        ft = [("実行ファイル", "*.exe"), ("すべてのファイル", "*")]
        fp = "C:\\Program files"
        self.path_exe_file = self.material_exe_filechoice = tkinter.filedialog.askopenfilename(filetypes= ft, initialdir= fp)

        return self.path_exe_file

    # 表示
    def showWindow(self):
        self.window.mainloop()


    # タイプコンボボックスの項目が変わったときに動作する
    def selectType(self, event):
        if(self.material_type_combobox.get() == "特定拡張子"):
            self.material_extension_textbox.delete(0, tkinter.END)
            self.material_extension_textbox.configure(state= "normal")
        else:
            self.material_extension_textbox.delete(0, tkinter.END)
            self.material_extension_textbox.insert(0, "*")
            self.material_extension_textbox.configure(state= "readonly")


    # 設定項目の確認
    def showSetting(self):

        # str_registry = self.material_registry_combobox.get()
        reg_registry = self.convRegistry(self.material_registry_combobox.get())
        # str_extension = self.material_extension_textbox.get()
        reg_extension = self.convExtension(self.material_extension_textbox.get())

        # ファイルを参照していない場合での例外処理があるとうれしくなる
        str_exe = self.path_exe_file
        # reg_exe = self.convExe(self.path_exe_file)
        reg_exe = str_exe
        # str_rootkey = self.material_rootkey_combobox.get()
        reg_rootkey = self.convRootkey(self.material_rootkey_combobox.get())
        # str_type = self.material_type_combobox.get()
        reg_type = self.convType(self.material_type_combobox.get(), self.convExtension(self.material_extension_textbox.get()))

        reg_name = self.convName(self.material_name_textbox.get())



        print(f'ルートキー is {self.material_rootkey_combobox.get()}')
        print(f'対象項目 is {self.material_type_combobox.get()}')
        print(f'キー名称 is {self.material_name_textbox.get()}')
        print(f'拡張子 is {self.material_extension_textbox.get()}')
        print(f'レジストリ種類 is {self.material_registry_combobox.get()}')
        print(f'実行ファイルpath is {str_exe}\n')

        print(f'ルートキー is {reg_rootkey}')
        print(f'対象項目 is {reg_type}')
        print(f'キー名称 is {reg_name}')
        print(f'拡張子 is {reg_extension}')
        print(f'レジストリ種類 is {reg_registry}')
        print(f'実行ファイルpath is {reg_exe}\n')

    def showOverview(self):
        show_key = self.material_rootkey_combobox.get()
        if(show_key == "HKCR"):
            show_key = "HKEY_CLASSES_ROOT"
        elif(show_key == "HKCU"):
            show_key = "HKEY_CURRENT_USER"
        elif(show_key == "HKLM"):
            show_key = "HKEY_LOCAL_MACHINE"
        elif(show_key == "HKU"):
            show_key = "HKEY_USERS"
        elif(show_key == "HKCC"):
            show_key = "HKEY_CURRENT_CONFIG"
        else:
            show_key = "Something Error"

        self.material_rootkey_overview_label['text'] = show_key


        show_type = self.convType(self.material_type_combobox.get(), self.convExtension(self.material_extension_textbox.get()))
        self.material_type_overview_label['text'] = "\\" + show_type[:-1]

        show_name = self.convName(self.material_name_textbox.get())
        self.material_name_overview_label['text'] = "\\" + show_name



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
        elif(temp_type == "背景"):
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

    def convExtension(self, temp_extension):
        # 頭と尻についた空白を取り除く
        temp_extension = temp_extension.strip()
        # 2単語以上で構成されている場合最初の単語を選択する
        temp_extension = temp_extension.split(" ")[0]

        # 入力された単語の中に不適切な文字が入っていないか検証し、あれば削除する
        sym = '.\\/:*?"<>|'
        for i in range(len(sym)):
            temp_extension = temp_extension.replace(sym[i], "")
        return temp_extension

    def convName(self, temp_name):
        # 頭と尻についた空白を取り除く
        temp_name = temp_name.strip()
        # 2単語以上で構成されている場合最初の単語を選択する
        # temp_name = temp_name.split(" ")[0]

        # 入力された単語の中に不適切な文字が入っていないか検証し、あれば削除する
        sym = '.\\/:*?"<>|'
        for i in range(len(sym)):
            temp_name = temp_name.replace(sym[i], "")
        return temp_name

    def convExe(self, temp_exe):
        temp_exe = temp_exe.split("/")[-1]
        temp_exe = temp_exe.split(".")[0]
        # temp_exe = temp_exe.strip()

        return temp_exe

    def addReg(self):
        self.showSetting()
        RegistryAdd().addKey()


# レジストリの登録
class RegistryAdd():
    def dummy_addKey(self):
        # 7-zipにtestキーを追加して値「hello world」を追加する
        path = r'Software\\7-Zip\\test'

        newkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path)
        winreg.CloseKey

        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'PanelPath0', 0, winreg.REG_SZ, 'hello world')
        winreg.CloseKey(key)

    # def addKey(self):
        # pass


    def addKey(self):
        # レジストリキーを追加する
        # ここで文字列が帰ってこない 謎
        temp_reg_path = reg_type + reg_name
        # new_key = winreg.CreateKeyEx(reg_rootkey, temp_reg_path)
        # winreg.CloseKey

        print("ここです" + temp_reg_path)



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
