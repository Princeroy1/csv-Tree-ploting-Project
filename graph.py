# pip install plotly
# https://pypi.org/project/plotly/

import plotly.express as px
# Documentation for plotly python lib
# https://plotly.com/python/

import pandas as pd
# https://pypi.org/project/pandas/

# importing plotly for subgraph
from plotly.subplots import make_subplots 
# https://plotly.com/python/subplots/
import plotly.graph_objects as go

# read file with the help of pandas lib
data = pd.read_csv('my.csv')

# for subgraph define total row colum and type of plot scatter or pie we define 3 cols and 3 type of graph 2 scatter 1 pie
fig=make_subplots(rows=1,cols=3,specs=[[{"type":"Scatter"},{"type":"Scatter"},{"type":"pie"}]])

# for first graph  row nd col is 1,1
fig.add_trace(go.Scatter(x=data['TreeNo'],y=data['Height_2017'],mode='markers',name='height of tree') ,row=1,col=1)
# for 2nd graph row 1 col 2
fig.add_trace(go.Scatter(x=data['TreeNo'],y=data['DBH_2017'],mode='markers',name='Date of birth') ,row=1,col=2)
# for 3rd graph we define pie instead of scatter
fig.add_trace(go.Pie(labels=data['TreeName'],values=data['Volume_2017'],title='Volume of tree'),row=1,col=3)


# title for x axis for row 1 col 1
fig.update_xaxes(title_text='Number of Tree',row=1,col=1)
# title for x axis for row 1 col 2
fig.update_xaxes(title_text='Number of Tree',row=1,col=2)
# title for y axis for row 1 col 1
fig.update_yaxes(title_text='Height_2017',row=1,col=1)

# title for y axis for row 1 col 2
fig.update_yaxes(title_text='DBH_2017',row=1,col=2)
# for result call fig.show function
fig.show()

              
              
              
           