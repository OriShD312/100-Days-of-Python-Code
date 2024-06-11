import smtplib
from datetime import datetime, timedelta
import requests
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASS")

TEQUILA_KEY = {"apikey": "-8tbhz_rCp2oYsDMFda-BpY-avvCPk4u"}
TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
ORIGIN_CITY = "Tel Aviv"
FLIGHT_ORIGIN = "TLV"
CURRENCY = "USD"

GOOGLE_SHEETS_URL = os.environ.get("GOOGLE_URL")

sheets_headers = {
    "Authorization": os.environ.get('TOKEN')
}

tomorrow_date = datetime.today() + timedelta(days=1)
half_year = tomorrow_date + timedelta(days=180)
response = requests.get(url=GOOGLE_SHEETS_URL+"prices", headers=sheets_headers)
with open("deals.txt", "w") as file:
    for destination in response.json()["prices"]:
        tequila_params = {
            "fly_from": FLIGHT_ORIGIN,
            "fly_to": destination["iataCode"],
            "date_from": tomorrow_date.strftime("%d/%m/%Y"),
            "date_to": half_year.strftime("%d/%m/%Y"),
            "price_to": destination["lowestPrice"],
            "curr": CURRENCY
        }
        flights = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=tequila_params, headers=TEQUILA_KEY)
        print(destination["iataCode"], destination["lowestPrice"])
        flights = flights.json()
        data = flights['data']
        try:
            deal_price = data[0]['price']
            deal_destination_city = data[0]['cityTo']
            deal_destination_iata = data[0]['cityCodeTo']
            deal_leave_date = data[0]['local_departure'].split("T")[0]
            deal_return_date = data[0]['local_arrival'].split("T")[0]
            print(f"Low price alert! Only {deal_price}$ to fly from {ORIGIN_CITY}-{FLIGHT_ORIGIN} "
                  f"to {deal_destination_city}-{deal_destination_iata}, "
                  f"from {deal_leave_date} to {deal_return_date}.")
            file.write(f"Low price alert! Only {deal_price}$ to fly from {ORIGIN_CITY}-{FLIGHT_ORIGIN} "
                       f"to {deal_destination_city}-{deal_destination_iata}, "
                       f"from {deal_leave_date} to {deal_return_date}.\n")
        except IndexError:
            print(f"Sorry, no deals for {destination['city']}")
            file.write(f"Sorry, no deals for {destination['city']}\n")


with open("deals.txt", "r") as file:
    text = file.read()
response = requests.get(url=GOOGLE_SHEETS_URL+"users", headers=sheets_headers)
data = response.json()['users']
for user in data:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=user["email"],
                            msg=f"Subject:Flight Deals!!!\n\n"
                                f"{text}"
                            )
