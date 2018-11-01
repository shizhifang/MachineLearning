# -*- coding: utf-8 -*-
"""
------------------------------K-近邻算法
描述：采用测试不同特征之间的距离方法进行分类
优点：精度高、对异常值不敏感，无数据输入假定；
适用场景：
Created on Tue Oct 30 14:25:27 2018
@author: fanshengli
"""
from numpy import *  #科学计算包
from sklearn.datasets import *
from collections import defaultdict
from operator import itemgetter 
import matplotlib
import matplotlib.pyplot as plt

import operator  #运算符模块
from os import listdir

# =============================================================================
# 2.1、k-近邻算法演示
# =============================================================================
def createDataSet():
    dataSet=array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels=[1,1,2,2]
    return dataSet,labels
def classify(newData,dataSet,label,k):
    dataSize = dataSet.shape[0]
    ####计算欧式距离 [ 1.70293864  0.2236068   1.48660687  3.2984845 ]
    diff = tile(newData,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    squareDist = sum(sqdiff,axis = 1)###行向量分别相加，从而得到新的一个行向量
    dist = squareDist ** 0.5
    
    ##对距离进行排序 [1 2 0 3]
    sortedDistIndex = argsort(dist)##argsort()根据元素的值从大到小对元素进行排序，返回下标
    classCount={}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    ###选取出现的类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes

def testDemo():
    dataSet,labels=createDataSet()
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    #plt.scatter(dataSet[:,0],dataSet[:,1],20*np.array(labels),c='g',marker="s")
    plt.scatter(dataSet[:,0],dataSet[:,1],20*np.array(labels),20*np.array(labels),marker="s",label="训练数据")
    for x, y in zip(dataSet[:,0], dataSet[:,1]):
        plt.annotate(
            '(%s, %s)' %(x, y),
            xy=(x, y),
            xytext=(0, -10),
            textcoords='offset points',
            ha='right',
            va='top')
    
    newData = array([1.1,0.3])
    print(newData[0],newData[1],sep='--->')
    plt.scatter(newData[0],newData[1],s=60,c='b',marker="*",label="测试数据")
    plt.legend(loc='upper right')#这个必须有，没有你试试看
    plt.title('K-近邻算法')
    plt.grid(True) #显示网格线
    plt.show()
    k = 3
    classes=classify(newData,dataSet,labels,k)
    print("类别：",classes)

# =============================================================================
# 2.2、改进约会网站
# =============================================================================
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  #测试的行数
    diffMat = tile(inX, (dataSetSize,1)) - dataSet #当前行距离后500行的距离
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    #从小到大排序后，继而返回相应值的索引
    sortedDistIndicies = distances.argsort()     
    classCount={}
    #取某点到500训练数据，距离最近的前3个数据的类别，并对每个类别进行计数       
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        if voteIlabel not in classCount:
            classCount[voteIlabel] = 1
        else:
            classCount[voteIlabel] += 1
    sortedClassCount = sorted(classCount.items(),key=itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
#归一化特征值(在处理不同取值范围的特征值的业务时，newValue=(oldValue-min)/(max-min))
def autoNorm(dataSet):
    minVals = dataSet.min(0)  #
    maxVals = dataSet.max(0)
    #print("第{0}种特征的数据 每列最大值：{1} 每列最小值:{2}".format(index+1,maxVals,minVals))
    ranges = maxVals - minVals
    print("",ranges)
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

def testEngagement():
    file2="F:/bigdata/ml/machinelearninginaction/Ch02/datingTestSet2.txt"
    datingDataMat,datingLabels = file2matrix(file2)       #load data setfrom file
#    制作原始数据的散点图,每次调用figure的时候都会重新申请一个figure对象
    fig1_2=plt.figure()
    ax1=fig1_2.add_subplot(111)
    ax1.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.xlabel("分类1:每年获得的飞行常客里程数")
    plt.ylabel("分类2：玩视频游戏所消耗时间百分比")
    
    fig2_3=plt.figure()
    ax=fig2_3.add_subplot(111)
    #ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.xlabel("分类2：玩视频游戏所消耗时间百分比")
    plt.ylabel("分类3:每周消费的冰淇淋公升数")
    plt.show()   
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]   #总行数
    hoRatio = 0.50      #hold out 10%
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],5)
        print("%d  推测出的类别为: %d, 原本的类别为: %d" % (i,classifierResult,datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print(errorCount)
    
if __name__ == '__main__':
    testEngagement()
    


