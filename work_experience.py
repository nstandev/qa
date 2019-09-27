import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, perform_login, perform_registration, send_card_details, \
    get_mail_content, get_driver, get_parser, close_firefox

parser = get_parser()

ENTRY_LEVEL_XPATH = "//div[@class='row first-section']/div[@class='col-12 col-md-5 col-sec-1']/div[@class='abouttext4']/div[@class='text-center']/a"
PROFESSIONAL_LEVEL_XPATH = "//div[@class='col-12 col-md-5']/div[@class='abouttext3']/div[@class='text-center']/a"
REQ_XPATH = "//div[@class='row']/div[@class='col-md-8 modal-content']/h2"
PROCEED_XPATH = "//div[@class='sldbtnd']/a"


class WorkExperience(unittest.TestCase):

    print("============ WORK EXPERIENCE =============== ")
    def setUp(self):
        self.logger = get_logger('WorkExperience')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def test_work_experience_page_is_active(self):
        print(" + test_work_experience_page_is_active \n".upper())
        self.driver.find_element_by_link_text("Work Experience").click()
        self.assertIn("Work", self.driver.title)
        with self.subTest(name="test_price_is_not_visible_to_guests"):
            try:
                self.driver.find_element_by_xpath(
                    "//div[@class='col-12 col-md-5 col-sec-1']/div[@class='abouttext4']/h4[@id='marg']")
            except NoSuchElementException:
                return True
            else:
                raise AssertionError("Price was visible to guest user")
            # todo Fix when user redirection is fixed
        with self.subTest("test_price_is_visible_to_authenticated_user"):
            print(" + test_price_is_visible_to_authenticated_user \n".upper())
            perform_login(self.driver)
            self.driver.find_element_by_link_text("Work Experience")
            try:
                self.driver.find_element_by_xpath(
                    "//div[@class='col-12 col-md-5 col-sec-1']/div[@class='abouttext4']/h4[@id='marg']")
            except NoSuchElementException:
                raise AssertionError("Authenticated user unable to see WE price")
            with self.subTest("test_aurhenticated_user_on_click_entry_level_terms_and_condition_page_is_displayed"):
                print(" + test_aurhenticated_user_on_click_entry_level_terms_and_condition_page_is_displayed \n".upper())
                self.driver.find_element_by_xpath(ENTRY_LEVEL_XPATH).click()
                # todo Figure out if uest should see terms and confitions
                self.driver.find_element_by_link_text("I AGREE").click()
                self.assertIn("Log in", self.driver.title.upper())

    def test_guest_on_click_entry_level_login_page_is_showed(self):
        print(" + test_guest_on_click_entry_level_login_page_is_showed \n".upper())
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(ENTRY_LEVEL_XPATH).click()
        # todo Figure out if uest should see terms and confitions
        self.driver.find_element_by_link_text("I AGREE").click()
        self.assertIn("Log in".upper(), self.driver.title.upper())

    def test_aurhenticated_user_on_click_entry_level_terms_and_condition_page_is_displayed(self):
        print(" + test_aurhenticated_user_on_click_entry_level_terms_and_condition_page_is_displayed \n".upper())
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(ENTRY_LEVEL_XPATH).click()
        # todo Figure out if uest should see terms and confitions
        try:
            self.assertTrue(self.driver.find_element_by_link_text("I AGREE"))
            with self.subTest(name="test_terms_and_condition_entry_leads_to_payment_page"):
                self.driver.find_element_by_link_text("I AGREE").click()
                self.assertIn("Pay", self.driver.title)


        except NoSuchElementException:
            raise AssertionError("Agreement page not reached")

    def test_guest_on_click_professional_level_login_page_is_showed(self):
        print(" + test_guest_on_click_professional_level_login_page_is_showed \n".upper())
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(PROFESSIONAL_LEVEL_XPATH).click()
        # todo Figure out if uest should see terms and confitions
        self.driver.find_element_by_link_text("I AGREE").click()
        self.assertIn("Log in".upper(), self.driver.title.upper())

    def test_authenticated_user_on_click_professional_level_terms_and_condition_page_is_displayed(self):
        print(" + test_authenticated_user_on_click_professional_level_terms_and_condition_page_is_displayed \n".upper())
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(PROFESSIONAL_LEVEL_XPATH).click()
        # todo Figure out if uest should see terms and confitions
        try:
            self.assertTrue(self.driver.find_element_by_link_text("I AGREE"))
            with self.subTest(name="test_terms_and_condition_professional_leads_to_payment_page"):
                self.driver.find_element_by_link_text("I AGREE").click()
                self.assertIn("Pay", self.driver.title)
        except NoSuchElementException:
            raise AssertionError("Agreement page not reached")

    def test_payment_succeeds_for_entry_level(self):
        print(" + test_payment_succeeds_for_entry_level \n".upper())
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(ENTRY_LEVEL_XPATH).click()
        c = self.driver.find_element_by_link_text("I AGREE")
        self.driver.execute_script("arguments[0].click();", c)
        send_card_details(self.driver, "//form[@id='stripejsfilemain']/button[@class='stripe-button-el']")
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, REQ_XPATH)))
            with self.subTest(name="test_authenticated_user_can_access_contract_page_on_entry_payment"):
                print(" + test_authenticated_user_can_access_contract_page_on_entry_payment \n".upper())
                self.driver.find_element_by_xpath(PROCEED_XPATH).click()
                self.assertIn("Income Share Agreement",
                              self.driver.find_element_by_xpath(
                                  "//div[@class='el-card__body']/div[@class='row'][2]/div[@class='col-lg-12']/h4").text)

            with self.subTest(name="test_user_is_forced_to_fill_unfilled_form_on_login"):
                print(" + test_user_is_forced_to_fill_unfilled_form_on_login \n".upper())

                self.driver.get(self.url.rstrip('/') + "/logout")
                self.driver.get(self.url)
                perform_login(self.driver, d['username'])
                self.assertIn("Work Experience",
                              self.driver.find_element_by_xpath("//h2[@class='title-4']").text)
            with self.subTest(name="test_profile_form_fill_success"):
                print(" + test_profile_form_fill_success \n".upper())

                self.driver.find_element_by_name('types').send_keys(parser.get("we", 'types'))
                self.driver.find_element_by_name('current_position').send_keys(parser.get("we", 'current_position'))
                self.driver.find_element_by_name('state').send_keys(parser.get("we", 'state'))
                self.driver.find_element_by_name('income').send_keys(parser.get("we", 'income'))
                self.driver.find_element_by_name('date').send_keys(parser.get("we", 'date'))
                self.driver.find_element_by_xpath("//*[@type='submit']").click()
                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                 "//div[@class='jobtype'][1]/p[@class='jobtypeh'][1]")))
                except:
                    raise AssertionError("Form submit failed")
            # todo fix mail notification not sending
            with self.subTest(name="test_notification_is_sent__entry_successful_payment"):
                print(" + test_notification_is_sent__entry_successful_payment \n".upper())
                self.assertIn("EXPERIENCE",
                              get_mail_content(*d['email'].split("@")))

        except Exception as e:
            print(e)
            raise AssertionError("Failed")

    def test_payment_succeeds_for_professional__level(self):
        print(" + test_payment_succeeds_for_professional__level \n".upper())
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])
        self.driver.find_element_by_link_text("Work Experience").click()
        self.driver.find_element_by_xpath(PROFESSIONAL_LEVEL_XPATH).click()
        c = self.driver.find_element_by_link_text("I AGREE")
        self.driver.execute_script("arguments[0].click();", c)
        send_card_details(self.driver, "//form[@id='stripejsfilemain']/button[@class='stripe-button-el']")
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, REQ_XPATH)))
            with self.subTest(name="test_authenticated_user_can_access_contract_page_on_professional_payment"):
                print(" + test_authenticated_user_can_access_contract_page_on_professional_payment \n".upper())

                self.driver.find_element_by_xpath(PROCEED_XPATH).click()
                self.assertIn("Income Share Agreement",
                              self.driver.find_element_by_xpath(
                                  "//div[@class='el-card__body']/div[@class='row'][2]/div[@class='col-lg-12']/h4").text)

            with self.subTest(name="test_user_is_forced_to_fill_unfilled_form_on_login"):
                print(" + test_user_is_forced_to_fill_unfilled_form_on_login \n".upper())

                self.driver.get(self.url.rstrip('/') + "/logout")
                self.driver.get(self.url)
                perform_login(self.driver, d['username'])
                self.assertIn("Work Experience",
                              self.driver.find_element_by_xpath("//h2[@class='title-4']").text)
            with self.subTest(name="test_profile_form_fill_success"):
                print(" + test_profile_form_fill_success \n".upper())

                self.driver.find_element_by_name('types').send_keys(parser.get("we", 'types'))
                self.driver.find_element_by_name('current_position').send_keys(parser.get("we", 'current_position'))
                self.driver.find_element_by_name('state').send_keys(parser.get("we", 'state'))
                self.driver.find_element_by_name('income').send_keys(parser.get("we", 'income'))
                self.driver.find_element_by_name('date').send_keys(parser.get("we", 'date'))
                self.driver.find_element_by_xpath("//*[@type='submit']").click()
                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                 "//div[@class='jobtype'][1]/p[@class='jobtypeh'][1]")))
                except:
                    raise AssertionError("Form submit failed")
            # todo fix mail notification not sending
            with self.subTest(name="test_notification_is_sent__professional_successful_payment"):
                print(" + test_notification_is_sent__professional_successful_payment \n".upper())

                try:
                    self.assertIn("EXPERIENCE",
                                  get_mail_content(*d['email'].split("@")))
                except NoSuchElementException:
                    raise AssertionError("Mail not sent")

        except Exception as e:
            print(e)
            raise AssertionError("Failed")

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
