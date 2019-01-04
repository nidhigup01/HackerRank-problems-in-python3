# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:43:28 2019

@author: nidhi
"""

def jumpingOnClouds(n, c):
    counter = 0
    jump = 0
    while counter<n:
        if counter+2 < n and c[counter] == 0 and c[counter+2]==0:
                jump += 1
                counter += 2
                #print('c', counter)
                #print('j', jump)
        elif counter+2<n and c[counter] ==0 and c[counter+1]==0 and c[counter+2] == 1:      
            jump+=1
            counter += 1
            #print('b', counter)
            #print('j2', jump)
            
        elif counter ==(n-2) :
            jump = jump +1
            #print ('jump', jump)
            print (jump)
            return jump
        elif counter == (n-1):
            jump = jump
            return jump
    
#            
#def jumpingOnClouds(c):
#    jumps, i = 0, 0
#        while i < len(c)-1:
#            # if 2 cloud jumps
#            if i+2 < len(c) and c[i+2] != 1:
#                i += 1
#            jumps += 1
#            i += 1
#        return jumps
n = int(input('input a number n'))
c = list(map(int, input('enter n numbers in a row').rstrip().split()))
jumpingOnClouds(n, c)