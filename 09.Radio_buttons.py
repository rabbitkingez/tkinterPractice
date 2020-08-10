# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("radio buttons")

r = IntVar() #  tkinter variable
r.set("2")


MODES = [
        
        ("pepperoni","pepperoni"),
        ("cheese","cheese"),
        ("mushroom","mushroom"),
        ("onion","onion")
        ]


pizza = StringVar()
pizza.set("pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="click", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()