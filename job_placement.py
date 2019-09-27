import os
import unittest

from selenium.common.exceptions import *

from utils import get_logger, perform_registration, perform_login, get_mail_content, get_parser, get_driver, \
    close_firefox

parser = get_parser()
BASE_DIR = os.getcwd()
FORM_HEADER_XPATH = "//h2[@class='title-4']"
GET_STARTED_ENTRY_XPATH = "//div[@class='col-12 col-md-5']/div[@class='fresh-text']/div[@class='text-center']/a[@class='btn btn-lg reg-sub']"
GET_STARTED_SENOIR_XPATH = "//div[@class=' jp2-content']/div[@class='row']/div[@class='col-12 col-md-5']/div[@class='fresh-text2']/div[@class='text-center']/a[@class='btn btn-lg reg-sub']"
import platform

docpath = "/documents/test_resume.pdf" if "linux" in platform.system().lower() else r"\documents\test_resume.pdf"


class JobPlacement(unittest.TestCase):
    print("============== JOB PLACMENTS ==================\n")
    def setUp(self):
        self.logger = get_logger('JobPlacement')
        self.driver = get_driver()
        # self.driver.maximize_window()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.find_element_by_link_text("Job Placement Program").click()

    def test_job_placement_page_active(self):
        print(" + test_job_placement_page_active \n".upper())

        self.assertIn("Job", self.driver.title)

    def test_guest_user_cannot_access_entry_placement_form(self):
        print(" + test_guest_user_cannot_access_entry_placement_form \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_ENTRY_XPATH).click()
        # todo check the title instead
        try:
            self.driver.find_element_by_xpath(FORM_HEADER_XPATH)
            self.assertNotIn("Application Form", self.driver.find_element_by_xpath(FORM_HEADER_XPATH).text,
                             "Guest could access entry page")
        except NoSuchElementException:
            return True
        else:
            raise AssertionError("Other Error")

    def test_guest_user_cannot_access_senoir_placement_form(self):
        print(" + test_guest_user_cannot_access_senoir_placement_form \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_SENOIR_XPATH).click()
        # todo check the title instead22
        try:
            self.driver.find_element_by_xpath(FORM_HEADER_XPATH)
            self.assertNotIn("Application Form", self.driver.find_element_by_xpath(FORM_HEADER_XPATH).text,
                             "Guest could access senoir page")
        except NoSuchElementException:
            return True
        else:
            raise AssertionError("Other Error")

    def test_guest_user_is_directed_to_entry_placement_page_on_authentication(self):
        print(" + test_guest_user_is_directed_to_entry_placement_page_on_authentication \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_ENTRY_XPATH).click()
        data = perform_registration(self.driver, True)
        perform_login(self.driver, data['username'])
        # todo check the title instead
        try:
            # todo fix redirection to page
            self.driver.find_element_by_xpath(FORM_HEADER_XPATH)
            self.assertIn("Application Form", self.driver.find_element_by_xpath(FORM_HEADER_XPATH))
        except NoSuchElementException:
            raise AssertionError("Not directed to placement form")

    def test_guest_user_is_directed_to_senoir_placement_page_on_authentication(self):
        print(" + test_guest_user_is_directed_to_senoir_placement_page_on_authentication \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_SENOIR_XPATH).click()
        data = perform_registration(self.driver, True)
        perform_login(self.driver, data['username'])
        # todo check the title instead
        try:
            # todo fix redirection to page
            self.driver.find_element_by_xpath(FORM_HEADER_XPATH)
            self.assertIn("Application Form", self.driver.find_element_by_xpath(FORM_HEADER_XPATH))
        except NoSuchElementException:
            raise AssertionError("Not directed to placement form")

    def test_authenticated_user_can_submit_job_junior_level_placement_form_no_certificate(self):
        print(" + test_authenticated_user_can_submit_job_junior_level_placement_form_no_certificate \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_ENTRY_XPATH).click()
        data = perform_registration(self.driver, True)
        perform_login(self.driver, data['username'])
        # todo check the title instead
        try:
            # todo fix redirection to page
            self.driver.find_element_by_link_text("Job Placement Program").click()
            self.driver.find_element_by_xpath(GET_STARTED_ENTRY_XPATH).click()
            self.driver.find_element_by_xpath('//*[@id="id_education"]').send_keys(parser.get('jp_e', 'id_education'))
            self.driver.find_element_by_xpath('//*[@id="id_resume"]').send_keys(
                BASE_DIR + docpath
            )
            self.driver.find_element_by_xpath('//*[@id="id_career"]').send_keys(parser.get('jp_e', 'id_career'))
            self.driver.find_element_by_xpath('//*[@id="id_is_certified"]').send_keys(
                parser.get('jp_e', 'id_is_certified'))
            self.driver.find_element_by_xpath('//*[@id="app"]/div[11]/input').click()
            with self.subTest(
                    name="test_entry_level_applicant_with_no_certificate_redirected_to_the_certification_page"):
                print(" + test_entry_level_applicant_with_no_certificate_redirected_to_the_certification_page \n".upper())

                text = ""
                try:
                    text = self.driver.find_element_by_tag_name("h2").text.lower()
                except NoSuchElementException:
                    pass
                    # raise AssertionError("Not taken to certification page")
                self.assertIn("not met", text)

            # todo fix mail sending.
            # with self.subTest(name="test_notification_email_is_sent_on_success"):
            #     self.assertIn("PLACEMENT",
            #                   get_mail_content(*data['email'].split("@")))

        except Exception as e:
            raise AssertionError("Form not submitted")

    def test_authenticated_user_can_submit_job_senoir_level_placement_form(self):
        print(" + test_authenticated_user_can_submit_job_senoir_level_placement_form \n".upper())

        self.driver.find_element_by_xpath(GET_STARTED_SENOIR_XPATH).click()
        data = perform_registration(self.driver, True)
        perform_login(self.driver, data['username'])
        # todo check the title instead
        try:
            # todo fix redirection to page
            self.driver.find_element_by_link_text("Job Placement Program").click()
            self.driver.find_element_by_xpath(GET_STARTED_SENOIR_XPATH).click()
            self.driver.find_element_by_xpath('//*[@id="id_education"]').send_keys(parser.get('jp_s', 'id_education'))
            self.driver.find_element_by_xpath('//*[@id="id_resume"]').send_keys(
                BASE_DIR + docpath
            )

            self.driver.find_element_by_xpath('//*[@id="id_career"]').send_keys(parser.get('jp_s', 'id_career'))
            self.driver.find_element_by_xpath('//*[@id="id_experience"]').send_keys(parser.get('jp_s', 'id_experience'))
            self.driver.find_element_by_xpath('//*[@id="id_certificates"]').send_keys(
                BASE_DIR + docpath
            )
            self.driver.find_element_by_xpath('//*[@id="id_is_certified"]').send_keys(
                parser.get('jp_s', 'id_is_certified'))
            self.driver.find_element_by_xpath('//*[@id="app"]/div[11]/input').click()

            with self.subTest(
                    name="test_senoir_level_applicant_with_certificate_not_redirected_to_the_certification_page"):
                print(" + test_senoir_level_applicant_with_certificate_not_redirected_to_the_certification_page \n".upper())

                text = ""
                try:
                    text = self.driver.find_element_by_tag_name("h2").text.lower()
                except NoSuchElementException as e:
                    print(e)
                    raise AssertionError("Error")
                self.assertIn("requirements met", text)

            with self.subTest(name="test_proceed_on_senoir_leads_to_agreement"):
                print(" + test_proceed_on_senoir_leads_to_agreement \n".upper())

                self.driver.find_element_by_link_text("Proceed").click()
                self.assertIn("leif", self.driver.title.lower())

            # todo fix mail sending.
            with self.subTest(name="test_notification_email_is_sent_on_success"):
                print(" + test_notification_email_is_sent_on_success \n".upper())

                self.assertIn("AGREEMENT",
                              get_mail_content(*data['email'].split("@")))

        except Exception as e:
            print(e)
            raise AssertionError("Form not submitted")

    def test_authenticated_user_senior_level_placement_form_zero_experience_redirects_to_entry_level_application(self):
        print(" + test_authenticated_user_senior_level_placement_form_zero_experience_redirects_to_entry_level_application \n".upper())

        try:
            d = perform_registration(self.driver)
            perform_login(self.driver, d['username'])
            self.driver.find_element_by_link_text("Job Placement Program").click()
            self.driver.find_element_by_xpath(GET_STARTED_SENOIR_XPATH).click()
            self.driver.find_element_by_xpath('//*[@id="id_education"]').send_keys(parser.get('jp_s', 'id_education'))
            self.driver.find_element_by_xpath('//*[@id="id_resume"]').send_keys(
                BASE_DIR + docpath
            )
            self.driver.find_element_by_xpath('//*[@id="id_career"]').send_keys(parser.get('jp_s', 'id_career'))
            # self.driver.find_element_by_xpath('//*[@id="id_certificates"]').send_keys(
            #     BASE_DIR + "\documents\\test_resume.pdf")[2:]
            # )
            self.driver.find_element_by_xpath('//*[@id="id_is_certified"]').send_keys(
                parser.get('jp_e', 'id_is_certified'))
            self.driver.find_element_by_xpath('//*[@id="app"]/div[11]/input').click()
            self.assertIn("not meet",
                          self.driver.find_element_by_xpath("//*[@class='alert alert-danger']").text.lower())
        except Exception as e:
            print(e)
            raise AssertionError("Test failed")

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()

