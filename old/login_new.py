from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
parser = ConfigParser()
parser.read("credentials.ini")
parser.read("settings.ini")


def login_detail(self):
    username = parser.get('stage', 'username')
    password = parser.get('stage', 'password')
    self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    self.driver.find_element_by_xpath("//*[@type='submit']").click()
