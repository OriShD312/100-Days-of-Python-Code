from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import FontDialog

# my function that opens the font dialog window and sets the test_label font according to chosen parameters
def open_font_dialog_window():
    fd = FontDialog()
    fd.show()
    test_label.config(font=fd.result)

# main window
window = tb.Window(themename='superhero')
window.title('Image Watermark')
window.geometry('1500x800')

# label with random text for testing of FontDialog
test_label = Label(window, text='Sample Text')
test_label.pack()

# font dialog window open from button
font_button = Button(window, text='Choose Font', command=open_font_dialog_window)
font_button.pack()

window.mainloop()