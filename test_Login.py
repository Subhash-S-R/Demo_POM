from Homepage import *
from Loginpage import *
from Excel_utilities import *
import pytest

# args = "username, password"
# data = [
#     ('subhash@gmail.com', 'abcdefgh'),
#     ('abc@gmail.com', 'uvwxyz')
# ]

file = r"C:\Users\User\Pythontesting\Online_7\Pytest_7\POM\Params_7.xlsx"

args = readArgs(file, "Loginpage")
data = read_all_data(file, "Loginpage")

@pytest.mark.parametrize(args, data)
def test_login(SAM, username, password):
    obj1 = HomePage(SAM)
    obj1.login()

    obj2 = LoginPage(SAM)
    obj2.Login(username, password)


