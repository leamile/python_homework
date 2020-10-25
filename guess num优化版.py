# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:24:56 2020

@author: admin
"""

import random
n=random.randint(0, 100)
print(n)
try: 
    m=int(input('请输入一个0到100的整数:'))
    count=1
    while m != n:
            if m<=100 and m>=0 :    #判断用户输入的m是否在[0,100]之间
                if m > n: #判断用户输入是否大于所给随机数
                    print("你猜的也太大了")
                    m=int(input('请再输入一个0到100的整数:'))
                    count+=1
                else: #判断用户输入是否小于所给随机数
                    print("你猜的数字有点小啊")
                    m=int(input('请再输入一个0到100的整数:'))
                    count+=1
            else: #若用户所给数字超过[0,100]，提示用户再次输入
                print("请输入一个在0到100之间的整数，不要超过范围")
                m=int(input('请再输入一个0到100的整数:'))     
    else: #猜对了则完成程序运行，给出次数
        print("你猜对了,一共猜了{}次".format(count))
except: #判断是否输入的是数字，如果不是数字则自动退出程序
    print("你输入的是整数嘛？？OWO")
    print("请仔细读题后重新启动吧")