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
parser.read("settings.ini")


#######################################################################
# To test the case comment out the second function first while running this script
# To enable recovery link sent to the mail you provide
# Then Uncomment and comment the first function out and replace the recovery link with the link in your mail
#########################################################################

class Password_Recovery(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)

    # def test_password_recovery(self):
    #     try:
    #         #Click the forgot password link
    #         self.driver.find_element_by_link_text('Forgot password?').click()
    #         time.sleep(3)
    #         #Enter your email you want to recovery password
    #         email_field = self.driver.find_element_by_xpath('//*[@id="login"]/input[2]')
    #         email_field.send_keys('sobby04@yahoo.co.uk')
    #         #click the submit button
    #         self.driver.find_element_by_xpath('//*[@id="introduction-login"]/div/div/div[1]/div/form/div[3]/input').click()
    #         time.sleep(3)
    #         #Check that success message of email sent on page
    #         message_sent = self.driver.find_element_by_xpath('//*[@id="login"]/p')
    #         if (message_sent.text == 'An email with password reset information has been sent to you. Check your email to proceede.'):
    #             print ('Password reset message sent to mail')
    #             print (message_sent.text)
    #         else:
    #             print ('Message not sent')

    #     except NoSuchElementException as exceptions:
    #         print ('Test Failed: Could not find Forgot Password link')
    #         self.driver.save_screenshot('screenshot/password_recovery.png')

    # After link has been extracted from email replace it in this function link
    def test_new_password(self):
        url = parser.get('site_to_test', 'url')
        # Go to the password reset link or copy the reset link from your link here
        self.driver.get(url + '/reset_password/ujxpuzdvuyqcrorsjtyguvdakdnrjmgruqxqbhsrsumrzkwsotxeptnjfylrijeo')
        password1 = self.driver.find_element_by_xpath('//*[@id="login"]/input[2]')
        password2 = self.driver.find_element_by_xpath('//*[@id="login"]/input[3]')
        password1.send_keys('password12')
        password2.send_keys('password12')
        self.driver.find_element_by_xpath('//*[@id="introduction-login"]/div/div/div[1]/div/form/div[3]/input').click()
        # Check if the successful password change message is outputed
        message_change = self.driver.find_element_by_xpath('//*[@id="login"]/p')
        if (message_change.text == 'You have successfully changed your password.'):
            print('Password Changed Successfuly')
            print(message_change.text)
        else:
            print('Error in changing password')

        # Login with the New Password
        self.driver.get(url + '/login')
        # Login details
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys('sobby04@yahoo.co.uk')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('password12')
        self.driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        if (self.driver.current_url == url + '/courses/userinterest'):
            print('Test Passed: New Password Logged User in')
        else:
            print('Test Failed: New Password Failed')
            self.driver.save_screenshot('ScreenShot/password_failed.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
