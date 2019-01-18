# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:20:31 2019
Sample Input

2(number of test cases)
5(case1: number of people standing in the row)
2 1 5 3 4
5(case2: number of people standing in the row)
2 5 1 3 4

Sample Output
3(case 1)
Too chaotic
@author: nidhi
"""
'''
This doesn't work as it doesn;t take care of the case when muliple people 
like 5,6,7, 8 make 4 go totally back in 4swaps and then 4 swaps with 8 before him)
def minimumBribes(q):
    q_list = []
    bribes = 0
    for i in range (0, len(q)):
        q_list.append(i+1)
    print(q_list)
    diff = [x1-x2 for (x1,x2) in zip(q, q_list)]
    print('diff', diff)
    i = 0
    while i< len(q):
        if diff[i]>0 and diff [i]< 3:
            bribes = bribes + diff[i]
            i += 1  
        elif diff[i]>= 3:
            return ('Too chaotic')
        else:
            i+= 1
            
    return(bribes)
        
    


t = int(input())
for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    minimumBribes(q)
'''

def minimumBribes(q):
    q_list = []
 
    for i in range (0, len(q)):
        q_list.append(i+1)
    #print(q_list)
    diff = [x1-x2 for (x1,x2) in zip(q, q_list)]
    #print('diff', diff)
    k = 0
    for k in range (0, len(diff)):
        if diff[k]>= 3:
            return ('Too chaotic')
    bribes = 0
    while True:
        corrected = False
        i=0
        for i in range (0, len(q)-1):
            if q[i]>q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                bribes += 1
                #print (bri)
                corrected = True
        if corrected == False:
            return (bribes)
            
             
    return (bribes)
                
            
    
    
    
    
    
t= 1
for _ in range (0, t):
    n =5
    q = [2,1,5,3,4]
    
print( 'bribes', minimumBribes(q))