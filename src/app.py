import tkinter
from tkinter import ttk
import frame
import menu


main_win = tkinter.Tk()
main_win.title("確率計算")
main_win.geometry("360x160")

main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)

# menu
menu = menu.Menu()
menu.second_init(main_win)

# frame
widget = frame.Wigets(main_frm)
widget.init_parameter()
widget.wigets()
widget.position()




# 配置決定
main_win.columnconfigure(0,weight=1)
main_win.rowconfigure(0,weight=1)
main_frm.columnconfigure(2,weight=1)

main_win.mainloop()
