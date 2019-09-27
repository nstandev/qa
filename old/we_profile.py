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
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

parser.read("credentials.ini")
parser.read("settings.ini")


class WorkExperienceProfile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/login')
        login_detail(self)

    # To check Profile you need to RUn with a User that has signed up for WE

    def test_we_profile_form(self):
        url = parser.get('site_to_test', 'url')
        # Fill the WE Profile Form
        self.driver.get(url + '/workexperience/apply/')
        time.sleep(2)
        self.driver.find_element_by_name('types').send_keys('DevOps')
        time.sleep(2)
        self.driver.find_element_by_name('current_position').send_keys('Developer')
        time.sleep(2)
        self.driver.find_element_by_name('state').send_keys('Michigan')
        time.sleep(2)
        self.driver.find_element_by_name('income').send_keys('$5000')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[7]/input').click()
        WE_Profile_Page = self.driver.find_element_by_xpath('/html/body/div[1]/div/h1')
        print(WE_Profile_Page.text)

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
