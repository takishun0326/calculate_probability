import tkinter
from tkinter import ttk
import calc
import parse_json
import menu

class Wigets:
    def __init__(self, main_frm):
        self.main_frm = main_frm

    def init_parameter(self):
    # パラメータ
        self.input_counter = tkinter.StringVar()
        self.btn_counter = tkinter.StringVar()
        self.result_counter = tkinter.StringVar()
        self.result_label_txt = tkinter.StringVar()

    def wigets(self):
        self.s = ttk.Style()
        self.s.configure('my.TButton', font=('Helvetica', 30),background="#00bfff")

        # Label
        self.cnt_label = ttk.Label(self.main_frm, text="回数")


        # ウィジェット
        self.counter_box = ttk.Entry(self.main_frm,width=15, textvariable=self.input_counter)
        self.counter_box.insert(tkinter.END, "0")
        self.counter_calc_btn = ttk.Button(self.main_frm, text="値の更新", command = self.counter_set)

        # リセット
        self.counter_reset_btn = ttk.Button(self.main_frm, text ="リセット", command = self.counter_reset)

        # カウンター
        self.btn_counter.set(0)
        self.counter_label = ttk.Label(self.main_frm, text="カウンター")
        self.counter_btn = ttk.Button(self.main_frm, textvariable=self.btn_counter, command = self.counter_cnt, style='my.TButton')


        # calc result
        self.result_label_txt.set("0回までに出る確率")
        self.result_label = ttk.Label(self.main_frm, textvariable=self.result_label_txt)
        self.result_box = ttk.Entry(self.main_frm,textvariable=self.result_counter)
        self.result_box.configure(state='readonly')

    def position(self):
        # 配置
        self.cnt_label.grid(column=0, row=0, pady=10)
        self.counter_box.grid(column=1,row=0,sticky=tkinter.W,padx=5)
        self.counter_calc_btn.grid(column=1, row=1, sticky = tkinter.W)
        self.counter_reset_btn.grid(column=1,row=2, sticky=tkinter.W,pady=5)

        self.counter_label.grid(column=2,row=0, sticky=tkinter.W, padx = 5)
        self.counter_btn.grid(column=2, row=1, sticky=tkinter.NSEW, rowspan=2, padx=5)
        self.result_label.grid(column=2, row=5, sticky=tkinter.W, padx=5)
        self.result_box.grid(column=2, row=6, sticky=tkinter.NSEW, rowspan=2, pady=5, padx=5)

    def calc_func(self):
        # calc pow 1-(up/down)^n
        updown = 1- parse_json.get_json_value(int(menu.Menu.vari.get()))
        calc_result = calc.calc_probability(updown, float(self.btn_counter.get()))
        # set result
        self.result_box.configure(state='nomal')
        self.result_counter.set("{0:.10f}".format(calc_result) + '%')
        self.result_box.configure(state='readonly')

    def counter_set(self):
        self.btn_counter.set(self.input_counter.get())
        self.calc_func()
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")


    def counter_reset(self):
        self.btn_counter.set('0')
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")


    def counter_cnt(self):
        self.btn_counter.set(str(int(self.btn_counter.get()) + 1))
        self.calc_func()
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")
