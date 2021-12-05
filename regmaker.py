import tkinter
from tkinter import ttk

# ウィンドウを作る
class MakeWindow():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry() # サイズ設定
        self.window.title("hello world")
        self.window.configure(background="#add8e6")

    # フレーム作成
    def makeFrame(self):
        self.winf = tkinter.Frame(self.window)
        self.winf.grid(column=0, row=0, sticky=tkinter.NSEW, padx=10, pady=10) # NSEW:位置揃え, padx,y:上下、左右の余白
        self.winf.configure(background="#4682b4")

    # ウィジェット作成
    def makeWidget(self):
        # ラベル
        self.material_title = tkinter.Label(self.winf, text="右クリックしたときに出る項目追加するやーつ")
        self.material_rootkey_label = tkinter.Label(self.winf, text="ルートキー設定")
        self.material_regstry_label = tkinter.Label(self.winf, text="レジストリの種類")
        self.material_extension_label = tkinter.Label(self.winf, text="対象拡張子")
        self.material_exe_label = tkinter.Label(self.winf, text="適応実行ファイル")

        # コンボボックス
        self.material_rootkey_combobox = tkinter.ttk.Combobox(self.winf, values=["ルートキー1", "ルートキー2", "ルートキー3", "ルートキー4"])
        self.material_rootkey_combobox.current(0)
        self.material_regstry_combobox = tkinter.ttk.Combobox(self.winf, values=["項目1", "項目2", "項目3", "項目4", "項目5", "項目6", "項目7",])
        self.material_regstry_combobox.current(0)


    # widget設定
    def setWidget(self):
        self.material_title.grid(column=0, row=0, pady=10)

        self.material_rootkey_label.grid(column=0, row=1, pady=10)
        self.material_rootkey_combobox.grid(column=2, row=1, pady=10)

        self.material_regstry_label.grid(column=0, row=2, pady=10)

        self.material_extension_label.grid(column=0, row=3, pady=10)

        self.material_exe_label.grid(column=0, row=4)

    # 表示
    def showWindow(self):

        self.window.mainloop()



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
