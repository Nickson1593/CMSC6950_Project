import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata

# Set fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=15)

# Load data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish X, Y, Z Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

#Create X, Y Mesh
x = np.linspace(X.min(), X.max(), 50)
y = np.linspace(Y.min(), Y.max(), 50)
X1, Y1 = np.meshgrid(x, y)

#Apply Z-Values to XY Mesh
Z1 = griddata(coordinates, Z, (X1, Y1), method='cubic')

#Create 3D Surface Using Plotly
fig = go.Figure(data=[go.Surface(x=X1, y=Y1, z=Z1,colorscale='hot')])

#Update the 3D Surface Layout
fig.update_layout(scene=dict(xaxis_title='Easting (m)', 
		  yaxis_title='Northing (m)'), 
                  width=1200, height=1000)
                  

