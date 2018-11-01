# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:59:55 2018

@author: fanshengli
"""
# 导入模块
import numpy as np
def testTile(line01):
    print("tile")


def aa(array02):
    #函数将数组的值从小到大排序后，并按照其相对应的索引值输出
    

def testShape():
    datingLabels=np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
    array01 = np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43],[51,52,53],[61,62,63],[71,72,73],[81,82,83]])
#    print("shape 几行几列：",array01.shape)
#    print("shape[0]  {0}行".format(array01.shape[0]))
#    print("shape[1] {0}列".format(array01.shape[1]))
    m=array01.shape[0]
    hoRatio = 0.50      #hold out 10%
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        # x:num,: 等同于   x:num ，都表示 index(num-x)、index(num-x+1)。。index(num-1) 前闭后开
        print(i,array01[i,:3],array01[numTestVecs:m,:],datingLabels[numTestVecs:m],sep='==')
    
    return array01
    

if __name__ == '__main__':
    array01=testShape()
    testTile(array01[0])
  
