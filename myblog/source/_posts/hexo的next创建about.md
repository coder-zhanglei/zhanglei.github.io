---
title: hexo的next创建about
date: 2018-12-09 14:09:44
tags: 
    - 初识hexo
categories: 
    - 初识hexo
---
## hexo的next创建about
### 创建步骤
 - 1、新建一个about页面，命令如下 ： 
 

``` bash
$ hexo new page about
```
 注：在myBlog/source下会生成一个行的文件夹about，在该文件夹下会有一个index.md文件

	- 2、 菜单显示about链接，在主题的thems/next/_configy.yml设置中将menu中的about前面的注释去掉
	
``` bash
menu:
home: /
archives: /archives/
categories: /categories/
tags: /tags/
about: /about/
```


