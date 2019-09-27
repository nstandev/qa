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


class LiveHelpTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)

    def test_live_help(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Live help').click()
        self.assertEqual(url + '/home/livehelp', self.driver.current_url)
        self.driver.find_element_by_link_text('Buy Now').click()
        time.sleep(3)

        if (self.driver.current_url == url + '/login/?next=/home/pay/livehelp'):
            # Login
            login_detail(self)

            # go to the pay url
            self.driver.get(url + '/home/pay/livehelp')
            self.driver.find_element_by_xpath("//*[@id='stripejsfilemain']/div/div[2]/button/span").click()
            time.sleep(3)
            # send card details
            send_details(self)
            time.sleep(2)
            message = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/span")
            print(message.text)
            self.assertIn("Congratulations, you have successfully subscribed", message.text)
        else:
            self.driver.find_element_by_partial_link_text('Pay with Card').click()
            # send card details
            send_details(self)
            time.sleep(2)
            message = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/span")
            print(message.text)
            self.assertIn("Congratulations, you have successfully subscribed", message.text)

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
