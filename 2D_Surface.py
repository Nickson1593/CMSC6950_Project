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
x = np.linspace(X.min(), X.max(), 100)
y = np.linspace(Y.min(), Y.max(), 100)
X1, Y1 = np.meshgrid(x, y)

#Interpolate Z Values
Z1 = griddata((X, Y), Z, (X1,Y1), method='linear')

#Create Scatter Plot
plt.figure(figsize=(10,8))
scatter = plt.scatter(X, Y, c=Z, cmap='Spectral', s=10, edgecolor='None')

#Create Surface Contours
contour = plt.contour(X1, Y1, Z1, levels=10, colors='black', linestyles='solid', linewidths=0.8)
plt.clabel(contour, inline=True, fontsize=10, fmt='%1.0f')

#Set Plot Paramaters
plt.colorbar(scatter, label='Crustal Thickness (msec two-way travel time (TWT))')
plt.ticklabel_format(style='plain', axis='x')
plt.xlabel('Easting', fontsize=14)
plt.ylabel('Northing', fontsize=14)
plt.title('Crustal Thickness Map of the Orphan Basin', fontsize=22)
plt.margins(x=0,y=0)
plt.tight_layout()
plt.show()
