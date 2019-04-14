---
layout: ew
title: 创建自己的github代码库
date: 2019-04-13 22:12:00
tags: 
    - 创建自己的代码库
categories: 
    - 代码托管
---

## 我的代码库
  网址： https://github.com/coder-zhanglei/zhanglei.github.io.git
  参考的博客： https://www.cnblogs.com/zhixi/p/9584624.html
  
## 准备工作
1、 在github上创建自己账号，建立自己的代码库，已完成
2、 安装git软件，下载地址：https://windows.github.com/  或  https://git-scm.com/download/win
注：安装好git后右键就有Git Bash Here可以打开git上传下载文件的框

## 基本配置
1、 添加本地目录到远程仓库
  在你的本地文件目录下右击，就会出现Git Bash选项，点击进入。
2、 设置用户名和邮箱地址。这两个值是作为上传时记录的值。输入命令：

```bash
    git config --global user.name "用户名"
    git config --global user.email "邮箱"
   #设置好后可以用命令查看当前的设置：
   git config --global user.name
   
```
## 下载和上传远程仓库的文件
1、 首先初始化本地仓库
  
```bash
    git init 
    
```
  注：会生成.git的隐藏文件。没有生成就是没初始化成功
  
2、 连接远程仓库

```bash
    git remote add origin "https://github.com/GitHub用户名/代码仓库名称.git"
    git remote add origin  https://github.com/coder-zhanglei/zhanglei.github.io.git
```
  可以通过git remote -v 查看本地链接到的远程仓库
```bash
    git remote -v 
    
```

  若分支设置错误，可以查看后切换分支
【git remote rm origin】 删除现有远程仓库 
【git remote add origin url】添加新远程仓库

```bash
   git remote rm origin
   git remote add origin url
   
```
    
### 下载
1、 从远程仓库拉取所有更新（每次上传项目都要操作）

```bash
    git pull origin master
    
```

  注意：此处极易报错！
  因为远程代码仓库和本地代码仓库合并后，可能会有冲突，如有报错，使用git status查看状态
  
  pull，因为两个仓库不同，发现refusing to merge unrelated histories，无法pull
  因为他们是两个不同的项目，要把两个不同的项目合并，git需要添加一句代码，在git pull，这句代码是在git 2.9.2版本发生的，最新的版本需要添加--allow-unrelated-histories
git pull origin master --allow-unrelated-histories
  注：在 git pull origin master --allow-unrelated-histories此步操作时，.gitignore文件错误冲突并没有解决，只是强制合并忽略掉了

### 创建分支，上传文件
  因为git是分布式管理，所以尽量不要在master主分支上作开发，例如自己有一个项目，在外面开发时，可以使用分支1，在家开发时可以使用分支2，如果有其他人参入 ，分别 使用分支3，4，5
每次提交本地代码时候，先合并远程master主分支到本地，再提交

1、 创建本地分支

```bash
   git branch 分支名
    
```
2、 切换本地分支
```bash
   git checkout 分支名
    
```

3、 本地分支提交

```bash
   git  add .
   git  commit -m ‘dev'
   git push -u origin dev
    
```

4、 合并本地分支到master

```bash
   git  checkout master
   git pull origin master
   git merge origin/master  //合并分支
   git status
   
On branch master
Your branch is ahead of 'origin/master' by 12 commits.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean
   #上面的意思就是你有12个commit，需要push到远程master上 
   #执行下面命令即可

   git push origin master
   
```
#### 上传指令的区别
$ git push origin

上面命令表示，将当前分支推送到origin主机的对应分支。 
如果当前分支只有一个追踪分支，那么主机名都可以省略。 
$ git push 如果当前分支与多个主机存在追踪关系，那么这个时候-u选项会指定一个默认主机，这样后面就可以不加任何参数使用git push。
$ git push -u origin master 上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了。
 不带任何参数的git push，默认只推送当前分支，这叫做simple方式。此外，还有一种matching方式，会推送所有有对应的远程分支的本地分支。Git 2.0版本之前，默认采用matching方法，现在改为默认采用simple方式。
## 仓库的管理
  删除仓库，参考博客：https://blog.csdn.net/weixin_42152081/article/details/80635777
### 一.删除已有仓库
  如果我们想要删除Github中没有用的仓库，应该如何去做呢？
  进入到我们需要删除的仓库里面，找到“settings”即仓库设置：
  然后，在仓库设置里拉到最底部，找到“Danger Zone”即危险区域：
  点击“Delete this repository”这样就可以删除该仓库了。
### 二.删除Github中的某个文件或文件夹
  1.本地仓库和远程仓库同时删除
  例如要删除如图所示的_config.yml和index.md两个文件：
  我们先在本地把两个文件删除，然后执行以下命令：
  
```bash
    git add * //把本地仓库的文件上传到缓存。
    git commit -m 'del' //把第一步上传到缓存的东西上传到本地仓库，其中'del'是操作标识，内容随便填，方便用户观看。
    git push origin master //把本地仓库的文件上传到远程仓库。
    
```
  这样，再打开远程仓库就可以看到两个文件已经被删除了：
  