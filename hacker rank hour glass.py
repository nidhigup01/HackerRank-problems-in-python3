# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 06:24:26 2019

@author: nidhi
"""
arr = []
rows = 6
for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
print (arr)
m = len (arr)
n = len (arr[0])
print('m, number of rows', m)
print('n, number of columns', n)


'''
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
 '''
def hourglassSum(arr):
    m = len (arr)
    n = len (arr[0])
    #print('m, number of rows', m)
    #print('n, number of columns', n)
    max_sum_list = []
    max_sum = -63
    for i in range (0, m-2):
        for j in range (0,n-2):
            #print(i,j)
            max_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
            max_sum_list.append(max_sum)
             
 
    max_res = max(max_sum_list)
    return (max_res)
