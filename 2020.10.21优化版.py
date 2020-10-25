# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:24:56 2020

@author: admin
"""

import random
n=random.randint(0, 100)
print(n)
try:
    m=eval(input('请输入一个0到100的整数:'))
    if type(m)==int:
        if m < 100 and m > 0:
            count=1
            while m != n:
                if m != n:    
                    if m > n:
                        print("你猜的也太大了")
                        m=eval(input('请再输入一个0到100的整数:'))
                    
                    else:
                        print("你猜的数字有点小啊")
                        m=eval(input('请再输入一个0到100的整数:'))
                    count+=1
            else:
                if count == 1:
                    print("竟然真的有人能一次就猜对，兄弟买彩票去吧")
                elif  count < 10:
                    print("你只猜了{}次就猜对了？".format(count))
                else:
                    print("不会真的有人要猜{}次才对吧！".format(count))
        else:
            print("要输入的是0到100啊！！！读题认真一点好不好")
            print("请仔细读题后重新启动")
    else:
        print("要输入一个整数啊！整！数！！！")
        print("请仔细读题后重新启动吧")
except:
    print("你输入的是整数嘛？？OWO")
    print("请仔细读题后重新启动吧")