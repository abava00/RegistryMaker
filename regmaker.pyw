import os
import random
import winreg
import subprocess
import tkinter
from tkinter import Widget, ttk
from tkinter import filedialog

#参考
# https://itasuke.hatenablog.com/entry/2018/01/08/133510



# 宣言
str_rootkey = "" # 使用するルートキー
str_type = "" # 適応するレジストリの位置
str_registry = "" # レジストリの型(?)の種類
str_extension = "" # 対象拡張指名
str_exe = "" # 実行ファイルpath
str_name = "Default" # キーの名前
str_description = "" # 右クリックしたときに出るメニューの名前
str_shortcut = "" # ショートカット

reg_rootkey = winreg.HKEY_CLASSES_ROOT # 使用するルートキー
reg_type = "test type" # 適応するレジストリの位置
reg_registry = "" # レジストリの型(?)の種類
reg_extension = "" # 対象拡張指名
reg_exe = "" # 実行ファイルpath
reg_name = "Default"# キーの名前
reg_description = "" # 右クリックしたときに出るメニューの名前
reg_shortcut = "" # ショートカット

version = "0.1"

path = os.getcwd()
lnker = f'{path}\\lnkmaker.vbs'

# ウィンドウを作る
class MakeWindow():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry() # サイズ設定
        self.window.title("RegistryMaker ver." + version)
        self.window.resizable(width= False, height= False)
        self.path_exe_file = ""
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

        if(random.randint(0,10) != 5):
            self.material_system = tkinter.Label(self.winf, text= "試作版　試作版　試作版　試作版")
        else:
            self.material_system = tkinter.Label(self.winf, text= "BIG'B' IS WATCHING YOU")
        self.material_system.configure(foreground= '#fd7e00' ,background= '#4682b4')
        # self.material_title = tkinter.Label(self.winf,width= 50, height= 100, text= "右クリックしたときに出る項目追加するやーつ")
        self.material_rootkey_label = tkinter.Label(self.winf, text= "ルートキー設定")
        self.material_registry_label = tkinter.Label(self.winf, text= "レジストリの種類")
        self.material_type_label = tkinter.Label(self.winf, text = "対象項目")
        self.material_type_label.configure(foreground='#b22222')
        self.material_exe_label = tkinter.Label(self.winf, text = "適応実行ファイル")
        self.material_exe_label.configure(foreground='#b22222')
        self.material_extension_label = tkinter.Label(self.winf, text = "対象拡張指名")
        self.material_extension_label.configure(foreground='#c0c0c0')
        self.material_space_label = tkinter.Label(self.winf, text= " ")
        self.material_space_label.configure(background= '#4682b4')
        self.material_name_label = tkinter.Label(self.winf, text= "キーの名称")
        self.material_name_label.configure(foreground='#b22222')
        self.material_description_label = tkinter.Label(self.winf, text= "右クリックで出る説明")
        self.material_description_label.configure(foreground='#b22222')
        self.material_shortcut_label = tkinter.Label(self.winf, text= "ショートカットの設定")

         #選択によって表示されるレジストリキーのパスを出力するラベル
        self.material_overview_label = tkinter.Label(self.winf, text= "　　　生成されるキー　　　")
        self.material_rootkey_overview_label = tkinter.Label(self.winf, text= "")
        self.material_rootkey_overview_label.bind("<Button-1>", self.clickLabel)
        self.material_registry_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_type_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_type_overview_label.bind("<Button-1>", self.clickLabel)
        self.material_exe_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_overview2_label = tkinter.Label(self.winf, text= "　　　生成されるデータ　　　")
        self.material_name_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_name_overview_label.bind("<Button-1>", self.clickLabel)
        self.material_description_overview_label = tkinter.Label(self.winf, text= " ")
        self.material_shortcut_overview_label = tkinter.Label(self.winf, text= " ")

        # コンボボックス
        self.material_rootkey_combobox = tkinter.ttk.Combobox(self.winf, values=["HKCR", "HKCU", "HKLM", "HKU", "HKCC"])
        self.material_rootkey_combobox.configure(state= "readonly")
        self.material_rootkey_combobox.current(1)
         # (展開可能)文字列値以外のデータの生成に失敗している
        # self.material_registry_combobox = tkinter.ttk.Combobox(self.winf, values=["文字列値", "バイナリ値", "DWORD(32bit)値", "QWORD(64bit)値", "複数行文字列値", "展開可能な文字列値", "キー",])
        self.material_registry_combobox = tkinter.ttk.Combobox(self.winf, values=["文字列値","展開可能な文字列値"])
        self.material_registry_combobox.configure(state= "readonly")
        self.material_registry_combobox.current(0)
         # デスクトップでの右クリックメニューの変更を確認できなかった
        # self.material_type_combobox = tkinter.ttk.Combobox(self.winf, values=["デスクトップ","フォルダ背景", "フォルダ", "ファイル", "特殊フォルダ", "特定拡張子"])
        self.material_type_combobox = tkinter.ttk.Combobox(self.winf, values=["フォルダ背景", "フォルダ", "ファイル", "特殊フォルダ", "特定拡張子", "スタートメニュー"])
        self.material_type_combobox.bind('<<ComboboxSelected>>', self.selectType) # コンボボックスが変更されたときに発生するイベント
        self.material_type_combobox.configure(state= "readonly")
        self.material_type_combobox.current(2)

        # テキストボックス
        self.material_extension_textbox = tkinter.ttk.Entry(self.winf)
        self.material_extension_textbox.insert(0, "*")
        self.material_extension_textbox.configure(state= "readonly", foreground= '#c0c0c0')
        self.material_name_textbox = tkinter.ttk.Entry(self.winf)
        self.material_description_textbox = tkinter.ttk.Entry(self.winf)
        self.material_shortcut_textbox = tkinter.ttk.Entry(self.winf)

        # ボタン
        self.material_exe_button = tkinter.ttk.Button(self.winf, text= "参照", command= self.choiceExeFile)
        self.material_exe_button.bind('<Return>', lambda event: self.choiceExeFile())
        self.material_add_button = tkinter.ttk.Button(self.winf, text= "レジストリ追加", command= self.addData)
        self.material_add_button.bind('<Return>', lambda event: self.addData())

         # 概要表示ボタン
        self.material_overview_button = tkinter.ttk.Button(self.winf, text= "レジストリキーを確認", command= self.showOverview)
        self.material_overview_button.bind('<Return>', lambda event: self.showOverview())




    # widget設定
    def setWidget(self):
        self.material_title.grid(column= 0, row= 0, columnspan= 5, padx= 10, pady= 10, sticky= tkinter.W + tkinter.E)
        self.material_system.grid(column=0, row=1, columnspan= 3, sticky= tkinter.W + tkinter.E)

        self.material_space_label.grid(column= 1, row=1, rowspan= 8, padx=1)
        self.material_space_label.grid(column= 3, row=1, rowspan= 8, padx=1)

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

        self.material_description_label.grid(column= 0, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_description_textbox.grid(column= 2, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_description_overview_label.grid(column= 4, row= 7, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)

        self.material_shortcut_label.grid(column= 0, row= 8, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_shortcut_textbox.grid(column= 2, row= 8, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_shortcut_overview_label.grid(column= 4, row= 8, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)

        self.material_exe_label.grid(column= 0, row= 9, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_exe_button.grid(column= 2, row= 9, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_exe_overview_label.grid(column= 4, row= 9, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)

        self.material_add_button.grid(column= 0, row= 10, columnspan= 3, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)
        self.material_overview_button.grid(column= 4, row= 10, padx= 2, pady= 5, sticky= tkinter.W + tkinter.E)





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
        # 多分event引数を用いた賢い書き方があると思うの
         # 特定拡張子を選択した場合
        if(self.material_type_combobox.get() == "特定拡張子"):
            self.material_extension_textbox.delete(0, tkinter.END)
            self.material_extension_textbox.configure(state= "normal", foreground= '#000000')
            self.material_extension_label.configure(foreground='#000000')
        else:
            self.material_extension_textbox.delete(0, tkinter.END)
            self.material_extension_textbox.insert(0, "*")
            self.material_extension_textbox.configure(state= "readonly", foreground= '#c0c0c0')
            self.material_extension_label.configure(foreground='#c0c0c0')

         # スタートメニューを選択した場合
        if(self.material_type_combobox.get() == "スタートメニュー"):
             # 設定できない項目の除外
            self.material_rootkey_label.configure(foreground='#c0c0c0')
            self.material_rootkey_combobox.configure(foreground='#c0c0c0')
             # Registryコンボボックスの項目名、内容の変更
            self.material_registry_label['text']= "登録する場所"
            self.material_registry_label.configure(foreground='#b22222')
            self.material_registry_combobox['values'] = ("上","中","下")
            self.material_registry_combobox.configure(state= "readonly")
            self.material_registry_combobox.current(0)
             # 概要ラベルの設定変更
            self.material_overview_label['text'] = "ショートカットを作成する場所"
             # 名前ラベルの設定変更
            self.material_name_label['text'] = "ショートカットの名称"

        else:
            self.material_rootkey_label.configure(foreground='#000000')
            self.material_rootkey_combobox.configure(foreground='#000000')
            self.material_name_label.configure(foreground='#b22222')

            self.material_registry_combobox['values'] = ("文字列値","展開可能な文字列値")
            self.material_registry_label.configure(foreground='#000000')
            self.material_registry_combobox.configure(state= "readonly")
            self.material_registry_combobox.current(0)
            self.material_registry_label['text'] = "レジストリの種類"

            self.material_name_label['text'] = "キーの名称"

            self.material_overview_label['text'] = "　　　生成されるキー　　　"

    def clickLabel(self, event):

        subwin = tkinter.Tk()
        subwin.geometry("630x130")
        subwin.title("予測される生成キーPATH")

        temp_massage = self.showOverview()

        path = tkinter.ttk.Entry(subwin)
        path.place(x = 10, y = 10, width=600, height=100)
        path.insert(0, temp_massage[0])

        if(self.material_type_combobox.get() == "スタートメニュー"):
            subprocess.call(['explorer.exe', temp_massage[0]])



    # 設定項目の確認
    def showSetting(self):
        global str_rootkey
        global str_type
        global str_registry
        global str_extension
        global str_exe
        global str_name
        global str_description
        global str_shortcut

        global reg_rootkey
        global reg_type
        global reg_registry
        global reg_extension
        global reg_exe
        global reg_name
        global reg_description
        global reg_shortcut

        # str_registry = self.material_registry_combobox.get()
        reg_registry = self.convRegistry(self.material_registry_combobox.get())
        # str_extension = self.material_extension_textbox.get()
        reg_extension = self.convExtension(self.material_extension_textbox.get())

        # ファイルを参照していない場合での例外処理があるとうれしくなる
        str_exe = self.path_exe_file
        reg_exe = self.convExe(self.path_exe_file)
        # reg_exe = str_exe
        # str_rootkey = self.material_rootkey_combobox.get()
        reg_rootkey = self.convRootkey(self.material_rootkey_combobox.get())
        # str_type = self.material_type_combobox.get()
        reg_type = self.convType(self.material_type_combobox.get(), self.convExtension(self.material_extension_textbox.get()))

        # str_name = self.convName(self.material_name_textbox.get())
        reg_name = self.convName(self.material_name_textbox.get())
        reg_description = self.convDescription(self.material_description_textbox.get())

        reg_shortcut = self.convShortcut(self.material_shortcut_textbox.get())
        if(reg_shortcut == "定義できませんでした"):
            reg_shortcut = ""


        print(f'ルートキー(rootkey) is {self.material_rootkey_combobox.get()}')
        print(f'対象項目(type) is {self.material_type_combobox.get()}')
        print(f'キー名称(name) is {self.material_name_textbox.get()}')
        print(f'拡張子(extension) is {self.material_extension_textbox.get()}')
        print(f'レジストリ種類(registry) is {self.material_registry_combobox.get()}')
        print(f'右クリック時説明(description)is {self.material_description_textbox.get()}')
        print(f'ショートカット(shortcut)is {self.material_shortcut_textbox.get()}')
        print(f'実行ファイルpath(exePATH) is {str_exe}\n')

        print(f'ルートキー(rootkey) is {reg_rootkey}')
        print(f'対象項目(type) is {reg_type}')
        print(f'キー名称(name) is {reg_name}')
        print(f'拡張子(extension) is {reg_extension}')
        print(f'レジストリ種類(registry) is {reg_registry}')
        print(f'右クリック時説明(description)is {reg_description}')
        print(f'ショートカット(shortcut)is {reg_shortcut}')
        print(f'実行ファイルpath(exePATH) is {reg_exe}\n')

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



        show_type = self.convType(self.material_type_combobox.get(), self.convExtension(self.material_extension_textbox.get()))

        if(not self.convName(self.material_name_textbox.get())):
            show_name = str_name
        else:
            show_name = self.convName(self.material_name_textbox.get())

        show_reg = self.material_registry_combobox.get()
        if(show_reg == "文字列値"):
            show_reg = "REG_SZ"
        elif(show_reg == "バイナリ値"):
            show_reg = "REG_BINARY"
        elif(show_reg == "DWORD(32bit)値"):
            show_reg = "REG_DWORD"
        elif(show_reg == "QWORD(64bit)値"):
            show_reg = "REG_QWORD"
        elif(show_reg == "複数行文字列値"):
            show_reg = "REG_MULTI_SZ"
        elif(show_reg == "展開可能な文字列値"):
            show_reg = "REG_EXPAND_SZ"
        elif(show_reg == "キー"):
            show_reg = "よぐわがんない"

        elif(show_reg == "上"):
            show_reg = "Group3"
        elif(show_reg == "中"):
            show_reg = "Group2"
        elif(show_reg == "下"):
            show_reg = "Group1"

        show_description = self.convDescription(self.material_description_textbox.get())

        show_shortcut = self.convShortcut(self.material_shortcut_textbox.get())
        if(self.material_shortcut_textbox.get() == "" and self.material_shortcut_textbox.get() == ""):
            show_shortcut = ""
        show_exe = self.convExe(self.path_exe_file)

        show_full = ['keyPATH', 'regDATA', 'regNUMBER', 'commandNAME', 'commandEXE']
        show_full[0] = show_key + show_type + show_name
        show_full[1] = show_reg
        show_full[2] = show_description
        show_full[3] = show_shortcut
        show_full[4] = show_exe

        # 出力
        self.material_rootkey_overview_label['text'] = show_key
        self.material_type_overview_label['text'] = "\\" + show_type[:-1]
        self.material_name_overview_label['text'] = "\\" + show_name
        self.material_registry_overview_label['text'] = show_reg
        self.material_description_overview_label['text'] = show_description
        self.material_shortcut_overview_label['text'] = show_shortcut
        self.material_exe_overview_label['text'] = show_exe

        # C:\Users\abava\AppData\Local\Microsoft\Windows\WinX\Group3
        if(self.material_type_combobox.get() == "スタートメニュー"):
            show_key = os.path.expanduser('~')
            show_type = f"\\AppData\\Local\\Microsoft\\Windows\\WinX"
            self.material_rootkey_overview_label['text'] = show_key
            self.material_type_overview_label['text'] = show_type
            self.material_name_overview_label['text'] = f"\\{show_reg}"
            self.material_registry_overview_label['text'] = show_name
            # self.material_registry_overview_label['text'] = " "
            show_full = ['keyPATH', 'regDATA', 'regNUMBER', 'commandNAME', 'commandEXE']
            show_temp = show_name
            show_name = f"\\{show_reg}"
            show_reg = show_temp
            show_full[0] = show_key + show_type + show_name
            show_full[1] = show_reg
            show_full[2] = show_description
            show_full[3] = show_shortcut
            show_full[4] = show_exe

        return show_full



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
        else:
            temp_key = "Something Error (in rootkey)"
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

         # スタートメニューの場合
        elif(temp_reg == "上"):
            temp_reg = "Group3"
        elif(temp_reg == "中"):
            temp_reg = "Group2"
        elif(temp_reg == "下"):
            temp_reg = "Group1"
        else:
            temp_reg = "Something Error(in registry type) "
        return temp_reg


    def convType(self, temp_type, temp_extension):
        if(temp_type == "デスクトップ"):
            temp_type = "Software\\Classes\\DesktopBackground\\"
        elif(temp_type == "フォルダ背景"):
            temp_type = "Software\\Classes\\Directory\\Background\\shell\\"
        elif(temp_type == "フォルダ"):
            temp_type = "Software\\Classes\\Directory\\shell\\"
        elif(temp_type == "ファイル"):
            temp_type = "Software\\Classes\\*\\shell\\"
        elif(temp_type == "特殊フォルダ"):
            temp_type = "Software\\Classes\\Folder\\shell\\"
        elif(temp_type == "特定拡張子"):
            temp_type = f"Software\\Classes\\SystemFileAssociations\\.{temp_extension}\\shell\\"
        elif(temp_type == "スタートメニュー"):
            temp_type = f"StartMenu\\"
        else:
            temp_type = "Something Error (in right click menu)"
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
        temp_name = temp_name.strip() # 2単語以上で構成されている場合最初の単語を選択する
        # temp_name = temp_name.split(" ")[0]


        if (not self.material_name_textbox.get()):
            temp_name = str_name
        else:
            # print("処理前のtemp_name は" + temp_name)
            # 入力された単語の中に不適切な文字が入っていないか検証し、あれば削除する
            sym = '.\\/:*?"<>|'
            for i in range(len(sym)):
                temp_name = temp_name.replace(sym[i], "")

        return temp_name

    def convExe(self, temp_exe):
        temp_exe = temp_exe.replace('/', '\\')

        return temp_exe

    def convDescription(self, temp_description):
        sym = '.\\/:*?"<>|&'
        for i in range(len(sym)):
            temp_description = temp_description.replace(sym[i], "")

        return temp_description

    def convShortcut(self, temp_shortcut):
        temp_shortcut = temp_shortcut.strip()
        temp_shortcut = temp_shortcut.split(" ")[0]

        sym = '.\\/:*?"<>|&'
        for i in range(len(sym)):
            temp_shortcut = temp_shortcut.replace(sym[i], "")

        if(not temp_shortcut):
            return "定義できませんでした"
        temp_shortcut = list(temp_shortcut)[0]

        return f'&{temp_shortcut}'


    def addData(self):
        self.showSetting()


        if (self.confirmationWindow()):

            if(self.material_type_combobox.get() == "スタートメニュー"):
                DataAdd().addlnk()
                # DataAdd().dummy_addlnk()
            else:
                DataAdd().addKey()
                # DataAdd().dummy_addKey()
                # print("True")
                return
        # print("false")

        return

    def confirmationWindow(self):
        temp = self.showOverview()
        if(self.material_type_combobox.get() == "スタートメニュー"):
            return True
        else:
            if(self.path_exe_file == ""):
                tkinter.messagebox.showerror("エラー", "多分 実行ファイルが選択されていません\n")
                return False

            # 確認ダイアログ表示
            window_message = tkinter.messagebox.askyesno('確認', f'レジストリキー: \n{temp[0]}　に\n型: {temp[1]}　で\nデータ: {temp[2]}　を\n登録しますか？')
            return window_message



# レジストリの登録
class DataAdd():
    def dummy_addKey(self):
        print("Finish")


    def addKey(self):


        # レジストリキーを追加する
        temp_reg_path = reg_type + reg_name

        temp_data = ""
        if(reg_shortcut == ""):
            temp_data = f'{reg_description}'
        temp_data = f'{reg_description} ({reg_shortcut})'

        with winreg.CreateKeyEx(reg_rootkey, temp_reg_path) as key:
            name = None
            # 展開可能文字列値でないとダメっぽい? 大丈夫っぽいぞ？
            winreg.SetValueEx(key, name, 0, reg_registry, temp_data)
            name = "icon"
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, reg_exe)

        temp_reg_path += f'\\command'
        temp_exe_path = f'"{reg_exe}" "%V"'
        with winreg.CreateKeyEx(reg_rootkey, temp_reg_path) as key:
            name = None
            winreg.SetValueEx(key, name, 0, reg_registry, temp_exe_path)

        # print(temp_data)
        # print(reg_exe)




        # key = winreg.OpenKeyEx(reg_rootkey, temp_reg_path, access=winreg.KEY_WRITE)
        # 文字列値と展開可能な文字列値のみ読み取ることができた、バイナリ値などは対応を調べる
        # winreg.SetValueEx(key, 'test', 0, reg_registry, temp_reg_exe)
        # winreg.CloseKey(key)

    def addlnk(self):


        temp_root = os.path.expanduser('~')
        temp_path = f"\\AppData\\Local\\Microsoft\\Windows\\WinX"
        lnk_path = temp_root + temp_path + f"\\{reg_registry}"
        lnk_exe = reg_exe
        lnk_name = reg_name
        lnk_shortcut = reg_shortcut.split('&')[-1]
        lnk_description = reg_description

        subprocess.call(['explorer.exe', lnk_path])

        # ショートカットを作成する処理(できませんでした)
        # subprocess.call([lnker, lnk_exe, lnk_path, lnk_name, lnk_description, lnk_shortcut], shell= True)

        return


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
