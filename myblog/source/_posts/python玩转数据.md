---
title: python玩转数据
date: 2019-04-05 16:21:35
tags: 
    - Python数据处理
categories: 
    - Python心得
---
## Python数据编码

- 表1：编码方式

| 编码        |  说明    | 
| :--------:   | :-----:  | 
|   'ascii'   |  经典的7比特ASCII编码      |  
|   'utf-8'   |  最长用的以8比特为单位的变长编码      |  
|   'latin-1' |  被称为ISO 8859-1编码      |  
|   'cp-1252'   |  windows常用编码      |  
|   'unicode-escape' |  Python中Unicode的转义文本格式，\uxxxx或者\uxxxxxxxx    |  

## 解码
  解码是将字节序列转化为Unicode字符串的过程。
  
```python
    place = 'abcrdddd'
    place_bytes = place.encode('utf-8')
    place2 = place.decode('utf-8')

```
  尽可能统一使用UTF-8编码，出错率低，兼容性好，可以表达所有的Unicode字符
  
## 格式化
### 使用%的旧式格式化

- 表2：转换类型

| 格式        |  说明    | 
| :--------:   | :-----:  | 
|  %s     |  字符串      |  
|  %d   |  十进制整数     |  
|   %x |  十六进制整数     |  
|   %o  |  八进制整数     |  
|  %f |  十进制浮点数   |
|   %e | 以科学计数法表示的浮点数    |  
|   %g  |  十进制或科学计数法表示的浮点数     |  
|  %% |  文本值%本身   |   

```python
    '%s' %42
    '%10d %10f %10s' %(n,f,s) #最小域宽为10个字符，右对齐
    '%-10d %-10f %-10s' %(n,f,s) #最小域宽为10个字符，左对齐
    '%10.4d %10.4f %10.4s' %(n,f,s) #设定最大字符宽度为4，右对齐，浮点数的精度限制在小数点后4位

```

### 使用{}和format的新式格式化

```python
    '{} {} {}'.format(n,f,s)
    '{2} {0} {1}'.format(n,f,s)#0代表第一个参数
    
    d = {'n':42,'f':7.03,'s':'string cheese'}
    '{0[n]} {0[f]} {0[s]} {1}'.format(d,'other')#0代表整个字典，{1}代表字典后面的字符串的值
    
    '{0:>10d} {1:>10f} {2:>10s}'.format(n,f,s)#最小域宽为10个字符，左对齐
    '{0:<10d} {1:<10f} {2:<10s}'.format(n,f,s)#最小域宽为10个字符，右对齐
    '{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s)#最小域宽为10个字符,居中
    
    '{0:<10.4d} {1:<10.4f} {2:<10.4s}'.format(n,f,s)#设定最大字符宽度为4，右对齐，浮点数的精度限制在小数点后4位
    
    '{0:!^20s}'.format('BIG SALE')#用！代替空格填充
```

## 使用正则表达式匹配
  相关功能都在标准库re中，因此首先需要引用他。match()函数用于查看源是否是以模式开头
  
```python
  result = re.match('You','Young Frankenstein')
  youpatter = re.compile('You') #编译以加快匹配速度
  result = youpatter.match('Young Frankenstein')
  
```
- search()返回第一次成功匹配，如果存在的话
- findall() 返回所有不重叠的匹配，如果存在的话
- split()会根据pattern将source切分成若干段，返回这些片段组成的列表，
- sub()需要一个额外的参数replacement，它会把source中所有匹配的pattern改成replacement

### 特殊字符

表1：特殊字符

| 模式        |   匹配   | 
| :--------:   | :-----:  | 
|  \d     |  一个数字字符      |  
|  \D   |  一个非数字字符   |  
|  \w   | 一个字母或数字字符   |  
|  \W  |  一个非字母非数字字符    |  
|  \s  |  空白符   |
|  \S  |  非空白符   |  
|  \b  | 单词边界     |  
|  \B  | 非单词边界     |   
  
  
表2：模式标识符

| 模式        |   匹配   | 
| :--------:   | :-----:  | 
|  abc   |  文本值      |  
|  （expr）   |  expr   |  
|  .  |  除\n外的任何字符   |  
|  ^  |  源字符串的开头   |
|  $  |  源字符串的结尾   |  
|  prev?  | 0个或1个prev    |  
|  prev*  | 0个或多个prev，尽可能多地匹配    |   
|  prev*?  | 0个或多个prev，尽可能少地匹配    |  
|  prev+  | 1个或多个prev，尽可能多地匹配    |  
|  prev+？  | 1个或多个prev，尽可能少地匹配    | 
|  prev{m}  | m个连续的prev    |  
|  prev{m,n}  | m到n个连续的prev，尽可能多地匹配    |  
|  prev{m,n}？  | m到n个连续的prev，尽可能少地匹配    |  
|  [ abd ]  |  a或b或c |  
|  [^abd ]  |  非（a或b或c）   |  
|  prev{?=next}  | 如果后面为next，返回prev    |  
|  prev{?!next}  | 如果后面非next，返回prev    |  
|  （?<=prev）next | 如果前面为prev，返回next    |  
|  （?<!prev）next | 如果前面非prev，返回next    |  

  注：在匹配是为了防止转义用r'\bxxxxx'，  "expr1 | expr2" 表示 eppr1或expr2 。
 
### 模式：定义匹配的输出
  当使用match()或search()时，所有的匹配会以m.group()的形式返回到对象m中。
  
```python
  source = ''' I wish I may,I wish I might have a dish of fish tonight'''
  m = re.search(r'(. dish\b).*(\bfish)',source)
  >>> m.group()
  'a dish of fish'
  
  m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)',source)#(?P<name>expr)这样的匹配模式会匹配expr，并将匹配结果存入name的组中
  >>> m.groups()
    ('a dish', 'fish')
  >>> m.group('DISH')
    'a dish'
  >>> m.group('FISH')
    'fish'
  
```


 
 