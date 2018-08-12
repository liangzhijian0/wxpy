# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:09:11 2018

@author: LIANGOC
"""


import requests
import itchat  # 这是一个用于微信回复的库

 
KEY = '5f9787b837214241a49b9ba267f346b0'  # 这个key可以直接拿来用

#users=itchat.search_friends("杜学安")
#userName= users[0]['UserName']
#print(userName)
#itchat.send('你好杜学安',toUserName=userName)
 
# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

#私聊自动回复(文本)
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    #need_reply_name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    #if need_reply_name == 'A,bb' or need_reply_name == '豪' :
        # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = 'I received: ' + msg['Text']
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        return reply or defaultReply

#私聊自动回复(图片/表情，语音，视频) 
@itchat.msg_register([itchat.content.PICTURE,itchat.content.RECORDING,itchat.content.VIDEO])
def other_replay(msg):
    defaultReplay='请发文字'
    return  defaultReplay


# 群聊自动回复
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def tuling_reply(msg):
    need_reply_group_name = itchat.search_chatrooms(userName=msg['FromUserName'])['NickName']
    if need_reply_group_name == '测试群' :
        if msg['isAt']:
            # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
            defaultReply = 'I received: ' + msg['Text']
            # 如果图灵Key出现问题，那么reply将会是None
            reply = get_response(msg['Text'])
            # a or b的意思是，如果a有内容，那么返回a，否则返回b
            return reply or defaultReply
   
    
# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=False)
itchat.run()