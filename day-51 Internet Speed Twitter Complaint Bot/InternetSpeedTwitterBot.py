import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test").click()
        time.sleep(45)
        self.down = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text
        return self.down, self.up

    def tweet_at_provider(self, expected_down, expected_up):
        try:
            with open("speeds.txt", "w") as file:
                file.write(f"My speeds are: {self.down}/{self.up}.\n"
                           f"My expected speeds are: {expected_down}/{expected_up}")
        except:
            print("An error occurred while trying to save")


