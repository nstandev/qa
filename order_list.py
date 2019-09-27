import unittest

from utils import get_logger, perform_login, get_driver, get_parser, close_firefox

parser = get_parser()


class OrderList(unittest.TestCase):
    def setUp(self):
        self.logger = get_logger('ORDER_LIST')
        self.driver = get_driver()
        self.url = parser.get('site_to_test', 'url')
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def test_authenticated_user_can_view_all_orders(self):
        perform_login(self.driver)
        # self.driver.execute_script("argument[0].click;",self.driver.find_element_by_xpath(
        # "//div[@class='container text-1 ']/div[@class='col-md-4 col-sm-6'][2]/ul/li/a"))
        self.assertIn("Order", self.driver.title)

    def tearDown(self) -> None:
        self.driver.quit()
        close_firefox()


if __name__ == "__main__":
    unittest.main()
