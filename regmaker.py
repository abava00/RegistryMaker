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
        self.material_rootkey_combobox = tkinter.ttk.Combobox(self.winf, values=["ルートキー1", "ルートキー2", "ルートキー3", "ルートキー4"])
        self.material_rootkey_combobox.configure(state= "readonly")
        self.material_rootkey_combobox.current(0)
        self.material_registry_combobox = tkinter.ttk.Combobox(self.winf, values=["項目1", "項目2", "項目3", "項目4", "項目5", "項目6", "項目7",])
        self.material_registry_combobox.configure(state= "readonly")
        self.material_registry_combobox.current(0)
        self.material_type_combobox = tkinter.ttk.Combobox(self.winf, values=["右クリック1", "右クリック2", "右クリック3", "特定拡張子"])
        self.material_type_combobox.bind('<<ComboboxSelected>>', self.selectCombobox) # コンボボックスが変更されたときに発生するイベント
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


    # コンボボックス選択時に動作する
    def selectCombobox(self, event):
        if(self.material_type_combobox.get() == "特定拡張子"):
            self.material_extension_textbox.configure(state= "normal")
        else:
            self.material_extension_textbox.configure(state= "readonly")


    # 設定項目の確認
    def showSetting(self):

        str_rootkey = self.material_rootkey_combobox.get()
        str_type = self.material_type_combobox.get()
        str_registry = self.material_registry_combobox.get()
        # ここに例外処理がほしい
        str_extension = self.material_extension_textbox.get()
        str_exe = self.path_exe_file



        print(f'rootkey is {str_rootkey}')
        print(f' type is {str_type}')
        print(f'registry is {str_registry}')
        print(f'extension is {str_extension}')
        print(f' exefile is {str_exe}')





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
