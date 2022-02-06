import requests
import urllib3
import json
import base64
import os

urllib3.disable_warnings()
headers = {"Content-Type": "application/json;charset=UTF-8"}

def gettoken1():
    url = "https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens"
    data = {
    "auth": {
        "identity": {
            "methods": [
                "hw_ak_sk"
            ],
            "hw_ak_sk": {
                "access": {
                    "key": "962EVFKR6KJNDH0W1DTD"
                },
                "secret": {
                    "key": "ZJV5C8qbu5nOLQ3maktBDsjqY3ASZCa94X9TEPIw"
                }
            }
        },
        "scope": {
            "project": {
                "name": "cn-north-4"
            }
        }
    }

}

    r = requests.post(url=url, json=data, headers=headers, verify=False)
    print(r.status_code)
    xx = (r.headers)

    token = (xx['X-Subject-Token'])
    #print(token)
    return token

def ZXService(rou):
    url = "https://5fcb3b055f0841f88acf7fa77fc732bd.apig.cn-north-4.huaweicloudapis.com/v1/infers/51ba2bb4-636f-4b8f-a05a-a9a59831f21e"
    headers = {
        'X-Auth-Token': gettoken1()
    }

    data={}
    files = [
        ('images', open(rou, 'rb'))
    ]
    r = requests.post(url=url, json=data,headers=headers, files = files,verify=False)
    # print(r.status_code)
    # print(r.text)
    return r.text

# if __name__ == '__main__':
#   a= ZXService('helmet_recognition/data/test/zGyemNNhudXz7fngYSn_00860.jpg')
#  print(a)