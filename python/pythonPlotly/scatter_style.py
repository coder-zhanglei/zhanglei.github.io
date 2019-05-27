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


data = [trace0]

layout = dict(
    title = 'Styled Scatter',
    yaxis = dict(zeroline = True),
    xaxis = dict(zeroline = False)
)

fig = dict(data=data, layout = layout)
pyplt(fig, filename='scatter_basic_demo.html')
