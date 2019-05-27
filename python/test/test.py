#utf-8

import os
import requests
import plotly as py
import pandas as pd
import plotly.graph_objs as pygo
from plotly.graph_objs import *

print (os.getcwd()   )
trace0 = pygo.Scatter(
    x = [1,2,3,4],
    y = [10,15,13,17]
)

trace1 = pygo.Scatter(
    x = [1,2,3,4],
    y = [16,5,11,9]
)

#data = pygo.Data([trace0,trace1])
data = Data([trace0,trace1])

#py.offline.plot(data,filename = os.getcwd() + 'first_start_introduction.html')

#py.offline.plot(data)
#py.offline.plot(data,filename = os.getcwd() + 'first_start_introduction.html',image='png')

py.plot(data,filename = os.getcwd() + 'first_start_introduction')

print ("fsadfasf"    )

