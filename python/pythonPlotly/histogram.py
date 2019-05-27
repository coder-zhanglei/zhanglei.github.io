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
