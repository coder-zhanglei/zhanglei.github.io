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

