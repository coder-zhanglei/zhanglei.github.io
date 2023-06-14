---
title: linux基本配置指令04
date: 2019-02-24 15:32:24
tags: 
    - Linux指令
categories: 
    - linux浅见
---
### export ：设置或在显示环境变量

#### 范例
```bash
    export -p #列出所有环境变量
    export M_ENV = http://www.linux.org/ #定义环境变量 
 ```
### lsmod：显示Linux内核的模块信息

#### 范例
```bash
    lsmod #显示载入系统的模块信息
    
    ```
### reboot指令：重新启动

- 语法: reboot [-可选参数]
#### 范例
```bash
    reboot -f #强制重启
    reboot -i #关闭网络设置后在重新启动
    reboot -n #先保存数据，再重启
    
    ```
### hostname ：显示或者设置当前系统的主机名
- 语法：hostname [必要参数][选择性参数]

#### 范例
```bash
    hostname -i #显示主机ip地址
    hostname -d #显示主机域名
    hostname Apple #设置主机名称
    ```
    