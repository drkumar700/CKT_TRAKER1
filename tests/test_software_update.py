from pages.login_page import LoginPage
from pages.softwer_update_module import SoftwerUpdate

class TestSoftwareUpdate:
    def test_software(self):
        login_page = LoginPage()
        login_page.open_browser()
        login_page.username()
        login_page.password()
        login_page.click_login()

        software_module= SoftwerUpdate(login_page.driver)
        software_module.navi_softwer_update_page()
        print("navigate sucssesfull to software update page ")
        software_module.upload_os_file()
        software_module.next_btn()
        print("selected required OS")

        software_module.select_devies()
        software_module.next_btn2()
        print("select devices ")
        software_module.giving_job_name()
        software_module.run_now()  
        print("given job name and selected run noe")

        software_module.start_job() 
        print("jon was sucsuesfully running")

        software_module.verify_first_job()     
