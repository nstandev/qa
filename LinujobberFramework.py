import os
import unittest

import HTMLTestRunner
# The Individual Scripts
from account_settings import AccountSettings
from authentication import Authentication
from groupclass import Groupclass
from job_placement import JobPlacement
from order_list import OrderList
from projects import Projects
from try_free import TryFree
from userprofile import UserProfile
from utils import get_mail_client, get_parser
from work_experience import WorkExperience

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
    def test_allTest(self):
        linux_Test = unittest.TestSuite()
        linux_Test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(UserProfile),
            unittest.defaultTestLoader.loadTestsFromTestCase(Projects),
            unittest.defaultTestLoader.loadTestsFromTestCase(AccountSettings),
            unittest.defaultTestLoader.loadTestsFromTestCase(OrderList),
            unittest.defaultTestLoader.loadTestsFromTestCase(TryFree),
            unittest.defaultTestLoader.loadTestsFromTestCase(JobPlacement),
            unittest.defaultTestLoader.loadTestsFromTestCase(WorkExperience),
            unittest.defaultTestLoader.loadTestsFromTestCase(Groupclass),
        ])
        with open(direct + "/TestResult-Int.html", "w") as outfield:
            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfield,
                title="LinuxJobber Test Report",
                description="New Automated Test for the Main FUnctions of the Linuxjobber Site"
            )
            runner1.run(linux_Test)
        # todo Add a mail notification when the script runs finish
        mailer = get_mail_client()
        parser = get_parser()
        site = parser.get('site_to_test', 'url')
        recipient_list = parser.get('mail', 'recipients')
        from utils import send_email_ses
        send_email_ses('Int', recipient_list)


if __name__ == '__main__':
    unittest.main()
