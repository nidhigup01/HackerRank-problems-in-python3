# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:26:16 2019

@author: nidhi
"""

import random
import re
import sys
from collections import Counter
def best_divisor(n):
    factors = []
    x = 1
    while x<=n:
        if n%x == 0:
            factors.append(x)
            x += 1
        else:
            x += 1
    print(factors , 'factors')
    sum_digit=[]
    for item in factors:
        sum_item = sum(map(int, str(item)))
        sum_digit.append(sum_item)
    print(sum_digit, 'sum_digit')
    max_sum = max(sum_digit)
    print (max_sum)
    dic_ = dict(zip(factors, sum_digit))
    print('dic_', dic_)
    dic_sum_freq = Counter(sum_digit)
    for key, values in dic_sum_freq.items():
        if key == max_sum and values>=2:
            freq =values
            print('freq', freq)
            alist = []
            for key, values in dic_.items() :
                if dic_[key] == max_sum:
                    alist.append (key)
            return min(alist)
        elif key ==max_sum and values<2:
            for key, values in dic_.items() :
                if dic_[key] == max_sum:
                    return key
        
   
    
    


        

if __name__ == '__main__':
    n = 100000
    print (best_divisor(n))
