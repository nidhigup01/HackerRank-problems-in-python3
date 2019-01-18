# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:42:16 2018
Sample Input
n d
6 4
1 2 3 4 5 6
Sample Output

5 6 1 2 3 4 
@author: nidhi
"""
# Python3 program to find  minimum number  
# of swaps required to sort an array 
  
# Function returns the minimum  
# number of swaps required to sort the array 
def minimumSwaps(arr): 
    n = len(arr) 
      
    # Create two arrays and use  
    # as pairs where first array  
    # is element and second array 
    # is position of first element 
    arrpos = [*enumerate(arr)] 
    print('arrpos', arrpos)
      
    # Sort the array by array element  
    # values to get right position of  
    # every element as the elements  
    # of second array. 
    arrpos.sort(key = lambda item:item[1]) 
    print('sorted', arrpos)
      
    # To keep track of visited elements.  
    # Initialize all elements as not  
    # visited or false. 
    vis = {k:False for k in range(n)} 
    print('vis', vis)
      
    # Initialize result 
    ans = 0
    for i in range(n): 
          
        # alreadt swapped or  
        # alreadt present at  
        # correct position 
        if vis[i] or arrpos[i][0] == i+1: 
            print('i', i)
            print('arrpos[i][0]', arrpos[i][0])
            continue
              
        # find number of nodes  
        # in this cycle and 
        # add it to ans 
        cycle_size = 0
        j = i 
        while not vis[j]: 
              
            # mark node as visited 
            vis[j] = True
              
            # move to next node 
            j = arrpos[j][0] 
            cycle_size += 1
              
        # update answer by adding 
        # current cycle 
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    # return answer 
    return ans 
  
# Driver Code      
arr4 = [7,8,5,4,1,2,3,6]
arr1 = [3 ,1, 4, 2 ,5]
arr2 = [4, 3, 1, 2]
arr3 = [1, 3, 5, 2, 4, 6, 7]
arr = [1, 5, 4, 3, 2] 
print(minimumSwaps(arr3)) 
  
# This code is contributed 
# by Dharan Aditya 