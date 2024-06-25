from tkinter import *
import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import sqlite3
from ttkbootstrap.dialogs import Messagebox

location = {"a":["aa2aq.db","ac8r2z.db"],
            "b":"b.db",
            "c":["ca2cq.db","ac8r2z.db"],
            "d":"d.db",
            "e":"le.db",
            "f":"fg.db",
            "g":"fg.db",
            "h":"hn.db",
            "i":"io.db",
            "j":"jkqvw.db",
            "k":"jkqvw.db",
            "l":"le.db",
            "m":"m.db",
            "n":"hn.db",
            "o":"io.db",
            "p":["pa2pl.db","pm2pz.db"],
            "q":"jkqvw.db",
            "r":"rxyz.db",
            "s":["sa2sl.db","sm2sz.db"],
            "t":"t.db",
            "u":"u.db",
            "v":"jkqvw.db",
            "w":"jkqvw.db",
            "x":"rxyz.db",
            "y":"rxyz.db",
            "z":"rxyz.db",
            }

def find():
    deflabel1.config(text="")
    deflabel2.config(text="")
    deflabel3.config(text="")
    poslabel1.config(text="")
    poslabel2.config(text="")
    poslabel3.config(text="")
    word = inputbox.get().lower()
    if word == "":
        return
    ans= "oops"
    if len(word) == 1:
        oops  = Messagebox.ok("THAT IS NOT A WORD","ARE YOU SERIOUS?")
        return
    for item,value in location.items():
        if word[0]==item:
            loc = value
    
    if word[0] in "ac":
        seq = "abcdefghijklmnopq"
        if word[1] in seq:
            loc = loc[0]
        else:
            loc = loc[1]
    
    if word[0] in "ps":
        seq = "abcdefghijkl"
        if word[1] in seq:
            loc=loc[0]
        else:
            loc=loc[1]
    
    connection = sqlite3.connect(loc)
    c=connection.cursor()
    c.execute(f"SELECT * FROM dictionary WHERE word = '{word}'")

    lis = c.fetchmany(3)
    d1 = " "
    d2 = " "
    d3 = " "
    p1 = " "
    p2 = " "
    p3 = " "
    if len(lis) == 0:
        oops = Messagebox.ok("WORD WAS NOT FOUND.\nTRY A DIFFERNT SPELLING","WORD NOT FOUND")
    elif len(lis) == 1:
        if len(lis[0])==2:
            d1 = lis[0][1]
        elif len(lis[0])==3:
            p1 = lis[0][1].upper()
            d1 = lis[0][2]
    elif len(lis)==2:
        if len(lis[0])==2:
            d1 = lis[0][1]
        elif len(lis[0])==3:
            p1 = lis[0][1].upper()
            d1 = lis[0][2]
        if len(lis[1])==2:
            d2 = lis[1][1]
        elif len(lis[1])==3:
            p2 = lis[1][1].upper()
            d2 = lis[1][2]
    elif len(lis) == 3:
        if len(lis[0])==2:
            d1 = lis[0][1]
        elif len(lis[0])==3:
            p1 = lis[0][1].upper()
            d1 = lis[0][2]
        if len(lis[1])==2:
            d2 = lis[1][1]
        elif len(lis[1])==3:
            p2 = lis[1][1].upper()
            d2 = lis[1][2]
        if len(lis[2])==2:
            d3 = lis[2][1]
        elif len(lis[2])==3:
            p3 = lis[2][1].upper()
            d3 = lis[2][2]

    deflabel1.config(text=d1)
    deflabel2.config(text=d2)
    deflabel3.config(text=d3)
    poslabel1.config(text=p1)
    poslabel2.config(text=p2)
    poslabel3.config(text=p3)

    connection.commit()
    connection.close()

def clean():
    inputbox.delete(0,"end")
    deflabel1.config(text="")
    deflabel2.config(text="")
    deflabel3.config(text="")
    poslabel1.config(text="")
    poslabel2.config(text="")
    poslabel3.config(text="")

root = tkb.Window(themename="superhero")
root.title("Dictionary")
root.geometry("800x500")

root.minsize(800,500)
root.maxsize(850,550)

header = tkb.Frame(root)
header.place(x = 0,y=0,relheight=0.17,relwidth=1)

searchframe = tkb.Frame(root)
searchframe.place(x = 0,rely=0.17,relheight=0.2,relwidth=1)

resultframe = tkb.Frame(root)
resultframe.place(x = 0,rely=0.37,relheight=0.7,relwidth=1)


title_label = tkb.Label(header, text="DICTIONARY", font=("Times new roman", 24), bootstyle="light")
title_label.pack(pady=10)

sep = tkb.Separator(header,bootstyle = "light",orient="horizontal")
sep.pack(fill = "x",padx = 20)

searchframe.columnconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
searchframe.rowconfigure((0,1,2),weight=1)

mylabel = tkb.Label(searchframe, text="WORD:  ", bootstyle="info")
mylabel.grid(row=0,column=3,sticky="e")

inputbox = tkb.Entry(searchframe)
inputbox.grid(row =0,column=4,columnspan=2 ,sticky="we")

buttonframe = tkb.Frame(searchframe)
buttonframe.grid(row=1,column=4,rowspan=1,columnspan=2,sticky="wn")

search_button = tkb.Button(buttonframe, text="Search", bootstyle="info",command = find)
search_button.pack(side="left",padx = 13,pady=7)

clear_button = tkb.Button(buttonframe, text="Clear", bootstyle="secondary",command= clean)
clear_button.pack(side="right",padx = 1,pady=7)

defi = tkb.Notebook(resultframe,width=780,height=250)
defi.pack()

defi1 = tkb.Frame(defi)
defi2 = tkb.Frame(defi)
defi3 = tkb.Frame(defi)

poslabel1 = tkb.Label(defi1,text = " ")
poslabel1.grid(row=0,column=0,sticky="w",padx=10,pady = 20)

deflabel1= tkb.Label(defi1,text = " ", wraplength=650)
deflabel1.grid(row=1,column=0,sticky="ws",rowspan="2",padx=10,pady = 20)

poslabel2 = tkb.Label(defi2,text = " ")
poslabel2.grid(row=0,column=0,sticky="w",padx=10,pady = 20)

deflabel2= tkb.Label(defi2,text = " ", wraplength=650)
deflabel2.grid(row=1,column=0,sticky="ws",rowspan="2",padx=10,pady = 20)

poslabel3 = tkb.Label(defi3,text = " ")
poslabel3.grid(row=0,column=0,sticky="w",padx=10,pady = 20)

deflabel3= tkb.Label(defi3,text = " ", wraplength=650)
deflabel3.grid(row=1,column=0,sticky="ws",rowspan="2",padx=10,pady = 20)

defi.add(defi1,text="DEF 1")
defi.add(defi2,text="DEF 2")
defi.add(defi3,text="DEF 3")

root.mainloop()
