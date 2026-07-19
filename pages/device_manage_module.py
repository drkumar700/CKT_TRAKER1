from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions as EC 
from helpers.variables import *
from helpers.locators import *


class DeviceManageModule:
    def __init__(self, driver):
        self.driver = driver

    def naviagete_to_device_page(self):
        self.driver.find_element(*device_management).click()

    def enter_device_name(self):
        self.driver.find_element(*device_name).send_keys(device_name)

    def enter_device_ip(self):
        self.driver.find_element(*device_ip).send_keys(device_ip)
        time.sleep(0.5)
    def enter_device_uname(self):
        self.driver.find_element(*device_uname).send_keys(device_uname)

    def enter_device_password(self):
        self.driver.find_element(*device_password).send_keys(device_password)
        time.sleep(0.5)
    def enter_device_type(self):
        select = Select(self.driver.find_element(*device_type))
        select.select_by_visible_text(DEVICE_TYPE)

    def enter_device_version(self):
        select = Select(self.driver.find_element(*device_version))
        select.select_by_visible_text(DEVICE_VERSION)
        time.sleep(0.5)
    def enter_device_protocal(self):
        select = Select(self.driver.find_element(*device_protocal))
        select.select_by_visible_text(DEVICE_PROTOCAL)
        #time.sleep()
        time.sleep(0.3)
    def click_add_device(self):
        self.driver.find_element(*add_device_btn).click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        print('\n\n',alert.text)
        alert.accept()
        time.sleep(5)

