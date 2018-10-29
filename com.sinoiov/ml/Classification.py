# -*- coding: utf-8 -*-
import numpy as np

# 把一个模块的所有内容全都导入到当前的命名空间
from sklearn.datasets import *
from collections import defaultdict
from operator import itemgetter 

# =============================================================================
# 花萼（长） 花萼（宽）  花瓣（长）  花瓣（宽cm） 
# 该数据集共有三种类别：
#    Iris Setosa（山鸢尾）、Iris Versicolour（变色鸢尾）和Iris Virginica（维吉尼亚鸢尾 
# =============================================================================

#该算法目的是通过这四个特征中的一个以分辨种类，即，如果某一植物的特征feature_index 的离散值为valu
#那么该植物最有可能是most_frequent_class，错误率为error
# =============================================================================
# X为离散后的数据
# y_true为每组数据的植株种类
# feature_index为以第几个特征为标准
# value为特征值
# =============================================================================
def train_feature_value(X,y_true,feature_index,value):
	class_counts = defaultdict(int)
	for sample,y in zip(X,y_true):
		if sample[feature_index] == value:
			class_counts[y]+=1
	sorted_class_counts = sorted(class_counts.items(),key=itemgetter(1),reverse=True)
	print("sorted_class_counts",sorted_class_counts,sep='=')
	most_frequent_class = sorted_class_counts[0][0]
	print("most_frequent_class",most_frequent_class,sep='=')
	incorrect_predictions = [class_count for class_vlue,class_count in class_counts.items() if class_vlue != most_frequent_class]
	print("incorrect_predictions",incorrect_predictions)
	error = sum(incorrect_predictions)
	return most_frequent_class,error

if __name__ == '__main__':
   dataset = load_iris()
   X = dataset.data   #每株植物的四个特征
   Y = dataset.target #每株植物的种类，有3个种类
   attribute_means = X.mean(axis=0)  #求4个特征的平均值
   #当该值大于平局值时为1，小于平局值时为0，完成原始数据的离散化
   X_d = np.array(X >= attribute_means, dtype='int') 
   print(X_d)
   train_feature_value(X_d,Y,0,1)   #1=Iris Versicolour

