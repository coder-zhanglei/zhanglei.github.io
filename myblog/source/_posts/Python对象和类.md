---
title: Python对象和类
date: 2019-04-04 11:07:13
tags: 
    - Python中的类
categories: 
    - Python心得
---

## 对象
  Python中所有数据都是以对象的形式出现，只有当你想要创建属于自己的对象或者需要修改已有的对象的行为时，才需要关注对象的内部
实现细节。对象就是包含了代码的超级数据结构。

## class 定义类
  
```python
    class Person():
        def __init__(self):#初始化，self是参数指向了这个正在被创建的对象的本身
            pass
    
```
  在类声明里定义__init__()方法时，第一个参数必须为self，在定义类的方法（函数）时，第一个参数也必须为self。在定义中__init__
不是必须的。只有当需要区分由该类创建的不同对象时，才需要指定。

## 继承
  从已有的类衍生出新的类，添加或修改部分功能。习惯称原始的类为父类，超类或基类，将新的类称为子类或衍生类。

```python
    class Person():
        def __init__(self):#初始化，self是参数指向了这个正在被创建的对象的本身
            pass
    class People(Person):#继承了Person
        pass 
```
  在子类中可有覆盖父类的方法，从新实现父类的方法即可实现方法的覆盖。
  
### 用super从父类得到帮助
  重子类中调用父类的方法，用super实现

```python
    class Person():
        def __init__(self,name):#初始化，self是参数指向了这个正在被创建的对象的本身
            pass
    class People(Person):#继承了Person
        def __init__(self,name):
            super().__init__(name)#调用父类的方法
        pass 
```

## 使用属性对特性进行访问和设置
  不希望别人直接访问这个特性，因此需要定义两个方法：getter，setter。
```python
    class Person():
        def __init__(self,name):#初始化，self是参数指向了这个正在被创建的对象的本身
            pass
    class People(Person):#继承了Person
        def __init__(self,name):
            super().__init__(name)#调用父类的方法
        @property    #用于指定getter方法
        def name(self):
            retrun 'afad'
        @name.setter  #用于指定setter方法
        def name(self,input_name)
            self.name = input_name
```
  如果没有指定setter属性，将无法从类的外部对它进行值的改变。
  
## 使用名称重整保护私有特性
  对那些需要刻意隐藏在类内部的特性有自己的命名规范：由（__）双下划线开头。
  
```python
    class Duck():
        def __init__(self):
            pass
            
        @property
        def name(self):
            retrun self.__name
        @name.setter
        def name(self,name)
            self.__name = name#这种，让外部的代码无法使用
            
```

## 方法的类型’
  有些数据（特性）和函数（方法）是类本身的一部分，还有一些是由类创建的实例的一部分。在类的定义中，以self作为第一个参数的方法
都是实例的方法。

```python
    class A():
        count = 0
        def __init__(self):
            A.count += 1;#类特性
        def __init__(self):
            print 'I'm an A'
        @classmethod#类方法，第一个参数是类本身。参数被写作cls，全称class是保留字
        def kids(cls):
            print 'A has',cls.count,"little objects"
    easy_A =A()
    
            
```

## 特殊方法
  特殊方法的名称以双下划线（__）开头和结束。
- 表1：和比较相关的方法

| 方法名        | 使用    |
| :--------:   | :-----:  | 
| _ _eq_ _(self,other)     | self == other     |
|  _ _ ne _ _(self,other)        | self != other     |
|  _ _ lt _ _(self,other)        | self < other     |
|  _ _gt_ _(self,other)        | self > other     |
|  _ _le_ _(self,other)        | self <= other     |
|  _ _ge_ _(self,other)        | self >= other     |

- 表2：和数学相关的方法

| 方法名        | 使用    |
| :--------:   | :-----:  | 
| _ _ _add_ _(self,other)     | self + other     |
|  _ _ _sub_ _ _(self,other)        | self != other     |
|  _ _ _ mul _ _ _(self,other)        | self * other     |
|  _ _ _floordiv_ _ _(self,other)        | self // other     |
| _ _ _truediv_ _ _(self,other)        | self / other     |
| _ _ _mov_ _ _(self,other)        | self % other     |
|  _ _ _pow_ _ _(self,other)        | self ** other     |

- 表2：其他种类的方法

| 方法名        | 使用    |
| :--------:   | :-----:  | 
| _ _ _str_ _ _(self,other)     | str(self)  |
|  _ _ _repr_ _ _(self,other)        | repr(self)     |
|  _ _ _len_ _ _(self,other)        | len(self)   |


```python
    class Word():
        def __init__(self,text):
            self.text = text
        def __eq__(self,words):
            return self.text.lower = words.text.lower()
        def __str__(self,words):
            return self.text
        def __repr__(self,words):
            return 'Word(" 'self.text' ")'
    first = word('ha')
    
            
```
## 组合
  将类作为参数传入另一个类。
```python
    class Bill():
        def __init__(self,description):
            self.description = description
            
    class Bill():
        def __init__(self,length):
            self.length = length
    class Duck():
        def __init__(self,bill,tail):
            self.bill = bill
            self.tail = tail
        def about(self):
            print('this duck has a ',bill.description,'bill and a',tail.length,'tail')
            

```