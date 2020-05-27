import tkinter
from tkinter import ttk
import Parse_json

class Menu2:

    def __init__(self,main_win):
        Menu2.vari = tkinter.StringVar()
        Menu2.vari.set(0)

        # menuバー
        menu_top = tkinter.Menu(main_win)
        optn = tkinter.Menu(menu_top,tearoff=0)

        main_win.configure(menu=menu_top)

        # menu 項目追加
        menu_top.add_cascade(label="確率", menu=optn, under=6)
        cnt = 0
        for L in Parse_json.get_json():
            optn.add_radiobutton(label=L, variable=Menu2.vari, value=cnt)
            cnt = cnt + 1
