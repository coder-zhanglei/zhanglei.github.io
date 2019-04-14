---
title: linux网络服务01
date: 2019-03-14 20:50:26
tags: 
    - Linux指令
categories: 
    - linux浅见
---

## ifconfig: 显示或者配置网络设备
- 语法：ifconfig [网络设备] [-可选参数]

### 范例
```bash
    ifconfig  #显示当前网络设备状态
    ifconfig eth0 192.168.1.1 netmask 255.255.255.0 #配置网卡参数
    ifconfig eth1 down #关闭网卡
    ifconfig eth1 up #开启网卡
    ifconfig eth1 hw ether 00:10:B2:56:64:2B #修改网卡的物理地址
```

## ping:测试网络
- 语法：ping [-可选参数] 网络地址

### 范例
```bash
    ping 128.168.12.13 #检测ping的与远端主机的连通情况
    ping -c 128.168.12.13 #指定发送数据包的次数
```

## netstat：显示网络状态
- 语法：netstat [必要参数] [选择性参数]

### 范例
```bash
    netstat -r #显示系统的路由表
    netstat -an #显示详细的网络状况
```
## telnet:远程登录
- 语法：telnet [-可选参数] 主机名/IP

### 范例
```bash
    telnet 192.168.1.1 #远程登录
    
```
## rsh ：远端登录的shell
- 语法：rsh [-可选参数] 主机 指令

### 范例
```bash
    chkconfig rlogin on #启动rlogin工具
    rlogin 192.168.1.1 #登录远程主机
    rsh -l mary 192.168.1.1 /bin/pwd #登录远程主机执行指令/bin/pwd,要正确执行该指令，必须现在远程主机192.168.1.1上启动rlogin指令

```














