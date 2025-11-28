import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt', sep='\s+', names=['X','Y','Z'])

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Compute Meaningful Statistics
mean_crustal_thickness = np.mean(Crustal_Thickness)
median_crustal_thickness = np.median(Crustal_Thickness)
std_dev_crustal_thickness= np.std(Crustal_Thickness)


