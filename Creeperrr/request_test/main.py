# -*- coding:utf-8 -*-
import json
import requests

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('users/imoocdemo'))
    print better_print(response.text)
    # 明文传输，不安全
    # response = requests.geet(build_uri('user/emails'), auth=('imoocdemo','imoocdemo123'))
    # print response


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print better_print(response.text)
    print response.request.headers
    print response.url


def json_request():
    # 改东西
    response = requests.patch(build_uri('user'), auth=('imoocdemo','imoocdemo123'),
                              json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code
    print response.reason


if __name__ == '__main__':
    # request_method()
    # params_request()
    json_request()
