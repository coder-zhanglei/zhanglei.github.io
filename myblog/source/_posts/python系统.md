---
title: python系统
date: 2019-04-08 14:53:49
tags: 
    - Python系统
categories: 
    - Python心得
---
## 文件
- 创建文件

```python
    fb = open('test.txt','wt')
    fb.close()

```
- 检查文件是否存在

```python
    import os
    os.path.exists('oops.txt')

```
- 用isfile()检查是否为文件
```python
    #判断是否文件
    name = 'oops.txt'
    os.path.isfile(name)
    #判断是否是目录
    os.path.isdir(name)
    #isabs()判断参数是否是一个绝对路径名，参数不需要是一个真正的文件
    os.path.isabs(name)
    os.path.isabs('/big/fake/name')
    
    
```
- copy()复制文件
  copy()函数来自另一个模块shutil

```python
    import shutil
    shutil.copy(oops.txt,'ohno.txt')
    
```
- rename()重命名文件

```python
    import os
    os.rename('ohno.txt','ohwell.txt')
    
```
- 用abspath()获取路径名
  该函数会把相对路径扩展为一个绝对路径名
  os.path.abspath('oops.txt')
  
- realpath()获取符号的路径名

- remove 删除文件
 os.remove('oops.txt')
 
## 目录
- 创建目录
  os.mkdir('pomes')
- rmdir()删除目录
  os.rmdir('pomes')
- 列出目录内容
  os.listdir('pomes')
  
- 使用chdir()修改当前目录
  可以从一个目录跳转到另一个目录
  os.chdir('pomes')

- glob()列出匹配文件
 
```python
    import golb
    glob.glob('m*')#获取以m开头的文件和目录
    glob.glob('？？')#获取所有名称为两个字符的文件和目录
    glob.glob('m????e')#获取名称为6个字符并且以m开头以e结尾
    glob.glob('[klm]*e')#获取所有以k、l或者m开头的文件和目录
    #[!abc]会匹配除了a、b和c之外的所有字符
    
```
## 程序和进程
  进程之间是相互隔离的，一个进程无法访问其他进程的内容，也无法操作其他进程。操作系统会根据所有正在运行的进程，给每一个进程一小段运行时间，然后切换到
其他进程，这样既可以做到公平又可以响应用户操作。

```python
    import os
    os.getpid()#获取当前进程id号
    os.getcwd()#当前工作目录
    os.getuid()#获取用户ID
    os.getgid()#获取用户组ID
    
```
### subprocess创建进程
  import subprocess
  ret = subprocess.getoutput('date')
  
## 使用multiprocessing创建进程
  multiprocessing模块可以在一个程序中运行多个进程
  
```python
import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print 'Process %s says:%s' %(os.getpid(),what)
    

if __name__=="__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,args=("I'm function %d" %n))
        p.start()
    
```
## 使用terminate()终止进程

```python
     p = multiprocessing.Process(target=do_this,args=("I'm function %d" %n))
     p.start()
     p.terminate()
     
```

## 日期和时间
  import calendar
  calendar.isleap(1900)#判断1900是否死闰年

### datetime模块
  dattime定义了4个主要的对象：
- date 处理年、月、日
- time 处理时、分、秒
- datetime 处理日期和时间同时出现的情况
- timedelta处理日期和时间的间隔

```python
     from datetime import date 
     halloween = date(2014,10,31)
     halloween.day
     halloween.month
     halloween.isoformat()#打印一个date对象，ISO是ISO 8601，一种表示日期和时间的国际标准
     
```
### time模块
  一种表示绝对时间的方法是计算从某个起点开始的秒数。unix时间使用的是从1970年1月1日0点开始的秒数。
  time模块的time()函数会返回当前时间的纪元
  localtime()函数返回当前系统时区下的时间，gmtime()返回UTC时间
  strftime()
```python
    import time
    now = time.time()
    time.ctime(now) #把一个纪元值转换为一个字符
    curtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))#获取当天的时间
    cur = time.mktime(time.strptime(curtime,'%Y-%m-%d'))

```
## 读写日期和时间

|格式化字符串 | 日期/时间单元  | 范围  |
| --------   | -----:  | :----: |
| %Y   | 年  |  1900-... |
| %m       |   月   |   01-12    |
| %B       |   月名    |   January，....    |
| %b  | 月名缩写  | Jan-... |
| %d       |   日  |   01-31    |
| %A       |   星期    |   Sunday，....    |
| %a       |   星期缩写  |  Sun-... |
| %H       |   时（24小时制）   |   00-23    |
| %I       |   时（12小时制）   |   01-12....    |
| %p       |   上午/下午  |  AM，PM |
| %M       |   分   |   00-59    |
| %S       |   秒   |   00-59    |

  
```python
    import time
    fmt ="It's %A ,%B %d,%Y,local time  %I:%M%S%p"
    t = time.localtime()
    

```

## 其他模块
- arrow分
- dateutil
- iso8601
- fleming 提供许多时区的函数




