from Homepage import *
from Registerpage import *
from Excel_utilities import *
import pytest

# args = "gender, fname, lname, email, password, confirmpassword"
# data = [
#     ("female", "abc", "xyz", "subhash@gmail.com", "abcdefgh", "abcdefgh"),
#     ("male", "xyz", "abc", "sam@gmail.com", "efghabcd", "efghabcd")
# ]

file = r"C:\Users\User\Pythontesting\Online_7\Pytest_7\POM\Params_7.xlsx"

args = readArgs(file, "Registerpage")
data = read_all_data(file, "Registerpage")

@pytest.mark.parametrize(args, data)
def test_register(SAM, gender, fname, lname, email, password, confirmpassword):
    obj1 = HomePage(SAM)
    obj1.register()

    obj2 = RegisterPage(SAM)
    obj2.Register(gender, fname, lname, email, password, confirmpassword)

