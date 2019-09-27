import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, perform_login, send_card_details, perform_registration, get_parser, \
    get_driver, close_firefox

parser = get_parser()

TRY_FREE_XPATH = "//nav/ul[@class='nav navbar-nav navbar-right main-nav']/li[@class=' sub-menu ']/a"


class TryFree(unittest.TestCase):
    print("============= TRY FREE ==================\n")
    def setUp(self):
        self.logger = get_logger('TryFree')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def test_try_free_button_is_visible_on_page(self):
        print(" + test_try_free_button_is_visible_on_page \n".upper())

        self.assertEqual("TRY FREE",
                         self.driver.find_element_by_xpath(TRY_FREE_XPATH).text.upper())

    def test_guest_user_cannot_access_try_free_page_unless_registered(self):
        print(" + test_guest_user_cannot_access_try_free_page_unless_registered \n".upper())

        self.driver.find_element_by_xpath(TRY_FREE_XPATH).click()
        try:
            self.driver.find_element_by_xpath(
                "//div[@class='col-md-4 reg-sidebar']/div[@class='reg-sidebar-inner text-center']/h3")
        except NoSuchElementException:
            return True
        else:
            raise AssertionError("Guest user could access page without registering")

    def test_registered_user_payment_succeeds(self):
        print(" + test_registered_user_payment_succeeds \n".upper())

        data = perform_registration(self.driver)
        perform_login(self.driver, data['username'])
        self.driver.find_element_by_xpath(TRY_FREE_XPATH).click()
        send_card_details(self.driver)
        wait = WebDriverWait(self.driver, 30)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))
            with self.subTest(name="test_user_roles_changes_role_on_payment"):
                print(" + test_user_roles_changes_role_on_payment \n".upper())

                self.driver.get(self.url)

                try:
                    cli = self.driver.find_element_by_xpath("//div[@class='col-md-3 col-sm-4 col-xs-12'][2]/ul/li[1]/a")
                    self.driver.execute_script("arguments[0].click();", cli)
                    self.assertNotIn("No Access",
                                     self.driver.find_elements_by_xpath(
                                         "//div[@class='level-right']"))
                except NoSuchElementException as e:
                    raise AssertionError("Could not navigate to course: \n {}".format(e))

        except Exception as e:
            print(e)
            raise AssertionError("Payment did not succeed")

    @unittest.skip("Still trying to figure a solution")
    def test_user_permission_is_revoked_on_trial_expiry(self):
        pass

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
