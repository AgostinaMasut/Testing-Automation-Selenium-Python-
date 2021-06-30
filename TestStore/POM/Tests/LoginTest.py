import unittest
from selenium import webdriver
from POM.Pages.IndexPage import IndexPage


class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.fullscreen_window()

    def test_success_Login(self):
        indexPage = IndexPage(self.driver)

        indexPage.gotologin(self.driver)