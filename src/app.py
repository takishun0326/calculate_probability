import tkinter
from tkinter import ttk
import Frame1
import Menu2

if __name__ == '__main__':

    main_win = tkinter.Tk()
    main_win.title("確率計算")
    main_win.geometry("360x160")

    main_frm = ttk.Frame(main_win)
    main_frm.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)

    # menu
    menu = Menu2.Menu2(main_win)

    # frame
    frame1 = Frame1.Frame1(main_frm)
    frame1.widgets()
    frame1.position()




    # 配置決定
    main_win.columnconfigure(0,weight=1)
    main_win.rowconfigure(0,weight=1)
    main_frm.columnconfigure(2,weight=1)

    main_win.mainloop()
