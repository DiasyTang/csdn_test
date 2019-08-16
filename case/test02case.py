import json
import unittest
import sys
import os
import urllib.parse
import paramunittest
import requests
import re

from common.readExcel import ReadExcel
from common.readConfig import ReadConfig
from common.configHttp import ConfigHttp
from common.concurrentRequest import call_gevent

search_xls = ReadExcel().get_xls("userCase.xlsx", "search")
read_config = ReadConfig()
uaToken = read_config.get_http("uaToken")
webUmidToken = read_config.get_http("webUmidToken")
result_get_html = os.path.join(os.path.abspath("."), "result", "html")


@paramunittest.parametrized(*search_xls)
class testBlogSearch(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.result_totals = []

    def description(self):
        print("%s" % self.case_name)

    def setUp(self):
        print("%s测试开始前准备" % self.case_name)

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        call_gevent(self.checkResult, 20)

    def checkResult(self, n):
        print("task is %d" % n)
        data = dict(urllib.parse.parse_qsl(self.query))
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Connection": "keep-alive",
            "Content-Encoding": "gzip",
            "Content-Language": "zh-CN",
            "Content-Type": "text/html;charset=UTF-8",
            "Cookie": "TY_SESSION_ID=6c812483-3352-4c61-a1df-02d77788b34f; JSESSIONID=E62E183BD6BD2A87AA3DC1B11DDEA645; uuid_tt_dd=10_10329108650-1547794895960-167900; dc_session_id=10_1547794895960.393812; UN=u011388215; BT=1565763635974; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_10329108650-1547794895960-167900!5744*1*u011388215!1788*1*PC_VC; smidV2=201908141444333f78e78f04f07551979eeefed73a53b400ab4131da83a0360; acw_tc=2760827a15657650963887448e7e8fb030368f4d80f80c63f95d7d7530d460; __yadk_uid=cNHtPqmQajQyt2Tq3MZMVTBZIdMBsBDS; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1565764691,1565769735,1565770408,1565850770; firstDie=1; c-login-auto=4; acw_sc__v3=5d561bf0ba0c347fe3009a65f309cf89d3ceaaec; acw_sc__v2=5d561bec7e9546a25a73f78958901807e00b846f; dc_tos=pwb6y9; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1565924337",
        }
        info = requests.get(url=self.path, params=data, headers=headers).content.decode(
            "utf-8"
        )
        total = re.findall("共(\\d*)条结果", info, re.S)
        self.result_totals.append(total)
        if n == 19:
            print("total is %s" % self.result_totals)
            length = self.result_totals.__len__()
            assert length == 20


if __name__ == "__main__":
    unittest.main

