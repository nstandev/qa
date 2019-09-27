import os
import unittest

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, perform_login, get_parser, get_driver, close_firefox

parser = get_parser()
BASE_DIR = os.getcwd()
UPLOAD_XPATH = "//button[@class='btn btn-upload']"


class AccountSettings(unittest.TestCase):
    def setUp(self):

        self.logger = get_logger('AccountSettings')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_authenticated_user_can_access_account_settings_page(self):
        text = ""
        username = parser.get("authentication", 'username')
        password = parser.get("authentication", 'password')
        perform_login(self.driver, username, password,after_signup=False)
        self.driver.get(self.url.rstrip("/") + "/user/account/settings")
        try:
            text = self.driver.find_element_by_xpath("//h3[@class='hblue']").text
        except NoSuchElementException as e:
            print(e)
        self.assertTrue("Credentials" in text)
        # Todo self.assertTrue("Account" in self.driver.title)

        with self.subTest(name="authenticated_user_can_play_the_video"):
            self.driver.switch_to.frame(
                self.driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
                self.driver.switch_to.default_content()
            except Exception as e:
                print(e)
                raise AssertionError("Could not play video")

        with self.subTest(name="authenticated_user_invalid_file_upload_fails"):

            self.driver.find_element_by_id("upload-file").send_keys(BASE_DIR + "/documents/non_csv.png")
            self.driver.find_element_by_xpath(UPLOAD_XPATH).click()
            self.assertIn("csv files only",
                          self.driver.find_element_by_xpath("//div[@class='alert alert-danger']/p").text)

        with self.subTest(name="authenticated_user_invalid_csv_upload_fails"):
            self.driver.find_element_by_id("upload-file").send_keys(BASE_DIR + "/documents/invalid_key.csv")
            self.driver.find_element_by_xpath(UPLOAD_XPATH).click()
            self.assertIn("error while validating credentials",
                          self.driver.find_element_by_xpath(
                              "//div[@class='alert alert-danger']/p").text)

        with self.subTest(name="authenticated_user_cannot_start_machine_with_invalid_csv"):
            self.assertEqual("Invalid",
                             self.driver.find_element_by_xpath(
                                 "//div[@class='col-xs-12 col-sm-12 col-lg-6 mgb50'][1]/p[@class='hred rnd-back2']").text)

        with self.subTest(name="authenticated_user_valid_csv_upload_succeeds"):
            self.driver.find_element_by_id("upload-file").send_keys(BASE_DIR + "/documents/valid_key.csv")
            self.driver.find_element_by_xpath(UPLOAD_XPATH).click()
            self.assertIn("Valid",
                          self.driver.find_element_by_xpath(
                              "//div[@class='col-xs-12 col-sm-12 col-lg-6 mgb50'][1]/p").text)

        with self.subTest(name="authenticated_user_can_start_machine_with_valid_csv"):
            pass

    def tearDown(self):
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
