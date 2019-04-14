---
title: Python真正的开发者
date: 2019-04-08 20:21:43
tags: 
    - Python开发
categories: 
    - Python心得
---
## 寻找Python代码

- Python标准库：http://docs.python.org/3/library/ 
- python包索引(PyPi)：https://pypi.python.org/pypi

## 安装包
### 安装包的方法
- 用pip，如：pip install flask
- 用操作系统自带的包管理工具
- 源代码安装:python install setup.py


## 调试代码
### 用pdb进行调试

1、 语句
```bash
  Python -m pdb capitals.py   
  (Pdb) c  #输入c（继续），程序会一直运行下去，直到正常结束或者出现错误
  (Pdb) s  #单步执行，一行一行的执行Python代码，会进入函数内部
  (Pdb) n  #也是单步执行，但是不会进入函数内部
  (Pdb) l  #列表，查看之后的几行
   ->  # 指示当前行
  (Pdb) b 6 #在第6行设置一段点
  (Pdb) p line #打印line的值   
  (Pdb) l 1 #l会显示代码行，1表示起始行。从第一行开始

```

## 记录错误日志
  logging模块包含以下内容：
  
- 你想保存到日志中的消息
- 不同优先级以及对应的函数：debug()、info()、warn()、error()、critical().
- 一个或多个logger对象，主要通过它们使用模块
- 把消息写入终端、文件、数据库或者其他地方的handler
- 创建输出的formatter；
- 基于输入进行筛选的过滤器。

```python
    import logging
    logging.basicConfig(level='DEBUG',filename='bulue_ox.log')#filename会创建一个fileHandler并对logger进行设置。logging模块至少包含15钟handler
    
    #以日期和时间的格式写入日志文件
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='./gzipcompressor.log',
                        filemode='a',
                        level=logging.DEBUG, 
                        format=LOG_FORMAT)

```

## 算法和数据结构
  列表解析比添加元素快2倍。
  NumPy是Python的一个数学库，它是用c编写的，运行速度很快。Python并不会编译成机器语言，而是被翻译成中间语言，然后被虚拟机解释执行。
  












