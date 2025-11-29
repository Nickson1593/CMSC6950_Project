import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.path import Path

#Load Crustal Thickness data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish XY Coordinates
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

#Make Copy of Masked Crustal Thickness Data to Apply Thickness Mask
Rift_masks = data_clean.copy()

#Establish Z Values from Rift_masks
Z_mask = Rift_masks[:, 2]

#Create Crustral Thickness Mask for Z Values Above 2800 msec
threshold = 2800
Rifts_mask_2800 = Z_mask > threshold
Rift_masks[Rifts_mask_2800, 2] = np.nan
df_mask = pd.DataFrame(Rift_masks)

#Remove NaN Values Set by Crustal Thickness Mask
df_2800 = df_mask.dropna()

#Save & Load New Masked XYZ File 
df_2800.to_csv('Rift_Mask_2800.csv', index=False)
Rifts_2800 = np.loadtxt('Rift_Mask_2800.txt')

#Establish New XYZ Variables for Rift_Mask_2800.txt
X_2800 = Rifts_2800[:, 0]
Y_2800 = Rifts_2800[:, 1]
Z_2800 = Rifts_2800[:, 2]

xtick_values = [400000, 500000, 600000, 700000, 800000, 900000, 1000000]
xtick_text = ['400000', '500000', '600000', '700000', '800000', '900000', '1000000']

ytick_values = [5100000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000, 5800000]
ytick_text = ['5100000', '5200000', '5300000', '5400000', '5500000', '5600000', '5700000', '5800000']

ztick_values = [3000, 2000, 1000, 0]
ztick_values_colorbar = [3000, 2500, 2000, 1500, 1000, 500]
ztick_text = [ '3000', '2000', '1000', '0']
ztick_text_colorbar = [ '3000', '2500', '2000', '1500', '1000', '500']

#Plot 3D Crustal Thickness Data Below 2800 msec (go.Scatter3d)
fig = go.Figure(data=[go.Scatter3d(x=X_2800, y=Y_2800, z=Z_2800, mode='markers', marker=dict(size=1, color=Z_2800, colorscale='Spectral', colorbar=dict(tickvals=ztick_values_colorbar, ticktext=ztick_text_colorbar,title_side='right', title=dict(text='Crustal Thickness Below 2800 msec', font=dict(size=20)),tickfont=dict(size=16))))])

#Format Layout
fig.update_layout(scene = dict(xaxis = dict(tickmode = 'array', tickvals = xtick_values, ticktext = xtick_text, title = dict(text = 'Easting (m)', font = dict(size = 18)), range = [420000, 995000], tickfont = dict(size = 13)), yaxis = dict(tickmode = 'array', tickvals = ytick_values, ticktext = ytick_text, title = dict(text = 'Northing (m)', font = dict(size = 18)), range = [5180000, 5750000], tickfont = dict(size = 13)), zaxis = dict(tickmode = 'array', tickvals = ztick_values, ticktext = ztick_text, title = dict(text = 'Thickness (msec)', font = dict(size = 18)), range = [0, 3000], tickfont = dict(size = 13))), width = 1000, height = 800)

#Update the Aspect Ratio
fig.update_layout(scene = dict(aspectmode = 'manual', aspectratio = dict(x = 3, y = 3, z = 1)))

#Set Camera Projection
fig.update_layout(autosize = True, scene_camera_eye = dict(x = -1.8, y = -3, z = 5))

#Show Figure
fig.show()
