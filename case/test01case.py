import json
import unittest
import sys
import urllib.parse
import paramunittest
from common.readExcel import ReadExcel
from common.readConfig import ReadConfig
from common.configHttp import ConfigHttp

login_xls = ReadExcel().get_xls("userCase.xlsx", "login")
read_config = ReadConfig()
uaToken = read_config.get_http("uaToken")
webUmidToken = read_config.get_http("webUmidToken")


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        print("%s" % self.case_name)

    def setUp(self):
        print("%s测试开始前准备" % self.case_name)

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        self.checkResult()

    def checkResult(self):
        data = dict(urllib.parse.parse_qsl(self.query))
        data["uaToken"] = uaToken
        data["webUmidToken"] = webUmidToken
        info = ConfigHttp().run_request(
            self.method,
            self.path,
            json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1),
        )
        result = json.loads(info)
        if self.case_name == "login":
            assert result["code"] == "0"
        if self.case_name == "login_error":
            assert result["code"] == "1041"
        if self.case_name == "login_null":
            assert result["code"] == "1011"


if __name__ == "__main__":
    unittest.main

