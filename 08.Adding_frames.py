# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("adding frame")


# 프레임의 생성
frame = LabelFrame(root, text="my frame", padx=5, pady=5) # 프레임에서 내부 오브젝트까지의 거리 자종
frame.pack(padx=10, pady=10) # 바깥창에서 프레임까지의 거리 지정

b = Button(frame, text="don't click")
b.grid(row=0,column=0)

b2 = Button(frame, text="click")
b2.grid(row=1,column=0)



root.mainloop()