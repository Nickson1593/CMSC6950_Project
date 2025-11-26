import numpy as np
import matplotlib.pyplot as plt

#Load Data File
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish XYZ Variables
X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]

 
