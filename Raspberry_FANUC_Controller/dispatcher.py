import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


class Dispatcher:
    def __init__(self, trigger_register, enable_next_register):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        # chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=chrome_options,
                                        executable_path=r"C:\Users\RSK_Robotics\Desktop\Coding\Raspberry_kontroler\chromedriver.exe")
        self.trigger_register = trigger_register
        self.trigger_iVal = f"iVal{trigger_register.strip('R')}"
        self.enable_next_register = enable_next_register
        self.enable_next_iVal = f"iVal{enable_next_register.strip('R')}"
        print(f'Fanuc Dispatcher object created')

    def go_to_numeric_registers(self):
        '''Makes the broser get to numeric registers frame to enable selecting
        the registers via CSS_selectors'''
        self.browser.get('http://172.18.1.201/KAREL/COMMAIN')
        self.browser.switch_to.frame(
            self.browser.find_element(By.CSS_SELECTOR,
                                      "frame[name='frmList']"))
        numericRegisters = self.browser.find_element(By.LINK_TEXT,
                                                     'Numeric Registers')
        numericRegisters.click()

        time.sleep(0.3)
        self.browser.switch_to.parent_frame()
        time.sleep(0.3)
        self.browser.switch_to.frame(
            self.browser.find_element(By.CSS_SELECTOR,
                                      "frame[name='frmMain']"))
        time.sleep(0.3)

        print(f'Browser in numeric registers!')

    def send_trigger(self):
        '''Triggers the next robot movement (pulse on - off)'''
        Trigger_register = self.browser.find_element(By.NAME,
                                                     self.trigger_ival)
        time.sleep(0.3)
        Trigger_register.clear()
        Trigger_register.send_keys(0.3)
        Trigger_register.send_keys(Keys.RETURN)
        time.sleep(0.3)
        Trigger_register.clear()
        Trigger_register.send_keys(0)
        Trigger_register.send_keys(Keys.RETURN)
        print(f'Trigger register - trigger sent')

    def enable_next_cycle(self):
        '''Enables the next robot movement (stays on until robot shuts it off)'''
        Trigger_register = self.browser.find_element(By.NAME,
                                                     self.enable_next_iVal)
        Trigger_register.send_keys(Keys.CONTROL + "a")
        Trigger_register.send_keys(Keys.DELETE)
        Trigger_register.send_keys(0)
        Trigger_register.send_keys(Keys.ENTER)
        time.sleep(0.2)
        Trigger_register.send_keys(Keys.CONTROL + "a")
        Trigger_register.send_keys(Keys.DELETE)
        Trigger_register.send_keys(1)
        Trigger_register.send_keys(Keys.ENTER)
        time.sleep(0.2)

        print(f'Enable register - enable set to ON')

    def set_value_to_register(self, register, value):
        Sending_register = self.browser.find_element(
            By.NAME, f"iVal{register.strip('R')}")

        Sending_register.clear()
        time.sleep(0.1)
        Sending_register.send_keys(value)
        Sending_register.send_keys(Keys.RETURN)
        time.sleep(0.1)


    def dink(self):
        print(f'You got dinked!')
