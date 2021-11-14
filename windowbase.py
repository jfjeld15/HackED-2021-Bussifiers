import tkinter as tk
from tkinter.constants import NW
import resortbuttons as rb


def initWindow(root):  # Create base window
    root.title("Bussifiers' Ski Trip Planner")

    earthmap = tk.PhotoImage(file="./images/rockylabels.png")
    marker = tk.PhotoImage(file="./images/marker.png")

    baseC = tk.Canvas(root, width=833, height=766)  # Canvas dimensions are the image dimensions
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    rb.genButts(root, baseC, marker)  # Uses module resortbuttons to generate buttons that link resort websites
    baseC.pack()
    root.mainloop()
    return

if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    initWindow(root)
    