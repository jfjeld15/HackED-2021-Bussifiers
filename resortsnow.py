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
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "300 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2004:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "130 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2005:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "139 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2006:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "275 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2007:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "260 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2008:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "169 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2009:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "148 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2010:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "363 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2011:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "137 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2012:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "343 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2013:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "74 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2014:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "160 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2015:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "338 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2016:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "189 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2017:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "133 cm","x","x","x","x","x","x","x","x","x"
    elif yearS.get() == 2018:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "373 cm","x","x","x","x","x","x","x","x","x"
    whistler = tkinter.Label(root, text="Whistler snowfall in Dec. {}:\n{}".format(yearS.get(),wpop), width=28, bg="red")
    whistler.place(x=833, y=66, anchor=NW)
    sunP = tkinter.Label(root, text="Sun Peaks snowfall in Dec. {}:\n{}".format(yearS.get(),SPpop), width=28, bg="blue")
    sunP.place(x=833, y=116, anchor=NW)
    silv = tkinter.Label(root, text="SilverStar snowfall in Dec. {}:\n{}".format(yearS.get(),SSpop), width=28, bg="red")
    silv.place(x=833, y=166, anchor=NW)
    revy = tkinter.Label(root, text="Revelstoke snowfall in Dec. {}:\n{}".format(yearS.get(),Revpop), width=28, bg="blue")
    revy.place(x=833, y=216, anchor=NW)
    kicky = tkinter.Label(root, text="Kicking Horse snowfall in Dec. {}:\n{}".format(yearS.get(),kickpop), width=28, bg="red")
    kicky.place(x=833, y=266, anchor=NW)
    louise = tkinter.Label(root, text="Lake Louise snowfall in Dec. {}:\n{}".format(yearS.get(),louisepop), width=28, bg="red")
    louise.place(x=833, y=316, anchor=NW)
    SV = tkinter.Label(root, text="Sunshine Village snowfall in Dec. {}:\n{}".format(yearS.get(),SVpop), width=28, bg="red")
    SV.place(x=833, y=366, anchor=NW)
    fernie = tkinter.Label(root, text="Fernie snowfall in Dec. {}:\n{}".format(yearS.get(),fernpop), width=28, bg="red")
    fernie.place(x=833, y=416, anchor=NW)
    RM = tkinter.Label(root, text="Red Mountain snowfall in Dec. {}:\n{}".format(yearS.get(),RMpop), width=28, bg="red")
    RM.place(x=833, y=466, anchor=NW)
    BW = tkinter.Label(root, text="Big White snowfall in Dec. {}:\n{}".format(yearS.get(),BWpop), width=28, bg="red")
    BW.place(x=833, y=516, anchor=NW)
    
