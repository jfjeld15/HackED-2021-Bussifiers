import tkinter as tk
from tkinter.constants import NW, CENTER
import resortbuttons as rb


def initWindow(root):  # Create base window
    root.title("Bussifiers' Ski Trip Planner")
    earthmap = tk.PhotoImage(file="./images/rockylabels.png")
    baseC = tk.Canvas(root, width=833, height=766)  # Canvas dimensions are the image dimensions
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    genButts(root, baseC)
    baseC.pack()
    root.mainloop()
    return

def genButts(root, baseC):  # Generate Buttons
    whistler = tk.Button(root, bg="black", command=rb.open_whistler)
    baseC.create_window(105,498, width=11,height=9, anchor=CENTER, window=whistler)
    return

if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    baseC = initWindow(root)
    