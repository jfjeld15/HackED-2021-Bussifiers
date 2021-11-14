import tkinter

x = tkinter.Tk()
x.title("Snow Map")
funnydog = tkinter.PhotoImage(file="./funydog.png")
butty = tkinter.Button(x, activebackground="aquamarine3", image=funnydog, text="WORDS")
butty.pack()
x.mainloop()