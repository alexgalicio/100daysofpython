from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km_result_label.config(text=miles * 1.609)


# windows
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# text
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(pady=10, padx=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
