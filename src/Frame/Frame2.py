import tkinter
from tkinter import ttk

import sys
sys.path.append('../')

import Calc

class Frame2():
    def __init__(self, frm):
        self.frm = frm

        # parameters
        self.Numerator_par = tkinter.StringVar()
        self.Denominator_par = tkinter.StringVar()
        self.counter_par = tkinter.StringVar()
        self.btn_counter_par = tkinter.StringVar()
        self.result_label_par = tkinter.StringVar()
        self.result_box_par = tkinter.StringVar()

    def widgets(self):
        self.s = ttk.Style()
        self.s.configure('my.TButton', font = ('Helvetica',30), background='#00bfff')

        self.Numerator_par.set('1')
        self.Denominator_par.set('1')

        # 確率入力欄
        self.pro_label = ttk.Label(self.frm, text='確率')
        self.Numerator_box = ttk.Entry(self.frm, textvariable=self.Numerator_par, width=5)
        self.slash_label = ttk.Label(self.frm, text = '/')
        self.Denominator_box = ttk.Entry(self.frm, textvariable=self.Denominator_par,width=5)

        # widgets
        self.counter_label = ttk.Label(self.frm,text='回数')
        self.counter_par.set('0')
        self.counter_box = ttk.Entry(self.frm, textvariable=self.counter_par,width=15)
        self.counter_calc_btn = ttk.Button(self.frm, text="更新", command=self._counter_set,width = 6)

        # reset
        self.counter_reset_btn = ttk.Button(self.frm, text="esc",command=self._counter_reset, width = 6)

        # counter
        self.btn_counter_par.set('0')
        self.btn_counter_label = ttk.Label(self.frm, text="カウンター")
        self.btn_counter = ttk.Button(self.frm, textvariable=self.btn_counter_par, command=self._counter_cnt , style = 'my.TButton')

        # result
        self.result_label_par.set('n回までに出る確率')
        self.result_label = ttk.Label(self.frm, textvariable=self.result_label_par)
        self.result_box = ttk.Entry(self.frm, textvariable= self.result_box_par)
        self.result_box.configure(state='readonly')

    def position(self):

        self.counter_label.grid(column=0,row=1, pady=10)
        self.counter_box.grid(column=1,row=1,sticky=tkinter.W, padx=5)
        self.counter_calc_btn.grid(column=1,row=2, sticky = tkinter.NW,padx = 6)
        self.counter_reset_btn.grid(column=1,row=2, sticky = tkinter.NE, padx=6)

        self.btn_counter_label.grid(column=2,row=0, sticky = tkinter.W, padx=5)
        self.btn_counter.grid(column=2,row=1, sticky=tkinter.NSEW, rowspan=2,padx=5)

        self.result_label.grid(column=2,row=3, sticky=tkinter.W,padx=5)
        self.result_box.grid(column=2, row=4, sticky = tkinter.EW, rowspan=2, padx=5,pady=5)

        self.pro_label.grid(column=0,row=4, sticky=tkinter.W)
        self.Numerator_box.grid(column=1,row=4, sticky = tkinter.W,padx=10)
        self.slash_label.grid(column=1,row=4, padx=10)
        self.Denominator_box.grid(column=1, row=4, sticky = tkinter.E,padx=10)
    def _calc_func(self):
        if float(self.Denominator_par.get()) == 0:
            self.Denominator_par.set('1')
        if float(self.Denominator_par.get()) < 0:
            if '.' in self.Denominator_par.get():
                self.Denominator_par.set(str(float(self.Denominator_par.get()) * -1))
            else :
                self.Denominator_par.set(str(int(self.Denominator_par.get()) * -1))
        if float(self.Numerator_par.get()) < 0:
            if '.' in self.Numerator_par.get():
                self.Numerator_par.set(str(float(self.Numerator_par.get()) * -1))
            else :
                self.Numerator_par.set(str(int(self.Numerator_par.get()) * -1))

        value = 1 - float(self.Numerator_par.get())/float(self.Denominator_par.get())
        result = Calc.calc_probability(value, float(self.btn_counter_par.get()))

        # set result
        self.result_box.configure(state='nomal')
        self.result_box_par.set("{0:.10f}".format(result) + '%')
        self.result_box.configure(state='readonly')

    def _counter_set(self):
        self.btn_counter_par.set(self.counter_par.get())
        self._calc_func()
        self.result_label_par.set(self.btn_counter_par.get() + "回までに出る確率")

    def _counter_cnt(self):
        self.btn_counter_par.set(int(self.btn_counter_par.get()) + 1)
        self._calc_func()
        self.result_label_par.set(self.btn_counter_par.get() + "回までに出る確率")

    def _counter_reset(self):
        self.btn_counter_par.set('0')
        self._calc_func()
        self.result_label_par.set(self.btn_counter_par.get() + "回までに出る確率")
