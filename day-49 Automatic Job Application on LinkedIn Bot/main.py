import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "shhar2ma@gmail.com"
ACCOUNT_PASSWORD = "46Kimattnla92"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3842899468&f_AL=true&f_E=2&geoId=101620260&"
#                "keywords=junior%20python%20developer&location=Israel&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3835928708&f_AL=true&geoId=101174742&"
               "keywords=junior%20python%20developer&location=Canada&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div a.nav__button-secondary").click()

time.sleep(2)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, "div ul.scaffold-layout__list-container li strong")
for job in jobs:
    job.click()
    driver.find_element(By.CSS_SELECTOR, "div.mt5 div button.jobs-save-button").click()
    time.sleep(2)
