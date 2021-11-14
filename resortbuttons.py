import tkinter
from tkinter.constants import CENTER
import webbrowser

def genButts(root, baseC, marker):  # Generate Buttons
    whistler = tkinter.Button(root, bg="gold", command=open_whistler)  # Whistler
    baseC.create_window(105,498, anchor=CENTER, window=whistler)

    sunPeak = tkinter.Button(root, bg="gold", command=open_sunPeak)  # Sun Peaks
    baseC.create_window(362,404, height=13, width=13, anchor=CENTER, window=sunPeak)
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

def open_sun():  # Sunshine
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

