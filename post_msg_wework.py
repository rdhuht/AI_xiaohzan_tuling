import requests


# content 的内容可以用 shimoGetMsg.py 获取石墨的文档 内容
content = "https://shimo.im/sheets/e5lEHBzq608uzFj7/MdOfa/ 《校区课程表、邀约开课表、开课信息表》，可复制链接后用石墨文档 App 或小程序打开"


def robot_wework_test(content):
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "text",
        "text": {
        "content": content,
        }
    }
    r = requests.post(
        url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=48131f50-f0ef-4b9e-b075-6b7d7d2b9131',
        headers=headers, json=data)
    print(r.text)


robot_wework_test(content)

