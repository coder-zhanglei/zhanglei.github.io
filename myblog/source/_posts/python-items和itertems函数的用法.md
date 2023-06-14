---
title: python items和itertems函数的用法
date: 2018-07-28 21:05:15
tags: 
	- python 字典的访问方法
categories: 
	- python相关函数
---
## 字典的定义
``` python 
#第一种：创建空字典
dict={}
#第二种：创建字典常量
dict={'key1':'value1','key2':'value2'}
#第三种：创建字典
dict=dict()

```

## 字典的赋值
``` python
#第一种：直接赋值
dict={'key1':'value1','key2':'value2'};
#第二种：创建时赋值
dict(key1='value1',key2='value2')

```

## items函数
- 函数说明：items函数，将一个字典以列表的形式返回，因为字典是无序的，所以返回的列表也是无序的。
``` python
a = {'a':1,'b':3}
a.items()
返回 ：a = [('a',1),('b',3)]

```

## iteritems函数
- 函数说明：该函数返回一个迭代器
``` python 
a = {'a':1,'b':3}
b = a.iteritems()
list(b) = [('a',1),('b',3)]

for k, v in b:
    print k,v
    
返回：a 1 
      b 3
      
注：在Python 3.x 里面，iteritems()方法已经废除了。在3.x里用 items()替换iteritems() ，可以用于 for 来循环遍历。
```