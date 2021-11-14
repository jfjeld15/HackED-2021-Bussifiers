import tkinter as tk
import os
from tkinter.constants import NW, CENTER
import resortbuttons as rb


def initWindow(root):  # Create base window
    root.title("Bussifiers' Ski Trip Planner")
    earthmap = tk.PhotoImage(file="./images/rockylabels.png")
    baseC = tk.Canvas(root, width=833, height=766)  # Canvas dimensions are the image dimensions
    baseC.pack()
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    root.mainloop()
    return(baseC)  # Return canvas for future use


if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    baseC = initWindow(root)
    rb.genButts(baseC)