import numpy as np
import matplotlib.pyplot as plt

#Load Data File
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish XYZ Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

#Create Scatter Plot
plt.figure(figsize=(10,8))
scatter = plt.scatter(X, Y, c=Z, cmap='Spectral', s=10, edgecolor='None')
 
#Set Plot Paramaters
plt.colorbar(scatter, label='Crustal Thickness (msec two-way travel time (TWT))')
plt.ticklabel_format(style='plain', axis='x')
plt.xlabel('Easting', fontsize=14)
plt.ylabel('Northing', fontsize=14)
plt.title('Crustal Thickness Map of the Orphan Basin', fontsize=22)
plt.margins(x=0,y=0)
plt.tight_layout()
plt.show()
