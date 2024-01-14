from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    if miles.isdigit() or (miles[0] == '-' and miles[1:].isdigit()):
        miles = float(miles)
        kilometers = miles * 1.60934
        kilometres_input.delete(0, END)
        kilometres_input.insert(0, round(kilometers, 2))
    else:
        kilometres_input.delete(0, END)
        kilometres_input.insert(0, "Invalid Input")

def km_to_miles():
    kilometers = kilometres_input.get()
    if kilometers.isdigit() or (kilometers[0] == '-' and kilometers[1:].isdigit()):
        kilometers = float(kilometers)
        miles = kilometers / 1.60934
        miles_input.delete(0, END)
        miles_input.insert(0, round(miles, 2))
    else:
        miles_input.delete(0, END)
        miles_input.insert(0, "Invalid Input")

window = Tk()

window.title("Miles to Kilometres Converter")
window.minsize(width=300, height=200)

# Entry for Miles
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=0, row=0, pady=10)
miles_input = Entry()
miles_input.grid(column=0, row=1, pady=10)

# Entry for Kilometres
kilometres_label = Label(text="Kilometres", font=("Arial", 16, "bold"))
kilometres_label.grid(column=2, row=0, pady=10)
kilometres_input = Entry()
kilometres_input.grid(column=2, row=1, pady=10)

# Conversion Buttons
miles_to_km_button = Button(text="Miles to KM", command=miles_to_km)
miles_to_km_button.grid(column=0, row=2, pady=10)

km_to_miles_button = Button(text="KM to Miles", command=km_to_miles)
km_to_miles_button.grid(column=2, row=2, pady=10)

window.mainloop()


