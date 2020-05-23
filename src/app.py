import tkinter
from tkinter import ttk
import calc

def menu_init():
    # menuバー
    men = tkinter.Menu(main_win)
    main_win.config(menu=men)

def calc_prob_set():
    calc.calc_probability(1/4, counter_box.get())

main_win = tkinter.Tk()
main_win.title("確率計算")
main_win.geometry("360x120")

main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)


# パラメータ
input_counter = tkinter.StringVar()

# ウィジェット
counter_box = ttk.Entry(main_frm, textvariable=input_counter)
counter_box.insert(tkinter.END, "10")

counter_calc_btn = ttk.Button(main_frm, text="計算", command = calc_prob_set)



counter_box.grid(column=0,row=0, pady=10)
counter_calc_btn.grid(column=1, row=0)

# 配置
main_win.columnconfigure(0,weight=1)
main_win.rowconfigure(0,weight=1)
main_frm.columnconfigure(1,weight=1)

main_win.mainloop()
