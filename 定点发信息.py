# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 15:54:15 2018

@author: LIANGOC
"""

import os,time
import sys
import requests
from wxpy import *
from datetime import datetime, timedelta

bot = Bot() 

def DeltaSeconds():
    SECONDS_PER_DAY = 24 * 60 * 60
    
    curTime = datetime.now()
    desTime = curTime.replace(hour=17, minute=51, second=0, microsecond=0)  #这里添加时间
    delta = desTime - curTime
    skipSeconds = delta.total_seconds() % SECONDS_PER_DAY
    print ("Must sleep %d seconds" % skipSeconds)
    return skipSeconds


while True:
    
    s = DeltaSeconds()
    time.sleep(s)
    
    try:
        #需要发送的微信号    
        my_friend = bot.friends().search(u'A,bb')[0]
         
        def showmsg(js):
            #显示时间
            date=js['result']['realtime']
            str = '地点:{0} 现在时间：{1} 农历：{2}'.format(date['city_name'],date['date'],date['moon']+'\n')
            #预报天气状况
            weather=js['result']['weather'] 
            weinfo=weather[0]['info']
        
            for k,v in weinfo.items():
                a = (k,':','天气情况:{0} 最高气温:{1}'.format(v[1],v[2]))
                b = "".join(tuple(a))
                str += b + '\n'
            print(str)
            my_friend.send(str)
        
    
        appkey='b38672c8cfa4434eaa1c2418592b39ad'
        city='珠海'
        value={
            'key':appkey,
            'cityname':city,
        }
        url='http://api.avatardata.cn/Weather/Query'
        s=requests.get(url,params=value)
        js=s.json()
        showmsg(js)     
     
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('A,bb')[0]
        my_friend.send(u"今天消息发送失败了")