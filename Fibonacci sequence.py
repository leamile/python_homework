# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:36:57 2020

@author: leamile liu
"""

#使用生成器实现斐波那契数列
def fibonacci(num):    #num表示想生成的斐波那契数列数字个数
    count, pre_num, next_num = 0, 0, 1
    while count < num:    #用循环来输出斐波那契数列
        yield pre_num
        pre_num, next_num = next_num, pre_num+next_num
        count += 1
g = fibonacci(15)    #此处可控制输出的斐波那契数列个数，此处假定输出15个数据
print("斐波那契数列：")
for i in g :    #遍历生成的斐波那契数列的数字并展示出来  
    print(i,end=",")
    
print('\n')    #换行

# 使用循环来生成斐波那契数列
num_1 = 0
num_2 = 1    #定义前两个数字
count = 2    #因为前两个数字已经定义，所以数据要从2开始循环
print("斐波那契数列：")
print(f'{num_1},{num_2}',end=",")    #先打印出前两个数字
while count < 15:    #此处可控制输出的斐波那契数列个数，此处假定输出15个数据
   new_num = num_1 + num_2    #不断循环计算斐波那契数列
   print(new_num,end=",")    #每计算出一个新的数据便打印出来
   num_1 = num_2
   num_2 = new_num
   count += 1
   
print('\n')    #换行

#用矩阵方法生成斐波那契数列
import numpy as np
num = 15    #num表示想生成的斐波那契数列数字个数
n1 = 0    #定义第一个数字为0
print("斐波那契数列：")
if num <= 1:    #若想要生成一个数字，直接输出第一个数字
    print(n1)
else:    #若想生成多个数字，则进行数列运算
    print(n1,end=',')    #先输出第一个数字
    a = np.array([[1,1],[1,0]])
    b = np.array([[1,1],[1,0]])
    for i in range (num-1):    #由于已经输出第一个数字，所以循环num-1次
        m = a[1,0]    #提取每一个矩阵的第二行第一列数字，就是计算出的斐波那契数
        a = a@b    #更新a
        print(m,end=',')    #分别打印出每一次计算出的数据，组成斐波那契数列