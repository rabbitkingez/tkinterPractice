# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("checkboxes")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="wanna supersize?", variable=var, onvalue= "supersize", offvalue="regularsize") #선택과 미선택 시 값을 부여
c.deselect() # 기본 설정을 미설정으로 지정하며, 없을 시 아무 값도 가지지 않은 상태로 출력됨(버그)
c.pack()


mybutton = Button(root, text="show selection", command=show).pack()

root.mainloop()