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


class CompanyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/login')
        login_detail(self)

    # Java 1:1 Training
    def test_java(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        try:
            # Click the Java slide on the 1:1 section
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/a/img').click()
            page_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (page_title.text == 'Java'):
                print('Test Passed: Java Page Reached')
                print(page_title.text)
            else:
                print('Test Failed: Java Page not Reached')
                print(page_title.text)
                self.driver.save_screenshot('ScreenShot/java.png')
        except NoSuchElementException as exceptions:
            print('Test Failed: COuld not Find the Java Section on 1:1')
            self.driver.save_screenshot('ScreenShot/java.png')

    # Linux 1:1 Training
    def test_linux(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        try:
            # Click the Linux slide on the 1:1 section
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/a/img').click()
            page_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (page_title.text == 'Linux Fundamentals'):
                print('Test Passed: Linux Page Reached')
                print(page_title.text)
            else:
                print('Test Failed: linux Page not Reached')
                print(page_title.text)
                self.driver.save_screenshot('ScreenShot/linux.png')
        except NoSuchElementException as exceptions:
            print('Test Failed: COuld not Find the Linux Section on 1:1')
            self.driver.save_screenshot('ScreenShot/linux.png')

    # AWS 1:1 Training
    def test_aws(self):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        try:
            # Click the AWS slide on the 1:1 section
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/a/img').click()
            page_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (page_title.text == 'Amazon AWS'):
                print('Test Passed: AWS Page Reached')
                print(page_title.text)
            else:
                print('Test Failed: AWS Page not Reached')
                print(page_title.text)
                self.driver.save_screenshot('ScreenShot/aws.png')
        except NoSuchElementException as exceptions:
            print('Test Failed: COuld not Find the AWS Section on 1:1')
            self.driver.save_screenshot('ScreenShot/aws.png')

    # View More 1:1 Training
    def test_view_more(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        try:
            # Click the View More slide on the 1:1 section
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/a/img').click()
            time.sleep(3)
            page = url + '/courses/userinterest'
            if (page == self.driver.current_url):
                print('Test Passed: View More Page Reached')
                print(self.driver.current_url)
            else:
                print('Test Failed: View More Page not Reached')
                print(self.driver.current_url)
                self.driver.save_screenshot('ScreenShot/aws.png')
        except NoSuchElementException as exceptions:
            print('Test Failed: COuld not Find the AWS Section on 1:1')
            self.driver.save_screenshot('ScreenShot/aws.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
