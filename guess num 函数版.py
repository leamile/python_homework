# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:09:37 2020

@author: admin
"""

def guess_num(m,n,count):
    try:
        m=eval(input('请输入一个0到100的整数:'))
        while m != n:
                if m<100 and m>0 :    
                    if m > n:
                        print("你猜的也太大了")
                        m=int(input('请再输入一个0到100的整数:'))
                    else:
                        print("你猜的数字有点小啊")
                        m=int(input('请再输入一个0到100的整数:'))
                        count+=1
                else:
                    print("请输入一个在0到100之间的整数，不要超过范围")
                    m=int(input('请再输入一个0到100的整数:'))     
        else:
            print("你猜对了,一共猜了{}次".format(count))
    except:
        print("你输入的是整数嘛？？OWO")
        guess_num(1, n, 1)
import random
n=random.randint(0, 100)
print(n)
guess_num(1, n, 1)