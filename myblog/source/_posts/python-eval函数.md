---
title: python eval函数
date: 2018-10-04 19:35:06
tags: 
    - Python eval函数
categories: 
    - python相关函数
---
## Python中eval函数的作用
1、函数说明
eval函数就是实现list、dict、tuple与str之间的转化
str函数把list、dict、tuple转为字符串
eg1：字符串转换成列表
``` python
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(b)
# 输出：
    <type 'str'>
    [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
    
```
eg2:字符串转换成字典
``` python
a = "{1: 'a', 2: 'b'}"
print(type(a))
b = eval(a)
print(type(b))
print(b)
# 输出：
    <type 'str'>
    <type 'dict'>
    {1: 'a', 2: 'b'}

```
eg3：字符串转换成元组
``` python
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))
b=eval(a)
print(type(b))
print(b)
# 输出：
    <type 'str'>
    <type 'tuple'>
    ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))
  
```