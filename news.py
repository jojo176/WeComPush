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
    "msgtype" : "news",
    "agentid" : 1000002,
    "news" : {
        "articles" : [
           {
               "title" : "中秋节礼品领取",
               "description" : "今年中秋节公司有豪礼相送",
               "url" : "URL",
               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
           }
                ]
    },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
