import json
import unittest
import sys
import urllib.parse
import paramunittest

import http.client

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
        conn = http.client.HTTPSConnection("passport.csdn.net")
        headers = {
            "Host": "passport.csdn.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://passport.csdn.net/login?code=public",
            "Connection": "keep-alive",
            "Cookie": "uuid_tt_dd=10_9922834940-1551775074076-435898; dc_session_id=10_1551775074076.624681; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1551775075; c-login-auto=1; dc_tos=pwbj0m; SESSION=1a09e36f-7b18-439b-8f25-6bcd7b6ef747",
            "TE": "Trailers",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }
        conn.request(
            "GET",
            "https://passport.csdn.net/v1/api/riskControl/checkNVC?nvcValue=%7B%22a%22%3A%22FFFF00000000016C467E%22%2C%22c%22%3A%221565939974900%3A0.10010072678920356%22%2C%22d%22%3A%22nvc_other%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22defaultToken3_init_callback_not_called%40%40https%3A%2F%2Fpassport.csdn.net%2Flogin%3Fcode%3Dpublic%40%401565939976187%22%7D%2C%22b%22%3A%22119%23MlN85CljMeLhAMMziC0Lsg7DcEBixFSEyGzojtQL5jJ6WcaUf5zdu%2BN7SpgAY52d8jJ3enGGeF0LNOfrl7drzw26%2BJ4ukeJ%2BP%2FCrLZ09x3IlHmHFRdbvLnp6FB7k8U46fTUBP3BJcS9BPcBRE0qB8Ltovzh4y4AMS4gDlvy7AEd9uUno8RamWfFpv7zRxHCuV4npfI4iu5%2BBmf7hjAOOtrI8Zh69dNG7aHVkRMHBTyOVbcIzgdgnEFeVyDKUTqzB%2FX7T%2FPoCmzCwwHWrZd8gmz9fy1ixRf6ACvSJRaJNWLJIu8fdKqjLY6KnwQStSsIdl%2BCpY%2BgRNQdBrbQ5NEwMyvwe2MMsyc7Bi4qAizjWBGNAJva95EAyiFMsOQUC7OX%2FkgcoGdmsEOZ%2FFTn6%2FirF%2BGZFk%2FcnfluEXeGHDjwLDEfsmWoDI%2BpFs35AMVhO3C5L9UWS4QcJdeuxRmKWNN33yrAzRPVedJgLfU%2Bz4luQWtUSXgqdML8GfeASRBsU3vm4PUib4WkLdeHTkIKO4rRSfxaSWPseOEFa2zPr46nO3AyyOcSnXt8G9eAzyBgjpsdtzeWB4WDLH63pkmeWNNFL9DNzR%2FMjxEF34mWq4Qy2dUFLR26ONEFLjnAqRcItdAFf22WS4lkLduN8RJBqrAHH16ASRSSUddi8fU%2Bz4QyJ20A8Rbhb9RU9FCM6I5m%2BM6ILfPFv4Yvnq6z%2BmcTuVWm1RDqyv22g5%2Bo1fojBJZz5iY0KiFpYVQTdeqqOxFNZd4d5Yjp37h7ywVg00qpUB9mE%2FHzZ%2Bqfl7i5HX0QmPFTYP8RmnzuBZGvrihEi2LLYv4tSwg4kMl8NwIfwIisLGB7ncLyKqkDynrMIT0geCxPIpfQhmEdmAdy2v9ELwqhnqz%2FuU3uq4qwRpa126angMM1QuixbkoFyqMBa9CzXS%2B4lHKd3K%2BxHjPKqrOt2NjAMFThX%2BKqHOLDoinOeRk%2BEZCmDsq6Fdl4Gk1dkbHMNrdEkg1NNro2bnFZbZ9J1s%2BWMSG%2Bfc6rbUaAi9ik90u9C%2BLEEwnJh94O2V74dbzfUaGNfUOc5fW5TGZ7M%2BtOpRyrpAfrL3QPv3fdYRTD0fHMmi3fAThhrXYb1tzF7yrfbBaUtuNyZF53FG9NSVmrOFrKRU17IxiLJ6wLPKbfgCpFLzH3%2BRjgZIvjwjor7l9EEgTqe8KikYaONpPxz5bks71w0SwsabdOpjRhLHUW1686oEDPM%2FIGl%2F3Qapip%3D%22%2C%22e%22%3A%22NaE4uUORv07qmnsyyjCRUW--WEc6WDzjDmTUrYhu9M2Ou02fmTbbQ8TJwo5S8wQyW2-yr_Fc0rgzoaAqqVkt6_kzaWYB4-0TYCGCRwHHkDVWsZGXe39du4gEi0eDx88nfDb8WfgHSyZXlC8htBNiWA%22%7D&callBackMethod=jsonp_05505435686998531&source=pc_password",
            headers=headers,
        )
        checkRes = conn.getresponse()
        checkData = checkRes.read()
        data = dict(urllib.parse.parse_qsl(self.query))
        data["uaToken"] = uaToken
        data["webUmidToken"] = webUmidToken
        headers = {
            "Host": "passport.csdn.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://passport.csdn.net/login?code=public",
            "Content-Type": "application/json;charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "1476",
            "Connection": "keep-alive",
            "Cookie": "uuid_tt_dd=10_9922834940-1551775074076-435898; dc_session_id=10_1551775074076.624681; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1551775075; c-login-auto=1; dc_tos=pwbj0m; SESSION=1a09e36f-7b18-439b-8f25-6bcd7b6ef747",
            "TE": "Trailers",
        }
        info = ConfigHttp().run_request(
            self.method,
            self.path,
            json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1),
            headers=headers,
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

