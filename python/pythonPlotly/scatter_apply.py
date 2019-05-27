#-*- coding: utf-8 _*_
#散点和线图的应用案例

import pandas as pd
import plotly as py
import plotly.graph_objs as pygo

#-----------pre def
pd.set_option('display.width', 450)
pyplt = py.offline.plot

#-----------code
df = pd.read_csv('./scatter_apply.csv')
df9 = df[:10]
print(df9['温度'])


