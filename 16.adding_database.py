# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 07:06:36 2020

@author: Rabbitking
"""

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("using database")


# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table

c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zopcode integer
        )""")





# Commit Changes
conn.commit()


# Clase Connection
conn.close()

root.mainloop()