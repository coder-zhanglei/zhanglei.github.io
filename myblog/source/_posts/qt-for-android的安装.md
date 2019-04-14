---
title: qt-for-android的安装
date: 2019-03-05 10:58:14
tags:
    - QT for Android环境搭建
categories: 
    - QT学习
---
## QT软件的安装
### 下载软件
https://pan.baidu.com/s/1o8CxKaptmVthHVE3x3sjXw  zndu
参考相关博客链接：https://www.jianshu.com/p/437465a530dc  
                  https://blog.csdn.net/qq_32250025/article/details/79106662
### 1、安装安装  java -jdk ,android-ndk,android-sdktools
- 安装 java -jdk，
  对应版本：jdk1.8.0_201
- 安装android-ndk ，
   安装ndk的时候，android-ndk-r10e以上的版本没有arm-linux-androideabi-gdb.exe，所以
在下载安装包的时候不能下载版本太高，10以下的版本就够.
- 安装android-sdktools  
   在安装sdk的时候会出现jdk找不到，或者版本过低，这时要先配置环境变量。当配置好环境变量出现版本过低的时候要重新下载jdk安装文件重新安装
，之前我安装jdk-11.0.2后，再安装sdk时出现版本过低，重新下载了jdk1.8.0_201安装就可以。
在配置qt文件的时候会出现不适一个平台，这时候要启动sdk文件夹下的SDK Manager.exe安装Android包。
- 安装ant
    这个是在qt软件上:工具->选项->android:下的Ant executable项后面有一个下载的符号，点击可自动下载。
ps：对应的软件都在网盘里
### 环境变量的配置
(1) JAVA_HOME  值： C:\Program Files\Java\jdk1.8.0_45
(2)ANDROID_HOME   值：D:\Android\sdk
(3)CLASSPATH   值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;

### 编译文件
   在构建的时候选择Android构建和运行就能够编译出.apk文件，对应的文件再编译文件夹下的/bin目录