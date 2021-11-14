import tkinter
from tkinter.constants import NW

""" LABELS:
wpop: Whistler yearly snowfall (https://www.whistler.com/weather/history/)
SPpop: Sun Peaks
SSpop: Silverstar
Revpop: Revelstoke
kickpop: Kicking Horse
louisepop: Lake Louise
SVpop: Sunshine Village
fernpop: Fernie
RMpop: Red Mountain
BWpop: Big White
"""
def genLabels(root, yearS):
    if yearS.get() == 2003:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "975 cm","sun peaks (cm)","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2004:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "685 cm","sun peaks (cm)","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2005:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1192 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2006:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1416 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2007:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1019 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2008:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "930 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2009:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1494 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2010:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1579 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2011:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1389 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2012:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1112 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2013:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "905 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2014:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "672 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2015:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1257 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2016:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1307 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2017:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1239 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2018:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "957 cm","x","x","x","x","x","x","x","x","x"
    whistler = tkinter.Label(root, text="Whistler total snowfall in {}:\n{}".format(yearS.get(),wpop), width=28, bg="red")
    whistler.place(x=833, y=66, anchor=NW)
    sunP = tkinter.Label(root, text="Sun Peaks total snowfall in {}:\n{}".format(yearS.get(),SPpop), width=28, bg="blue")
    sunP.place(x=833, y=116, anchor=NW)
    silv = tkinter.Label(root, text="SilverStar total snowfall in {}:\n{}".format(yearS.get(),SSpop), width=28, bg="red")
    silv.place(x=833, y=166, anchor=NW)
    revy = tkinter.Label(root, text="Revelstoke total snowfall in {}:\n{}".format(yearS.get(),Revpop), width=28, bg="blue")
    revy.place(x=833, y=216, anchor=NW)
    kicky = tkinter.Label(root, text="Kicking Horse total snowfall in {}:\n{}".format(yearS.get(),kickpop), width=28, bg="red")
    kicky.place(x=833, y=266, anchor=NW)
    louise = tkinter.Label(root, text="Lake Louise total snowfall in {}:\n{}".format(yearS.get(),louisepop), width=28, bg="red")
    louise.place(x=833, y=316, anchor=NW)
    SV = tkinter.Label(root, text="Sunshine Village total snowfall in {}:\n{}".format(yearS.get(),SVpop), width=28, bg="red")
    SV.place(x=833, y=366, anchor=NW)
    fernie = tkinter.Label(root, text="Fernie total snowfall in {}:\n{}".format(yearS.get(),fernpop), width=28, bg="red")
    fernie.place(x=833, y=416, anchor=NW)
    RM = tkinter.Label(root, text="Red Mountain total snowfall in {}:\n{}".format(yearS.get(),RMpop), width=28, bg="red")
    RM.place(x=833, y=466, anchor=NW)
    BW = tkinter.Label(root, text="Big White total snowfall in {}:\n{}".format(yearS.get(),BWpop), width=28, bg="red")
    BW.place(x=833, y=516, anchor=NW)
    
