# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:56:13 2019

@author: nidhi
"""

def equalizeArray(n,arr):
    from collections import Counter
    c = dict(Counter(arr))
    c_max_value = max(c.values())
    for x in c.keys():
        if c[x] == c_max_value:
            n_in_arr = x
    #print('c', c)
    list_to_delete=[]
    for key, value in c.items():
        if key!=n_in_arr:
            list_to_delete.append(value)
    #print('f', list_to_delete)
    number_deletions = sum(list_to_delete)
    #print(number_deletions)
    return number_delitions
        
        
 

n= int(input('number of elements in array:'))
arr = list(map(int, input('enter n array elements in a row').strip().split()))
equalizeArray(n,arr)

            
            