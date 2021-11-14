import tkinter
from tkinter.constants import CENTER
import webbrowser

def genButts(root, baseC):  # Generate Buttons
    whistler = tkinter.Button(root, bg="black", command=open_whistler)
    baseC.create_window(105,498, width=11,height=9, anchor=CENTER, window=whistler)
    return

def open_whistler():
    webbrowser.open_new_tab("https://www.whistlerblackcomb.com/")
    return
