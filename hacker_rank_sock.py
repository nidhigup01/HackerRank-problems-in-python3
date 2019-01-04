# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:15:36 2019

@author: nidhi
"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    from collections import Counter
    a = dict(Counter(ar))
    print(a)
    num_pair = []
    for key, value in a.items():
        w=value//2
        num_pair.append(w)
    print (sum(num_pair))

sockMerchant(6, [1,1,2,2,3,4])
