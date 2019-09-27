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


class gain_experience(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)

    # def test_Adult_Experience(self):
    #     url = parser.get('site_to_test', 'url')
    #     self.driver.find_element_by_partial_link_text('Gain Experience').click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('/html/body/section[5]/div/div[2]/div[2]/a').click()
    #     time.sleep(2)
    #     WE_page = url+'/workexperience/'
    #     if (self.driver.current_url == WE_page):
    #         print ('WOrk Experience Page reahed from Gain Experience')
    #         print (self.driver.current_url)
    #     else:
    #         print ('Adult Expereience Button Failed')

    def test_student_internship(self):

        url = parser.get('site_to_test', 'url')
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_partial_link_text('Gain Experience').click()
        time.sleep(2)
        gain_experience = self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[1]/strong/h1')
        if (gain_experience.text == 'Work Experience While You Learn'):
            print('Gain Experience Page reached')
            self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[1]/a').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/a').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/section[5]/div/div[1]/div[2]/a').click()
            time.sleep(2)
            print('student page reached')
            self.driver.find_element_by_xpath('/html/body/section[1]/div/div/a').click()
            time.sleep(2)
            firstname = parser.get('internship', 'firstname')
            lastname = parser.get('internship', 'lastname')
            phone = parser.get('internship', 'phone')
            email = parser.get('internship', 'email')
            Address = parser.get('internship', 'Address')
            college = parser.get('internship', 'college')
            country = parser.get('internship', 'country')
            course = parser.get('internship', 'course')
            experience = parser.get('internship', 'experience')

            self.driver.find_element_by_name('firstname').send_keys(firstname)
            self.driver.find_element_by_name('lastname').send_keys(lastname)
            self.driver.find_element_by_name('phone').send_keys(phone)
            self.driver.find_element_by_name('email').send_keys(email)
            self.driver.find_element_by_name('Address').send_keys(Address)
            self.driver.find_element_by_name('college').send_keys(college)
            self.driver.find_element_by_name('country').send_keys(country)
            self.driver.find_element_by_name('course').send_keys(course)
            self.driver.find_element_by_name('experience').send_keys(experience)
            self.driver.find_element_by_xpath('//*[@id="id_resume"]').send_keys(
                r"C:\Users\Jide\Downloads\scrum_instructions.txt")
            self.driver.find_element_by_xpath('//*[@id="add_ser_prd_btn"]').click()
            print("Gain Experience applied for")
        else:
            print('Gain Experience Page not reached')
            self.driver.save_screenshot('ScreenShot/gain_experience.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
