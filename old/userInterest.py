import time
import unittest
from configparser import ConfigParser

from login import *
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


class UserInterestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.get(url + '/login')
        login_detail(self)

    # Linux Fundamentals Under Course Interest
    def test_userinterestpage_fundamentals(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the linux fundamentals course in the user Interest Courses to see the description page
        self.driver.find_element_by_id('box-color').click()
        self.driver.implicitly_wait(10)
        course_topic_title = self.driver.find_element_by_class_name("course-intro-title")
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Linux Fundamentals', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Linu fundamental URL
        topic_url = url + '/courses/Linux_Fundamentals/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Linux_Fundamentals')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Linux_Fundamentals')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Linux_Fundamentals/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Linux Proficiency
    def test_userinterestpage_proficiency(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the linux proficiency course description
        self.driver.find_element_by_id('box-color2').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)

        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Linux Proficiency', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Linux Proficiency URL
        topic_url = url + '/courses/Linux_Proficiency/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Linux_Proficiency')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Linux_Proficiency')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Linux_Proficiency/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # HTML & CSS description

    def test_userinterestpage_html_css(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the HTML & CSS course description
        self.driver.find_element_by_id('box-color3').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('HTML CSS', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm HTML & CSS URL
        topic_url = url + '/courses/HTML_CSS/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/HTML_CSS')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/HTML_CSS')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/HTML_CSS/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        # AWS course description

    def test_userinterestpage_aws(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the AWS proficiency course description
        self.driver.find_element_by_id('box-color4').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Amazon AWS', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm AWS URL
        topic_url = url + '/courses/Amazon_AWS/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Amazon_AWS')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Amazon_AWS')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Amazon_AWS/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        # Puppet Course description

    def test_userinterestpage_puppet(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the Puppet Training proficiency course description
        self.driver.find_element_by_id('box-color5').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('PUPPET Training', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Puppet URL
        topic_url = url + '/courses/PUPPET_Training/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Amazon_AWS')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/PUPPET_Training')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/PUPPET_Training/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        # JAVA User interest Page

    def test_userinterestpage_java(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')

        # Click the JAVA proficiency course description
        self.driver.find_element_by_id('box-color6').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Java', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm JAVA URL
        topic_url = url + '/courses/PUPPET_Training/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Amazon_AWS')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/PUPPET_Training')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/PUPPET_Training/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        # RHCSA USer Interests

    def test_userinterestpage_RHCSA(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the RHCSA proficiency course description
        self.driver.find_element_by_id('box-color7').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('RHSCA', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm RHCSA URL
        topic_url = url + '/courses/RHSCA/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/RHSCA')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/RHSCA')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/RHSCA/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Angular
    def test_userinterestpage_Angular(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')

        # Click the Angular course description
        self.driver.find_element_by_id('box-color8').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Angular', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Angular URL
        topic_url = url + '/courses/Angular/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Angular')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Angular')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Angular/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Cyber Security
    def test_userinterestpage_Cyber_Security(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')
        # Click the Cyber Security course description
        self.driver.find_element_by_id('box-color9').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Cyber Security', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Cyber SEcurity URL
        topic_url = url + '/courses/Cyber_Security/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Cyber_Security')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Cyber_Security')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Cyber_Security/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Business Analysis
    def test_userinterestpage_bus_analysis(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')

        # Click the business Analysis course description
        self.driver.find_element_by_id('box-color10').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Business Analysis', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Business Analysis URL
        topic_url = url + '/courses/Business_Analysis/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Business_Analysis')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Business_Analysis')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Business_Analysis/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Database
    def test_userinterestpage_database(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')

        # Click the  course description
        self.driver.find_element_by_id('box-color11').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title.text)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Database', course_topic_title.text)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Database URL
        topic_url = url + '/courses/Database/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Database')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Database')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Database/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    # Python
    def test_userinterestpage_python(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url + '/courses/userinterest')

        # Click the Python course description
        self.driver.find_element_by_id('box-color13').click()
        course_topic_title = self.driver.find_element_by_class_name('course-intro-title')
        # Print the title of the course description in console
        print(course_topic_title)
        # Confirm that the page is the Linux FUndamental description Page
        self.assertEqual('Python', course_topic_title)

        # Get started button to access the course itself
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/div/a/button').click()
        time.sleep(3)

        # Confirm Python URL
        topic_url = url + '/courses/Python/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

        self.driver.get(url + '/courses/description/Python')
        # Try it NOW Button
        self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/a/button').click()
        time.sleep(3)
        try_free_url = url + '/tryfree/standardPlan/'
        if (self.driver.current_url == try_free_url):
            print('Try it now button works')
            # self.assertAlmostEqual(self.driver.current_url, try_free_url)
            print(self.driver.current_url)
        else:
            print('TRY it now button fails')

        self.driver.get(url + '/courses/description/Python')
        # Enrol Now Button
        self.driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div/a/button').click()
        time.sleep(3)
        topic_url = url + '/courses/Python/topics/'
        if (self.driver.current_url == topic_url):
            # self.assertAlmostEqual (self.driver.current_url , topic_url)
            print(self.driver.current_url)
            print('Getting started button works')
        else:
            print('Getting started Button fails')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
