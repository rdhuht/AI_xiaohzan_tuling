# Author: Jeremy Tsui
# Date  : 2019-06-23 10:29
# File  : 24_tulingAPI.py
# IDE   : PyCharm

import urllib.request
import json
import time
from mcpi import minecraft
import sys

APIkey = '85fa9349884747f5b72913a7c60bbcab'
opList = ["JeremyTsui", "momo", "ningliang"]

address = '47.105.46.254'
# address = '101.200.42.193'
mc = minecraft.Minecraft.create(address=address)
l
for i in opList:
    try:
        myId = mc.getPlayerEntityId(i)
        opList.append(myId)
        print(i, "online")
    except:
        print(i, "offline")


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
    # try:
    req = json.dumps(data).encode('utf-8')  # ANSI_X3.4-1968
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf-8')
    response_dic = json.loads(response_str)
    # print(response_dic)
    results_text = response_dic['results'][0]['values']['text']
    return results_text
    # except:
    #     return None


def tuling_reply_text():
    for chatpost in mc.events.pollChatPosts():
        if chatpost.entityId in opList:
            ms = chatpost.message.lower()
            pName = mc.entity.getName(chatpost.entityId)
            pMsg = chatpost.message
            print("{} said [{}] to AI.".format(pName, pMsg))
            name = ms.split(" ")[0]
            content = ms.split(" ")[1:]
            msg = ''
            print(content)
            # showMsg = []
            for i in content:
                msg += " " + i
            if name == "xiaozhan":
                r = get_response(msg)
                # x, y, z = mc.entity.getPos(chatpost.entityId)
                # mc.setBlock(x + 2, y + 1, z, 20)
                print('RESPONSE:', r)
                # for i in re.split(",|，", r):
                #     showMsg.append(i)
                # print(showMsg)
                mc.postToChat('ministack AI: ' + str(r))
            # mc.setSign(x + 1, y + 1, z, 68, 4, showMsg)


while True:
    time.sleep(0.5)
    tuling_reply_text()
