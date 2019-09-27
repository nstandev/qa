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
parser.read('settings.ini')


class CompanyFooterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options,
                                       executable_path=r"C:\Users\Jide\Desktop\Training\Projects\LinuxJobberProject\Testing\chromedriver.exe")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        time.sleep(3)

    # About Us
    def test_about_us(self):
        try:
            # Click the About us link
            self.driver.find_element_by_partial_link_text('About US').click()
            time.sleep(3)
            page_header = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')

            if (page_header.text == 'About Us'):
                print('Test Passed: About Us Page Reached')
                print(page_header.text)
            else:
                print('TEst Failed: about Us page could not be Found')
                print(page_header.text)
                self.driver.save_screenshot('ScreenShot/about_us.png')

        except NoSuchElementException as exceptions:
            print('Test Failed: Could not find About Us Link')
            self.driver.save_screenshot('ScreenShot/about_us.png')

    # Location
    def test_locations(self):
        try:

            # Click the Locations link
            self.driver.find_element_by_partial_link_text('Location').click()
            time.sleep(3)
            page_header = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')

            if (page_header.text == 'Training Location'):
                print('Test Passed: Locations Page Reached')
                print(page_header.text)
            else:
                print('TEst Failed: Locations page could not be Found')
                print(page_header.text)
                self.driver.save_screenshot('ScreenShot/locations.png')

        except NoSuchElementException as exceptions:
            print('Test Failed: Could not find Locations Page in drop down')
            self.driver.save_screenshot('ScreenShot/locations.png')

    # Policies
    def test_policies(self):
        try:

            # Click the Policies link
            self.driver.find_element_by_partial_link_text('Policies').click()
            time.sleep(3)
            page_header = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')

            if (page_header.text == 'Our Policy'):
                print('Test Passed: Policies Page Reached')
                print(page_header.text)
            else:
                print('TEst Failed: Policies page could not be Found')
                print(page_header.text)
                self.driver.save_screenshot('ScreenShot/policies.png')

        except NoSuchElementException as exceptions:
            print('Test Failed: Could not find Policies Page in drop down')
            self.driver.save_screenshot('ScreenShot/policies.png')

    # Contact Us
    def test_contact_us(self):
        try:

            # Click the Contact Us link
            self.driver.find_element_by_partial_link_text('Contact Us').click()
            time.sleep(3)
            page_header = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')

            if (page_header.text == 'Chat with Us'):
                print('Test Passed: Contact Us Page Reached')
                print(page_header.text)
            else:
                print('TEst Failed: Contact Us page could not be Found')
                print(page_header.text)
                self.driver.save_screenshot('ScreenShot/contact_us.png')

        except NoSuchElementException as exceptions:
            print('Test Failed: Could not find Contact Us Page in drop down')
            self.driver.save_screenshot('ScreenShot/contact_us.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
