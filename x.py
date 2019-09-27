import os
import sys
import unittest

# The Individual Scripts
# from utils import get_mail_client, get_parser

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
    def test_allTest(self):
        # todo Add a mail notification when the script runs finish
        mailer = get_mail_client()
        print('here')
        parser = get_parser()
        site = parser.get('site_to_test', 'url')
        recipient_list = parser.get('mail', 'recipients')
        developer_mail = ""
        import datetime
        print('here')
        with mailer:
            mailer.send(
                to=recipient_list.split(","),
                #  bcc = developer_mail,
                subject="Test Completed for {}".format(site),
                contents="""
                Find attached the results of the test as at {}
    
                """.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                attachments="LinuxTest.html"
            )
        print('here')
        sys.exit()


if __name__ == '__main__':
    unittest.main()
