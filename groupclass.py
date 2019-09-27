import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, generate_details, get_driver, get_parser, close_firefox

parser = get_parser()


class Groupclass(unittest.TestCase):

    def setUp(self):
        self.classes = []
        self.active_class = None
        self.logger = get_logger('Groupclass')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.maximize_window()

    def test_all_available_group_class_is_visible(self):
        self.driver.find_element_by_link_text('Group Class').click()
        self.classes = self.driver.find_elements_by_xpath("//div[@class='pull-right']/button")
        self.assertTrue(len(self.classes) > 0 or "None" in self.classes.text)

    def test_active_group_class_opens_the_registration_page(self):
        return
        self.driver.find_element_by_link_text('Group Class').click()
        c = self.driver.find_element_by_xpath("//div[@id='gsched']/div[2]/div/div/div[2]/button")
        self.driver.execute_script("arguments[0].click();", c)
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, "xpath=//input[@id='fullname']")))
            d = generate_details()
            self.driver.find_element_by_xpath("//div[@id='g2']/div").click()
            self.driver.find_element_by_xpath("xpath=//input[@id='fullname']").send_keys(d['fullname'])
            self.driver.find_element_by_xpath("xpath=//input[@id='email']").send_keys(d['email'])
            self.driver.find_element_by_xpath("xpath=//input[@id='password']").send_keys(
                parser.get('authentication', 'password'))
            self.driver.find_element_by_link_text("REGISTER NOW").click()
        except:
            raise AssertionError("Registration page did not open")

    def test_nonregistered_group_class_member_is_taken_to_the_payment_page(self):
        return
        d = generate_details()
        self.driver.find_element_by_link_text('Group Class').click()
        self.classes = self.driver.find_elements_by_xpath("//div[@class='pull-right']/button")
        # self.active_class = list(filter(lambda x: "Enroll" in x.text, self.classes))
        self.driver.execute_script("arguments[0].click();", self.active_class)

    def test_active_group_class_registration_page_single_access_success_for_a_new_user(self):
        pass

    def test_active_group_class_registration_page_subscription_success_for_a_new_user(self):
        pass

    def test_active_group_class_registration_page_success_shows_a_notification(self):
        pass

    def test_active_group_class_registration_page_success_sends_email(self):
        pass

    def test_active_group_class_registration_page_detects_registered_user(self):
        pass

    def test_active_group_class_registration_page_success_for_existing_user(self):
        pass

    def test_expired_groupclass_shows_expired(self):
        pass

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
