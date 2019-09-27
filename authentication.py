import time
import unittest
from configparser import ConfigParser

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, generate_details, perform_login, get_driver, perform_registration, close_firefox

parser = ConfigParser()
options = Options()
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

parser.read("credentials.ini")
parser.read('settings.ini')


class Authentication(unittest.TestCase):
    print(' ========= AUTHENTICATION ================== \n')
    def setUp(self):
        self.logger = get_logger('Authentication')
        self.driver = get_driver()
        # self.driver.maximize_window()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def test_user_can_signup(self):
        print(" + test_user_can_signup \n".upper())
        self.logger.info("test_user_can_signup")
        data = generate_details()
        self.driver.find_element_by_link_text("Sign Up").click()
        fullname = data.get('fullname')
        email = data.get('email')
        password = parser.get('authentication', 'password')
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_name('fullname').send_keys(fullname)
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_class_name('btn-loginform').click()
        time.sleep(2)
        self.assertTrue("Success" in self.driver.title, "Sign up failed")

    def test_authorized_user_login_success(self):
        print(" + test_authorized_user_login_success \n".upper())

        self.logger.info("test_authorized_user_login_success")
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'password')
        first_name = parser.get('authentication', 'firstname')
        perform_login(self.driver, username, password)
        self.driver.get(self.url)
        elem = ""
        try:
            elem = self.driver.find_element_by_xpath(
                "//li[@class='has-dropdown sub-menu profile']/a[@class='b-n']").text
        except Exception:
            pass
        self.assertTrue(first_name.upper() in elem, "Login failed for " + username)

    def test_unauthorized_user_login_failed(self):
        print(" + test_unauthorized_user_login_failed \n".upper())

        self.logger.info("test_unauthorized_user_login_failed")
        username = parser.get('authentication', 'fakeuser')
        password = parser.get('authentication', 'fakepassword')
        perform_login(self.driver, username, password)
        elem = ""
        try:
            elem = self.driver.find_element_by_xpath(
                "//li[@class='has-dropdown sub-menu profile']/a[@class='b-n']").text
        except Exception:
            pass
        self.assertFalse(username in elem, "Unauthorized user was granted access" + username)

    def test_duplicate_user_email_detected(self):
        print(" + test_duplicate_user_email_detected \n".upper())
        self.logger.info("test_duplicate_user_email_detected")
        self.driver.find_element_by_link_text('Sign Up').click()
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'password')
        self.driver.find_element_by_name('fullname').send_keys(username + "" + password)
        self.driver.find_element_by_name('email').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_class_name('btn-loginform').click()
        time.sleep(2)
        self.assertFalse("Success" in self.driver.title, "Sign up failed")

    @unittest.skip('Invalid password detection not implemented')
    def test_invalid_password_entered(self):
        self.logger.info("test_invalid_password_entered")
        self.driver.find_element_by_link_text("Log In").click()
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'fakepassword')
        perform_login(self.driver, username, password)
        # Todo Include the command to detect if invalid password message is printed

    def test_user_login_redirect_to_the_previous_page(self):
        self.logger.info("test_user_login_redirect_to_the_previous_page")
        self.driver.find_element_by_link_text("Policies").click()
        self.driver.find_element_by_link_text("Log In").click()
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'password')
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        self.assertIn("Policies".upper(), self.driver.title.upper())

    def test_user_password_recovery_mail_sent(self):
        print(" + test_user_password_recovery_mail_sent \n".upper())
        self.logger.info("test_user_password_recovery_success")
        self.driver.find_element_by_link_text('Log In').click()
        message_sent = ""
        try:
            # Click the forgot password link
            self.driver.find_element_by_link_text('Forgot password?').click()
            # Enter your email you want to recovery password
            email_field = self.driver.find_element_by_xpath('//*[@id="login"]/input[2]')
            username = parser.get('authentication', 'username')
            email_field.send_keys(username)
            # click the submit button
            self.driver.find_element_by_xpath(
                '//*[@id="introduction-login"]/div/div/div[1]/div/form/div[3]/input').click()
            time.sleep(3)
            # Check that success message of email sent on page
            message_sent = self.driver.find_element_by_xpath('//*[@id="login"]/p').text
            if ("sent to you" in message_sent):
                print('Password reset message sent to mail')

            else:
                print('Message not sent')

        except Exception:
            self.driver.save_screenshot('screenshot/test_user_password_recovery_mail_sent.png')
        self.assertTrue("sent to you" in message_sent, "Email not sent, screenshot saved")

    @unittest.skip("Not properly implemented. Error message should be immediately the token is sent")
    def test_invalid_password_token_detected(self):
        username = parser.get("authentication", "username")
        # Removing a character makes it invlaid
        recovery_url = self.get_recovery_url(*username.split('@'))[:-5]
        self.driver.get(recovery_url)

    def test_user_password_recovery_succeeds(self):
        print(" + test_user_password_recovery_succeeds \n".upper())
        try:
            username = parser.get("authentication", "username")
            recovery_url = self.get_recovery_url(*username.split('@'))
            self.driver.get(recovery_url)
            self.driver.find_element_by_xpath("//div[@id='login']/input[2]").send_keys("password")
            self.driver.find_element_by_xpath("//div[@id='login']/input[3]").send_keys("password")
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//form/div[@id='login']/p"), "successfully"))
            t = self.driver.find_element_by_xpath("//form/div[@id='login']/p")
            self.assertTrue("successfully" in t.text, "Password recovery failed")
        except Exception:
            self.driver.save_screenshot("screenshots/test_user_password_recovery_succeeds.png")

    @unittest.skip("Todo later, confused here")
    def test_user_login_opens_the_current_course(self):
        d = perform_registration(self.driver)
        perform_login(self.driver, d['username'])

    def test_user_login_goes_to_available_courses(self):
        print(" + test_user_login_goes_to_available_courses \n".upper())
        self.logger.info("test_user_login_goes_to_available_courses")
        self.driver.find_element_by_link_text("Log In").click()
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'password')

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        try:
            elem = self.driver.find_element_by_xpath(
                "//li[@class='has-dropdown sub-menu profile']/a[@class='b-n']").text.upper()
            self.assertTrue(username.upper() in elem, "Login failed for" + username)
        except Exception:
            self.driver.save_screenshot('screenshot/test_user_login_goes_to_available_courses.png')

    def test_user_login_goes_to_selected_course(self):
        print(" + test_user_login_goes_to_selected_course \n".upper())
        self.logger.info("test_user_login_goes_to_selected_course")
        cli = self.driver.find_element_by_xpath("//div[@class='col-md-3 col-sm-4 col-xs-12'][2]/ul/li[1]/a")
        text = self.driver.execute_script("return arguments[0].innerText;", cli)
        self.driver.execute_script("arguments[0].click();", cli)
        username = parser.get('authentication', 'username')
        password = parser.get('authentication', 'password')

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath("//*[@type='submit']").click()

        try:
            elem = self.driver.find_element_by_xpath("//div[@class='col-md-4 animate-box'][2]/span").text
            self.assertTrue(text.upper() in elem.upper(),
                            "Did not return to selected course before login was successful")

        except Exception:
            self.driver.save_screenshot('screenshot/test_user_login_goes_to_selected_course.png')

    def get_recovery_url(self, email_name, email_url):
        print(" + get_recovery_url \n".upper())
        print('In get_validation_code')
        driver_mail = get_driver(True)
        driver_mail.get("http://www." + email_url)

        wait = WebDriverWait(driver_mail, 30)
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, 'sm')))
        name_field = driver_mail.find_element_by_id("mailbox")
        name_field.clear()
        name_field.send_keys(email_name)
        submit_btn.click()

        wait = WebDriverWait(driver_mail, 30)
        wait.until(EC.url_to_be("http://mailnesia.com/mailbox/" + email_name))
        driver_mail.find_element_by_xpath("//tbody/tr[1]/td[2]").click()
        wait = WebDriverWait(driver_mail, 30)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '//pre/a[1]'), "http"))
        code = driver_mail.find_element_by_xpath("//pre/a[1]").text
        driver_mail.quit()
        close_firefox()
        return code

    def tearDown(self):
        # self.driver.service.process.send_signal(signal.SIGTERM)
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
