# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:01:56 2020

@author: admin
"""

import random
n=random.randint(0, 100)
print(n)
m=eval(input('请输入一个整数:'))
y = 1
while m != n:
    if m != n:    
        if m > n:
            print("输入的数字过大")
        else:
            print("输入的数字过小")
        m=eval(input('请再输入一个整数:'))
    y = y + 1
else:
    print("你一共猜了{}次才对".format(y))