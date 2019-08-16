import os
import sys
from gevent import monkey

from common.HTMLTestRunner import HTMLTestRunner
from common.configEmail import SendEmail
from common.readConfig import ReadConfig
import pythoncom
import unittest
from apscheduler.schedulers.blocking import BlockingScheduler

result_path = os.path.join(os.path.abspath("."), "result", "report.html")
email_on_off = ReadConfig().get_email("on_off")


class AllTest:
    def __init__(self):
        self.caselist_file_path = os.path.join(
            os.path.abspath("."), "case", "caselist.txt"
        )
        self.cases_file = os.path.join(os.path.abspath("."), "case")
        self.case_list = []

    def set_case_list(self):
        with open(self.caselist_file_path) as fb:
            for value in fb.readlines():
                data = str(value)
                if data != "" and not data.startswith("#"):
                    self.case_list.append(data.replace("\n", ""))

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list:
            case_name = case.split("/")[-1]
            top_dir = case.split("/")[0]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(
                os.path.join(self.cases_file, top_dir),
                pattern=case_name + ".py",
                top_level_dir=None,
            )
            suite_module.append(discover)
            print("suite_module:" + str(suite_module))
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print("else:")
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            print("try")
            print(str(suit))
            if suit is not None:
                print("if-suit")
                with open(result_path, "wb") as fp:
                    runner = HTMLTestRunner(
                        stream=fp, title="Test Report", description="Test Description"
                    )
                    runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
        finally:
            print("*********TEST END***********")
        if email_on_off == "on":
            SendEmail().smtp()


if __name__ == "__main__":
    AllTest().run()

