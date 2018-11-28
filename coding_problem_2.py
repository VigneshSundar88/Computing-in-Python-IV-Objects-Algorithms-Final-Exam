# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:39:18 2018

@author: Hi
"""

def joynernacci(val):
    if val <= 2:
        return 1
    else:
        if val % 2 == 0:
            return joynernacci(val - 1) + joynernacci(val - 2)
        else:
            return joynernacci(val - 1) - joynernacci(val - 2)
print(joynernacci(5))