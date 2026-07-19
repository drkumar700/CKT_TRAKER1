from selenium import webdriver
import time
import sys
import os
from selenium.webdriver.common.by import By

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

class TestLoginPage:
    def test_login(self):
        print("step 1 : open browser and navigate to login page")
        login=LoginPage()
        print("step 2 : enter username and password")
        login.open_browser()
        print("step 3 : click on login button")
        login.username()
        print("step 4 : enter password")
        login.password()
        print("step 5 : click on login button")
        login.click_login()
        print("step 6 : verify dashboard page")
        login.dashboard()
        print("step 7 :click on softweare update buttom")
        # login.software_update()
        

if __name__ == "__main__":
    test = TestLoginPage()
    test.test_login()