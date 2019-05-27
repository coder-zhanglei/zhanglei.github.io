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
