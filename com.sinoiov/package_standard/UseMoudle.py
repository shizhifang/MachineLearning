# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:32:13 2018

@author: admin
"""
# 导入模块
import numpy as np
import math
# os 模块提供了非常丰富的方法用来处理文件和目录
import os

# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字
#content = dir(math)
 
#print("len={}".format(len(content)),sep=';')
#for index in range(len(content)):
#    print(index,content[index],sep='--->')

# =============================================================================
# *********************************************OS实战
# =============================================================================
#print(os.path.expanduser("~"))

# =============================================================================
# *********************************************numpy实战
# =============================================================================
#默认类型为 float
x = np.zeros((351,34), dtype = 'float')


#原文中dtype 为'float' ，此处应该为 int 类型，其自动将true 转换成 1 ，false转换成 0  
array01 = np.array([[1.0,2.0],[3.0,4.0]])
print(array01)

# 同样的数据（5,0) 重复三行2列
array02=np.tile([5,0],(3,2))
print(array02)



array03=np.array([[11,12,13],[15,8,14]])
print("最小值：",array03.min(0))
print("最大值：",array03.max(0))
