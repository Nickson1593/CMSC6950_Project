import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

#Load Data File
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish XYZ Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

#Create a Mesh Grid 
x = np.linspace(X.min(), X.max(), 500)
y = np.linspace(Y.min(), Y.max(), 500)
X1, Y1 = np.meshgrid(x, y)

#Interpolate Z Values
Z1 = griddata((X, Y), Z, (X1,Y1), method = 'linear')

#Create Scatter Plot
plt.figure(figsize=(10,8))
scatter = plt.scatter(X1, Y1, c = Z1, cmap = 'Spectral', s = 10, edgecolor = 'None')

#Colorbar Parameters
cbar = plt.colorbar(scatter, label = 'Crustal Thickness (msec)')
cbar.set_label('Crustal Thickness (msec)', fontsize = 16)
cbar.ax.tick_params(labelsize = 12)

#Create Surface Contours
contour = plt.contour(X1, Y1, Z1, levels = 10, colors = 'black', linestyles = 'solid', linewidths = 0.8)

#Set Plot Paramaters
plt.tick_params(axis = 'x', labelsize = 12)
plt.tick_params(axis = 'y', labelsize = 12)
plt.ticklabel_format(style = 'plain', axis = 'x')
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.xlabel('Easting (m)', fontsize = 16)
plt.ylabel('Northing (m)', fontsize = 16)

#Plot Format
plt.margins(x = 0, y = 0)
plt.tight_layout()
plt.show()
