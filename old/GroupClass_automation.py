import time
import unittest
from configparser import ConfigParser

from login import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from stripe_card_test import *

parser = ConfigParser()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
options.add_argument('--disable-gpu')

parser.read("credentials.ini")
parser.read("settings.ini")


class GroupClassTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def test_GroupClass_python(self):
        self.driver.get('http://stage.linuxjobber.com')
        self.driver.find_element_by_link_text('Group Class').click()
        group_class = self.driver.find_element_by_xpath('/html/body/h2')
        if (group_class.text == 'Why Join Group Class?'):
            print('Group Class Reached')
            self.driver.find_element_by_xpath('//*[@id="force-b"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="c1"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="fullname"]').send_keys('Joshua Kingsley')
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('king@test.com')
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('my')
            self.driver.find_element_by_xpath('//*[@id="button"]').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            send_details(self)
            time.sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('/html/body/p/a').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            print("User has joined Python GroupClass")
        else:
            print('Group Class not Reached')
            self.driver.save_screenshot('ScreenShot/group_class.png')

    def test_GroupClass_Django(self):
        self.driver.get('http://int.linuxjobber.com')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Group Class').click()
        time.sleep(2)
        group_class = self.driver.find_element_by_xpath('/html/body/h2')
        if (group_class.text == 'Why Join Group Class?'):
            print('Group Class Reached')
            self.driver.find_element_by_xpath('//*[@id="force-b"]/h4').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="c1"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="fullname"]').send_keys('Doris Jenni')
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('jenni@test.com')
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('my')
            self.driver.find_element_by_xpath('//*[@id="button"]').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            send_details(self)
            time.sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('/html/body/p/a').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            print("User has joined Django GroupClass")
        else:
            print('Group Class not Reached')
            self.driver.save_screenshot('ScreenShot/group_class.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
