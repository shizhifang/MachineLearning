# -*- coding: utf-8 -*-
"""
Python 2D-绘图领域使用最广泛的套件
将数据图形化，并且提供多样化的输出格式
"""
import numpy as np  #科学计算包
import operator  #运算符模块
import matplotlib.pyplot as plt

# =============================================================================
# ￼同时绘制多条曲线
# =============================================================================
# 从[-1,1]中等距取5个数作为x的取值
x = np.linspace(-1, 1, 5)
y = 2**x + 1
# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y)
# 必要方法，用于将设置好的figure对象显示出来
plt.show()

# =============================================================================
# 散点图
# =============================================================================
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
n = 4
# 从[0]
#numpy.random.random(size=(3, 2))

#高斯分布随机数 np.random.normal(0, 1, n)
#X = np.random.randint(0,10,n)
#Y = np.random.randint(0,10,n)
X=(1.0,1.2,0.1,0.3,1.1)
Y=(2.0,0.1,1.4,3.5,0.3)
labels=[1,1,2,2,20]
dataSet=np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])

#plt.plot(dataSet[:,0],dataSet[:,1],"go") #plot是默认生成折线图
#plt.scatter(X,Y,s=40,c='r',marker="*")
plt.scatter(X,Y,30*np.array(labels),30*np.array(labels),marker="s")

# =============================================================================
# for x, y in zip(dataSet[:,0], dataSet[:,1]):
#     plt.annotate(
#         '(%s, %s,%s)' %(x, y,'a'),
#         xy=(x, y),
#         xytext=(0, -10),
#         textcoords='offset points',
#         ha='center',
#         va='top')
# =============================================================================

#plt.xticks(())  
#plt.yticks(())
plt.title('K-近邻算法')
plt.xlabel("x轴")
plt.ylabel("y")
plt.grid(True) #显示网格线
plt.show()
# =============================================================================
# 条形图
# =============================================================================
