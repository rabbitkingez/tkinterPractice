# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *

root = Tk()


 # Creating a label widget 라벨 위젯 만들기
myLabel1 = Label(root, text="hello world")#.grid(row=0, column=0) 도 가능함
myLabel2 = Label(root, text="my name is jihwan")
myLabel3 = Label(root, text="what your name")


 # Shoving it onto the screen 위젯을 화면에 열과 행을 기준으로 띄우기
 # 행과 열은 상대적임
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=0, column=1)



root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
