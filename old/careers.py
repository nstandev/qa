import time
import unittest
from configparser import ConfigParser

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options

parser = ConfigParser()
# options = webdriver.ChromeOptions()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

parser.read("credentials.ini")
parser.read("settings.ini")


class CareerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)

    ######################################################
    # Part time Job Application #
    ######################################################

    def test_part_time(self):
        try:
            # Click the career icon
            self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div[1]/nav/ul/li[4]/a').click()
            self.driver.implicitly_wait(5)
            # click the part-time icon
            self.driver.find_element_by_xpath('//*[@id="company"]/div/div[2]/ul/li/a').click()

            # Fill the form
            self.driver.find_element_by_xpath('//*[@id="JobFname"]').send_keys('Part-Time Frontend Developer')
            fullname = parser.get('careers', 'fullname')
            email = parser.get('careers', 'email')
            phone = parser.get('careers', 'phone')
            self.driver.find_element_by_name('fullname').send_keys(fullname)
            self.driver.find_element_by_name('email').send_keys(email)
            self.driver.find_element_by_name('phone').send_keys(phone)

            self.driver.find_element_by_name('cv').send_keys(r"/home/nathan/Documents/Resume/Pelumi_CV.pdf")

            self.driver.find_element_by_xpath('//*[@id="formd"]/div[2]/div[2]/div[1]/label[1]').click()
            self.driver.find_element_by_xpath('//*[@id="formd"]/div[2]/div[2]/div[2]/div/button').click()

            feedback_message = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span')
            if (feedback_message.text == 'Application Submitted'):
                print('Part-TIme Application submitted Successsfully')
                print(feedback_message.text)
            else:
                print('Part-Time Application NOT submitted successfully')
                print(feedback_message.text)

        except NoSuchElementException as exceptions:
            print('Could not locate the Career Icon')

    ####################################################
    # FUll time Application#
    ####################################################

    def test_full_time(self):
        try:
            # Click the career icon
            self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div[1]/nav/ul/li[4]/a').click()
            self.driver.implicitly_wait(5)
            # Click the full time application
            self.driver.find_element_by_xpath('//*[@id="company"]/div/div[1]/ul/li/a/span/i').click()
            # Click the Linux Administrator Apply Button
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a').click()

            # Fill Form for Full Time
            fullname = parser.get('careers', 'fullname')
            email = parser.get('careers', 'email')
            phone = parser.get('careers', 'phone')
            self.driver.find_element_by_name('fullname').send_keys(fullname)
            self.driver.find_element_by_name('email').send_keys(email)
            self.driver.find_element_by_name('phone').send_keys(phone)
            self.driver.find_element_by_name('resume').send_keys(r"/home/nathan/Documents/Resume/Pelumi_CV.pdf")

            self.driver.find_element_by_xpath('//*[@id="formd"]/div[2]/div[2]/div/div/button').click()
            feedback_message = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span')
            if (feedback_message.text == 'Application Submitted'):
                print('Application Full Time Successfully')
                print(feedback_message.text)
            else:
                print('Full Time Application NOT submitted')
                print(feedback_message.text)

        except NoSuchElementException as exceptions:
            print('Could not locate the Career Link')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
