# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title("creating windows")

def open():
    top = Toplevel()
    top.title("second windows")
    global my_image  # 함수 내에서는 이미지를 불러오기 위해서 Global 변수로 변경해야 함
    my_image = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray1.jpg"))
    label = Label(top, text="hello world", image=my_image).pack()
    button2 = Button(top, text="close window", command=top.destroy).pack()

button = Button(root, text="open second windows", command=open).pack()





root.mainloop()