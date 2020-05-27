import tkinter
from tkinter import ttk
import parse_json

class Menu:


    def second_init(self,main_win):
        Menu.vari = tkinter.StringVar()
        Menu.vari.set(0)

        # menuバー
        menu_top = tkinter.Menu(main_win)
        menu_probability_optn = tkinter.Menu(menu_top,tearoff=0)

        main_win.configure(menu=menu_top)

        # menu 項目追加
        menu_top.add_cascade(label="確率", menu=menu_probability_optn, under=6)
        cnt = 0
        for L in parse_json.get_json():
            menu_probability_optn.add_radiobutton(label=L, variable=Menu.vari, value=cnt)
            cnt = cnt + 1
