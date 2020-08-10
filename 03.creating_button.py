# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *

root = Tk()


 # 버튼에 기능 부여를 위한 함수작성
def myClick():
    myLabel = Label(root, text="i clicked a button.!")
    myLabel.pack()

 # Creating a button 버튼 위젯 만들기
myButton1 = Button(root, text="click me", state=DISABLED) # DISABLED로 버튼 비활성화
myButton1.pack()

myButton2 = Button(root, text="click me", padx=50,pady=30, fg="blue", bg="#000000") # padx, pady로 가로 세로 길이 지정, fg로 폰트 색상, bg로 배경 색상 지정
myButton2.pack()

myButton3 = Button(root, text="click me", command=myClick) # command로 지정함수를 기능부여함
myButton3.pack()


#myButton4 = Button(root, text='click me2') # pack이 완료된 창에서는 grid를 적용할 수 없음
#myButton4.grid(row=1,column=2)

root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
