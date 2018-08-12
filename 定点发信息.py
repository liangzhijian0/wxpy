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
    desTime = curTime.replace(hour=18, minute=42, second=0, microsecond=0)  #这里添加时间
    delta = desTime - curTime
    skipSeconds = delta.total_seconds() % SECONDS_PER_DAY
    print ("Must sleep %d seconds" % skipSeconds)
    return skipSeconds


while True:
    
    s = DeltaSeconds()
    time.sleep(s)
    
    try:
        #需要发送的微信号    
        wenzi = bot.friends().search(u'A,bb')[0]
        primary_group = bot.groups().search('这么多年的兄弟')[0]
        
       # Dino_group = bot.groups().search('Dino')[0]
        FoShanList = [wenzi]
        GuangZhouList = [primary_group,wenzi]
       # ZhuHaiList = [Dino_group]
         
        def sendWeather(js,list):
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
            for i in list:
                i.send(str)
            
        
    
        appkey='b38672c8cfa4434eaa1c2418592b39ad'
        url='http://api.avatardata.cn/Weather/Query'
        
        FoShanValue={
            'key':appkey,
            'cityname':'佛山',
        }
        
        GuangZhouValue={
            'key':appkey,
            'cityname':'广州',
        }
        
        ZhuHaiValue={
            'key':appkey,
            'cityname':'珠海',
        }
        
            
        FoShanJs = requests.get(url,params=FoShanValue).json()
        GuangZhouJs = requests.get(url,params=GuangZhouValue).json()
        ZhuHaiJs = requests.get(url,params=ZhuHaiValue).json()
        
        sendWeather(FoShanJs,FoShanList) #发送佛山天气  
        #sendWeather(GuangZhouJs,GuangZhouList) #发送广州天气
        #sendWeather(ZhuHaiJs,ZhuHaiList) #发送珠海天气
        
        
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('A,bb')[0]
        my_friend.send(u"今天消息发送失败了")