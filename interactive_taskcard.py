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
    "msgtype" : "interactive_taskcard",
    "agentid" : 1000002,
    "interactive_taskcard" : {
        "title" : "赵明登的礼物申请",
        "description" : "礼品：A31茶具套装\n用途：赠与小黑科技张总经理",
        "url" : "URL",
        "task_id" : "taskid123",
        "btn":[
            {
                "key": "key111",
                "name": "批准",
                "color":"red",
                "is_bold": true
            },
            {
                "key": "key222",
                "name": "驳回"
            }
        ]
    },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
