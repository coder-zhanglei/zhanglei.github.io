import plotly as py
import plotly.graph_objs as go
import os
pyplt = py.offline.plot

import numpy as np

N = 100
random_x = np.linspace(0,1,N)
random_y = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

trace0 = go.Scatter(x = random_x,
                    y= random_y,
                    mode = 'markers',
                    name = 'markers'
                    )

trace1 = go.Scatter(x = random_x,
                    y= random_y1,
                    mode = 'lines+markers',
                    name = 'lines+markers'
                    )
trace2 = go.Scatter(x = random_x,
                    y= random_y2,
                    mode = 'lines',
                    name = 'lines'
                    )


data =  [trace0, trace1, trace2]
pyplt(data, filename= os.getcwd() + 'scatter_basic_demo.html')

