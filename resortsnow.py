import tkinter
from tkinter.constants import NW

""" LABELS:
wpop: Whistler yearly snowfall (https://www.onthesnow.com/british-columbia/whistler-blackcomb/historical-snowfall)
SPpop: Sun Peaks (https://www.onthesnow.com/british-columbia/sun-peaks/historical-snowfall)
SSpop: Silverstar (https://www.onthesnow.com/british-columbia/silver-star/ski-resort)
Revpop: Revelstoke (https://www.onthesnow.com/british-columbia/revelstoke-mountain/historical-snowfall)
kickpop: Kicking Horse (https://www.onthesnow.com/british-columbia/kicking-horse/historical-snowfall)
louisepop: Lake Louise (https://www.onthesnow.com/alberta/lake-louise/historical-snowfall)
SVpop: Sunshine Village (https://www.onthesnow.com/alberta/sunshine-village/historical-snowfall)
fernpop: Fernie (https://www.onthesnow.com/british-columbia/fernie-alpine/historical-snowfall)
RMpop: Red Mountain (https://www.onthesnow.com/british-columbia/red-resort/historical-snowfall)
BWpop: Big White (https://www.onthesnow.com/british-columbia/big-white/historical-snowfall)
"""
def genLabels(root, yearS):
    if yearS.get() == 2011:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "711","414","406","485","376","467","531","754","353","1379"
    elif yearS.get() == 2012:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "696","437","366","561","561","757","688","787","290","424"
    elif yearS.get() == 2013:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "556","386","376","549","498","465","429","544","391","508"
    elif yearS.get() == 2014:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1105","545","643","724","518","338","574","688","620","927"
    elif yearS.get() == 2015:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "1283","932","630","638","569","544","759","960","335","810"
    elif yearS.get() == 2016:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "803","467","574","615","617","737","762","919","841","861"
    elif yearS.get() == 2017:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "950","277","432","470","480","505","442","701","348","579"
    elif yearS.get() == 2018:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "749","414","386","531","447","536","686","643","297","630"
    elif yearS.get() == 2019:
        wpop,SPpop,SSpop,Revpop,kickpop,louisepop,SVpop,fernpop,RMpop,BWpop = "714","178","203","551","384","445","754","523","312","404"
    whistler = tkinter.Label(root, text="Whistler total snowfall in {}:\n{} cm".format(yearS.get(),wpop), width=28, bg="gray")
    whistler.place(x=833, y=66, anchor=NW)
    sunP = tkinter.Label(root, text="Sun Peaks total snowfall in {}:\n{} cm".format(yearS.get(),SPpop), width=28, bg="gray")
    sunP.place(x=833, y=116, anchor=NW)
    silv = tkinter.Label(root, text="SilverStar total snowfall in {}:\n{} cm".format(yearS.get(),SSpop), width=28, bg="gray")
    silv.place(x=833, y=166, anchor=NW)
    revy = tkinter.Label(root, text="Revelstoke total snowfall in {}:\n{} cm".format(yearS.get(),Revpop), width=28, bg="gray")
    revy.place(x=833, y=216, anchor=NW)
    kicky = tkinter.Label(root, text="Kicking Horse total snowfall in {}:\n{} cm".format(yearS.get(),kickpop), width=28, bg="gray")
    kicky.place(x=833, y=266, anchor=NW)
    louise = tkinter.Label(root, text="Lake Louise total snowfall in {}:\n{} cm".format(yearS.get(),louisepop), width=28, bg="gray")
    louise.place(x=833, y=316, anchor=NW)
    SV = tkinter.Label(root, text="Sunshine Village total snowfall in {}:\n{} cm".format(yearS.get(),SVpop), width=28, bg="gray")
    SV.place(x=833, y=366, anchor=NW)
    fernie = tkinter.Label(root, text="Fernie total snowfall in {}:\n{} cm".format(yearS.get(),fernpop), width=28, bg="gray")
    fernie.place(x=833, y=416, anchor=NW)
    RM = tkinter.Label(root, text="Red Mountain total snowfall in {}:\n{} cm".format(yearS.get(),RMpop), width=28, bg="gray")
    RM.place(x=833, y=466, anchor=NW)
    BW = tkinter.Label(root, text="Big White total snowfall in {}:\n{} cm".format(yearS.get(),BWpop), width=28, bg="gray")
    BW.place(x=833, y=516, anchor=NW)
    
