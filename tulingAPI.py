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

# address = '47.105.46.254'
address = '101.200.42.193'
# address = 'localhost'
mc = minecraft.Minecraft.create(address=address)


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


def tuling_reply_text():
    for chatpost in mc.events.pollChatPosts():
        print(chatpost)
        print(type(chatpost.message))
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


# 你好
while True:
    time.sleep(0.5)
    tuling_reply_text()
