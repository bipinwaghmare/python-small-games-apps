from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(height=300, width=500)
window.config(padx=00, pady=20)

is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

miles_label = Label(text=" Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

miles_input = Entry(width=10)
# print(miles_input.get())
miles_input.grid(column=1, row=0)

calculate_button = Button(text="Click Here", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
