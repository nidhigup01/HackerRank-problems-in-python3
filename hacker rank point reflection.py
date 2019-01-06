# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:27:32 2019

@author: nidhi
#"""
#n=int(input('enter an integer'))
#for i in range(n):
#    px, py, qx, qy = map(int, (input('enter n intergers in a row').strip().split()))
##def findPoint(n, px, py, qx, qy):
#    print('{} {}'.format((px+2*(qx-px)),(py + 2*(qy-py))))
#
#
#

 
#findPoint(n,px,py,qx,qy)
    
def findPoint(n,in_array):
    #
    # Write your code here.
    result = []
    for row in range(0,n):
        print('row', row)
        print('g', in_array[row][0])
        print('h', in_array[row][1])
        print('i', in_array[row][2])
        print('j', in_array[row][3])
        a = in_array[row][0] + 2*(in_array[row][2]-in_array[row][0])
        b = in_array[row][1] + 2*(in_array[row][3]-in_array[row][1])
        a_list = [a,b]
        result.append(a_list)
        print (result)
    print(''.join(map(str, result)))
#    print('\n'.join([' '.join(['{}'.format(item) for item in row]) 
#    for row in result]))
#        
       
        


n = int(input())
in_array = []
for i in range (n):
    arr = list(map(int, input().strip().split()))
    in_array.append(arr)
print (in_array)

#print('px', in_array[row][0])
#print('py', in_array[row][1])
#print('qx', in_array[row][2])
#print('px', in_array[row][3])
findPoint(n,in_array)