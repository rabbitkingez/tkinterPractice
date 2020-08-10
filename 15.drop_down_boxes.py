# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("dropboxes")


def show():
    myLabel = Label(root, text=clicked.get()).pack() # 선택하여 받는 변수를 확인하는 방법


options = [
        "Mon","Tue","Wed","Thu","Fri","Sat"
]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options) # 선택지로 받을 리스트 앞에 * 표시
drop.pack()

myButton = Button(root, text="show selection", command=show).pack() # 선택하여 받는 변수를 확인하는 방법

root.mainloop()