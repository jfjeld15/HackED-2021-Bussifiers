import tkinter as tk
import os
from tkinter.constants import NW

def initWindow(root):  # Create base window
    root.title("Bussifiers' Ski Trip Planner")
    earthmap = tk.PhotoImage(file="./images/rockylabels.png")
    baseC = tk.Canvas(root, width=833, height=766)
    baseC.pack()
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    root.mainloop()
    return

if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    initWindow(root)