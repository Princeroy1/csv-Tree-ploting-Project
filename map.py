# pip install pyproj
# https://pypi.org/project/pyproj/
from pyproj import Proj

# pip install pandas
# import pandas for reading csv file
import pandas as pd

# pip install plotly
import plotly.express as px
# read file
data=pd.read_csv('my.csv')

# we have data in utm it is lib to convert utm data into lat long after then we will get lat lon
myProj=Proj('+proj=utm +zone=33 +north +east +ellps=WGS84',preserve_units=False)

# save lat lon in our csv file
data['long'],data['lat']=myProj(data['X'].values,data['Y'].values,inverse=True)

# now we have lat lon in our csv file
# print(data)

# scattermapbox python lib for map our lat long 
# for more doc 
# https://plotly.com/python/scattermapbox/
fig=px.scatter_mapbox(data,
                      lon=data['long'],
                      lat=data['lat'],
                      zoom=3,
                      color=data['TreeName'],
                      size=data['Volume_2017'],
                      width=1200,
                      height=900,
                      title='Tree'
                      )
# update map to streetmap
fig.update_layout(mapbox_style="open-street-map")
fig.show()
