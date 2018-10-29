# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:32:13 2018

@author: admin
"""
# 导入模块
import math
# os 模块提供了非常丰富的方法用来处理文件和目录
import os

# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字
content = dir(math)
 
print("len={}".format(len(content)),sep=';')
for index in range(len(content)):
    print(index,content[index],sep='--->')

