from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x400")

# Craete A main frame
main_frame1 = Frame(root)
main_frame1.pack()

main_frame2 = Frame(root)
main_frame2.pack(fill=BOTH, expand=1)

my_label = Label(main_frame1, text="100").pack()

# Create A canvas
my_canvas = Canvas(main_frame2)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add ascrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))


# create another frame instide the canvas
second_frame = Frame(my_canvas)
# add new frame to a window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(100):
    Button(second_frame, text=f'Buttton {thing} yo!').grid(row=thing, column=0)



root.mainloop()