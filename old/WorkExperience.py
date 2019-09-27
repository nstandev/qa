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


class WorkExperience(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()

    def test_Work_Eperience(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.find_element_by_link_text('Work Experience').click()
        time.sleep(2)
        work_experience = self.driver.find_element_by_xpath('/html/body/div[1]/div/h3')
        if (work_experience.text == 'WORK EXPERIENCE'):
            print('Work Experience page reached')
            # Click the apply button
            self.driver.find_element_by_link_text('Apply Now').click()

            # Click the Agree button to accept T & C
            self.driver.find_element_by_partial_link_text('I AGREE').click()
            time.sleep(3)
            current_page = url + '/login/?next=/workexperience/pay/'
            if (self.driver.current_url == url + '/login/?next=/workexperience/pay/'):

                login_detail_we(self)
                self.driver.find_element_by_class_name('stripe-button-el').click()
                send_details(self)
                time.sleep(3)
                success_message = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/h2')

                if (success_message.text == 'Requirements Met'):
                    print('Work Experience Payment successful ')
                    print(success_message.text)
                    self.driver.find_element_by_link_text('Proceed').click()

                else:
                    print('Payment not successful for Work Experience')
                    self.driver.save_screenshot('ScreenShot/work_experience.png')
            else:
                print('I agree button not working')



        else:
            print('Work Experience page not reached')
            self.driver.save_screenshot('ScreenShot/work_experience.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
