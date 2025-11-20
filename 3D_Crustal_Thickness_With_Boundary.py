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



