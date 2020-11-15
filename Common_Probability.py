# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:15:26 2020

@author: admin
"""
import numpy as np
'''简化函数，便于后续书写'''

rng = np.random.default_rng()  

'''
编写一个字典，使其包含常见的概率分布，并使其名字与函数一一对应，便于调用
需要更改参数时便可以在字典中更改
'''

pro = {'0-1分布' : rng.binomial(n= 1 , p= 0.5 , size= 10),
       '均匀分布' : rng.uniform(low= -1 , high= 1 , size= 10),
       '几何分布' : rng.geometric(p= 0.5, size= 10),
       '二项分布' : rng.binomial(n= 100, p= 0.5, size= 10),
       '泊松分布' : rng.poisson(lam= 5, size= 10),
       
       '标准正太分布' : rng.standard_normal(size= 10),
       '正太分布' : rng.normal(loc= 0, scale= 1, size= 10),
       '指数分布' : rng.exponential(scale= 3, size= 10),
       
       '卡方分布' : rng.chisquare(df= 2, size= 10),
       't分布' : rng.standard_t(df= 5, size= 10),
       'F分布' : rng.f(dfnum= 5, dfden= 5, size= 10),
       
       '伽马分布' : rng.gamma(shape= 5, scale= 5, size= 10),
       '贝塔分布' : rng.beta(a= 0.5, b= 0.5, size= 10),
       }

'''定义函数，计算数据的统计量'''
def Calculate_values(data):
    '''计算均值'''
    print(f'它的均值为{np.mean(data)}')
    '''计算方差'''
    print(f'它的方差为{np.var(data)}')
    '''计算标准差'''
    print(f'它的标准差为{np.std(data)}')
    '''计算极差'''
    print(f'它的极差为{np.ptp(data)}')

'''
遍历字典，把常见概率分布所生成的随机数打印出来
并且打印出各自的均值方差标准差极差
'''
for i in pro:
    
    pro[i]
    print(f'{i}所生成的随机数为：')
    print(pro[i])
    Calculate_values(pro[i])
    print()
    