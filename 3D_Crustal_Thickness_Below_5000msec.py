import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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
data_clean = np.loadtxt('cleaned_XYZ.txt')

