from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from helpers.variables import *
from helpers.locators import *


class DeviceConfig():
    def __init__(self, driver):
        self.driver=driver
        self.wait= WebDriverWait(driver, 10)

    def navigate_config_module(self):
        config = self.wait.until(
            EC.element_to_be_clickable(device_config)
            )
        config.click()
        time.sleep(0.5)

    def enter_config_name(self):
        self.driver.find_element(*config_name).send_keys(device_config1)
        time.sleep(0.5)

    def enter__config_discription(self):
        self.driver.find_element(*config_Description).send_keys(config_dis)
        time.sleep(0.5)

    def enter_btn(self):
        next_btn = self.wait.until(
            EC.element_to_be_clickable(config_next_btn)
        )
        next_btn.click()
        time.sleep(0.5)

    def check_device_name(self):
        d_n = Select(self.driver.find_element(*config_device))
        d_n.select_by_value(config_device1)
        time.sleep(0.5)

    def enter_type(self):
        d_t = Select(self.driver.find_element(*config_type))
        d_t.select_by_visible_text(config_divce_type)
        time.sleep(0.5)

    def config_command_script(self):
        scr = self.wait.until(
            EC.presence_of_element_located(config_command)
        )
        scr.send_keys(command_script)
        time.sleep(0.5)

    def validate_script(self):
        self.driver.save_screenshot(script_screenshot_path)
        time.sleep(0.5)
    
    def push_config(self):
        save_btn = self.wait.until(
            EC.element_to_be_clickable(config_save)
        )
        save_btn.click()
        time.sleep(0.5)

    def config_ok_alert(self):
        alert = self.wait.until(
        EC.element_to_be_clickable(ok_button))
        alert.click()
        time.sleep(2) 

    def configer_validate(self):
        self.driver.save_screenshot(config_validation_screen_path)
        time.sleep(3)
    

