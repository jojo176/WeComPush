import requests
import json

getdata = {
    "corpid":"",
    "corpsecret":""
}
geturl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
response = requests.get(geturl,params=getdata)
token1 = response.text[43:257]
postdata = {
    "touser" : "@all",
    "msgtype" : "miniprogram_notice",
    "miniprogram_notice" : {
        "appid": "wx123123123123123",
        "page": "pages/index?userid=zhangsan&orderid=123123123",
        "title": "会议室预订成功通知",
        "description": "4月27日 16:16",
        "emphasis_first_item": true,
        "content_item": [
            {
                "key": "会议室",
                "value": "402"
            },
            {
                "key": "会议地点",
                "value": "广州TIT-402会议室"
            },
            {
                "key": "会议时间",
                "value": "2018年8月1日 09:00-09:30"
            },
            {
                "key": "参与人员",
                "value": "周剑轩"
            }
        ]
    },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
