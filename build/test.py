from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar

def calculate(*args):
    try:
        value = float(entry_var.get())
        result_var.set(f"Result: {value * 2}")  # Example calculation
    except ValueError:
        result_var.set("Invalid input")

window = Tk()
window.geometry("400x200")
window.configure(bg="#F4EEEE")

entry_var = StringVar()
entry_var.trace_add("write", calculate)

entry = Entry(window, textvariable=entry_var, font=("Outfit", 14))
entry.place(x=50, y=50, width=200, height=30)

result_var = StringVar()
result_label = Label(window, textvariable=result_var, font=("Outfit", 14), bg="#F4EEEE")
result_label.place(x=50, y=100)

window.mainloop()
