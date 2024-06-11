import smtplib
import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API = os.environ.get("ALPHA_VANTAGE_KEY")
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
STOCK_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API
}

NEWS_API = os.environ.get("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_PARAMS = {
        "q": COMPANY_NAME,
        "pageSize": 3,
        "apikey": NEWS_API
    }

FROM_EMAIL = "or9shah2@gmail.com"
MY_PASSWORD = os.environ.get("MY_GMAIL_PASSWORD")
TO_EMAIL = "shhar2ma@gmail.com"
OWM_api_key = os.environ.get("OWM_API_KEY")

DIFFERENCE_NOTICE = 5/100


def get_news():
    news_data = requests.get(url=NEWS_API_URL, params=NEWS_API_PARAMS).json()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:{COMPANY_NAME} stock news \n\n"
                                f"{news_data}"
                            )

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_data = requests.get(url=ALPHA_VANTAGE_URL, params=STOCK_API_PARAMS).json()
dates = list(stock_data["Time Series (Daily)"].keys())
last_two_days = [float(stock_data["Time Series (Daily)"][date]["4. close"]) for date in dates[:2]]

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

print(last_two_days[1] * DIFFERENCE_NOTICE < round(abs(last_two_days[0] - last_two_days[1]), 2))

if last_two_days[1] * DIFFERENCE_NOTICE < round(abs(last_two_days[0] - last_two_days[1]), 2):
    get_news()
else:
    print('Regular day')

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""