from selenium.webdriver.common.by import By
username_locator = By.ID, "username"
password_locator = By.ID, "password"
login_button_locator = By.CLASS_NAME, "btn-login"
dashborad_locater = By.XPATH,"//*[@class='app-dashboard-title']" 
#software_update_locator = By.XPATH, "//a[@class='nav-item']"
software_update_locator = (By.XPATH, "//your_xpath")

###device manage module locators
device_mangement = By.XPATH, '//a[@href="#device-management"]'
device_management = device_mangement
device_name = By.ID, "deviceName"
device_ip = By.ID, "deviceIp"
device_uname = By.ID, "deviceUname"
device_password = By.ID, "devicePassword"
device_type = (By.ID, "deviceType")
device_version = By.ID, "deviceVersion"
device_protocal = By.ID,"deviceProtocol"
add_device_btn = By.XPATH, '(//button[@class="btn-primary"])[4]'


##software update module locatorsa  
software_update_btn = By.XPATH,'//*[@href="#software-update"]'
file_upload = By.ID,'imageFile'
next_button1 = By.ID,'nextStep1'

select_devies = By.XPATH,'//*[@id="selectAllDevices"]'
next_btn2 = By.ID,'nextStep2'
job_name_locate = By.ID,'jobName'
run_now = By.XPATH,'//*[@class="radio-card-content"]'
start_job_btn3 = By.ID,'startJob'



JOB_NAME =(By.XPATH, "//table[@class='jobs-table']/tbody/tr[1]/td[2]")
STATUS = By.XPATH, "//table[@class='jobs-table']/tbody/tr[1]/td[3]"
RUN_STATUS = By.XPATH,"//table[@class='jobs-table']/tbody/tr[1]/td[4]"
RUN_TIME = By.XPATH, "//table[@class='jobs-table']/tbody/tr[1]/td[5]"
DURATION = By.XPATH, "//table[@class='jobs-table']/tbody/tr[1]/td[6]"

#device config locators
device_config = By.XPATH,'//*[@href="#device-config"]'
config_name = By.ID,"cfgName"
config_Description = By.ID,"cfgDescription"
config_next_btn = By.ID,"cfgNext"
config_device = By.ID,"cfgDeviceSelect"
config_type = By.ID,"cfgPlatform"
config_command = By.ID,"cfgScript"
config_save = By.ID,"cfgSave"
ok_button = By.XPATH,'//button[@id="configPushSuccessOk"]'

