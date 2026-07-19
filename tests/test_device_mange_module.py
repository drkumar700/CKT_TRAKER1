from pages.device_manage_module import DeviceManageModule
from pages.login_page import LoginPage


class TestDeviceManageModule:
    def test_device_management_flow(self):
        login_page = LoginPage()
        login_page.open_browser()
        login_page.username()
        login_page.password()
        login_page.click_login()
        print("login suscsusfully")

        device_module = DeviceManageModule(login_page.driver)
        #navigate to devicemanagement module
        device_module.naviagete_to_device_page()
        print("navigated to device management module")

        device_module.enter_device_name()
        device_module.enter_device_ip()
        print("device and ip added sucesfully")

        device_module.enter_device_uname()
        device_module.enter_device_password()
        print("divec uname and pass entered sucsusfully")

        device_module.enter_device_type()
        device_module.enter_device_version()
        device_module.enter_device_protocal()
        print("device type and version  and protocol entered sucsusfully")

        device_module.click_add_device()

        print("device added sucsusfully")

        login_page.driver.quit()
        print("driver closed")