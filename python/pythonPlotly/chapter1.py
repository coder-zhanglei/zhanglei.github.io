import plotly as py
from plotly.graph_objs import Scatter, Layout, Data

#py.offline.init_notebook_mode()     #该条语句是在Jupyter Notebook（此前被称为 IPython notebook）中绘图
trace0 = Scatter(
    x = [1,2,3,4,],
    y = [10,15,12,17]
)
trace1 = Scatter(
    x = [1,2,3,4,],
    y = [16,5,11,9]
)

data = Data([trace0, trace1])
data1 = Data(trace1)

#py.offline.iplot(data, filename='first_offline_start') IPlot是在Notebook中绘图的函数
py.offline.plot(data1, filename='first_offline_start')
