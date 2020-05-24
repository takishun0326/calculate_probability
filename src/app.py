import tkinter
from tkinter import ttk
import calc

Option_List_up = ["1","1","1","1","1","1"]
Option_List_down = ["2", "8","10","100","1024","4096"]

def calc_func():
    # calc pow 1-(up/down)^n
    updown = 1-float(Option_List_up[int(vari.get())]) / float(Option_List_down[int(vari.get())])
    calc_result = calc.calc_probability(updown, float(btn_counter.get()))
    # set result
    result_box.configure(state='nomal')
    result_counter.set(str(calc_result) + '%')
    result_box.configure(state='readonly')


def counter_set():
    btn_counter.set(input_counter.get())
    calc_func()
    result_label_txt.set(btn_counter.get() + "回までに出る確率")


def counter_reset():
    btn_counter.set('0')
    result_label_txt.set(btn_counter.get() + "回までに出る確率")


def counter_cnt():
    btn_counter.set(str(int(btn_counter.get()) + 1))
    calc_func()
    result_label_txt.set(btn_counter.get() + "回までに出る確率")




main_win = tkinter.Tk()
main_win.title("確率計算")
main_win.geometry("360x160")

main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)


# パラメータ
vari = tkinter.StringVar()
input_counter = tkinter.StringVar()
btn_counter = tkinter.StringVar()
result_counter = tkinter.StringVar()
result_label_txt = tkinter.StringVar()


# menuバー
vari.set(0)
menu_top = tkinter.Menu(main_win)
menu_probability_optn = tkinter.Menu(menu_top,tearoff=0)

main_win.configure(menu=menu_top)

# menu 項目追加
menu_top.add_cascade(label="確率", menu=menu_probability_optn, under=6)
for L in range(len(Option_List_up)):
    menu_probability_optn.add_radiobutton(label=Option_List_up[L]+"/"+Option_List_down[L], variable=vari, value=L)




# https://stackoverflow.com/questions/37068708/how-to-change-font-size-in-ttk-button
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 30),background="#00bfff")


# Label
cnt_label = ttk.Label(main_frm, text="回数")


# ウィジェット
counter_box = ttk.Entry(main_frm,width=15, textvariable=input_counter)
counter_box.insert(tkinter.END, "0")
counter_calc_btn = ttk.Button(main_frm, text="値の更新", command = counter_set)

# リセット
counter_reset_btn = ttk.Button(main_frm, text ="リセット", command = counter_reset)

# カウンター
btn_counter.set(0)
counter_label = ttk.Label(main_frm, text="カウンター")
counter_btn = ttk.Button(main_frm, textvariable=btn_counter, command = counter_cnt, style='my.TButton')


# calc result
result_label_txt.set("0回までに出る確率")
result_label = ttk.Label(main_frm, textvariable=result_label_txt)
result_box = ttk.Entry(main_frm,textvariable=result_counter)
result_box.configure(state='readonly')





# 配置
cnt_label.grid(column=0, row=0, pady=10)
counter_box.grid(column=1,row=0,sticky=tkinter.W,padx=5)
counter_calc_btn.grid(column=1, row=1, sticky = tkinter.W)
counter_reset_btn.grid(column=1,row=2, sticky=tkinter.W,pady=5)

counter_label.grid(column=2,row=0, sticky=tkinter.W, padx = 5)
counter_btn.grid(column=2, row=1, sticky=tkinter.NSEW, rowspan=2, padx=5)
result_label.grid(column=2, row=5, sticky=tkinter.W, padx=5)
result_box.grid(column=2, row=6, sticky=tkinter.NSEW, rowspan=2, pady=5, padx=5)

# 配置決定
main_win.columnconfigure(0,weight=1)
main_win.rowconfigure(0,weight=1)
main_frm.columnconfigure(2,weight=1)

main_win.mainloop()
