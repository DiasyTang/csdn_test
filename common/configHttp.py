import requests
import json


class ConfigHttp:
    def send_post(self, url, data, headers):
        result = requests.post(url=url, data=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data, headers):
        result = requests.get(url=url, params=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_request(self, method, url=None, data=None, headers=None):
        result = None
        if method == "post":
            result = self.send_post(url, data, headers)
        elif method == "get":
            result = self.send_get(url, data, headers)
        else:
            print("method值错误！！！")
        return result


if __name__ == "__main__":
    result = ConfigHttp().run_request(
        "post", "http://127.0.0.1:8888/login", "name=xiaoming&pwd=111"
    )
    print(result)

