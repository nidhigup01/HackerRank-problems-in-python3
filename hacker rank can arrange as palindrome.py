# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:37:23 2019

@author: nidhi
"""

def gameOfThrones(s):
    if len(s) == 1:
        return true
    from collections import Counter
    dict_s = dict (Counter(s))
    print (dict_s)
    
gameOfThrones('adaaa')