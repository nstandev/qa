import time
import unittest
from configparser import ConfigParser

from login import *
from selenium import webdriver
from selenium.common.exceptions import *
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


class CoursesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/login')
        login_detail(self)

    # Linux FUndamentals
    def test_course_linux_fundamentals(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_link_text('LEARN').click()
        self.driver.implicitly_wait(5)
        try:
            # Click the linux Fundamental course
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[1]/ul/li[1]/a/span').click()
            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Linux Fundamentals'):
                print('TEst Passed: Linux FUndamental Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('File Access, Management and Security').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)

            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/linux_fundamental.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/linux_fundamental.png')

    # Amazon AWS
    def test_course_amazon_aws(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the Amazon AWS link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[2]/ul/li[1]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Amazon AWS'):
                print('TEst Passed: Amazon AWS Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('File Access, Management and Security').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                    # click a course video to test the permission
                    self.driver.find_element_by_partial_link_text('Understanding Elastic Compute Cloud').click()
                    time.sleep(3)
                    payment_page = url + '/access_course'
                    if (self.driver.current_url == payment_page):
                        print('User cannot access course')
                        print(self.driver.current_url)
                    else:
                        print('User can access the course')
                        print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/amazon_aws.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/amazon_aws.png')

    # RHCSA
    def test_course_rhcsa(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the RHCSA link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[3]/ul/li[1]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'RHSCA'):
                print('TEst Passed: RHCSA Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Manage Security: SELinux').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/rhcsa.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/rhcsa.png')

    # Business Analysis
    def test_course_business_analysis(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the Business Analysis link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[4]/ul/li[1]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Business Analysis'):
                print('TEst Passed: Business Analysis Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Planning Domain Area, Part 1').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/bus_analysis.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/bus_analysis.png')

    # Linux Proficiency
    def test_course_linux_proficiency(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the Linux Proficiency Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[1]/ul/li[2]/a/span').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Linux Proficiency'):
                print('TEst Passed: Linux Proficiency Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Understanding Server Administration').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/linux_proficiency.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/linux_proficiency.png')

    # Puppet Training
    def test_course_puppet_training(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the Puppet Training Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[2]/ul/li[2]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'PUPPET Training'):
                print('TEst Passed: PUPPET Training Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Puppet Module Installation And Usage').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/puppet_training.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/puppet_training.png')

    # JAVA
    def test_course_java(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the JAVA Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[3]/ul/li[2]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Java'):
                print('TEst Passed: Java Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Java Encapsulation and Subclassing').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/java.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/java.png')

    # Databases
    def test_course_databases(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Cick the Databases Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[4]/ul/li[2]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Database'):
                print('TEst Passed: Database Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text(
                    'Begin Inserting and Retrieving Data From Databases').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/databases.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/databases.png')

    # HTML & CSS
    def test_course_html_css(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the HTML&CSS Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[1]/ul/li[3]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'HTML CSS'):
                print('TEst Passed: HTML CSS Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Images').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/html_css.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/html_css.png')

    # Angular
    def test_course_angular(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the Angular Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[2]/ul/li[3]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Angular'):
                print('TEst Passed: Angular Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Creating Routes').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/angular.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/angular.png')

    # Cyber Security
    def test_course_cyber_security(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the Cyber Security Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[3]/ul/li[3]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Cyber Security'):
                print('TEst Passed: Cyber Security Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Working With Data Output').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/cyber_security.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/cyber_security.png')

    # Machine Learning
    def test_course_machine_learning(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the Machine LEarning Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[4]/ul/li[3]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Machine Learning'):
                print('TEst Passed: Machine Learning Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Introduction To Machine Learning').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/machine_learning.png')

        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/machine_learning.png')

    # Django
    def test_course_django(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the Django Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[1]/ul/li[4]/a').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Django'):
                print('TEst Passed: Django Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Setting up Django Administrator').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/django.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/django.png')

    # DevOps
    def test_course_devops(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the DevOps Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[2]/ul/li[4]/a/span').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'DevOps'):
                print('TEst Passed: DevOps Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Adding a Github Webhook to Jenkins').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/devops.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/devops.png')

    # Python
    def test_course_python(self):
        url = parser.get('site_to_test', 'url')

        self.driver.implicitly_wait(5)
        # Click the Courses Dropdown
        self.driver.find_element_by_partial_link_text('LEARN').click()
        self.driver.implicitly_wait(5)

        try:
            # Click the Python Link
            self.driver.find_element_by_xpath('//*[@id="course"]/div/div[3]/ul/li[4]/a/span').click()

            topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
            if (topic_title.text == 'Python'):
                print('TEst Passed: Python Topic Page')
                print(topic_title.text)
                # click a course video to test the permission
                self.driver.find_element_by_partial_link_text('Introduction to Classes in Python').click()
                time.sleep(3)
                payment_page = url + '/access_course'
                if (self.driver.current_url == payment_page):
                    print('User cannot access course')
                    print(self.driver.current_url)
                else:
                    print('User can access the course')
                    print(self.driver.current_url)
            else:
                print('Test Failed: Page not reached')
                self.driver.save_screenshot('ScreenShot/python.png')


        except NoSuchElementException as exceptions:
            print('Page not Found')
            self.driver.save_screenshot('ScreenShot/python.png')

    # #Independent Authors
    #     def test_course_independent_author(self):
    #         url = parser.get('site_to_test', 'url')

    #         self.driver.implicitly_wait(5)
    #         try:
    #             #Click the Courses Dropdown
    #             self.driver.find_element_by_partial_link_text('LEARN').click()
    #             self.driver.implicitly_wait(5)

    #             try:
    #                 #Click the Independent Author Link
    #                 self.driver.find_element_by_xpath('//*[@id="course"]/div/div[4]/ul/li[4]/a').click()

    #                 topic_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
    #                 if (topic_title.text == 'Independent Authors'):
    #                     print ('TEst Passed: Independent Authors Topic Page')
    #                     print (topic_title.text)
    #                 else:
    #                     print('Test Failed: Page not reached')
    #                     self.driver.save_screenshot('ScreenShot/independent_author.png')

    #             except NoSuchElementException as exceptions:
    #                 print ('Page not Found')
    #                 self.driver.save_screenshot('ScreenShot/independent_author.png')

    #         except NoSuchElementException as exceptions:
    #             print ('COuld not Find the Link on Page')
    #             self.driver.save_screenshot('ScreenShot/independent_author.png')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
