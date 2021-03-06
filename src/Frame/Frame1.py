import tkinter
from tkinter import ttk
import sys
sys.path.append('../')

import Calc
import Parse_json
from Menu import Menu2

class Frame1:
    def __init__(self, main_frm):
        self.main_frm = main_frm
    # パラメータ
        self.input_counter = tkinter.StringVar()
        self.btn_counter = tkinter.StringVar()
        self.result_counter = tkinter.StringVar()
        self.result_label_txt = tkinter.StringVar()


    def widgets(self):
        self.s = ttk.Style()
        self.s.configure('my.TButton', font=('Helvetica', 30),background="#00bfff")

        # Label
        self.cnt_label = ttk.Label(self.main_frm, text="回数")

        # ウィジェット
        self.counter_box = ttk.Entry(self.main_frm,width=15, textvariable=self.input_counter)
        self.counter_box.insert(tkinter.END, "0")
        self.counter_calc_btn = ttk.Button(self.main_frm, text="更新", command = self._counter_set,width=6)

        # リセット
        self.counter_reset_btn = ttk.Button(self.main_frm, text ="esc", command = self._counter_reset,width=6)

        # カウンター
        self.btn_counter.set(0)
        self.counter_label = ttk.Label(self.main_frm, text="カウンター")
        self.counter_btn = ttk.Button(self.main_frm, textvariable=self.btn_counter, command = self._counter_cnt, style='my.TButton')


        # calc result
        self.result_label_txt.set("0回までに出る確率")
        self.result_label = ttk.Label(self.main_frm, textvariable=self.result_label_txt)
        self.result_box = ttk.Entry(self.main_frm,textvariable=self.result_counter)
        self.result_box.configure(state='readonly')

    def position(self):
        # 配置
        self.cnt_label.grid(column=0, row=1, pady=10)
        self.counter_box.grid(column=1,row=1,sticky=tkinter.W,padx=5)
        self.counter_calc_btn.grid(column=1, row=2, sticky = tkinter.NW,padx=6)
        self.counter_reset_btn.grid(column=1,row=2, sticky=tkinter.NE,padx=6)

        self.counter_label.grid(column=2,row=0, sticky=tkinter.W, padx = 5)
        self.counter_btn.grid(column=2, row=1, sticky=tkinter.NSEW, rowspan=2, padx=5)
        self.result_label.grid(column=2, row=5, sticky=tkinter.W, padx=5)
        self.result_box.grid(column=2, row=6, sticky=tkinter.NSEW, rowspan=2, pady=5, padx=5)


    def _calc_func(self):
        # calc pow 1-(up/down)^n
        updown = 1- Parse_json.get_json_value(int(Menu2.Menu2.vari.get()))
        calc_result = Calc.calc_probability(updown, float(self.btn_counter.get()))
        # set result
        self.result_box.configure(state='nomal')
        self.result_counter.set("{0:.10f}".format(calc_result) + '%')
        self.result_box.configure(state='readonly')

    def _counter_set(self):
        self.btn_counter.set(self.input_counter.get())
        self._calc_func()
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")


    def _counter_reset(self):
        self.btn_counter.set('0')
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")


    def _counter_cnt(self):
        self.btn_counter.set(str(int(self.btn_counter.get()) + 1))
        self._calc_func()
        self.result_label_txt.set(self.btn_counter.get() + "回までに出る確率")
