import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter
import pandas as pd
from matplotlib.path import Path

#Load Crustal Thickness data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish Crustal Thickness X, Y, Z Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]
coordinates = data[:, :2]

#Load Study Area Boundary data from file
data_B = np.loadtxt('basement_boundary_points.txt')

#Estbalish Boundary X, Y Points
boundary_points = data_B[:, :2]

#Create Study Area Boundary as a Path
boundary = Path(boundary_points)

#Identify Crustal Thickness XY Points Within the Boundary
is_inside = boundary.contains_points(coordinates)

#Make Copy of Crustal Thickness Data To Apply Mask
masked_data = data.copy()

#Apply Mask to Crustal Thickness Data (Make XY Points Outside of the Boundary = NaN)
masked_data[~is_inside] = np.nan

#Use Pandas to Create a Data Frame and Delete Values = NaN
df = pd.DataFrame(masked_data)
df_cleaned = df.dropna()

#Save & Load New XYZ File 
df_cleaned.to_csv('cleaned_XYZ.csv', index=False)
data_clean = np.loadtxt('Crustal_Thickness_With_Boundary_XYZ.txt')

#Establish Masked Crustal Thickness XYZ Variables
X_clean = data_clean[:, 0]
Y_clean = data_clean[:, 1]
Z_clean = data_clean[:, 2]
coordinates_clean = data_clean[:, :2]

#Create Masked Mesh Grid
x = np.linspace(X_clean.min(), X_clean.max(), 100)
y = np.linspace(Y_clean.min(), Y_clean.max(), 100)
X1, Y1 = np.meshgrid(x, y)

#Use scipy.interpolate (griddata) to Interpolate Masked XYZ Data
Z1_clean = griddata(coordinates_clean, Z_clean, (X1, Y1), method = 'linear')

#Smooth Interpolation
smoothed_Z1_clean = gaussian_filter(Z1_clean, sigma = 0.2)

#Define Tick Values
xtick_values = [400000, 500000, 600000, 700000, 800000, 900000, 1000000]
xtick_text = ['400000', '500000', '600000', '700000', '800000', '900000', '1000000']

ytick_values = [5100000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000, 5800000]
ytick_text = ['5100000', '5200000', '5300000', '5400000', '5500000', '5600000', '5700000', '5800000']

ztick_values = [10000, 8000, 6000, 4000, 2000, 0]
ztick_text = ['10000', '8000', '6000', '4000', '2000', '0']

#Create 3D Surface Using Plotly
fig = go.Figure(data = [go.Surface(x = X1, y = Y1, z = smoothed_Z1_clean, colorscale = 'Spectral', colorbar = dict(tickvals = ztick_values, ticktext = ztick_text, title_side = 'right', title = dict(text = 'Crustal Thickness (msec)', font = dict(size = 20)),tickfont = dict(size = 16)), contours = {"z" : {"show" : True, "start" : 0, "end" : 11000, "size" : 1500}})])

#Update the 3D Surface Layout 
fig.update_layout(scene = dict(xaxis = dict(tickmode = 'array', tickvals = xtick_values, ticktext = xtick_text, title = dict(text = 'Easting (m)', font = dict(size = 18)), range = [420000, 995000], tickfont = dict(size = 13)), yaxis = dict(tickmode = 'array', tickvals = ytick_values, ticktext = ytick_text, title = dict(text = 'Northing (m)', font = dict(size = 18)), range = [5180000, 5750000], tickfont = dict(size = 13)), zaxis = dict(tickmode = 'array', tickvals = ztick_values, ticktext = ztick_text, title = dict(text = 'Thickness (msec)', font = dict(size = 18)), range = [0, 11000], tickfont = dict(size = 13))), width = 1000, height = 800)
                  
#Update the Aspect Ratio
fig.update_layout(scene = dict(aspectmode = 'manual', aspectratio = dict(x = 3, y = 3, z = 1)))

#Set Camera Projection
fig.update_layout(autosize = True, scene_camera_eye = dict(x = -1.8, y = -3, z = 5))

#Show Figure
fig.show()
