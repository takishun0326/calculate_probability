import tkinter
from tkinter import ttk

from . import Frame1
from . import Frame2

class Frame:
    def __init__(self,main_win):

        # ノートブック
        nb = ttk.Notebook(main_win)
        nb.grid(column=0, row=0,sticky=tkinter.NSEW, padx=5, pady=5)

        # make tabs
        self.frame1 = ttk.Frame(nb)
        self.frame2 = ttk.Frame(nb)

        nb.add(self.frame1, text='カウンター', padding=3)
        nb.add(self.frame2, text='テスト', padding=3)

        self.Frame1()
        self.Frame2()

        self.frame1.columnconfigure(2,weight=1)
        self.frame2.columnconfigure(2,weight=1)


    # Frames
    def Frame1(self):
        frame1 = Frame1.Frame1(self.frame1)
        frame1.widgets()
        frame1.position()

    def Frame2(self):
        frame2 = Frame2.Frame2(self.frame2)
