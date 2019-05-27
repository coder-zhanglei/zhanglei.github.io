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
