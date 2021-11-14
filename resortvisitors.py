import tkinter
from tkinter.constants import NW


def set_year(val):
    set_year.year = val
    return

# THIS IS A MESS LOL
def genPops(root, yearS):
    whistler = tkinter.Label(root, text=str(set_year.year), width=28, bg="red")
    whistler.place(x=833, y=66, anchor=NW)
    return