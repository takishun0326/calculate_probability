import tkinter
from tkinter import ttk
from . import Frame1

class Frame:
    def __init__(self,main_win):
        self.main_frm = ttk.Frame(main_win)
        self.main_frm.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)

        self.Frame1()

        self.main_frm.columnconfigure(2,weight=1)


    # Frames
    def Frame1(self):
        frame1 = Frame1.Frame1(self.main_frm)
        frame1.widgets()
        frame1.position()
