import tkinter
from tkinter import ttk

from . import Menu2

class Menu:
    def __init__(self,main_win):
        self.main_win = main_win

        self.Menu2()

    def Menu1(self):
        pass

    def Menu2(self):
        Menu2.Menu2(self.main_win)
