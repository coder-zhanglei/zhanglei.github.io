---
title: linux基本配置指令03
date: 2019-02-23 17:30:05
tags: 
    - Linux指令
categories: 
    - linux浅见
---
### manpath ：设置man手册的查询路径

#### 范例
```bash
    manpath #列出目前的查询路径
    manpath -M /home/zhang #指定查询路径
    ```
### free：显示内存信息

#### 范例

```bash
    free -b #以字节为单位显示
    free -k #以KB为单位显示
    free -m #以MB为单位显示
    free -s 10 #每隔10s执行一次free，连续显示内存信息
    ```
### crontab ：指定自动执行任务
- 语法: crontab [-u<用户名>] [-可选参数]

#### 创建新的 crontab 文件，或编辑现有文件
  创建 crontab 文件的最简单方法是使用 crontab -e 命令。
  此命令会调用已为系统环境设置的文本编辑器。系统环境的缺省编辑器在 EDITOR 环境变量中定义。如果尚未设置此变量，crontab 命令将使用缺省编辑器 ed。最好选择您熟悉的编辑器。
**以下示例说明如何确定是否已定义编辑器，以及如何将 vi 设置为缺省值**
``` bash
$ which $EDITOR
$ 
$ EDITOR=vi
$ export EDITOR
```

#### 创建 crontab 文件时，该文件会自动放入 /var/spool/cron/crontabs 目录，
 并以您的用户名命名。如果具有超级用户特权，则可为其他用户或 root 创建或编辑 crontab 文件。
  **$ crontab -e [username]**
**以下示例说明如何为其他用户创建 crontab 文件**
```bash 
  crontab -e jones
  1 0 * * 0 rm /home/jones/*.log > /dev/null 2>&1 #添加到新 crontab 文件中的以下命令项将在每个星期日的凌晨 1:00 自动删除用户起始目录中的所有日志文件。由于该命令项不重定向输出，因此将重定向字符添加到 *.log 之后的命令行中。这样可以确保正常执行命令。
  crontab -l #列出目前的时程表
  crontab -r #删除目前的时程表
 ```
 
#### 时程表格式如下
```bash
    f1 f2 f3 f4 f5 program
   #其中 f1 是表示分钟，f2 表示小时，f3 表示一个月份中的第几日，f4 表示月份，f5 表示一个星期中的第几天。program 表示要执行的程序。
   #当 f1 为 * 时表示每分钟都要执行 program，f2 为 * 时表示每小时都要执行程序，其馀类推
   #当 f1 为 a-b 时表示从第 a 分钟到第 b 分钟这段时间内要执行，f2 为 a-b 时表示从第 a 到第 b 小时都要执行，其馀类推
   #当 f1 为 */n 时表示每 n 分钟个时间间隔执行一次，f2 为 */n 表示每 n 小时个时间间隔执行一次，其馀类推
   #当 f1 为 a, b, c,... 时表示第 a, b, c,... 分钟要执行，f2 为 a, b, c,... 时表示第 a, b, c...个小时要执行，其馀类推
```
