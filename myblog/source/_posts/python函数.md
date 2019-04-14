---
layout: w
title: python函数
date: 2019-03-31 10:18:01
tags: 
    - Python代码结构
categories: 
    - Python心得
---

## 函数的定义
  依次输入def，函数名，带有参数的圆括号，最后紧跟冒号（:），一个函数可以接受任何类型的值作为输入变量，并且返回任何数量的任何类型的结果。
如果函数不显示调用return，会默认返回none。
  注：none不代表false，作为布尔值和FALSE是一样的。
```python
    def do_nothing
        pass

```
## 函数的参数

### 位置参数
    传入的参数值是按照顺序依次复制过去的，顺序不同，参数的引用结果不同、
### 关键字参数
  调用参数时可以指定对应参数的名字，这样可以不遵从顺序传入的原则。若一部分指定了参数名字，而另一部分参数没有指定名字，则没指定名字的
按照顺序传入的原则调用。
### 指定默认参数值
    默认参数值在函数被指定时已经计算出来了，而不是在程序运行时。
```python
    def menu(wine,entree,dessert='pudding'):
        return {}
```
### 使用*收集位置参数
   
```python
    def print_args(*args):
        pass
```
    星号将一组可变数量的位置参数集合成参数值的元组。同样的道理，如果你的函数同时有限定的位置参数，那么*args会收集剩下的参数。
    
### 使用**收集关键字参数
    使用两个星号可以将参数收集到一个字典中，参数的名字是字典的键，对应参数的值是字典的值。
```python
    def print_args(**args):
        pass
```
    如果把带有*args和**args的位置参数混合起来，就会按照顺序解析。
    
## 文档字符串
    在函数体开始的部分附上函数定义说明的文档，就是函数的字符串。
```python
    def print_args(**args):
        'echo return its input argument'
        pass
        
  #可以定义更长的字符串
    def print_args(**args):
        '''echo return its input argument
        gdjglajfgag jfaojigiab fjajofdi '''
        pass
        
```
    用Python函数help()可以打印出一个函数的文档字符串。如：help(print_args)
    
## 一等公民：函数（函数复杂定义及应用）
  Python中一切皆对象，包括数字，字符串，元组，列表，字典，函数。函数是Python中一等公民，可以把它们（返回值赋给变量），可以作为
被其他函数调用，也可以从其他函数中返回值。
    
```python
    #函数中的函数,传入的值是一个函数名，在一个函数中调用另一个函数
    def run_something(func)
        func()
    #传参函数的函数
    def run_something(func,arg1,arg2)
        func(arg1,arg2)
```
### 内部函数
    可以在函数中定义另外一个函数
```python
    #返回的是一个值
    def print_args(**args):
        def inner():
            pass
        return inner()
```
### 闭包
    闭包：一个可以被动态创建的可以记录外部变量的函数。
    
```python
    #返回的是一个函数，
    def print_args(args):
        def inner():
            return "%s" ,%args
        return inner 
        
```

### 匿名函数：lambda()函数
    lambda函数是用一个语句表达的匿名函数，可以用它来代替小的函数。
    
```python
    def edit_stroy(words,func):
        for word in words:
            print(func(word))
    
    def enliven(word):
        return word.capitalize() + '!'
        
    #调用函数为
    edit_stroy(starirs,enliven)
    #用匿名函数为
    edit_stroy(starirs,lambda word: word.capitalize() + '!')
    
    #lambda函数接收一个参数word。在冒号和末尾圆括号之间的部分为函数的定义。
    
    
```
    
## 生成器
  生成器使用来创建一个Python对象的。用它可以迭代庞大的序列，且不需要在内存中创建和存储整个序列。通常，生成器是为迭代器产生数的。
它会记录上一次调用的位置，并且返回下一个值。这一点和普通函数都是不一样的，一般函数不记录前一次调用，而且都会在函数的第一行执行。

```python
    def my_range(first=0,last=10,step=1):
        number=first
        while number < last:
            yield number   #记录上一次调用的位置，并且返回下一个值
            number += step
        
```
## 装饰器
    装饰器实质是一个函数 =。它把一个函数作为输入并且返回另外一个函数。通常使用如下技巧：
- *args 和 **kwargs
- 闭包
- 作为参数的函数

## 名称中的_和_的用法
    
```python
    def my_range(first=0,last=10,step=1):
        number=first
        while number < last:
            yield number   #记录上一次调用的位置，并且返回下一个值
            number += step
    
    my_range._name_ #显示函数名
    my_range._doc_ #显示文档字符串
```

## try和except处理错误
    正常执行try后面的语句，错误则执行except后面的语句。
```python
    try：
        pass
    except：
        pass
     
```
    获取异常对象：
        except exceptiontype as name
    如：except IndexError as err：将一个IndexError异常值赋给err
    

