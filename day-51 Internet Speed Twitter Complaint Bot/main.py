from InternetSpeedTwitterBot import InternetSpeedTwitterBot

EXPECTED_DOWN = "1000"
EXPECTED_UP = "100"

bot = InternetSpeedTwitterBot()
[speed_down, speed_up] = bot.get_internet_speed()
bot.tweet_at_provider(EXPECTED_DOWN, EXPECTED_UP)
