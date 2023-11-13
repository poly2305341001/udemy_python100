# import tkinter
import tkinter
from tkinter import *


def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


# TODO: Window class
# window = tkinter.Tk()
window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=50, pady=50)


# TODO: Label class
# my_label = tkinter.Label(text="I am a label", font=("consolas", 24, "normal"))
my_label = Label(text="Text", font=("Arial", 25, "bold"))
# my_label.pack(side="left")
my_label["text"] = "New text"
my_label.config(text="New text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# TODO: Button class
# button = tkinter.Button()
button = Button(text='Click me!', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
button.config(padx=20, pady=20)


# TODO: Entry class
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


new_button = Button(text="New button")
new_button.grid(column=2, row=0)




window.mainloop()
