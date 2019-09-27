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


class Resume_Services(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/login')
        login_detail(self)

    def test_Resume_Services(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('Resume Services').click()
        time.sleep(2)
        resume_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
        if (resume_title.text == 'RESUME PREPARATION'):
            print('Resume page reached')
            self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/div/a').click()
            print('Purchasing Resume')
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            self.driver.switch_to.frame("stripe_checkout_app")
            self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys('sobby04@yahoo.co.uk')
            time.sleep(2)
            self.driver.switch_to.default_content()
            time.sleep(2)
            send_details(self)
            time.sleep(2)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath('//*[@id="id_resume"]').send_keys(r"C:\Users\Jide\Downloads\quiz.py")
            time.sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div[2]/div/div/div/form/fieldset/div[2]/div[2]/div/input').click()
            print("Resume submitted Successfully")
        else:
            print('Resume page not reached')
            self.driver.save_screenshot('ScreenShot/resume.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
