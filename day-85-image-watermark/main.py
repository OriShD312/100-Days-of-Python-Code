from pathlib import Path
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
        self.text_items = [] # list that holds all the text added to the image

        self.my_notebook = Notebook(self) # create a notebook to include all app features
        self.my_notebook.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=NS)
        
        self.configure_grid()

        self.my_canvas = Canvas(self, width=1280, height=960) # canvas to hold image
        self.my_canvas.grid(row=0, column=2, rowspan=3, padx=(0, 10), pady=10)

        self.browse_for_image_button = Button(self, text='Browse', command=self.browse_for_image) # button to browse for image
        self.browse_for_image_button.grid(row=1, column=0, sticky=EW, padx=10, pady=(0, 10))

        self.save_image_button = Button(self, text='Save', command=self.save_image) # button to save image after changes
        self.save_image_button.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky=EW)

        self.undo_button = Button(self, text='Undo Last Action', command=self.undo_action) # button to undo last action
        self.undo_button.grid(row=2, column=0, padx=10, pady=(0,10), sticky=EW, columnspan=2)

        self.customization_tab = Frame(self.my_notebook) # Notebook Frame
        self.my_notebook.add(self.customization_tab, text='Customize Your Image')

        self.user_text_label = Label(self.customization_tab, text='Your text here:') # user text prompt
        self.user_text_label.grid(row=0, column=0, padx=10, pady=10)

        self.text_opacity = Scale(self.customization_tab, command=self.update_alpha) # opacity scale slider
        self.text_opacity.grid(row=1, column=1, padx=10, pady=10)

        self.alpha_value_label = Label(self.customization_tab, text=f'Opacity: {self.text_opacity.get()}') # show current opacity value
        self.alpha_value_label.grid(row=1, column=0, padx=10, pady=10)

        self.user_text = Entry(self.customization_tab) # user text entry box
        self.user_text.grid(row=0, column=1, padx=10, pady=10, sticky=EW)
                        
        self.open_font_dialog_window_button = Button(self.customization_tab, text='Open Font Settings', command=self.open_font_dialog_window) # button that opens font dialog window
        self.open_font_dialog_window_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

        self.open_color_chooser_window_button = Button(self.customization_tab, text='Open Font Color Settings', command=self.open_color_chooser_window) # button that opens color choice window
        self.open_color_chooser_window_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

        self.add_text_button = Button(self.customization_tab, text='Add Your Text to Image', command=self.add_text) # button that adds user text to canvas image
        self.add_text_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

        self.remove_bg_button = Button(self.customization_tab, text='Remove Image Background', command=self.remove_bg) # button that activates remove image background function
        self.remove_bg_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

        self.rotate_image_counter_clockwise_button = Button(self.customization_tab, text='↪', style='my.TButton', command=lambda: self.rotate_image(90), width=10) # button to rotate image 90 degrees counter clockwise
        self.rotate_image_counter_clockwise_button.grid(row=6, column=0, padx=10, pady=10)

        self.rotate_image_clockwise_button = Button(self.customization_tab, text='↩', style='my.TButton', command=lambda: self.rotate_image(-90), width=10) # button to rotate image 90 degrees clockwise
        self.rotate_image_clockwise_button.grid(row=6, column=1, padx=(0,10), pady=10)

    def update_alpha(self, e):
        self.alpha_value_label.config(text=f'Opacity: {self.text_opacity.get():,.1f}')
    
    def add_text(self):
        if self.user_text.get():
            self.image_history.append(img.copy())
            x, y = 100, 100
            text_id = self.my_canvas.create_text(x, y, text=self.user_text.get(), font=self.text_font, fill=self.text_color)
            self.text_items.append((text_id, self.user_text.get(), self.text_font, self.text_color, x, y))
            self.make_draggable(text_id)

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
                img_size = round(1280*img_ratio), 1280
                img = img.resize(size=img_size)
            pic = ImageTk.PhotoImage(img)
            self.my_canvas.create_image(0, 0, anchor=NW, image=pic)
            
            self.image_history = [img.copy()] # Clear history and save initial state
            self.text_items = []
        else:
            print('No file was chosen, please choose a file')

    def remove_bg(self):
        global img, pic, img_size
        try:
            self.image_history.append(img.copy())  # Save current state before modifying
            img = remove(img).resize(img_size)
            pic = ImageTk.PhotoImage(img)
            self.my_canvas.create_image(0, 0, anchor=NW, image=pic)
            self.reapply_text_items()
        except Exception as e:
            messagebox.showerror('No Image', f'No image loaded, use browse to look for your image/n{e}')
        
    def configure_grid(self):
            self.rowconfigure(0, weight=1)

    def open_color_chooser_window(self):
        color_chooser = ColorChooserDialog()
        color_chooser.show()
        self.text_color = color_chooser.result.hex

    def undo_action(self):
        global img, pic
        if len(self.image_history) > 1:
            img = self.image_history[-1].copy()  # Get the previous state
            self.image_history.pop()  # Remove the current state
            pic = ImageTk.PhotoImage(img)
            self.my_canvas.create_image(0, 0, anchor=NW, image=pic)
            self.reapply_text_items()

    def rotate_image(self, angle):
        global img, pic
        try:
            self.image_history.append(img.copy())  # Save current state before rotating
            img = img.rotate(angle, expand=True)
            pic = ImageTk.PhotoImage(img)
            self.my_canvas.create_image(0, 0, anchor=NW, image=pic)
            self.reapply_text_items()
        except:
            messagebox.showerror('No Image', 'No image loaded, use browse to look for your image')
            
    def save_image(self):
        save_path = filedialog.asksaveasfilename(title='Choose Save Location', filetypes=[('JPG', '.jpg')], defaultextension=".jpg")
        if save_path:
            try:
                img_with_text = img.copy()
                draw = ImageDraw.Draw(img_with_text)
                for _, text, font, color, x, y in self.text_items:
                    text_font = ImageFont.truetype('arial.ttf', size=font['size'])
                    draw.text((x, y), text=text, font=text_font, fill=color)
                img_with_text.save(save_path)
                messagebox.showinfo('Image Saved', 'Image Saved Successfully!')
            except Exception as e:
                messagebox.showerror('Error Saving', f'Failed to Save Image/n{str(e)}')

    def make_draggable(self, item):
        def on_drag_start(event):
            event.widget._drag_data = {'x': event.x, 'y': event.y}
            event.widget._drag_item = item  # Store the current item being dragged

        def on_drag_motion(event):
            widget = event.widget
            x_delta = event.x - widget._drag_data['x']
            y_delta = event.y - widget._drag_data['y']
            widget.move(item, x_delta, y_delta)
            widget._drag_data = {'x': event.x, 'y': event.y}
            for i, (text_id, text, font, color, x, y) in enumerate(self.text_items):
                if text_id == item:
                    self.text_items[i] = (text_id, text, font, color, x + x_delta, y + y_delta)
                    break

        def on_key_press(event):
            if event.keysym == 'Delete' and hasattr(self.my_canvas, '_drag_item'):
                item_to_delete = self.my_canvas._drag_item
                self.my_canvas.delete(item_to_delete)
                self.text_items = [(text_id, text, font, color, x, y) for (text_id, text, font, color, x, y) in self.text_items if text_id != item_to_delete]

        self.my_canvas.tag_bind(item, "<Button-1>", on_drag_start)
        self.my_canvas.tag_bind(item, "<B1-Motion>", on_drag_motion)
        self.my_canvas.bind_all("<KeyPress>", on_key_press)  # Bind the Delete key press event globally

    def reapply_text_items(self):
        for _, text, _, font, color, x, y in self.text_items:
            text_id = self.my_canvas.create_text(x, y, text=text, font=font, fill=color)
            self.make_draggable(text_id)

app = App(style='superhero')
app.mainloop()