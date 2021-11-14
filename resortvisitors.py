import tkinter
from tkinter.constants import LEFT, NW


def year(val):  # Gets the year from the slider
    year = print(str(val))
    return year


def genPops(root, yearS, year):
    whistler = tkinter.Label(root, text="Total visitors in {}:\n{}".format(year,6), width=28, bg="red")
    whistler.place(x=833, y=66, anchor=NW)
    return