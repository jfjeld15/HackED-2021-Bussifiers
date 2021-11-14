from tkinter import * 
import time
from time import sleep

ws = Tk()
ws.title('HackEDbeta 2021')
ws.geometry('496x187+100+100')
ws.config(bg='#345')

on_off_label = Label(ws, font=("Helvetica", 20))
on_off_label.place(x = 180, y = 82)

buttonState = 'ON'

def toggleState():
    global buttonState
    print(time.asctime()+'  toggling...')
    if buttonState == 'ON':
        on_off_label.config(bg = '#000FFF000', text = " ON")
        buttonState = 'OFF'
    else:
        on_off_label.config(bg = '#FFF000000', text = "OFF")
        buttonState = 'ON'
    ws.after(1000, toggleState)

#
# Run forever...
#
ws.after(1000, toggleState)
ws.mainloop()