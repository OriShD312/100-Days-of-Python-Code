from selenium import webdriver
from selenium.webdriver.common.by import By
import time

UPGRADE_CHECK = 2
TOTAL_GAME_TIME = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
my_money = driver.find_element(By.ID, "money")
store_ids = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]

timeout = time.time() + UPGRADE_CHECK
end_time = time.time() + TOTAL_GAME_TIME

while time.time() <= end_time:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = store_ids[n]

        affordable_upgrades = {}
        for cost, id in upgrades.items():
            if int(my_money.text.replace(",", "")) > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + UPGRADE_CHECK

    if time.time() > end_time:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        break

print(upgrades)
print(affordable_upgrades)
driver.quit()
