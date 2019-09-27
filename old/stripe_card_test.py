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


def send_details(self):
    card_number = parser.get('card_details', 'number')
    date = parser.get('card_details', 'date')
    cvv = parser.get('card_details', 'cvc')
    self.driver.switch_to.frame("stripe_checkout_app")
    self.driver.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(card_number)
    self.driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys(date)
    self.driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys(cvv)
    self.driver.find_element_by_xpath('//*[@type="submit"]').click()
    self.driver.switch_to.default_content()
