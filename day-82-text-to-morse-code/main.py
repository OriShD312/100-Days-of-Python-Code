from tkinter import *
import time
import winsound
import json
import threading

# Set constants
BACKGROUND_COLOR = "#B1DDC6"
SHORT = 100
LONG = SHORT*3
SHORT_GAP = SHORT*3/1000
MEDIUM_GAP = SHORT*7/1000

# Load morse code dictionary
with open('morse_code.json', 'r') as file:
    morse_code = json.load(file)

# Create a lock to make sure that only one instance of the translation can run at a time
lock = threading.Lock()

# Play sound according to the mark from the breakdown of each letter/digit sent from the translate_to_morse function
def play_sound(mark):
    if mark == '.':
        winsound.Beep(700, SHORT)
    else:
        winsound.Beep(700, LONG)
    time.sleep(SHORT_GAP)

# Break down user input to word by word, then to char in word and send each char to the play_sound function
def translate_to_morse(user_input):
    with lock:
        for word in user_input.split():
            for char in word:
                canvas.itemconfig(translated_text, text=f"{char}\n{morse_code.get(char, '')}")
                if char in morse_code:
                    for mark in morse_code[char]:
                        if mark != ' ' or '':
                            play_sound(mark)
            time.sleep(MEDIUM_GAP)
        canvas.itemconfig(translated_text, text="Translation Complete")
        translate_button.config(state=NORMAL, text='Translate to Morse Code')

# Begin translation process by opening thread + disable button interaction
def translate():
    translate_button.config(state=DISABLED, text='Running translation...')
    user_input = entry.get().upper()
    translate_thread = threading.Thread(target=translate_to_morse, args=(user_input,))
    translate_thread.start()

# Window setup
window = Tk()
window.title('Text to Morse Code')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Adding Canvas that will display current letter being translated with Morse Code representation
canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR)
translated_text = canvas.create_text(100, 100, text='Write something into the\nentry and click the button', font=('Arial', 10, 'bold'), justify=CENTER)
canvas.pack()

# User text input area
entry = Entry(window, justify=CENTER)
entry.pack(pady=20)

# Button to initiate translation to Morse Code
translate_button = Button(window, text='Translate to Morse Code', activebackground='green', activeforeground='white', command=translate)
translate_button.pack()

window.mainloop()

# TODO #1: add keeping track of which words were inputted and save to either file or db
# TODO #2: add "show statistics" button that opens a bar graph with top 20 (or any n) words used