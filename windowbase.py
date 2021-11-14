import tkinter as tk
from tkinter.constants import HORIZONTAL, NW
import resortbuttons as rb
import resortsnow as rs


def initWindow(root):  # Create base window
    def printyear():
        rs.genLabels(root, yearS)  # Uses module resortsnow to generate labels in window
        root.after(200, printyear)  # Update the labels every 200ms
        return


    def show_elev(x):  # Button press, overlay gradient
        baseC.create_image(0,0, anchor=NW, image=grad_plt)
        return
    

    def hide_elev(x):  # Button release, overlay original map
        baseC.create_image(0, 0, anchor=NW, image=earthmap)
        return


    root.title("Bussifiers' Ski Trip Planner")
    earthmap = tk.PhotoImage(file="./images/rockylabels.png")  # Define window title and images
    grad_plt = tk.PhotoImage(file="./images/grad_plt_trans.png")

    baseC = tk.Canvas(root, width=1033, height=766)  # Canvas dimensions are the image dimensions
    yearS = tk.Scale(root, from_=2011, to=2019, orient=HORIZONTAL, width=20, length=200)  # Slider for yearly snowfall data
    baseC.create_image(0, 0, anchor=NW, image=earthmap)
    elev = tk.Button(root, bg="lime", text="Show Elevation Map")  # Elevation Gradient Reveal Button
    baseC.create_window(833,566, width=200, height=200, anchor=NW, window=elev)
    elev.bind("<ButtonPress-1>",show_elev)
    elev.bind("<ButtonRelease-1>",hide_elev)
    rb.genButts(root, baseC)  # Uses module resortbuttons to generate buttons that link resort websites
    yearS.place(x=833, y=0, anchor=NW)
    baseC.pack()
    root.after(200, printyear)
    root.mainloop()

if __name__== "__main__":  # Main function
    root = tk.Tk()  # Create base window "root" using built-in tkinter module
    initWindow(root)
