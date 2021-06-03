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
    "msgtype" : "markdown",
    "agentid" : 1000002,
    "markdown" : {
        "content": "您的会议室已经预定，稍后会同步到`邮箱` 
                                >**事项详情** 
                                >事　项：<font color=\"info\">开会</font> 
                                >组织者：@miglioguan 
                                >参与者：@miglioguan、@kunliu、@jamdeezhou、@kanexiong、@kisonwang 
                                > 
                                >会议室：<font color=\"info\">广州TIT 1楼 301</font> 
                                >日　期：<font color=\"warning\">2018年5月18日</font> 
                                >时　间：<font color=\"comment\">上午9:00-11:00</font> 
                                > 
                                >请准时参加会议。 
                                > 
                                >如需修改会议信息，请点击：[修改会议信息](https://work.weixin.qq.com)"
    },
    "enable_duplicate_check": 0,
}
posturl='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
responese = requests.post(posturl+token1,data=json.dumps(postdata))
