# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:04:35 2018

@author: LIANGOC
"""
from wxpy import *

bot = Bot() 
wxpy_groups = bot.groups().search('这么多年的兄弟')[0]
print(type(wxpy_groups))
print(wxpy_groups)
wxpy_groups.send("how are you")