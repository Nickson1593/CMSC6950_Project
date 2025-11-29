import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

# Load data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish X, Y, Z Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]
coordinates = data[:, :2]

#Create X, Y Mesh
x = np.linspace(X.min(), X.max(), 50)
y = np.linspace(Y.min(), Y.max(), 50)
X1, Y1 = np.meshgrid(x, y)

#Apply Z-Values to XY Mesh
Z1 = griddata(coordinates, Z, (X1, Y1), method='linear')

#Apply Gaussian Filter to Smooth Z1
smoothed_Z1 = gaussian_filter(Z1, sigma=0.2)

#Define Tick Values
xtick_values = [400000, 500000, 600000, 700000, 800000, 900000, 1000000]
xtick_text = ['400000', '500000', '600000', '700000', '800000', '900000', '1000000']

ytick_values = [5100000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000, 5800000]
ytick_text = ['5100000', '5200000', '5300000', '5400000', '5500000', '5600000', '5700000', '5800000']

ztick_values = [14000, 10000, 6000, 2000]
ztick_values_colorbar = [14000, 12000, 10000, 8000, 6000, 4000, 2000]
ztick_text = [ '14000', '10000', '6000', '2000']
ztick_text_colorbar = ['14000', '12000', '10000', '8000', '6000', '4000', '2000']

#Create 3D Surface Using Plotly
fig = go.Figure(data=[go.Surface(x=X1, y=Y1, z=smoothed_Z1,colorscale='Spectral', colorbar=dict(tickvals=ztick_values_colorbar, ticktext=ztick_text_colorbar,title_side='right', title=dict(text='Crustal Thickness (msec)', font=dict(size=20)),tickfont=dict(size=16)), contours = {"z":{"show": True, "start": 0, "end": 15848, "size": 1500}})])

#Update the 3D Surface Layout 
fig.update_layout(scene=dict(xaxis=dict(tickmode='array', tickvals=xtick_values, ticktext=xtick_text, title=dict(text='Easting (m)', font=dict(size=18)), range=[420000, 995000], tickfont=dict(size=13)),
                  yaxis=dict(tickmode='array', tickvals=ytick_values, ticktext=ytick_text, title=dict(text='Northing (m)', font=dict(size=18)), range=[5100000, 5800000], tickfont=dict(size=13)),zaxis=dict(tickmode='array', tickvals=ztick_values, ticktext=ztick_text, title=dict(text='Thickness (msec)', font=dict(size=18)), range=[0,16000], tickfont=dict(size=13))), width=1000, height=800)

                  
#Update the Aspect Ratio
fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=3,y=3,z=1)))

#Set Camera Projection
fig.update_layout(autosize=True, scene_camera_eye=dict(x=-1.8, y=-3, z=5))

#Show Figure
fig.show()


