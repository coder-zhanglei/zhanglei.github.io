---
title: linux的日志与进程管理
date: 2019-03-16 10:23:28
tags: 
    - Linux指令
categories: 
    - linux浅见
---

## nice:设置优先级
- 语法：nice [-可选参数] [指令] [属性]
### 范例
```bash
    nice -n 17 free -s 60& # 在后台运行free指令，设置优先级为17
   # 注解：将free -s 60&的优先级设为17，通过ps -l输出的NI项就可以看当前系统中相关进程的优先级
    
```

## ps指令：报告程序状况
- 语法：ps [-可选参数]

### 范例
```bash
    ps -a #显示系统进程
    pstree -anh #显示进程间的关系 a:显示完整的指令，n:以进程ID排序，h:对现在执行的程序进行特别标注
```

## fg：将后台任务拉到前台执行
### 范例
```bash
    ftp 192.198.88.2 &
    fg %1 #将ftp拉到前台执行
```

## killall：杀死同名的所有进程
### 范例
```bash
    killall joe
```


