import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter
import pandas as pd

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
data_clean = np.loadtxt('cleaned_XYZ.txt')

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
Z1_clean = griddata(coordinates_clean, Z_clean, (X1, Y1), method='cubic')

#Smooth Interpolation
smoothed_Z1_clean = gaussian_filter(Z1_clean, sigma=0.2)

#Create 3D Surface Using Plotly
fig = go.Figure(data=[go.Surface(x=X1, y=Y1, z=smoothed_Z1_clean,colorscale='spectral', colorbar=dict(title='Crustal Thickness (msec)'), contours={"z":{"show":True}})])])

#Update the 3D Surface Layout 
fig.update_layout(scene=dict(xaxis=dict(title='Easting (m)', range=[420000, 995000]),
                  yaxis=dict(title='Northing (m)', range=[5100000, 5800000]),
                  zaxis=dict(title='Thickness (msec)', range=[0,15850])), 
                  width=1000, height=800)
                  
#Update the Aspect Ratio
fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=2,y=2,z=0.75)))

#Show Figure
fig.show()



