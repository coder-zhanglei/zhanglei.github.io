---
title: linux文件操作与管理03
date: 2019-03-09 11:05:14
tags: 
    - Linux指令
categories: 
    - linux浅见
---
## rcp ：远程复制文件或目录
- 语法：rcp [- 可选参数]远程/本地主机名：源文件/目录  本地/远程主机名：目标文件/目录
- 参数选择

|  参 数        |  说明    |
| :--------:    | :----: |
| -p     | 保留源文件/目录的属性                  |
|   -r     | 处理指定文件夹下的文件及其子目录下的所有文件            |







### 范例
```bash
    rcp -p 192.168.1.121:/home/vc /home/yy/ #复制文件，将远程文件复制到本地/home/yy/，同时保留源文件的属性，一般主机名不用给
    
```
## tar ：打包同时压缩/解压文件
- 语法：[- 可选参数] [文件]
- 参数选择

|  参 数        |  说明    |
| :--------:    | :----: |
| -c  |   压缩文件            |
|  -x | 解压文件     |
|  -r |添加文件到已存在的备份文件的尾部     |
| -j  |   使用bzip2压缩文件            |
|  -z | 使用gzip压缩文件     |
| -v  |   显示详细信息            |
|  -f |指定备份文件     |
### 范例
```bash
    tar -xzvf s1.tar.gz  #解压s1.tar.gz 文件
    tar -czvf s1.tar.gz *.txt  #压缩.txt文件
    tar  -c a1.txt a2.txt >s1.tar #打包文件
```
## whereis ，which：查找文件
-语法 ：whereis/which [-可选参数] 文件
### 范例
```bash
    whereis *.txt #查找文件，查找目录下的.txt文件
    which az #查找文件，执行which az， 在环境变量$PATH指定的目录“/usr/bin”下查找文件，显示查找结果
```
## info：读取目录信息
### 范例
```bash
    info init >1.log #显示init的帮助信息
    info info #显示info的具体使用方法
```


