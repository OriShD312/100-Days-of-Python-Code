from tkinter import *
from tkinter import messagebox
import pandas
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
current_card = ""


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = data.sample()
    foreign_word = current_card.iloc[:, 0].to_string(index=False)
    canvas.itemconfig(card_img, image=canvas_front_img)
    canvas.itemconfig(card_word, text=foreign_word, fill="black")
    canvas.itemconfig(card_title, text=current_card.columns[0], fill="black")
    timer = window.after(3000, func=translation)


def i_know():
    data.drop(current_card.index.item(), inplace=True)
    next_card()


def translation():
    local_word = current_card.iloc[:, 1].to_string(index=False)
    canvas.itemconfig(card_img, image=canvas_back_img)
    canvas.itemconfig(card_title, text=current_card.columns[1], fill="white")
    canvas.itemconfig(card_word, text=local_word, fill="white")


# Window setup
window = Tk()
window.title("Polingo")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
timer = window.after(3000, func=translation)

# Flashcard setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_front_img = PhotoImage(file="images/card_front.png")
canvas_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=canvas_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
next_card()
canvas.grid(column=0, row=0, columnspan=2)

# Buttons setup
cross_img = PhotoImage(file="images/wrong.png")
i_do_not_know_button = Button(image=cross_img, bg=BACKGROUND_COLOR, command=next_card)
i_do_not_know_button.grid(column=0, row=1)
check_img = PhotoImage(file="images/right.png")
i_know_button = Button(image=check_img, bg=BACKGROUND_COLOR, command=i_know)
i_know_button.grid(column=1, row=1)

window.mainloop()
if messagebox.askokcancel(title="Good session 😊", message="Update dictionary based "
                                                          "on current session?"):
    data.to_csv("data/words_to_learn.csv", index=False)
