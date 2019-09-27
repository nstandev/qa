import time
import unittest
from configparser import ConfigParser

from selenium import webdriver
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


class CreateUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)

    def test_create_user(self):
        # Go to the signup page

        self.driver.find_element_by_link_text('Sign Up').click()

        time.sleep(3)
        fullname = parser.get('create_user', 'fullname')
        email = parser.get('create_user', 'email')
        password = parser.get('create_user', 'password')
        self.driver.find_element_by_name('fullname').send_keys(fullname)
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_class_name('btn-loginform').click()
        time.sleep(3)

        success_message = self.driver.find_element_by_xpath('//*[@id="introduction-login"]/div/div/div[1]/div/h5[1]')
        error_message = self.driver.find_element_by_xpath('//*[@id="introduction-login"]/div/div/div[1]/div/form/p[2]')

        if (success_message):
            print(success_message.text)

        else:
            print(error_message.text)

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
