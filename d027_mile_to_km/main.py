from tkinter import *

FONT = ("Arial", 16, "normal")

def mile_to_km():
    res = round(float(miles_input.get()) * 1.609344, 2)
    return res

def button_clicked():
    km_output.config(text=mile_to_km())

window = Tk()
window.title("Miles to Km calculator")
# window.minsize(width= 300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

mile_label = Label(text="mile(s)", font=FONT)
mile_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

km_output = Label(text="0", font=FONT)
km_output.grid(column=1, row=1)

km_label = Label(text="km", font=FONT)
km_label.grid(column=2, row=1)

button = Button(text="calculate", command=button_clicked)
button.grid(column=2, row=2)




window.mainloop()