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


# In the case of testing a new user(a user with no account at all), your credential details must be the same.. e.g  user_profile must contain the name and password with Sign_up_details

def login_detail(self):
    username = parser.get('authentication', 'username')
    password = parser.get('authentication', 'password')
    self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    self.driver.find_element_by_xpath("//*[@type='submit']").click()


def login_detail_1(self):
    username = parser.get('int_login', 'username')
    password = parser.get('int_login', 'password')
    self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    self.driver.find_element_by_xpath("//*[@type='submit']").click()


def login_detail_new_user(self):
    username = parser.get('int_login', 'username')
    password = parser.get('int_login', 'password')
    self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    self.driver.find_element_by_xpath("//*[@type='submit']").click()


def login_detail_we(self):
    username = parser.get('new_user', 'username')
    password = parser.get('new_user', 'password')
    self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    self.driver.find_element_by_xpath("//*[@type='submit']").click()


def signup_detail(self):
    fullname = parser.get('sign_up_details', 'fullname')
    email = parser.get('sign_up_details', 'email')
    password = parser.get('sign_up_details', 'password')
    self.driver.find_element_by_name('fullname').send_keys(fullname)
    self.driver.find_element_by_name('email').send_keys(email)
    self.driver.find_element_by_name('password').send_keys(password)
    self.driver.find_element_by_xpath('//*[@id="introduction-login"]/div/div/div[1]/div/form/div[4]/button').click()
