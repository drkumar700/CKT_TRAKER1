from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pages.login_page import LoginPage
from helpers.variables import *
from helpers.locators import *
import time

class SoftwerUpdate:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def navi_softwer_update_page(self):
        soft_page = self.wait.until(EC.element_to_be_clickable(software_update_btn))
        soft_page.click()
        time.sleep(0.5)

    def upload_os_file(self):
        self.wait.until(EC.presence_of_element_located(file_upload))
        up_file = self.driver.find_element(*file_upload)
        if not up_file.is_displayed():
            self.driver.execute_script("arguments[0].style.display='block';", up_file)
        up_file.send_keys(os_path)
        time.sleep(0.5)

    def next_btn(self):
        nxt = self.wait.until(EC.element_to_be_clickable(next_button1))
        nxt.click()
        time.sleep(0.5)

    def select_devies(self):
        selection=self.wait.until(
            EC.element_to_be_clickable(select_devies)
            )
        selection.click()
        time.sleep(0.5)

    def next_btn2(self):
        next = self.wait.until(
            EC.element_to_be_clickable(next_btn2)
            )
        next.click()
        time.sleep(0.5)

    def giving_job_name(self):
        self.driver.find_element(*job_name_locate).send_keys(job_name)
        time.sleep(0.5)

    def run_now(self):
        button = self.wait.until(
            EC.element_to_be_clickable(run_now)
        )
        button.click()
        time.sleep(0.5)

    def start_job(self):
        button3 = self.wait.until(
            EC.element_to_be_clickable(start_job_btn3)
        )
        button3.click()
        time.sleep(0.5)

        time.sleep(3)
    def verify_first_job(self):
        # Wait until the first row is visible
        row = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//table/tbody/tr[1]")
            )
        )
        time.sleep(0.5)
        
        job_name = self.driver.find_element(*JOB_NAME).text.strip()
        status = self.driver.find_element(*STATUS).text.strip()
        run_status = self.driver.find_element(*RUN_STATUS).text.strip()
        run_time = self.driver.find_element(*RUN_TIME).text.strip()
        duration = self.driver.find_element(*DURATION).text.strip()

        print("Job Name   :", job_name)
        print("Status     :", status)
        print("Run Status :", run_status)
        print("Run Time   :", run_time)
        print("Duration   :", duration)

        # Assertions
        assert status == "Completed", f"Expected Completed but got {status}"
        assert run_status == "Success", f"Expected Success but got {run_status}"
        
        print(f"Duration = {duration}")        
        
    

        

       
