# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title("slider")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


my_button =Button(root, text="click", command=slide).pack()

root.mainloop()