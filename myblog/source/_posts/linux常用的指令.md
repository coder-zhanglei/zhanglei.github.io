---
title: linux常用的指令
date: 2019-01-20 17:31:44
tags: 
    - Linux指令
categories: 
    - linux浅见
---
## linux查询进程指令
1、进程查询指令
```1c
    ps -ef | grep calculatorBuysell | grep -v grep | wc -l
```
注：该命令可以查询calculatorBuysell进程的个数

