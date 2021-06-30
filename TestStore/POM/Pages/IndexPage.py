import unittest
from selenium.webdriver.common.by import By

class IndexPageLocators:
    singinOrRegisterButon = (By.CSS_SELECTOR, '#customer_menu_top > li')


class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    def gotologinpage(self):
        self.driver.find_element(*IndexPageLocators.singinOrRegisterButon).click()