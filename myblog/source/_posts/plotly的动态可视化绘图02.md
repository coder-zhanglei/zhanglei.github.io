---
title: plotly的动态可视化绘图02
date: 2019-05-24 11:39:44
tags: 
    - plotly基础图形
categories: 
    - Python数据分析
---

## 散点图
  plotly没有独立的线形图函数，而是把线形图与散点图全部用Scatter函数实现。

散点图和线图的混合
```python
import plotly as py
import plotly.graph_objs as go

#--------pre def
pyplt = py.offline.plot

#-------code
# Create random data with numpy
import numpy as np

N = 100
random_x =  np.linspace(0,1,N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

#Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',       #纯散点图的绘制
    name = 'markers'        #曲线名称
)

trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',  # 散点+线 图的绘制
    name='lines+markers'  # 曲线名称
    
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',  # 线 图的绘制
    name='lines'  # 曲线名称

)

data = [trace0, trace1,trace2]
pyplt(data,filename='scatter_basic_demo.html')

```
  markers、lines、lines+markers三个图形的输出格式不同，是因为Scatter函数中的mode参数不同，

样式的设置：

```python
import plotly as py
import plotly.graph_objs as go

# --------pre def
pyplt = py.offline.plot

# -------code
# Create random data with numpy
import numpy as np

N = 500
x = np.linspace(0, 1, N)

random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
trace0 = go.Scatter(
    x=np.random.randn(N),
    y=np.random.randn(N)+2,
    mode='markers+lines',  # 纯散点图的绘制
    name='above',  # 曲线名称
    marker = dict(
        size = 10,#设置点的宽度
        color = 'rgba(152, 0, 0, .8)',#设置点的颜色
        line = dict(
            width = 2, #设置线条的宽度
            color = 'rgb(0, 0, 0)' #设置线条的颜色
        )
    )
    
)

trace1 = go.Scatter(
    x=np.random.randn(N),
    y=np.random.randn(N) - 2,
    mode='markers',  # 散点+线 图的绘制
    name='Below',  # 曲线名称
    marker = dict(
        size = 10,#设置点的宽度
        color = 'rgba(255, 182, 193, .9)',#设置点的颜色
        line = dict(
            width = 2, #设置线条的宽度
            
        )
    )
)


data = [trace0, trace1]

layout = dict(
    title = 'Styled Scatter',
    yaxis = dict(zeroline = True),
    xaxis = dict(zeroline = False)
)

fig = dict(data=data, layout = layout)
pyplt(fig, filename='scatter_basic_demo.html')


```

使用Scatter函数可以绘制线形图与散点图，主要参数如下;
- connectgaps:布尔变量，用于连接缺失数据
- dx、dy:x、y坐标的步进值，默认值是1
= error_x,error_y:x,y出错信息
- fillcolor：填充模式
- hoverfinfo：当用户与图形互动时，鼠标指针显示的参数，包括x，y，z坐标数据，
以及text（文字信息），name（图形名称）等参数的组合，可使用+，all，none和skip（忽略）作为组合连接符号，默认是all（全部消失）
- hoveron：当用户与图形互动时，鼠标指针显示的模式，包括points（点图），fills（填充图）和points+fills三种模式
- ids：在动画图表中数据点和图形key键的列表参数。
- legendgroup：图例参数，默认是空字符串
- line：线条参数，包括大小，颜色，格式等
- marker：数据节点参数，包括大小，颜色，格式等
- mode ： 图形格式，包括lines，marker，text，使用+或none等符号进行模式组合
- name：名称参数
- opacity：透明度参数，范围是0~1
- rsrc，xsrc，ysrc，tsrc，idssrc，textsrc，textpositionsrc：字符串源数列表
- r、t：仅用与极坐标图，r用于设置径向坐标（半径），t用于设置角坐标
- showlegend：布尔变量，用于切换图标显示
- stream：数据流，用于实时显示数据图表
- textfont：文本字体参数，包括字体名称，颜色，大小等
- textposition：“文本”元素的位置参数，包括top left（）
- text:文本数据
- type：数据显示模式 constant，percent，sqrt，array（数组）
- x0,y0:坐标起点坐标
- xaxis，yaxis：x，y坐标参数
- xcalendar，ycalender：坐标时间参数的格式，默认是公历。
- x，y：设置坐标x，y轴的坐标数据











