---
title: python外壳：代码结构
date: 2019-03-30 10:27:26
tags: 
    - Python代码结构
categories: 
    - Python心得
---

## 引言
    python 没有用花括号（{}）或者关键字(begin和end)来划分代码段，Python用空白来区分代码结构，
用严格的缩进来区分代码块结构。用“#”号来对代码进行注释。用“\”做为续行符来连接不同行的代码。

## if、elif和else
    用法跟c语言的一样，不同的是，在每个判断语句后不用加括号，但是要加冒号(:),表示判断的结束。
每个判断语句下面的执行语句，要有严格的缩进，表示一个代码块。
### 比较操作符
    in 表示属于，其余跟c一样。在连接不同的比较时，有and ，or，not布尔操作符进行不同判断语句的连接。
比如：5 < x and x < 10;可以写成： 5 < x < 10;是同样的效果。
#### 真值的判断
    在所有的比较判断中，非空（零）即真。
    
## while和for循环
    判断同if一样，while 语句后的冒号（：）表示该语句的结束（如：while count < 5 :）;
for循环，在Python中也称对容器的迭代；其中列表，字符串，元组，集合等都是可以迭代的对象，
基本语法：如：for rabbit in rabbits: rabbits可以是上述的迭代对象。元组或列表的迭代都是产生
一项，而字符串的迭代则产生单个字符。
   对字典的迭代，可以迭代键（for key in keys.key(): 或for key in keys:）也可以迭代值
（for value in value.value():）,也可以用元组的方式返回
（for item in accusation.items(): 或者分别赋值 for card,contents in accusation.items():）。   
    
### break和continue
    break和continue都是在循环体里使用，break跳出整个循环，continue跳出当前循环。
### 在循环外使用else
    基本形式如下：
    
```python
    while pos < len(num):
        .....
        break
        
        
    else： #没有执行break
        ...
        
    #for的结构
    
    for cheese in cheeses:
        ...
        break
        
    else： #没有执行break
        ...

```
    上述代码，如果没有执行break，即没有找到可执行的解。则执行else。
## 用zip()并行迭代
    所谓并行迭代就是把多个列表（或者其他容器）放在一起同时迭代，在最短序列用完后，迭代结束。
```python

    days = ['mon','tue',wed]
    fruits = ['banana','orangs','peach']
    drinks = ['offee','tea','beer']
    #在最短序列用完后结束迭代
    for day, fruits, drinks in zip(days, fruits, drinks):
        ...
    #用zip()配对两个元组
    English = 'mon','tue','wed'
    french = 'lundi','mardi','mercredi'
    
    list(zip(English, french))
    #生成字典
    dict(zip(English, french))
    

```
## 用range（）生成自然序列
    range()函数可以返回在特定区间的自然序列，range(start,stop,step),start默认为0，产生的最后一个
数的值是stop的前一个：stop - 1。step默认为1；也可以反向创建自然序列，step = -1；
```python
    for x in range(0,3):
    
    #反向创建
    for x in range(2,-1,-1): 

```
## 推导式
    推导式是一个或者多个迭代器快速简洁地创建数据结构的一种方法，可以将循环和条件判断
相结合，从而避免语法冗长。

### 列表和集合推导式
    语法：[expression for item in iterable]
          [expression for item in iterable if condition]
          
    集合语法：{expression for expression in iterable} 中括号变为花括号      
```python

    number_list = [number for number in range(0,3)]
    a_list = [number for number in range(1,6) if number % 2 == 1]
     
    cells = [(row, col) for row in rows for col in cols]
    for cell in cells:
        print(cell)

```
## 字典的推导式
    
    语法： {key_expression:value_expression for expression in iterable}
    也可以有if判断，以及多个for循环迭代

```python
    
    words = 'letters'
    
    letter_counts = {letter:words.count(letter) for letter in words}
    print(letter_counts)
        {'s': 1, 'r': 1, 'e': 2, 'l': 1, 't': 2}
    #对于程序执行来说，两次调用word.count(letter)浪费时间，因为‘t’和‘e’出现了两次
    # 优化如下
    letter_counts = {letter:words.count(letter) for letter in set(words)}#这是对集合进行迭代而不是字符串
    
```
## 生成器推导式
    元组是没有推导式的。用圆括号是生成器推导式
    
```python
    
>>> number_thing=(number for number in range(1,6))
>>> number_thing
<type 'generator'>

>>> for number in number_thing:
...     print number
... 
1
2
3
4
5
#一个生成器只能运行一次，之后就会被擦除

```




