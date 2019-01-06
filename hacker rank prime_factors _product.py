# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 23:54:51 2019

@author: nidhi
"""
from functools import reduce
def primeCount(n):
    #[1,n]
    # Write your code here.
    def list_create(m):
        list_till_m=[]
        for i in range(2,m):
            list_till_m.append(i)
        return list_till_m

    n = 50
    no_prime =[]
    a = 2
    def isprime(a,n):
        if n==0 or n==1:
            return False
        elif n==2:
            return True
        else: 
            if a>=n:
                return True
            if n%a ==0:
                return False
            else:
                return isprime(a+1, n)
        return False
    b = list_create(200)
    print('b', b)
    print('\n')
    f = (lambda x: isprime(2,x))
    prime_list = list(filter(f,b))
    print('list of prime numbers', prime_list)
        
    def f2(n, prime_list):
        x = 0
        product = 1
        while x < len(prime_list):
            while product<n:
                a =prime_list[x]
                print('a', a)
                product = product*a
                x =x+1
                print('product', product)
            product = int(product/a)
            return product
        
                
                    
 
    product_unique_fac = f2(n,prime_list)
    print('g', product_unique_fac)
    
    print('isprimecheck', isprime(2,9) )
primeCount(11)
    