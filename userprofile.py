import time
import unittest

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger, perform_login, screenshot, get_driver, get_parser

parser = get_parser()


class UserProfile(unittest.TestCase):

    def setUp(self):
        self.logger = get_logger('Authentication')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def test_logged_in_user_can_open_the_profile_page(self):
        return
        text = ""
        perform_login(self.driver)
        # Todo Javascript action fails in selenium headless
        # self.driver.execute_script("arguments[0].click();",
        # self.driver.find_element_by_xpath("//div[@class='container text-1 ']/div[@class='col-md-4 col-sm-6'][1]/ul/li[1]/a"))
        self.driver.get(self.url.rstrip("/") + "/courses/labprofile")
        try:
            w = WebDriverWait(self.driver, 10)
            w.until(
                EC.text_to_be_present_in_element_value((By.XPATH, "//div[@class='display-tc animate-box h1-bg']/h1"),
                                                       "Lab Profile"))
            text = self.driver.find_element_by_xpath("//div[@class='display-tc animate-box h1-bg']/h1").text

        except NoSuchElementException as e:

            print("Ex:  {}".format(e))
            screenshot(self.driver, "test_logged_in_user_can_open_the_profile_page")
        self.assertTrue("Profile" in text, "Profile Page not reached")

    @unittest.skip("Module not properly implemented, shows all_courses")
    def test_logged_in_user_can_see_registered_courses(self):
        pass

    @unittest.skip("Module not properly implemented, shows all_courses")
    def test_logged_in_user_can_see_labs_progress(self):
        pass

    @unittest.skip("Module not properly implemented, shows all_courses")
    def test_logged_in_user_clicking_labs_button_open_course_topic_list_success(self):
        pass

    @unittest.skip("To be used later")
    def test_user_profile(self):
        url = parser.get('site_to_test', 'url')
        # Click the username icon to show the dropdown
        self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/div[2]/nav/ul/li/a').click()
        time.sleep(2)
        # Click the Lab Profile Link
        self.driver.find_element_by_link_text('Lab Profile').click()
        header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
        if (header.text == 'Lab Profile'):
            print(' Lab Profile Page Reached')
            print(header.text)
            time.sleep(3)

            # #Click the Fundamental profile
            # self.driver.find_element_by_xpath('//*[@id="myList"]/div[1]/div[2]/a').click()
            # time.sleep(3)
            # course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            # if (course_lab_header.text == 'Linux Fundamentals Lab Result'):
            #     print ('Result page of Linux Fundamental Reached')
            #     print (course_lab_header.text)
            # else:
            #     print('Result Page of Linux Fundamental not reached')

            self.driver.get(url + '/courses/labprofile')

            # Click the Proficiency profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[2]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Linux Proficiency Lab Result'):
                print('Result page of Linux Proficiency Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Linux Proficiency not reached')

            self.driver.get(url + '/courses/labprofile')

            # Click the HTML CSS profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[3]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'HTML CSS Lab Result'):
                print('Result page of HTML CSS Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of HTML CSS not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Django profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[4]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Django Lab Result'):
                print('Result page of Django Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Django not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Amazon AWS profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[5]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Amazon AWS Lab Result'):
                print('Result page of Amazon AWS Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Amazon AWS not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the PUPPET Training profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[6]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'PUPPET Training Lab Result'):
                print('Result page of PUPPET Training Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of PUPPET Training not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Angular profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[7]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Angular Lab Result'):
                print('Result page of Angular Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Angular not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the DevOps profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[8]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'DevOps Lab Result'):
                print('Result page of DevOps Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of DevOps not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the RHCSA profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[9]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'RHCSA Lab Result'):
                print('Result page of RHCSA Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of RHCSA not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Java profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[10]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Java Lab Result'):
                print('Result page of Java Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Java not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Cyber Security profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[11]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Cyber Security Lab Result'):
                print('Result page of Cyber Security Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Cyber Security not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Python profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[12]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Python Lab Result'):
                print('Result page of Python Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Python not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Business Analysis profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[13]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Business Analysis Lab Result'):
                print('Result page of Business Analysis Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Business Analysis not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Database profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[14]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Database Lab Result'):
                print('Result page of Database Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Database not reached')

            self.driver.get(url + '/courses/labprofile')
            # Click the Machine Learning profile

            self.driver.find_element_by_xpath('//*[@id="myList"]/div[15]/div[2]/a').click()
            time.sleep(3)
            course_lab_header = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            if (course_lab_header.text == 'Machine Learning Lab Result'):
                print('Result page of Machine Learning Reached')
                print(course_lab_header.text)
            else:
                print('Result Page of Machine Learning not reached')

        else:
            print('Lab Profile Page not reached')
            self.driver.save_screenshot('ScreenShot/lab_profile.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
