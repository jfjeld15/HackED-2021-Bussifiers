import tkinter
import webbrowser
from tkinter.constants import CENTER, NW

def open_link1():
    canvo2=tkinter.Canvas(x,width=100,height=100,bg="black")
    canvo.create_window(100,100,anchor=CENTER, window=canvo2)
    webbrowser.open_new_tab("https://www.whistlerblackcomb.com/")
    return

x = tkinter.Tk()
x.title("Snow Map")
funnydog = tkinter.PhotoImage(file="./funydog.png")
canvo = tkinter.Canvas(x, width=900, height=900)
canvo.create_image(0,0,anchor=NW, image=funnydog)
butty = tkinter.Button(x,bg="red",command=open_link1)
canvo.create_window(390,110, width=10,height=10, anchor=CENTER, window=butty)
canvo.pack()
x.mainloop()
