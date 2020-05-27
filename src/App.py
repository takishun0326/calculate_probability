import tkinter
from tkinter import ttk
from Frame import Frame
from Menu import Menu

if __name__ == '__main__':

    main_win = tkinter.Tk()
    main_win.title("確率計算")
    main_win.geometry("360x200")

    # Menu
    menu = Menu.Menu(main_win)

    # Frame
    frame = Frame.Frame(main_win)


    # 配置決定
    main_win.columnconfigure(0,weight=1)
    main_win.rowconfigure(0,weight=1)

    main_win.mainloop()
