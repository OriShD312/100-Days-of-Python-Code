import smtplib
import datetime as dt
import random

MY_EMAIL = "or9shah2@gmail.com"
PASSWORD = "heojyguhaevohial"
now = dt.datetime.now()
print(now.weekday())

with open("quotes.txt", "r") as file:
    data = file.readlines()
    random_quote = random.choice(data)
    if now.weekday() == 5:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="shhar2ma@gmail.com",
                                msg=f"Subject:Monday Inspiration\n\n{random_quote}"
                                )

