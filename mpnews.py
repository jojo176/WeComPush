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
    "msgtype" : "mpnews",
    "agentid" : 1000002,
    "mpnews" : {
        "articles":[
           {
               "title": "Title", 
               "thumb_media_id": "MEDIA_ID",
               "author": "Author",
               "content_source_url": "URL",
               "content": "Content",
               "digest": "Digest description"
            }
       ]
    },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
