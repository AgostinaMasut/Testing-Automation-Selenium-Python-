import unittest
from selenium.webdriver.common.by import By


class AccountPageLocators:
    tittle = (By.CLASS_NAME, 'heading1')
    spanSubtext = (By.CLASS_NAME, 'subtext')
    editAccountLink = (By.CSS_SELECTOR, 'a[data-original-title="Edit account details"]')
    changePasswordLink = (By.CSS_SELECTOR, 'a[data-original-title="Change password"]')
    menuAccountDropdownList = (By.CLASS_NAME, 'top menu_account')


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

#obtener el text del tittle y subtitle para hacer un accert
    def getTittleText(self):
        return self.driver.find_element(*AccountPageLocators.tittle).text()

    def getSubtitleText(self):
        return self.driver.find_element(*AccountPageLocators.spanSubtext).text()
