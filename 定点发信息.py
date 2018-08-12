# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 15:54:15 2018

@author: LIANGOC
"""

import os,time
import sys
from wxpy import *
from datetime import datetime, timedelta

bot = Bot() 

def DeltaSeconds():
    SECONDS_PER_DAY = 24 * 60 * 60
    
    curTime = datetime.now()
    desTime = curTime.replace(hour=16, minute=30, second=1, microsecond=0)  #这里添加时间
    delta = desTime - curTime
    skipSeconds = delta.total_seconds() % SECONDS_PER_DAY
    print ("Must sleep %d seconds" % skipSeconds)
    return skipSeconds


while True:
    
    s = DeltaSeconds()
    time.sleep(s)
    
    try:
     

   # 你朋友的微信名称，不是备注，也不是微信帐号。    
     my_friend = bot.friends().search(u'A,bb')[0]
     my_friend.send(u"Have a good one!") 
     
    except:

     # 你的微信名称，不是微信帐号。

     my_friend = bot.friends().search('A,bb')[0]
     my_friend.send(u"今天消息发送失败了")