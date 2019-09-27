import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_driver, get_parser, perform_login, perform_registration, send_card_details, close_firefox

parser = get_parser()
PROJECT_XPATH = "//a[contains(@href,'/course') and @class='projlink']/div/div"


class Projects(unittest.TestCase):
    print("================ PROJECTS ===================\n")
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(parser.get('site_to_test', 'url'))
        self.driver.find_element_by_link_text("Projects").click()

    def test_project_page_is_active(self):

        try:
            self.driver.find_element_by_xpath("//h1[@class='projbanh1']")
            self.assertIn("projects", self.driver.find_element_by_xpath("//h1[@class='projbanh1']").text.lower())
        except Exception as e:
            print(e)
            raise AssertionError("Failed")

    def test_guest_is_taken_to_log_in(self):
        self.driver.find_element_by_xpath(PROJECT_XPATH).click()
        self.driver.find_element_by_link_text("Start Project").click()
        self.assertTrue("Log In" in self.driver.title)

    def test_authenticated_user_redirected_to_selected_project(self):
        self.driver.find_element_by_xpath(PROJECT_XPATH).click()
        previous_url = self.driver.current_url
        self.driver.find_element_by_link_text("Start Project").click()
        perform_login(self.driver, after_signup=False)
        self.assertEqual(previous_url, self.driver.current_url)

    def test_authenticated_user_subscription_success(self):
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])
        self.driver.find_element_by_link_text("Projects").click()
        x = self.driver.find_elements_by_xpath(PROJECT_XPATH)
        # self.driver.find_elements_by_xpath(PROJECT_XPATH).click()
        x[-1].click()
        self.driver.find_element_by_link_text("Start Project").click()
        try:
            # self.driver.find_element_by_xpath("//button[@class='stripe-button-el']/span")
            send_card_details(self.driver)
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))
            self.assertEqual("Congratulations, you have successfully subscribed for our Standard Plan package.",
                             self.driver.find_element_by_xpath(
                                 "//div[@class='alert alert-success']").text)
            # todo on subscription, return to the item paid for
            with self.subTest(name="test_authenticated_user_redirect_on_subscription_success"):
                pass
        except:
            raise AssertionError("Failed")

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
