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
    "msgtype" : "video",
    "agentid" : 1000002,
    "video" : {
        "media_id" : "MEDIA_ID",
        "title" : "Title",
       "description" : "Description"
       },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
