# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:20:38 2019
- n array of integers .
d An integer , the number of rotations.
@author: nidhi
"""

def rotLeft(n, d, a):
#    n = len(list1)
#    d =4
#    list1 =[1, 2, 3 ,4, 5, 6] 
    b = a[d:n+1]
    c = a[0:d]
    #print('b', b)
    #print('c', c)
    b.extend(c)
    return (b)

rotLeft(6, 4, [1,2,3,4,5,6])