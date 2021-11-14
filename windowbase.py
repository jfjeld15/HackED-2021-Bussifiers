import tkinter as tk
from tkinter.constants import HORIZONTAL, NW
import resortbuttons as rb
import resortvisitors as rv


def initWindow(root):  # Create base window
    root.title("Bussifiers' Ski Trip Planner")

    earthmap = tk.PhotoImage(file="./images/rockylabels.png")

    baseC = tk.Canvas(root, width=1033, height=766)  # Canvas dimensions are the image dimensions
    yearS = tk.Scale(root, from_=2000, to=2018, orient=HORIZONTAL, width=20, length=200)  # Slider for yearly pop. data
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    rb.genButts(root, baseC)  # Uses module resortbuttons to generate buttons that link resort websites
    yearS.place(x=833, y=0, anchor=NW)
    ###########rv.genPops(root, yearS)  # Uses module resortvisitors to generate visitor populations based on slider
    baseC.pack()
    root.mainloop()
    return

if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    initWindow(root)
    