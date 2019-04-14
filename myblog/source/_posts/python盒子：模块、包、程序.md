---
title: python盒子：模块、包、程序
date: 2019-04-02 15:20:13
tags: 
    - Python程序
categories: 
    - Python心得
---

## 命令行参数
  主要是sys库，调用sys.argv
```python
    import sys
    print ('fafdsaf:',sys.argv)#接收外部的参数

```

## 模块
### 使用别名导入模块

```python
    import report as wr # 把report别名为wr

```
## 包
  把多个模块组织成文件层次，称之为包。
```python
    #主程序是boxes/weather.py
    from source import daily,weekly#模块1：boxes/sources/daily.py  模块2：boxes/source/weekly.py
    
    #还要在sources目录下添加一个文件：init.py。这个文件可以是空的，但是不能少
    #在主程序下就可以调用source目录下的文件了
    
    import report as wr # 把report别名为wr

```

## 双端队列
  模块deque，from collections import deque;函数popleft()去掉最左边的项并返回该项，pop()去掉最右边的项并返回该项。
  
```python
    def palindrome(word):
        from collections import deque
        dq = deque(word)
        while len(dq) > 1:
            if dq.popleft != dq.pop()：
                return False
            return True
            
```
## itertools迭代代码结构
  在for...in循环中调用迭代函数，每次会返回一项，并记住当前调用的状态
  
```python
    import itertools
    for item in itertools.chain([[1,2],['a','b']):
        print(item) #每次输出一项
    ... 
    1
    2
    a
    b
    cycle()是在参数之间循环的无限迭代器
    accumulate()计算积累的值
```
## 友好输出pprint
  pprint()会尽量排列输出元素从而增加可读性

```python
    from pprint import pprint
    

```
## 获取更多python代码
- pypi: http://pypi.python.org 也称为cheese shop
- github： http://github.com/python
- readthedocs https://readthedoces.org




