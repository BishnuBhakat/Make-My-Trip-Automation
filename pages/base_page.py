from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def click(self, locator):
        self.wait.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait.wait_for_element(locator).send_keys(text)
