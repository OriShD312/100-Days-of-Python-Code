from tkinter import filedialog, colorchooser
from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
from ttkbootstrap.dialogs.dialogs import FontDialog

# Constants
# FONT_SIZES = [10, 12, 14, 16, 18, 20, 24, 36, 48, 72]
# FONTS = ['Helvetica', 'Arial', ]

# function that opens dialog window to locate image + resizes it to 720p and updates label to show it
def browse_open_image():
    global img
    fileTypes = [('Image Files', '*.png;*.jpg;*.jpeg')]
    image_path = filedialog.askopenfilename(title='Browse for Image', filetypes=fileTypes)

    if image_path:
        img = ImageTk.PhotoImage(Image.open(image_path).resize((1280,720)))
        label.config(image=img, bg='black')

    else:
        print('No file was chosen, please choose a file')

# function that uses remove bg feature
def remove_img_bg():
    pass

# function that reads font size combo box input and updates font size value
# def set_font_size_option(e):
#     font_size = font_size_option.get()
#     print(font_size)

# function that uses FontDialog to set font parameters
def open_font_dialog_window():
    fd = FontDialog()
    fd.show()
    test_label.config(font=fd.result)
    
# main window
window = tb.Window(themename='superhero')
window.title('Image Watermark')
window.geometry('1500x800')

# notebook to hold each frame
my_notebook = tb.Notebook(window)
my_notebook.pack(side=LEFT)

# frames to hold buttons and features
watermark_frame = Frame(my_notebook)
my_notebook.add(watermark_frame, text='Add Text to Image')

remove_bg_frame = Frame(my_notebook)
my_notebook.add(remove_bg_frame, text='Remove Background')

# label that will hold the image
label = Label(window)
label.pack(side=RIGHT)

# button that will open dialog window to locate image
browse_open_image_button = Button(watermark_frame, text='Browse for Image', command=browse_open_image)
browse_open_image_button.pack()

# font size combo box
# font_size_option = tb.Combobox(watermark_frame, values=FONT_SIZES, width=5)
# font_size_option.current(4)
# font_size_option.bind('<<ComboboxSelected>>', set_font_size_option)
# font_size_option.pack()

test_label = Label(watermark_frame, text='Sample Text')
test_label.pack()

# different option - font dialog window open from button
font_button = Button(watermark_frame, text='Choose Font', command=open_font_dialog_window)
font_button.pack()

# button that will remove bg from image
remove_bg_button = Button(remove_bg_frame, text='Remove Image Background', command=remove_img_bg)
remove_bg_button.pack()

# start app
window.mainloop()
 
# TODO: create GUI that includes:
# TODO: button to browse for wanted image + function √ 
# TODO: button to save image after watermark addition 
# TODO: font type drop down menu
# TODO: font size choice with drop down menu and/or increase/decrease buttons
# TODO: font color option with color wheel
# TODO: font opacity (alpha) parameter choice (using number between 0-1)
# TODO: option to drag text around + rotate (depends on difficulty)
# TODO: reset to default button (depends on difficulty)
# TODO: save user choices as default (?)
# TODO: batch image upload (?)
# TODO: add remove background feature in a separate tab using tb.Notebook
