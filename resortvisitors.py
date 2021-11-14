import tkinter
from tkinter.constants import NW


def genLabels(root, yearS):
    whistler = tkinter.Label(root, text=yearS.get(), width=28, bg="red")
    whistler.place(x=833, y=66, anchor=NW)
    
