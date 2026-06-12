from lib import *
from Excel_utilities import *

class HomePage:

    # locators = {
    #     'register': ('xpath', "//a[text()='Register']"),
    #     'login': ('xpath', "//a[text()='Log in']")
    # }

    file = r"C:\Users\User\OneDrive\Desktop\Class\Online_7\Locators_7.xlsx"

    locators = readLocators(file, "Homepage")

    def __init__(self, driver):
        self.driver = driver

    def register(self):
        s = wrapper(self.driver)
        s.clicks(self.locators['register'])

    def login(self):
        s = wrapper(self.driver)
        s.clicks(self.locators['login'])

