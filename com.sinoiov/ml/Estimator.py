# -*- coding: utf-8 -*-
"""
-----------------------使用scikit-learn 估计器分类
Created on Tue Oct 30 11:17:29 2018
1、估计器（estimator） 用于分类、聚类和回归分析
@author: admin
"""

import numpy as np
import csv

#加载数据集 http://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/
with open(r'F:\wp_python\data\fence.csv','r') as input_file:
  reader = csv.reader(input_file)
  for i , row in enumerate(reader):
    print(row)
#    data = [float(datum) for datum in row[:-1]]     #将前34个特征保存到x 中
#        y[i] = row[-1]=='g'    #把字母型转换成数值型