#Load Slope Function
%load Slope_Function.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Define Variables Using Slope Function
X,Y,Z,Slope = surface_slope('Crustal_Thickness_With_Boundary_XYZ.txt')

#Make Subplots
fig = make_subplots(rows=2, cols=1,specs=[[{'type':'surface'}],[{'type':'surface'}]], subplot_titles=[('Aspect Ratio 2:2:0.75'),('Aspect Ratio 2:2:0.001')], horizontal_spacing=0.01, vertical_spacing=0.05)

#Create 3D Surface
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=Slope, colorscale='Picnic', colorbar=dict(title='Slope')), row=1, col=1)

#Update 3D Surface Layout
fig.update_layout(scene1=dict(xaxis=dict(title='Easting (m)', range=[420000, 995000]),
                  yaxis=dict(title='Northing (m)', range=[5100000, 5800000]),zaxis=dict(title='Thickness (msec)', range=[0,12000])), width=1000, height=1000)
fig.update_layout(scene1=dict(aspectmode='manual', aspectratio=dict(x=2,y=2,z=0.75)))

#Create 'Flat' 3D Surface (Z: Aspectratio = 0.001)
fig.add_trace(go.Surface(x=X, y=Y, z=Z, surfacecolor=Slope, colorscale='Picnic', colorbar=dict(title='Slope')), row=2, col=1)

#Update 'Flat' 3D Surface Layout
fig.update_layout(scene2=dict(xaxis=dict(title='Easting (m)', range=[420000, 995000]),
                  yaxis=dict(title='Northing (m)', range=[5100000, 5800000]),zaxis=dict(title='Thickness (msec)', range=[0,12000])), width=1000, height=1000)
fig.update_layout(scene2=dict(aspectmode='manual', aspectratio=dict(x=2,y=2,z=0.001)))

#Show Figure
fig.show()
