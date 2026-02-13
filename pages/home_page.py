import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    CLOSE_POPUP = (By.CLASS_NAME, "commonModal__close")
    MINIMIZE = (By.XPATH, "//img[@alt='minimize']")
    FSW = (By.CLASS_NAME, "fsw ")
    BUS_TAB = (By.XPATH, "//span[text()='Buses']")

    def close_popups(self):
        time.sleep(3)
        self.click(self.CLOSE_POPUP)
        time.sleep(3)
        self.click(self.MINIMIZE)

    def open_bus_module(self):
        self.click(self.FSW)
        self.click(self.BUS_TAB)
