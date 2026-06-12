from lib import *
from Excel_utilities import *

class RegisterPage:

    # locators = {
    #     "male_rdb": ("id", 'gender-male'),
    #     "female_rdb": ('id', 'gender-female'),
    #     "Fname": ("id", 'FirstName'),
    #     "Lname": ("id", 'LastName'),
    #     "Email": ("id", "Email"),
    #     "Password": ("id", 'Password'),
    #     "Cfm_Password": ("id", "ConfirmPassword")
    # }

    file = r"C:\Users\User\OneDrive\Desktop\Class\Online_7\Locators_7.xlsx"

    locators = readLocators(file, "Registerpage")

    def __init__(self, driver):
        self.driver = driver

    def Register(self, gender, fname, lname, email, password, confirmpassword):
        s = wrapper(self.driver)

        if gender.lower() == 'male':
            s.clicks(self.locators['male_rdb'])
        else:
            s.clicks(self.locators['female_rdb'])

        s.enters(self.locators['Fname'], fname)
        s.enters(self.locators['Lname'], lname)
        s.enters(self.locators['Email'], email)
        s.enters(self.locators['Password'], password)
        s.enters(self.locators['Cfm_Password'], confirmpassword)
