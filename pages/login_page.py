from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from helpers.variables import *
from helpers.locators import *

class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(5)
    def username(self):
        self.driver.find_element(*username_locator).send_keys(username)
    def password(self):
        self.driver.find_element(*password_locator).send_keys(password)
    def click_login(self):
        self.driver.find_element(*login_button_locator).click()
    def dashboard(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text
        assert self.dashboard() == dashboard_title 
