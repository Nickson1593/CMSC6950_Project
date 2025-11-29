#Load Slope Function
%load Slope_Function.py

import plotly.graph_objects as go

xtick_values = [400000, 500000, 600000, 700000, 800000, 900000, 1000000]
xtick_text = ['400000', '500000', '600000', '700000', '800000', '900000', '1000000']

ytick_values = [5100000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000, 5800000]
ytick_text = ['5100000', '5200000', '5300000', '5400000', '5500000', '5600000', '5700000', '5800000']

#Define Variables Using Slope Function
X,Y,Z,Slope = surface_slope('Crustal_Thickness_With_Boundary_XYZ.txt')

#Create 3D Surface
fig = go.Figure(data = [go.Surface(x = X, y = Y, z = Z, surfacecolor = Slope, colorscale = 'Picnic', colorbar = dict( title_side = 'right', title = dict(text = 'Slope', font = dict(size = 20)),tickfont = dict(size = 16)))])

#Update 3D Surface Layout
fig.update_layout(scene = dict(xaxis = dict(tickmode = 'array', tickvals = xtick_values, ticktext = xtick_text, title = dict(text = 'Easting (m)', font = dict(size = 18)), range = [420000, 995000], tickfont = dict(size = 13)), yaxis = dict(tickmode = 'array', tickvals = ytick_values, ticktext = ytick_text, title = dict(text = 'Northing (m)', font = dict(size = 18)), range = [5180000, 5750000], tickfont = dict(size = 13)), zaxis = dict(zaxis=dict(title='', showticklabels=False)), width = 1000, height = 800)

#Set Aspect Ratio
fig.update_layout(scene = dict(aspectmode = 'manual', aspectratio = dict(x = 3, y = 3, z = 0.001)))

#Set Camera Projection
fig.update_layout(autosize = True, scene_camera_eye = dict(x = -2.6, y = -3, z = 3))

#Show Figure
fig.show()
