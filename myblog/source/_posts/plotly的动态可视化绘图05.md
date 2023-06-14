---
title: plotly的动态可视化绘图05
date: 2019-05-27 14:50:10
tags: 
    - plotly基础图形
categories: 
    - Python数据分析
---

## 面积图
  面积图就是在曲线的下方有所填充。
  
```python
import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot
s1 = np.random.RandomState(8) #定义局部种子
s2 = np.random.RandomState(9) #定义局部

rd1 = s1.rand(100)/10 - 0.02
rd2 = s1.rand(100)/10 -0.002

initial1 = 100000
initial2 = 100000

total1 = []
total2 = []

for i in range(len(rd1)):
    initial1 = initial1*rd1[i] +initial1
    initial2 = initial2*rd2[i] + initial2
    total1.append(initial1)
    total2.append(initial2)
    
trace1 = go.Scatter(
    y = total1,
    fill = None,
    mode = 'lines', #none 无边界线
    name = "策略1"
)
trace2 = go.Scatter(
    y = total2,
    fill = 'tonexty',
    mode = 'lines', #none 无边界线
    name = "策略2"
)

data = [trace1, trace2]
layout = dict(
    title = '策略净值曲线',
    xaxis = dict(title = '交易天数'),
    yaxis = dict(title = '净值'),
)

fig = dict(data = data, layout =layout)
pyplt(fig,filename='basic_areal.html')

```
主要参数：fill，第一条线没有填充，None，第二条线的填充为tonexty.

## 直方图
  用plotly绘制直方图用到graph_objs包中的Histogram函数。将数据赋值给函数中的变量x，即x=data，就可绘制直方图，若将数据赋值给y，则绘制水平直方图。histnorm是Histogram函数的
另一个属性。用Numpy生成随机数。
```python 
 import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot

s1 = np.random.RandomState(1)
x = s1.randn(1000)
data = [go.Histogram(
    x=x,
    histnorm = 'probability'
)]


pyplt(data,filename="basic_histogrm.html")

```
### 重叠直方图
  将layout中设置barmode属性，将其改为‘overlay’,
```python
    layout = go.Layout(barmode = 'overlay')
```

### 层叠直方图
    将layout中设置barmode属性，将其改为‘stack’,
```python
    layout = go.Layout(barmode = 'stack')
```
### 累计直方图
  累计直方图是直方图的累积形式，即第n+1个区间的展示数目是第N-1个区间的展示数目与第n个区间中实际样本数目之和，
通过设置Histogram函数中的cumulative属性实现，即cumulative = dict(enable = True)
```python
    trace1 = [go.Histogram(
        x = x1
        cumulative = dict(enable=True)
        )]
```
#### 直方图参数解读
- histnorm:设置纵坐标显示格式，可选的参数有“”，percent，probability，density
- histfunc：指定分组函数，可选的参数有count，sum，avg，min，max
- orientation：设置图形放向，有v和h两个参数，v表示垂直，h表示水平
- cumulative：累计直方图参数，有enableed，directio和currentbin三个关键字。
- autobinx：布尔型，是否自动划分区间
- nbinsx：整形，最大显示区间数目
- xbins：设置划分区间属性

## 饼图
  Pie函数可绘制饼图
```python
import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot

labels = ['股票','债券','现金','衍生品','其他']
values = [33.7, 20.33, 9.9, 8.6, 27.47]

trace = [go.Pie(labels = labels,
                values=values)  ]
layout = go.Layout(
    title = '基金资产配置比例图',
)

fig = go.Figure(data = trace, layout = layout)
pyplt(fig,filename='basic_pie_chart.html')

```
## 环形饼图
  绘制环形饼图，只需要在Pie函数中设置控制环形中心空白大小的hole属性即可实现。Pie函数中的hoverinfo属性用于控制当用户将鼠标指针放到环形
图上显示的内容，设置为“label+percent”表示显示标签加数据所占的比例。
```python
    trace = go.Pie(
        labels = labels,
        values = values,
        hole = 0.7,
        hoverinfo = "label+percent")]
    )
```




