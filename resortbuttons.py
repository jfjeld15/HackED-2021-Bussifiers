import tkinter
from tkinter.constants import CENTER
import webbrowser

def genButts(root, baseC):  # Generate Buttons
    whistler = tkinter.Button(root, bg="gold", command=open_whistler)  # Whistler
    baseC.create_window(105,498, height=13, width=13, anchor=CENTER, window=whistler)

    sunPeak = tkinter.Button(root, bg="gold", command=open_sunPeak)  # Sun Peaks
    baseC.create_window(362,404, height=13, width=13, anchor=CENTER, window=sunPeak)

    kicky = tkinter.Button(root, bg="gold", command=open_kicky)  # Kicking Horse
    baseC.create_window(599,345, height=13, width=13, anchor=CENTER, window=kicky)

    louise = tkinter.Button(root, bg="gold", command=open_louise)  # Lake Louise
    baseC.create_window(671,324, height=13, width=13, anchor=CENTER, window=louise)

    revy = tkinter.Button(root, bg="gold", command=open_revy)  # Revelstoke
    baseC.create_window(508,393, height=13, width=13, anchor=CENTER, window=revy)

    sunsh = tkinter.Button(root, bg="gold", command=open_sunsh)  # Sunshine
    baseC.create_window(706,365, height=13, width=13, anchor=CENTER, window=sunsh)

    sStar = tkinter.Button(root, bg="gold", command=open_sStar)  # SilverStar
    baseC.create_window(433,473, height=13, width=13, anchor=CENTER, window=sStar)

    bWhite = tkinter.Button(root, bg="gold", command=open_bWhite)  # Big White
    baseC.create_window(445,556, height=13, width=13, anchor=CENTER, window=bWhite)

    redMtn = tkinter.Button(root, bg="gold", command=open_redMtn)  # Red Mtn
    baseC.create_window(541,636, height=13, width=13, anchor=CENTER, window=redMtn)

    fernie = tkinter.Button(root, bg="gold", command=open_fernie)  # Fernie
    baseC.create_window(773,579, height=13, width=13, anchor=CENTER, window=fernie)
    return

def open_whistler():  # Whistler
    webbrowser.open_new_tab("https://www.whistlerblackcomb.com/")
    return

def open_sunPeak():  # Sun Peaks
    webbrowser.open_new_tab("https://www.sunpeaksresort.com/")
    return

def open_kicky():  # Kicking Horse
    webbrowser.open_new_tab("https://kickinghorseresort.com/")
    return

def open_louise():  # Lake Louise
    webbrowser.open_new_tab("https://www.skilouise.com/")
    return

def open_revy():  # Revelstoke
    webbrowser.open_new_tab("https://www.revelstokemountainresort.com/")
    return

def open_sunsh():  # Sunshine
    webbrowser.open_new_tab("https://www.skibanff.com/")
    return

def open_sStar():  # SilverStar
    webbrowser.open_new_tab("https://www.skisilverstar.com/")
    return

def open_bWhite():  # Big White
    webbrowser.open_new_tab("https://www.bigwhite.com/")
    return

def open_redMtn():  # Red Mtn
    webbrowser.open_new_tab("https://www.redresort.com/")
    return

def open_fernie():  # Fernie
    webbrowser.open_new_tab("https://skifernie.com/")
    return

