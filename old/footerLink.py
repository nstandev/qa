import time
import unittest
from configparser import ConfigParser

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


class FooterLinkTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options, executable_path=r"/usr/bin/chromedriver")
        self.driver.maximize_window()

    ########################################################################################
    ############# Company #################

    def test_footer_AboutUS(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('About US').click()
        time.sleep(3)
        about_us = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')
        if (about_us.text == "About Us"):
            print(about_us.text)
            print('About Page Reached')
        else:
            print('About Us not Reached')
            self.driver.save_screenshot('ScreenShot/about_us.png')

    def test_footer_ContactUS(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Contact US').click()
        time.sleep(3)
        contact_us = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')
        if (contact_us.text == "Contact Us"):
            print(contact_us.text)
            print('Contact Page Reached')
        else:
            print('Contact Us not Reached')
            self.driver.save_screenshot('ScreenShot/contact_us.png')

    def test_footer_Policies(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Policies').click()
        time.sleep(3)
        policy = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')
        if (policy.text == "Our Policy"):
            print(policy.text)
            print('Policy Page Reached')
        else:
            print('Policy not Reached')
            self.driver.save_screenshot('ScreenShot/policy.png')

    def test_footer_Location(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Location').click()
        time.sleep(3)
        location = self.driver.find_element_by_xpath('/html/body/section[1]/div[1]/div/div/div/h1')
        if (location.text == "Training Location"):
            print(location.text)
            print('Location Page Reached')
        else:
            print('Location not Reached')
            self.driver.save_screenshot('ScreenShot/location.png')

    ############################################################################
    ##### Quick Links ############

    def test_footer_home(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Home').click()
        time.sleep(2)
        home_title = self.driver.find_element_by_xpath('/html/body/div[1]/div/h1')
        if (home_title.text == 'Work Experience and Job Placement'):
            print(home_title.text)
            print('Home page reached')
        else:
            print('Home Page not reached')
            self.driver.save_screenshot('ScreenShot/home.png')

    def test_footer_Resume_Services(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Resume Services').click()
        time.sleep(2)
        resume_title = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
        if (resume_title.text == 'RESUME PREPARATION'):
            print('Resume page reached')
            self.assertEqual(url + '/resumeservice', self.driver.current_url)
        else:
            print('Resume page not reached')
            self.driver.save_screenshot('ScreenShot/resume.png')

    def test_footer_Student_Packages(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Student Packages').click()
        time.sleep(2)
        student_packages = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/h1')
        if (student_packages.text == 'Choose a Package'):
            print('Student Package page reached')
            self.assertEqual(url + '/home/packages', self.driver.current_url)

        else:
            print('Student Package page not reached')
            self.driver.save_screenshot('ScreenShot/student.png')

    def test_footer_Server_Services(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Server Services').click()
        time.sleep(2)
        server_service = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/h1')
        if (server_service.text == 'Server Service'):
            print('Server Service page reached')
            self.assertEqual(url + '/home/server/service', self.driver.current_url)
        else:
            print('Server Service page not reached ')
            self.driver.save_screenshot('ScreenShot/server.png')

    def test_footer_Live_Help(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Live help').click()
        time.sleep(2)
        live_help = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/div[2]/span')
        if (live_help.text == 'Live Help Available'):
            print('Live Help page Reached')
            self.assertEqual(url + '/home/livehelp', self.driver.current_url)
        else:
            print('Live Help page not Reached')
            self.driver.save_screenshot('ScreenShot/live.png')

    def test_footer_Projects(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Projects').click()
        time.sleep(2)

        try:
            project = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/h1')

            if (project.text == 'Project Groups'):
                print('Project page reached')
                self.assertEqual(url + '/projects/', self.driver.current_url)
            else:
                print('Project page not reached')
                self.driver.save_screenshot('ScreenShot/project.png')

        except NoSuchElementException as exception:
            print('Page not found')
            self.driver.save_screenshot('ScreenShot/project_page.png')

    def test_footer_faq(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('FAQ').click()
        time.sleep(2)
        faq = self.driver.find_element_by_xpath('//*[@id="myCarousel"]/div/div/div/div/h1')
        if (faq.text == 'FAQs'):
            print('FAQ page reached')
            self.assertEqual(url + '/faq', self.driver.current_url)
        else:
            print('FAQ page not reached')
            self.driver.save_screenshot('ScreenShot/faq.png')

    def test_footer_Contact(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Contact Us').click()
        time.sleep(2)
        contact = self.driver.find_element_by_xpath('/html/body/section[2]/div[1]/div[1]/div/div/h1')
        if (contact.text == 'Chat with Us'):
            print('Contact Us page reached')
            self.assertEqual(url + '/companys/contact', self.driver.current_url)
        else:
            print('Contact page not reached')
            self.driver.save_screenshot('ScreenShot/contact')

    def test_footer_GroupClass(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Group Class').click()
        time.sleep(2)
        group_class = self.driver.find_element_by_xpath('/html/body/h2')
        if (group_class.text == 'Why Join Group Class?'):
            print('Group Class Reached')
            self.assertEqual(url + '/groupCourse/', self.driver.current_url)
        else:
            print('Group Class not Reached')
            self.driver.save_screenshot('ScreenShot/group_class.png')

    def test_footer_InPerson(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('In-Person Training').click()
        time.sleep(2)
        in_person = self.driver.find_element_by_xpath('/html/body/section[2]/div/div/div[2]/div/h3')
        if (in_person.text == 'ATTEND IN-PERSON LESSONS WITH LIVE INSTRUCTOR'):
            print('In person Page reached')
            self.assertEqual(url + '/home/liveinstructor', self.driver.current_url)
        else:
            print('In Person Page not reached')
            self.driver.save_screenshot('ScreenShot/in_person.png')

    def test_footer_WorkExperience(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Work Experience').click()
        time.sleep(2)
        work_experience = self.driver.find_element_by_xpath('/html/body/div[1]/div/h3')
        if (work_experience == 'WORK EXPERIENCE'):
            print('Work Experience Page reached')
            self.assertEqual(url + '/workexperience/', self.driver.current_url)
        else:
            print('Work Experience page not reached')
            self.driver.save_screenshot('ScreenShot/work_experience.png')

    def test_footer_Gain_Experience(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Gain Experience').click()
        time.sleep(2)
        gain_experience = self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[1]/strong/h1')
        if (gain_experience == ' Work Experience While You Learn '):
            print('Gain Experience Page reached')
            self.assertEqual(url + '/gainexperience', self.driver.current_url)

        else:
            print('Gain Experience Page not reached')
            self.driver.save_screenshot('ScreenShot/gain_experience.png')

    def test_footer_Job_Placement(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text('Job Placement Program').click()
        job_placement = self.driver.find_element_by_xpath('//*[@id="job"]')
        if (job_placement == 'Job'):
            print('Job Placement Page Reached')
            self.assertEqual(url + '/jobplacements/', self.driver.current_url)
        else:
            print('Job Placement not reached')
            self.driver.save_screenshot('ScreenShot/job_placement.png')

    #######################################################################################
    ######### Social Media Links #######

    def test_footer_facebook(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath('//*[@id="footer"]/section[2]/ul/li[1]/a').click()

            time.sleep(2)
            self.driver.implicitly_wait(5)

            facebook_page = 'https://web.facebook.com/linuxjobber?_rdc=1&_rdr'
            if (self.driver.current_url == 'https://web.facebook.com/linuxjobber?_rdc=1&_rdr'):
                print('Facebook page reached')
                self.assertEqual('https://web.facebook.com/linuxjobber?_rdc=1&_rdr', self.driver.current_url)
            else:
                print('Facebook page not reached')
                print(self.driver.current_url)
        except NoSuchElementException as exceptions:
            print('Could not find the facebook icon')

    def test_footer_twitter(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="footer"]/section[2]/ul/li[2]/a/i').click()
        time.sleep(2)
        self.driver.implicitly_wait(5)
        twitter_page = 'https://twitter.com/linuxjobber'
        if (self.driver.current_url == 'https://twitter.com/linuxjobber'):
            print('Twitter page reached')

            self.assertEqual('https://twitter.com/linuxjobber', self.driver.current_url)
        else:
            print('Twitter page not reached')
            print(self.driver.current_url)

    def test_footer_instagram(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="footer"]/section[2]/ul/li[3]/a/i').click()
        time.sleep(3)
        instagram_page = 'https://www.instagram.com/linuxjobber_/'
        if (self.driver.current_url == 'https://www.instagram.com/linuxjobber_/'):
            print('Instagram page reached')
            print(self.driver.current_url)
            self.assertEqual('https://www.instagram.com/linuxjobber_/', self.driver.current_url)
        else:
            print('Instagram page not reached')
            print(self.driver.current_url)

    def test_footer_linkedin(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="footer"]/section[2]/ul/li[4]/a/i').click()
        time.sleep(2)
        self.driver.implicitly_wait(5)
        linkedin_page = 'https://www.linkedin.com/company/linuxjobber'
        if (self.driver.current_url == 'https://www.linkedin.com/company/linuxjobber'):
            print('Linkedin page reached')
            print(self.driver.current_url)
            self.assertEqual('https://www.linkedin.com/company/linuxjobber', self.driver.current_url)
        else:
            print('Linkedin page not reached')
            print(self.driver.current_url)

    def test_footer_googleplus(self):
        url = parser.get('site_to_test', 'url')
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath('//*[@id="footer"]/section[2]/ul/li[5]/a/i').click()
            time.sleep(2)
            self.driver.implicitly_wait(5)
            googleplus_page = 'https://plus.google.com/u/0/104352481273501435159'
            if (self.driver.current_url == 'https://plus.google.com/u/0/104352481273501435159'):
                print('Google+ page reached')
                self.assertEqual('https://plus.google.com/u/0/104352481273501435159', self.driver.current_url)
            else:
                print('Google+ page not reached')
                print(self.driver.current_url)
        except NoSuchElementException as exceptions:
            print('Could not find the Google+ icon')

    def tearDown(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
