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


class InPersonTraining(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        self.driver.get('http://stage.linuxjobber.com')

    def test_in_person_training(self):
        # Click the in_person_training Link
        self.driver.find_element_by_link_text('In-Person Training').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('Buy Now').click()
        login_detail_we(self)
        self.driver.find_element_by_xpath('//*[@id="stripejsfilemain"]/div/div[2]/button/span').click()
        send_details(self)
        time.sleep(5)
        success_message = self.driver.find_element_by_class_name('alert-success')
        print(success_message.text)
        if (success_message.text == 'Congratulations, you have successfully subscribed for live help'):
            print(' In Live Person Payment Successful')
            print(success_message.text)
        else:
            print('InLive Person Payment not Successful')
            self.driver.save_screenshot('ScreenShot/in_person.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
