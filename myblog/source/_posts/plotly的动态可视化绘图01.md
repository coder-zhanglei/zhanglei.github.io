---
title: plotly的动态可视化绘图01
date: 2019-05-23 19:40:42
tags: 
    - plotly模块开始
categories: 
    - Python数据分析
---
## plotly安装
```bash
    pip install ploty
    pip install ploty --upgrade #更新plotly

```
- 查看帮助 
```bash
    import plotly 
    help(plotly.offline.plot)
    
```

## 离线绘图函数

```python
import plotly as py
from plotly.graph_objs import Scatter, Layout, Data

py.offline.init_notebook_mode()     #该条语句是在Jupyter Notebook（此前被称为 IPython notebook）中绘图
trace0 = Scatter(  #确定坐标 x，y
    x = [1,2,3,4,],
    y = [10,15,12,17]
)
trace1 = Scatter(
    x = [1,2,3,4,],
    y = [16,5,11,9]
)

data = Data([trace0, trace1])#两条线

#py.offline.iplot(data, filename='first_offline_start') IPlot是在Notebook中绘图的函数
py.offline.plot(data, filename='first_offline_start')
#py.offline.plot(data, filename='first_offline_start',image='png')#保存画出的png图片

```
   参数解释：
   def plot(figure_or_data, show_link=False, link_text='Export to plot.ly',
         validate=True, output_type='file', include_plotlyjs=True,
         filename='temp-plot.html', auto_open=True, image=None,
         image_filename='plot_image', image_width=800, image_height=600,
         config=None, include_mathjax=False, auto_play=True,
         animation_opts=None):
   py.plot是绘制图形的主函数，主要参数如下：
   figure_or_data：绘图的数据
   show_link:默认为False，显示右下角的链接
   link_text:右下角显示的文字，默认为Export to plotly.ly
   validate:确保所有关键字是有效的。但是当需要额外、非必须的关键字或plo.js版本比graph_reference.json版本旧时，会忽略这部分内容。
   filename：设置绘图结果的存储路径。
   image_filename：保存绘制的图片(.png ) 格式

### 模块解释
  plotly模块库里的graph_obj（图像对象）子模块的Scatter（数据布局）对象定义，跟函数和对象一样是字典格式。
  Data函数，把代表两条曲线的变量定义为一组图形数据，一列表的格式[]。
    
## 基本绘图流程

- 添加图规数据（add_trace）,使用的是Scatter等函数命令
- 设置画面布局，使用layout命令
- 集成图形，布局数据，命令有Data，Figure。
- 绘制图形的输出，命令是offline.plot,自定义的短命令是pyplt。







