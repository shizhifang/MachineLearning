# -*- coding: utf-8 -*-
"""
=========================>>亲和性分析
@see https://www.cnblogs.com/llhy1178/p/6850470.html
@author: fansl
Created on Thu Oct 25 21:42:07 2018
"""
import numpy as np 
dataset_filename = "F:/wp_python/data/Agreeableness.data" 
x= np.loadtxt(dataset_filename)
# 查看前5行文本数字,x[num]则表示索引为num的行数据
#1或0，表示是否购买了某种商品
print("{} {} {} {} {}".format("面包","牛奶","奶酪","苹果","香蕉"))
print(x[:5])

# ----------------------------什么是支持度、置信度
num_apple_purchases=0
for sample in x:
    if sample[3]==1:
        num_apple_purchases+=1
#print("{0} people bought apple".format(num_apple_purchases))

# 接着我们计算有多少人购买了苹果，后又购买了香蕉。同时计算支持度和置信度。
num_apples_bananas_purchases = 0
for sample in x:
    if sample[3] == 1 and sample[4] == 1:
        num_apples_bananas_purchases += 1
valid_rules = num_apples_bananas_purchases
num_occurances = num_apple_purchases
support = valid_rules
confidence = valid_rules/float(num_occurances)
print("{0} people bought Apples, but {1} people also bought bananas".format(num_apple_purchases, num_apples_bananas_purchases))
print("------")
# 支持度
print("支持度：{0}".format(support))
# 置信度
print("{0:.3f}".format(confidence))

"""
----------------------------实现简单的排序规则
我们接着将所有规则下的可能性都统计出来，找出亲和性最高的几个。
    首先，分为两种：一种是规则应验，一种是规则无效。
    分别创建字典。字典的键是由条件和结论组成的元组，元组元素为特征在特征列表中的索引值，
    比如“如果顾客买了苹果，他们也会买香蕉”就用（3，4）表示。这里使用defaultdict，好处是如果查找的键不存在，返回一个默认值。
"""
from collections import defaultdict
features = ["bread", "milk", "cheese", "apple", "banana"]
valib_rules = defaultdict(int)  #规则应验
invalib_rules = defaultdict(int) #规则失效
num_occurances = defaultdict(int)  #条件相同的规则数量
# 依次对样本的每个个体及个体的每个特征值进行处理。第一个特征为规则的前提条件。
for sample in x:
    for premise in range(4):
        if sample[premise] == 0:
            continue
        num_occurances[premise] += 1
        # 比如“顾客买了苹果，他们也买了苹果”，这样的规则是没有意义的。
        for conclusion in range(len(features)):
            if premise == conclusion:
                continue
            if sample[conclusion] == 1:
                valib_rules[(premise, conclusion)] += 1
            else:
                invalib_rules[(premise, conclusion)] += 1
support = valib_rules
confidence = defaultdict(float)
'''
for premise, conclusion in valib_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = valib_rules[rule] / num_occurances[premise]
'''
# 这样我们就得到了支持度字典和置信度字典。我们再来创建一个函数，以便更加方便查看结果。
def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    confidence[(premise, conclusion)] = valib_rules[(premise, conclusion)] / float(num_occurances[premise])
    print("Rule: If a person buys {0} they will also buy {1}".format(premise_name, conclusion_name))
    print("- Support: {0}".format(support[(premise, conclusion)]))
    print("- Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))
if __name__ == "__main__":
    premise = 1
    conclusion = 3
    # print print_rule(premise, conclusion, support, confidence, features)

# 排序找出最佳的规则。对字典排序：首先字典的items（）函数返回包含字典所有元素的列表，再使用itemgetter（）类作为键，这样就可以对嵌套列表进行排序了。
from operator import itemgetter
sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
# 提取支持度最高的5条
for index in range(5):
    print("Rule #{0}".format(index + 1))
    premise, conclusion = sorted_support[index][0]
    print_rule(premise, conclusion, support, confidence, features)