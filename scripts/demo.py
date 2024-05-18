# -*- coding: utf-8 -*-
import requests
import datetime


def push_report(web_hook):
    projectName = "oom"
    start_time = str(datetime.datetime.now())[:19]
    end_time = str(datetime.datetime.now())[:19]
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    message_body = {
        "msg_type": "interactive",
        "card": {
            "elements": [
                {
                    "fields": [
                        {
                            "text": {
                                "content": "**🔴 💡🔔告警服务：**\n${projectName}",
                                "tag": "lark_md"
                            }
                        },
                        {
                            "text": {
                                "content": "**🕐 告警时间：**\n${createTime}",
                                "tag": "lark_md"
                            }
                        }
                    ],
                    "tag": "div"
                },
                {
                    "tag": "div",
                    "text": {
                        "content": "**🛎 详细信息：** \n\n${detail}",
                        "tag": "lark_md"
                    }
                },
                {
                    "fields": [
                        {
                            "text": {
                                "content": f"**🕐 告警时间：**\n{start_time}",
                                "tag": "lark_md"
                            }
                        },
                    ],
                    "tag": "div"
                },
                {
                    "tag": "div",
                    "text": {
                        "content": "** 距离告警事件已过了${durationText}，请及时跟进，避免对业务造成大的影响～ **\n",
                        "tag": "lark_md"
                    }
                },

                {
                    "tag": "div",
                    "text": {
                        "content": "[查看Allure报告](http://localhost:8080/job/demo/allure/)",
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "div",
                    "text": {
                                "content": "at所有人<at id=all></at> ",
                            "tag": "lark_md"
                    },

                },
                {
                    "tag": "hr"
                }
            ],
            "header": {
                "template": "blue",
                "title": {
                    "content": "🔔 ABFerry测试报告",
                    "tag": "plain_text"
                }
            }
        }
    }

    ChatRob = requests.post(url=web_hook, json=message_body, headers=header)
    opener = ChatRob.json()
    print("opener:{}".format(opener))
    if opener["StatusMessage"] == "success":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))


if __name__ == '__main__':
    # webhook 来自于 获取机器人webhook：复制webhook 中的那个值
    webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/6781be16-87e4-47ab-b255-d6bf87c06a9f"
    push_report(webhook)
