import unittest
from selenium.webdriver.common.by import By

class LoginPageLocators:
    nameTexbox = (By.NAME, 'loginname')
    passwordTexbox = (By.NAME, 'password')
    loginButton = (By.CSS_SELECTOR, 'button[title="Login"]')
    toRegisterButton = (By.CSS_SELECTOR, 'button[title="Continue"]')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def gotoRegister(self):
        self.driver.find_element(*LoginPageLocators.toRegisterButton)

    def login(self, name, password):
        self.driver.find_element(*LoginPageLocators.nameTexbox).send_keys(name)
        self.driver.find_element(*LoginPageLocators.passwordTexbox).send_keys(password)
        self.driver.find_element(*LoginPageLocators.loginButton).click()

#Agostina
#Masut
#agomasu@hotmail.com
#321654987
#159357
#Darwoft
#Lalaland 360
#Lalaland 365
#Salsipuedes
#Cordoba
#3115
#Argentina
#SeleniumPython
#Dell1234
