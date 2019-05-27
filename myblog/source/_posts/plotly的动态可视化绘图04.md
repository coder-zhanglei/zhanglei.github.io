---
title: plotly的动态可视化绘图04
date: 2019-05-26 20:10:33
tags: 
    - plotly基础图形
categories: 
    - Python数据分析
---
## 柱状图
示例代码：
```python

import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

#Trace
trace_basic = [go.Bar(
                x = ['Variable_1','Variable_2','Variable_3','Variable_4','Variable_5'],
                y = [1,2,3,2,4],
)]#画柱状图

#Layout
layout_basic = go.Layout(
    title = 'The Graph Title',
    xaxis = go.XAxis(range = [-0.5,4.5], domain = [0,1])
)
#Figure
figure_basic = go.Figure(data = trace_basic, layout = layout_basic)
# Plot
pyplt(figure_basic,filename='Basic_BarChart.html')

```
  代码go.Bar是画柱状图的函数，x是柱状图的名称，y是柱状图的值，layout是布局，range = [-0.5,4.5]代表y值的大小，大于-0.5，小于5；domain默认为[0,1]
  
### 柱状簇
   将多个同类型的柱状图的数据叠加在一起即为柱状簇。

```python
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

#Trace
trace0 = go.Bar(
                x = ["上海物贸","广东明珠","五矿发展"],
                y = [4.12, 5.32, 0.60],
                name = "201609"
)

trace1 = go.Bar(
                x = ["上海物贸","广东明珠","五矿发展"],
                y = [3.65, 6.14, 0.58],
                name = "201612"
)

trace2 = go.Bar(
                x = ["上海物贸","广东明珠","五矿发展"],
                y = [2.15, 1.35, 0.19],
                name = "201703"
)

trace = [trace0,trace1,trace2]

#Layout
layout_basic = go.Layout(
    title = '国际贸易板块净资产收益率对比',
    #xaxis = go.XAxis(range = [-0.5,5])
)
#Figure
figure_basic = go.Figure(data = trace, layout = layout_basic)
# Plot
pyplt(figure_basic,filename='Basic_BarChart.html')

```

### 瀑布式柱状图

![效果图](https://i.imgur.com/g3VAMEG.jpg)

悬浮的式效果
```python

import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

x_data = ['流动负债','非流动负债','负债','所有者权益','总资产']
y_data = [56000000, 65000000,65000000,81000000,81000000]
text = ['57,999,848万元','8,899,916万元','66,899,764万元','16,167,657万元','83,067,421万元']

#Base
trace0 = go.Bar(
    x = x_data,
    y = [0,57999848,0,66899764,0],
    marker = dict(
        color = 'rgb(255,255,255)',
    )
)


#Trace
trace1 = go.Bar(
    x=x_data,
    y=[57999848, 889916, 66899764, 16167657, 83067421],
    marker=dict(
        color='rgb(55,128,191,0.7)',
        line = dict(
            color = 'rgba(55,128,191,1.0)',
            width = 2,
        )
    )
    
)

data = [trace0,trace1]
layout = go.Layout(
    title = '万科A资产负债结构图',
    barmode = 'stack',
    showlegend = False
)

annotations = []

for i in range(0,5):
    annotations.append(dict(x = x_data[i], y = y_data[i],text=text[i], font=dict(family='Arial', size = 14,
                                                                       color = 'rgb(245,246,249,1)'),
                                                                       showarrow = False))
    layout['annotations'] = annotations

#Figure
figure_basic = go.Figure(data = data, layout = layout)
# Plot
pyplt(figure_basic,filename='Basic_BarChart.html',image='png')

```
  trace0 中的y，表示第1,3,5根柱状图从0开始显示，第二根从57999848开始显示，第4根从66899764开始显示，将trace0所示的柱形设置为白色rgb(255,255,255)
 
### 图形样式设置
  样式的设置主要是marker变量的设置。

```python
    marker = dict(
        color = ['rgb....','rgb...']
        line = dict(
              color = 'rgb...',
              width = 2,
        )
        
    
    )
    
```

## 水平条图形
  水平条与柱状图类似，只需要在Bar函数中设置orientation=‘h’，x，y的数据交换。

```python
    go.Bar(
        x = [29.4, 34.62, 30.16],
        y = ['万科','国农','世纪']，
        orientation = 'h'
    )
    
```

 
 


