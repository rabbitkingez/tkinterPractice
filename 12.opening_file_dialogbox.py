# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title("open file dialog box")


def openImage():
    global my_image
    route=root.filename = filedialog.askopenfilename(initialdir="d://", title="select a file", filetypes=(("jpg files", "*.jpg"), ("all files","*.*")))
    label = Label(root, text=route).pack()
    my_image = ImageTk.PhotoImage(Image.open(route))
    my_image_label = Label(image=my_image).pack()

button = Button(root,text="open image",command=openImage).pack()

root.mainloop()