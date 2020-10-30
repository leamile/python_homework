# 1.列表的简介
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表的数据项不需要具有相同的类型，可以是字符串类型、整数类型、浮点类型、布尔类型。元素间存在先后顺序。
## 1.1列表的创建
比如我想创建一个以字符串，整数，列表为元素的列表

```
>>>list=["abc",123,"一二",[1,'a']]
>>>print(list)
['abc',123,"一二",[1,'a']]
```

创建列表需要把逗号分隔的不同的数据项用方括号括起来
![](https://github.com/leamile/picture/blob/master/1.png)
## 1.2列表内元素的访问与提取
列表内元素可以单独访问，也可以访问一系列元素

```
>>> print(list[0])
abc
>>> print(list[0:2])
['abc', 123]
```

列表内的位置从0开始
![](https://github.com/leamile/picture/blob/master/2.png)
## 1.3列表中元素的添加与删减
想要在列表中添加元素，可以使用append()方法，表示在列表尾部插入元素

```
>>> list.append("Python")
>>> list.append("987")
>>> print(list)
['abc', 123, '一二', 'Python', '987']
>>> del list[2]
>>> print(list)
['abc', 123, 'Python', '987']
```

列表可以添加和删除元素
![](https://github.com/leamile/picture/blob/master/3.png)
## 1.4列表的其他操作
列表也可以进行长度计算，列表组合，列表重复，判定元素是否在列表中等
```
>>> print(list)
['abc', 123, 'Python', '987']
>>> len(list)
4
>>> list + ["Hi","十"]
['abc', 123, 'Python', '987', 'Hi', '十']
>>> list*3
['abc', 123, 'Python', '987', 'abc', 123, 'Python', '987', 'abc', 123, 'Python', '987']
>>> 123 in list
True
```

![](https://github.com/leamile/picture/blob/master/4.png)

当列表中套入了列表，可认为是高维列表，对高维列表中索引可得到一个新的列表，还可以继续索引，以此类推。


# 2.python中列表与数组的不同之处
## 2.1 不同点
### 2.1.1 定义不同
列表（list）是python的内置数据类型，可以包括任何类型的内容，其中的元素之间没有任何关系；它可以方便、高效的的添加删除元素。
数组（array）是numpy中的一个函数，是一个同一类型的数据的有限集合。ndarray是一个多维的数组对象，具有矢量运算和复杂的广播能力。数组具有执行速度快和节省空间的特点。
### 2.1.2 可进行的处理不同
列表list不可以进行数学四则运算，数组array可以进行数学四则运算
```
>>> import numpy as np
>>> a = np.array([1,2,3,4])
>>> list1 = [1,2,3,4]
>>> print(list1 + list1)
[1, 2, 3, 4, 1, 2, 3, 4]
>>> print(a + a)
[2 4 6 8]
>>> print(list1*3)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> print(a*3)
[ 3  6  9 12]
```
![](https://github.com/leamile/picture/blob/master/5.png)
### 2.1.3 存储效率和输入输出性能不同
相对于数组（array），列表（list）会使用更多的存储空间
## 2.2 相同点
1 都具有多维的形式：列表可嵌套成多维的，数组可以指定大小或嵌套成多维的

2 都可以根据索引来取其中的元素

3 列表和数组都可使用len()函数计算长度
```
>>> print(list1[0],list1[2],a[0],a[2])
1 3 1 3
>>> len(list1)
4
>>> len(a)
4
```
![](https://github.com/leamile/picture/blob/master/6.png)