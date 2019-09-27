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


class Student_Services(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/login')
        login_detail(self)

    def test_Student_Packages_standard_plan(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_link_text('Student Packages').click()
        time.sleep(2)
        student_packages = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/h1')
        if (student_packages.text == 'Choose a Package'):
            print('Student Package page reached')
            self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[1]/div/div[3]/a').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            send_details(self)
            time.sleep(2)

            print('Standard Payment Successful')
            time.sleep(2)

            # go to a course and check if you access the videos
            self.driver.get(url + '/courses/Linux_Proficiency/topics/')
            self.driver.find_element_by_partial_link_text('Network Configuration and Management').click()
            time.sleep(3)
            payment_url = url + '/access_course'
            if (self.driver.current_url == payment_url):
                print('Standard Plan User Still cannot access course after payment')
            else:
                print('standard Plan User can Access course')

        else:
            print('Student Package page not reached')
            self.driver.save_screenshot('ScreenShot/student.png')

    def test_Student_Packages_Premium_plan(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_link_text('Student Packages').click()
        time.sleep(2)
        student_packages = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/h1')
        if (student_packages.text == 'Choose a Package'):
            print('Student Package page reached')
            self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div/div/a').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            send_details(self)
            time.sleep(3)
            print('Premium Payment Successful')
            time.sleep(2)
            # go to a course and check if you access the videos
            self.driver.get(url + '/courses/Linux_Proficiency/topics/')
            self.driver.find_element_by_partial_link_text('Network Configuration and Management').click()
            time.sleep(3)
            payment_url = url + '/access_course'
            if (self.driver.current_url == payment_url):
                print('Premium Plan User Still cannot access course after payment')
            else:
                print('Premium Plan User can Access course')


        else:
            print('Student Package page not reached')
            self.driver.save_screenshot('ScreenShot/student.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
