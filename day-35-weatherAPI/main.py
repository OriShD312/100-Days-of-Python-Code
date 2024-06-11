import smtplib
import os
import requests

# 50.40433871914115, 32.8443866004386 Zhytomyr
# 32.770279, 35.042690 Nesher

FROM_EMAIL = "or9shah2@gmail.com"
MY_PASSWORD = os.environ.get("MY_GMAIL_PASSWORD")
TO_EMAIL = "shhar2ma@gmail.com"
OWM_api_key = os.environ.get("OWM_API_KEY")
OWM_url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 50.40,
    "lon": 32.84,
    "exclude": "current,minutely,daily",
    "appid": OWM_api_key,
}

response = requests.get(OWM_url, params=parameters)
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

rain = False

for hour_data in weather_slice:
    weather_id = hour_data['weather'][0]['id']
    if weather_id < 700:
        rain = True

if rain:
    print("rain")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:Rain warning\n\n"
                                "Bring an umbrella!"
                            )
