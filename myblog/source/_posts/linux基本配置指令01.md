---
title: linux的基本配置指令01
date: 2018-10-04 17:10:11
tags: 
    - Linux指令
categories: 
    - linux浅见
---
### alias指令： 设置指令的别名
- 目的： 使用该指令可以对存在的指令设置一个容易记忆的别名
- 语法： alias 别名 = ‘复杂的指令’
#### 范例
```bash
	alias p = ‘passwd’
	alias a = 'adduser -d /home/she-p 123456 sun' #设置别名
	alias #列出当前已经设置的别名
```
ps： 重启系统别名失效，如果想要永久生效，需要编辑文档/home/gec/.bashrc来实现
该文件在root用户下。

### man:显示指令的帮助信息
- 目的:用man指令查看shell指令和相关函数
- 语法:[-可选参数] 指令名
- 说明: ubuntu中man的手册默认没有装。用下面几条命令就行了：
 sudo apt-get install manpages 
 sudo apt-get install manpages-de 
 sudo apt-get install manpages-de-dev 
 sudo apt-get install manpages-dev
ubuntu man手册完善
Linux提供了丰富的帮助手册，当你需要查看某个命令的参数时不必到处上网查找，只要man一下即可。
Linux 的man手册共有以下几个章节：
1、Standard commands （标准命令）
2、System calls （系统调用）
<font color=#7e7129>3、Library functions （库函数）</font>
4、Special devices （设备说明）
5、File formats （文件格式）
6、Games and toys （游戏和娱乐）
7、Miscellaneous （杂项）
8、Administrative Commands （管理员命令）
#### 范例
```bash
	man --help #帮助文档
	man 3 open #查看open函数，3代表查看库函数
	man 1 ls #查看ls命令，1代表查看标准命令
```
ps：man -k who 后面提到，-k：显示与指定字符匹配的标题字符串的每一行

### apropos：查找使用手册的名字和相关描述
- 目标：查找一个不知道的能完成某种特殊任务的命令名称，有时候会忘记执行特定任务的命令，就可以使用apropos找出来
- 语法：apropos [必要参数] [选择性参数] 关键词
- 参数说明：
（1）必要参数

|  参 数        |  说明    |
| :--------:    | :----: |
|-d   | 输出调试信息                 |
|  -v       | 输出详细的警告信息        |
| -r       | 认为每个关键词是一个通常的表达式    |  
|  -w       | 认为每个关键词进行精确匹配  |     
|  -c      | 对每个关键词进行精确匹配     |                        

（2）非必要参数

|  参 数        |  说明    |
| :--------:    | :----: |
|-s      | 只在给定的部分进行搜索                |
|   -h       | 帮助信息            |
| -V       | 版本信息      |  

内建指令：whatis，man
#### 范例
```bash
    apropos -r ls#以通常的方式找关键词ls
    apropos who #等同于man -k who 
```






