---
title: linux用户指令01
date: 2019-03-03 20:20:28
tags: 
    - Linux指令
categories: 
    - linux浅见
---
## who：显示系统用户信息

### 范例
```bash
    who #显示当前登录系统的用户信息
    who -l -H# 显示用户登录位置
    
```

## whois：查找用户/域名信息

### 范例
```bash
    whois mary #查找Mary用户的信息
    whois www.miwifi.com # 查找目标网络信息
    
```
## bunzip2，bzip2，bzip2recover：解压.bz2类型的文件，压缩成.bz2文件，损坏.bz2文件的修复
### 范例
```bash
    bunzip2 -c filename.bz2 #解压后文件直接输出到标准输出
    bzip2 filename
    bzip2 -7 -k filename #压缩文件filename并保留原文件
    bzip2-b filename.bz2 #解压文件
    bzip2recover filename #修复.bz2文件
    
```
## linux中cat、more、less命令区别详解 
  linux中命令cat、more、less均可用来查看文件内容，主要区别有：
   cat是一次性显示整个文件的内容，还可以将多个文件连接起来显示，
它常与重定向符号配合使用，适用于文件内容少的情况；
more和less一般用于显示文件内容超过一屏的内容，并且提供翻页的功能。
**more比cat强大**，提供分页显示的功能，**less比more更强大**，提供翻页，跳转，查找等命令。
而且more和less都支持：用空格显示下一页，按键b显示上一页。下面详细介绍这3个命令。
 
 
 
 