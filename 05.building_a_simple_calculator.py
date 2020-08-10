# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:41:59 2020

@author: Rabbitking
"""

from tkinter import *

root = Tk()
root.title("simple calculator") # title method로 창제목 지정


e = Entry(root, width=35, bg='blue', fg='white', borderwidth=5) # borderwidth로 테두리 두께 조정
e.grid(row=0,column=0, columnspan=3) # columnspan으로 열병합 처리

global f_num
global calculation


def button_click(number):
#    e.delete(0,END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0,END)
    
def button_add():
    global f_num
    global calculation
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)
    calculation = "add"

def button_substract():
    global f_num
    global calculation
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)
    calculation = "substract"

def button_multiply():
    global f_num
    global calculation
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)
    calculation = "multiply"

def button_division():
    global f_num
    global calculation
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)
    calculation = "division"



def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if calculation == "add":
        e.insert(0, f_num + int(second_number))
    elif calculation == "substract":
        e.insert(0, f_num - int(second_number))
    elif calculation == "multiply":
        e.insert(0, f_num * int(second_number))
    elif calculation == "division":
        e.insert(0, f_num / int(second_number))
    else:
        print("this is error")


# define buttons

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click("0"))

buttonAdd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonEqual = Button(root, text="=", padx=90, pady=20, command=button_equal)
buttonClear = Button(root, text="Clear", padx=80, pady=20, command=button_clear)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
buttonDivision = Button(root, text="/", padx=40, pady=20, command=button_division)
buttonSubstract = Button(root, text="-", padx=40, pady=20, command=button_substract)


# put the button on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)

buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonMultiply.grid(row=6, column=0)
buttonDivision.grid(row=6, column=1)
buttonSubstract.grid(row=6, column=2)

root.mainloop() # 프로그램을 꺼지지 않게 무한 반복
