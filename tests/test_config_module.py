from pages.login_page import LoginPage
from pages.device_config_module import DeviceConfig
from pages.device_manage_module import DeviceManageModule


class TestDeviceConfig:
    def test_device_config(self):
        login_page = LoginPage()
        login_page.open_browser()
        login_page.username()
        login_page.password()
        login_page.click_login()
        print("login suscsusfully")
       
        device_module = DeviceManageModule(login_page.driver)
        device_module.naviagete_to_device_page()
        device_module.enter_device_name()
        device_module.enter_device_ip()
        device_module.enter_device_uname()
        device_module.enter_device_password()
        device_module.enter_device_type()
        device_module.enter_device_version()
        device_module.enter_device_protocal()
        device_module.click_add_device()
        print("device added sucsusfully")

        device_test = DeviceConfig(login_page.driver)
        device_test.navigate_config_module()
        print("navigatedsucsusfully")

        device_test.enter_config_name()
        print("giving config name ")

        device_test.enter__config_discription()
        print("given config discription")

        device_test.enter_btn()
        
        device_test.check_device_name()
        device_test.enter_type()
        device_test.enter_btn()
        print("select device and configer type")

        device_test.config_command_script()
        device_test.enter_btn()
        print("give command for config")

        device_test.validate_script()
        device_test.push_config()
        print("push config command")

        device_test.config_ok_alert()
        device_test.configer_validate()

        print("device configer and validation  sucsusfully ")





        
