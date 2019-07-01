# Author: Jeremy Tsui
# Date  : 2019-06-23 10:29
# File  : 24_tulingAPI.py
# IDE   : PyCharm

import urllib.request
import json
import time
from mcpi import minecraft

APIkey = '85fa9349884747f5b72913a7c60bbcab'
opList = ["Hy", "IvyGao", "JeremyTsui", "momo", "Ningliang"]

address = '47.105.46.254'
# address = '101.200.42.193'
# address = 'localhost'
mc = minecraft.Minecraft.create(address=address)


def get_response(text_input):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    req = {
        "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
        "perception":  # 信息参数
            {
                "inputText":  # 文本信息
                    {
                        "text": text_input
                    },

                "selfInfo":  # 用户参数
                    {
                        "location":
                            {
                                "city": "Beijing",  # 所在城市
                                "province": "Beijing",  # 省份
                                "street": "GuangquRoad"  # 街道
                            }
                    }
            },

        "userInfo":
            {
                "apiKey": "85fa9349884747f5b72913a7c60bbcab",
                "userId": "007"  # # 用户唯一标识(随便填, 非密钥)
            }
    }
    try:
        req = json.dumps(req).encode('utf-8')  # dict->utf-8
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf-8')
        response_dic = json.loads(response_str)
        results_text = response_dic['results'][0]['values']['text']
        return results_text
    except:
        return None


def tuling_reply_text():
    for chatpost in mc.events.pollChatPosts():
        playername = mc.entity.getName(chatpost.entityId)
        if playername in opList:
            ms = chatpost.message.lower()
            pName = mc.entity.getName(chatpost.entityId)
            pMsg = chatpost.message
            print("{} said [{}] to AI.".format(pName, pMsg))
            name = ms.split(" ")[0]
            content = ms.split(" ")[1:]
            msg = ''
            print(content)
            for i in content:
                msg += " " + i
            if name == "xiaozhan":
                r = get_response(msg)
                print(type(r))
                mc.postToChat('ministack AI: ' + r)


while True:
    time.sleep(0.5)
    tuling_reply_text()
