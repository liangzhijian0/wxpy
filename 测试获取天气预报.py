# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:43:37 2018

@author: LIANGOC
"""

#天气预报查询接口
import requests
def showmsg(js):
    #显示时间
    date=js['result']['realtime']
    print('地点:{0} 现在时间：{1} 农历：{2} {3}'.format(date['city_name'],date['date'],date['moon'],date['time']))
    str = '地点:{0} 现在时间：{1} 农历：{2} {3}'.format(date['city_name'],date['date'],date['moon'],date['time']+'\n')
    #预报天气状况
    weather=js['result']['weather'] 
    weinfo=weather[0]['info']

    for k,v in weinfo.items():
        print(k,':','天气情况:{0} 最高气温:{1}'.format(v[1],v[2]))
        a = (k,':','天气情况:{0} 最高气温:{1}'.format(v[1],v[2]))
        b = "".join(tuple(a))
        print(type(b))
        str += b + '\n'
    
    print(str)

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
