import unittest
from selenium.webdriver.common.by import By


class RegisterPageLocators:
    firstNameInput = (By.NAME, 'firstname')
    lastNameInput = (By.NAME, 'lastname')
    emailInput = (By.NAME, 'email')
    telephoneInput = (By.NAME, 'telephone')
    faxInput = (By.NAME, 'fax')
    companyInput = (By.NAME, 'company')
    firstAddressInput = (By.NAME, 'address_1')
    secondAddressInput = (By.NAME, 'address_2')
    cityInput = (By.NAME, 'city')
    regionSelector = (By.NAME, 'zone_id')
    zipCodeInput = (By.NAME, 'postcode')
    countrySelector = (By.NAME, 'country_id')
    loginNameInput = (By.NAME, 'loginname')
    passwordInput = (By.NAME, 'password')
    passwordConfirmInput = (By.NAME, 'confirm')
    yesNewsletterInput = (By.ID, 'AccountFrm_newsletter1')
    noNewsletterInput = (By.ID, 'AccountFrm_newsletter0')
    privacyPolicyInput = (By.ID, 'AccountFrm_agree')
    registerButton = (By.CSS_SELECTOR, 'button[title="Continue"]')


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def getFirstName(self):
        return self.driver.find_element(*RegisterPageLocators.firstNameInput)

    def getLastName(self):
        return self.driver.find_element(*RegisterPageLocators.lastNameInput)

    def getEmail(self):
        return self.driver.find_element(*RegisterPageLocators.emailInput)

    def getTelephone(self):
        return self.driver.find_element(*RegisterPageLocators.telephoneInput)

    def getFax(self):
        return self.driver.find_element(*RegisterPageLocators.faxInput)

    def getCompany(self):
        return self.driver.find_element(*RegisterPageLocators.firstNameInput)

    def getFirstAddress(self):
        return self.driver.find_element(*RegisterPageLocators.firstAddressInput)

    def getSecondAddress(self):
        return self.driver.find_element(*RegisterPageLocators.secondAddressInput)

    def getCity(self):
        return self.driver.find_element(*RegisterPageLocators.cityInput)

    def getRegion(self):
        return self.driver.find_element(*RegisterPageLocators.regionSelector)

    def getZipCode(self):
        return self.driver.find_element(*RegisterPageLocators.zipCodeInput)

    def getCountry(self):
        return self.driver.find_element(*RegisterPageLocators.countrySelector)

    def getLoginName(self):
        return self.driver.find_element(*RegisterPageLocators.loginNameInput)

    def getPassword(self):
        return self.driver.find_element(*RegisterPageLocators.passwordInput)

    def getConfirmPassword(self):
        return self.driver.find_element(*RegisterPageLocators.passwordConfirmInput)

    def getYesNewsletter(self):
        return self.driver.find_element(*RegisterPageLocators.yesNewsletterInput)

    def getNoNewsletter(self):
        return self.driver.find_element(*RegisterPageLocators.noNewsletterInput)

    def getPrivacyPolicy(self):
        return self.driver.find_element(*RegisterPageLocators.privacyPolicyInput)

    def getRegisterButton(self):
        return self.driver.find_element(*RegisterPageLocators.registerButton)

#primero ingresar país y dsp ciudad
    def register(self, firstname, lastname, email, telephone, fax, company, address1, address2, city, zipcode, loginname, password):
        self.getFirstName().send_keys(firstname)
        self.getLastName().send_keys(lastname)
        self.getEmail().send_keys(email)
        self.getTelephone().send_keys(telephone)
        self.getFax().send_keys(fax)
        self.getCompany().send_keys(company)
        self.getFirstAddress().send_keys(address1)
        self.getSecondAddress().send_keys(address2)
        self.getCity().send_keys(city)
        self.getZipCode().send_keys(zipcode)
        self.getLoginName().send_keys(loginname)
        self.getPassword().send_keys(password)
        self.getConfirmPassword().send_keys(password)
