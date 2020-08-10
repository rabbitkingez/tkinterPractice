# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icons,images,exit buttons") # title method로 창제목 지정
root.iconbitmap("C://Users//Rabbitking//Anaconda3//Lib//site-packages//conda//shell//conda_icon.ico") # 창 아이콘 변경하기


 # 이미지를 변수로 먼저 담고, 그 변수를 다시 레이블에 담아서 표시함
my_image1 = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray1.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray3.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray4.jpg"))
my_image5 = ImageTk.PhotoImage(
        Image.open("D://mantaray//mantaray5.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("D://mantaray//mantaray6.jpg"))

image_list=[my_image1,my_image2, my_image3,my_image4,my_image5,my_image6]

status = Label(root, text="image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_next
    global button_back
    my_label.forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    status = Label(root, text="image" + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    
    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_next
    global button_back 
    my_label.forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="exit", command=root.destroy)
button_forward = Button(root, text=">>", command=lambda: forward(2))



button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=10)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)




#button_quit=Button(root, text="exit", command=root.destroy) # 종료 시키기
#button_quit.pack()



root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
