# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program_miles to km converter")
window.minsize(width=300, height=200)
window.config(padx=20,pady=50)

#label
is_equal_to = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0,row=1)
is_equal_to.config(padx=10,pady=10)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2,row=0)

km_string = Label(text="Km", font=("Arial", 12, "bold"))
km_string.grid(column=2,row=1)

km = Label(text="0", font=("Arial", 12, "bold"))
km.grid(column=1,row=1)
#Button
def button_clicked():
    new_miles = float(input.get())
    output = str(new_miles * 1.60934)
    km.config(text=output)

button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)

#Entry
input = Entry(width= 10)
input.grid(column=1,row=0)


window.mainloop()