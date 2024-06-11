import tkinter

window = tkinter.Tk()
window.minsize(width=200, height=100)
window.title("Mile to Km Converter")
window.config(pady=20, padx=20)

entry = tkinter.Entry(width=7)
entry.grid(column=1, row=0)
entry.focus()

label_Miles = tkinter.Label(text="Miles")
label_Miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = tkinter.Label(text="0")
label_result.grid(column=1, row=1)

label_Km = tkinter.Label(text="Km")
label_Km.grid(column=2, row=1)


def convert():
    miles = float(entry.get())
    km = miles * 1.60934
    label_result.config(text=f"{km}")


button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
