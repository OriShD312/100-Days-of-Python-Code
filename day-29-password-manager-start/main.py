from tkinter import *
from tkinter import messagebox
from random import choices, randint, shuffle
import pyperclip
import json

# ---------------------------- ACCOUNT SEARCH ----------------------------------- #


def find_account():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if web_entry.get() in data:
            account = data[web_entry.get()]
            messagebox.showinfo(title=web_entry.get(),
                                message=f"Username: {account['email']} "
                                        f"\nPassword: {account['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web_entry.get()} exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [char for char in choices(letters, k=randint(8, 10))]
    password_list += [char for char in choices(symbols, k=randint(2, 4))]
    password_list += [char for char in choices(numbers, k=randint(2, 4))]

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_account():
    new_data = {
        web_entry.get(): {
            "email": email_entry.get(),
            "password": pass_entry.get(),
        }
    }
    if len(web_entry.get()) != 0 and len(pass_entry.get()) != 0 and len(email_entry.get()) != 0:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            # Updating old data with new data
            data.update(new_data)
        finally:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please fill all fields")


# ---------------------------- UI SETUP ------------------------------- #


# Create window
window = Tk()
window.config(pady=50, padx=50)
window.title("My Password Manager")

# Create canvas for logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Web label and user entry fields
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_name = StringVar()
web_entry = Entry(textvariable=web_name)
web_entry.grid(column=1, row=1, sticky="EW")
web_entry.focus()

web_search_button = Button(text="Search", command=find_account)
web_search_button.grid(column=2, row=1, sticky="EW")

# Email/Username label and user entry field
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

user_email = StringVar()
email_entry = Entry(textvariable=user_email)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "shhar2ma@gmail.com")

# Password label, user entry and generation button
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

user_pass = StringVar()
pass_entry = Entry(textvariable=user_pass)
pass_entry.grid(column=1, row=3, sticky="EW")

gen_button = Button(text="Generate Password", command=generate_pass)
gen_button.grid(column=2, row=3, sticky="EW")

# Add account button
add_button = Button(text="Add", width=35, command=add_account)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
