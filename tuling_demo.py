# coding:utf-8
# Author: Jeremy Tsui
# Date  : 2019-06-30 20:50
# File  : tuling_demo.py
# IDE   : PyCharm
import urllib.request
import json
import time

APIkey = '85fa9349884747f5b72913a7c60bbcab'


def get_response(msg):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "perception":
            {
                "inputText":
                    {
                        "text": msg
                    },

                "selfInfo":
                    {
                        "location":
                            {
                                "city": "Beijing",
                                "province": "Beijing",
                                "street": "GuangquRoad"
                            }
                    }
            },

        "userInfo":
            {
                "apiKey": "85fa9349884747f5b72913a7c60bbcab",
                "userId": "OnlyUseAlphabet"
            }
    }
    try:
        req = json.dumps(data).encode('utf-8')
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf-8')
        response_dic = json.loads(response_str)
        results_text = response_dic['results'][0]['values']['text']
        return results_text
    except:
        return None


def tuling_reply_text(message):
    print("You said [{}] to AI.".format(message))
    r = get_response(message)
    return r


# 你好
while True:
    time.sleep(0.5)
    msg = input("直男/女：")
    r = tuling_reply_text(msg)
    print("AI：", r)
