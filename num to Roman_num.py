# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:45:50 2020

@author: admin
"""

class NumChange:
    def __init__(self,Num):    #设置属性
        self.Num = Num

#设置函数，用来对照数字来输出相对应的罗马数字        
    def numToRomanNum(self):
        num_list=[1000, 900, 500, 400, 100, 
                   90, 50, 40, 10, 9, 5, 4, 1]
        str_list=["M", "CM", "D", "CD", "C", 
                   "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res=''    #定义输出的字符串
        for i in range(len(num_list)):
             while self.Num >= num_list[i]:    #比较数字来选取相应的索引输出
                 self.Num -= num_list[i]
                 res += str_list[i]    #不断填写字符串
        return res
     

while True:
#判断用户输入是否是一个1-3999的整数
        try:  
            num = input('请输入一个你想转化的1到3999的整数：')
            num = int(num)
            if num < 1 or num > 3999:    #判断用户输入的范围是否正确
                print('输入范围错误')
                continue
                
            else:
                print (NumChange(num).numToRomanNum())    #实例化并输出结果
                break
            
        except:
            print('你输错啦')