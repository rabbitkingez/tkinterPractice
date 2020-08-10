# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title("message box")


# showinfo : 알림 메시지, showwaring : 경고 메세지, showerror : 에러메세지, askquestion : 의견 묻기, askokcancel : ok/cancel, askyesno : yes/no
def popup():
    response = messagebox.askquestion("this is my popup", "hello world") # 알림 메세지창 띄우기, 첫번째 인자: 메시지창 제목, 두번째인자 : 창 내용
#    Label(root, text=response).pack()  # 메시지를 변수로 받아서 출력하기
    if response == "yes": # 메세지를 변수로 받아서 조건 처리
        Label(root, text="click yes").pack()

Button(root, text="popup", command=popup).pack()


root.mainloop()