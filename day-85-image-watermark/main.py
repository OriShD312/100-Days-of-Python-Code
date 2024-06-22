from tkinter import filedialog, messagebox
from ttkbootstrap import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from ttkbootstrap.dialogs.dialogs import FontDialog
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
from rembg import *

class App(Window):
    def __init__(self, style):
        super().__init__(themename=style)
        self.text_font = ('Arial', 24)
        self.text_color = '#FFFFFF'
        self.title('test')
        self.geometry('1570x990')

        my_style = Style()
        my_style.configure('my.TButton', font=('Arial', 24))

        self.image_history = [] # list that holds image states for undo function

        # create two tab notebook, one for watermark addition and another for background removal
        self.my_notebook = Notebook(self)
        self.my_notebook.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=NS)
        
        self.configure_grid()

        self.image_label = Label(self)
        self.image_label.grid(row=0, column=2, rowspan=3, pady=10)

        # general buttons
        self.browse_for_image_button = Button(self, text='Browse', command=self.browse_for_image)
        self.browse_for_image_button.grid(row=1, column=0, sticky=EW, padx=10, pady=(0, 10))

        self.save_image_button = Button(self, text='Save', command=self.save_image)
        self.save_image_button.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky=EW)

        self.undo_button = Button(self, text='Undo Last Action', command=self.undo_action)
        self.undo_button.grid(row=2, column=0, padx=10, pady=(0,10), sticky=EW, columnspan=2)

        # Frame
        self.customization_tab = Frame(self.my_notebook)
        self.my_notebook.add(self.customization_tab, text='Customize Your Image')

        # Labels
        self.user_text_label = Label(self.customization_tab, text='Your text here:')
        self.user_text_label.grid(row=0, column=0, padx=10, pady=10)

        self.text_opacity = Scale(self.customization_tab)
        self.text_opacity.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Entries
        self.user_text = Entry(self.customization_tab)
        self.user_text.grid(row=0, column=1, padx=10, pady=10, sticky=EW)
                
        # Buttons
        self.open_font_dialog_window_button = Button(self.customization_tab, text='Open Font Settings', command=self.open_font_dialog_window)
        self.open_font_dialog_window_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.open_color_chooser_window_button = Button(self.customization_tab, text='Open Font Color Settings', command=self.open_color_chooser_window)
        self.open_color_chooser_window_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.add_text_button = Button(self.customization_tab, text='Add Text to Image', command=self.add_text_to_image)
        self.add_text_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.remove_bg_button = Button(self.customization_tab, text='Remove Image Background', command=self.remove_bg)
        self.remove_bg_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.rotate_image_counter_clockwise_button = Button(self.customization_tab, text='↪', style='my.TButton', command=lambda: self.rotate_image(90))
        self.rotate_image_counter_clockwise_button.grid(row=6, column=0, padx=10, pady=10)

        self.rotate_image_clockwise_button = Button(self.customization_tab, text='↩', style='my.TButton', command=lambda: self.rotate_image(-90))
        self.rotate_image_clockwise_button.grid(row=6, column=1, padx=10, pady=10)

    def add_text_to_image(self):
        self.watermark = Label(self, text=self.user_text.get(),
                          font=self.text_font,
                          foreground=self.text_color,
                          )
        self.watermark.grid(row=0, column=2, padx=10, pady=10)
        self.make_draggable(self.watermark)
        
    def open_font_dialog_window(self):
        fd = FontDialog()
        fd.show()
        self.text_font = fd.result

    def browse_for_image(self):
        global img, pic, img_size
        fileTypes = [('Image Files', '*.png;*.jpg;*.jpeg')]
        image_path = filedialog.askopenfilename(title='Browse for Image', filetypes=fileTypes)

        if image_path:
            img = Image.open(image_path)
            img_ratio = img.size[0]/img.size[1]
            if img_ratio >= 1:
                img_size = 1280, round(1280/img_ratio)
                img = img.resize(size=img_size)
            else:
                img_size = round(1280/img_ratio), 1280
                img = img.resize(size=img_size)
            pic = ImageTk.PhotoImage(img)
            self.image_label.config(image=pic, background='black')
            
            # Clear history and save initial state
            self.image_history = [img.copy()]
        else:
            print('No file was chosen, please choose a file')

    def remove_bg(self):
        global img, my_img, img_size
        try:
            self.image_history.append(img.copy())  # Save current state before modifying
            output = remove(img).resize(img_size)
            img = output
            my_img = ImageTk.PhotoImage(output)
            self.image_label.config(image=my_img)
        except:
            messagebox.showerror('No Image', 'No image loaded, use browse to look for your image')

    def make_draggable(self, widget):

        def on_drag_start(event):
            widget = event.widget
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y

        def on_drag_motion(event):
            widget = event.widget
            new_x = widget.winfo_x() - widget._drag_start_x + event.x
            new_y = widget.winfo_y() - widget._drag_start_y + event.y
            widget.place(x=new_x, y=new_y)

        widget.bind("<Button-1>", on_drag_start)
        widget.bind("<B1-Motion>", on_drag_motion)

    def configure_grid(self):
        self.grid_columnconfigure(0, weight=0)
        # self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

    def open_color_chooser_window(self):
        color_chooser = ColorChooserDialog()
        color_chooser.show()
        self.text_color = color_chooser.result.hex

    def undo_action(self):
        global img, pic, my_img, img_size
        if len(self.image_history) > 1:
            self.image_history.pop()  # Remove the current state
            previous_img = self.image_history[-1]  # Get the previous state
            img = previous_img
            pic = ImageTk.PhotoImage(img)
            self.image_label.config(image=pic, background='black')

    def rotate_image(self, angle):
        global img, pic, img_size
        try:
            self.image_history.append(img.copy())  # Save current state before rotating
            img = img.rotate(angle, expand=True)
            pic = ImageTk.PhotoImage(img)
            self.image_label.config(image=pic, background='black')
        except:
            messagebox.showerror('No Image', 'No image loaded, use browse to look for your image')
        print(self.watermark.winfo_x(), self.watermark.winfo_y())
            
    def save_image(self):
        save_path = filedialog.asksaveasfilename(title='Choose Save Location', filetypes=[('JPG', '.jpg')], defaultextension=".jpg")
        if save_path:
            self.user_text
            img.save(save_path)

app = App(style='superhero')
app.mainloop()

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
