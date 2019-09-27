import time
import unittest
from configparser import ConfigParser

from login import *
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from stripe_card_test import send_details

parser = ConfigParser()
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

parser.read("credentials.ini")
parser.read("settings.ini")


class TryFree(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def test_try_free(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        time.sleep(3)
        # Get the try try free link
        try:
            self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div[1]/nav/ul/li[5]/a').click()
            # self.driver.find_element_by_partial_link_text('Try Free').click()
            # Login
            login_detail(self)
            time.sleep(2)

            # Click the pay with card button
            self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
            time.sleep(2)
            # Send card details
            send_details(self)
            try:
                message = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/span")
                print(message.text)
                self.assertIn("Congratulations, you have successfully subscribed", message.text)

                # Wait for 10 sec and check if you can access a course
                time.sleep(5)
                # Try to access a course after payment
                self.driver.get(url + '/courses/Linux_Proficiency/topics/')
                self.driver.find_element_by_partial_link_text('Understanding Server Administration').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course after try free payment')
                    print(self.driver.current_url)
                else:
                    print('User can access course after Try Free Payment')
                    print(self.driver.current_url)

            except NoSuchElementException as exceptions:
                print('Payment not successful')


        except NoSuchElementException as exceptions:
            print('Could not locate Try free button')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
