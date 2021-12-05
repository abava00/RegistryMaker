import tkinter

# ウィンドウを作る
window = tkinter.Tk()
window.geometry() # サイズ設定


window.title("hello world")

winf = tkinter.Frame(window)
winf.grid(column=0, row=0, sticky=tkinter.NSEW, padx=10, pady=10) # NSEW:位置揃え, padx,y:上下、左右の余白

winlabel = tkinter.Label(winf, text="hello")


winlabel.grid(column=0, row=0, pady=10)


window.mainloop()