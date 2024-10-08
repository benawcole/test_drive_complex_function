from lib.age_checker import *

def test_age_input():
    assert age_checker("2022-01-01") == "Access denied - You have to be 16 or older to enter"
    assert age_checker("2001-01-01") == "Access granted"
    assert age_checker("2008-10-08") == "Access granted"