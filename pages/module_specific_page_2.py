import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CityPage(BasePage):

    FROM_CITY = (By.ID, "fromCity")
    TO_CITY = (By.ID, "toCity")
    FROM_INPUT = (By.XPATH, "//input[@placeholder='From']")
    TO_INPUT = (By.XPATH, "//input[@placeholder='To']")
    SUGGESTIONS = (By.XPATH, "//ul[@class='react-autosuggest__suggestions-list']/li")

    def select_from_city(self, city):
        self.click(self.FROM_CITY)
        self.send_keys(self.FROM_INPUT, city[:3])
        time.sleep(2)
        for s in self.driver.find_elements(*self.SUGGESTIONS):
            if city in s.text:
                s.click()
                break

    def select_to_city(self, city):
        self.click(self.TO_CITY)
        self.send_keys(self.TO_INPUT, city[:2])
        time.sleep(2)
        for d in self.driver.find_elements(*self.SUGGESTIONS):
            if city in d.text:
                d.click()
                break
