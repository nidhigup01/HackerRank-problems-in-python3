# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:55:28 2019

@author: nidhi
"""

def reverse_game(t, n, k):
    
    if k>=n//2:
        return ((n-1-k)*2)
    else:
        return (2*k + 1)

        


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print (reverse_game(t, n, k))
