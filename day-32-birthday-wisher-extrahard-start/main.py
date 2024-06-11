##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "or9shah2@gmail.com"
MY_PASSWORD = "heojyguhaevohial"
PLACEHOLDER = "[NAME]"
LETTER = "letter_"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")
mask = (birthdays.month == now.month) & (birthdays.day == now.day)
if True in mask.values:
    indices = birthdays.index[mask]
    for i in indices:
        with open(f"letter_templates/{LETTER + str(random.randint(1, 3))}.txt") as text:
            letter = text.read()
            letter = letter.replace(PLACEHOLDER, birthdays.name[i])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=birthdays.email[i],
                                    msg=f"Subject:Happy Birthday {birthdays.name[i]}\n\n"
                                        f"{letter}"
                                    )

