# logging_example.py
# Create a custom logger
from configparser import ConfigParser

import yagmail
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

parser = ConfigParser()
parser.read("credentials.ini")
parser.read('settings.ini')
username = parser.get('authentication', 'username')
password = parser.get('authentication', 'password')
url = parser.get('site_to_test', 'url')


def get_logger(log_name):
    import logging
    logger = logging.getLogger(log_name)
    # Create handlers
    # c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    f_handler.setLevel(logging.INFO)
    # Create formatters and add it to handlers
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    # c_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(f_handler)
    logger.setLevel(logging.INFO)
    # logger.addHandler(c_handler)
    return logger


def perform_login(driver, username=username, password=password, after_signup=True):
    if after_signup:
        driver.get(url)
        return
    else:
        try:
            driver.find_element_by_link_text("Log In").click()
        except:
            pass
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//*[@type='submit']").click()


def perform_registration(driver, on_reg_page=False):
    data = generate_details()
    logger = get_logger('perform_registration')
    if not on_reg_page:
        driver.find_element_by_link_text("Sign Up").click()
    else:
        driver.find_element_by_link_text("Create new account").click()
    fullname = data.get('fullname')
    email = data.get('email')
    password = parser.get('authentication', 'password')
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_name('fullname').send_keys(fullname)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_class_name('btn-loginform').click()
    import time
    time.sleep(20)
    if "Success" in driver.title:
        driver.get(url)
        logger.info(data)
        return data
    elif "Error" in driver.title:
        driver.get(url)
        return data
    else:
        print(driver.title)
        raise AssertionError("Error in sign up")


def generate_details():
    import random
    data = {}
    names = ['Ismail', 'Korede', 'Sharon', 'Temidire', 'Kanyinsola', 'Nike', 'Dotun', 'Kikelomo', 'Tomisin',
             'Abosede', 'Blessing',
             'Ibrahim', 'Funsho']
    data['firstname'] = random.sample(names, 1)[0]
    data['lastname'] = random.sample(names, 1)[0]
    data['username'] = "test_" + "".join(
        [data['firstname'], "".join(random.sample("1234567890_qwertyuiopasdfghjklzxcvbnm", 3))])
    data['email'] = data['username'] + "@mailnesia.com"
    data['fullname'] = data['firstname'] + " " + data['lastname']
    return data


def send_card_details(driver, button_xpath="//*[@id='stripejsfilemain']/div/div[2]/button"):
    card_number = parser.get('card_details', 'number')
    date = parser.get('card_details', 'date')
    cvv = parser.get('card_details', 'cvc')
    driver.find_element_by_xpath(button_xpath).click()
    driver.switch_to.frame("stripe_checkout_app")
    wait = WebDriverWait(driver, 20)
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Card number']")))
    driver.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(card_number)
    driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys(date)
    driver.find_element_by_xpath("//*[@placeholder='CVC']").send_keys(cvv)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.switch_to.default_content()


def get_mail_content(email_name, email_url):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait

    print('In Confirm Mail Receipt')
    driver_mail = get_driver(True)
    driver_mail.get("http://www." + email_url)

    wait = WebDriverWait(driver_mail, 10)
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, 'sm')))
    name_field = driver_mail.find_element_by_id("mailbox")
    name_field.clear()
    name_field.send_keys(email_name)
    submit_btn.click()

    wait = WebDriverWait(driver_mail, 10)
    wait.until(EC.url_to_be("http://mailnesia.com/mailbox/" + email_name))
    driver_mail.find_element_by_xpath("//tbody/tr[1]/td[2]").click()
    wait = WebDriverWait(driver_mail, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//pre/a[1]'), "http"))
    content = driver_mail.find_element_by_xpath("//pre").text
    driver_mail.quit()
    close_firefox()
    return content.upper()


def get_driver(utils=False):
    if not utils:
        try:
            close_firefox()
        except:
            pass
    DEBUG = False
    BROWSER = "chrome"
    try:
        parser = get_parser()
        DEBUG = parser.getboolean("config", 'debug')
        BROWSER = parser.get("config", 'browser')
    except:
        print("Could not read config")
        pass
    finally:
        if BROWSER == "chrome":
            if not DEBUG:
                options = Options()
                options.add_argument('no-sandbox')
                options.add_argument('disable-dev-shm-usage')
                # options.add_argument('headless')
                options.add_argument('disable-gpu')
                from selenium.webdriver import \
                    Remote  # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                driver = Remote(command_executor='http://50.112.205.140:4444/wd/hub',
                                desired_capabilities=options.to_capabilities())
                return driver
            return Chrome()
        else:
            from selenium import webdriver
            if not DEBUG:
                opt = webdriver.FirefoxOptions()
                opt.add_argument('-headless')
                opt.add_argument('--disable-dev-shm-usage')
                return webdriver.Remote(desired_capabilities=opt.to_capabilities())
                return webdriver.Firefox(options=opt)
            return webdriver.Firefox()


def get_parser(*val):
    parser = ConfigParser()
    parser.read("credentials.ini")
    parser.read('settings.ini')
    if val:
        for i in val:
            parser.read(i)
    return parser


def get_mail_client():
    parser = get_parser()
    username = parser.get('mail', 'username')
    password = parser.get('mail', 'password')
    # yag = yagmail.SMTP(username,password)
    return yagmail.SMTP(user=username, password=password, host="email-smtp.us-west-2.amazonaws.com", port=587,
                        starttls=True)


def screenshot(driver, file_name):
    driver.save_screenshot("screenshot/{}.png".format(file_name))


def close_firefox():
    return
    import psutil
    try:
        PROCNAME = "geckodriver" if parser.get('config',
                                               'browser') == "firefox" else "chrome"  # or chromedriver or IEDriverServer
        PROCNAME2 = "firefox" if parser.get('config',
                                            'browser') == "firefox" else "chrome"  # or chromedriver or IEDriverServer # or chromedriver or IEDriverServer
        x = [proc.kill() for proc in psutil.process_iter(attrs=['pid', 'name'])
             if PROCNAME in proc.name() or PROCNAME2 in proc.name()]
    except psutil.NoSuchProcess:
        pass


def send_email_ses(environment, recipients,
                   username=parser.get('mail', 'username'),
                   password=parser.get('mail', 'password'),
                   from_address=parser.get('mail', 'sender')):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = recipients
    msg['Subject'] = "Test Notification: {}".format(environment.upper())

    from bs4 import BeautifulSoup
    try:

        with open('TestResult-{}.html'.format(environment), 'r') as stream:
            data = "{}".format(BeautifulSoup(stream.read()))
            data = data.replace('\n', '').replace('\r', '')
            html = data
            body = 'Test results for {}'.format(environment)

            from email.mime.text import MIMEText
            msg.attach(MIMEText(body, 'plain'))
            msg.attach(MIMEText(html, 'html'))

            server = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(from_address, recipients.split(','), text)
            server.quit()
            logger = get_logger('Mailing')
            logger.info('Mail Sent')
    except Exception as e:
        logger = get_logger('Mailing')
        logger.info('Mail Not Sent: \n {}'.format(e))
