---
title: plotly的动态可视化绘图03
date: 2019-05-25 14:48:57
tags: 
    - plotly基础图形
categories: 
    - Python数据分析
---

## 气泡图
1、 基本绘制方法
```python
import plotly as py
import plotly.graph_objs as go

#----pre def
pyplt =  py.offline.plot

#-------------code


trace0 = go.Scatter(
    x = [1,2,3,4],
    y = [10,11,12,13],
    mode = 'markers',
    marker = dict(
        size = [40,60,80,100],#定义每个点的大小
    )
    
)

data =  [trace0]
pyplt(data, filename="bubble_basice_demo.html")

```
2、 样式的设置
```python

trace0 = go.Scatter(
    x = [1,2,3,4],
    y = [10,11,12,13],
    mode = 'markers',
    text = ['A<br>size:40','B<br>size:60','C<br>size:80','D<br>size:100'],
    marker = dict(
        color = [120, 125, 130, 135],
        opacity = [1, 0.8, 0.6, 0.4],
        size = [40,60,80,100],
        showscale = True,
    )
    
)

```
 text指定每一个对应的悬浮文字（<br> 表示换行），color指定每个点的颜色，opacity指定每个点的透明度，size指定每个点的大小，showscale = Ture 表示显示右边的颜色条的大小。

3、 缩放设置
 调节气泡尺寸大小可以通过sizeref参数进行设置，当sizeref值大于1时，将减小气泡的大小，当小于1时，将增大气泡大小。
```python

trace0 = go.Scatter(
    x = [1,2,3,4],
    y = [10,11,12,13],
    mode = 'markers',
    name = 'default',
    text = ['A</br>size:40</br>default','B</br>size:60</br>default','C</br>size:80</br>default','D</br>size:100</br>default'],
    marker = dict(
        size = [400,600,800,1000],
        sizemode = 'area',
    )
    
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[14, 15, 16, 17],
    mode='markers',
    name='default',
    text=['A</br>size:40</br>sizeref:0.2', 'B</br>size:60</br>sizeref:0.2', 'C</br>size:80</br>sizeref:0.2',
          'D</br>size:100</br>sizeref:0.2'],
    marker=dict(
        size=[400, 600, 800, 1000],
        sizeref = 0.2,
        sizemode='area',
    )

)

trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[20, 21, 22, 23],
    mode='markers',
    name='default',
    text=['A</br>size:40</br>sizeref:2', 'B</br>size:60</br>sizeref:2', 'C</br>size:80</br>sizeref:2',
          'D</br>size:100</br>sizeref:2'],
    marker=dict(
        size=[400, 600, 800, 1000],
        sizeref = 2,
        sizemode='area',
    )

)

```
  sizeref=2表示将气泡大小设置为原来的1/2,；参数sizemode有diameter和area两个值，diameter表示按直径缩放，area表示按面积缩放

 参数解读 ：
详情参考：https://plot.ly/python/reference/#scatter-marker-sizeref
- text：列表，元素为相应节点的悬浮文字内容
- marker：数据节点参数，包括大小，颜色，格式等
    size：列表，元素为相应节点的悬浮文字内容
    sizeref：缩放比例，如设置为2，则缩小为原来的1/2
    sizemode：缩放的标准，默认以diameter（直径缩放），也可以area（面积缩放）。
    color：列表，元素为相应节点的颜色
    showscale：默认为FALSE，不显示右侧的颜色条，TRUE显示
    opacity：列表，元素为0~1之间的数，表示相应节点的透明度

## 线形图
1、 基本案例
```python
import plotly as py
import plotly.graph_objs as go
import pandas as pd
pyplt = py.offline.plot

profit_rate = [-0.001,-0.013,0.004,0.002,0.003,-0.001,-0.009,0.0,0.007,-0.005,0.0,0.001,-0.006,-0.006,-0.009,-0.013,0.005,0.007,0.004,-0.006,
-0.009,-0.004,0.015,0.007,0.001,0.003,-0.009,-0.005,0.001,-0.008,-0.016,0.002,-0.013,-0.009,-0.014,0.009,-0.003,0.002,-0.001,0.011,0.004]

date = pd.date_range(start = '3/1/2017', end = '4/30/2017')

trace = [go.Scatter(
    x =date,
    y = profit_rate
)]

layout = dict(
    title = '浦发银行20170301-20170428涨跌幅变化',
    xaxis =dict(title = 'Date'),
    yaxis = dict(title = 'profit_rate')
)

fig = dict(data = trace, layout = layout)
pyplt(fig, filename='basic-line.html')

```
### 数据缺口与连接
 数据集往往并不完美，可能有缺失的数据，在plotly中可以通过设置Scatter函数中的connectgaps属性来显示这些数据缺口或对缺口进行连接。
