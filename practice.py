

from tkinter import *

# object and method
window = Tk()

window.title("My First Gui Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.grid(column=1, row=0, pady=15)  # Top center


def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=6, pady=20)  # Middle,

new_button = Button(text="New Button")
new_button.grid(column=1, row=7, pady=10)

input = Entry()
input.grid(column=1, row=3, pady=15)  # Below the button

# keeps window open
window.mainloop()
