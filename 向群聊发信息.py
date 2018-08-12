# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:04:35 2018

@author: LIANGOC
"""
from wxpy import *

bot = Bot() 
wenzi = bot.friends().search(u'MM7')[0]
wxpy_groups = bot.groups().search('Dino')[0]
print(type(wxpy_groups))
print(wxpy_groups)
wenzi.send("how are you")
wxpy_groups.send("how are you")