# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *

root = Tk()



myLabel = Label(root, text="hello world") # 라벨 위젯 만들기
myLabel.pack() # 라벨 위젯을 화면에 표시




root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
