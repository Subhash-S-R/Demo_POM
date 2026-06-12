from lib import wrapper
from Excel_utilities import *

class LoginPage:

    # locators = {
    #     'Username': ("id", "Email"),
    #     'Password': ("id", "Password"),
    #     'login_btn': ("xpath", "//input[@value = 'Log in']")
    # }

    file = r"C:\Users\User\OneDrive\Desktop\Class\Online_7\Locators_7.xlsx"

    locators = readLocators(file, "Loginpage")

    def __init__(self, driver):
        self.driver = driver

    def Login(self, username, password):
        s = wrapper(self.driver)
        s.enters(self.locators['Username'], username)
        s.enters(self.locators['Password'], password)
        s.clicks(self.locators['login_btn'])
