# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *

root = Tk()




myLabel = Label(root, text="enter your name")
myLabel.pack()



# 사용자 입력을 받는 Entry 위젯 생성
e = Entry(root, width=100, bg='blue', fg='white', borderwidth=5) # borderwidth로 테두리 두께 조정
e.pack()
e.insert(0,"enter your name...") # insert로 기본 입력 문구 지정



def myClick():
    hello = "hello " + e.get() # Entry의 get method를 통해 받은 입력값을 가지고 온다
    myLabel = Label(root, text=hello) 
    myLabel.pack()


myButton = Button(root, text="ok", command=myClick)
myButton.pack()

root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