```python
import plotly as py
import plotly.graph_objs as go
import pandas as pd

pyplt = py.offline.plot

month = ['January', 'February','March','April','May','June','July','August','September','October','November','December'] #x轴坐标
high_2000 = [32.5,37.6,49.9,53.0,None,75.4,76.5,76.6,70.7,60.6,45.1,29.3]
low_2000 = [13.8,22.3,32.5,37.2,None,56.1,57.7,58.3,51.2,42.8,31.6,15.9]
high_2007 = [36.5,26.6,43.6,52.3,None,81.4,80.5,82.2,76.0,67.3,46.1,35.0]
low_2007 = [23.6,14.0,27.0,36.8,None,57.7,58.9,61.2,53.3,48.5,31.0,23.6]
high_2014 = [28.8,28.5,37.0,56.3,None,79.7,78.5,77.8,74.1,62.6,45.3,39.9]
low_2014 = [12.7,14.3,18.6,35.5,None,58.0,60.0,58.6,51.7,45.2,32.2,29.1]



trace0 = go.Scatter(
    x =month,
    y = high_2014,
    name = 'High 2014',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4
    ) ,
    connectgaps = True
    
)

trace1 = go.Scatter(
    x=month,
    y=low_2014,
    name='low_2014 2014',
    line=dict(
        color=('rgb(22, 96, 167)'),
        width=4
    ),
    connectgaps=False

)

trace2 = go.Scatter(
    x=month,
    y=high_2007,
    name='high_2007 ',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=4,
        dash = 'dash'    #虚线（断线），dot虚线（点），dashdot
    ),
    connectgaps=False

)

trace3 = go.Scatter(
    x=month,
    y=low_2007,
    name='low_2007',
    line=dict(
        color=('rgb(22, 96, 167)'),
        width=4,
        dash = 'dash'
    ),
    connectgaps=False

)
trace4 = go.Scatter(
    x=month,
    y=high_2000,
    name='high_2000',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=4,
        dash = 'dot'
    ),
    connectgaps=False

)

trace5 = go.Scatter(
    x=month,
    y=low_2000,
    name='low_2000',
    line=dict(
        color=('rgb(22, 96, 167)'),
        width=4,
        dash = 'dot'
    ),
    connectgaps=False

)

data = [trace0, trace1, trace2, trace3, trace4,trace5]

layout = dict(
    title = 'Average High and Low Temperatures in New York',
    xaxis =dict(title = 'Month'),
    yaxis = dict(title = 'Temperature(degrees F)')
)

fig = dict(data = data, layout = layout)
pyplt(fig, filename='styled-line.html')

```
 数据中缺失的数据设置为None。在Scatter函数中，设置connectgaps属性为False，表示不连接，显示接口，Ture表示为连接。Scatter函数中的line属性用于对线形图形的样式控制；
color控制颜色，width设置宽度；dash用于设置类型，dash表示有短线组成的虚线，dot表示由点组成的虚线，dashdot表示由点和短线组成的虚线。
### 数据插值 
  调整Scatter函数line属性中的shape值可以对插值的方法进行控制，完成数据点的插值设置。插值的方法就是根据已有的零散数据点，找到一条满足一定条件的曲线，使之经过全部的数据点。
plotly提供6种插值的方法。分别是‘linear’，‘spline’，‘hv’，‘vh’，‘hvh’，‘vhv’。如：shape：‘spline’
```python
trace5 = go.Scatter(
    x=month,
    y=low_2000,
    name='low_2000',
    line=dict(
        color=('rgb(22, 96, 167)'),
        width=4,
        shape = 'linear' #直线连接
        
    ),
    connectgaps=False

)

```
### 填充线形图
   要绘制恒宝股份在一段时间内的最高价与最低价，每条可见线对应股票的开盘价，线条的上影线对应当天的最高价，线条的下影线对应当天的最低价。
要绘制这样的图，先把其拆分为两部分，一部分是对3条可见线的绘制，另一部分是对三条填充线进行绘制。
```python
#完成了对三条填充线进行绘制
x = x + x_rev,#（x只给了10个数据）是从0到10，再从10到1的逆序
y = y1_upper+y1_lower, # 从第一天的最高价到第10天的最高价，再从第10天到第1天的最高价的序列
fill = 'tozerox',
fillcolor = 'raba(0,0,205,0.2)',
line = go.Line(color = 'transparent')#color属性为 'transparent'，对线条进行隐藏
#其中y1_lower = y1_lower[ : : -1] 逆序，x_rev = x[::-1]

#设置数据轨迹
trace1  = go.Scatter(
    x = x + x_rev,#（x只给了10个数据）是从0到10，再从10到1的逆序
    y = y1_upper+y1_lower, # 从第一天的最高价到第10天的最高价，再从第10天到第1天的最高价的序列
    fill = 'tozerox',
    fillcolor = 'raba(0,0,205,0.2)',
    line = go.Line(color = 'transparent')#color属性为 'transparent'，对线条进行隐藏
    showlegend = False,#布尔变量，用于切换图标显示
    name = '恒宝股份'

)
trace2  = go.Scatter(
    x = x,
    y = y1,
    line = go.Line(color = 'reb(0,0,205)')
    mode = 'line',
    name = '恒宝股份'

)
#布局
layout = go.Layout(
    paper_bgcolor = 'rgb(255,255,255)',
    plot_bgcolor = 'rgb(229,229,229)',
    xaxis = go.XAxis(
            gridcolor = 'rgb(255,255,255)',
            range = [1,10],
            showgrid = Ture,
            showline = False,
            showticklabels = TRUE,
            tickcolor = 'rgb(127,127,127)',
            ticks = 'outside',
            zeroline = False
        ),
    yaxis = go.YAxis(
        gridcolor = 'rgb(255,255,255)',
        showgrid = Ture,
        showline = False,
        showticklabels = TRUE,#显示坐标标记
        tickcolor = 'rgb(127,127,127)',
        ticks = 'outside',
        zeroline = False

    )

)
 
```
    
   
   

