import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter.constants import NW

root = tk.Tk()


earthmap = tk.PhotoImage(file="./rocky.png")
canvas = tk.Canvas(root, width=1779, height=1691)


canvas.pack()

canvas.create_image(0, 0, anchor=NW, image = earthmap)


root.mainloop()

