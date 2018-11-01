# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:19:03 2018

@author: admin
"""
from numpy import *  #科学计算包
from sklearn.datasets import *
from collections import defaultdict
from operator import itemgetter


strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] += 1
print(counts)
