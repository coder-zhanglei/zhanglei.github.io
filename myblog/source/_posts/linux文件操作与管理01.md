---
title: linux文件操作与管理01
date: 2019-03-06 15:34:49
tags: 
    - Linux指令
categories: 
    - linux浅见
---
## diff：生成差异文件

（1）参数说明

|  参 数        |  说明    |
| :--------:    | :----: |
|-c      | 显示所有内容，同时标出不同之处                |
|   -a       | 对文本文件进行逐行比较，非文本文件看作文本文件进行比较            |
| -i       | 忽略大小写的不同      |  
| -r       | 比较目录时递归比较子目录中的文件      |  

### 范例
```bash
    diff -a a1.txt a3.txt #比较两个文件的不同
    diff Desktop/yy1  Desktop/yy2  # 比较两个文件夹的不同
    diff -c a1.txt a3.txt #比较两个文件的不同，并生成差异文件

```
## find ：查找目录或者文件
- 语法： find[路径][-可选参数]

### 范例
```bash
    find *.txt # 查找.txt的文件
    find /root/edsktop/yy1/ -ctime -2  #查找448小时内被修改过的文件
    find -name yy* #查找指定字符串类型的目录
    find -name yy.*#查找的结果是以yy命名的文件
    find -size 0#查找字节数为0的文件
```
## ftp ：文件传输指令

### 范例
```bash
    ftp 192.168.1.1 connected to 192.168.1.2#使用ftp地址建立ftp连接

```
注：建立的过程会输入用户名和密码，建立之后可用get和put指令实现文件的上传和下载
删除文件用delete指令

## gunzip：解压文件

### 范例
```bash
    gunzip yy.txt.gz #解压文件
    gunzip -l yy.txt.gz #解压文件时显示文件相关信息

```
## gzip：压缩文件

### 范例
```bash
    gzip -v yy.txt #压缩文件时显示文件相关信息
    gzip -d yy.txt.gz #解压指定文件

```



