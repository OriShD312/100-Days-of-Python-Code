import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

MY_GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdcyTvpTmYFsJLOhEXDTq2J0QzDAjpHFT8QbWAOVONKrzgmqA/" \
                 "viewform?usp=sf_link"
ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"


# Bot that will be linked to relevant google form and automatically fill it in
class AddressBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url=MY_GOOGLE_FORM)

    def fill_table(self, address, price, link):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link)
        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


# Connect to Zillow + create soup
response = requests.get(url=ZILLOW_CLONE)
soup = BeautifulSoup(response.text, "html.parser")

# Collect prices + set them into list
prices_soup = soup.select("div.StyledPropertyCardDataArea-fDSTNn")
prices_list = [price.text.strip().split("+")[0].split("/")[0] for price in prices_soup]

# Collect addresses + set them into list
address_soup = soup.find_all(name="address")
addresses_list = [address.text.strip().replace("|", "") for address in address_soup]

# Collect links + set them into list
link_soup = soup.find_all(name="a", class_="property-card-link")
links_list = [link["href"] for link in link_soup]

# Create bot instance and call form fill method
auto_bot = AddressBot()
for i in range(len(prices_list)):
    auto_bot.fill_table(addresses_list[i], prices_list[i], links_list[i])