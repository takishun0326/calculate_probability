import tkinter
from tkinter import ttk

class Frame2():
    def __init__(self, frm):
        self.frm = frm

        # parameters
        self.Numerator = tkinter.StringVar()
        self.Denominator = tkinter.StringVar()
        self.counter = tkinter.StringVar()
        self.btn_counter = tkinter.StringVar()
        self.result_label = tkinter.StringVar()

    def widgets(self):
        self.s = ttk.Style()
        self.s.configure('my.TButton', font = ('Helvetica',30), background='#00bfff')

        # 確率入力欄
        self.pro_label = ttk.Label(self.frm, text='確率')
        self.Numerator_box = ttk.Entry(self.frm, textvariable=self.Numerator)
        self.slash_label = ttk.Label(self.frm, text = '/')
        self.Denominator_box = ttk.Entry(self.frn, textvariable=self.Debinubatir_box)

        # widgets
