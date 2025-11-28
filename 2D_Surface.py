import numpy as np
import matplotlib.pyplot as plt

#Load Data File
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish XYZ Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

#Create Scatter Plot
plt.figure()
scatter = plt.scatter(X, Y, c=Z, cmap='Spectral', s=10, edgecolors='none')
 
#Set Plot Paramaters
plt.colorbar(scatter, label='Crustal Thickness (msec two-way travel time (TWT))')
plt.xlabel('Easting', fontsize=14)
plt.ylabel('Northing', fontsize=14)
plt.title('Crustal Thickness Map of the Orphan Basin', fonsize=22)
plt.show()
