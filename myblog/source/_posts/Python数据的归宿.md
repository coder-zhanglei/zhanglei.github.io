---
title: Python数据的归宿
date: 2019-04-08 10:42:09
tags: 
    - Python数据的存取
categories: 
    - Python心得
---

## 文件的输入/输出
  一个运行中的程序会存取放在随机存储器（ARM）上的数据。
  fileobj = open(filname,mode)
  mode的第一个字母表明对其的操作：
- r表示读模式
- w表示写模式。如果文件不存在则新创建，如果存在则重写新内容
- x表示文件不存在的情况下创建并写文件
- a表示文件如果存在，在文件的末尾追加写内容
  mode的第二个字母是文件类型：
- t(或者省略)代表文本类型
- b代表二进制文件

```python
    fb = open('test.txt','wt')
    fb.write(str1)
    fb.close()

```
### write()写文本文件
  数据大可以分块写：

```python
    fout = open('relativity','wt')
    size = len(pome)
    offset = 0
    chunk = 100
    while Ture:
        if offset > size:
            break
        fout.write(pome[offset:offset+chunk])
        offset += chunk
    

``` 
### 用read、readline、readlines读取文本文件
  read()读到文件末尾，再次调用read()会返回字符串‘’。 readline()读取文件的一行，readlines()调用时读取一行，并返回单行字符列表。
  
```python
    fout = open('relativity','wt')
    while Ture:
        line = fout.readline()
        if not line:
            break
        poem += line
    fout.close()

``` 
### 使用with自动关闭文件
  with expression as variable:
  
```python
  with open('relativity','wt') as fout:
    fb.write(str1)
    
``` 
### 使用seek()改变位置
  函数tell()返回距离文件开始处的字节偏移量。函数seek()允许跳转到文件其他字节偏移量的位置。
  seek(offset,origin)
- 如果origin=0，从头开始偏移offset个字节
- 如果origin=1，从当前位置偏移offset个字节
- 如果origin=2，距离最后结尾处偏移offset个字节


```python
  fin = open('relativity','rt')
  fin.tell()
  fin.seek(151)#偏移到151处
``` 
## 关系型数据库

  数据库展现了表单形式的不同类型数据之间的关系，每一项有对应的关系。NoSQL数据库是键值对形式存储的数据。

```python
db = sqlite3.connect('books.db')#连接数据库
curs = db.cursor() #创建一个cursor对象来管理数据库
curs.execute('''create table book (title text,author text,year int)''') #对数据库执行一个或多个sql命令
db.commit()
#插入数据
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv','rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)
        print book[' title']
        curs.execute(ins_str,(book[' title'],book['author'],book['year']))

``` 
### DB-API
  应用程序编程接口。是访问某些服务的函数集合。DB_API是Python中访问关系型数据库的标准API。
主要函数如下所示：
- connect（） 连接数据库，包含参数用户名，密码，服务器地址等
- cursor()创建一个cursor对象来管理数据库
- execute()和executemany() 对数据库执行一个或者多个SQL命令
- fetchone()、fetchmany()和fetchall()得到execute之后的结果





