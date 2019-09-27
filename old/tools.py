import time
import unittest
from configparser import ConfigParser

from login import *
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options

parser = ConfigParser()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

parser.read("credentials.ini")
parser.read("settings.ini")


class ToolsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        self.driver.get('http://int.linuxjobber.com/login')
        login_detail(self)

    # Monitoring tools
    def test_monitoring(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Monitoring icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[1]/ul/li[1]/a/span').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Monitoring Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Monitoring Page not reached')
                    self.driver.save_screenshot('ScreenShot/monitoring.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Monitoring Page not reached')
                self.driver.save_screenshot('ScreenShot/monitoring.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Monitoring Icon not found')
                self.driver.save_screenshot('ScreenShot/monitoring.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/monitoring.png')

    # Configuration tools
    def test_configuraion(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Configuration icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[2]/ul/li[1]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Configuartion Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Monitoring Page not reached')
                    self.driver.save_screenshot('ScreenShot/configuration.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Monitoring Page not reached')
                self.driver.save_screenshot('ScreenShot/configuration.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Configuration Icon not found')
                self.driver.save_screenshot('ScreenShot/configuration.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/configuration.png')

    # Automation tools
    def test_automation(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Automation icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[3]/ul/li[1]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Automation Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Automation Page not reached')
                    self.driver.save_screenshot('ScreenShot/automation.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Automation Page not reached')
                self.driver.save_screenshot('ScreenShot/automation.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Automation Icon not found')
                self.driver.save_screenshot('ScreenShot/automation.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/automation.png')

    # Version Control tools
    def test_version_control(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Version Control icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[1]/ul/li[2]/a/span').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Version Control Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: VErsion Control Page not reached')
                    self.driver.save_screenshot('ScreenShot/version_control.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Version Control Page not reached')
                self.driver.save_screenshot('ScreenShot/version_control.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Version Control Icon not found')
                self.driver.save_screenshot('ScreenShot/version_control.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/version_control.png')

    # FileSystems tools
    def test_filesystems(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the File Systems icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[2]/ul/li[2]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: File Systems Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: File Systems Page not reached')
                    self.driver.save_screenshot('ScreenShot/filesystems.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: File Systems Page not reached')
                self.driver.save_screenshot('ScreenShot/filesystems.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: File Systems Icon not found')
                self.driver.save_screenshot('ScreenShot/filesystems.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/filesystems.png')

    # Cloud tools
    def test_cloud_tools(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Cloud Tools icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[3]/ul/li[2]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Cloud Tools Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Cloud Tools Page not reached')
                    self.driver.save_screenshot('ScreenShot/cloud_tools.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Cloud Tools Page not reached')
                self.driver.save_screenshot('ScreenShot/cloud_tools.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Cloud Tools Icon not found')
                self.driver.save_screenshot('ScreenShot/cloud_tools.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/cloud_tools.png')

    # Application Servers
    def test_application_servers(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Application Servers icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[1]/ul/li[3]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Application Servers Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Application Servers Page not reached')
                    self.driver.save_screenshot('ScreenShot/application_servers.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Application servers Page not reached')
                self.driver.save_screenshot('ScreenShot/application_servers.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Application Servers Icon not found')
                self.driver.save_screenshot('ScreenShot/application_servers.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/application_servers.png')

    # Authentication
    def test_authentication(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(5)
        try:
            # Click the tools dropdown
            self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div[2]/nav/ul/li[2]/a').click()
            self.driver.implicitly_wait(10)
            try:
                # Click the Authentication icon in the dropdown
                self.driver.find_element_by_xpath('//*[@id="tool"]/div/div[1]/ul/li[4]/a').click()
                load_button = self.driver.find_element_by_xpath('//*[@id="loadMore"]/a')
                if (load_button.text == 'Load More Tools'):
                    print('Test Passed: Authentication Page Reached')
                    print(load_button.text)
                else:
                    print('Test Failed: Authentication Page not reached')
                    self.driver.save_screenshot('ScreenShot/authentication.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Authentication Page not reached')
                self.driver.save_screenshot('ScreenShot/authentication.png')

            except NoSuchElementException as exceptions:
                print('TEst Failed: Authentication Icon not found')
                self.driver.save_screenshot('ScreenShot/authentication.png')

        except NoSuchElementException as exceptions:
            print('TEst Failed: Tools Dropdown not found')
            self.driver.save_screenshot('ScreenShot/authentication.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
